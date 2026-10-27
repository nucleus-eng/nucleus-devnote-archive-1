---
title: "An AI Scientist For High-Throughput Bio-Processing"
subtitle: "ARIA AI Scientist Program: Executive Summary"
abstract: |
  Find What Matters' IGOR AI scientist was deployed within b.next's compositional biology platform to design, run, and interpret high-throughput experiments optimizing a cell-free energy module (PAP) integrated into Cytosol. Across three deliverables, IGOR's Bayesian engine was upgraded to handle categorical features, intra- and inter-batch constraints, and automated data curation, while an agentic workflow interfaced with a human domain expert. The final deliverable identified energy module compositions delivering a 56% yield improvement over baseline, charted a performance trade-off ridge across four small-molecule components, and surfaced a rate-limiting mechanism outside the explored compositional space, at an iteration rate of roughly one round per three days across five rounds.
---

<!--
TODO before this devnote is publish-ready (see PR description / conversion notes):

1. D3's own devnote (item 4 in Resources below) is listed as "in preparation"
   in the source document. Update the link once it is published.
2. This source carries gdoc_comment_begin/end markers from the Google Docs
   export (converted here to plain text, markers stripped); a few of those
   comment threads may still be open/unresolved on the original Doc. Confirm
   nothing substantive was left unaddressed.
3. Resources items 6 and 7 link directly to internal Google Drive files
   (link-shared, not public). Confirm these are meant to be published
   verbatim in a CC-BY-4.0 devnote, as opposed to attached as devnote
   resources or marked "available on request" like item 8.
-->

:::{note}
This article was written by a **human author**.
:::

# Executive Summary

AI scientists promise to accelerate fields like biology, but few have been tested where it counts: in a working wet lab, on real high-throughput experiments, alongside the scientists who run them. We set out to deploy Find What Matters' IGOR AI scientist (Iterative Guide and Orchestrated Research) to optimize defined biological energy modules within b.next's bottom-up compositional biology platform. We had three major goals: to identify and push the boundaries of AI scientists, to determine the potential of AI science for optimization of compositional biology, and to specifically build understanding of, integrate, and optimize energy modules within cytosol, a defined cell-free system. We proposed a closed experimental loop, where IGOR generated experimental designs in concert with a scientific domain expert; the experiments were run on an automated high-throughput platform, and the data returned to IGOR for analysis and subsequent experimental design [1]. Experimental results are published as Developer Notes [1, 2, 4], micropublication "data packets" that encapsulate human-readable information and directly computable raw data and results.

As the project progressed, we responded to new findings by adapting our approach and the specific systems being optimized. We substantially upgraded IGOR's Bayesian engine to handle inter- and intra-batch constraints in response to experimental requirements [2, 3, 5]; and we exchanged the glycolysis energy module for PAP, an energy module with fewer components, in order to push the iteration loop faster and better test the upgraded AI scientist [4, 10]. Throughout, we collected learnings on the capability, limitations, and operational requirements not only for AI scientists but also for high-throughput experimentation for compositional biology [7, 8].

Finally, we identified energy module conditions delivering a 56% performance gain, and a performance frontier indicating a rate-limit outside of the compositional space being optimized [4]. Our iteration rate accelerated to ~1 iteration per 3 days, across 5 rounds covering 86 distinct experimental conditions and 452 total experiments (wells). We implemented substantial improvements to the IGOR scientist, across both the Bayesian engine and the agentic guide: categorical feature handling, intra- and inter-batch constraints, quantitative data curation and wrangling, and a context-driven AI scientist workspace [3, 5]. We reached and overcame limits that appear as an AI scientist drives experiments outside of familiar experimental regimes, particularly as multiple variables are simultaneously changed. We also learned how biology experimentalists interact with AI scientists, and the benefits and challenges associated with AI-enabling wet lab biology [8].

Our ARIA AI scientist project effectively prototyped and validated an end-to-end AI-driven platform for designing and composing biological systems from scratch. We are excited to scale and deploy the platform to advance compositional biology and build new biotechnology applications.

# Problem and Approach

:::{figure} ./figures/aria-fig-ai.png
:name: fig-aria-workflow
:align: center
:width: 90%
**Workflow and platform.** **(top)** IGOR is a closed loop AI scientist framework that autonomously generates hypotheses, DOEs, data interpretation, and publications, in tandem with the b.next experimental, open data, and publication platform. **(left)** IGOR is composed of scientific LLM agents, grounded by an empirical Bayesian engine. **(center)** AI-published open data, findings, and concrete biotechnology open new frontiers of science and engineering. **(right)** Project timeline.
:::

Compositional biology enables complete definition of bulk cell-free systems and synthetic cells at the level of molecules and proteins, rather than solely DNA sequence. This compositional capability offers a unique opportunity for the application of an AI scientist: access to and the ability to explore the compositional space to achieve an objective. Synthetic cells have applications across sensing, synthetic immunity, and biomanufacturing, and the ability to optimize and extend their core componentry is critical to unlocking their potential. In particular, increasing energy supply by mapping and optimizing the defined base cytosol and integrating new energy pathways (modules) is an immediate scientific need [10]. Doing so requires efficiently navigating a high-dimensional compositional space with complex molecular and methodological interactions, ideal for AI scientist support [9]. Moreover, as the capability of composed biological systems and synthetic cells increases, we expect the number and complexity of integrated modules to rise, further motivating the development of scalable means of experimentation.

IGOR pairs a machine-learning Bayesian Optimization engine (handling multiple objectives, categorical inputs, failure regions, and constrained experimental batches, among others) [3, 5] with a grounded multi-agent scientific workflow. The agents read the scientific literature alongside the lab's documents, Slack, Notion, and Drive; maintain an audited memory; and propose changes for human approval [2, 6]. Together, the Bayesian engine grounds experimental design in quantitative data with calculated uncertainty, while the agentic guide enables mechanistic interpretation, context-informed experimental design, and direct interaction with experimental scientists [4].

We implemented an experimental workflow integrating IGOR into b.next's high-throughput compositional biology platform ("Discovery Plates"). IGOR integrates results from prior experiments (both AI- and human-designed) with scientific context from the literature and internal sources (documentation, presentations, etc.) and generates experiments for testing based on mechanistic hypotheses and Bayesian-grounded optimization [3]. These experiments are run using the high-throughput low-volume Discovery Plate experimental platform, supplied using custom materials produced by b.next's manufacturing facility. Data from experiments is fed back into the IGOR workspace, where a domain-expert scientist is able to analyze and interpret the data in concert with IGOR, producing a new round of experimental designs. We deployed this workflow to optimize the PURE cell-free system based base cytosol ("Cytosol") used by b.next, as well as the PAP energy module on top of it [1, 2].

We were also intrigued by the question of how AI scientists can effectively communicate with humans (to provide direction and oversight) and one another (to inform experiments or later analysis). We prototyped the use of Developer Notes (i.e., micropublications that incorporate written prose as well as raw, computable data and analysis) as human and machine-readable data packets that could communicate results throughout the project [1, 2].

# Summary of Deliverables

:::{figure} ./figures/final-report-overview.png
:name: fig-deliverables-overview
:align: center
:width: 90%
Overview of deliverable outcomes. **(left)** D1: trained surrogate model predicts base cytosol recipes with improved steady state yield performance. **(center)** D2: experimental platform design for intermediate basis mixes, used to increase the number of compositional dimensions which can be simultaneously varied. **(right)** D3: steady state yield relative standard-recipe PAP control achieved by means of different experimental design strategies, across iterations.
:::

Our initial plan involved first using IGOR to optimize a polyphosphate kinase-based energy module (PPK) and validate our experimental workflow, followed by implementation and optimization of the more-complex glycolysis pathway. As a result of experimental limitations outside the scope of the first optimization task (in particular, inconsistent performance and limited substrate availability for the PPK module) and encouraged by ARIA to push the envelope of the AI scientist's challenge, we adapted our experimental plan to focus on different components of the workflow across the three deliverables:

- **D1:** operationalize workflow and integrate IGOR with compositional biology platform [1].
- **D2:** use multiple experimental approaches to push IGOR and drive upgrades to AI science capabilities [2].
- **D3:** deploy IGOR and compositional platform to optimize energy modules [3, 5].

The results from each deliverable are reported in a Developer Note, encapsulating findings as well as the datasets and curated context used in and generated during the run. Key components are summarized here:

### Deliverable 1

**Operationalize workflow and integrate IGOR with compositional biology platform.**

- **Goal:** use IGOR to optimize base cytosol salt composition, and implement data workflows to run experimental designs on the platform, return data to IGOR, and publish results as Developer Notes.
- **Method:** IGOR designed experiments manipulating key cytosol salts and components: ATP, GTP, magnesium acetate, creatine phosphate, potassium glutamate, and tRNA, with and without the PPK module.
- **Outcome:** final discovery plate examined 35 different compositions across 7 PURE parameters, resulting in a wide dataset which predicts improvements to PURE performance. Implementation and testing of the workflow meant few iterations were run, which limited our ability to verify and build on these improvements.
- **Findings and Improvements:** D1 drove our integration of IGOR and the experimental platform, highlighting both experimental (e.g. viscous liquid handling) and AI bottlenecks (e.g. data curation). We implemented handling of categorical input features, improved experimental platform performance, and implemented means for Developer Note export from IGOR.

### Deliverable 2

**Use multiple experimental approaches to push IGOR and drive upgrades to AI science capabilities.**

- **Goal:** continue iterations and develop and test a new means of assembling experiment samples in order to explore an increased number of compositional dimensions simultaneously.
- **Method:** we designed a new means of assembling experimental reactions, creating multiple intermediate "basis mixtures" combining components and assembling these into final reactions, providing the means to change more parameters simultaneously at the expense of experimental design complexity.
- **Outcome**: we achieved improvement in baseline cytosol protein production performance with our next iteration. Moving to intermediate mixes created new experimental design and platform implementation challenges as we moved into unexplored composition and operational territory.
- **Findings and Improvements**: this deliverable drove substantial upgrades to IGOR's bayesian engine and agentic workflow. In particular: implementation of batch Bayesian optimization for intra- and inter-batch constraints, improved constraint handling for experimental platform constraints generally, an agentic data curation and wrangling workflow to simplify data exchange with IGOR, and data connectors to provide increased context to the scientific agents.

### Deliverable 3

**Deploy IGOR and compositional platform to optimize energy module.**

- **Goal:** drive iterations to test the operational workflow and AI scientist in implementing the PAP (pyruvate–acetate pathway) energy module [10].
- **Method:** we reverted to our initial experimental setup, removing the intermediate bases, and adopted the PAP energy module as a relevant module that could be used to test the upgraded IGOR AI scientist and experimental platform.
- **Outcome**: we ran 5 iterations, over 8 experimental plates for a total of 452 experimental wells within 16 days. IGOR identified integrated energy module compositions resulting in 12–56% performance improvements over the standard energy module composition. Moreover, IGOR identified and charted a performance trade-off ridge across four small molecules (CP, K-phosphate, Na-pyruvate, Mg-glutamate), and identified a potential rate-limiting mechanism (protein concentration) that was outside of the experiment optimization dimensions (see figure) [8].
- **Findings and Improvements**: our key goal in this deliverable was to test IGOR in a scenario where multiple comparable iterations could be run rapidly, pushing our improved platform to deliver gains against the optimization objective as well as improved system understanding. This goal was achieved. The upgraded IGOR agentic scientist and workspace also provided value in interacting with the human scientist: identifying outliers caused by an instrumentation failure and allowing data to be salvaged; aiding in the visualization and interpretation of high-dimensional data landscape, particularly indicating when the landscape was "tapped out" due to a mechanistic limitation; and identifying putative mechanisms for experimental designs and to interpret results [8]. Improvements to context integration enabled IGOR to design mechanism and context-informed baseline experiments to seed the initial dataset, rather than traditionally used statistical low discrepancy sampling techniques.

# Conclusions and Next Steps

The project validated the potential of AI scientists to accelerate implementation, optimization and integration of compositional biology systems. Access to the full compositional space provides the opportunity to deeply explore mechanism and the performance landscape, but immediately raises the challenge of how to effectively understand and navigate such a complex high-dimensional space. Through the project, we drove improvements to the IGOR AI scientist, our experimental platform, and, at a higher level, our way of working with an AI scientist, by optimizing energy modules integrated with cytosol. This lead to several key outcomes:

- 56% improvement in yield performance of the PAP energy module relative to baseline [4].
- Increase in experimental iteration time from approximately 1 per month (D1) to 1 per 3 days [1, 4].
- Greater AI scientist insight into system mechanisms, and identification of mechanistic rationale for frontiers explored and identified by the AI scientist.

We were driven to develop key AI scientist capabilities, including several that were simultaneously recognized as critical for effective optimization of biological experiments [9]: batch Bayesian optimization; experimental platform constraint optimization; mixed categorical variables; multi-objective and safe Bayesian optimization; and outlier handling. In particular, we identified and tested the increasing power of human- and AI-scientist-in-the-loop design, building a workspace where a domain-expert human scientist could collaboratively work with IGOR to analyze and interpret data and design experiments, establishing a division of labor in which IGOR proposed designs the bench scientist would not have reached, and the bench scientist ruled out designs the model could not know were unrunnable. The result was a mechanistic finding neither party had hypothesized: a stoichiometric maximum yield ridge IGOR surfaced through constrained exploration and the scientist independently corroborated [8].

Our final deliverable saw our AI, platform, and experimental improvements converge, leading to rapid iterations driving system integration and performance. There are several immediate next steps to pursue:

- Leveraging our operational platform to pursue further iterations with the PAP module, adding additional experimental dimensions to explore and push through the rate-limiting mechanism identified by IGOR.
- Further updates to IGOR: improved workspaces to connect additional forms of context and data (for instance, data from earlier cytosol optimization experiments, and integration of the mechanistic model of cytosol we are currently developing); and an adaptive surrogate architecture that would allow the bayesian engine to operate directly on time-series data using ODE neural networks rather than relying on summary statistics.
- Exploring the potential of IGOR as a co-scientist by deploying it to additional synthetic cell builders and compositional biologists, enabling them to design experiments and interpret data even in the absence of high-throughput capabilities.
- Turning IGOR on its own development, so that friction and unmet needs surfaced during user sessions become tracked engineering work that IGOR implements and submits for review, a self-improving platform in the most literal sense [7].

The field of bottom-up compositional biology is growing, driven by the increasing capability and momentum of synthetic cells for research and biotechnology. Deploying compositional biology effectively requires the understanding and optimization of cell and cytosol components of increasing number and complexity. AI scientists provide a means to address this complexity at scale. Through this ARIA AI Scientist project, IGOR has developed key enabling features in response to experimental needs, and demonstrated the ability to operate experiments, assist domain scientists, and optimize effectively. We look forward to further pushing the envelope of AI science in concert with compositional biology.

# Resources and Further Reading

### Project deliverables (Nucleus Developer Notes)

1. **D1.** *AI Scientist: Base Module Report* (April 2026). [devnotes.nucleus.engineering/articles/d1-20260426](https://devnotes.nucleus.engineering/articles/d1-20260426)
2. **D2.** *Defining AI Scientific Workflows: Using IGOR for Optimization of PURE* (July 2026). [doi:10.63765/kxfm6388](https://devnotes.nucleus.engineering/articles/aria-d2)
3. **Lozier, J. (2026).** *Batch Bayesian Optimization.* [doi:10.63765/mkjg5795](https://devnotes.nucleus.engineering/articles/lozier-2026-batch-bayesian-optimization)
4. **D3.** *PAP energy module Developer Note* (in preparation).

### Supporting material and literature

5. **ARIA knowledge-sharing deck:** intra- and inter-batch constraints. [deck.findwhatmatters.ai/aria-knowledge-sharing/?key=y6qb-e75f-6ujf](https://deck.findwhatmatters.ai/aria-knowledge-sharing/?key=y6qb-e75f-6ujf)
6. **Agents as low-discrepancy samplers:** [drive.google.com/file/d/1t4PjXeId4S9bJwTfJl2jj_WlaqfLaiR-/view](https://drive.google.com/file/d/1t4PjXeId4S9bJwTfJl2jj_WlaqfLaiR-/view?usp=sharing)
7. **The self-improving IGOR platform:** [drive.google.com/file/d/1KSQQXOZucZkWfMExVew-DMobsY2odAI9/view](https://drive.google.com/file/d/1KSQQXOZucZkWfMExVew-DMobsY2odAI9/view?usp=sharing)
8. D3 chat logs with IGOR (rounds 1–2 and 1–3) and the two-part chat-log analysis (available on request).
9. **Siska, M. et al. (2026).** A Guide to Bayesian Optimization in Bioprocess Engineering. *Biotechnology and Bioengineering* 123(4), 805–830. [doi:10.1002/bit.70129](https://doi.org/10.1002/bit.70129)
10. **Yadav, S. et al. (2025).** ATP Regeneration from Pyruvate in the PURE System. *ACS Synthetic Biology*. [doi:10.1021/acssynbio.4c00697](https://doi.org/10.1021/acssynbio.4c00697)
