---
title: "Developer Studio"
abstract: |
  Developer Studio brings together 12 labs organized into two Nodes for a three-week sprint to reproduce, integrate, and document synthetic cell engineering demonstrations at Nucleus Labs in San Francisco. This DevNote describes the event's structure, the technical capacities required to support collaborative synthetic cell engineering at scale, and the data and documentation pipelines — from bench measurement to published DevNote — developed to enable rapid, reusable documentation across participating labs.
---

## Overview

Developer Studio is an event that brings together 12 labs organized into two Nodes to do integrated synthetic cell engineering. Over the last 9 months, each Node has been working at their own institutions to figure out how to integrate pre-existing synthetic cell technologies into charismatic demonstrations, the so-called [London](https://devnotes.nucleus.engineering/articles/london-demo-1) and [Chicago](https://devnotes.nucleus.engineering/articles/chicago-demo-1) Demos. The goal of the studio is to reproduce the work done over the last 9 months in a three-week period and ensure that it is documented for reusability, significantly expanding the amount of integrated synthetic cell technology available on [Nucleus](https://docs.nucleus.engineering/). More succinctly, the goals are:

Reproduce demonstration projects in new labs.
Document the modules and underlying dependencies for reusability.
Improve the underlying tools to document the modules along the way.

By working together to build and document these demos on a short timeline, we have been prototyping collaborative synthetic cell engineering and learning the principles of this new field — building on earlier work begun at the [DevCells Kickoff Workshop](https://devnotes.nucleus.engineering/articles/devcells-kickoff-workshop). This Developer Note aims to describe the underlying technical and organizational structure for running Developer Studios in the future.

## Synthetic Cell Engineering

Several capacities must be in place in order for Developer Studio to accomplish its goals. These capacities are also aligned with those needed to scale the size of collaboration in integrative synthetic cell engineering. This compiles down to three core pieces:

Reliable materials: Reliable materials that support documentation and reusability
Data pipelines: Ability to quickly transform an experimental design into well annotated data
Documentation Workflows: A means for quickly creating and modifying specifications to evolve with emerging constraints

Many of these capacities exist in some form on Nucleus already. However, we need to adapt these tools to accommodate the form of this event and ensure that they work reliably. What follows is a checklist for what needs to be demonstrated and its current status.

## Capacities checklist

::::{tab-set}
:::{tab-item} Pipeline
```{include} assets/pipeline-diagram.md
```
:::
:::{tab-item} Chicago Module Dependencies
```{include} assets/chicago-module-dependencies.md
```
:::
:::{tab-item} London Module Dependencies
```{include} assets/london-module-dependencies.md
```
:::
::::

Our plan is to develop and validate our data pipeline and documentation workflows against a specific test case. The proposed test case will be embedding base cell in an agarose hydrogel. This will test our documentation workflows using two standard data workflows: microplate reader and microscopy. This will test the process from the bench to data to DevNote to documentation.

:::{note} 
Status per item will be added starting the week of 9/4, once this week's build work is further along. 
:::

### Reliable materials

Custom reagents or materials with long lead times need to be procured and validated in advance of the event.

### Data pipeline
- **Instrument access & data delivery.** Participants require a way for easily accessing measurement readouts without relying on our central file system.
- 
Platemap generation. Participants require a method to convert a platemap in their own format into one compatible with - **Nucleus's [CDK](https://pypi.org/project/nucleus-cdk/) tools.** This is currently the most critical and least developed component of the pipeline.

CDK and compute access. Participants require reliable access to CDK tools, most likely via Colab-based template workbooks rather than local installations.

- **Figure generation and analysis.** Participants require a means to modify the CDK outputs, suggest improvements, and integrate analysis into a collaborative drafting environment.
- 
- **Collaborative drafting environment.** Participants require a shared workspace, likely hosted on Google Drive, for assembling figures and notes into a draft. The draft must follow defined semantic conventions to support downstream parsing.
- 
- **Livestream.** Instrument output needs to be reliably piped to a public [YouTube](https://www.youtube.com/channel/UC_8cK6nOMQgEp-fnS3S5rXw) stream as data is generated, so participants and outside followers can watch data come off the machines in real time.

### Documentation workflows

- **Draft to DevNote.** A process is required to convert a participant's draft created in the shared workspace into a [MyST-based DevNote](https://devnotes.nucleus.engineering/).

- **DevNote to Docs.** A process is required to extract content from a DevNote into a documentation page for publication on [Nucleus Docs](https://docs.nucleus.engineering/).

- **Documentation management.** A process is required to adapt and modify documentation as more data is collected and additional constraints are identified.

- **Decision making.** Some engineering decisions during the Studio will lack an obvious answer or owner. A process for making and recording these decisions, likely as DevNotes framed as RFCs, should be defined in advance.

### Structure of the event

As a starting point, we expect that the event will have the following week-by-week structure.

- **Week 1.** Replicate and test individual modules — get what worked at the home labs working in San Francisco.
- **Week 2.** Resolve issues and get each Node's full integrated demo working.
- **Week 3.** Make another attempt if needed; otherwise, integrate or swap modules across Nodes.

### Follow along

This event will be open — feel free to drop by and participate over the three weeks (9/23 – 10/14). We'll be livestreaming instrument output directly to YouTube as data comes in, so you can follow along with what's happening on the bench in real time, not just see the final demos. Please reach out!
