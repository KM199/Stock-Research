Parent Industry: [[AI Buildout]]
Last update: 2026-07-29

## Overview

High Bandwidth Memory and the collateral damage it inflicts on the rest of the memory market. HBM is stacked DRAM die connected by through-silicon vias, packaged next to the logic die — see [[Advanced Packaging]].

The important structural fact: **HBM and conventional DRAM compete for the same wafers.** HBM consumes roughly three times the wafer area per bit of conventional DRAM because of die stacking, TSV overhead, and lower yields. Every wafer moved to HBM removes roughly three wafers' worth of DDR5 from the market. This is the cleanest example of a second-order AI effect landing somewhere seemingly unrelated.

## Demand

- HBM consumed **23% of global DRAM wafers in 2026**, up from 8% in 2024
- HBM **sold out for 2026**; Samsung and SK Hynix raised HBM contract pricing ~20% for the year
- Server DDR5 contract prices +57.3% QoQ in Q1 2026 and +49.7% QoQ in Q2 ([Findchips](https://blog.findchips.com/dram-memory-shortage-2026-pricing-lead-times-where-to-buy/))
- DDR5 64GB RDIMM prices roughly doubled; DDR4 up 60–80%
- Consumer collateral: a 32GB DDR5 kit at ~$95 in mid-2025 expected to peak at $550–600 in Q2 2026
- SK Hynix has warned the shortage may persist past 2030

## Supply

### Structure

A three-firm oligopoly — SK Hynix, Samsung, Micron — with essentially no credible fourth entrant at the leading edge outside China. This is the tightest market structure in the semiconductor industry and the reason pricing power is so extreme in this cycle.

### Why This Cycle Is Structural, Not Cyclical

The usual memory cycle runs: high prices → capacity added → glut → crash. That mechanism is partly broken here. New wafer capacity being built today is targeted at **HBM, not conventional DRAM**, because HBM margins justify the investment and DDR5 margins do not. Conventional DRAM supply therefore does not recover even as total industry capex rises.

This is worth holding sceptically — every memory cycle in history has been described as structural near the top. But the wafer-conversion mechanism is real and arithmetically verifiable, which is more than can usually be said.

### Technology Roadmap

HBM3E is the 2025–26 volume product; HBM4 introduces a wider interface and, importantly, a **logic base die** that in some designs is fabricated at a foundry rather than by the memory maker. That shifts value and competitive dynamics toward foundry-memory partnerships. Custom HBM base dies for individual accelerator customers are the direction of travel.

### Inputs

Standard DRAM front-end inputs — see [[Semiconductor Fab Inputs]]. HBM adds TSV etch and fill, wafer thinning, and stacking/bonding steps, each with its own equipment and materials tail.

### NAND and Storage

Less discussed but not immune. AI training and inference clusters consume very large quantities of high-performance SSD, and NAND has tightened alongside DRAM. Storage is a smaller share of cluster cost but a real demand line.

### Supply Shocks
- Korea concentration — the majority of world HBM capacity sits in two countries
- Yield excursion on a new HBM generation, which removes supply immediately
- China's mature-node DRAM push eventually pressuring the DDR4/DDR5 tail
- A power or water event at a major fab

## Industry Type
- Cyclicality: The most cyclical major industry in technology. Historically boom-bust with brutal amplitude. Currently in the boom.
- Capital Intensity: Extreme. Fabs cost tens of billions and depreciate fast.

## Risks
- **Memory always mean-reverts.** The base rate for "this time the memory cycle is different" is poor. Capacity being added for HBM in 2026–27 arrives in 2028–29, and if AI demand growth decelerates at all, the oversupply is severe.
- HBM4 transition risk — a maker that stumbles on a node loses a generation of share.
- Customer concentration: NVIDIA's qualification decisions effectively allocate the market.
- **Downstream demand destruction.** DDR5 at 5x price does not just get absorbed; it suppresses PC, phone, and general server demand, which eventually reduces total industry volume.
- Price-cost squeeze on everyone downstream who buys memory — an underrated margin headwind for server OEMs and device makers.

## Stocks
-
