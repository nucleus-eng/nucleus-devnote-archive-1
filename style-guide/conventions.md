# Conventions

## Notation and units

These follow NIST SP 811, with the divergences noted at the end.

| | Write | Not |
| --- | --- | --- |
| Unit spacing | `10 mL` | `10mL` |
| Compound units | `ng/µL` | `ng / µL` |
| Micro symbol | `µL`, `µM`, `µg`, `µm` | `uL`, `uM` |
| Degrees | `55 °C` | `55C`, `55 C`, `degC` |
| Ion charges | `Mg²⁺`, `Na⁺`, `Ca²⁺`, `K⁺` | `Mg2+`, `Mg++` |
| Chemical formulae | `H₂O`, `MgCl₂`, `OD₆₀₀`, `A₂₆₀` | `H2O`, `OD600` |
| House casing | `rpm`, `Kan`, `kDa`, `4x` | `RPM`, `KAN`, `KDA`, `4X` |
| Thousands | `40 000 units` | `40,000 units` |
| Time | `h`, `min`, `s`, `d`, `yr`, `mo` | `hours`, `minutes` |
| Ranges | `16 mM to 18 mM`, `(16–18) mM` | `16-18 mM` |
| Mixtures | `LB + Kan` | `LB+Kan` |

**Numbers under five digits take no thousands separator** (NIST SP 811).

**Deliberate divergences from NIST**, so they read as decisions: `25%` with no space before the sign, because `25 %` reads as unusual to bench scientists; and `ppm` is permitted as accessible shorthand.

## These are checked, and the check warns

**The rules above are enforced by Vale, and in this repo every rule is `warning` level.** Nothing here blocks a merge.

That is deliberate and it is not laxity. New vocabulary flows *in* from DevNotes — blocking the source would stop the glossary growing. The place that blocks is `nucleus-docs`, where vocabulary settles.

**A warning needs somewhere to appear, or it is not a rule.** Findings surface in two places: a **job summary** on the CI run, and a **comment on the pull request**. The job summary is the record; the PR comment is what an author actually reads.

**The rule files are shared**, not copied. They live in `nucleus-eng/nucleus-skills` and each repo points its own `.vale.ini` at them and sets its own severity. Only the severity is local — a rule that differs between repos is a bug in one of them.

## When a convention is missing

**Write the page, then say what you had to decide.** This guide is small on purpose and grows from real need. If you invented a convention to finish a DevNote, that is the strongest possible case for adding it here — raise it rather than leaving the next author to invent a different one.

A convention nobody needed is a rule that will be broken by accident and enforced by nobody.
