Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

Moving data between accelerators. In an AI cluster the network is not peripheral — training performance is bounded by interconnect bandwidth, so optics scale roughly in proportion to GPU count and increasingly faster than it, as topologies grow more connection-dense per accelerator.

## Demand

- 800G transceiver demand jumped from **24 million units in 2025 to a projected 63 million in 2026**
- AI-focused optical transceiver market growing from $16.5B (2025) to **$26B (2026)**, +57% YoY ([TrendForce](https://www.trendforce.com/presscenter/news/20260420-13017.html))
- McKinsey projects 800G production running **40–60% below demand through 2027**, with 1.6T shortfalls likely through 2029
- Roadmap: 800G → 1.6T → 3.2T, with each generation arriving faster than the last

## Supply

### EML Lasers — the Chokepoint

Electro-absorption modulated lasers integrate modulation onto the laser chip. Manufactured by a handful of firms globally; the production threshold is very high and III-V epitaxy yields are the limiter.

In March 2026 **NVIDIA committed $4B to Lumentum and Coherent to secure priority EML access**, pushing lead times for every other buyer beyond 2027 ([TechTimes](https://www.techtimes.com/articles/317281/20260527/ai-data-center-optical-component-shortage-nvidias-4b-laser-lockup-pushes-rivals-past-2027.htm)). This is a notable move: the chip designer reaching three layers down the supply chain to lock capacity, which tells you where the real constraint sits.

Substrate inputs are indium phosphide and gallium arsenide — see [[AI Critical Materials]] for gallium export controls.

### DSPs and Retimers

Transceiver DSPs are now leading-edge parts. **3nm DSP shortages in 2026 pushed 800G lead times past 40 weeks.** This creates a circular dependency: the optics needed to build AI clusters depend on the same foundry capacity the accelerators do. Linear pluggable optics (LPO) and linear receive optics (LRO) remove or simplify the DSP and are being pursued partly to escape this constraint.

### Co-Packaged Optics

Moving the optical engine onto the switch or accelerator package. Cuts power meaningfully and is the direction of travel, but pulls optics into [[Advanced Packaging]] and creates serviceability problems — a failed laser on a $50k package is a very different repair from swapping a pluggable module.

### Fiber and Cable

- Fiber optic cable lead times have stretched to roughly **a year**
- Preform manufacturing is the upstream constraint; adding draw-tower capacity is faster than adding preform capacity
- Both intra-datacenter (single-mode and multi-mode) and the long-haul builds now being commissioned to link geographically distributed training clusters — a distinct and growing demand line

### Copper Interconnect

Direct-attach copper (DAC) and active copper cables handle short in-rack runs more cheaply and with lower power than optics. NVIDIA's rack-scale designs use very large copper cable bundles. This is a genuine substitute at short reach and it caps optics demand growth inside the rack — but copper cannot reach beyond a few meters at these data rates, so scale-out remains optical.

### Supply Shocks
- Single-supplier III-V fab incident
- Further capacity lock-ups by large buyers, which are effectively supply shocks for everyone else
- Foundry allocation shifting away from DSPs toward higher-value accelerator dies
- Gallium/indium export restrictions

## Industry Type
- Cyclicality: High and historically brutal — optical component makers have a long record of boom, capacity addition, and margin collapse.
- Capital Intensity: High for III-V fabs, moderate for module assembly. Module assembly is where Chinese competition is most intense and margins thinnest.

## Risks
- **The historical base rate here is bad.** Optical components is an industry that has repeatedly converted a demand boom into a margin bust by over-adding capacity. The current shortage is real; the durability of the pricing is the question.
- Chinese module makers compete hard on price and are working up the value chain into components.
- Technology transition — CPO and LPO both restructure who captures value.
- Copper DAC substitution at short reach.
- Customer concentration is extreme, and NVIDIA has demonstrated willingness to reach directly into the supply chain and dictate allocation.

## Stocks
-
