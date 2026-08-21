Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

The assembly of an AI accelerator from multiple separate dies — logic chiplets, HBM stacks, I/O — into a single package. Front-end wafer fabrication inputs are covered in [[Semiconductor Fab Inputs]]; the memory itself in [[Memory and HBM]].

Advanced packaging has moved from a low-margin back-end afterthought to the binding constraint on AI chip supply. Every NVIDIA H100, H200, B200 and Rubin part, every AMD MI-series part, and every hyperscaler custom ASIC requires it. There is no way around this step and, for now, essentially one credible supplier at scale.

## Demand

- 2026 CoWoS demand estimated near **1,000,000 wafers**; supply running at roughly **80%** of that ([Oplexa](https://oplexa.com/ai-chip-packaging-bottleneck-2026/))
- TSMC monthly CoWoS capacity projected at 120–140k wafers in 2026, up from ~35k/month in late 2024 — a >3x expansion that still leaves a gap
- TSMC guiding to >80% CAGR in CoWoS capacity 2022–2027
- Supply–demand gap expected to narrow from ~20% to ~10% by end-2026 ([TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/))
- CEO C.C. Wei has described capacity as "extremely tight and sold out through 2026"; assembly lead times 52–78 weeks

## Supply

### CoWoS and Successors

CoWoS (Chip-on-Wafer-on-Substrate) is the only production-proven 2.5D technology for integrating large logic dies with HBM stacks. Variants:
- **CoWoS-S** — silicon interposer, the decade-long standard. Interposer size is limited by reticle field, forcing multi-reticle stitching for the largest parts.
- **CoWoS-L** — local silicon interconnect bridges embedded in organic material. Relieves the interposer size limit and is where volume is migrating.
- **CoPoS** (Chip-on-Panel-on-Substrate) — TSMC's next platform, moving from round wafers to rectangular panels for far better area utilisation. The medium-term capacity unlock worth tracking.
- **SoIC / hybrid bonding** — true 3D die stacking, increasingly used inside HBM as well.

### ABF Substrates

Ajinomoto Build-up Film is the dielectric layer in the organic package substrate. **Japan controls ~95% of global ABF film supply** and there is no qualified alternative at scale. Substrate manufacturing itself is concentrated in Japan, Taiwan and Korea. Large-body, high-layer-count substrates for AI packages have far lower yields than standard parts, so nameplate substrate capacity overstates effective AI capacity.

Historical precedent for the fragility: the 2011 Tōhoku earthquake took out ~90% of global BT resin supply.

### Interposers and Silicon Content

Silicon interposers consume 300mm wafer capacity themselves — the packaging step competes for the same wafers as the chips. Glass substrates are the widely-discussed replacement (better flatness, larger panels, better thermal match) but remain years from volume.

### Equipment

Thermocompression and hybrid bonders, die attach, molding, plating, and inspection. Bonder throughput is a real physical limit — hybrid bonding is slow, and units-per-hour is the number that determines how fast capacity actually scales. Lead times for these tools run into 2027.

### Thermal Interface and Materials

Thermal interface materials (TIM), underfill, molding compound, lids and integrated heat spreaders. Copper and specialty polymer inputs; a small cost line with an outsized ability to gate a ramp on qualification failures.

### Supply Shocks
- **Taiwan concentration.** The overwhelming majority of CoWoS capacity sits on one island. This is the single largest tail risk in the AI supply chain.
- Japan concentration on ABF film and substrate materials — earthquake and single-country regulatory exposure
- A yield excursion at any of the two or three qualified substrate suppliers
- Bonder tool delivery slippage

## Industry Type
- Cyclicality: High and amplified. Packaging sits downstream of chip demand with no diversification into consumer end markets at the leading edge.
- Capital Intensity: Very high and rising. Advanced packaging capex is now approaching front-end fab capex per unit of output, which is a genuine change in industry structure.

## Risks
- **The gap is closing.** Supply catching demand by late 2026/2027 removes the scarcity premium. The bottleneck is being solved, unlike transformers or electricians.
- Competition arriving — Samsung, Intel Foundry, and the OSAT tier are all investing hard into 2.5D/3D.
- Technology transition risk: capital deployed into CoWoS-S is stranded by CoWoS-L and CoPoS. Panel-level packaging is a step-change in cost per die that reprices the whole layer.
- Customer concentration — a handful of buyers underwrite the entire capacity expansion.
- Geopolitical: Taiwan Strait risk is not hedgeable and not priced in any conventional way.

## Stocks
-
