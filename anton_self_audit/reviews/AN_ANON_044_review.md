# Review of AN_ANON_044

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This software manuscript introduces a Web-based visual analysis framework integrated into the `[AUTHOR]` genomics workbench, combining client-side JavaScript/HTML5/Canvas/D3 components (`Visualization`, `Cache`, `GenomeDataManager`, `Track`, `Genome`, `Bookmark`) with server-side Python data converters, multi-resolution indexers, and RESTful data providers supporting standard genomic formats (`SAM/BAM`, `BED`, `GFF/GTF`, `VCF`, `Wiggle`, `BedGraph`, `BigWig/BigBed`, tabular, and phylogenetic formats `PhyloXML`/`Newick`/`Nexus`). Using this architecture, the authors implement five interactive applications: `Scatterplot` (for tabular comparisons, illustrated on BodyMap 2.0 `E-MTAB-513` RNA-seq FPKM values), `PhyloViz` (a D3/SVG phylogenetic viewer claiming support for up to ~10,000 nodes), `Circster` (a Web-based Circos-style viewer demonstrated on ~20 GB of bladder cancer `SRP013232` and BodyMap 2.0 RNA-seq reads plus ChimerDB 2.0 chimeric arcs), `Trackster` (a multi-resolution genome browser supporting inline tool re-execution and dynamic feature filtering), and `Sweepster` (a parameter-space tree explorer demonstrated by sweeping Cufflinks `minimum_isoform_fraction` and `pre-mRNA_fraction` parameters across *TP53* and *VHL* loci in T24 bladder cancer RNA-seq `SRX148575`).

The framework provides a well-integrated software architecture that elevates visualizations to shareable, persistent first-class objects within `[AUTHOR]` histories and Pages while introducing a genuinely useful paradigm for interactive parameter-space exploration via `Sweepster`. However, the manuscript has two substantive methodological gaps: first, its core mechanism for interactive tool coupling—automatically subsetting genomic data to the visible browser window and running tools like Cufflinks on that local subset—can produce transcript models and abundance estimates that diverge from full-dataset runs because tools estimate global parameters (library size, fragment length distributions, multi-mapping weights) across the entire genome; second, the paper makes strong quantitative scalability claims (~10,000-node SVG trees in `PhyloViz`, ~20 GB datasets in `Circster`, millions of reads in `Trackster`) without reporting any empirical benchmarks of indexing time, REST API latency, or client browser memory/rendering performance. Addressing local-versus-global subsetting artifacts and providing empirical performance metrics would substantially strengthen the manuscript.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Decoupling server-side multi-resolution Python data providers/indexers from client-side JavaScript/D3/Canvas views enables modular creation and sharing of Web-based genomic visualizations within `[AUTHOR]`: [Well Supported].**  
  The five implemented applications (`Scatterplot`, `PhyloViz`, `Circster`, `Trackster`, `Sweepster`) span diverse data modalities (tabular, phylogenetic, circular whole-genome, linear browser tracks, and parameter trees) while reusing common RESTful data provider endpoints and `[AUTHOR]` sharing/publishing infrastructure.

* **`Sweepster` enables systematic visual comparison of tool outputs across multi-dimensional parameter grids on selected genomic intervals: [Well Supported].**  
  Figure 5 clearly demonstrates how augmenting a tool form into a hierarchical parameter tree (`minimum_isoform_fraction` $\times$ `pre-mRNA_fraction`) and stacking output track tiles across bookmarked loci (*TP53* and *VHL*) exposes locus-specific parameter sensitivity before launching a full-dataset run.

* **Automatically subsetting datasets to visible regions and running analysis tools on those subsets accurately previews full-dataset tool behavior for parameter selection: [Fragile].**  
  In `Trackster` and `Sweepster` (lines 68, 73, 87), tools such as Cufflinks are executed on regional BAM slices (e.g., the 21 kb *TP53* locus and 14 kb *VHL* locus) to identify "good settings," which are then applied to the complete dataset. However, Cufflinks and similar NGS algorithms estimate global library parameters (fragment length distribution, total mapped read depth for FPKM normalization, and multi-mapped read allocation) from the full alignment file and require reads spanning exon-exon junctions at window boundaries. Running the tool on an isolated gene slice alters these global statistics, potentially yielding different isoform filtering behavior on the subset than when the identical parameters are subsequently run genome-wide.

* **`PhyloViz` efficiently renders large phylogenetic trees up to ~10,000 nodes in SVG, and `Circster`/`Trackster` scale smoothly to ~20 GB datasets and millions of features: [Moderately Supported].**  
  While the multi-resolution coverage/detail switching strategy is architecturally sound and Figures 2–4 demonstrate working visualizations, the manuscript provides zero quantitative benchmarks (server indexing runtime, payload sizes, client DOM node counts, memory footprint, or frames-per-second during panning/zooming). Rendering 10,000 SVG DOM elements and text labels in D3 typically induces substantial browser layout lag without Canvas virtualization or automated clade collapsing.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Quantify Concordance Between Regional Subset Execution and Full-Dataset Execution in `Trackster`/`Sweepster`
* **WHY:** Users tuning Cufflinks or variant-calling parameters on a 15–20 kb region in `Sweepster` assume the resulting track tiles match what the tool will produce on the full genome. If regional BAM subsetting alters global library size, fragment length estimation, or boundary spliced-read retention, parameters chosen visually may perform differently on the full dataset.
* **WHAT:** Test and document the concordance between transcript assemblies generated on regional subsets versus full-genome runs for the *TP53* and *VHL* example (Figure 5), and support passing pre-computed global library statistics to regional tool runs.
* **HOW:** Compare the Cufflinks GTF isoform structures and FPKM values for *TP53* (`chr17:7569899-7591385`) and *VHL* (`chr3:10182352-10196520`) generated via `Sweepster` regional subsetting on `SRX148575` against the exact same parameter combinations run on the full BAM file; report the Jaccard similarity of assembled exons/introns and modify the subsetting wrapper to pass global mapped-read counts or pre-estimated fragment distributions where supported by the underlying tool.

#### 2. Add Quantitative Benchmarks of Indexing Time, API Latency, and Client Rendering Performance
* **WHY:** Claims of smooth interactive exploration across ~10,000 tree nodes (`PhyloViz`), ~20 GB of RNA-seq alignments (`Circster`), and millions of reads (`Trackster`) require empirical performance measurements to establish practical operating limits.
* **WHAT:** Add a benchmark table reporting server-side preprocessing/indexing time, REST API response latency (summary coverage mode vs. base-pair detail mode), and client browser frame rate / memory usage across dataset scales.
* **HOW:** Measure initial index generation time and JSON payload transfer times for BAM/BigWig files of 100 MB, 1 GB, and 20 GB in `Trackster`/`Circster`, and measure D3 SVG rendering latency and pan/zoom frame rates in `PhyloViz` for trees of 100, 1,000, and 10,000 tips in a standard browser.

#### 3. Editorial and Typographical Cleanup
* **WHY:** Multiple grammatical omissions and duplicated words detract from the presentation of the manuscript.
* **WHAT & HOW:** Fix the following text errors:
  - Abstract (line 6): *"We have created a platform simplifies the creation..."* $\rightarrow$ *"We have created a platform that simplifies the creation..."*
  - Background (line 16): *"...such as SNP calling algorithms and dynamic [ 7 , 8 ]."* $\rightarrow$ supply the missing noun after *"dynamic"* (e.g., *"dynamic track filtering"*).
  - Results and discussion (line 38): *"...yet they require require no dataset downloads..."* $\rightarrow$ remove duplicated *"require"*.
  - Results and discussion (line 40): *"...can be done in second by clicking..."* $\rightarrow$ *"...can be done in seconds by clicking..."*
  - Results and discussion (line 64): *"...are rendered instantaneously and be undone..."* $\rightarrow$ *"...and can be undone..."*
  - Results and discussion (line 68): *"...filters are tools are run only on visible data..."* $\rightarrow$ *"...filters and tools are run only on visible data..."*
