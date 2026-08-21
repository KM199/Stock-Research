Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Generation assets and fuel required to energise AI datacenters. Distinct from [[Grid and Electrical Equipment]], which covers moving and transforming the power once generated.

The defining feature of this layer is **speed to power**. Grid interconnection now takes a median ~5 years to commercial operation, so developers increasingly bypass the utility entirely with behind-the-meter (BTM) generation. That shifts the buying decision from a utility procurement cycle to a corporate capex cycle, which is far faster and far less price sensitive.

## Demand

- ~101 GW of BTM generation capacity announced by datacenter developers, ~75% of it gas ([Avanza](https://avanzaenergy.substack.com/p/the-416-billion-gas-grab-that-infrastructure))
- That 75% gas share translates to roughly **4.9–5.6 Bcf/d of new natural gas demand** — competing head-on with LNG export for the same molecules
- 9.8+ GW of nuclear capacity committed to AI infrastructure across 13 announced projects as of May 2026; every major US hyperscaler has signed at least one deal ([Carnegie](https://carnegieendowment.org/research/2026/06/beyond-the-hype-assessing-hyperscaler-nuclear-commitments-against-u-s-energy-realities))
- Demand is inelastic to power price. A GW of AI compute generates revenue that dwarfs its fuel bill, so datacenter buyers will outbid industrial and residential load for both molecules and equipment.

## Supply

### Gas Turbines

A three-firm global oligopoly: GE Vernova, Siemens Energy, Mitsubishi Heavy Industries. This is the single hardest physical constraint in the buildout.

- GEV gas turbine backlog **116 GW** as of Q2 2026, up from 100 GW in Q1; guiding to ~125 GW including slot reservations by year end ([Utility Dive](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/))
- OEMs booking deliveries **into 2031**; reservations routinely four to five years out
- Mitsubishi sold out into 2028 even while doubling stated production
- Pricing up 10–20 points vs Q4 2025

The gate is not turbine assembly — it is upstream: large forgings, single-crystal superalloy hot-section blades, and the specialised casting capacity for them. Adding a forging press is a multi-year, capital-heavy commitment that OEMs are reluctant to make against a demand curve they suspect is a cycle.

### Reciprocating Engines and Gensets

Faster to deploy than turbines and modular, which suits phased datacenter energisation. Cummins is sold out of high-horsepower gensets through 2028. Increasingly used as primary BTM generation rather than pure backup, which changes emissions permitting exposure materially.

### Nuclear

Three separate paths, with very different timelines:
- **Existing fleet uprates and restarts** — the only nuclear that matters this decade. Microsoft's $16B / 20-year Three Mile Island contract takes 100% of output from 2027.
- **Large new-build AP1000-class** — 2035+, gated by large forgings and EPC skill that the US no longer possesses at scale.
- **SMRs** — Meta's ~6.6 GW commitment (TerraPower, Oklo) is the largest hyperscaler pledge, but essentially nothing is delivering power before the early 2030s.

Nuclear's real fuel bottleneck is **HALEU** (high-assay low-enriched uranium) for advanced designs, plus the same large-forging constraint that limits turbines. Domestic enrichment capacity is being rebuilt from near zero. See [[AI Critical Materials]] for uranium.

### Renewables and Storage

Solar plus battery is the fastest generation to build but wrong-shaped for a 24/7 load with ~95% utilisation. It functions as an energy hedge and a PPA/RE-credit instrument rather than as firm capacity. Batteries in this application compete for the same cells as EVs — see [[AI Critical Materials]].

### Fuel Supply

- Firm pipeline transport capacity is now a site-selection variable equal in weight to land and fiber
- Basis risk matters: cheap Permian or Appalachian gas at the wellhead is worthless without firm transport to the site
- Coal retirements are being deferred to hold capacity on the system — a live optionality for [[Thermal Coal]]

### Supply Shocks
- A turbine OEM production stumble or blade-supplier failure directly deletes GW of 2029–2031 capacity
- Gas price spike from the collision of LNG export growth and BTM datacenter demand
- Reversal of coal retirement deferrals if political winds shift
- Nuclear project cancellation cascade if one high-profile SMR fails to hit cost targets

## Industry Type
- Cyclicality: Historically deeply cyclical (turbines went through a decade-long depression post-2015). The current cycle is demand-led and the backlog now extends past most investment horizons, which suppresses near-term cyclicality but does not remove it.
- Capital Intensity: Very high for OEMs and for generation asset owners. Backlog visibility is unusually good; the risk is order cancellation, not order absence.

## Risks
- **Order book is a promise, not revenue.** Slot reservations four to five years out convert to cash only if the AI capex cycle holds. Cancellation terms are the thing to read.
- **Emissions permitting** on BTM gas — running gensets as primary rather than backup power invites a regulatory fight that has not yet fully arrived.
- **Rate socialisation backlash.** BTM generation is partly a way to avoid the political fight over who pays for grid upgrades; regulators are starting to close that door.
- **Nuclear timeline slippage** is the base case, not the risk case. Treat announced SMR GW as optionality with near-zero near-term delivery.
- Shared bottlenecks with [[Grid and Electrical Equipment]] — a project with a turbine but no step-up transformer generates nothing.

## Stocks
-
