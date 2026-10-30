# Review of AN_ANON_025

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a community-driven educational and training infrastructure built around a web-based biomedical workflow platform. Inspired by Software and Data Carpentry, the authors developed a centralized GitHub repository hosting Markdown-based hands-on tutorials, HTML slide decks, extracted computational workflows, interactive browser tours (via a Tour Builder plugin), downsampled Zenodo-archived benchmark datasets (with DOIs), and topic-specific Docker images for offline/on-demand deployment. Each tutorial is annotated with YAML metadata linked to the EDAM bioinformatics ontology to automatically populate the ELIXIR TeSS training portal under FAIR principles, and undergoes continuous integration (CI) testing for HTML generation and broken links/images upon pull request submission. Across 11 major topics (including Assembly, ChIP-Seq, Epigenetics, Metagenomics, Proteomics, Sequence Analysis, Transcriptomics, Administration, Development, and Instructor Training), the network has engaged over 60 contributors and 33 scientific groups under a CC-BY 4.0 license.

This is a well-architected, fully open-source community resource paper whose software engineering, FAIR metadata integration (YAML/EDAM/TeSS), Zenodo dataset archival, and containerized offline reproducibility are exemplary. Its primary limitation is that while the technical infrastructure for content creation is thoroughly validated, the manuscript provides no quantitative pedagogical or operational evaluation of learner outcomes, tutorial execution pass rates against live tool updates, or long-term maintenance verification of the topic Docker containers. In addition, the abstract and final section make sweeping claims about precipitating a "complete re-engineering of undergraduate and graduate curricula" and teaching "fundamental statistical and data science topics," whereas Table 1 currently contains domain tool pipelines without dedicated statistical inference or experimental design modules. These limitations can be addressed by adding empirical usage/evaluation metrics and tempering the curricular scope claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A GitHub-based Markdown/YAML architecture with automated pull-request CI testing, EDAM ontology mapping, and ELIXIR TeSS integration supports scalable, community-led bioinformatics tutorial development: [Well Supported].**  
  The repository structure (Figure 2) cleanly standardizes topic metadata, slide decks, Markdown tutorials, interactive tour scripts, workflows, Zenodo data links, and tool manifests. The fork-and-pull-request editorial workflow has already onboarded >60 contributors and 33 participating training groups across 11 life-science domains (Table 1, Figure 3).

* **Coupling Zenodo-archived downsampled datasets with automated topic-specific Docker images ensures portable, self-contained tutorial execution across public servers and offline environments: [Well Supported].**  
  Downsampling published empirical datasets to minimal sizes that still yield biologically interpretable outputs (archived with persistent DOIs on Zenodo) solves the runtime bottleneck of live workshops, while generating topic-specific Docker flavors directly from each tutorial's declarative tool configuration file provides a reproducible fallback when public servers are overloaded or internet connectivity is limited.

* **Automated CI checks guarantee that tutorials remain current and functional against evolving software tools and workflows: [Moderately Supported].**  
  In the section "Infrastructure to facilitate community-led content development" (line 168), the authors state that when a pull request is created, "the newly added content is automatically tested for HTML generation and all links and images are verified." While syntactic HTML/link checking prevents broken web pages, it does not test whether the underlying bioinformatics tools, parameter names, or extracted workflows inside the tutorial still execute and produce the expected biological outputs when tool versions are updated on public servers.

* **The framework expands training to "fundamental statistical and data science topics" and precipitates a "complete re-engineering of undergraduate and graduate curricula": [Overstated].**  
  In the Abstract (line 122) and "A vision for the future" (line 188), the authors emphasize statistical reasoning (such as experimental replication in RNA-seq) and university curriculum re-engineering. However, inspection of the entire tutorial catalog in Table 1 (lines 145–156) shows zero tutorials dedicated to foundational biostatistics, experimental design, power/replication analysis, or false discovery rate control, and no case studies or adoption data from formal undergraduate/graduate degree curricula are presented.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Extend Continuous Integration from Static HTML/Link Checking to Automated Workflow Execution Testing
* **WHY:** Verifying only Markdown-to-HTML compilation and valid URLs (line 168) allows "tutorial rot," where a tutorial page renders cleanly on the website while its step-by-step tool parameters or Zenodo inputs fail on current platform releases due to tool wrapper upgrades.
* **WHAT:** Add automated workflow execution testing to the CI pipeline so that each tutorial's companion workflow is periodically executed against its Zenodo input datasets.
* **HOW:** Since each tutorial directory already includes a `workflows/` subdirectory, a `data-library.yaml` file (Zenodo links), and a `tools.yaml` list (line 170), configure a scheduled CI job that spins up the topic Docker container, imports the Zenodo test data, executes the tutorial workflow via the platform API, and flags any tutorial whose workflow fails or whose outputs diverge from expected assertions.

#### 2. Report Quantitative Learner Feedback, Web Analytics, and Workshop Evaluation Summaries
* **WHY:** The manuscript reports the number of contributors (>60) and registered events (Figure 3), but includes no empirical learner metrics (e.g., pre-/post-workshop comprehension surveys, tutorial completion rates, interactive tour usage, or page views) to substantiate the effectiveness of the side-by-side interactive format and question boxes.
* **WHAT:** Summarize post-workshop trainee survey results and web/Zenodo usage statistics collected across the GTN events shown in Figure 3.
* **HOW:** Add a concise subsection or table reporting: (i) total learners trained across the registered GTN workshops in Figure 3A, (ii) standardized post-workshop feedback scores (e.g., clarity of research stories, usefulness of question boxes and interactive tours), and (iii) Zenodo dataset download counts and Docker image pull statistics per topic.

#### 3. Align Claims Regarding Statistical Training and University Curricula with Table 1 Content
* **WHY:** Claiming in the Abstract (line 122) and Discussion (line 188) that the resource teaches fundamental statistical concepts (e.g., RNA-seq sample size/replication) is not yet matched by the actual catalog in Table 1, which focuses on bioinformatic tool execution.
* **WHAT:** Clearly distinguish between currently deployed domain pipelines (Table 1) and planned statistical/curricular extensions, or document specific statistical concepts already embedded within existing tutorials (e.g., dispersion estimation and FDR in the Transcriptomics RNA-seq tutorials).
* **HOW:** Revise the Abstract and Discussion to frame foundational statistics modules and university curriculum integration as explicit next-phase roadmap goals, and add a column to Table 1 indicating which quantitative/statistical concepts (e.g., multiple hypothesis testing, normalization, clustering) are covered within each existing domain tutorial.
