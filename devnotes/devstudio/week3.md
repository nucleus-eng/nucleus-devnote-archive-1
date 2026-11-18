---
title: "Week 3, October 5 to 9"
---

Week 3 saw two of the four demonstrations run through to completion. The pH sensing demo was completed ({ref}`pH Sensing <fig:week3-ph>`), and an attempt to pattern the sensor and read the output with a phone application was attempted but inconclusive. The LuxR-GFP demo also successfully crossed the finish line ({ref}`LuxR-GFP <fig:week3-ahl-lysate>`). Several attempts at tuning the aTc sensor demo ultimately did not reproduce the visible color change the demo required ({ref}`aTc Sensor <fig:week3-atc>`). Finally, the CRAIC demo, relying on constructs untested before DevStudio, saw some characterization of its constructs in base cell ({ref}`CRAIC <fig:week3-craic>`).

::::{tab-set}

:::{tab-item} pH Sensing

```{include} assets/week3/week3-demo-ph.md
```

:::

:::{tab-item} aTc Sensor

```{include} assets/week3/week3-demo-atc.md
```

:::

:::{tab-item} LuxR-GFP in lysate

```{include} assets/week3/week3-demo-ahl-lysate.md
```

:::

:::{tab-item} CRAIC

```{include} assets/week3/week3-demo-craic.md
```

:::

::::

## Daily log

These are the summaries circulated to PIs and to participants who could not attend. Days 14 and 15 have no entries below: pace picked up heading into the final stretch, and logging lost out to the work itself.

**Day 13, October 5.**

- Cytosol: a lower temperature was tried to slow T7 transcription down.
- Cells: at 1200 mOsm, LLUVs held their contents without leaking, confirmed with Charlie Newell. Setup began on an EsaO/R-mNeonGreen system.
- Gels: a repeat ran better in gel, though what the sensor's plate-reader output actually reads is still being worked out. A sensor was put into gel with LUVs. Setup began for a gel test of the LuxR-GFP line with synthetic AHL.
- Tooling: a QR-code approach to labeling samples was explored, outside of gel work.

**Day 16, October 8.**

- Cytosol: An additional bulk EsaO/R-mNeonGreen reaction ran alongside the GUV test below, pushing for more dynamic range against a signal low enough to disappear into the repressor's own noise floor.
- Cells: EsaO/R-mNeonGreen GUVs were tested again; microscopy stayed ambiguous, and the open question is how far that noise floor can be pushed down before the signal goes with it. A working GUV preparation was to move into gel next. Separately, a LacZ-vesicle preparation for the PLA1-lysis line gave flatter dose curves after switching to a Tween-based emulsion, with no clear jump from added aTc; a titration is planned. One run of that prep was short a beta-galactosidase addition, then given 1 µL of LacZ after the fact, so it is unclear whether too little enzyme reached the vesicles or a second population formed. CPRG dye release in the LuxR-PLA1 line failed in glucose-only buffer and needs HEPES; GUV stability across different gels is being tested ahead of using it to lyse a CPRG sensor.
- Gels: LUVs showed a color change only with HEPES buffer, and only in some of the gels tested.
- Full demonstrations: the LuxR-GFP demonstration's two-fold difference in gel with synthetic AHL was the week's first hard number; supernatant was repeated the next day and backfilled against lysate data already in hand. A constitutive control worked with supernatant and cells, though differently across media.
- DevNotes: drafting is in flight for the LuxR-GFP demonstration.

**Day 17, October 9.**

- Cytosol: EsaO/R-GFP ran in bulk alongside the synthetic-cell test below.
- Cells: EsaO/R-GFP was tested in synthetic cells. PLA1 was tested in both GUV and SUV form. A HEPES-buffer experiment was rebuilt and left overnight for microscopy. The LacZ/GFP two-population vesicle system, where protein expression is meant to trigger lysis, still needs analysis.
- Gels: patterned hydrogel development continued. The LuxR-GFP supernatant retry moved into gel today, alongside a solution-phase LuxR-cells-with-supernatant test.

## Expected outputs

These tables update the ones on the Week 2 page. Week 2's table assumed one DevNote per demonstration. That pattern held for pH Sensing and for the EsaO/R detector: each produced exactly the one DevNote expected, now under its actual title. It did not hold for the other two demonstrations. The aTc Sensor's actual development journey turned out to be five distinct devnotes: characterization in cytosol, characterization in GUVs, PLA1 in vesicles with its own titration and patterning, PLA1's lysis step tested on its own rather than as part of the aTc trigger, and a variant that co-encapsulates PLA1 expression with the beta-galactosidase substrate in a single GUV population instead of keeping the two separate. 

The LuxR-GFP demonstration split in two for a related reason: the bulk color-change result, LuxR-PLA1 lysing a CPRG carrier in solution, is a different chassis from the gel-embedded sensing the main demonstration is about, so it earned a DevNote of its own.

One further DevNote, on embedding tolerances across LGA, ULGA, and PEG-NB, characterizes the hydrogels used across all four demonstrations.


:::{table} DevNotes drafted during Week 3 and the weekend after.
:label: tbl:week3-devnotes
:align: center

| DevNote | Covers | Status |
| --- | --- | --- |
| [Two Vesicle Colorimetric pH Sensor System](https://devnotes.nucleus.engineering/articles/sh-20261011) | The pH Sensing demonstration | Draft exists |
| [Bacterial Sensing in Hydrogel Embedded Synthetic Cells using LuxR Dependent Transcriptional Regulation](https://devnotes.nucleus.engineering/articles/ln-20261011-03) | The LuxR-GFP demonstration, embedded in a gel | Draft exists |
| [Implementing of a bulk color change module into bacterial quorum sensing](https://devnotes.nucleus.engineering/articles/ln-20261011-01) | LuxR driving PLA1 to lyse a CPRG carrier, a bulk extension of the LuxR-GFP line | Draft exists |
| [Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation](https://devnotes.nucleus.engineering/articles/ln-20261011-02) | The EsaO/R detector, characterized on its own | Draft exists |
| [GUV Encapsulation of a TetR/aTc-Inducible deGFP Cell-Free Sensor](https://devnotes.nucleus.engineering/articles/mk-20261011-01) | The aTc Sensor demonstration, GUV form | Draft exists |
| [Expressing Cell-Free TetO-GFP in Solution with aTc Titration](https://devnotes.nucleus.engineering/articles/mkmb-20261011-03) | The aTc Sensor demonstration, solution-phase proxy work | Draft exists |
| [TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning](https://devnotes.nucleus.engineering/articles/mkmb-20261011-02) | The aTc Sensor demonstration, with PLA1 in place of the proxy | Draft exists |
| [Triggered Lysis of beta-Galactosidase-Loaded GUVs by Cell-Free Expressed Phospholipase A1](https://devnotes.nucleus.engineering/articles/mkop-20261011-01) | The aTc demonstration's PLA1 lysis step, on its own | Draft exists |
| [Co-Encapsulated Cell-Free PLA1 Expression in beta-Galactosidase GUVs](https://devnotes.nucleus.engineering/articles/mkmb-20261011-04) | The aTc demonstration's co-encapsulation variant | Draft exists |
| [Understanding Liposome Behaviour in Hydrogel Matrices](https://devnotes.nucleus.engineering/articles/opmb-20261011-01) | Embedding tolerances across LGA, ULGA and PEG-NB | Draft exists, metadata incomplete |
| CRAIC demonstration | The CRAIC demonstration, end to end | Never drafted; the demonstration itself never closed |
| Low cost spectrophotometer | Instrument build and characterization | Never drafted; superseded when the board moved to a standard plate reader |
:::

Week 2's table expected documentation table was based on pages drafted before the event and refined by the proposals described on week 1. In general, DevNotes inform documentation. As a result, the final documentation was tweaked to reflect the experiments as described in the DevNotes. Three kinds of page make up this corpus. A Module is a biochemical formulation that performs one function, answering what it is and what to expect when it's implemented. A Process is a protocol: the steps that turn physical materials into Base Cytosol, Base Cell, or a derived substrate. An Implementation is a documented combination of Modules and Processes operated together and characterized across operating conditions, a complete, working synthetic cell behavior rather than one of its parts. Only one DevStudio demonstration has resulted in an Implementation page that will live in Nucleus Documentation: Colorimetric pH Sensor. This reflects the fact that it was implemented in Cytosol *and* also replicated in one other lab.


:::{table} Nucleus Docs pages expected from DevStudio, checked against nucleus-docs.
:label: tbl:week3-docs
:align: center

| Page | Kind | Status |
| --- | --- | --- |
| PLA1 Lysis | Module | Not yet published |
| EsaO/R-AHL detector | Module | Live (draft), [`detector-esar`](https://docs.nucleus.engineering/docs/modules/detector-esar/spec/) |
| pH detector | Module | Live (draft), [`detector-ph`](https://docs.nucleus.engineering/docs/modules/detector-ph/spec/) |
| tetO/R aTc detector | Module, update to an existing page | Live (validated), [`detector-tetr-atc`](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/) |
| SUV preparation | Process | Not yet published as a generic process; the CPRG carrier's SUV form is in [`substrate-cprg-suv`](https://docs.nucleus.engineering/docs/modules/substrate-cprg-suv/spec/) |
| LUV preparation | Process | Not yet published as a generic process; the CPRG carrier's LUV form is in [`substrate-cprg-luv`](https://docs.nucleus.engineering/docs/modules/substrate-cprg-luv/spec/) |
| Embed cells in gels | Process | Live (draft), as two pages, [`embed-photocrosslinking`](https://docs.nucleus.engineering/docs/processes/embed-photocrosslinking/main/) and [`embed-thermal-setting`](https://docs.nucleus.engineering/docs/processes/embed-thermal-setting/main/) |
| Gel: LGA | Module | Live (draft), [`gel-lga`](https://docs.nucleus.engineering/docs/modules/gel-lga/spec/) |
| Gel: ULGA | Module | Live (draft), [`gel-ulga`](https://docs.nucleus.engineering/docs/modules/gel-ulga/spec/) |
| Gel: PEG-NB | Module | Live (draft), [`gel-peg-nb`](https://docs.nucleus.engineering/docs/modules/gel-peg-nb/spec/) |
| CPRG color change | Process | Live (draft), [`colorimetric-readout`](https://docs.nucleus.engineering/docs/processes/colorimetric-readout/main/) |
| Colorimetric pH Sensor | Implementation | Live (draft), [`colorimetric-ph-sensor`](https://docs.nucleus.engineering/docs/implementations/colorimetric-ph-sensor/main/) |
| Color Change | Module | Live (draft), [`color-change`](https://docs.nucleus.engineering/docs/modules/color-change/spec/) |
| pH Cascade | Module | Live (draft), [`ph-cascade`](https://docs.nucleus.engineering/docs/modules/ph-cascade/spec/) |
| pH Sensing Cell | Module | Live (draft), [`ph-sensing-cell`](https://docs.nucleus.engineering/docs/modules/ph-sensing-cell/spec/) |
| Reporter: LacZ Enzyme | Module | Live (draft), [`reporter-lacz-enzyme`](https://docs.nucleus.engineering/docs/modules/reporter-lacz-enzyme/spec/) |
| Anneal pH Trigger Duplex | Process | Live (draft), [`anneal-ph-trigger-duplex`](https://docs.nucleus.engineering/docs/processes/anneal-ph-trigger-duplex/main/) |
| Encapsulation: Freeze-Thaw | Process | Live (draft), [`encapsulate-freeze-thaw`](https://docs.nucleus.engineering/docs/processes/encapsulate-freeze-thaw/main/) |
:::

## Retrospective

DevStudio set out to reproduce each Node's demonstration in a new lab, document the modules behind them for reuse, and improve the tools connecting experimental work to that documentation. By the end of Week 3, two of the four demonstrations, pH Sensing and LuxR-GFP, were reproduced end to end. The aTc Sensor and CRAIC demonstrations advanced module by module, providing practical insights into implementing systems involving the tetR-aTc and newly introduced EsaR-AHL sensing systems. 

The tooling built going into the Studio held up under use. DevNotes are populated directly from logs adjacent to data stored in google drive. The other half of that pipeline, DevNote to Docs, also shipped: every Nucleus Docs page now carries a "Supported by" list of the DevNotes behind it, generated automatically rather than maintained by hand ({ref}`fig:week3-supported-by`).

:::{figure} assets/week3/week3-supported-by.png
:label: fig:week3-supported-by
:align: center
:width: 80%

The "Supported by" section on the pH detector's own Nucleus Docs page, naming the DevNote behind it automatically.
:::

This workflow was also deployed the following week with visitors who took part in discussions on the Developer Cell program and worked in the lab to reproduce Base Cell. Their validation DevNote demonstrates the pipeline end to end: [Build a Base Cell Validation](https://github.com/nucleus-eng/nucleus-devnote-archive-1/tree/main/devnotes/devstudio-validation-base-cell). The caveat worth naming plainly: the tools still took real effort from the maintainers to set up and hand off, and streamlining that remains a priority.