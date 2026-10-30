# Review of AN_ANON_006

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This perspective manuscript examines software usability, dependency management, deployment reproducibility, and user training across molecular evolution and population genetics. Motivated by an informal audit of 23 Methods and Resource software articles published in *Molecular Biology and Evolution* (*MBE*) between January `[YEAR]` and March `[YEAR]`, the authors report that while 22 of 23 tools deposited open-source code in GitHub or CRAN, only 3 provided sufficient documentation or tutorials to be easily installed and used, and only 2 were packaged in Bioconda. To bridge this gap between open source code and practical usability, the article outlines a three-part modernization strategy illustrated with IQ-TREE: (1) cross-platform package and environment management via Conda/Bioconda; (2) automated software containerization via Docker, Singularity, and rkt; and (3) integration into unified web-based workflow platforms (`[SOFTWARE]`, augmented with Jupyter/RStudio Interactive Environments) paired with FAIR, community-curated Markdown tutorials hosted by the `[WORKFLOW_PLATFORM]` Training Network (GTN).

As a best-practices commentary, the manuscript offers practical, technically sound recommendations that directly address software decay and installation barriers in evolutionary bioinformatics. Its primary methodological weakness lies in the informal 23-paper *MBE* usability survey used to anchor the narrative: the inclusion criteria (restricting to open-access papers or those with a URL in the abstract) and the evaluation rubric for what constitutes "easily installed and used" are not defined in the main text, making the headline "only 3 of 23 tools" statistic difficult to audit or reproduce independently. In addition, a factual error in the "Going Forward" section misidentifies the Newick tree format as a sequence alignment input format for PhyML. Clarifying the survey methodology and fixing the technical errors will make the perspective substantially more rigorous.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Conda/Bioconda packaging and containers (Docker/Singularity) streamline installation and pin exact software versions for reproducible evolutionary analyses: [Well Supported].**  
  Figure 1A–B and the accompanying text accurately contrast manual source compilation (`cmake`, compiler toolchains, `PATH` configuration) with single-command `conda install` and automated Bioconda container builds (`docker run`), demonstrating how version pinning (e.g., IQ-TREE 1.5.5) isolates runtime dependencies.

* **Integrating Conda-packaged evolutionary tools and Interactive Environments into `[SOFTWARE]` enables end-to-end multi-step workflows: [Well Supported].**  
  The manuscript clearly explains how Bioconda recipes can be wrapped into `[SOFTWARE]` (Figure 1C) so that raw read QC, mapping, variant calling, alignment, and phylogenetic selection analyses can be chained together alongside interactive RStudio/Jupyter sessions without local installation.

* **While 22 of 23 surveyed *MBE* software tools are open source, only 3 of 23 are easily installed and usable in practice: [Fragile].**  
  Although Supplementary Table S1 lists the 23 surveyed papers, the main text provides no operational definition or standardized test protocol for how "enough information (documentation and/or tutorials) to actually be easily installed and used" was scored. Specifically, it is unclear how many evaluators tested each tool, what operating systems were used, how CRAN R packages (which install via a standard single command `install.packages()`) failed the usability criterion, or how many total *MBE* Methods/Resource papers were excluded by the paywall/abstract-URL filter.

* **Community-curated Markdown training repositories (GTN) modeled on Software/Data Carpentry lower barriers to evolutionary software adoption: [Well Supported].**  
  The description of the GitHub-backed GTN infrastructure (`training-material`), open peer review via pull requests, and hands-on Markdown tutorials across 33 participating groups provides a verifiable, reusable blueprint for community education.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Define the Evaluation Rubric and Sampling Frame for the 23-Tool *MBE* Usability Audit
* **WHY:** Reporting that only 3 of 23 recently published *MBE* software tools contained enough information to be "easily installed and used" is a striking quantitative claim, but without explicit scoring criteria, readers cannot tell whether tools failed due to broken compilation, missing dependency lists, absent sample datasets, or subjective documentation preferences.
* **WHAT:** Explicitly state the total number of Methods/Resource articles published in *MBE* during the January–March window before filtering, and define the exact binary criteria used to classify a tool as installable and documented.
* **HOW:** Add 3–4 sentences to paragraph 2 of the Main Text specifying: (i) the total number of *MBE* software papers in that period prior to applying the open-access/abstract-URL filter; (ii) the separate pass/fail counts for *installation success* vs. *presence of a worked tutorial with example input data*; and (iii) the test environment used to evaluate the 23 tools.

#### 2. Correct the Technical Error Regarding Sequence Alignment vs. Tree Formats in PhyML
* **WHY:** In "Going Forward" (paragraph 3, line 46), the text states: *"For example, a website implementing a tree reconstruction algorithm (such as PhyML; Guindon et al. [YEAR]) will use sequence alignments in a particular format (e.g., Newick) as the input."* Newick is a parenthetical representation of phylogenetic trees, whereas PhyML requires multiple sequence alignments in PHYLIP (or FASTA/NEXUS) format as input and outputs trees in Newick format.
* **WHAT:** Replace `(e.g., Newick)` with `(e.g., PHYLIP)` in the discussion of sequence alignment input formats.
* **HOW:** In line 46, revise the sentence to read: *"For example, a website implementing a tree reconstruction algorithm (such as PhyML; Guindon et al. [YEAR]) will use sequence alignments in a particular format (e.g., PHYLIP) as the input, and output trees in Newick format."*

#### 3. Discuss Limitations of Docker Containers on Shared High-Performance Computing (HPC) Clusters
* **WHY:** While the text mentions Docker, Singularity, and rkt together, molecular evolution users frequently run computationally intensive phylogenetic and population genomic software (e.g., BEAST, RevBayes, IQ-TREE, PSMC) on multi-tenant university HPC clusters where Docker is disallowed due to root-daemon security escalation risks.
* **WHAT:** Briefly distinguish rootless HPC runtime execution (via Singularity/Apptainer converting Docker/Bioconda images) from local/cloud Docker execution.
* **HOW:** Add two sentences in the "Tools for Packaging and Distributing Software" section noting that Bioconda's automatically generated Docker/Quay.io containers can be directly pulled and executed without root privileges on standard academic HPC clusters using Singularity.

#### 4. Technical and Editorial Cleanup
* **WHY:** Several minor grammatical and typographical errors appear in the text and figure legend.
* **WHAT & HOW:**
  1. **Main Text (line 11):** Change `"Two additional tools has been added to Bioconda"` to `"Two additional tools have been added to Bioconda"`.
  2. **Figure 1 Legend (line 14):** Change `"is can be installed"` to `"it can be installed"`, `"These instruction do not include"` to `"These instructions do not include"`, and `"Ability of specify software versions"` to `"The ability to specify software versions"`.
  3. **Tools for Packaging and Distributing Software (line 21):** Change `"Contains are straightforward to create and they are automatically generated for every tool included into Bioconda"` to `"Containers are straightforward to create and are automatically generated for every tool included in Bioconda"`.
