# Review of AN_ANON_035

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.2/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This perspective article formulates ten practical rules for ensuring computational reproducibility in bioinformatics and quantitative biology: (1) tracking provenance and parameters of every result via executable workflows, (2) replacing manual file manipulation with scripted/automated transformations, (3) archiving exact versions of external binaries or virtual machine (VM) images, (4) version-controlling custom scripts (`Git`, `Subversion`, `Mercurial`), (5) recording standardized intermediate results to aid debugging and partial re-execution, (6) recording pseudo-random number generator (PRNG) seeds for stochastic analyses, (7) storing raw numerical data and plotting code behind figures, (8) generating hierarchical outputs (e.g., linked HTML summaries) to allow inspection of underlying distributions behind summary statistics, (9) linking textual claims in manuscripts/notes directly to specific analysis outputs (via literate programming or workflow pages), and (10) providing public access to input data, code, workflows, and results. Each rule distinguishes an ideal best practice (automated via command-line makefiles or workflow management systems) from an attainable minimum baseline for individual researchers.

This is a clear, well-structured, and pragmatic guide that effectively bridges daily researcher habits (self-reproducibility and productivity) with community-wide scientific transparency. Because it is a methodological commentary rather than an empirical study, its evaluation rests on the technical precision and completeness of the ten rules. While the core principles are sound, three technical nuances warrant refinement so that readers do not adopt false assumptions about bit-level determinism or storage scalability: (1) Rule 6 asserts that providing the same PRNG seed guarantees *"identical results every time it is run"*, which fails to account for multi-threaded/GPU race conditions, non-associative floating-point reductions, and cross-platform library/hardware differences; (2) Rules 3 and 5 emphasize monolithic full-OS virtual machine images and storing all intermediate files without discussing lightweight declarative environments/checksums when intermediate NGS files span terabytes; and (3) Rule 10 calls for making all input data and intermediate results publicly accessible without noting privacy-mandated controlled-access protocols for identifiable human clinical/genomic cohorts.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Executable workflows (Rule 1), scripted data transformations (Rule 2), version control of custom scripts (Rule 4), and literate/hyperlinked coupling of figures and text to underlying data (Rules 7–9) prevent documentation drift and hidden manual errors: [Well Supported].**  
  The distinction between manual note-taking (which rapidly drifts out of sync with iterative re-analyses) and executable specifications (shell scripts, `Makefiles`, workflow management systems, and `Sweave`/workflow pages) is technically accurate and directly addresses the primary failure modes of computational studies.

* **Providing the same initial random seed guarantees that stochastic analyses will produce identical results every time they are executed (Rule 6): [Overstated].**  
  In Rule 6 (line 61), the authors state: *"However, given the same initial seed, all random numbers used in an analysis will be equal, thus giving identical results every time it is run."* In practice, fixing a single top-level PRNG seed is necessary but often insufficient for exact bitwise reproduction: (i) in multi-threaded (OpenMP/pthreads), distributed (MPI), or GPU-accelerated bioinformatics tools, thread execution order is non-deterministic unless per-thread/per-task substream seeds (e.g., L'Ecuyer-CMRG or counter-based PRNGs) and deterministic reductions are enforced; (ii) IEEE 754 floating-point addition is non-associative, so different SIMD instruction sets (AVX2 vs. AVX-512 vs. ARM NEON) or BLAS libraries yield slightly different numerical trajectories; and (iii) PRNG implementations and default hash seeds can change across language/library versions.

* **Archiving full virtual machine (VM) images (Rule 3) and permanently storing all intermediate results and hierarchical drill-down files (Rules 5 and 8) ensures long-term executability and inspectability: [Moderately Supported].**  
  Storing a full OS virtual machine image preserves binary dependencies, and retaining intermediate results enables rapid bisection of pipeline discrepancies. However, in high-throughput sequencing and large-scale simulation studies, intermediate files (e.g., unaligned SAM/FASTQ intermediates or per-iteration MCMC states) frequently exceed raw inputs by $5\text{–}20\times$, making permanent storage of all intermediate files impractical unless paired with cryptographic hashes (MD5/SHA-256) of deterministic intermediates and lightweight declarative package specifications.

* **All input data, scripts, versions, parameters, and intermediate results should be made publicly and easily accessible (Rule 10): [Moderately Supported].**  
  While open deposition in domain repositories is the gold standard for non-sensitive data, Rule 10 does not mention ethical and legal privacy constraints on human genomic and clinical data (e.g., HIPAA/GDPR and participant consent requiring deposition in controlled-access repositories such as dbGaP or EGA), where full reproducibility is achieved by pairing controlled-access raw data accessions with publicly available de-identified/synthetic test datasets and open source code.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Qualify Rule 6 Regarding Parallel, Floating-Point, and Cross-Platform Non-Determinism
* **WHY:** Readers who set `set.seed()` or `--seed` in a multi-threaded or GPU-accelerated pipeline frequently observe slight numerical differences across runs or across machines and may wrongly conclude their workflow is broken—or conversely assume that setting a single seed guarantees bit-identical results under parallel execution.
* **WHAT:** Expand Rule 6 by 2–3 sentences explaining when a fixed PRNG seed is sufficient (single-threaded execution on the same software/hardware stack) versus when parallel thread scheduling, floating-point non-associativity, or PRNG library updates can still introduce minor numerical variance.
* **HOW:** Recommend recording both the PRNG seed and the number of threads/processes (or using parallel-safe stream-splitting PRNGs) and verifying that scientific conclusions are robust across multiple random seeds (sensitivity analysis) rather than relying on a single lucky seed.

#### 2. Balance Rule 5 and Rule 8 Against Storage Constraints Using Checksums and Selective Checkpointing
* **WHY:** In large-scale genomics workflows, storing every intermediate file (Rule 5) and generating full un-summarized HTML drill-down trees for all data points (Rule 8) can consume tens of terabytes and become a barrier to archiving.
* **WHAT:** Suggest recording cryptographic checksums (`md5sum` / `sha256sum`) and summary diagnostics of large, deterministically regenerable intermediate files when full file retention is storage-prohibitive, while archiving compact post-alignment/post-filtering checkpoints.
* **HOW:** Add a practical rule-of-thumb in Rule 5 distinguishing bulky transient intermediates (where recording the command + SHA-256 checksum suffices) from expensive or non-trivial checkpoints (which should be archived in standardized indexed formats such as BAM/CRAM/VCF/HDF5).

#### 3. Address Controlled-Access Human Data and Synthetic Test Datasets in Rule 10
* **WHY:** Biomedical researchers working with patient genomes or electronic health records cannot legally post raw input data or individual-level intermediate files on public web servers.
* **WHAT:** Clarify in Rule 10 how to satisfy computational reproducibility when raw inputs are subject to participant privacy protections.
* **HOW:** Note that when human data must reside in controlled-access repositories (e.g., dbGaP, EGA), authors should (i) document the exact controlled-access study/dataset identifiers and access procedure, and (ii) provide a small, non-sensitive or simulated example dataset alongside their public scripts/workflows so peers can verify that the code executes end-to-end.
