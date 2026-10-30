# Review of AN_ANON_062

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This community resource and software update manuscript summarizes two years of architectural, interface, and ecosystem developments in the web-based `[WORKFLOW_PLATFORM]` (Galaxy) workbench. Key technical additions include hierarchical dataset collections with key-value group tags (demonstrated on multi-factor RNA-seq differential expression with `DESeq2`), a cross-history/cross-library dataset selector dialog, Interactive Tools (`Jupyter`, `RStudio`, `cellxgene`) integrated into the standard tool configuration schema, federated authentication via OpenID Connect (OIDC) paired with short-lived token delegation for direct data transfers between `[WORKFLOW_PLATFORM]` and cloud object stores (AWS S3, Azure, Google Cloud Storage), single-hop remote job staging via `[SOFTWARE_PACKAGE]` (Pulsar), a YAML-based workflow specification, and newly wrapped domain suites for single-cell omics (`Seurat`, `Scater`), machine learning (`Scikit-learn`, `TensorFlow`), and bioimaging (`ImageJ`). The paper also documents the global infrastructure (>7,500 ToolShed wrappers, >36,000 Singularity containers for Bioconda packages, 5.6 TB of CVMFS-distributed reference data across US, European, and Australian flagships and >125 public servers) and training network (155 tutorials across 20 topics).

As a resource report for a major open-source bioinformatics infrastructure, the engineering enhancements—particularly CVMFS/Singularity container synchronization across continental flagships, OIDC least-privilege token delegation, and rule-based dataset collection tagging—directly address real bottlenecks in large-scale multi-sample biomedical workflows. However, the manuscript has three notable weaknesses: (1) it claims that Interactive Tools (`Jupyter`, `RStudio`) "inherit all the capabilities of existing Galaxy tools" alongside the blanket assertion that "Reproducibility is ensured, as Galaxy automatically captures execution information," without addressing how arbitrary interactive state mutations inside a live RStudio/Jupyter session break deterministic workflow provenance; (2) architectural performance claims regarding single-hop remote job data staging and scheduling "complex workflows involving thousands of datasets" lack quantitative throughput or latency benchmarks; and (3) Table 1 ("Members of the four major regional Galaxy teams–Africa, Australia, Europe and North America") is truncated mid-way through the European team (ending at letter K) and omits the entire North American team.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Global infrastructure coherence across US, European, and Australian flagship servers is maintained via >7,500 ToolShed wrappers, >36,000 Bioconda-derived Singularity containers, and 5.6 TB of shared reference data: [Well Supported].**  
  The manuscript documents a concrete, verifiable software distribution architecture where tool dependencies are encapsulated in versioned Bioconda packages and Singularity containers alongside shared reference indices, ensuring that standard non-interactive tools execute in identical software environments across federated deployments.

* **Hierarchical dataset collections and key-value group tags enable structured multi-factor experimental designs (such as `DESeq2` condition/replicate comparisons) across hundreds of files: [Well Supported].**  
  Figures 1 and 2 and the accompanying description clearly demonstrate how paired-end lists and factor-level group tags (`Smoker`, `Replicate 1`) propagate through collection-aware tool wrappers without manual file-by-file selection.

* **Starting an Interactive Tool (`Jupyter`, `RStudio`, `cellxgene`) "inherits all the capabilities of existing Galaxy tools" within a platform where "Reproducibility is ensured, as Galaxy automatically captures execution information": [Overstated].**  
  In line 12, the authors state that reproducibility is ensured because the platform automatically captures tool versions, inputs, outputs, and parameters. In line 79, they state that starting an Interactive Tool (`Jupyter`, `RStudio`) is no different from invoking any other tool and inherits all capabilities of existing tools. However, an open-ended interactive RStudio or Jupyter session permits ad hoc command execution, out-of-order cell evaluation, interactive GUI filtering (e.g., in `cellxgene`), and runtime package installation (`install.packages` / `pip install`) that are not automatically recorded as deterministic, non-interactive tool parameters in the Galaxy history unless specific notebook-capture and environment-freezing mechanisms are enforced.

* **Single-hop remote job staging via `[SOFTWARE_PACKAGE]` and workflow engine improvements provide "efficient scheduling of complex workflows involving thousands of datasets": [Moderately Supported].**  
  While bypassing the central server during remote input fetching (Figure 4) logically reduces network hops from two to one, the manuscript provides no quantitative metrics—such as workflow scheduling throughput (jobs/second), collection size scaling limits, or wall-clock transfer savings—to empirically benchmark these engine improvements.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restore the Missing European (L–Z) and North American Entries in Table 1
* **WHY:** Line 20 states that contributors are listed in Table 1 ("Members of the four major regional Galaxy teams–Africa, Australia, Europe and North America"). However, Table 1 (lines 25–59) lists Africa, Australia, and Europe up to "KWS SAAT SE & Co. KGaA" (alphabetized by affiliation), cutting off the remainder of Europe (L–Z) and the entire North America section.
* **WHAT & HOW:** Restore the missing rows of Table 1 so that all European institutions (L–Z) and all North American team members and affiliations are included as promised by the table title and text.

#### 2. Explicitly Clarify Provenance Boundaries and Best Practices for Interactive Tools
* **WHY:** Equating live interactive environments (`RStudio`, `Jupyter`, `cellxgene`) with deterministic CLI tool wrappers overstates automatic reproducibility: if a user modifies data interactively inside RStudio and saves an output file back to the history, another user inspecting the history cannot automatically replay the exact transformations unless the executed code script and container state were captured.
* **WHAT:** Qualify the reproducibility discussion in lines 77–83 to distinguish between exploratory interactive sessions and deterministic batch workflows, and explain what provenance artifacts (e.g., saved `.ipynb` notebooks, `.Rhistory`/`.Rmd` scripts, and container digests) are persisted to the user's history when an Interactive Tool terminates.
* **HOW:** Add a paragraph in the Interactive Tools section detailing how users should transition from exploratory interactive analysis in `Jupyter`/`RStudio` to reproducible workflow execution (for instance, via `Papermill` parameterized notebook execution or converting stabilized scripts into standard Galaxy tool wrappers).

#### 3. Provide Quantitative Benchmarks for Workflow Scheduling and Single-Hop Data Transfers
* **WHY:** Claims of "efficient scheduling of complex workflows involving thousands of datasets" (line 95) and "more secure and efficient job execution" via single-hop `[SOFTWARE_PACKAGE]` staging (lines 90–94) are presented purely qualitatively.
* **WHAT:** Report empirical benchmark numbers comparing workflow scheduling latency and remote data staging throughput before and after the architectural updates.
* **HOW:** Add a supplementary table or brief quantitative summary reporting (1) workflow invocation and step-scheduling time for a 1,000-sample collection workflow across recent release versions, and (2) total data transfer time and server I/O load for staging a 50 GB dataset collection from S3/object storage to a remote compute node via direct `[SOFTWARE_PACKAGE]` pull versus the legacy two-hop relay.
