# Experiments

Each directory holds one figure's notebook, its inputs under `data/`, and the
figure PNG the notebook writes. Every path in every notebook is relative and
resolves inside its own directory — verified by tracing every file open during a
full execution. Nothing reads from glycine or any mounted volume.

| Directory | Figure | Notebook | Inputs |
| --- | --- | --- | --- |
| `20260909-simulated-landscape/` | Figure 1 (simulated) | `fig1_optimum_moves.py --two-panel` | none |
| `20251105-labcraft-energy-sweep-01/` | Mg × K heatmap | `Consolidating.ipynb` | 3 |
| `20251106-labcraft-protein-sweep-01/` | 3D scatter + interaction plots | `analysis.ipynb` | 2 |
| `20260306-discoveryplate-aria-r0/` | 5-factor pairplot | `kinetics_QC.ipynb` | 5 |
| `20260318-discoveryplate-aria-r1/` | 7-factor pairplot | `kinetics_QC.ipynb` | 5 |
| `20260506-discoveryplate-aria-r3/` | 8-factor pairplot | `kinetics_QC.ipynb` | 5 |

All five notebooks execute end to end with zero errors on
`nucleus-cdk==0.5.0rc2`, pinned in each notebook's first cell.

## Provenance

Copied from `sharon@glycine:/home/sharon/bnext/experiments/` on 2026-09-09 with
`scp` (read-only; nothing on glycine was modified), then reduced to the files
each figure actually reads.

| Directory here | Source on glycine |
| --- | --- |
| `20251105-labcraft-energy-sweep-01` | `20251105-labcraft-energy-sweep-01` |
| `20251106-labcraft-protein-sweep-01` | `20251106_labcraft_protein_sweep_01` |
| `20260306-discoveryplate-aria-r0` | `20260306-DisoveryPlate-ARIA-R0` |
| `20260318-discoveryplate-aria-r1` | `20260318-DiscoveryPlate-ARIA-R1` |
| `20260506-discoveryplate-aria-r3` | `20260506-DiscoveryPlate-ARIA-R3` |

The raw file for the 3-factor sweep lives in a separate tree on glycine
(`bnext/instrument/biotek-cysteine/experiments/`), not beside its notebook; it
was copied in and the notebook's path updated to match.

## Changes made to the notebooks

Each notebook was truncated after the cell that produces its figure — the
exploratory analysis that followed is not part of this note. Beyond that:

- **all** — added the pinned `nucleus-cdk==0.5.0rc2` install cell as the first
  cell, per `migrate-devnote/references/prepare.md §5`; rewrote input paths to
  `data/`; removed commented-out lines pointing at glycine or `/Volumes`.
- **20251105** — four cells referenced `[Mg] (mM)` / `[K] (mM)` while the cell
  above renamed those columns to `Magnesium acetate` / `Potassium glutamate`, so
  the notebook could not run top to bottom. Restored the bracketed names, which
  are also the axis labels in the published figure.
- **20251106** — switched the raw-data read to the relative path the author had
  already written and commented out one line above.
- **20260318** — removed a hard-coded `os.chdir` to a mounted volume. Reverted
  the steady-state binning from 4 bins / `rocket_r` to the 3 bins and
  red-orange-green palette the published figure uses.
- **20260506** — removed a hard-coded `os.chdir`. Repointed
  `from cdk.calculators.naming import …` at the vendored `cdk_naming.py`; that
  module exists only in CDK 0.6.0, which deleted the plate-reader API the
  notebooks use. Without it the axes show titration-only concentrations rather
  than final ones.

## Known difference from the published figures

The 5-factor pairplot's magnesium axis spans roughly 2.5 mM to 12 mM here, where
the Notion draft shows 5 mM to 25 mM. The notebook applies a magnesium stock
correction that postdates the draft figure:

```python
samples["[Magnesium acetate] (mM)"].apply(lambda x: x * 95.2 / 203.3)
```

recorded on the source page as *"Possibly the Magnesium stock was incorrectly
made! Potentially used 203 g/mol (MgCl hexahydrate?) not 95.21 g/mol MgCl₂."*
Every other axis, the binning, the palette and the point structure match. **This
needs a decision:** publish the corrected axis and note the change, or publish
the draft's uncorrected axis. The corrected version is what ships today.

The Mg × K heatmap's colour scale also tops out near 9 000 where the draft
reaches about 10 500. The pattern is identical; the difference is in the
steady-state fit, and the draft figure was made by a sibling notebook
(`Untitled.ipynb`) that is not part of this note.

## Re-execution environment

Outputs were produced with Python 3.12.12, nucleus-cdk 0.5.0rc2, numpy 2.5.3,
scipy 1.18.1, pandas 2.3.3, matplotlib 3.11.1, seaborn 0.13.2, shap 0.52.0 —
not the `b.next CDK` kernel the notebooks declare, and not live compute's Python
3.14. Re-run them in the real kernel before opening the PR.
