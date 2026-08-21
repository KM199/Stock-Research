Parent Industry: [[Technology]]
Last update: 2026-07-29

## Overview

Hub note mapping the physical supply chain of the AI datacenter buildout — every material, product, service, and energy input required, from the accelerator down to the mine.

Scope is **hardware and physical inputs only**. Software, model labs, and application layers are deliberately excluded.

Scale of the spend being absorbed by this chain:
- Big-5 hyperscaler capex ~$660–725B in 2026, roughly 2x the 2022–2024 three-year total ([Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/), [Goldman via Intellectia](https://intellectia.ai/blog/ai-infrastructure-investment-july-2026))
- ~23 GW of datacenter IT capacity under construction globally, ~75% in the US ([BNEF](https://about.bnef.com/insights/data-centers/ai-data-center-build-advances-at-full-speed-five-things-to-know/))
- IEA projects global datacenter electricity consumption reaching ~1,000 TWh in 2026 — roughly Japan's total national consumption

The central investment observation: **capital is no longer the constraint — physical throughput is.** Money can be raised in a quarter. A transformer takes four years, a gas turbine slot is booked to 2031, and an electrician takes four years to train. Every layer below is a place where the money queues up behind an object that cannot be manufactured faster.

## Order Map

**1st order — the thing being bought**
Accelerators (GPU/ASIC), AI servers, rack-scale systems, switching, storage, the datacenter shell and its power/cooling plant.

**2nd order — required to build or operate the 1st order**
- [[Advanced Packaging]] — CoWoS, interposers, ABF substrates
- [[Memory and HBM]] — HBM stacks, and the DDR5 crowd-out they cause
- [[Semiconductor Fab Inputs]] — litho/dep/etch tools, wafers, resists, wet chemicals
- [[Optical Networking]] — transceivers, EML lasers, DSPs, fiber
- [[Power Electronics]] — SiC/GaN devices, 800 VDC conversion, solid-state transformers, BBUs
- [[Power Generation for Data Centers]] — gas turbines, nuclear/SMR, reciprocating gensets, fuel supply
- [[Grid and Electrical Equipment]] — transformers, switchgear, breakers, cable, interconnect
- [[Data Center Cooling]] — CDUs, cold plates, chillers, manifolds, coolants
- [[Data Center Construction]] — shell, land, water, permitting, and the labor to install all of the above

**3rd order — inputs to the 2nd order**
Silicon wafers, EUV photoresist and mask blanks, ABF film, specialty and bulk gases, CMP slurry and pads, sputtering targets, quartz crucibles, grain-oriented electrical steel, copper wire rod and busbar, large forgings and castings, turbine superalloy blades, refrigerants and dielectric coolants, high-purity water treatment, transformer oil, cement and structural steel.

**4th order — raw commodities and molecules**
See [[AI Critical Materials]] for the full mine-to-molecule layer: copper, gallium, germanium, helium, neon, rare earths, silicon metal, high-purity quartz sand, nickel/cobalt, aluminum, iron ore/coking coal, uranium, natural gas.

## Binding Constraints

Ranked by how hard the wall is. A constraint is "hard" when capacity cannot be added inside the investment horizon regardless of price.

| Constraint | Current lead time / gap | Why it can't be fixed fast |
| --- | --- | --- |
| Large power transformers | 128–160+ weeks, extremes of 48–60 months | GOES steel from a handful of mills; new mill = 5+ yrs |
| Gas turbines | Booking into 2031; 116 GW backlog at GEV alone | 3 global OEMs; forging and blade capacity is the gate |
| Grid interconnection | Median ~5 yrs to COD; up to 12 yrs in some queues | Regulatory + transmission, not manufacturing |
| Advanced packaging (CoWoS) | 52–78 wk; supply ~80–90% of demand | Tool delivery and cleanroom build |
| HBM | Sold out for 2026 | Wafer capacity is fungible with DDR5 — zero-sum |
| EML lasers / 800G optics | Production 40–60% below demand thru 2027 | Handful of qualified fabs; NVDA pre-bought capacity |
| Skilled electricians | 300k–500k worker shortfall | 4-yr apprenticeship; cannot be imported quickly |
| Medium-voltage switchgear | 52–120 wk; effectively sold out to 2028 | Copper, breakers, and skilled assembly |
| Copper | 2026 deficit >400kt | New mine = 10–15 yrs discovery to production |
| CDUs | 16–24 wk and lengthening | New category; capacity being built from a low base |

## Second-Order Effects Worth Tracking

Places where AI demand shows up somewhere unrelated, which is usually where the mispricing sits.

- **DRAM crowd-out.** HBM took 23% of global DRAM wafers in 2026 vs 8% in 2024, with a ~3:1 wafer conversion penalty. Consumer and enterprise DDR5 pricing doubled as collateral damage. See [[Memory and HBM]].
- **Grid cost socialisation.** Datacenter load raises retail rates for everyone on the same interconnection, creating political risk — the main non-technical threat to the buildout. See [[Grid and Electrical Equipment]].
- **Gas demand.** ~101 GW of announced behind-the-meter gas translates to ~5 Bcf/d of incremental demand, competing directly with LNG export for Permian and Appalachian molecules. See [[Power Generation for Data Centers]] and [[Natural Gas Power Generation]].
- **Trades wage inflation.** Datacenter construction labor costs up 8–12% YoY, which reprices every other construction project competing for the same crews. See [[Data Center Construction]].
- **Export-control weaponisation.** China has now extended controls from rare earths to gallium/germanium to graphite to helium (July 2026) — the pattern is expanding, not stabilising. See [[AI Critical Materials]].
- **Refrigerant and coolant demand.** Direct-to-chip and immersion create a new industrial demand line for dielectric fluids and PFAS-adjacent chemistries facing simultaneous regulatory pressure. See [[Data Center Cooling]].

## Risks to the Whole Thesis

- **Demand air pocket.** If model economics disappoint, the order book unwinds fastest at the long-lead layers where buyers have prepaid for 2029–2031 slots. The bottleneck names have the most operating leverage in both directions.
- **Efficiency shock.** An architectural change that cuts compute-per-token materially would hit the physical chain harder than the chip layer, because the physical chain is sized to peak plan.
- **Delivery failure is not the same as demand failure.** Estimates suggest 30–50% of planned 2026 US capacity could slip on equipment availability alone — this defers revenue for the chain rather than destroying it.
- **Political backlash** on rates, water, and land use — the softest layer to attack and the fastest to change.
- **Concentration.** Roughly five buyers underwrite the entire chain. Any one of them cutting capex is a demand shock to every layer below.

## Notes
-
