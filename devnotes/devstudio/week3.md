---
title: "Week 3, October 5 to 9"
---

Week 3 ran from Day 13 to Day 17. It closed two of the four demonstrations and left the other two where Week 2 found them. Most of the remaining week was module-level work rather than demonstration-level results.

The pH Sensing demonstration is complete, and every node on its figure is green ({ref}`pH Sensing <fig:week3-ph>`). The rerun on SUVs that Day 10 left unreported worked, which resolved the leaky CPRG carriers behind the ambiguous color of Day 8. The Chicago base membrane is now confirmed rather than assumed, closing a question that had been open since the first overlay.

The LuxR-GFP demonstration is also complete ({ref}`LuxR-GFP <fig:week3-ahl-lysate>`). Thursday's two-fold difference in gel with synthetic AHL was the first hard number of the sprint, but it was supernatant, the real analyte source the board draws, that had to work, and it did: the demonstration now senses AHL from bacterial supernatant end to end. Two renamings go with it. `(M11)` is renamed from Spectrometer to Plate Reader, since the lab reads this demonstration on a standard plate reader rather than the board's 3D-printed spectrometer. `(M12) UV lamp` is red, the first red node of the sprint, retired in the same swap rather than abandoned by failure.

The other two did not move on the figures ({ref}`aTc Sensor <fig:week3-atc>` and {ref}`CRAIC <fig:week3-craic>`). The aTc demonstration is still entirely orange, with leaky tetO expression the named cause. CRAIC deliberately held at an mNeonGreen proxy rather than advancing the real PLA1 construct, in order to chase a repressor noise floor on the microscope.

That last case shows a limit of this notation worth recording. The figure reads orange whether a team is advancing toward PLA1 or holding at GFP on purpose to debug detection, so good experimental judgment and lack of progress look identical. A module validation view would fix it, saying something closer to "EsaO/R: validated to GFP in cells, not PLA1, not gels", and it belongs in the module dependency layer rather than bolted onto these device figures.

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

## Where things stand

DevStudio set out to reproduce each Node's demonstration in a new laboratory and document it for reuse. Two demonstrations reached that bar. The pH Sensing demonstration is complete, and the LuxR-GFP demonstration is complete, sensing AHL from bacterial supernatant rather than only from synthetic AHL.

The other two each stop for a different reason, and the reasons are worth separating. The aTc demonstration has a named fault, leaky tetO expression, and a topology change in prospect, with LacZ possibly moving into its own vesicle population, which these graphs do not yet draw. CRAIC is held at a proxy on purpose while a repressor noise floor is chased on the microscope.

Four EsaO/R results from Days 6 to 8 remain unreported. Two open questions carry forward: whether the LuxR-GFP demonstration uses a plasmid or a linear template, and whether the PURE-containing vesicles from Day 9 belong on any figure at all. The spectrometer question is resolved: the demonstration is read on a standard plate reader, and the board's 3D-printed spectrometer is retired.

## Expected outputs

These tables update the ones on the Week 2 page, which stay as that week's record. Most of the DevNotes below were drafted on Saturday, October 11, the weekend immediately after Week 3 ended. This page counts that weekend as Week 3's output rather than holding the table to a hard Friday cutoff.

The real list is more finely split than Week 2's table expected. Where Week 2 named one DevNote per demonstration, several demonstrations produced two or more, each covering a specific sub-experiment rather than the whole cascade.

:::{table} DevNotes drafted during Week 3 and the weekend after.
:label: tbl:week3-devnotes
:align: center

| DevNote | Covers | Status |
| --- | --- | --- |
| Two Vesicle Colorimetric pH Sensor System | The pH Sensing demonstration | Draft exists |
| Bacterial Sensing in Hydrogel Embedded Synthetic Cells using LuxR Dependent Transcriptional Regulation | The LuxR-GFP demonstration, embedded in a gel | Draft exists |
| Implementing of a bulk color change module into bacterial quorum sensing | LuxR driving PLA1 to lyse a CPRG carrier, a bulk extension of the LuxR-GFP line | Draft exists |
| Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation | The EsaO/R detector, characterized on its own | Draft exists |
| GUV Encapsulation of a TetR/aTc-Inducible deGFP Cell-Free Sensor | The aTc Sensor demonstration, GUV form | Draft exists |
| Expressing Cell-Free TetO-GFP in Solution with aTc Titration | The aTc Sensor demonstration, solution-phase proxy work | Draft exists |
| TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning | The aTc Sensor demonstration, with PLA1 in place of the proxy | Draft exists |
| Triggered Lysis of beta-Galactosidase-Loaded GUVs by Cell-Free Expressed Phospholipase A1 | The aTc demonstration's PLA1 lysis step, on its own | Draft exists |
| Co-Encapsulated Cell-Free PLA1 Expression in beta-Galactosidase GUVs | The aTc demonstration's co-encapsulation variant | Draft exists |
| Understanding Liposome Behaviour in Hydrogel Matrices | Embedding tolerances across LGA, ULGA and PEG-NB | Draft exists, metadata incomplete |
| CRAIC demonstration | The CRAIC demonstration, end to end | Not started |
| Low cost spectrophotometer | Instrument build and characterization | Proposed |
:::

One further DevNote, "Double Vesicle Lysis System Leveraging deGFP CFPE," reached the board on October 22, well after this window. It continues the aTc and PLA1 line above and is left off this table because it belongs to a later week's record.

Documentation templates were drafted before DevStudio. This table was written against those templates; it is now checked against what actually landed on `nucleus-eng/nucleus-docs`, which arrived in two waves, one at the Week 3 boundary and a larger one three weeks later.

:::{table} Nucleus Docs pages expected from DevStudio, checked against nucleus-docs.
:label: tbl:week3-docs
:align: center

| Page | Kind | Status |
| --- | --- | --- |
| PLA1 Lysis | Module | Not yet published |
| EsaO/R-AHL detector | Module | Published, `detector-esar`, [nucleus-docs#303](https://github.com/nucleus-eng/nucleus-docs/pull/303) (Oct 26) |
| pH detector | Module | Published, `detector-ph`, [nucleus-docs#302](https://github.com/nucleus-eng/nucleus-docs/pull/302) (Oct 26) |
| tetO/R aTc detector | Module, update to an existing page | Updated, `detector-tetr-atc`, [nucleus-docs#284](https://github.com/nucleus-eng/nucleus-docs/pull/284) (Oct 12) |
| SUV preparation | Process | Not yet published as a generic process; the CPRG carrier's SUV form is in `substrate-cprg-suv`, [nucleus-docs#302](https://github.com/nucleus-eng/nucleus-docs/pull/302) (Oct 26) |
| LUV preparation | Process | Not yet published as a generic process; the CPRG carrier's LUV form is in `substrate-cprg-luv`, [nucleus-docs#302](https://github.com/nucleus-eng/nucleus-docs/pull/302) (Oct 26) |
| Embed cells in gels | Process | Published as two pages, `embed-photocrosslinking` and `embed-thermal-setting`, [nucleus-docs#283](https://github.com/nucleus-eng/nucleus-docs/pull/283) (Oct 26) |
| Gel: LGA | Specification | Published, `gel-lga`, [nucleus-docs#283](https://github.com/nucleus-eng/nucleus-docs/pull/283) (Oct 26) |
| Gel: ULGA | Specification | Published, `gel-ulga`, [nucleus-docs#283](https://github.com/nucleus-eng/nucleus-docs/pull/283) (Oct 26) |
| Gel: PEG-NB | Specification | Published, `gel-peg-nb`, [nucleus-docs#283](https://github.com/nucleus-eng/nucleus-docs/pull/283) (Oct 26) |
| CPRG color change | Process | Published, `colorimetric-readout`, [nucleus-docs#302](https://github.com/nucleus-eng/nucleus-docs/pull/302) (Oct 26) |
:::

Three gaps are real rather than administrative. PLA1 Lysis has no page: the module that the aTc and CRAIC demonstrations both depend on is still undocumented on Nucleus Docs. SUV preparation and LUV preparation also have no generic page; what exists instead is the CPRG carrier's own module spec in each form, which documents that one use rather than the general method a future demonstration could reuse.

The timing is worth naming plainly. Eight of these eleven pages arrived on October 26, three weeks after Week 3 ended, in three PRs: the gel Modules and embedding Processes together (`[nucleus-docs#283](https://github.com/nucleus-eng/nucleus-docs/pull/283)`), the pH demo corpus of seven Modules and four Processes (`[nucleus-docs#302](https://github.com/nucleus-eng/nucleus-docs/pull/302)`), and the EsaR Detector Module (`[nucleus-docs#303](https://github.com/nucleus-eng/nucleus-docs/pull/303)`). Only the tetR-aTc Detector update landed inside the Week 3 window itself, on October 12 (`[nucleus-docs#284](https://github.com/nucleus-eng/nucleus-docs/pull/284)`). Two further PRs on October 27 filled in detail on pages already published (`[nucleus-docs#327](https://github.com/nucleus-eng/nucleus-docs/pull/327)`, `[nucleus-docs#328](https://github.com/nucleus-eng/nucleus-docs/pull/328)`), and one more on November 10 tagged the pH corpus against its DevNote (`[nucleus-docs#330](https://github.com/nucleus-eng/nucleus-docs/pull/330)`).
