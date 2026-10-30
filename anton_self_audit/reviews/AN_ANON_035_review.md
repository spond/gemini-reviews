# Review of AN_ANON_035

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is a concise methodological perspective and best-practices guide presenting "Ten Simple Rules" for ensuring computational reproducibility in bioinformatics and quantitative life-science research. Framed around the distinction between independent *replication* (repeating a study on newly collected data) and computational *reproducibility* (repeating and extending data analyses on the original dataset), the authors organize practical habits and technical mechanisms into ten actionable rules: (1) tracking how every result was produced via executable workflows (`Makefiles`, shell scripts, or integrated platforms like `GenePattern`, `Galaxy`, `LONI`, and `Taverna`); (2) replacing manual data manipulation (e.g., spreadsheet copy-pasting) with scripted converters; (3) archiving exact versions of external binaries or full virtual machine images; (4) placing custom scripts under version control (`Subversion`, `Git`, `Mercurial`); (5) recording standardized intermediate results; (6) recording pseudo-random number generator (PRNG) seeds for stochastic analyses; (7) storing raw and processed numerical data plus plotting code (`R`) behind every figure; (8) generating hierarchical drill-down outputs (e.g., hypertext/HTML summaries linked to underlying distributions); (9) linking textual claims in notes and manuscripts directly to result identifiers via literate programming tools (`Sweave`, `GenePattern` Word add-in, `Galaxy Pages`); and (10) providing public access to input data, code, parameters, and run histories upon publication.

Evaluated as a short perspective/editorial piece, the manuscript is well-organized, pragmatic, and realistic about the day-to-day pressures faced by computational researchers. A particularly useful design feature is that every rule explicitly defines both a *gold-standard automated implementation* and a *minimum viable baseline* ("As a minimum..."), lowering the barrier to adoption for investigators transitioning from ad-hoc scripting to structured workflows. Because this is a brief conceptual commentary rather than an empirical research study, its limitations are primarily omissions of important technical nuances in computational reproducibility—specifically hardware/parallel floating-point non-determinism (even when PRNG seeds are fixed under Rule 6), ethical/privacy constraints on sharing sensitive human genomic/clinical data under Rule 10, and database/annotation versioning alongside software binary archiving under Rule 3.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Structured workflow tracking, scripted data manipulation, version control, and software environment archiving (Rules 1–5) prevent irreproducible drift between documented methods and executed analyses: [Well Supported].**  
  The combinatorics of software versions, command-line flags, and pre-processing filters make post-hoc reconstruction from memory virtually impossible (Introduction, line 19). Distinguishing between manual notes (which rapidly fall out of sync with re-runs) and executable workflow specifications (`Makefiles`, shell scripts, workflow management systems) accurately captures the primary source of bioinformatics pipeline failure.

* **Fixing and recording the underlying random seed guarantees identical results every time a stochastic analysis is executed (Rule 6): [Overstated].**  
  In Rule 6 (line 61), the authors state: *"However, given the same initial seed, all random numbers used in an analysis will be equal, thus giving identical results every time it is run."* In real-world scientific computing, fixing a single PRNG seed is necessary but often **not sufficient** for bit-for-bit identical output across runs or machines, for three reasons: (1) multi-threaded parallel execution (`OpenMP`, `MPI`, `pthreads`, or GPU kernels) introduces non-deterministic thread scheduling and non-associative IEEE 754 floating-point summation unless thread-indexed substream PRNGs and deterministic reductions are enforced; (2) changing the version of the underlying math library (`BLAS`/`LAPACK`, `glibc`) or language runtime (`R`, `Python`) can alter the PRNG algorithm or floating-point rounding even for the same seed; and (3) relying on a single fixed seed can mask algorithm instability if a fragile result only holds for that specific seed rather than across an ensemble of seeds.

* **Storing raw plot data, hierarchical drill-down summaries, and literate-programming links between prose and outputs (Rules 7–9) streamlines reanalysis and peer verification: [Well Supported].**  
  Separating raw unbinned observations from binned histogram counts (Rule 7), exposing summary statistics via linked HTML drill-down reports (Rule 8), and binding manuscript claims to exact analysis artifacts via `Sweave` or workflow pages (Rule 9) directly address the common failure mode where summary figures conceal upstream data-processing artifacts or cannot be traced back to specific parameter runs during peer review.

* **Providing public access to all input data, scripts, versions, parameters, and intermediate results (Rule 10) is universally achievable via supplementary material or open repositories: [Moderately Supported].**  
  While public deposition in domain repositories (e.g., microarray/gene expression databases) is appropriate for model-organism and non-sensitive datasets, Rule 10 does not mention how researchers should handle human clinical or identifiable genomic data governed by patient consent and privacy laws, where raw inputs and individual-level intermediate files must be deposited in controlled-access repositories (e.g., `dbGaP`, `EGA`) while keeping the analysis code, containers, and synthetic/summary test data openly executable.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Qualify Rule 6 to Address Parallel Non-Determinism and Seed Sensitivity
* **WHY:** Telling readers that a fixed random seed guarantees identical results every time a program is executed overlooks multi-threaded race conditions, hardware/library floating-point discrepancies, and the statistical danger of relying on a single fragile seed in Monte Carlo, MCMC, or bootstrapping analyses.
* **WHAT:** Expand Rule 6 by 3–4 sentences to distinguish bit-level reproducibility (single-threaded fixed seed) from statistical robustness across seeds and multi-threaded environments.
* **HOW:** Clarify in Rule 6 that (a) parallelized bioinformatics tools often require either setting a deterministic thread count or using parallel-safe PRNG streams to yield identical outputs for a given seed, and (b) while recording the exact seed is essential for exact auditability, researchers should verify that substantive scientific conclusions remain invariant across multiple independent random seeds.

#### 2. Expand Rule 3 to Include Reference Databases and Annotation Snapshots Alongside Software Binaries
* **WHY:** In bioinformatics and genomics, an analysis pipeline using the exact same software binary (`Rule 3`) and custom script (`Rule 4`) will still produce completely different results if external reference databases (`Ensembl` gene models, `dbSNP` build, `GenBank`/`NR`, `Gene Ontology`, or reference genome patch level) have been updated in the interim.
* **WHAT:** Explicitly include reference genome builds, annotation release numbers, and external database snapshots in Rule 3 (or Rule 1).
* **HOW:** Add two sentences to Rule 3 noting that external data dependencies—such as reference assemblies, gene annotation GTF/GFF releases, and ontology files—change just as frequently as software executables, and must therefore have their exact release dates/version numbers recorded and archived alongside the programs.

#### 3. Address Controlled-Access Human Data and Synthetic Test Fixtures in Rule 10
* **WHY:** Researchers working with clinical cohorts or identifiable human sequencing data cannot legally upload raw input files or individual-level intermediate results as journal supplementary material, and may mistakenly conclude that Rule 10 cannot apply to their work.
* **WHAT:** Add a brief note to Rule 10 explaining how to achieve computational reproducibility when raw data are subject to privacy restrictions.
* **HOW:** Specify that when ethical or legal rules require raw inputs to reside in controlled-access repositories (`dbGaP`, `EGA`), authors should (a) provide the controlled-access accession identifiers, and (b) include a small de-identified or simulated toy input dataset alongside their open-source scripts and workflows so peers and reviewers can verify that the full pipeline executes end-to-end.
