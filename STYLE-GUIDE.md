# Nucleus DevNote style guide

A DevNote is a **short, reproducible technical report on one experimental investigation** into a component or subsystem of the Nucleus platform. It carries its own raw data, analysis notebooks and figures alongside the narrative, and it is published open-access under CC-BY-4.0.

**DevNotes are not papers.** They are closer to a structured lab-notebook entry with a concise scientific summary. Be precise about reagent concentrations, instrument settings and protocol steps. Do not perform exhaustive literature review or broad contextualisation.

Write for engineers and scientists building on the platform — people who will reproduce the experiment, not people assessing it.

## This guide is deliberately small

| File | Holds |
| --- | --- |
| [`style-guide/principles.md`](style-guide/principles.md) | What a DevNote is for, tone and register, complete versus stub |
| [`style-guide/sections.md`](style-guide/sections.md) | The section structure, composition tables, figures, and how notebooks and data relate to the narrative |
| [`style-guide/conventions.md`](style-guide/conventions.md) | Notation, units, and where a warning surfaces |

**MyST mechanics are not here.** Fence depth, tab-set nesting, cross-reference anchors, `.md`-not-`.html` links and figure placement live in the `author-myst-content` skill in [`nucleus-eng/nucleus-skills`](https://github.com/nucleus-eng/nucleus-skills), because they are properties of MyST rather than of this repo. Invoke that skill when writing; this guide covers only what is specific to a DevNote.

## The rule about rules

**Permissive, iterative, learning-oriented.** This guide ships minimal and co-evolves with the corpus. A convention earns its place here by having been needed, not by being defensible in the abstract.

New terms flow **in** from DevNotes. That is why checks here warn and never block: blocking the source would stop the vocabulary growing.
