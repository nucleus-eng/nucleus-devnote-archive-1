---
title: "Testing Integration of a TetR Biosensor with a Toehold Exchange Riboregulator in Developer Cells with Nucleus Cytosol"
subtitle: "CSHL Synthetic Biology 2026"
---

<!--
TODO before this DevNote is publish-ready. See the PR description for the
full ingest notes.

1. The Google Docs comment thread on the source draft resolved most open
   placeholders (emission wavelengths, the TetR/aTc link, the aTc
   photobleaching citation, and the toehold exchange riboregulator
   citations). The thread's open question about the CSHL week 2 course
   attendees is resolved too. They are credited as the "CSHL Week 2
   Participants" author entry (curvenote.yml). They are also named in the
   Participants section below. This is the same hybrid pattern used by
   `devcells-kickoff-workshop`. The "automated image analysis" reference is
   resolved too, now linked to the nucleus-cdk source repository. The
   DevCell imaging plate question is resolved too: it is the same
   384-well glass bottom plate already in the Bill of Materials, confirmed
   against the Nucleus materials reference and linked there.

   Every open item from the comment thread is now resolved.
2. Figures 3 and 5 are the screenshot-resolution representative microscopy
   images the authors embedded in the Word draft. No notebook generates
   these, since they are raw images, not plots. Higher-resolution source
   material exists for them and this ingest did not substitute it
   automatically.
   - `resources/figure-3-and-5-panels.pptx` holds the authors' composed
     panels for Figures 3 and 5. This file is a candidate higher-resolution
     source.
   Figures 4, 6, 7, and 8 are quantification plots. They are now embedded
   live from the matching notebook cell (tagged `#| label: ...`, following
   the `module-Clpxp-Cells` pattern), not static images. The source does not
   state the mapping from cell to figure explicitly. This ingest matched
   each cell's condition list against the figure caption instead, and
   confirmed the match against the rendered preview (cell counts, n-values,
   and condition sets line up). Confirm it with the authors before you
   treat it as final.
3. The source draft had a trailing section ("Log / Experiment") that
   described an unrelated Cytosol pre-incubation lifetime experiment with
   empty Observation and Claim placeholders. This ingest dropped the
   section as out of scope for this DevNote, confirmed with the submitter.
4. The source Bill of Materials and reagent tables list catalog numbers
   and prices from the course date. Confirm they are still current before
   you publish.
5. Live interactive execution of the three analysis notebooks now works in
   Curvenote's live-compute kernel. Five issues blocked it, now fixed:
   - A dead `google.colab` import.
   - A missing `pyarrow` engine for `pd.read_parquet`.
   - `environment.yml`'s unpinned `scipy` line resolved to a version whose
     `dask` call chain raised a `TypeError` over `xp_capabilities()`. Pinned
     to `scipy=1.16.3` in `environment.yml`.
   - `nucleus-cdk` installed to the `--user` site directory
     (`/home/jovyan/.local/lib/python3.14/site-packages`). The kernel did
     not put that directory on `sys.path` for `importlib.metadata`
     lookups. The version assertion then raised `PackageNotFoundError`,
     even though the package was present on disk. Fixed by inserting
     `site.getusersitepackages()` into `sys.path` explicitly in each
     notebook's first cell, before the assertion.
   - The `scipy=1.16.3` pin did not stop the `xp_capabilities()` error.
     Each notebook had a second cell that force-reinstalled or upgraded
     `scipy` (along with `wasmtime` and `itkwasm`) to unpinned latest
     versions. This overrode the `environment.yml` pin at run time. The
     error surfaced only on the first figure across the three notebooks,
     not on every one. This fits a package getting reinstalled under an
     already-running kernel. Parts of `scipy` stay cached from an earlier
     import. Other parts load fresh from the reinstall. The two versions
     then disagree on `xp_capabilities()`'s signature. `nucleus-cdk`
     already pulls in compatible versions of `scipy`, `wasmtime`, and
     `itkwasm` as its own dependencies. A live pip log from this ingest
     confirmed this. This ingest removed the override line from all three
     notebooks, keeping only the `cdk.analysis.cell.microscopy` import it
     guarded. Not yet confirmed against a live run.
-->

:::{note}
This DevNote presents preliminary results from the
[2026 CSHL Synthetic Biology Summer Course](https://meetings.cshl.edu/courses.aspx?course=C-SYNBIO).
It is not a complete peer-reviewed research output.
:::

# Overview

Through the 2026 CSHL Synthetic Biology Summer Course, the students,
instructors, and teaching assistants helped optimize an anhyrotetracycline
(aTc) sensor, which uses a toehold exchange (THE) riboregulator RNA circuit
derepressed in the presence of aTc via the TetR transcription factor. This
aTc sensor was first optimized in bulk cell-free expression reactions using
PURExpress. The unregulated toehold exchange riboregulator circuit and the
full aTc sensing circuit were then tested in Developer Cells (DevCells), an encapsulated cell-free
expression system.

# Bill of Materials

:::{table} Reagents and materials
:label: tbl-bom
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| CPRG | Chlorophenol red-β-D-galactopyranoside | Roche | 10884308001 | $160 | -20 °C in water at 10 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| Cytosol (SMix, PMix, ribosomes, tRNA) | b.next | b.next | — | — | -80 °C | — |
| PURExpress | NEB PURExpress in vitro protein synthesis kit | New England Biolabs | E6800S | $307.00 | -80 °C | [link](https://www.neb.com/en-us/products/protein-expression/cell-free-protein-expression/purexpress) |
| aTc | Anhydrotetracycline hydrochloride | Sigma-Aldrich | 37919-100MG-R | $275.00 | Room temp | [link](https://www.sigmaaldrich.com/US/en/product/sial/37919) |
| RNase Inhibitor | RNase Inhibitor, Murine | New England Biolabs | M0314L | $347.00 | -20 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Lipid-in-Oil Kit | 16:0-18:1 PC (POPC) + Cholesterol + Cy5.5 | b.next | Composition in {ref}`tbl-membrane` | — | 4 °C | — |
| Optiprep | Optiprep | Serumwerk Bernburg | 1893 | — | Room temp | — |
| Glucose | D-(+)-Glucose, 99.5% | Sigma-Aldrich | G8270-1KG | — | Room temp | — |
| Nuclease-free water | Nuclease-free water | ThermoFisher Scientific | AM9916 | — | Room temp | — |
| 384-well glass bottom plates | 384-well glass bottom plate, 1.5 cover glass | Cellvis | P384-1.5H-N | $423.00 | Room temp | [link](https://www.cellvis.com/_384-well-glass-bottom-plate-with-high-performance-number-1.5-cover-glass_/product_detail.php?product_id=53) |
| Optical Adhesive Film | MicroAmp Optical Adhesive Film | ThermoFisher Scientific | 4311971 | — | Room temp | — |
| Osmometer | Freezing-point osmometer | Advanced Micro-Osmometer | Model 3300 | — | Room temp | — |
| PCR tubes | Thin-walled, RNase-free PCR tubes | ThermoFisher Scientific | AM12225 | — | Room temp | — |
:::

## DNA templates and sequences

DNA templates for the full toehold exchange (THE) riboregulator transcription
(TX) unit. **Bold** sequences indicate promoters. <u>Underlined</u> sequences
indicate the regions amplified using the specified primers. *Italic* sequences
indicate terminators. Annotated sequence maps are available on
[Benchling](https://benchling.com/sschafft1/f_/mW2x3M1k3j-toehold-exchange-riboregulator-published-sequences/).
Sequence files in GenBank format are included in `sequences/`.

:::{table} Primers
:label: tbl-primers
:align: center

| Name | Sequence (5' to 3') | Purpose |
| --- | --- | --- |
| T7fwd | TTCTAATACGACTCACTATAGGGAG | Forward primer for T7 promoter (used in all PCRs except `IN_1_TetR`) |
| fwd_U1 | CATTACTCGCATCCATTCTCAGG | Forward primer for `IN_1_TetR` PCR |
| T7rev | CAAAAAACCCCTCAAGACCCGTTTAG | Reverse primer for T7t terminator (For Gate / riboregulator template PCRs) |
| rev_Ux | GGTGGAAGGGCTCGGAGTTG | Reverse primer for `IN_1_TetR` PCR |
| Thyb10rev | AAAAAAAAACAGATAGCCGCGCGAAC | Reverse primer for Thyb10 terminator (For Input template PCRs) |
:::

:::{table} DNA templates
:label: tbl-templates
:align: center

| Name | Sequence (5' to 3') | Purpose |
| --- | --- | --- |
| `Io` | <span style="font-family: monospace;">gaagtctaacgctgctctgggctaactgtcCATTACTCGC<wbr>ATCCATTCTCAGGCTGTCTCGTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAATCAATAACACACATA*ataatcAGATAACAGATACttcgGtatctgttatctgttT<wbr>TTTTTcAACAGATAGCCGCGttcgCGCGGCtatctgttTT<wbr>TTTTt*</u>agctgtcaccggatgtgctttccggtctgatgagtccgtg<wbr>aggacgaaacagcctcCCAGGATACATAGATTACCACAAC<wbr>TCCGAGCCCTTCCACC</span> | Non-complementary input; minimum expression (OFF). Plasmid map: {ref}`seq-io`. |
| `IN_1` | <span style="font-family: monospace;">gaagtctaacgctgctctgggctaactgtcCATTACTCGC<wbr>ATCCATTCTCAGGCTGTCTCGTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAAATACTTAATACAAAATAATCAC<wbr>TTCACAACATCA*ataatcAGATAACAGATACttcgGtatctgttatctgttT<wbr>TTTTTcAACAGATAGCCGCGttcgCGCGGCtatctgttTT<wbr>TTTTt*</u>agctgtcaccggatgtgctttccggtctgatgagtccgtg<wbr>aggacgaaacagcctcCCAGGATACATAGATTACCACAAC<wbr>TCCGAGCCCTTCCACC</span> | Complementary input with maximum translation rate; maximum expression (ON). Plasmid map: {ref}`seq-in1`. |
| `IN_1_TetR` | <span style="font-family: monospace;"><u>CATTACTCGCATCCATTCTCAGGCTGTCTCGTCTCGTCTC<wbr>TTC**TAATACGACTCACTATA**GGTCCCTATCAGTGATAGAGACCAAATACTTAATACAAAA<wbr>TAATCACTTCACAACATCA*ataatcAGATAACAGATACttcgGtatctgttatctgttT<wbr>TTTTTcAACAGATAGCCGCGttcgCGCGGCtatctgttTT<wbr>TTTTt*CCAGGATACATAGATTACCACAACTCCGAGCCCTTCCACC</u>actgtgtacttgttataacatctgacagttaaagtcggga<wbr>gaataggagccgcaat</span> | DNA template with the TetR operator sequence downstream of the T7 promoter. Plasmid map: {ref}`seq-in1-tetr`. |
| `G_1 sCFP3A` | see {ref}`seq-g1-scfp3a` | Toehold exchange riboregulator that controls cyan fluorescent protein (CFP) expression in response to `IN_1` |
| `G_1 sfGFP` | see {ref}`seq-g1-sfgfp` | Toehold exchange riboregulator that controls green fluorescent protein (GFP) expression in response to `IN_1` |
| `T7p_TetR` | see {ref}`seq-pt7-tetr` | DNA template for T7-driven expression of TetR |
| `pOpen-deGFP` | see [pOpen-deGFP.gbk](https://github.com/nucleus-eng/DNA/blob/54a07a3d65edc1a348a462cff170dd17d11f26c6/reporters/pOpen-deGFP.gbk) | DevCell encapsulation control plasmid. Module documentation: [docs.nucleus.engineering/docs/modules/reporter-degfp/spec](https://docs.nucleus.engineering/docs/modules/reporter-degfp/spec/) |
:::

The full-length `G_1 sCFP3A`, `G_1 sfGFP`, and `T7p_TetR` sequences are long and are
provided verbatim as GenBank files in `sequences/` rather than inline. Plasmid
maps for all six constructs are shown below.

::::::{tab-set}

:::::{tab-item} Io
::::{figure}
:label: seq-io
:::{seqviz} ./sequences/Io.gb
:height: 500px
:::
Plasmid map of `Io`, the non-complementary input (OFF).
::::
:::::

:::::{tab-item} IN_1
::::{figure}
:label: seq-in1
:::{seqviz} ./sequences/IN_1.gb
:height: 500px
:::
Plasmid map of `IN_1`, the complementary input (ON).
::::
:::::

:::::{tab-item} IN_1_TetR
::::{figure}
:label: seq-in1-tetr
:::{seqviz} ./sequences/IN_1_TetR.gb
:height: 500px
:::
Plasmid map of `IN_1_TetR`, the TetR-regulated input.
::::
:::::

:::::{tab-item} G_1 sCFP3A
::::{figure}
:label: seq-g1-scfp3a
:::{seqviz} ./sequences/G_1-sCFP3A.gb
:height: 500px
:::
Plasmid map of `G_1 sCFP3A`, the CFP-reporting gate.
::::
:::::

:::::{tab-item} G_1 sfGFP
::::{figure}
:label: seq-g1-sfgfp
:::{seqviz} ./sequences/G_1-sfGFP.gb
:height: 500px
:::
Plasmid map of `G_1 sfGFP`, the GFP-reporting gate.
::::
:::::

:::::{tab-item} T7p_TetR
::::{figure}
:label: seq-pt7-tetr
:::{seqviz} ./sequences/pT7_TetR.gb
:height: 500px
:::
Plasmid map of `T7p_TetR`, the TetR expression template.
::::
:::::

::::::

# Design

The mechanistic details of how toehold exchange riboregulators work are
described in another DevNote:
[devnotes.nucleus.engineering/articles/ss-20260712](https://devnotes.nucleus.engineering/articles/ss-20260712).

The mechanistic details of TetR repression of transcription and derepression
of transcription in response to aTc are described in the Nucleus
documentation:
[docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/).

Key design notes for toehold exchange riboregulators are described in another
DevNote:
[devnotes.nucleus.engineering/articles/ss-20260712](https://devnotes.nucleus.engineering/articles/ss-20260712).

The sequences for the toehold exchange riboregulators are based on those
discussed in the following publication:
[biorxiv.org/content/10.1101/2025.09.25.678518v2](https://www.biorxiv.org/content/10.1101/2025.09.25.678518v2.abstract).

The sequences were generated using the ctRSD and THE riboregulator sequence
compiler:
- Documentation: [ctrsd-simulator.readthedocs.io/en/latest/SeqCompiler.html](https://ctrsd-simulator.readthedocs.io/en/latest/SeqCompiler.html)
- Colab: [colab.research.google.com/drive/1Bd-ZugIWnc7PMiFkpaia_UnWA24KF3Mv](https://colab.research.google.com/drive/1Bd-ZugIWnc7PMiFkpaia_UnWA24KF3Mv?usp=sharing)

# Protocol

- Linear DNA templates for the circuit were prepared as described in a
  previous DevNote:
  [devnotes.nucleus.engineering/articles/ss-20260712](https://devnotes.nucleus.engineering/articles/ss-20260712).
- The protocol follows the CSHL Synthetic Biology 2026 - Nucleus Base Cell
  protocol:
  [docs.nucleus.engineering/docs/processes/build-base-cell/main](https://docs.nucleus.engineering/docs/processes/build-base-cell/main/).
  - With respect to DevCell preparation, the protocol did not deviate from
    the Nucleus protocol, other than the outer solution osmolarity, which
    was 1050 mmol/kg here.
  - The Cytosol reaction setup table shows the concentrations and volumes
    used for each of the samples. The Membrane composition and Outer
    solution tables show the mixtures used to prepare the DevCells.
  - For DevCell experiments that included TetR, TetR was expressed in a
    bulk reaction of Nucleus Cytosol using 4 nM of linear `T7_TetR` template
    ({ref}`seq-pt7-tetr`).
    The reaction was incubated at 37 °C for at least 3 h.
  - This TetR-enriched cytosol was then mixed at a 1:4.56 volume ratio with
    fresh Nucleus Cytosol containing the circuit DNA templates, which was
    then encapsulated.
- After encapsulation, a 50 µL volume of DevCells for each sample was
  transferred to a 384-well glass bottom plate ({ref}`tbl-bom`; see also the
  [Nucleus materials reference](https://docs.nucleus.engineering/guides/materials-reference/)).
  Each sample was sufficiently diluted to
  prevent overcrowding of DevCells in the imaging wells. After initial
  imaging, the samples were incubated at 37 °C for 1.5 h or 2 h in a
  benchtop incubator before the first post-incubation imaging.
- After this first image, the samples were returned to the incubator and
  incubated at 37 °C for another 3 h before taking a final image.
- Imaging was conducted on a Cephla Squid fluorescence microscope with a 20x
  air objective (Olympus).
  - Green fluorescent protein (GFP) was imaged at 488 nm excitation. The
    DevCell membranes, which were labeled with Cy5.5, were imaged at 638 nm
    excitation. The microscope camera has no emission filter, so emission
    was captured as the integration of all wavelengths. For both
    fluorescence channels, the exposure times and excitation laser
    intensities were kept constant across all conditions within each
    experiment. Specific exposure time varied between experiments, depending
    on excitation laser power, to provide sufficient contrast across all
    samples.
  - For each sample, the entire area of the well was captured with 25
    non-overlapping images at each time point, and all images were used for
    analysis and quantification.
  - This microscope did not have onboard temperature control, which is why
    the DevCells were incubated in a benchtop incubator and imaged at only a
    few time points.
- Automated image analysis of DevCell intensities was conducted using the
  [Nucleus Cell Development Kit](https://github.com/nucleus-eng/nucleus)
  (nucleus-cdk), software developed by b.next for Nucleus.

## Cytosol reaction setup table

The last four columns indicate the volumes of each reagent to add for the
four different samples tested, for encapsulating cell-free reactions in
DevCells. These samples are detailed in {ref}`fig2`.

:::{table} Cytosol reaction setup
:label: tbl-cytosol-reaction

| Component                                                                                          | Stock Concentration | Final Concentration | Negative Control Volume (µL) | Positive Control Volume (µL) | EXP OFF Volume (µL) | EXP ON Volume (µL) |
| -------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | ---------------------------- | ---------------------------- | ------------------- | ------------------ |
| SMix                                                                                               | 3.33x               | 1.09x               | 7.2                          | 7.2                          | 7.2                 | 7.2                |
| PMix                                                                                               | 15 mg/mL            | 0.95 mg/mL          | 1.4                          | 1.4                          | 1.4                 | 1.4                |
| Ribosomes                                                                                          | 10 µM               | 0.36 µM             | 0.8                          | 0.8                          | 0.8                 | 0.8                |
| tRNA                                                                                               | 35 mg/mL            | 3.5 mg/mL           | 2.4                          | 2.4                          | 2.4                 | 2.4                |
| DNA template for Gate (`G_1 GFP`, {ref}`seq-g1-sfgfp`)                                             | 100 nM              | 2 nM                | 0.44                         | 0.44                         | 0.44                | 0.44               |
| DNA template for complementary input (`IN_1`, {ref}`seq-in1`, or `IN_1_TetR`, {ref}`seq-in1-tetr`) | 100 nM              | 18 nM               | 0                            | 3.96                         | 3.96                | 3.96               |
| Non-complementary input DNA (`Io`, {ref}`seq-io`)                                                  | 100 nM              | 18 nM               | 3.96                         | 0                            | 0                   | 0                  |
| TetR-enriched cytosol                                                                              | 1x                  | 0.215x              | 0                            | 0                            | 4.73                | 4.73               |
| RNase Inhibitor                                                                                    | 40 000 U/mL         | 2000 U/mL           | 1.4                          | 1.4                          | 1.4                 | 1.4                |
| Opti-Prep                                                                                          | —                   | 3.6%                | 0.8                          | 0.8                          | 0.8                 | 0.8                |
| Water                                                                                              | —                   | —                   | 4.77                         | 4.77                         | 0                   | 0                  |
:::

## Membrane composition table

:::{table} Membrane composition
:label: tbl-membrane
:align: center

| Lipid | Target Percentage % | Molecular Weight | Concentration (mg/mL) | Volume to Add (µL) |
| --- | --- | --- | --- | --- |
| 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine (POPC) | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| Cy5.5 | 0.05 | 1366.32 | 1 | 4 |
:::

## Outer solution table

:::{table} Outer solution
:label: tbl-outer-solution
:align: center

| Component | Concentration |
| --- | --- |
| Glucose | 1050 mM (for Nucleus Cytosol) or 870 mM (for NEB PURExpress) |
:::

# Results and Observations

Building on a [previous DevNote](https://devnotes.nucleus.engineering/articles/ss-20260712)
and [bulk cell-free expression experiments](https://www.biorxiv.org/content/10.1101/2025.09.25.678518v3.abstract)
([Piorino *et al.* 2025](https://www.biorxiv.org/content/10.1101/2025.09.25.678518v3.abstract)),
we sought to test toehold exchange riboregulators
([Piorino *et al.* 2025](https://www.biorxiv.org/content/10.1101/2025.09.25.678518v2.abstract),
[Schaffter *et al.* 2025](https://www.biorxiv.org/content/10.1101/2025.09.24.678369v1.abstract))
and small molecule biosensors in DevCells. We first validated that the coupling of a TetR-based biosensor
and the toehold exchange riboregulators worked in bulk cell-free expression
({ref}`fig1`). Due to constraints on the available fluorescence channels on the
microscopes available at the course, we had to switch from CFP expression in
bulk reactions to GFP expression in the DevCell reactions. Although we do not
expect this change to dramatically change system behavior, a detailed
comparison would be warranted in a future study. {ref}`fig2` shows the
schematics of the different systems we encapsulated in DevCells for testing.
In DevCells, we initially tested the same concentrations of Input template
and Gate template that we used in the bulk cell-free experiments, but we did
not observe much difference in expression levels between positive and
negative controls ({ref}`fig3`, {ref}`fig4`), which contained the unregulated toehold
exchange riboregulator circuit ({ref}`fig2`). We hypothesized that this might be
because we were using multiple templates and perhaps many of the DevCells did
not contain high enough concentrations of both templates. Thus, we retried
the experiment and increased the Input template concentration to 10-fold of
the Gate template. In microscope images, there were clearly many bright
DevCells in the positive control samples ({ref}`fig5`), suggesting that this
optimized ratio worked better. However, image analysis that quantified the
average intensity of the DevCells revealed little difference between the
positive and negative controls. There was just a much higher fraction of
highly fluorescent outliers in the positive control samples ({ref}`fig6`,
{ref}`fig7`, {ref}`fig8`),
which may suggest that only a small percentage of the DevCells received
enough of both the Input and Gate templates to activate protein expression.
In the experimental samples, in which TetR and aTc were included, we were
unable to assess whether the system worked because aTc exhibited a strong
fluorescence signal in the GFP channel ({ref}`fig3`, {ref}`fig5`, {ref}`fig7`).

:::{figure} ./figures/figure1-bulk-plate-reader.png
:label: fig1
:align: center
:width: 90%
Overview of system (**A**) and bulk plate reader results (**B**).
Experiments were conducted in PURExpress at 37 °C as described in the
[following DevNote](https://devnotes.nucleus.engineering/articles/ss-20260712)
with the following conditions: 2 nM of `G_1` template ({ref}`seq-g1-scfp3a`), 4 nM
of `IN_1` template ({ref}`seq-in1`) or `Io` template ({ref}`seq-io`), and 4 nM of
TetR template ({ref}`seq-pt7-tetr`). The plot shows
the mean CFP signal of three technical replicates, with the shaded regions
indicating the standard deviation of the mean.
:::

:::{figure} ./figures/figure2-devcell-schematics.png
:label: fig2
:align: center
:width: 90%
Overview of different systems encapsulated and tested in DevCells. The
negative and positive controls used input templates (`Io`, {ref}`seq-io`, or
`IN_1`, {ref}`seq-in1`) that did
not contain the TetR operator downstream of the T7 promoter and thus are
expected to have higher transcription rates for these inputs compared to the
input regulated with the TetR operator (`IN_1_TetR`, {ref}`seq-in1-tetr`) in the experimental
samples. The experimental samples were prepared by mixing TetR-enriched
cytosol, in which TetR had been expressed for 3 h before the start of the
experiment, with a freshly prepared cytosol mixture containing the RNA
circuit DNA templates. This mixture was then encapsulated. These
experimental samples thus had the same system encapsulated in the DevCells
and aTc was either added (EXP ON) or not added (EXP OFF) to the solution
surrounding the DevCells.
:::

:::{figure} ./figures/figure3-devcell-images-4nM-2nM.png
:label: fig3
:align: center
:width: 90%
Representative images of GFP fluorescence in DevCells after cell-free
expression at 37 °C. Here, the input-gate template ratio was 4 nM:2 nM. Contrast
and brightness adjustments were uniformly applied across all images for GFP
(green) and Cy5 membrane dye (red) fluorescence channels. Scale bar: 20 µm.
:::

<!-- #fig4-quantified-gfp-4nM-2nM -->
:::{figure} #fig4-quantified-gfp-4nM-2nM
:label: fig4
:align: center
:width: 90%
Quantified GFP fluorescence of DevCells after 1.5 h incubation at 37 °C
using bulk cell-free input-gate template ratio (4 nM:2 nM). This analysis
was conducted on the images collected in the same experiments as shown in
{ref}`fig3`, with n indicating the number of DevCells quantified for each
sample. See {ref}`fig2` for schematics of the different samples.
:::

:::{figure} ./figures/figure5-devcell-images-20nM-2nM.png
:label: fig5
:align: center
:width: 90%
Representative images of GFP fluorescence in DevCells after cell-free
expression at 37 °C. Here, the input-gate template ratio was (20 nM:2 nM).
Contrast and brightness adjustments were uniformly applied across all images for
GFP (green) and Cy5 membrane dye (red) fluorescence channels. Scale bar:
100 µm.
:::

<!-- #fig6-quantified-gfp-1-5hr -->
:::{figure} #fig6-quantified-gfp-1-5hr
:label: fig6
:align: center
:width: 80%
Quantified GFP fluorescence of DevCells after 1.5 h incubation at 37 °C
using optimized input-gate template ratio (20 nM:2 nM). This analysis was
conducted on the images collected in the same experiments as shown in
{ref}`fig5`, with n indicating the number of DevCells quantified for each
sample. See {ref}`fig2` for schematics of the different samples.
:::

<!-- #fig7-quantified-gfp-4-5hr -->
:::{figure} #fig7-quantified-gfp-4-5hr
:label: fig7
:align: center
:width: 80%
Quantified GFP fluorescence of DevCells after 4.5 h of incubation at 37 °C
using optimized input-gate template ratio (20 nM:2 nM). This analysis was
conducted on the images collected in the same experiments as shown in
{ref}`fig5`, with n indicating the number of DevCells quantified for each
sample. See {ref}`fig2` for schematics of the different samples.
:::

<!-- #fig8-quantified-gfp-5hr-all-conditions -->
:::{figure} #fig8-quantified-gfp-5hr-all-conditions
:label: fig8
:align: center
:width: 80%
Quantified GFP fluorescence after 5 h incubation using optimized
input-gate template ratio (20 nM :2 nM). Here,
all four conditions (Neg Control, Pos Control, EXP OFF, EXP ON) are
explored. n indicates the number of
DevCells quantified for each sample. See {ref}`fig2` for schematics of the
different samples. The high fluorescence in EXP ON is due to aTc's green
fluorescence, making inference of any activation difficult.
:::

## Failure modes

A big failure mode was the green fluorescence of aTc. In future experiments,
it is suggested to use a non-fluorescent read-out, such as luminescence, to
mitigate this issue. At high concentrations, the aTc signal was so strong
that it bled through channels other than the GFP channel, so switching to
another fluorescent protein may not resolve the issue. We also found that
aTc photobleached very quickly with our microscope setup, which can
inactivate the molecule for binding
([Baumschlager *et al.* 2020](https://www.nature.com/articles/s41467-020-17677-5)).

Not getting a high enough concentration of each of the templates in the
DevCells is another potential source of failure. There is still more work
that needs to be done around optimizing the concentrations of multi-template
systems in DevCells.

# Resources

- **THE riboregulator DevNote:**
  [devnotes.nucleus.engineering/articles/ss-20260712](https://devnotes.nucleus.engineering/articles/ss-20260712)
- **TetR/aTc detector module (Nucleus documentation):**
  [docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/)
- **ROSALIND small-molecule biosensor DevNote (Khalid Alam):**
  [devnotes.nucleus.engineering/articles/ka-30072024](https://devnotes.nucleus.engineering/articles/ka-30072024)
- **THE riboregulators in cell-free:**
  [biorxiv.org/content/10.1101/2025.09.25.678518v2](https://www.biorxiv.org/content/10.1101/2025.09.25.678518v2.abstract)
- **ctRSD and THE riboregulator sequence compiler**
  - Documentation: [ctrsd-simulator.readthedocs.io/en/latest/SeqCompiler.html](https://ctrsd-simulator.readthedocs.io/en/latest/SeqCompiler.html)
  - Colab: [colab.research.google.com/drive/1Bd-ZugIWnc7PMiFkpaia_UnWA24KF3Mv](https://colab.research.google.com/drive/1Bd-ZugIWnc7PMiFkpaia_UnWA24KF3Mv?usp=sharing)
- **Annotated sequence / plasmid maps from published THE riboregulator manuscripts**
  - Benchling: [benchling.com/sschafft1/f_/mW2x3M1k3j-toehold-exchange-riboregulator-published-sequences](https://benchling.com/sschafft1/f_/mW2x3M1k3j-toehold-exchange-riboregulator-published-sequences/)

# Participants

CSHL Week 2 participants: Gabriela Garza, Luis Montalvo-Gonzalez, Rocky Choi,
Corynne Adanho, Sushmita Halder, Dwon Jordana, Grace Montgomery.
