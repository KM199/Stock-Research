Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

The raw commodity floor of the AI buildout — the mined ores, refined metals, and molecules that every layer above eventually resolves to. Where a layer note mentions a material, the detail lives here.

Two observations shape this whole layer:

1. **Mine supply cannot respond inside the investment horizon.** A new copper mine is 10–15 years from discovery to production. AI demand appeared over 24 months. The adjustment therefore happens entirely through price and demand destruction elsewhere.

2. **Refining, not mining, is the chokepoint.** For most of these materials the ore is geologically common; what is scarce is the refining and purification capacity, and that capacity is overwhelmingly Chinese. This makes the supply chain a policy variable rather than a geological one.

## Demand

### Copper — the Largest Single Line

The most material commodity exposure in the entire theme.

- AI datacenter copper intensity: **~30–47 tonnes per MW** inside the facility itself
- Including grid infrastructure (transmission, substations): **100–150 t/MW**
- A 1 GW AI factory requires roughly **50,000 tonnes of copper**
- At ~15 GW/yr of build, datacenters alone add **~750,000 t/yr** of new copper demand ([Tom's Hardware](https://www.tomshardware.com/tech-industry/ai-data-center-buildout-pushes-copper-toward-shortages-analysts-warn), [Carbon Credits](https://carboncredits.com/data-centers-copper-hunger-how-ai-is-driving-a-looming-supply-crunch/))
- 2026 market deficit forecast **>400,000 tonnes**; Wood Mackenzie put 2025 at 304kt
- S&P Global (Jan 2026) sees the shortfall widening, with AI and defence spending compounding the existing EV and grid drivers

Copper appears in windings, busbar, cable, cold plates, PCB, and interposer metallisation — it is the one material touched by nearly every layer above.

### Grain-Oriented Electrical Steel (GOES)

Transformer cores. Produced by a handful of mills globally; NLMK Russia sanctioned in 2022 with capacity never recovered. Prices roughly doubled since 2020. This single material is the reason transformer lead times run to four years — see [[Grid and Electrical Equipment]]. The workaround is solid-state transformers, covered in [[Power Electronics]].

### Gallium and Germanium

- China produces ~**98%** of world refined gallium and germanium
- Export controls imposed July 2023; the US-directed ban was suspended until 27 November 2026, so this is a live expiry to diary
- Gallium: GaN power devices, GaAs laser substrates for [[Optical Networking]]
- Germanium: optical and infrared applications, SiGe

Neither is geologically rare — both are by-products (gallium from bauxite/alumina, germanium from zinc). The scarcity is entirely refining capacity, and the West is rebuilding it slowly.

### Helium

China imposed an **abrupt export ban in July 2026** — the first industrial gas to enter a major-economy export control regime. Notable that China itself imports ~90% of its helium, which suggests the measure is domestic supply protection rather than external leverage, and therefore may be more durable than a negotiating tactic.

Helium is used for cooling and purging in semiconductor manufacturing. There is **no synthetic production pathway** — it is a by-product of natural gas processing at a small number of helium-rich fields (US, Qatar, Algeria, Russia). Recycling is the only demand-side lever.

### Neon

DUV excimer laser gas. Ukraine supplied a large share of semiconductor-grade neon before 2022. The disruption forced diversification and prices spiked hard; the supply base is broader now but remains thin. A by-product of steelmaking air separation, which ties it to an unrelated industrial cycle.

### Rare Earths

- China: ~60% of global mining, **~91% of separation and refining**; Malaysia a distant second
- Magnet REE demand (Nd, Pr, Dy, Tb) has doubled since 2015, set to grow another third by 2030 ([IEA](https://www.iea.org/reports/rare-earth-elements/executive-summary))
- April 2025 controls on seven heavy REEs and magnets; further restrictions on US and Japan in March 2026
- Heavy rare earths (dysprosium, terbium) are the acute constraint — small volumes, dual-use restrictions, and near-total Chinese control

AI exposure: motors and fans, hard disk drives, and cerium oxide in CMP slurries for [[Semiconductor Fab Inputs]]. Datacenters are a smaller REE consumer than EVs or wind, but they compete for the same constrained heavy-REE pool.

### Silicon Metal and High-Purity Quartz

Metallurgical silicon → polysilicon → wafers. The genuinely remarkable dependency is **high-purity quartz for Czochralski crucibles**. Two operations in Spruce Pine, North Carolina account for **>80% of world commercial HPQ supply** (~180–200kt/yr), with the top Iota 8 grade at 99.9992% purity selling around $10,000/tonne.

Worth holding with some nuance — the popular framing that all chipmaking would halt without Spruce Pine is overstated, since alternative deposits and synthetic routes exist at higher cost, and inner-vs-outer crucible layers have different purity requirements. But as a near-term, price-inelastic single point of failure it is real. Hurricane Helene shutting the mines in 2024 was the live stress test.

### Uranium

Feeds [[Power Generation for Data Centers]]. The specific constraint is not U3O8 in the ground but **conversion and enrichment capacity**, and for advanced reactors, **HALEU**, where Western capacity is being rebuilt from near zero after decades of reliance on Russian supply.

### Natural Gas

The dominant marginal fuel. ~101 GW of announced behind-the-meter capacity, ~75% gas, implying **4.9–5.6 Bcf/d** of incremental demand competing directly with LNG export. See [[Natural Gas Power Generation]].

### Others

- **Aluminum** — busway, structures, heat sinks. Energy-intensive to smelt, which creates a reflexive loop with power prices.
- **Nickel, lithium, cobalt, graphite** — BBUs and grid storage, competing with EVs. Graphite is under Chinese export control.
- **Ruthenium, tantalum, cobalt** — sputtering targets and advanced interconnect. Small, illiquid markets where a modest demand increase moves price violently.
- **Indium phosphide** — laser substrates.
- **Iron ore and coking coal** — structural steel, turbine forgings, transformer tanks. See [[Met Coal]].
- **Cement** — enormous volumes for foundations; regional and rarely binding, but energy-intensive.
- **Water** — increasingly a permitting constraint rather than a cost, driving the closed-loop pivot in [[Data Center Cooling]].

## Supply

### Supply Shocks
- **China's expanding export control architecture.** The sequence — rare earths → gallium/germanium → graphite → helium — is expanding, not stabilising. Assume the next material on the list is one currently thought safe.
- November 2026 expiry of the suspended gallium/germanium ban to the US
- Copper mine disruption (Chile, Peru, DRC, Indonesia); Grupo México has already flagged AI-driven shortfall
- Resource nationalism and permitting delays in Western jurisdictions
- Any single-point failure: Spruce Pine quartz, a GOES mill, a helium plant

## Industry Type
- Cyclicality: Highly cyclical, and these are classic [[Cyclicals]] in the Lynch sense — commodity price is the earnings driver, not volume or management skill.
- Capital Intensity: Extreme, with the longest lead times of any layer. This is exactly why the constraint is real and durable.

## Risks
- **Demand destruction.** High prices for copper and DRAM ration demand elsewhere in the economy. The commodity does not care that AI can pay.
- **Substitution.** Aluminum for copper in some conductor applications; SSTs for GOES; closed-loop for water. Every constraint eventually invites engineering around it.
- **Recycling and scrap** supply responds faster than mine supply and caps the upside on price spikes.
- **Policy reversal.** Export controls are negotiating instruments and can be lifted as abruptly as they were imposed — the November 2026 gallium expiry is a concrete example. A détente would deflate several of these theses quickly.
- The cardinal error in commodity investing: assuming the current demand curve extrapolates. AI capex is currently underwritten by five buyers.

## Stocks
-
