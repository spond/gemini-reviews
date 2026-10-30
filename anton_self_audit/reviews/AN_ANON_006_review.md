# Review of AN_ANON_006

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound)  
**Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This perspective article examines software usability, dependency management, runtime reproducibility, and user training across molecular evolution and population genetics tools. Motivated by an informal survey of 23 software Methods and Resource articles published in *Molecular Biology and Evolution* (*MBE*) between January `[YEAR]` and March `[YEAR]`—in which 22 of 23 tools provided open-source code on GitHub or CRAN, but only 3 were judged to provide sufficient documentation/tutorials for straightforward installation and use (plus 2 packaged in Bioconda)—the authors outline a three-part modernization strategy for evolutionary software developers. Using IQ-TREE as a concrete worked example (Figure 1), they demonstrate how: (1) packaging tools in Conda/Bioconda eliminates manual compilation and dependency resolution while automatically generating isolated Docker/Singularity containers with pinned versions; (2) wrapping Conda-packaged tools into integrative workflow platforms (`[WORKFLOW_PLATFORM]` / Galaxy, augmented with Jupyter and RStudio Interactive Environments) allows end-to-end multi-tool analyses without command-line installation; and (3) developing FAIR, Markdown-based, community-reviewed tutorials via the Galaxy Training Network (GTN) addresses the training gap for biomedical researchers entering evolutionary genomics. Supplementary Table S1 and public repository URLs (`bioconda.github.io`, `training-material`) are provided.

The practical recommendations at the heart of the manuscript—adopting Bioconda and Linux containers for version-pinned binary distribution, avoiding isolated single-purpose web servers that cannot chain upstream alignment or downstream statistical steps, and investing in hands-on tutorials—are timely, technically accurate, and directly useful to the evolutionary biology software community. The primary methodological weakness lies in the lack of a transparent, reproducible evaluation rubric for the 23-paper *MBE* usability audit cited to motivate the piece: the main text does not state how many total *MBE* software papers were published prior to filtering, what objective criteria separated the 3 "usable" tools from the remaining 20 (especially given that CRAN packages undergo automated installation checks and mandatory documentation), or whether installation was tested systematically in a clean environment. Formalizing the audit criteria in the text will align the empirical survey with the transparency standards advocated by the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Packaging evolutionary biology tools in Conda/Bioconda and software containers (Docker/Singularity) streamlines installation and enables version-pinned runtime reproducibility: [Well Supported].**  
  Figure 1A–B and the accompanying text accurately contrast manual CMake/C++ source compilation against one-line `conda install` and `docker run` execution for IQ-TREE (v1.5.5), and appropriately note that containerization isolates host-kernel environment leakage that can still affect bare Conda virtual environments (citing Beaulieu-Jones and Greene `[YEAR]` and Kurtzer et al. `[YEAR]`).

* **Single-purpose web servers have limited utility for end-to-end evolutionary analyses compared with composable tools in integrative environments or workflow engines: [Well Supported].**  
  The critique in "Going Forward" (line 46)—pointing out that stand-alone web portals for individual phylogenetic algorithms (such as a standalone tree-building server) force users to manually format and shuttle intermediate alignments across incompatible web interfaces, whereas integrating Conda packages into multi-tool platforms (`[WORKFLOW_PLATFORM]`) and interactive notebooks (Jupyter/RStudio IEs) supports complete raw-reads-to-phylogeny pipelines—is well reasoned and grounded in real user bottlenecks.

* **Community-curated, Markdown-based hands-on tutorials (modeled on Software/Data Carpentry and FAIR principles via the GTN) lower the barrier to evolutionary analysis: [Well Supported].**  
  The architectural description of the GitHub-hosted training repository (`training-material`) and its active network of 33 scientific groups provides verifiable evidence of a scalable educational framework.

* **In a survey of 23 recent *MBE* software papers (22 on GitHub/CRAN), "only three tools contained enough information (documentation and/or tutorials) to actually be easily installed and used": [Fragile].**  
  While the broader point that academic bioinformatics tools often suffer from poor documentation is widely recognized, the specific quantitative claim (`3/23` usable) lacks methodological documentation in the main text:
  1. *Unspecified evaluation rubric:* The text combines two distinct criteria—"easily installed" and "used (documentation and/or tutorials)"—into a single binary pass/fail outcome without defining the rubric. Notably, tools deposited on CRAN (explicitly included in the 22 open-source tools on line 11) are required by CRAN policy to pass automated multi-platform build checks and include standardized function documentation and vignettes, making it unclear why CRAN packages failed the installation/documentation threshold unless a specific style of tutorial was required.
  2. *Unreported denominator before paywall/abstract-URL filtering:* Line 11 notes that the authors examined only articles that were either open-access or included a software URL directly in the abstract, without reporting how many total *MBE* Methods/Resource papers were published during the January–March window and excluded by this filter.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Explicitly Define the Evaluation Rubric and Denominator for the 23-Paper *MBE* Usability Survey
* **WHY:** Reporting that only 3 of 23 published tools can "actually be easily installed and used" (line 11) is a striking empirical finding, but without a stated rubric in the main text, readers cannot tell whether tools failed due to broken compilation, missing dependencies, lack of a README, or absence of a narrative tutorial with sample data.
* **WHAT:** Disaggregate the survey results for the 23 tools into explicit, verifiable binary dimensions in the main text (matching Supplementary Table S1).
* **HOW:** Expand the paragraph on line 11 by 3–4 sentences to report: (1) the total number of *MBE* Methods/Resource articles published between January `[YEAR]` and March `[YEAR]` before applying the open-access/abstract-URL filter; (2) the exact split between GitHub repositories and CRAN packages among the 22 open-source tools; and (3) separate pass counts for (a) *working installation instructions / package manager availability*, (b) *API/command-line reference documentation*, and (c) *end-to-end tutorial with example input/output datasets*.

#### 2. Acknowledge Command-Line Workflow Managers (Snakemake, Nextflow) Alongside Web-Based Integrative Frameworks
* **WHY:** In the "Integrative Frameworks" and "Going Forward" sections (lines 26–30, 46), the text frames the ecosystem primarily as a dichotomy between single-purpose web servers and the web-based `[WORKFLOW_PLATFORM]` GUI. In population genetics and molecular evolution, many power users chain Bioconda packages and Singularity containers using command-line workflow engines (e.g., Snakemake, Nextflow, CWL) on institutional HPC clusters.
* **WHAT:** Note that wrapping tools into Bioconda/BioContainers simultaneously enables *both* GUI-based integrative environments (`[WORKFLOW_PLATFORM]`) and command-line workflow managers (Snakemake/Nextflow).
* **HOW:** Add two sentences in line 30 or line 44 pointing out that once a developer contributes a Bioconda recipe for their evolutionary tool, that exact package and auto-generated container can be invoked seamlessly by `[WORKFLOW_PLATFORM]`, Snakemake (`--use-conda` / `--use-singularity`), Nextflow, and CWL pipelines alike, multiplying the developer's return on effort.

#### 3. Technical and Editorial Corrections
* **WHY:** Several typographical and grammatical errors appear in the main text and Figure 1 legend.
* **WHAT & HOW:**
  1. *Line 11:* Change `"Two additional tools has been added to Bioconda"` to `"Two additional tools have been added to Bioconda"`.
  2. *Line 14 (Figure 1B legend):* Change `"Because IQ-Tree is available from Bioconda (...) is can be installed"` to `"it can be installed"`; and change `"Ability of specify software versions"` to `"Ability to specify software versions"`.
  3. *Line 21:* Change `"Contains are straightforward to create"` to `"Containers are straightforward to create"`.
