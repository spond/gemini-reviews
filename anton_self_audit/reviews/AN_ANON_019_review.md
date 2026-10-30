# Review of AN_ANON_019

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript describes a suite of single-cell RNA-sequencing (scRNA-seq) analysis workflows, tool wrappers, format converters, and open educational tutorials integrated into a web-based bioinformatics platform and its global training network (GTN). The resource spans two primary analysis phases: (1) upstream preprocessing from raw FASTQ files to feature-count matrices via "1-click" droplet pipelines (RNA STARsolo as an open drop-in replacement for 10x Genomics Cell Ranger, alongside Salmon Alevin and scPipe) and customizable plate/microwell demultiplexing workflows (modeled on CEL-Seq2, SMART-seq2, and Drop-seq); and (2) downstream statistical analysis across five modular stages—filtering/QC (Scater), normalization, confounder regression (cell cycle removal), clustering/embedding (t-SNE, UMAP, Louvain), and pseudotime trajectory inference (ScanPy/PAGA and RaceID/StemID/FateID)—complemented by file converters across CSV, MTX, LOOM, and AnnData formats and interactive visualizations (cellxgene, Jupyter, RStudio).

This is a well-organized, community-backed training and workflow resource that lowers technical barriers for wet-lab biologists entering single-cell transcriptomics while enforcing version-locked reproducibility via Conda/Containers and Zenodo-archived tutorial datasets. However, as a scientific and methodological manuscript, it is entirely descriptive and includes no quantitative benchmarks of the integrated workflows (such as count-matrix concordance and runtime speedup between STARsolo, Cell Ranger, and Alevin on a reference dataset, or memory/cell-count scaling ceilings on the public server). Furthermore, several methodological statements in the text—such as encouraging users to "play with the plotting parameters to yield the best-looking clusters" in t-SNE/UMAP (line 101) or suggesting users mix an older version of ScanPy for QC with a newer version of ScanPy for clustering (line 38)—promote questionable analytical practices or overlook AnnData schema changes across ScanPy versions. Adding quantitative workflow benchmarks and correcting the statistical guidance around non-linear embeddings will strengthen the manuscript.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The single-cell portal and GTN provide end-to-end, version-locked workflows and open training materials spanning raw FASTQ demultiplexing to trajectory inference: [Well Supported].**  
  The workflow architecture (Figures 1–3, Supplemental Table 1), GitHub Tools-IUC wrapper repository, monthly GTN releases, and Zenodo-archived training datasets with permanent DOIs are thoroughly documented and openly accessible.

* **RNA STARsolo, Alevin, and scPipe workflows in the platform consume the same datasets and yield "approximately the same count matrices" as Cell Ranger with a 10-fold speedup: [Moderately Supported].**  
  While the speed and accuracy of STARsolo and Alevin relative to Cell Ranger are established in their respective upstream publications (references 24–27), the authors present no empirical benchmark within this manuscript demonstrating the exact cell-barcode overlap, gene count correlation, wall-clock execution time, or peak RAM consumption of their three "1-click" workflows on a shared tutorial dataset.

* **Users can seamlessly mix older and newer versions of ScanPy across stages of a workflow without compatibility issues: [Overstated].**  
  In line 38, the authors state that a user "could keep the quality control results obtained from an older version of ScanPy whilst running a newer ScanPy version at the clustering stage" and that "the burdens of software incompatibility... are now completely removed from the user." While Conda/Containers isolate the runtime dependencies of each individual step, the serialized `AnnData` (`.h5ad`) object passed between steps has undergone breaking schema changes across major ScanPy/anndata releases (e.g., changes in `.uns['neighbors']` storage and sparse matrix serialization between ScanPy 1.3, 1.4, and 1.6+), which can cause downstream tool wrappers to fail or misread neighborhood graphs when mixing tool versions.

* **Methodological guidance to "play with the plotting parameters to yield the best-looking clusters" in t-SNE/UMAP projections: [Methodologically Flawed].**  
  In line 101, while discussing t-SNE and UMAP embeddings, the text advises: "Ultimately the user is encouraged to play with the plotting parameters to yield the best-looking clusters." Encouraging beginners in a pedagogical resource to tune non-linear embedding hyperparameters (such as t-SNE perplexity or UMAP `n_neighbors` and `min_dist`) based on subjective visual appeal ("best-looking clusters") invites confirmation bias and p-hacking of visual cluster separation, especially when non-linear 2D embeddings distort global distances and density.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Quantitative Benchmark of the Pre-Processing and Downstream Workflows
* **WHY:** The manuscript makes specific quantitative claims about the integrated workflows (e.g., STARsolo's 10-fold speedup and "approximately the same count matrices" across STARsolo, Alevin, and scPipe on lines 62–64; RaceID scaling costs beyond 300–1,000 cells on line 79) without presenting a single data table or benchmark figure.
* **WHAT:** Add a compact benchmark table comparing the pre-processing (STARsolo, Alevin, scPipe) and downstream (ScanPy, RaceID, Scater) workflows on the standard Zenodo tutorial datasets.
* **HOW:** Run the Zenodo 10x tutorial dataset through the STARsolo, Alevin, and scPipe workflows on the public server and report: (1) wall-clock runtime and peak memory; (2) number of detected cell barcodes and median genes/UMIs per cell; (3) Pearson/Spearman correlation of per-cell UMI counts across methods; and (4) the maximum cell count $(N)$ that the ScanPy and RaceID workflows can process within the public server's memory quota.

#### 2. Revise the Pedagogical Guidance on t-SNE/UMAP Hyperparameter Tuning
* **WHY:** Instructing learners to "play with the plotting parameters to yield the best-looking clusters" (line 101) contradicts rigorous statistical practice in single-cell transcriptomics, where clustering (e.g., Louvain/Leiden) is performed on the high-dimensional PCA $k$-nearest-neighbor graph, not on the 2D t-SNE/UMAP coordinates, and where visual separation in 2D embeddings is sensitive to arbitrary `min_dist` and perplexity choices.
* **WHAT:** Rewrite line 101 to explain that clustering is determined in the high-dimensional neighborhood graph (independent of 2D plotting parameters) and that users should assess cluster robustness across parameter ranges using quantitative stability metrics (e.g., silhouette score, adjusted Rand index, or marker gene coherence) rather than visual aesthetics.
* **HOW:** Replace the sentence on line 101 with a clear explanation of the distinction between graph-based community detection (Louvain/Leiden on PCA space) and 2D manifold visualization (t-SNE/UMAP), warning users against visually cherry-picking embedding hyperparameters.

#### 3. Qualify Cross-Version Compatibility Claims for Serialized Object Formats (`AnnData` / `LOOM` / `RDS`)
* **WHY:** While containerization guarantees that each tool wrapper has its own locked library environment (line 38), passing binary `AnnData` (`.h5ad`) or R `SingleCellExperiment` (`.rds`) files between wrappers running different major versions of ScanPy or Bioconductor can still fail due to internal object schema changes.
* **WHAT:** Temper the claim on lines 38–40 that software incompatibility is "completely removed" and document how the platform handles `AnnData`/`LOOM` schema versioning across tool updates.
* **HOW:** Add a note in the Background/Methods clarifying that while containerization eliminates dependency conflicts between tools, workflows are tested and version-pinned as coherent suites to ensure `AnnData` and `SingleCellExperiment` object schema compatibility between sequential steps.

#### 4. Editorial Cleanup
* **WHY:** Minor typographical errors appear in the manuscript text.
* **WHAT & HOW:** Fix line 58 ("sequencing **lab oratoryas** to which" $\to$ "sequencing **laboratory as** to which") and line 62 ("not only because **is it** a feature update" $\to$ "not only because **it is** a feature update").
