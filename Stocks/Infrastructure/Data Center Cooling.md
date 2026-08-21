Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Heat rejection for AI racks. The transition from air to liquid is the single largest architectural change in datacenter mechanical design in twenty years, and it created a component supply chain that did not previously exist at scale.

Air cooling runs out of headroom somewhere around 40–50 kW per rack. GB200-era racks are ~120 kW; NVIDIA's Rubin Ultra generation targets **600 kW per rack**. There is no air-cooled path to that number, which makes liquid cooling non-optional rather than a preference.

## Demand

- With GB300 entering large-scale production in 2026, AI server cooling shifts from the GB200-era hybrid approach to **fully direct-to-chip liquid** ([TrendForce via fiisual](https://fiisual.com/blog/post/2026/outlook-part-3-key-industries-cooling-industry))
- Demand is per-watt-of-IT-load, so it scales directly with the ~23 GW under construction rather than with unit chip counts
- Retrofit demand is a separate and underrated line — existing air-cooled halls being converted, which is more component-intensive per MW than greenfield

## Supply

### Coolant Distribution Units (CDUs)

The acknowledged chokepoint. A customer can hold signed hyperscaler contracts and secured power and still be unable to deploy without a CDU.

- Standard lead times **16–24 weeks** and vendors with thin buffer inventory are quoting six months PO-to-ship
- Vertiv expanded CDU manufacturing capacity 45x in 2024; Modine committed ~$100M to a dedicated facility — both direct responses to this constraint
- Capacity is being built from a very low base, so percentage growth is enormous but absolute supply remains tight

### Cold Plates, Manifolds, Quick Disconnects

- Cold plates: precision-machined copper with microchannel structures. Copper intensity adds to the totals in [[AI Critical Materials]].
- **Quick disconnects (QDs)** are the quiet bottleneck — dripless, blind-mate connectors rated for thousands of cycles in a live datacenter. Few qualified suppliers, and a single QD failure can take out a rack, so qualification cycles are long and switching costs are high.
- Manifolds, hoses, and in-rack plumbing — lower technical barrier, higher competitive intensity.

### Pumps, Valves, Heat Exchangers

Pumps and valves require redesign for higher flow rates and non-conductive fluids, which extends what were previously commodity lead times. Rear-door heat exchangers serve as the transitional retrofit product.

### Chillers, Dry Coolers, Cooling Towers

The facility-side loop. Large industrial chillers carry their own multi-quarter lead times and compete with the same compressor and heat-exchanger supply chains used by commercial HVAC.

### Fluids and Chemistry

- Direct-to-chip typically uses treated water or water/glycol — cheap, but demands water treatment, biocide, and corrosion inhibition programmes
- Immersion cooling uses engineered dielectric fluids, many of which sit in PFAS-adjacent chemistries facing tightening regulation in parallel with rising demand — a genuine collision
- Refrigerant transition (low-GWP) is happening simultaneously, forcing equipment redesign on an already-strained supply base

### Water

- Traditional evaporative cooling: ~80% of withdrawn water evaporates; Microsoft has reported >125M litres/yr per datacenter at ~0.30 L/kWh WUE
- The industry is pivoting hard to **closed-loop, zero-water-evaporation** designs — Microsoft piloting in Phoenix and Mount Pleasant in 2026, Oracle deploying similarly
- Closed loop trades water for electricity: it moves the burden onto the power layer, which is already the binding constraint. This is the key trade-off to understand — water savings are not free.
- Water availability remains a hard site-selection gate regardless; see [[Data Center Construction]]

### Supply Shocks
- Single-source QD or CDU supplier failure
- PFAS regulation landing on dielectric fluids faster than substitutes qualify
- Copper price spike flowing into cold plate cost
- A high-profile liquid leak incident, which would slow adoption and force requalification across the industry

## Industry Type
- Cyclicality: Tied entirely to datacenter capex, so as cyclical as that. Mitigated slightly by retrofit and service revenue.
- Capital Intensity: Moderate. Manufacturing is assembly and precision machining rather than fab-scale. This means capacity *can* respond — the constraint is real but softer than transformers or turbines, and it should ease first.

## Risks
- **Capacity catches up.** This is the least defensible bottleneck in the buildout. Barriers are qualification and reputation, not physics or capital. Expect margin compression as entrants qualify.
- Component commoditisation — manifolds and hoses first, cold plates next, CDUs last.
- Architecture risk: if rack density plateaus or an alternative thermal approach wins, product roadmaps built for 600 kW strand investment.
- Adoption is gated by the same power and construction timelines as everything else; cooling vendors cannot ship into halls that do not exist.

## Stocks
-
