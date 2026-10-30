# Review of AN_ANON_015

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript describes the architectural integration of Jupyter (and RStudio) Interactive Environments (IEs) into a web-based bioinformatics workflow platform using isolated Docker containers. The system launches per-user Docker containers (built on `jupyter/minimal-notebook` with Python, R, Julia, Ruby, Haskell, and Octave kernels) via an Interactive Environment Entry Point (IEEP), communicates over SSL on randomized ports, and exposes custom `get()` and `put()` API functions to transfer datasets directly between the user's workflow history and the container without local workstation downloads. The authors demonstrate the hybrid workflow-plus-notebook paradigm across three examples: (1) visualizing read coverage across three simulated HIV-1 longitudinal resequencing samples; (2) running DESeq2 normalization and variance shrinkage on a 2-vs-2 subset of *Saccharomyces cerevisiae* WT vs. *snf2* knockout RNA-seq replicates (SRA ERP004763) mapped against `dm3` or yeast reference genomes; and (3) reproducing a published analysis of human mitochondrial heteroplasmy transmission across 312 FASTQ datasets from 39 mother-child pairs (156 samples, SRA SRP047378), recovering the positive correlation between maternal age and heteroplasmy count and estimating a germ-line bottleneck of ~40 segregating units.

The software architecture is well-conceived and solves a genuine usability and provenance gap between standardized GUI-based preprocessing and custom programmatic data exploration. All three examples are backed by live shareable workflow histories and supplementary notebook files (S1–S3 Files). However, the manuscript has several technical and methodological shortcomings: (1) it overstates the "utmost level of reproducibility" of interactive notebooks while permitting arbitrary on-demand `pip` package installations inside mutable containers that are not persisted once the container terminates; (2) there is a factual contradiction between the Figure 1B caption (which states the yeast *snf2* RNA-seq reads were mapped against the *Drosophila melanogaster* `dm3` genome) and the main text (which states they were mapped against the yeast genome); (3) Example 2 uses $n=2$ replicates per group from a 48-replicate benchmark study specifically designed to show that $n=2$ is underpowered; and (4) no system performance, container startup latency, or concurrency benchmarks are reported.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Docker-isolated Jupyter Interactive Environments enable secure, bidirectional data transfer with workflow histories without local downloads: [Well Supported].**  
  The Materials and Methods section (lines 19–27) clearly documents the IEEP architecture, Docker container isolation, SSL encryption, random port mapping, idle network-traffic termination, and the `get(dataset_id)` / `put(filename)` API bridge, and demonstrates end-to-end execution across three genomic workflows.

* **The hybrid platform scales to large multisample cohorts, processing 312 FASTQ datasets (118 GB) to reproduce published human mitochondrial heteroplasmy dynamics: [Well Supported].**  
  Example 3 (lines 59–62, Fig. 2) processes 312 paired-end Illumina datasets from 39 mother-child pairs through dataset collections (bwa-mem mapping to hg38, deduplication, quality/proper-pair filtering, indel realignment, and Naive Variant Caller) into a 2.6-million-row matrix (160 MB) and uses an embedded Jupyter notebook to replicate the published maternal age correlation and mitochondrial bottleneck estimate (~40 segregating units).

* **Saving Jupyter notebooks to the workflow history guarantees the "utmost level of reproducibility" during ad hoc data exploration: [Overstated].**  
  In lines 23 and 48, the authors state that users can install arbitrary packages on demand via `pip` or other kernel package managers inside the running container, and that saving the `.ipynb` notebook to the workflow history "ensures the reproducibility of data analysis." However, when the container is terminated on page close (line 23), any on-demand `pip` packages installed in the ephemeral container layer are destroyed. Re-opening the saved `.ipynb` file in a fresh default container will fail or use different library versions unless the exact environment specification (`requirements.txt` / Conda lockfile) or committed container image digest is captured alongside the notebook. Additionally, Jupyter notebooks permit out-of-order cell execution, which can break linear reproducibility if hidden state is not verified via clean top-to-bottom re-execution.

* **Example 2 demonstrates a valid RNA-seq normalization and variance-shrinkage workflow on *S. cerevisiae* WT vs. *snf2* mutants: [Fragile].**  
  First, there is a direct contradiction between the Figure 1B legend (line 51), which states that the WT and *snf2* knockout reads were mapped "against the *Drosophila melanogaster* genome (dm3) using HiSat split mapper" with `dm3` UCSC annotations, and the main text (line 57), which says they were mapped "against the yeast genome using HiSat" from Schurch et al. (SRA ERP004763, a *Saccharomyces cerevisiae* dataset). Mapping yeast reads against the fruit fly genome (`dm3`) is either a major figure-caption error or a bioinformatic mistake in the screenshot workflow. Second, subsetting the 48-replicate Schurch et al. dataset down to just $n=2$ replicates per condition provides minimal degrees of freedom for empirical Bayes dispersion shrinkage in DESeq2.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Resolve the *Drosophila* (`dm3`) vs. *S. cerevisiae* Reference Genome Contradiction in Example 2
* **WHY:** Line 51 (Figure 1B caption) explicitly states that *snf2* knockout RNA-seq reads were mapped against the *Drosophila melanogaster* (`dm3`) genome and annotated with `dm3` genes from the UCSC Table Browser, whereas line 57 states the dataset is *Saccharomyces cerevisiae* (ERP004763) mapped against the yeast genome.
* **WHAT:** Audit the live history (`http://bit.ly/rnaseq-jupyter`) and Figure 1B screenshot to determine whether the wrong reference genome (`dm3` instead of `sacCer3`) was used in the workflow or whether the Figure 1B legend was miswritten.
* **HOW:** If the workflow mapped yeast reads to `dm3`, re-run the HiSat and HTSeq-count steps against the *S. cerevisiae* reference genome (`sacCer3` / Ensembl R64), update Figure 1B and S2 File, and consider using at least $n=6$ replicates per condition (as recommended by Schurch et al.) rather than $n=2$. If only the caption is wrong, correct line 51 to state *S. cerevisiae* (`sacCer3`).

#### 2. Capture Ephemeral Package Dependencies to Ensure True Notebook Reproducibility
* **WHY:** Allowing users to run `pip install` inside an ephemeral Docker container (line 23) while only saving the `.ipynb` file back to the workflow history (line 27) means that custom library dependencies and versions are lost when the container stops.
* **WHAT:** Automatically record the container image digest and package environment state whenever a notebook is saved to the history, and temper the claim of "utmost level of reproducibility" (line 48) to acknowledge notebook state and dependency caveats.
* **HOW:** Modify the shutdown/save hook of the IEEP so that `pip freeze` / `conda list --explicit` (and the Docker image SHA256 digest) are exported as metadata or as an accompanying environment file in the workflow history, and recommend executing `Restart & Run All` before archiving a notebook.

#### 3. Quantify Container Startup Latency, Data Transfer Speed, and Multi-User Scaling
* **WHY:** The Methods section describes launching isolated Docker containers per user and transferring datasets via `get()` and `put()` over HTTP/SSL, including a 160 MB (2.6-million-row) variant table in Example 3, but reports no empirical performance metrics.
* **WHAT:** Add a brief benchmark paragraph or table reporting container startup time, memory overhead per active Jupyter container, and `get()`/`put()` transfer throughput across dataset sizes (e.g., 10 MB, 160 MB, 1 GB).
* **HOW:** Time the IEEP launch sequence and `get`/`put` API calls on the production server across 10 replicates for each file size, and state the hardware resource limits (CPU cores and RAM allocation per container) enforced on the public server.
