---
title: "Week 2, September 28 to October 2"
---

Week 2 built three of the four demonstrations end to end, and the work has shifted from assembly to tuning the output. The two-vesicle pH Sensor system ran first, in LGA on Day 7, and the aTc demonstration followed on Day 10 with tetO/R-PLA1 fully assembled in PEG-NB. The proxy reporters that Week 1 relied on were replaced by PLA1. Three challenges have since emerged: CPRG leaks in two-vesicle architectures; transcription is leaky in the repressed sensor systems; the efficiency of embedding cells in hydrogels is hard to quantify.

We've tracked progress on the four application demonstrations by updating the boards from Week 1, node for node ({ref}`pH Sensing <fig:week2-ph>`, {ref}`aTc Sensor <fig:week2-atc>`, {ref}`LuxR-GFP <fig:week2-ahl-lysate>`, and {ref}`CRAIC <fig:week2-craic>`). Updating the boards this week shows that our annotation scheme may not be adequate. Most nodes remain orange, and yet confidence in individual modules has grown: the EsaO/R-deGFP and PLA1 systems work well enough to document as standalone capacities, independent of any demonstration. The scheme turns a module green if it's demonstrated as intended to function in the end-to-end application demonstration. This means that a significant part of the aTc and CRAIC demos remain orange despite module validation being successful, i.e. detector-reporter constructs validated but not yet detector-lysis constructs.

On tooling, DevNotes can now be populated from logs, and the order of the steps changed. Rather than opening a Google Doc first, we populate a MyST Markdown DevNote, review it, and communicate the gaps to the developer with inline references to that draft. One short drafting session moved four experiments into a DevNote along with supporting documentation. We will refine this further in Week 3.

::::{tab-set}

:::{tab-item} pH Sensing

```{include} assets/week2/week2-demo-ph.md
```

:::

:::{tab-item} aTc Sensor

```{include} assets/week2/week2-demo-atc.md
```

:::

:::{tab-item} LuxR-GFP in lysate

```{include} assets/week2/week2-demo-ahl-lysate.md
```

:::

:::{tab-item} CRAIC

```{include} assets/week2/week2-demo-craic.md
```

:::

::::

## Daily log

These are the summaries circulated to PIs and to participants who could not attend.

**Day 6, September 28.**

- Cytosol: EsaO-PLA1 was expressed in Cytosol and used to test lysis of CPRG LUVs by color change. TetO/R-deGFP was tested in Cytosol. The ratio of luxR and plux-GFP was tuned in Cytosol.
- Cells: EsaO-PLA1 was expressed in Cells to test autolysis. TetO/R-deGFP was tested in Cells.
- Gels: Base Cell was embedded in LGA, ULGA and PEG-NB.
- DevNotes: a draft of "Two Vesicle Colorimetric pH Sensor System" was prepared.

**Day 7, September 29.**

- Cells: LuxR-GFP Cells were tested with AHSL. EsaO/R-PLA1 was tested with CPRG-containing vesicles.
- Gels: the two-vesicle pH Sensor system was tested in LGA, the first end-to-end demonstration. Base Cell was screened a second time in LGA, ULGA and PEG-NB.

**Day 8, September 30.**

- Cells: EsaO/R-PLA1 Cells and CPRG-containing vesicles were tested in solution. Leakiness of CPRG-containing vesicles was assayed.
- Full demonstrations: the pH Sensor system in LGA gave an ambiguous color change, with leaky CPRG vesicles the likely culprit. The tetO/R-PLA1 demonstration in PEG-NB was fully assembled and left to evaluate overnight. LuxR-GFP Sensors were embedded in ULGA to detect AHSL.
- Discussion: three challenges in implementing the demonstrations were discussed. First, the leakiness and unexpected difficulty of preparing CPRG-encapsulated vesicles. Second, leaky expression of repressed sensor systems. Third, assessing the tolerances of embedding cells in hydrogels with respect to signal generation.

**Day 9, October 1.**

- Cells: osmolarity sweep of CPRG- and PURE-containing vesicles in Cytosol.
- Gels: AHL sensing of bacterial supernatant by the LuxR-GFP Sensor in ULGA. PLA1-mediated lysis of vesicles in gels.
- Full demonstrations: the pH Sensor with SUVs was assembled.

**Day 10, October 2.**

- Cytosol: the EsaO/R system was tested with preincubated Mg to increase binding, and with lower DNA concentrations.
- Cells: LuxR-GFP in lysate GUVs was tested with both bacterial supernatant, which contains AHSL, and synthetic AHL.
- Full demonstrations: the pH Sensor system in LGA was reattempted with SUVs in place of LUVs, to address leaky CPRG. The full tetO/R-PLA1 demonstration in PEG-NB was assayed, and leaky expression of tetO gave ambiguous results.
- DevNotes: drafting began on DevNotes for the EsaO/R and tetO/R systems.

## Expected outputs

Each proposed demonstration earns a DevNote describing how it was built, including what did not work. Two further DevNotes are likely beyond the demonstrations themselves.

:::{table} DevNotes expected from DevStudio.
:label: tbl:expected-devnotes
:align: center

| DevNote | Covers | Status |
| --- | --- | --- |
| pH sensor in solution | The pH Sensing demonstration | Draft exists |
| EsaO/R-deGFP AHL Detector | The EsaO/R detector, characterized on its own | Draft exists |
| tetO/R system | The aTc Sensor demonstration | Drafting begun, Day 10 |
| CRAIC demonstration | The CRAIC demonstration, end to end | Not started |
| LuxR-GFP Sensor in lysate | The LuxR-GFP demonstration | Not started |
| Synthetic cells in gels | Embedding tolerances across LGA, ULGA and PEG-NB | Proposed |
| Low cost spectrophotometer | Instrument build and characterization | Proposed |
:::

Documentation covers the reusable parts the demonstrations are built from, as modules, processes and specifications on Nucleus Docs. Templates for each page were drafted before DevStudio, from conversations and updates with the contributors who own them. What remains is to populate them with the data and details that DevStudio produces.

:::{table} Nucleus Docs pages expected from DevStudio.
:label: tbl:expected-docs
:align: center

| Page | Kind | Status |
| --- | --- | --- |
| PLA1 Lysis | Module | Template exists |
| EsaO/R-AHL detector | Module | Template exists |
| pH detector | Module | Template exists |
| tetO/R aTc detector | Module, update to an existing page | Template exists |
| SUV preparation | Process | Template exists |
| LUV preparation | Process | Template exists |
| Embed cells in gels | Process | Template exists |
| Gel: LGA | Specification | Template exists |
| Gel: ULGA | Specification | Template exists |
| Gel: PEG-NB | Specification | Template exists |
| CPRG color change | Process | Template exists |
:::
