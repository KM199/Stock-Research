# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Obsidian markdown vault for stock research.

## Vault Structure

```
Stocks/
  <Sector>/
    <TICKER>/           ← every stock gets its own folder
      <TICKER>.md       ← main note
      <TICKER> YYYY-MM-DD <Description>.md  ← dated notes (see below)
    <Industry>.md       ← industry overview notes sit at sector level
People/                 ← notes on notable investors
Financial Concepts/     ← accounting and valuation concept definitions
Abbreviations/          ← financial abbreviation glossary
Idea Types/             ← Lynch investment category frameworks
Books/                  ← notes from investment books
scripts/                ← Python analysis scripts (not Obsidian notes)
  brent_spreads.py      ← Brent crude call spread analyzer
  xlsx_model.py         ← cloud-edit Excel models via markdown sidecars
.venv/                  ← virtual environment (do not edit)
requirements.txt        ← Python dependencies
```

**Sectors in use:** Technology, Healthcare, Industrials, Infrastructure, Financials, Consumer, Materials, Crypto, Natural Resources

## Scripts

Python scripts live in `scripts/`. The venv and `requirements.txt` are at the vault root.

**Setup (first time):**
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
```

**Run a script:**
```bash
.venv/bin/python scripts/brent_spreads.py
.venv/bin/python scripts/xlsx_model.py show
```

**`brent_spreads.py`** — fetches live Brent crude options from Barchart using a headless Chromium browser (Playwright), which intercepts the page's internal API call. No API key required. Compares $X/$200 call spreads across strikes $120/$130/$140/$150 for a given expiry, or holds the lower strike fixed at $120 and varies across expiry dates. Prices use bid/ask midpoint where a live market exists; falls back to last settlement price for illiquid strikes.

**`xlsx_model.py`** — cloud/Cursor-friendly Excel workflow. `.xlsx` files stay the formula engine; a markdown sidecar (`TICKER Model Inputs.md`) is the edit surface for blue input cells. Recalculates without Microsoft Excel.

```bash
.venv/bin/python scripts/xlsx_model.py list
.venv/bin/python scripts/xlsx_model.py show                  # live Cover outputs
.venv/bin/python scripts/xlsx_model.py dump                  # xlsx → markdown sidecar
.venv/bin/python scripts/xlsx_model.py apply                 # sidecar → xlsx, then recalc
.venv/bin/python scripts/xlsx_model.py set '01_Inputs!B6=35' # one-off cell edit + recalc
.venv/bin/python scripts/xlsx_model.py sheet 01_Inputs --values
.venv/bin/python scripts/xlsx_model.py check
.venv/bin/python scripts/test_xlsx_model.py
```

Default workbook is `GEO Complete Investment Model`. Pass `-w "GEO ICE"` (unique substring) for the ICE NAV workbook. After local Excel edits, run `dump` so the sidecar matches. Do not copy model outputs into stock notes — live numbers stay in the workbook / sidecar.

**Never duplicate — everything has a place.** This is the core Obsidian principle for this vault. If something is already written somewhere, link to it, never copy it. Industry risks belong in the industry overview note; stock notes link to that note rather than restating the risks.

**Wikilinks resolve by filename** — Obsidian finds notes by name regardless of folder, so `[[DAC]]` works even after moves. Dangling links (e.g., `[[Stalwarts]]`, `[[Near Shoring]]`) are intentional placeholders, not errors.

## Note Conventions

**Filename is the title** — in Obsidian the filename is the note title. Never add a heading that repeats the filename. Do not use `## {{title}}` or any equivalent in templates or notes.

**Ticker naming** — filenames are all-caps ticker only: `GOOG.md`, `TSLA.md`. Tickers are unique so no company name needed. Use `[[TICKER]]` for wikilinks.

**Dated notes** — short, time-stamped observations filed alongside the main note: `TICKER YYYY-MM-DD Description.md`. Use these for quick thoughts, earnings reactions, or trading notes. When a dated note is created, add a wikilink to it in the `## Notes` section of the main stock note, ordered earliest to latest.

**Date format** — `YYYY-MM-DD` in filenames (e.g., `GEO 2024-02-18.md`). Existing files use `YY-MM-DD`; prefer the 4-digit year going forward.

**Tags** — `#stock` is used on some ticker notes.

**Industry overviews** — placed at the sector level (e.g., `Stocks/Industrials/Marine Transportation.md`), not inside a stock subfolder. Two types exist:
- *Analysis notes* — investment-focused, use the Industry Overview template (Parent Industry / Overview / Demand / Supply / Industry Type / Risks / Stocks)
- *Definition notes* — explain what something is (e.g., `Bulk Carriers.md`), written freeform, no template needed

The `## Stocks` section in an analysis note links to every stock covered in that industry — the industry note is the hub, stock notes link back to it.

## Investment Framework

Research uses Peter Lynch's stock categories from *One Up on Wall Street*:
- **Stalwarts** — large, stable companies (BRK.B, PYPL, OMAB)
- **Fast Growers** — high-growth plays (TMDX, CELH, TSLA, NVDA)
- **Cyclicals** — economically sensitive (Met Coal, Nat Gas, shipping stocks)
- **Turnarounds** — recovery plays (MPW)

`Research List.md` is the active watchlist organized by these categories. `index.md` tracks current long positions.

## Stock Note Structure

A well-formed main stock note contains:
- **Idea** — Lynch category wikilink (e.g., `[[Cyclicals]]`)
- **Industry** — wikilink to the relevant industry overview
- **Last update** — date of most recent edit
- **Overview** — what the company does
- **Thesis** — investment case with numerical assumptions
- **Risks** — company-specific and industry risks
- **Catalysts** — specific events that would move the stock
- **Price targets** — valuation with methodology
