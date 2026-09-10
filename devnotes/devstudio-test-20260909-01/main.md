---
# Ensure that this title is the same as the one in `curvenote.yml`
title: "nucleus_cytosol_v05 (draft)"
abstract: |
  REVIEW: Abstract not present in the source DevNote(G) draft — add before publishing.
---

<!-- STYLE: abstract moved from a "## Abstract" body section (as it appeared in the DevNote(G) draft) into frontmatter, matching real archive convention (e.g. devnotes/10-nucleus_cytosol_v05/main.md) rather than left as a body section. -->

# Overview

REVIEW: Overview not present in the source DevNote(G) draft — add before publishing.

<!-- STYLE: non-standard section heading "Experiment 1: ..." / "Experiment 2: ..." — preserved per participant intent. The source DevNote(G) draft is organized by experiment rather than the flat Materials/Design/Protocol/Results structure this transform otherwise expects (see devstudio-devnote-g-to-devnote-m Step 2); no forced remapping attempted since both experiments are genuinely distinct, sequential mastermix/dose-response studies, not stages of one protocol. -->

The `pOpen-deGFP` construct used throughout both experiments below is shown here. Length verified at 2812 bp against the GenBank file attached to the source Drive folder — see `devstudio-verify-dna-constructs` check in the upstream figure-provenance manifest.

<!-- REVIEW: the canonical nucleus-eng/DNA copy of this construct (reporters/pOpen-deGFP.gbk) records its own LOCUS name as "pOpen-T7-deGFP", not "pOpen-deGFP" — lengths match exactly (2812 bp) so this is very likely the same construct under a slightly different internal name, but TA should confirm before treating them as interchangeable. -->

::::{figure}
:label: seq-degfp

:::{seqviz} ./plasmids/pOpen-deGFP.gb
:height: 400px
:::

Plasmid map of `pOpen-deGFP`.
::::

# Experiment 1: pOpen-deGFP expression in Nucleus Cytosol and PURExpress

*Source: LOG-sy-20251104 (2025-11-04)*

To test and compare the activity of Nucleus Cytosol, we expressed the pOpen-deGFP construct in both Nucleus Cytosol and PURExpress.

Five reactions were set up to test the activity:

1. Nucleus Cytosol (Pmix 08-02) + pOpen-deGFP (maxiprep + ethanol precipitation)
2. Nucleus Cytosol (Pmix 08-02) + pOpen-deGFP (maxiprep only)
3. Nucleus Cytosol (Pmix 08-02) without pOpen-deGFP template—*Negative Control*
4. PURExpress + pOpen-deGFP (maxiprep + ethanol precipitation)
5. PURExpress + pOpen-deGFP (maxiprep only)

The reaction setup for each condition is provided below. We prepared 35 μL of mastermix for each reaction and aliquoted 3 × 10 μL into a 384-well plate for fluorescence measurement.

## Reagents

<!-- REVIEW: these are per-condition reaction-composition tables (six-column schema per devstudio-author-myst-content: Component | Input concentration | Unit | Final concentration | Unit | Volume), not the seven-column Reagents/BOM schema (Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link) that devstudio-devnote-g-to-devnote-m's Step 3 otherwise assumes for a "Reagents" section — no product/vendor/catalog information was present in the source log, so the BOM schema does not apply here and was not forced onto this data. Vale magnitude-unit-spacing suppression is not needed either, since these cells are concentrations, not catalog numbers. -->

<!-- REVIEW: every condition table below was rendered in the source Word document as a single merged-cell table combining the reagent list, a "Total volume" row, and a "Calculation for DNA concentration" sub-block; already consolidated into a clean "Total volume" row plus a DNA-length/MW note at the DevNote(G) stage — no numeric value was altered or dropped, only a duplicate merged-cell rendering artifact. -->

:::::{tab-set}

::::{tab-item} Cytosol + pOpen-deGFP (maxi+EtOH)
:::{table} Nucleus Cytosol (Pmix 08-02) + pOpen-deGFP (maxiprep + ethanol precipitation)
:label: tbl-exp1-cond1
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 35 | mg/ml | 3.5 | mg/ml | 3.50 |
| Mg-Acetate | 200 | mM | 8 | mM | 1.40 |
| Water | — | — | — | — | 10.02 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} Cytosol + pOpen-deGFP (maxi only)
:::{table} Nucleus Cytosol (Pmix 08-02) + pOpen-deGFP (maxiprep only)
:label: tbl-exp1-cond2
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 155 | ng/µL | 3 | nM | 1.24 |
| Nucleus tRNA | 35 | mg/ml | 3.5 | mg/ml | 3.50 |
| Mg-Acetate | 200 | mM | 8 | mM | 1.40 |
| Water | — | — | — | — | 9.61 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} Cytosol, no DNA (negative control)
:::{table} Nucleus Cytosol (Pmix 08-02) without pOpen-deGFP template—Negative Control
:label: tbl-exp1-cond3
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 115 | ng/µL | 0 | nM | 0.00 |
| Nucleus tRNA | 35 | mg/ml | 3.5 | mg/ml | 3.50 |
| Mg-Acetate | 200 | mM | 8 | mM | 1.40 |
| Water | — | — | — | — | 10.85 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} PURExpress (maxi+EtOH)
:::{table} PURExpress + pOpen-deGFP (maxiprep + ethanol precipitation)
:label: tbl-exp1-cond4
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| SolA | 2.50 | × | 1 | × | 14.00 |
| Sol B | 8 | mg/mL | 2.40 | mg/mL | 10.50 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Water | — | — | — | — | 9.67 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} PURExpress (maxi only)
:::{table} PURExpress + pOpen-deGFP (maxiprep only)
:label: tbl-exp1-cond5
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| SolA | 2.50 | × | 1 | × | 14.00 |
| Sol B | 8 | mg/mL | 2.40 | mg/mL | 10.50 |
| pOpen-deGFP DNA | 155 | ng/µL | 3 | nM | 1.24 |
| Water | — | — | — | — | 9.26 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

:::::

## Results

:::::{tab-set}

::::{tab-item} Time series
:sync: exp1-results
:::{figure} #fig:kinetics-exp1
:name: fig-kinetics-exp1
:align: center
:width: 75%
REVIEW: caption placeholder — source DevNote(G) draft carried only the bare label "Kinetics", not a full caption sentence. Fluorescence over time, by condition.
:::
::::

::::{tab-item} End point
:sync: exp1-results
:::{figure} #fig:endpoint-exp1
:name: fig-endpoint-exp1
:align: center
:width: 75%
REVIEW: caption placeholder — source DevNote(G) draft carried only the bare label "Steady state", not a full caption sentence. Endpoint fluorescence, by condition.
:::
::::

:::::

# Experiment 2: Mg2+ sweep in Nucleus Cytosol

*Source: LOG-sy-20251107 (2025-11-07)*

To optimize protein expression yield in Nucleus Cytosol, we performed a Mg-acetate titration across a range of 4–12 mM in 2 mM increments. The reaction setup for each condition is provided below. We prepared 35 μL of mastermix for each reaction and aliquoted 3 × 10 μL into a 384-well plate for fluorescence measurement. All subsequent experiments used maxiprepped pOpen-deGFP cleaned up with ethanol precipitation.

## Reagents

:::::{tab-set}

::::{tab-item} 4 mM
:::{table} 4 mM Mg-Acetate
:label: tbl-exp2-cond1
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 29.6 | mg/ml | 3.5 | mg/ml | 4.14 |
| Mg-Acetate | 200 | mM | 4 | mM | 0.70 |
| Water | — | — | — | — | 10.08 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} 6 mM
:::{table} 6 mM Mg-Acetate
:label: tbl-exp2-cond2
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 29.6 | mg/ml | 3.5 | mg/ml | 4.14 |
| Mg-Acetate | 200 | mM | 6 | mM | 1.05 |
| Water | — | — | — | — | 9.73 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} 8 mM
:::{table} 8 mM Mg-Acetate
:label: tbl-exp2-cond3
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 29.6 | mg/ml | 3.5 | mg/ml | 4.14 |
| Mg-Acetate | 200 | mM | 8 | mM | 1.40 |
| Water | — | — | — | — | 9.38 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} 10 mM
:::{table} 10 mM Mg-Acetate
:label: tbl-exp2-cond4
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 29.6 | mg/ml | 3.5 | mg/ml | 4.14 |
| Mg-Acetate | 200 | mM | 10 | mM | 1.75 |
| Water | — | — | — | — | 9.03 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} 12 mM
:::{table} 12 mM Mg-Acetate
:label: tbl-exp2-cond5
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Nucleus tRNA | 29.6 | mg/ml | 3.5 | mg/ml | 4.14 |
| Mg-Acetate | 200 | mM | 12 | mM | 2.10 |
| Water | — | — | — | — | 8.68 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

::::{tab-item} PURExpress control
:::{table} PURExpress Positive Control
:label: tbl-exp2-cond6
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| SolA | 2.50 | × | 1 | × | 14.00 |
| Sol B | 8 | mg/mL | 2.40 | mg/mL | 10.50 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Water | — | — | — | — | 9.67 |
| Total volume [µL] | — | — | — | — | 35 |
:::
pOpen-deGFP DNA length: 2812 bp; avg. MW of bp: 650 g/mol.
::::

:::::

## Results

:::::{tab-set}

::::{tab-item} Time series
:sync: exp2-results
:::{figure} #fig:kinetics-exp2
:name: fig-kinetics-exp2
:align: center
:width: 75%
REVIEW: caption placeholder — source DevNote(G) draft carried only the bare label "Kinetics", not a full caption sentence. Fluorescence over time, by Mg2+ condition.
:::
::::

::::{tab-item} End point
:sync: exp2-results
:::{figure} #fig:endpoint-exp2
:name: fig-endpoint-exp2
:align: center
:width: 75%
REVIEW: caption placeholder — source DevNote(G) draft carried only the bare label "Steady state", not a full caption sentence. Endpoint fluorescence, by Mg2+ condition.
:::
::::

:::::

# Conclusions

REVIEW: Conclusions not present in the source DevNote(G) draft — add before publishing.
