# Review of AN_ANON_025

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.9 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a community-driven, open-source training infrastructure designed to teach biomedical data analysis through interactive, narrative-driven tutorials coupled to a web-based bioinformatics workbench. The framework organizes training materials by biological and technical topics (Table 1; 11 topic tracks spanning genome assembly, ChIP-seq, transcriptomics, epigenetics, metagenomics, proteomics, sequence analysis, tool development, platform administration, and instructor training) inside a GitHub repository authored in Markdown. Each tutorial integrates learning objectives, formative question boxes, curated downsampled datasets archived on Zenodo with persistent DOIs, interactive browser-guided tours, extracted workflow definitions, YAML metadata annotated with EDAM ontology terms (automatically indexed into ELIXIR's TeSS portal), WAVE web-accessibility checks, and auto-generated per-topic Docker images that bundle the platform, required tools, workflows, and data for offline or local use.

This is a well-engineered, FAIR-compliant educational resource that solves practical pain points for both learners and instructors (software installation, dataset curation, broken tutorial links, and unreliable workshop internet connections), backed by active community adoption (>60 contributors and 33 participating groups). The main limitations are that (1) continuous integration (CI) testing on pull requests currently verifies HTML rendering, links, and image alt-text, but does not automatically execute the underlying tutorial workflows against the Zenodo datasets to detect tool regressions; (2) the manuscript provides no empirical learner or workshop evaluation metrics (e.g., completion rates, user surveys, or learning assessments); and (3) while the abstract and conclusion highlight the urgent need for statistical training, the current curriculum (Table 1) lacks dedicated modules on foundational biostatistics and experimental design. Adding automated workflow execution checks and reporting basic learner/usage analytics would make the paper even stronger.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The GitHub/Markdown architecture, EDAM-annotated YAML metadata, and Zenodo dataset archiving provide a scalable, FAIR-compliant infrastructure for community-led tutorial development: [Well Supported].**  
  The repository structure (Figure 2), pull-request review workflow, automated HTML/link/WAVE accessibility checks, CC-BY 4.0 licensing, ELIXIR TeSS integration, and growth to >60 contributors across 33 groups demonstrate a functional, sustainable open-science training ecosystem.

* **Topic-specific Docker containers and interactive browser tours ensure tutorial portability and learner engagement across heterogeneous computing environments: [Well Supported].**  
  Generating topic-flavored Docker images directly from declarative tool configuration files alongside preloaded workflows, interactive tours, and Zenodo dataset links directly addresses public server overload and limited classroom internet connectivity.

* **Downsampled published datasets preserve biological interpretability while enabling rapid classroom execution: [Moderately Supported].**  
  Curating compact, DOI-archived datasets from real studies is essential for live workshops. However, the manuscript does not discuss how downsampling affects statistical power, false discovery rates, or assembly contiguity, or how tutorials guard against trainees misinterpreting artifacts of aggressive subsampling as biological findings.

* **The training framework bridges the quantitative and statistical skills gap in life science curricula: [Moderately Supported].**  
  While the platform effectively demystifies bioinformatic pipelines across major omics modalities (Table 1), the authors' first guiding recommendation ("Require quantitative training... background level statistical reasoning must be included in all training materials") is not yet reflected in Table 1 as dedicated tutorials on experimental design, replication, power, or statistical inference.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Extend Continuous Integration to Automatically Test Tutorial Workflows on Zenodo Datasets
* **WHY:** Currently, pull-request CI validates Markdown-to-HTML generation, hyperlinks, and image alt-text, but does not verify that the tutorial's extracted workflow still runs to completion and produces the expected outputs when tool versions or dependencies change.
* **WHAT:** Integrate automated execution testing of the extracted workflows (`workflows/` directory in Figure 2) against the linked Zenodo test datasets within the CI or nightly build pipeline.
* **HOW:** Using the declarative tool list and workflow files already stored in each tutorial subdirectory, configure a CI job (or scheduled check against the topic's Docker image) that imports the Zenodo input files, executes the tutorial workflow via the platform API, and verifies non-empty, valid output datasets.

#### 2. Report Quantitative Usage, Workshop Feedback, and Self-Paced Completion Metrics
* **WHY:** Figure 3 reports the number of registered training events and monthly GitHub contributors, but the manuscript includes no empirical data on learner traffic, self-paced tutorial usage, or trainee feedback from the workshops organized by the 33 network groups.
* **WHAT:** Summarize available web analytics, Zenodo dataset download counts, Docker image pulls, and standardized post-workshop survey metrics.
* **HOW:** Add a summary table or panel to Figure 3 reporting page views per topic, total downloads of the curated Zenodo training records, Docker Hub pull counts for the topic containers, and aggregated trainee satisfaction/comprehension scores from past workshops.

#### 3. Document Pedagogical Guidelines for Downsampling Empirical Datasets
* **WHY:** Downsampling sequencing reads (e.g., for RNA-seq, ChIP-seq, or genome assembly) can distort coverage distributions, peak calling sensitivity, or differential expression $p$-values unless done carefully (e.g., restricting reads to a single chromosome rather than uniform 1% subsampling across the whole genome).
* **WHAT:** Explain the specific strategies used to downsample tutorial datasets in the "Train the trainers" documentation and main text.
* **HOW:** Add a brief paragraph in "Interactive learning tailored to research problems" contrasting chromosome/locus-restricted subsampling (which preserves realistic local read depth) against uniform random subsampling, and note how question boxes alert learners to the effects of reduced sample size.
