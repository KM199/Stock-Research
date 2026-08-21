Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Everything between the generator and the rack: transformers, switchgear, breakers, busway, cable, substations, and the interconnection process itself. Generation is covered in [[Power Generation for Data Centers]]; conversion inside the white space is covered in [[Power Electronics]].

Wood Mackenzie's 2026 Grid Equipment Outlook calls transformer lead times "the single most critical constraint on the energy transition." That is a strong claim and it appears to be correct — this layer, not the chip layer, is where the AI buildout physically stalls.

## Demand

- US datacenter electrical equipment market ~$20B in 2026, projected to $65B by 2030
- Generator step-up (GSU) transformer demand **+274% from 2019 to 2025**; substation transformer demand +116% ([POWER Magazine](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/))
- Demand is not solely AI — grid replacement of a fleet largely installed in the 1960s–70s, electrification of transport, and reshored manufacturing all draw on the identical equipment pool. AI is the marginal buyer that broke a market already running tight.
- 30–50% of planned 2026 US datacenter capacity is estimated to be at risk of slipping or cancelling because this equipment cannot be delivered on time

## Supply

### Large Power Transformers

| Equipment | 2026 lead time |
| --- | --- |
| Standard power transformer | ~128 weeks |
| Generator step-up (GSU) | ~144 weeks, 100–150+ wk range |
| Substation transformer | 160+ weeks (was ~140 wk in 2023) |
| Constrained / extreme cases | 48–60 months |

The binding input is **grain-oriented electrical steel (GOES)** for the core. Produced by only a handful of mills globally; NLMK Russia — among the largest — was sanctioned in 2022 and that capacity has not returned. GOES prices have roughly doubled since 2020. A new GOES line is a 5+ year, billion-dollar commitment, and mills will not build it against a demand curve they read as a cycle. Secondary constraints: copper winding, transformer-grade mineral oil, and bushings.

### Switchgear and Protection

- Standard medium-voltage switchgear: 52–80 weeks
- Customised, 38 kV / 69 kV: 96–120 weeks
- MV switchgear effectively **sold out through 2028** in many channels

Bottleneck is copper busbar, vacuum interrupters, and skilled assembly labor rather than any exotic material.

### Cable and Conductor

HV/MV cable, busway, and the extraordinary quantity of copper inside a datacenter — see [[AI Critical Materials]] for the copper intensity numbers and deficit. Fiber optic cable lead times have stretched to roughly a year; covered in [[Optical Networking]].

### Interconnection — the Non-Manufacturing Bottleneck

- US interconnection queue backlog ~**2,600 GW**
- Median time to commercial operation approaching **5 years**; some datacenter projects facing up to 12
- PJM data: AI infrastructure entering service in 2025 averaged 7+ years — ~3 years to an interconnection service agreement, then ~4 more years to come online
- FERC has forced six grid operators to rewrite large-load interconnection rules for facilities over 20 MW, which is the main reform to watch

This is a regulatory and transmission-planning problem, not a manufacturing one, and it therefore responds to policy rather than to capex. It is the primary reason behind-the-meter generation exists.

### Supply Shocks
- Further loss of GOES capacity — the market has no slack
- Copper supply disruption (see [[AI Critical Materials]])
- Tariff regimes on imported transformers and steel, which reprice the entire order book mid-flight
- A major grid failure event that triggers emergency replacement demand competing with new build

## Industry Type
- Cyclicality: Moderate historically, currently in a structural upswing that looks more like a replacement supercycle than a normal cycle. The installed base needs replacing regardless of AI.
- Capital Intensity: High for manufacturers, extremely high for the upstream steel input — which is precisely why capacity is not being added.

## Risks
- **Capacity response.** The rational bear case: at these prices and lead times, capacity eventually gets added, and it arrives in 2029–2030 into a demand air pocket. Watch announced GOES and transformer capacity expansions as the leading indicator of the top.
- **Rate socialisation and political backlash.** Datacenter load raising retail rates for households is the most potent political attack surface on the entire buildout.
- **Order cancellation.** Long backlogs cut both ways — a capex pause shows up here with a lag but with force.
- Interconnection reform could partially defuse the queue bottleneck, which would reduce the premium on BTM workarounds.

## Stocks
-
