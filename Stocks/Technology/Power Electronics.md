Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Power conversion between the utility feed and the silicon. Distinct from [[Grid and Electrical Equipment]] (which delivers power to the building) and [[Power Generation for Data Centers]] (which produces it).

A conventional datacenter converts power roughly five or six times between the medium-voltage feed and the processor core, losing a few percent at each step. At 600 kW per rack that accumulated loss becomes both a cost and a thermal problem large enough to force an architectural rewrite. Hence the industry-wide move to **800 VDC**.

## Demand

- NVIDIA is working with 20+ AI infrastructure providers (CoreWeave, Lambda, Nebius, OCI among them) on 800 VDC datacenter designs, targeting the Rubin Ultra generation expected 2027 at up to **600 kW per rack**
- Claimed benefits: ~5% end-to-end power efficiency gain, ~70% reduction in maintenance cost from fewer PSU failures, and reduced cooling load from removing AC/DC conversion hardware inside the rack ([Institution of Electronics](https://institutionofelectronics.ac.uk/the-shift-to-800-vdc-power-architectures-in-ai-factories/))
- Every watt of the ~23 GW under construction passes through this layer, so demand scales with IT load rather than chip count

## Supply

### Wide-Bandgap Semiconductors

The 800 VDC architecture is only practical with wide-bandgap devices:
- **SiC MOSFETs** — high-voltage front-end conversion, e.g. 13.8 kV utility AC down to 800 VDC, and inside solid-state transformers
- **GaN HEMTs** — high-frequency, high-density DC/DC conversion inside the rack (800 V → 54 V → 12 V)

Notable market context: the SiC industry built enormous capacity for an EV demand curve that disappointed badly. Substrate and epitaxy utilisation fell to ~50% upstream and ~70% on device lines, and Yole expects the downturn to persist to **2027–2028** ([Semiconductor Today](https://www.semiconductor-today.com/news_items/2025/dec/yole-181225.shtml)). AI datacenter demand is arriving into that overhang.

This makes SiC an unusual case in the AI chain — a bottleneck-adjacent technology with *slack*, which changes the investment character entirely. It also caps the upside: one estimate puts the datacenter infrastructure opportunity at only **~$200M over five years** against a ~$2.2B 2026 SiC wafer market. SiC is a real AI beneficiary at the margin, not an AI story. Do not confuse the two. GaN is tighter, particularly at 650 V and above.

Inputs: SiC substrates (silicon carbide boule growth is slow and yield-limited), GaN-on-silicon epitaxy, and gallium — see [[AI Critical Materials]]. Epitaxy tool lead times are extending.

### Solid-State Transformers

SSTs replace the iron-and-copper transformer with high-frequency power electronics. Directly relevant because they sidestep the **grain-oriented electrical steel** constraint that dominates [[Grid and Electrical Equipment]] — the most interesting structural workaround in the buildout.

Enphase's IQ SST uses 342 GaN power modules per 1.25 MW rack at up to 98.5% efficiency, coordinated by a custom 22nm control ASIC ([pv magazine](https://pv-magazine-usa.com/2026/07/07/enphase-targets-800-v-dc-data-centers-with-distributed-solid-state-transformers/)). Wolfspeed and others are pursuing SiC-based designs.

Whether SSTs actually displace conventional transformers at scale is a genuinely open question — reliability track record at utility scale is thin and datacenter operators are conservative. But the incentive is enormous when the alternative has a four-year lead time.

### Rack Power and Backup

- Power shelves, busbars, and PSUs — shifting to 800 V changes every part
- **Battery backup units (BBUs)** at rack level, replacing or supplementing centralised UPS. Rack-level batteries suit the very high, very spiky load profile of AI training far better than a central UPS.
- Cells compete with EV and grid storage for the same LFP/NMC supply — see [[AI Critical Materials]]
- Supercapacitors for short-duration transient smoothing, an emerging category driven by the extreme power steps AI workloads impose on the grid

### Passive Components

Capacitors (film, MLCC, electrolytic), magnetics, inductors, and connectors. Unglamorous, high-volume, and periodically the actual thing that stops a production line. MLCC content per AI server is far above a conventional server.

### Supply Shocks
- Gallium export controls affecting GaN
- A reliability failure in an early SST deployment, which would set the category back years
- Battery cell allocation competition from EV and grid storage
- Passive component shortages, which historically appear suddenly and resolve slowly

## Industry Type
- Cyclicality: Moderate for the semiconductor content; the SiC/GaN makers are currently working through an EV-driven downcycle while AI demand builds — an unusual counter-cyclical setup within the AI theme.
- Capital Intensity: High for wide-bandgap substrate and device fabs. Moderate for module and system assembly.

## Risks
- **800 VDC adoption timing.** This is a 2027+ architecture. Designs and revenue assumptions built around it are exposed to slippage in the Rubin Ultra timeline.
- SiC overcapacity persisting — AI volumes may not be large enough to absorb capacity built for an EV market that did not arrive.
- Chinese SiC and GaN capacity is scaling aggressively and competing on price.
- SST is a promising story with limited field-proven reliability data; conservative buyers may simply wait out the transformer queue instead.
- This layer is a small share of total datacenter capex, so it is a leveraged play on the theme rather than a large direct beneficiary.

## Stocks
-
