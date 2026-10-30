# Review of AN_ANON_019

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This resource and educational manuscript describes the single-cell RNA-sequencing (scRNA-seq) analysis ecosystem and accompanying Galaxy Training Network (GTN) curriculum deployed on the `singlecell.[WORKFLOW_PLATFORM]` and `humancellatlas.[WORKFLOW_PLATFORM]` portals. Addressing software version instability, R/Python language barriers, and file format incompatibilities (`SingleCellExperiment`, `SeuratObject`, `SCSeq`, `LOOM`, `AnnData`, `MTX`, `CSV`) in single-cell transcriptomics, the authors integrate Conda/container-isolated tools and format converters into Galaxy alongside six core step-by-step training workflows (three upstream preprocessing routes—`10X STARsolo`, `Alevin`/`scPipe`, and a customizable `CEL-Seq2`/manual barcode demultiplexing pipeline—and three downstream analysis pipelines built around `Scater`, `RaceID`/`StemID`/`FateID`, and `ScanPy`/`PAGA`), supplemented by interactive visualization environments (`cellxgene`, Jupyter, RStudio) at `live.[WORKFLOW_PLATFORM]`. All tutorial datasets and workflows are archived with permanent DOIs on Zenodo, and tool wrappers are maintained in the open-source GitHub `Tools-IUC` repository.

As a community training and reproducible workflow infrastructure effort, the manuscript provides an accessible, well-organized, and openly archived resource that lowers technical barriers for wet-lab biologists entering single-cell transcriptomics. However, as a scientific methods paper, it is entirely descriptive and includes zero quantitative benchmarks or empirical validation results in the main text—for example, claiming that `RNA STARsolo` achieves a "10-fold speedup in comparison to Cell Ranger" and that `STARsolo`, `Cell Ranger`, `Alevin`, and `scPipe` "yield approximately the same count matrices" (lines 62, 64) without showing a single comparison table, correlation coefficient, memory profile, or runtime benchmark on the tutorial datasets. Even more importantly, several pedagogical and methodological statements in the text promote questionable statistical practices in scRNA-seq analysis, such as encouraging users to "play with the plotting parameters to yield the best-looking clusters" in t-SNE/UMAP (line 101) and advising users to perform PCA-based feature selection before removing low-quality cells/genes or normalizing library size (line 85). Correcting these statistical recommendations and adding a quantitative benchmark table across the integrated workflows on a standard GTN tutorial dataset would substantially elevate the manuscript.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: Conda/Container-isolated Galaxy tool wrappers and format converters (`CSV`, `MTX`, `LOOM`, `AnnData`) resolve package version instability and allow seamless mixing of R (`Scater`, `RaceID`, `Seurat`) and Python (`ScanPy`) scRNA-seq steps: [Well Supported].**  
  The architectural integration described in lines 38–40 and 117–125, backed by the `Tools-IUC` repository and Zenodo-archived GTN workflows, effectively solves dependency conflicts (e.g., pinning distinct `ScanPy` or Bioconductor versions per step) and enables web-based execution paired with `cellxgene` interactive exploration. One practical caveat worth addressing is whether lossless metadata transfer occurs when converting between `AnnData` (`.h5ad`), `LOOM`, and `SingleCellExperiment` objects across multi-step workflows (e.g., whether unstructured `.uns` slots, neighborhood graphs, and multiple dimensional reductions are preserved during conversion).

* **Claim 2: The 1-click preprocessing workflows (`STARsolo`, `Cell Ranger`, `Alevin`, `scPipe`) consume the same FASTQ datasets and "yield approximately the same count matrices," with `STARsolo` providing a 10-fold speedup over `Cell Ranger`: [Moderately Supported].**  
  While external benchmarks (references 24–28) have compared `STARsolo` and `Alevin` against `Cell Ranger`, the manuscript presents no empirical validation inside Galaxy (lines 62–64) showing the actual cell-barcode overlap, UMI count correlation, downstream cluster concordance, wall-clock runtime, or RAM usage when running the three GTN preprocessing workflows on the same Zenodo training dataset.

* **Claim 3: Users should "play with the plotting parameters to yield the best-looking clusters" when inspecting t-SNE and UMAP embeddings: [Methodologically Flawed].**  
  In line 101, the authors note that the same clustering can appear dissimilar under t-SNE versus UMAP projections and conclude: *"Ultimately the user is encouraged to play with the plotting parameters to yield the best-looking clusters."* In statistical genomics and manifold learning, tuning non-linear embedding hyperparameters (such as t-SNE perplexity or UMAP `n_neighbors` and `min_dist`) specifically to make pre-computed clusters "look best" visually is a classic form of visual confirmation bias ($p$-hacking of low-dimensional visualizations). Because non-linear 2D embeddings distort global distances and can manufacture apparent visual separation even in continuous Gaussian noise, cluster validity must be evaluated in the space where clustering is actually performed (e.g., via silhouette scores, modularity, stability under bootstrap subsampling, or marker gene biological coherence in PCA/graph space), not by cherry-picking 2D plotting aesthetics.

* **Claim 4: During the initial filtering stage, the `Scater` pre-analysis workflow can be used "to provide a principal component analysis–based method of feature selection so that only the highly variable genes are left in the analysis" prior to normalization: [Methodologically Flawed].**  
  In lines 77 and 85 (under *Cell and gene removal*, prior to *Library size normalization* in line 89), the authors state that `Scater` uses PCA on the raw count matrix for QC and feature selection *"so that only the highly variable genes are left in the analysis."* First, in `Scater` (McCarthy et al., reference 30), PCA during the QC stage is computed on **cell-level QC metrics** (such as total counts, number of detected features, and percentage of mitochondrial/spike-in reads) to detect outlier *cells*, not to select highly variable *genes* (HVGs). Second, selecting HVGs or running PCA on unnormalized counts *before* library size normalization (line 89) is statistically invalid because raw gene variance is dominated by library size and mean expression level; HVG selection and expression PCA must be performed *after* cell filtering and library-size log-normalization (or via deviance/Pearson residuals).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Quantitative Benchmark Table of the Preprocessing and Downstream Workflows on a Reference Tutorial Dataset
* **WHY:** The manuscript describes multiple preprocessing (`STARsolo`, `Alevin`, `scPipe`, manual `CEL-Seq2`) and downstream (`Scater`, `ScanPy`, `RaceID`) workflows in Galaxy without reporting a single runtime, memory footprint, cell count, or concordance statistic.
* **WHAT:** Include a concise benchmark table in the Methods or Results comparing the workflows on the standard 10x Genomics / GTN Zenodo tutorial dataset.
* **HOW:** Run the `10X STARsolo`, `Alevin`, and `scPipe` workflows on the GTN benchmark dataset on the public Galaxy server and report: (1) wall-clock runtime and peak memory, (2) number of cells passing knee/emptyDrops filtering, (3) median genes and UMIs per cell, and (4) Pearson/Spearman correlation of per-cell UMI counts and Adjusted Rand Index (ARI) of downstream `ScanPy` Louvain clusters across the three preprocessing engines.

#### 2. Correct the Statistical Recommendations on t-SNE/UMAP Parameter Tuning and Pre-Normalization HVG Selection
* **WHY:** Advising beginners in a training resource paper to *"play with the plotting parameters to yield the best-looking clusters"* (line 101) and describing `Scater` QC PCA as pre-normalization highly variable gene selection (line 85) teaches flawed single-cell statistical practices.
* **WHAT:** Revise lines 77, 85, and 101 to accurately reflect single-cell statistical best practices.
* **HOW:**
  1. In lines 77 and 85, clarify that `Scater` runs PCA on *cell-level quality control metrics* (library size, expressed feature count, mitochondrial transcript fraction) to identify outlier low-quality cells, whereas selection of highly variable genes (HVGs) is performed *after* library-size normalization and variance stabilization (modeling the mean–variance relationship).
  2. In line 101, replace *"play with the plotting parameters to yield the best-looking clusters"* with guidance that t-SNE (`perplexity`) and UMAP (`n_neighbors`, `min_dist`) alter the balance between local and global topology in 2D visualizations, and that users should assess cluster robustness across multiple hyperparameter settings and validate clusters using quantitative graph modularity/stability metrics and biological marker expression rather than visual aesthetics alone.

#### 3. Document Metadata Preservation Across Format Converters (`AnnData`, `LOOM`, `SCE`, `MTX`)
* **WHY:** Line 40 highlights that Galaxy converts between `CSV`, `MTX`, `LOOM`, and `AnnData` so users can mix modules across tools. In practice, converting rich objects (`AnnData` or `SingleCellExperiment`) through flat formats (`MTX`/`CSV`) or across HDF5 schemas (`LOOM` vs. `AnnData`) often strips dimensional reduction embeddings (`X_pca`, `X_umap`), cell-cell kNN graphs, or multiple assay layers (`raw` vs. `normcounts`).
* **WHAT:** Explicitly state in the text or Supplemental Table 1 which data slots are preserved vs. lost during each format conversion in Galaxy.
* **HOW:** Add a short paragraph or table note explaining which converters preserve full multi-slot metadata (cell/gene annotations, embeddings, layers) versus which converters only transfer the primary count matrix.

#### 4. Fix Minor Typographical Error in Line 58
* **WHY:** Line 58 contains a spacing typo: `"inquire directly with the sequencing lab oratoryas to which cell barcodes"`.
* **WHAT & HOW:** Replace `"lab oratoryas"` with `"laboratory as"` on line 58.
