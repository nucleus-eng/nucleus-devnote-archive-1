# Principles

## What a DevNote is for

One investigation, documented so someone else can run it again. That is the whole job.

A reader should be able to reproduce the experiment from the page and the files beside it, without asking the author a question. Everything else — framing, related work, implications — is optional and should be short when present.

## Tone and register

**Formal scientific prose.** Past tense for what was done, present tense for what it means.

**Protocol steps are imperative and numbered.** *"Add 1 mL mineral oil to the 1.8 mL glass vial."* *"Vortex the lipid-in-oil mixture for 10 seconds."*

**State quantities with precision, and always with units inline.** *"yields increasing by nearly 96% relative to the CP/CK module alone."* *"optimal protein expression at a final Mg²⁺ concentration of 8 mM."*

**Bold a component on first use in a protocol section**, with its abbreviation: *"1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine **(POPC)**."*

**Hedge preliminary results, and say so plainly.** *"These findings are preliminary and require further optimization."* A hedge is information; an unhedged preliminary result is a claim the data does not support.

**Cite with a DOI, inline.** `[[Wang *et al.* 2019](https://doi.org/10.1021/acssynbio.9b00456)]`. Link to prior DevNotes the same way — `[Nucleus Cytosol](https://doi.org/10.63765/fppr8928)` — so the chain of foundational work is navigable.

## Complete versus stub

A DevNote is **complete** when it has all of:

- a populated `abstract` in the frontmatter that states the key finding
- an Overview or Introduction with actual body text
- at least one composition table with exact concentrations
- at least one results figure
- a Conclusions section with a forward-looking statement
- the raw data files committed beside the notebook
- an analysis notebook that produces the result figures

**These signals mean it is still a stub**, and each has been seen in the archive:

| Signal | What it means |
| --- | --- |
| A section heading with no body under it | The section was scaffolded and never written |
| `Untitled.ipynb` | The notebook was never renamed after the experiment |
| Commented-out TOC entries in `curvenote.yml` | Content exists but is not published |
| A commented-out `doi:` | Not registered |
| `template-blank.md` or `template-example.md` still in the repo | Scaffolding was never cleared |

**Ship a stub if it is honest about being one.** An empty section is worse than an absent one — delete the heading rather than leaving it hollow.
