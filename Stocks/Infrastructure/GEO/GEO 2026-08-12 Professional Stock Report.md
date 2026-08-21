# The GEO Group (NYSE: GEO) — Professional Stock Report

**Date:** 2026-08-12 (model refreshed for formula-driven workbook)  
**Price / shares / BS:** edit live on `01_Inputs` in [[GEO Complete Investment Model]] (or the cloud sidecar [[GEO Complete Investment Model Inputs]])  
**Related:** [[GEO]] · [[GEO 2026-08-11 ICE RE NAV vs CoreCivic]] · [[GEO 2026-08-06 Q2 Earnings Call Notes]]

> **Where the numbers live:** All tables, forecasts, comps, SOTP, and segment multiples are in **[[GEO Complete Investment Model]]**. This note is the investment narrative and how to use the model — not a second copy of the spreadsheet.

---

## How to use the model

| Sheet | What to do |
| --- | --- |
| `01_Inputs` | **Only edit blue cells** — price, cash, debt, tax friction, beds, $/bed, growth rates, margins, segment multiples |
| `03_Segments` | Read FY26–29 segment Rev/NOI (formulas). **Multiples valuation at bottom** by segment |
| `04_IS_Fwd` | Consolidated P&L, EPS, FCF, implied P/E paths |
| `05_BS_Fwd` | Cash & debt bridge (**cash is explicit**; net debt = gross − cash) |
| `06_RE_NAV` | Bed × $/bed × net take; residual EBITDA after sale |
| `07_SOTP` | Four approaches — pick one; don’t double-count RE + owned-secure multiple |
| `08_CXW_Comps` | Trading + transaction comps (editable beds/prices) |
| `09_Scenarios` | Subjective probabilities → weighted $/sh |
| `00_Cover` | Live dashboard of key outputs |
| Cloud | Edit [[GEO Complete Investment Model Inputs]] then `.venv/bin/python scripts/xlsx_model.py apply` |

**Tax:** Federal statutory **21%** is on `01_Inputs!B27`. Sale friction uses **tax on gain** (`B32`, default 25%) + txn costs (`B31`) → net take `=1−B32−B31` (~71%). That matches CXW’s ~72% take-home; it is **not** “1 − 21% on the full sale price,” because tax applies to (price − basis) and GEO’s book basis is low.

**Cash:** Equity bridges use either `+Cash − Gross debt` (Approach A) or `− Net debt` (B/C, since net debt already nets cash). Do not add cash on top of net debt.

---

## 1. Investment conclusion

GEO is a **politically timed RE monetization story** inside a detention / EM operating company. Spot P/E on FY26 EPS *guide* is rich (~24×); EV/EBITDA ~10× is more sane. The stock works if ICE facility sales and/or a 2027 EBITDA ramp clear before the **2028 political window** closes.

Primary outputs (recalculate with `.venv/bin/python scripts/xlsx_model.py show` or Excel after edits):
- **Approach A** — segment multiples + cash − debt  
- **Approach B** — full ICE RE sale + residual EBITDA  
- **Approach C** — full RE NAV re-rate + asset-light residual  
- **Approach D** — “several” beds only  
- **Prob-weighted** — `09_Scenarios`

See `00_Cover` for live $/sh.

---

## 2. Business & segments

GEO owns/operates secure facilities, ICE processing, reentry, ISAP/EM, transport, and international managed prisons (~50.4k company-owned beds).

**Owned Secure ~29% NOI margin vs Managed Only ~17%** — that gap is ownership economics (~$5k NOI/bed/yr). CXW’s post-sale EBITDA guide cut implies ~$2.1k/bed/yr lost while keeping management — use the blend weight on `01_Inputs` to toggle between those views.

**EM (~49% NOI margin)** is the highest-quality segment and a partial hedge if detention is cut and ATD/ISAP is funded — with basis risk (ISAP was soft in 2024).

Deep segment build, growth rates, margins, unit economics, and **per-segment exit multiples** → sheet `03_Segments`.

---

## 3. History & calls (qualitative)

- **2024:** Refi extinguishment crushed GAAP NI; Adj. EBITDA is the clean lens. Capital return deferred until post-election visibility — buybacks followed in 2025–26.  
- **2025:** Lawton state sale ~$131k/bed (non-ICE anchor). GAAP NI includes sale gain.  
- **Feb 2026 guide** started at $490–510M Adj. EBITDA; **Aug raise to $550–560M** shows ICE ramp. Rivers/Big Horn (~$165M) and Florida managed-only (~$100M) sit **outside** 2026 guide.  
- **Mar 2026 presentation:** mgmt NAV $125k/$75k → ~$46/sh floor before CXW’s $307k ICE prints.  
- **CXW Jul–Aug 2026:** four facilities, ~$307k/bed, keep management — GEO’s template.  
- **GEO Q2’26:** “active process” for **several** turnkey sales — not a committed portfolio sale. Model “several” vs “full ICE” explicitly on `07_SOTP`.

Transcript notes: [[GEO 2026-08-06 Q2 Earnings Call Notes]] · [[GEO 2024-08-07 Q2 Earnings Call Notes]]

---

## 4. RE NAV vs ops multiples (don’t double-count)

| Approach | Idea | When to use |
| --- | --- | --- |
| A Segment multiples | Capitalize each segment’s NOI; +cash −debt | Holdco / no sale |
| B ICE sale + residual | Monetize ICE beds; residual still includes other owned RE | Near-term thesis |
| C Full RE MTM + AL residual | Mark all RE; strip ownership from EBITDA | Full NAV re-rate |
| D Several only | Matches management wording | Base path |

If you run **B or C**, cut Owned Secure’s ops multiple toward management-fee-only on `01_Inputs` (rows 105–110) so you don’t count the buildings twice.

Idle @ CXW pricing is upside, not base (`06_RE_NAV` + idle beds on inputs).

---

## 5. P/E and the 2028 window

High P/E on company guide is only coherent if the market prices **monetization and/or buybacks**. Without sales, mid-teens × FY26 EPS is a harsh but plausible derating (`09_Scenarios` PE compression block).

**Clock:** ICE is buying private detention RE under the current admin. A Democratic 2029 administration (overhaul/abolish-ICE primary energy; Padilla–Booker-style private-detention phaseout risk) can freeze the buyer and cut funded beds. Practical deadline for meaningful closings: **YE2027 / early 2028**.

**Paradox:** Federal title (CXW path) may harden detention infrastructure — but GEO only gets paid if **it** sells. Holding title into a Dem term leaves politically stranded private RE while CXW already cashed out.

---

## 6. Scenario framing

Probabilities are editable on `09_Scenarios`. Research stance:
- **Several sales** = most consistent with “active process” language  
- **Full ICE sale** = upside skew if CXW program expands to GEO’s ~23 sites  
- **No sale + Dem phaseout** = left tail that makes today’s guide P/E look reckless  

Position sizing should reflect **path dependency**, not a static “cheap on NAV” slogan.

---

## 7. Monitor

1. 8-K PSA for GEO→DHS/ICE facility sales  
2. Further CXW (or GEO) ICE RE prints  
3. CO/WA/FL/PA support-services awards  
4. ICE census vs funded beds  
5. Restricted-payment headroom post any sale  
6. 2028 platform language on private detention  
7. ISAP counts / GPS mix  

---

## Sources

GEO 2Q26 supplemental & call; FY25/init 2026 guide; March 2026 investor presentation; Lawton 8-K/PR; CXW sale PRs & Q2’26 materials; Dignity Act / 2028 Dem ICE coverage; market data as of report date. Detail and figures: **[[GEO Complete Investment Model]]**.
