Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Everything consumed or installed inside a wafer fab: lithography, deposition and etch tools, silicon wafers, photoresists, masks, specialty and bulk gases, wet chemicals, CMP consumables, sputtering targets, and the fab building itself.

This is the deepest and most geographically concentrated layer in the AI chain. The consistent pattern is that at each step there are between one and three qualified suppliers worldwide, and qualification cycles run years — so substitution is theoretically possible and practically not.

## Demand

- Driven by wafer starts at leading-edge logic, HBM (see [[Memory and HBM]]), and the silicon interposers consumed by [[Advanced Packaging]]
- ASML EUV backlog hit a record **45 systems in Q1 2026** as TSMC, Samsung and Intel all ordered for 2nm and below ([RivCut](https://www.rivcut.com/manufacturing-news/asml-euv-orders-ai-chip-demand/))
- ASML raising EUV output ~30% for 2027 on top of its 2026 baseline, toward roughly 65 low-NA systems/year
- Consumables demand scales with wafer starts and with process complexity — leading-edge nodes use far more layers, so consumables demand grows faster than wafer count

## Supply

### Equipment

| Category | Structure |
| --- | --- |
| EUV lithography | ASML monopoly. High-NA ~$370M/system |
| DUV immersion | ASML, with Nikon/Canon marginal |
| Deposition / etch | Applied Materials, Lam Research, Tokyo Electron |
| Metrology / inspection | KLA dominant |
| Ion implant, CMP, clean | More fragmented |

EUV lead times exceed 12 months with slots secured into 2027; the general 12–24 month equipment lead time is described as the gating constraint for the industry. The upstream constraint on ASML is not assembly — it is **Zeiss optics, precision-machined vacuum chamber components, and metrology**, supplied by a deliberately narrow list of qualified vendors.

### Silicon Wafers

300mm polished and epitaxial wafers from a five-firm oligopoly (Shin-Etsu, SUMCO, GlobalWafers, Siltronic, SK Siltron), heavily Japan-weighted. Inputs run back through polysilicon to **high-purity quartz sand** and silicon metal — see [[AI Critical Materials]]. Quartz crucibles for Czochralski crystal growth depend on a handful of ultra-high-purity quartz deposits, notably Spruce Pine, North Carolina — one of the more remarkable single-point dependencies in modern industry.

### Photoresists and Mask Materials

**Japan controls >90% of EUV photoresists and 93% of EUV mask blanks.** No alternatives exist at scale. Mask blanks in particular are a multi-year qualification item with extreme defectivity requirements. Pellicles for EUV are a separate and similarly narrow supply base.

### Gases

- **Bulk:** nitrogen, oxygen, argon, hydrogen — supplied on-site by the industrial gas majors under long-term contracts. Low margin, high stickiness.
- **Specialty:** fluorinated etch gases, dopants, precursors — high purity, few suppliers, cylinder and purification capacity is itself a bottleneck.
- **Neon** — used in DUV excimer lasers. Ukraine supplied a large share of semiconductor-grade neon pre-2022; the disruption forced diversification and remains a live vulnerability.
- **Helium** — China imposed an abrupt export ban in July 2026, the first industrial gas to enter a major-economy export control regime, despite China itself importing ~90% of its helium ([Seoul Economic Daily](https://en.sedaily.com/finance/2026/07/11/china-bans-helium-exports-rattling-chip-supply-chain-again)). No synthetic production pathway exists. See [[AI Critical Materials]].

### Wet Chemicals and CMP

High-purity acids and solvents, cleaning chemistries, and CMP consumables — polyurethane porous polishing pads and colloidal slurries of nano-SiO2 or nano-CeO2. Cerium ties back to rare earths. These are cheap per wafer and catastrophic when absent.

### Sputtering Targets

Ultra-high-purity metal targets for PVD — copper, tantalum, titanium, cobalt, ruthenium. Ruthenium in particular is a small, illiquid market becoming strategically important as it replaces cobalt in advanced interconnect.

### Fab Construction

Cleanrooms, subfab, abatement, ultrapure water plants, chemical delivery, and specialised process piping. Competes for the same skilled trades as [[Data Center Construction]]. The industry response is modular: build shell and cleanroom first, phase tool install as demand clarifies.

### Supply Shocks
- Japan earthquake or single-supplier fire — the 2011 Tōhoku precedent removed 20% of 300mm wafer supply for 6–18 months
- Escalating Chinese export controls on gases and minerals
- Taiwan Strait
- Export control regimes cutting both ways — US restrictions on tool sales to China removed a large revenue pool for equipment makers

## Industry Type
- Cyclicality: High, but equipment makers now have unusually long backlogs and growing service/consumables revenue that dampens the trough.
- Capital Intensity: Very high for fabs. Moderate for equipment makers, whose real moat is accumulated R&D and installed-base lock-in rather than physical plant.

## Risks
- **China localisation** eroding the mature-node and consumables markets over time, and eventually working up the stack
- Export control policy volatility in both directions
- Customer concentration — three leading-edge logic buyers and three memory buyers
- A capex digestion year after the 2026–27 expansion wave; equipment orders lead wafer demand and therefore turn first
- Single-point failures with no redundancy at nearly every step — this is a source of both moat and tail risk

## Stocks
-
