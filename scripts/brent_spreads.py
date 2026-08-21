#!/usr/bin/env python3
"""
Brent Crude Call Spread Analyzer

Always shows two tables:
  1. $120/$200 spread compared across all expiry dates
  2. All strikes ($120/$130/$140/$150) compared for the Jan 2027 contract

Data is cached per contract in scripts/.cache/ for 1 hour.
Only opens a browser for contracts that need fresh data.

Usage:
    .venv/bin/python scripts/brent_spreads.py           # use cache if fresh
    .venv/bin/python scripts/brent_spreads.py --refresh  # force fresh fetch
"""

import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from tabulate import tabulate
from playwright.sync_api import sync_playwright

# ── Config ─────────────────────────────────────────────────────────────────────

UPPER_STRIKE  = 200.0
LOWER_STRIKES = [120.0, 130.0, 140.0, 150.0]
FIXED_LOWER   = 120.0
SCENARIOS     = [115, 120, 125, 130, 135, 140, 145, 150, 160, 175, 200, 220]
CACHE_TTL     = 3600   # seconds (1 hour)
CACHE_DIR     = Path(__file__).parent / ".cache"
USER_AGENT    = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# (label, Barchart symbol, URL slug, approx option expiry)
# Brent options expire ~2 months before the delivery month.
EXPIRY_CONTRACTS = [
    ("Aug 2026", "CBQ26", "aug-26", "~Jun 18 2026"),
    ("Sep 2026", "CBU26", "sep-26", "~Jul 16 2026"),
    ("Oct 2026", "CBV26", "oct-26", "~Aug 18 2026"),
    ("Nov 2026", "CBX26", "nov-26", "~Sep 17 2026"),
    ("Dec 2026", "CBZ26", "dec-26", "~Oct 15 2026"),
    ("Jan 2027", "CBF27", "jan-27", "Nov 25 2026"),
]

def barchart_url(symbol, slug):
    return (
        f"https://www.barchart.com/futures/quotes/{symbol}/options/{slug}"
        f"?futuresOptionsView=merged&moneyness=allRows"
    )

# ── Cache ──────────────────────────────────────────────────────────────────────

def cache_file(symbol):
    CACHE_DIR.mkdir(exist_ok=True)
    return CACHE_DIR / f"{symbol}.json"


def cache_load(symbol):
    """Return calls dict if cache exists and is < CACHE_TTL seconds old, else None."""
    path = cache_file(symbol)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    age  = time.time() - data.get("fetched_at", 0)
    if age >= CACHE_TTL:
        return None
    # JSON keys are strings; convert back to float
    return {float(k): tuple(v) for k, v in data["calls"].items()}


def cache_save(symbol, calls):
    path = cache_file(symbol)
    payload = {
        "fetched_at": time.time(),
        "calls": {str(k): list(v) for k, v in calls.items()},
    }
    path.write_text(json.dumps(payload))


def cache_age_str(symbol):
    path = cache_file(symbol)
    if not path.exists():
        return None
    age = time.time() - json.loads(path.read_text()).get("fetched_at", 0)
    if age < 60:
        return f"{int(age)}s ago"
    if age < 3600:
        return f"{int(age/60)}m ago"
    return f"{age/3600:.1f}h ago"

# ── Fetching ───────────────────────────────────────────────────────────────────

def midpoint(raw):
    bid  = raw.get("bidPrice")  or 0
    ask  = raw.get("askPrice")  or 0
    last = raw.get("lastPrice") or 0
    if bid > 0 and ask > 0 and ask > bid:
        return round((bid + ask) / 2, 4), "mid"
    if last > 0:
        return round(last, 4), "last"
    return None, None


def fetch_from_barchart(page, symbol, slug):
    """Fetch live options data for one contract. Returns {strike: (price, ptype)}."""
    captured = []

    def on_response(response):
        if "proxies/core-api/v1/quotes/get" in response.url:
            try:
                captured.append(json.loads(response.body()))
            except Exception:
                pass

    page.on("response", on_response)
    page.goto(barchart_url(symbol, slug), wait_until="load", timeout=60_000)
    page.wait_for_timeout(2_000)
    page.remove_listener("response", on_response)

    calls = {}
    for payload in captured:
        for item in payload.get("data", {}).get("Call", []):
            raw    = item.get("raw", {})
            strike = raw.get("strike")
            if strike is None:
                continue
            price, ptype = midpoint(raw)
            if price is not None:
                calls[float(strike)] = (price, ptype)

    if not calls:
        raise RuntimeError(f"No call data returned for {symbol}.")
    return calls


def load_all_contracts(force_refresh=False):
    """
    Return {symbol: calls_dict} for all contracts.
    Uses cache where fresh; opens browser only for stale/missing contracts.
    """
    results   = {}
    to_fetch  = []

    for label, symbol, slug, expiry_date in EXPIRY_CONTRACTS:
        if not force_refresh:
            cached = cache_load(symbol)
            if cached:
                age = cache_age_str(symbol)
                print(f"  {label} ({symbol}): cached ({age})")
                results[symbol] = cached
                continue
        to_fetch.append((label, symbol, slug, expiry_date))

    if to_fetch:
        print(f"  Fetching {len(to_fetch)} contract(s) from Barchart...")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(user_agent=USER_AGENT)
            page    = context.new_page()
            for label, symbol, slug, _ in to_fetch:
                print(f"    {label} ({symbol})...", end=" ", flush=True)
                try:
                    calls = fetch_from_barchart(page, symbol, slug)
                    cache_save(symbol, calls)
                    results[symbol] = calls
                    print(f"{len(calls)} strikes")
                except RuntimeError as e:
                    print(f"FAILED ({e})")
                    results[symbol] = None
            browser.close()

    return results

# ── Analysis helpers ───────────────────────────────────────────────────────────

def get_price(calls, strike, label=""):
    if strike not in calls:
        nearby = sorted(calls.keys(), key=lambda x: abs(x - strike))[:5]
        raise ValueError(
            f"Strike ${strike:.0f} not found{' (' + label + ')' if label else ''}. "
            f"Closest: {[f'${s:.0f}' for s in nearby]}"
        )
    price, ptype = calls[strike]
    if not price or price <= 0:
        raise ValueError(f"Strike ${strike:.0f} has no valid price.")
    return price, ptype


def spread_stats(lower_price, upper_price, lower_strike):
    net     = round(lower_price - upper_price, 4)
    width   = UPPER_STRIKE - lower_strike
    max_pay = round(width - net, 4)
    return dict(net=net, breakeven=round(lower_strike + net, 4),
                max_pay=max_pay, ratio=round(max_pay / net, 2))


def crossover_price(s1_lower, s1_cost, s2_lower, s2_cost):
    denom = s2_cost - s1_cost
    if abs(denom) < 1e-10:
        return None
    return (s2_cost * s1_lower - s1_cost * s2_lower) / denom


def scenario_return(price, lower, net):
    if price <= lower + net:
        return -1.0
    if price >= UPPER_STRIKE:
        return round((UPPER_STRIKE - lower - net) / net, 2)
    return round((price - lower - net) / net, 2)

# ── Table 1: expiries ──────────────────────────────────────────────────────────

def print_expiries_table(all_contracts):
    rows_summary  = []
    rows_scenario = []

    for label, symbol, slug, expiry_date in EXPIRY_CONTRACTS:
        calls = all_contracts.get(symbol)
        if calls is None:
            rows_summary.append([label, expiry_date, "—", "—", "—", "—", "—", "—", "—"])
            continue
        try:
            lp, lpt = get_price(calls, FIXED_LOWER, label)
            up, upt = get_price(calls, UPPER_STRIKE, label)
            s = spread_stats(lp, up, FIXED_LOWER)
            rows_summary.append([
                label, expiry_date,
                f"${lp:.2f} ({lpt})", f"${up:.2f}",
                f"${s['net']:.2f}", f"${s['breakeven']:.2f}",
                f"${s['max_pay']:.2f}", f"{s['ratio']:.1f}x",
                f"${s['net']*1000:,.0f}",
            ])
            rows_scenario.append((label, FIXED_LOWER, s["net"], s["ratio"]))
        except ValueError as e:
            rows_summary.append([label, expiry_date, f"err: {e}", "—", "—", "—", "—", "—", "—"])

    hdrs = ["Expiry", "Option exp.", "Buy $120", "Sell $200", "Net cost",
            "Breakeven", "Max payout", "Ratio", "$/contract"]
    print(f"\n{'═'*86}")
    print(f"  TABLE 1 — $120/$200 CALL SPREAD ACROSS EXPIRY DATES")
    print(f"  Source: Barchart  |  1 contract = 1,000 bbl")
    print(f"{'═'*86}")
    print(tabulate(rows_summary, headers=hdrs, tablefmt="simple"))

    valid = [(lb, lo, net, ratio) for lb, lo, net, ratio in rows_scenario if net > 0]
    if valid:
        print(f"\n{'─'*86}")
        print("  SCENARIO RETURNS BY EXPIRY (per $ invested  |  -1.0x = full loss)")
        print(f"{'─'*86}")
        s_rows = [[f"${p}"] + [f"{scenario_return(p, lo, net):.1f}x" for _, lo, net, _ in valid]
                  for p in SCENARIOS]
        print(tabulate(s_rows, headers=["Price"] + [lb for lb, *_ in valid], tablefmt="simple"))
        print(f"\n  Note: returns capped above $200")

# ── Table 2: strikes (Jan 2027) ────────────────────────────────────────────────

def print_strikes_table(all_contracts):
    label, symbol, slug, expiry_date = EXPIRY_CONTRACTS[-1]   # Jan 2027
    calls = all_contracts.get(symbol)
    if calls is None:
        print(f"\n  Table 2 unavailable — no data for {label}")
        return

    try:
        upper_price, upper_ptype = get_price(calls, UPPER_STRIKE)
    except ValueError as e:
        print(f"\n  Table 2 unavailable: {e}")
        return

    spreads = []
    for lower in LOWER_STRIKES:
        try:
            lp, lpt = get_price(calls, lower)
            s = spread_stats(lp, upper_price, lower)
            spreads.append(dict(lower=lower, buy_price=lp, buy_ptype=lpt, **s))
        except ValueError as e:
            print(f"  Skipping ${lower:.0f} strike: {e}")

    rows = [[
        f"${int(s['lower'])}/$200",
        f"${s['buy_price']:.2f} ({s['buy_ptype']})",
        f"${upper_price:.2f}",
        f"${s['net']:.2f}",
        f"${s['breakeven']:.2f}",
        f"${s['max_pay']:.2f}",
        f"{s['ratio']:.1f}x",
        f"${s['net']*1000:,.0f}",
    ] for s in spreads]
    hdrs = ["Spread", "Buy", "Sell ($200)", "Net cost", "Breakeven", "Max payout", "Ratio", "$/contract"]

    print(f"\n{'═'*76}")
    print(f"  TABLE 2 — ALL STRIKES, {label} CONTRACT (expires {expiry_date})")
    print(f"  Source: Barchart  |  1 contract = 1,000 bbl")
    print(f"{'═'*76}")
    print(tabulate(rows, headers=hdrs, tablefmt="simple"))

    # Crossovers
    print(f"\n{'─'*76}")
    print("  CROSSOVER PRICES")
    print(f"{'─'*76}")
    for i in range(len(spreads) - 1):
        s1, s2 = spreads[i], spreads[i + 1]
        cross = crossover_price(s1["lower"], s1["net"], s2["lower"], s2["net"])
        lo, hi = int(s1["lower"]), int(s2["lower"])
        if cross and cross <= UPPER_STRIKE:
            print(f"  ${lo}/$200 vs ${hi}/$200  →  ${cross:.2f}")
            print(f"      < ${cross:.2f}: ${lo}/$200 better  |  > ${cross:.2f}: ${hi}/$200 better")

    # Scenarios
    print(f"\n{'─'*76}")
    print("  SCENARIO RETURNS (per $ invested  |  -1.0x = full loss)")
    print(f"{'─'*76}")
    rows = [[f"${p}"] + [f"{scenario_return(p, s['lower'], s['net']):.1f}x" for s in spreads]
            for p in SCENARIOS]
    print(tabulate(rows, headers=["Price"] + [f"${int(s['lower'])}/$200" for s in spreads],
                   tablefmt="simple"))
    print(f"\n  Note: returns capped above $200")

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true",
                        help="Ignore cache and fetch fresh data from Barchart")
    args = parser.parse_args()

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Brent Crude Spread Analyzer  [{ts}]")
    print(f"Cache TTL: {CACHE_TTL//60} min  |  Cache dir: {CACHE_DIR}")
    if args.refresh:
        print("  --refresh flag set: ignoring cache")
    print()

    all_contracts = load_all_contracts(force_refresh=args.refresh)

    print_expiries_table(all_contracts)
    print_strikes_table(all_contracts)
    print()


if __name__ == "__main__":
    main()
