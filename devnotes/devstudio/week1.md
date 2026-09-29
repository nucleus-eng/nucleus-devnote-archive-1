---
title: "Week 1, September 23 to 25"
---

We began DevStudio with a whiteboard exercise asking each participant to diagram their application demonstrations in terms of constituent Modules and Processes ({ref}`boards <fig:week1-boards>`). This exercise showed similarities across the proposed demonstrations, highlighted key intermediates, and gave us a means to track progress over the next 22 days. Each node is showing up with two proposed demonstrations. The Chicago Node is running a pH Sensing demonstration and an aTc Sensor demonstration. The London Node is running a LuxR-GFP Sensor demonstration in S30 Lysate and "CRAIC", a colorimetric reporter for AHL in cytosol.

Using a [Nucleus-Skills](https://github.com/nucleus-eng/nucleus-skills) based workflow we were able to quickly translate the hand-drawn schematic into digital diagrams that we can annotate ({ref}`pH Sensing <fig:week1-ph>`, {ref}`aTc Sensor <fig:week1-atc>`, {ref}`LuxR-GFP <fig:week1-ahl-lysate>`, and {ref}`CRAIC <fig:week1-craic>`). In this case, we've annotated Modules and Processes as green if they've been successfully implemented as the demonstration requires; orange if the modules or processes have been attempted but they require modification or additional tuning; red if the module or process has been ruled out, whether by choice or by failure, which nothing has been so far; and gray if the module or process remains untouched at DevStudio.

:::{figure} assets/week1/week1-diagrams.png
:label: fig:week1-boards
:align: center

The four demonstration boards as drawn at the end of Day 1. The handwriting is not meant to be read at this size. The boards are reproduced as a record of how the figures below ({ref}`pH Sensing <fig:week1-ph>`, {ref}`aTc Sensor <fig:week1-atc>`, {ref}`LuxR-GFP <fig:week1-ahl-lysate>`, and {ref}`CRAIC <fig:week1-craic>`) were made.
:::

::::{tab-set}

:::{tab-item} pH Sensing

```{include} assets/week1/week1-demo-ph.md
```

:::

:::{tab-item} aTc Sensor

```{include} assets/week1/week1-demo-atc.md
```

:::

:::{tab-item} LuxR-GFP in lysate

```{include} assets/week1/week1-demo-ahl-lysate.md
```

:::

:::{tab-item} CRAIC

```{include} assets/week1/week1-demo-craic.md
```

:::

::::

## Data pipeline updates

The path from experimental design to an annotated figure ran end to end for the first time during Week 1 ({ref}`pipeline <fig:week1-data-pipeline>`). It was useful to be able to flag gaps in compositional information that were missing from log files, e.g. is the concentration reported a stock or final? were the units of a reagent ambiguously labeled? etc. Given this tool, participants then suggested additional information that might be useful to be included in the structured format, such as links to sub-protocols for materials that requires additional preparation steps before making it into the well. 

:::{figure} assets/week1/week1-data-pipeline.png
:label: fig:week1-data-pipeline
:align: center

One experiment carried from design to figure. The plate map, the pipetting volumes, and the methods notes are drafted in a shared spreadsheet, where questions are raised and answered in comments against the design itself. The design becomes a standardized annotated table, one row per well, carrying the experiment, the kit, the DNA identifier, and every concentration. The annotated table runs smoothly through the [Cell Development Kit](https://github.com/nucleus-eng/nucleus) to produce an annotated figure (more on that in our next update).
:::

## Daily log

**Day 1, September 23.** 

Four routes toward a demonstration were sketched and agreed, with status, feasibility, and risk discussed for each against the three weeks ahead ({ref}`boards <fig:week1-boards>`). Participants prepared basic components, including stock solutions and amplified linear templates, and oriented themselves to the lab. With those pieces in place, first experiments were expected on Day 2, which would put the group in a position to start posting DevNotes and documentation early the following week.

**Day 2, September 24.**

- Materials: lipid stocks prepared for use over the next few weeks. Additional maxipreps in preparation.
- Cytosol: the AHSL Sensor tested in two implementations, LuxR to GFP in Nucleus Cytosol with and without T7 RNAP, and in S30 Lysate. The EsaR to mNeon Sensor system had a first test in Nucleus Cytosol. The pH Sensor is assembled.
- Cells: CPRG-containing liposomes prepared by the LUV method, and synthetic cells containing the pH Sensor prepared.
- Gels: no updates.

**Day 3, September 25.**

- Cytosol: DNA concentration tuning of the EsaR to mNeon Sensor system in Nucleus Cytosol. LuxR to GFP in Nucleus Cytosol tested against varying doses of AHL. TetO to plamGFP tested against varying doses of aTc.
- Cells: pH Sensor cells expressed PLA and lysed in response to different pH. An assay ran to find whether CPRG-containing vesicles were lysed and amenable to color change by LacZ.
- Gels: first cells embedded in PEG-norbornene gels.
