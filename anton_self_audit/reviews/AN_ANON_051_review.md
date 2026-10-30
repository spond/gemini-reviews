# Review of AN_ANON_051

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces an integrated, browser-based metagenomic phylogenetic profiling toolkit and reproducible workflow system, validated on the Sargasso Sea benchmark (Venter et al. / Huson et al.; `8,434` reads in Sample 1 and `5,678` reads in Samples 2–4) and applied to a novel eukaryotic metagenomic dataset of organic matter ("windshield splatter") collected on water-soluble bumper tapes across two highway trips (Trip A: Pennsylvania to Connecticut, `183,241` raw 454 FLX reads; Trip B: Maine to New Brunswick, `183,169` raw reads). The pipeline chains base-quality profiling, homopolymer-aware read segmentation (`221,422` and `212,634` trimmed segments), MegaBLAST searches against NCBI `NT` (`1.8 Gb`) and `WGS` (`102.3 Gb`), alignable-fraction filtering (top quartile $Q_3$), lowest-common-ancestor (`LCA`) diagnostic rank assignment, and taxonomic tree visualization, accompanied by a live online executable workflow supplement.

As a bioinformatics workflow and reproducibility resource, the work is well engineered: it demonstrates that nucleotide-level MegaBLAST searches with $Q_3$ alignable-fraction filtering recover the same dominant Gammaproteobacteria family profiles as protein-level `MEGAN` analyses while scaling to non-coding eukaryotic shotgun reads, and sets a high bar for transparent computational publishing. The primary methodological weakness lies in the statistical comparison of taxon abundances between Trip A and Trip B (Table 2), which models individual sequencing reads as independent events in a two-sample Poisson test. Because a single insect strike or plant fragment yields hundreds to thousands of correlated reads (as demonstrated by `9,317` of `10,242` Viridiplantae reads originating from the left-bumper subsample of Trip A), read counts per taxon follow a highly overdispersed compound process rather than a simple Poisson distribution. Leveraging the existing left- vs. right-bumper spatial subsamples to fit an overdispersed Poisson or Negative Binomial model would place the differential abundance comparisons on sound statistical footing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **End-to-end reproducible metagenomic profiling within an integrated workflow environment: [Well Supported].**  
  The six modular tools cover quality control, homopolymer-aware read splitting, database alignment, taxonomic mapping, LCA rank finding, and tree construction, and also interoperate with external `CAMERA` BLAST-XML exports (`126,032` hits across `123,241` reads). Converting execution histories directly into shareable, editable workflows with live online data supplements ensures full computational reproducibility.

* **Nucleotide-level MegaBLAST with alignable-fraction filtering accurately recovers taxonomic composition: [Well Supported].**  
  Re-analyzing the Sargasso Sea datasets against `NT` and `WGS` (`word size = 16`, filtering for alignable fraction $\ge Q_3$: `0.39` for Sample 1 and `0.25` for Samples 2–4) yields `5,847` diagnostic reads in Sample 1 that recapitulate the `MEGAN` protein-level Gammaproteobacteria profile (`Shewanellaceae`, `Pseudomonadaceae`, `Aeromonadaceae`, and `Enterobacteriaceae` comprising $>80\%$ of protein hits and $\sim 95\%$ of nucleotide hits) while remaining applicable to non-coding eukaryotic genomic DNA.

* **Detection of eukaryotic taxa and endosymbiont co-occurrence in windshield metagenomes, constrained by reference database skew: [Well Supported].**  
  The pipeline identifies `70,546` (Trip A) and `32,966` (Trip B) diagnostic reads below Kingdom level, dominated among animals by Diptera and Hemiptera. The biological validity of taxonomic recovery is corroborated by the concordant enrichment in Trip B of the pea aphid genus *Acyrthosiphon* and its obligate bacterial endosymbiont *Buchnera aphidicola* ($X = 9$ in Trip A vs. $Y = 59$ in Trip B). Furthermore, the authors accurately diagnose how severe taxon bias in GenBank (where `56%` of insect sequences belong to `Culicidae` and `Drosophilidae`, and human sequences outnumber wildlife such as white-tailed deer *Odocoileus virginianus*) causes reads from unsequenced relatives to map to model organisms or *Homo*.

* **Two-sample Poisson testing identifies statistically significant species abundance differences between Trip A and Trip B: [Methodologically Flawed].**  
  In Results (line 94) and Methods (lines 139–142), the authors justify the two-sample Poisson test (Huffman) by arguing that each insect or pollen collision with the vehicle is an independent Poisson event. While the *number of macroscopic organism collisions* may be approximately Poisson, the *number of 454 sequencing reads* generated per collision is a large random multiplier that varies with organism biomass, DNA extraction efficiency, and genome size. Consequently, read counts per taxon follow a compound Poisson (or Negative Binomial) distribution with variance $\text{Var}(X) \gg E[X]$. This is directly evidenced by Viridiplantae (`10,242` reads in Trip A vs. `612` in Trip B), where `9,317` reads (91%) came from a single plant fragment on the left side of the bumper. Treating correlated reads from single tissue fragments as independent Poisson arrivals severely underestimates sampling variance and inflates $Z$-scores across Table 2.

* **Normalization of cross-trip eukaryotic read counts via median Gammaproteobacteria ratio ($d = 0.32$): [Fragile].**  
  Setting the global expectation ratio $d = Y/X = 0.32$ based on the median ratio of Gammaproteobacteria genera with $\ge 50$ reads assumes that background Gammaproteobacteria biomass is spatially invariant between the PA–CT and ME–NB corridors. However, Gammaproteobacteria in insect-strike samples include insect gut microbiota and obligate endosymbionts (such as *B. aphidicola*), confounding background normalization with insect biomass and composition.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace the Read-Level Poisson Test with an Overdispersed / Negative Binomial Model Using Left/Right Bumper Replicates
* **WHY:** Because a single insect strike produces many sequencing reads, read counts per taxon violate the Poisson variance-equals-mean assumption ($\sigma^2 = \mu$). The authors already collected independent "left" (passenger) and "right" (driver) bumper subsamples on both Trip A and Trip B (lines 90, 132), which provide a direct empirical measure of within-trip biological clumping.
* **WHAT:** Quantify within-trip dispersion by comparing left vs. right bumper read counts within Trip A and within Trip B, and test between-trip differences using a Negative Binomial exact test (Robinson and Smyth, cited in line 60) or an overdispersed quasi-Poisson model.
* **HOW:** Tabulate taxon read counts separately for the four subsamples ($A_{\text{left}}, A_{\text{right}}, B_{\text{left}}, B_{\text{right}}$). Estimate the biological dispersion parameter $\phi$ across taxa from the within-trip replicate pairs $(A_{\text{left}}, A_{\text{right}})$ and $(B_{\text{left}}, B_{\text{right}})$ using the `edgeR` (Robinson and Smyth) method, and update Table 2 to report only taxa whose between-trip divergence exceeds within-trip left/right variance at $\text{FDR} < 0.01$.

#### 2. Evaluate Sensitivity of the Normalization Factor $d$ to Endosymbiont and Soil/Plant-Associated Bacteria
* **WHY:** Gammaproteobacteria genera used to estimate $d = 0.32$ include plant-associated (e.g., *Pseudomonas*, *Pantoea*) and insect-associated (e.g., *Buchnera*, *Enterobacter*) taxa whose counts can be driven by single leaf or insect strikes.
* **WHAT:** Report the distribution (interquartile range and left-vs-right stability) of B/A ratios across the Gammaproteobacteria genera in Supplemental Table 1, and compare $d = 0.32$ against total post-QC read ratio ($212,634 / 221,422 = 0.96$) and total diagnostic read ratio ($32,966 / 70,546 = 0.47$, or $32,354 / 60,304 = 0.54$ after excluding Viridiplantae).
* **HOW:** Exclude known obligate insect endosymbionts and plant-adherent genera that show $>3$-fold skew between left and right bumper halves before computing the median normalization factor $d$, and re-run the differential abundance test across the plausible range $d \in [0.32, 0.54]$.

#### 3. Technical, Mathematical, and Editorial Cleanup
* **WHY:** An inverted mathematical inequality in the workflow description and minor taxonomic spelling errors could confuse users replicating the pipeline.
* **WHAT & HOW:**
  1. **Inverted alignment coverage inequality (Line 101):** Line 101 states: *"it is simple to filter suboptimal hits by retaining those reads that satisfy the `c5/c15 <= 0.5` condition (value in column 5, alignment length divided by the value in column 15, read length) to data set 12. Here, we defined suboptimal hits as those in which an alignment between a 454 read and a database entry covers less than 50% of the read's length."* Retaining hits that cover at least 50% of the read requires `c5/c15 >= 0.5` (whereas `c5/c15 <= 0.5` retains the suboptimal hits). Correct the inequality to `c5/c15 >= 0.5`.
  2. **Taxonomic family spelling typos (Line 79):** Change `Preudomonadaceae` to `Pseudomonadaceae` and `Enterobacteriacaea` to `Enterobacteriaceae`.
