---
title: "Base Cell Validation, October 13"
---

Twelve labs reproduced the Build a Base Cell protocol at Nucleus Labs on October 13, during the [Developer Studio](https://devnotes.bnext.bio/devstudio) Capstone event. Visiting PIs and their trainees ran the protocol from the published Nucleus Docs page, not from an internal method. This DevNote records that one-off validation session on its own, separate from Developer Studio's weekly record.

Documentation referenced:

- Process protocol: [Build a Base Cell](https://docs.nucleus.engineering/docs/processes/build-base-cell/main/)
- Base cytosol specification: [Base Cytosol](https://docs.nucleus.engineering/docs/modules/base-cytosol/spec/)

## Results

The plate held 11 wells, one or two per guest, imaged over 9 timepoints. Every well carries the same reporter construct, pOpen-T7-deGFP, 2812 bp, circular, from [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk).

:::{seqviz} assets/pOpen-deGFP.gbk
:height: 400px
:::

:::{table} Wells, one or two per guest. Cytosol, DNA, and membrane were the same across the plate: Nucleus Cytosol, pT7-deGFP, 3:1 POPC:Chol.
:label: tbl:validation-platemap
:align: center

| Well | Person |
| --- | --- |
| D5 | Surendra Yadav |
| D6 | Neha Kamat |
| D7 | Andrew Ellington |
| D8 | Becky Pferdehirt |
| D9 | Richard Murray |
| E5 | Leopold Green |
| E6 | Michael Booth |
| E7 | Michael Booth |
| E8 | Michael Clear |
| E9 | Michael Clear |
| E10 | Claudia Contini |
:::

The full-resolution microscopy dataset is available at [data.nucleus.engineering](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/20261013-devstudio-liposomes-timeseries_2026-10-13_12-07-24.011026.zarr&viewState={%22target%22:[40038,13346],%22zoom%22:-5.636237316232194}).

### Population summary

:::{figure} assets/fogplot-compare-0.png
:label: fig-validation-fogplot-compare
:align: center
:width: 90%

Per-well GFP distributions compared directly against each other. Produced by {download}`fogplot-compare.ipynb <assets/fogplot-compare.ipynb>`, a trimmed extract of the session's full analysis notebook keeping only the cells behind this figure. Segmented data is available at [data.nucleus.engineering](https://data.nucleus.engineering/microscopy/nucleus-bnext-01/20261013-devstudio-liposomes-timeseries_2026-10-13_12-07-24.011026.parquet).
:::

## Discussion

### Did the protocol work as written?

- **Claudia Contini:** Everything worked as expected.
- **Michael Booth:** Instead of the 5 µL of water at the end, added 1 µL extra of ribosomes and 4 µL of water. Otherwise, the protocol worked very well and was clear, with Surendra Yadav also showing the steps.
- **Michael Clear:** Too much of the aqueous phase was still present before resuspending the pellet. About 100 µL of solution was left at the time of resuspension.

### What was unclear or missing?

- **Claudia Contini:** Adding 20 µL of lipid-oil solution on top of glucose.
- **Michael Clear:** Some lack of clarity around the lipid removal step after centrifugation. The general approach was clear, but it was not optimized for concentration.

## Participants

- Surendra Yadav, b.next, well D5
- Neha Kamat, Northwestern University, well D6
- Andrew Ellington, University of Texas at Austin, well D7
- Becky Pferdehirt, Astera Institute, well D8
- Richard Murray, Schmidt Sciences, well D9
- Leopold Green, Purdue University, well E5
- Michael Booth, University College London, wells E6 and E7
- Michael Clear, Schmidt Sciences, wells E8 and E9
- Claudia Contini, Imperial College London, well E10

## Acknowledgments

Thank you to Yen-Yu Hsu (b.next) and Surendra Yadav (b.next) for serving as TAs at this session.
