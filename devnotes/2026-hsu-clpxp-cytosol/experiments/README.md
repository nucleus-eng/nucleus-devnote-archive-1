# Experiments

Each directory holds the raw dataset behind one figure in `main.md`. A dataset
has three parts: a plate reader export (`.xpt` and its `-biotek.txt` /
`-biotek-cdk.txt` companions), a platemap `.csv`, and the analysis notebook.
This follows the same layout as `2026-yadav-cytosol-lifetime/experiments`.
Drop files into the matching directory below. The directory name already
matches the figure's file name under `general/Platereader/`, so no renaming is
needed.

| Directory | Experiment | Figure | Status |
| --- | --- | --- | --- | 
| `No DNA/` | Experiment 1 (No DNA) | `general/Platereader/No DNA/No DNA.png` | Wired |
| `1 DNA-ClpP/` | Experiment 2 (1 DNA: ClpP) | `general/Platereader/1DNA/1 DNA-ClpP.png` | Wired |
| `1 DNA-ClpX/` | Experiment 3 (1 DNA: ClpX) | `general/Platereader/1DNA/1 DNA-ClpX.png` | Wired |
| `1 DNA-deGFP-ssrA-1/` | Experiment 4 (1 DNA: GFP-ssrA) | `general/Platereader/1DNA/1 DNA-deGFP-ssrA-1.png` | Wired |
| `1 DNA-deGFP-ssrA-2/` | Experiment 4 (1 DNA: GFP-ssrA) | `general/Platereader/1DNA/1 DNA-deGFP-ssrA-2.png` | Wired |
| `2DNA-GFP_ClpP/` | Experiment 5 (2 DNA) | `general/Platereader/2DNAs/2DNA-GFP_ClpP.png` | Wired |
| `2DNA-GFP_ClpX/` | Experiment 6 (2 DNA) | `general/Platereader/2DNAs/2DNA-GFP_ClpX.png` | Wired |
| `3DNA/` | Experiment 7 (3 DNA) | `general/Platereader/3DNAs/3DNA.png` | Wired |
| `3DNA-NEB/` | Experiment 7 (3 DNA, NEB comparison) | `general/Platereader/3DNAs/3DNA-NEB.png` | Wired |

## Upload notes

`No DNA/` holds `20260605-No DNA.csv` and its companion files. The platemap
lists the four No-DNA conditions from `tbl-exp1`: ClpX + ClpP, ClpX only, ClpP
only, and deGFP-ssrA alone.

`1 DNA-ClpP/` holds two versions of the same run: `Untitled.ipynb` with
`20260604-2.csv` (older CDK API), and `new-cdk-version.ipynb` with
`new-platemap.csv` (newer CDK API). Both platemaps carry the same three
pT7-ClpP concentrations and the same deGFP-ssrA-only control from `tbl-exp2`.
The two notebooks render the same curves but with different axis tick
formats. `new-cdk-version.ipynb` (cell labeled `20260604-clpp`) is the exact
match for the published figure. `Untitled.ipynb` and `20260604-2.csv` are a
stale earlier draft of the same run. They can be removed once someone
confirms that.

`1 DNA-ClpX/` and `2DNA-GFP_ClpP/` come from one uploaded archive that held a
single plate reader run split across two experiments: wells A1 through C4
matched `tbl-exp3` (1 DNA: ClpX), and wells A5 through C7 matched `tbl-exp5` (2
DNA: ClpP and GFP-ssrA). The raw instrument export
(`20260608-131856-cytation5-pure-timecourse-gfp-biotek-cdk.txt`) covers both
well ranges, so a copy sits in each directory beside its own platemap and
notebook.

`2DNA-GFP_ClpX/` and `3DNA/` come from one upload that held a third shared
plate: wells A1 through C3 matched `tbl-exp6` (2 DNA: ClpX), and wells A4
through C6 matched `tbl-exp7` (3 DNA, Cytosol). The raw export
(`20260609-151420-cytation5-pure-timecourse-gfp-biotek-cdk.txt`) covers both
ranges, so a copy sits in each directory. The archive also held a third
notebook, `Untitled2.ipynb`, that reads an unrelated sample dataset not part
of this devnote. It was left out.

`1 DNA-deGFP-ssrA-1/` and `1 DNA-deGFP-ssrA-2/` share a plate with `No DNA/`.
All three use the same raw export,
`20260605-160608-cytation5-pure-timecourse-gfp-biotek-cdk.txt`. One run on
2026-06-05 covered the No-DNA wells (N1 through P4) and the deGFP-ssrA wells
(N5 through P8). The two deGFP-ssrA directories differ only in their platemap: `20260605-GFP-ssrA.csv` keeps the N8-P8 control wells for
`fig:deGFP-ssrA-1` (the "w/ control" tab), and `20260605-GFP-ssrA-2.csv` drops
them for `fig:deGFP-ssrA-2` (the "w/o control" tab).

## Wiring figures to notebook output

The nine filled directories are wired into `main.md` as live-compute figures,
not static image paths. Each notebook's plotting cell starts with a tag line,
for example `#| label: 20260605-no-dna`. The matching figure directive in
`main.md` reads that cell's output by the same name, for example
`:::{figure} #20260605-no-dna`. This is the same pattern
`module-Clpxp-Cytosol/main.md` and `2026-newman-cytosol-landscape/main.md`
use. Each wired notebook is also listed in `curvenote.yml`'s `toc`. Curvenote
needs that entry to execute the notebook.

The original static PNG under `general/Platereader/` stays in place as a
comment above each figure directive, for reference.

`3DNA-NEB/` holds the same experiment run in NEB PURExpress instead of
Nucleus Cytosol, for comparison against `3DNA/`. Its notebook already saves
its plot as `Raw Plot.png`, matching the published figure.

All nine figures are now wired. The only remaining open item is the stale
`1 DNA-ClpP/Untitled.ipynb` draft noted above, left uncommitted for now.

## Follow-up: BinderHub dependency

None of these notebooks install `nucleus-cdk` yet. A later commit needs to
add this line as the first cell of each wired notebook, so the notebook runs
on the deployment BinderHub.

```
!pip install nucleus-cdk==0.5.0rc2 | tail -n2
```
