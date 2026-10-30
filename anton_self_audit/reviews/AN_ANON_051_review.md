# Review of AN_ANON_051

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces an integrated, web-based metagenomic phylogenetic profiling toolkit and reproducible workflow system, validated on the Sargasso Sea benchmark dataset (samples 1 and 2–4) and applied to a pilot eukaryotic metagenomic survey of biological matter collected on water-soluble bumper tape attached to a moving vehicle across two North American highway transects (Trip A: Pennsylvania to Connecticut, 183,241 raw 454 FLX reads; Trip B: Maine to New Brunswick, 183,169 raw reads). The six-component pipeline performs base-quality profiling, homopolymer-aware high-quality read segmentation (yielding 221,422 and 212,634 fragments for Trips A and B), MegaBLAST alignment against NCBI NT and WGS nucleotide databases, upper-quartile alignable-fraction filtering, lowest-common-ancestor taxonomic assignment (identifying 70,546 and 32,966 diagnostic reads below Kingdom rank), and phylogenetic tree visualization. All raw sequences, executable histories, workflow definitions, and instructional screencasts are publicly provided in a live online supplement.

As a bioinformatics workflow resource and reproducibility demonstration, the manuscript succeeds: it demonstrates that nucleotide-level MegaBLAST searches against NT and WGS with top-quartile alignability filtering closely reproduce MEGAN's protein-level taxonomic profiles on the Sargasso Sea dataset while accommodating non-coding eukaryotic genomic reads and 454 homopolymer base-calling errors. The authors also provide a candid assessment of how NCBI sequence database skew (where ~56% of insect entries come from Culicidae and Drosophilidae, and unsequenced mammals map to *Homo*) distorts genus-level assignments. The primary methodological weakness lies in the statistical comparison of taxon abundances between Trip A and Trip B: modeling individual sequencing reads as independent events in a two-sample Poisson test ignores the extreme overdispersion caused by single macroscopic impacts (one insect or leaf fragment yielding thousands of reads) and lacks biological replication ($n=1$ collection per route, confounded by left/right subsamples). Re-analyzing the left and right bumper subsamples using an overdispersed count model (e.g., negative binomial or beta-binomial) would align the statistical testing with the physical sampling process.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The browser-based nucleotide MegaBLAST workflow accurately recovers community taxonomic profiles comparable to standalone MEGAN protein-level analyses: [Well Supported].**  
  Benchmarking on the Sargasso Sea dataset (samples 1 and 2–4) confirms that filtering NT/WGS MegaBLAST hits to the top quartile of read alignable fraction ($\ge 0.39$ and $\ge 0.25$) recovers the exact same dominant Gammaproteobacteria families (*Shewanellaceae*, *Pseudomonadaceae*, *Aeromonadaceae*, and *Enterobacteriaceae*) as MEGAN's protein-level BLASTX pipeline while operating entirely within a reproducible web workflow.

* **Homopolymer-aware quality segmentation preserves 454 FLX read utility and enables eukaryotic taxon detection alongside obligate bacterial endosymbionts: [Well Supported].**  
  Preventing read splitting at low-quality bases immediately following homopolymer runs increases usable segments from 82,917 and 45,354 to 221,422 and 212,634 for Trips A and B. Moreover, the co-enrichment of reads mapping to the pea aphid (*Acyrthosiphon pisum*) and its obligate endosymbiont (*Buchnera aphidicola*, $X=9$ in Trip A vs. $Y=59$ in Trip B) provides a compelling internal biological validation of taxonomic recovery.

* **Database representation bias severely distorts fine-scale eukaryotic taxonomic identification from random shotgun reads: [Well Supported].**  
  The authors convincingly show that only ~8% of reads map unambiguously to eukaryotes and that uneven genomic representation in NT/WGS causes reads from unsequenced local fauna (e.g., roadkill white-tailed deer, *Odocoileus virginianus*, or unsequenced insects) to cross-map to heavily sequenced relatives (*Homo* or model dipterans).

* **The two-sample Poisson test identifies statistically significant (1% FDR) geographic biodiversity differences between Trip A and Trip B: [Methodologically Flawed].**  
  The authors justify the two-sample Poisson test by arguing that *"each set of sequencing reads derived from an insect or a pollen particle colliding with a moving vehicle represents an independent event... [and] can be modeled as a Poisson process"* (line 94). While *organismal strikes* may follow a Poisson process, each strike contributes a large, variable burst of DNA molecules and sequencing reads (a compound Poisson process). This is directly demonstrated by the authors' own observation that a single plant fragment on the left side of the bumper generated 9,317 of the 10,242 Viridiplantae reads in Trip A (vs. 612 in Trip B). Treating individual *reads* ($X$ and $Y$) rather than *strikes* or biological replicates as independent Poisson draws underestimates the variance by orders of magnitude, inflating $Z$-scores and producing spurious 1% FDR significance across Table 2. Furthermore, calibrating the scaling factor $d = 0.32$ from the median $B/A$ ratio of Gammaproteobacteria genera assumes invariant background bacterial abundance across regions and includes insect-associated symbionts (such as *Buchnera*, itself a Gammaproteobacterium).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace the Read-Level Poisson Test with an Overdispersed Model Incorporating the Left/Right Bumper Subsamples
* **WHY:** Because a single insect or plant strike yields hundreds to thousands of reads, read counts violate the Poisson variance-equals-mean assumption ($\text{Var}(X) \gg E[X]$). Treating reads as independent events conflates within-specimen DNA mass with geographic taxon abundance.
* **WHAT:** Exploit the left (passenger-side) and right (driver-side) bumper subsamples collected on each trip (described in line 90 and Methods line 132) to estimate within-trip biological/sampling dispersion, and test for between-trip differences using a negative binomial model (e.g., `edgeR` Robinson and Smyth, already cited in the Introduction).
* **HOW:** Tabulate diagnostic read counts separately for the four subsamples (`TripA_Left`, `TripA_Right`, `TripB_Left`, `TripB_Right`). Estimate the common and tagwise dispersion parameters across taxa from the left vs. right replicate pairs within each trip, and compute exact negative binomial $P$-values and Benjamini–Hochberg FDR values for Trip A vs. Trip B. Taxa driven by a single localized strike (such as Viridiplantae on `TripA_Left`) will appropriately show high within-trip dispersion and lose artificial statistical significance.

#### 2. Sensitivity Analysis on the Normalization Factor $d$ Excluding Insect Endosymbionts
* **WHY:** The scaling factor $d = 0.32$ is derived from the median $B/A$ read ratio of Gammaproteobacteria genera with $\ge 50$ reads, but Gammaproteobacteria includes obligate and facultative insect endosymbionts (e.g., *Buchnera aphidicola*, *Enterobacter*, *Serratia*) whose abundances are directly coupled to the target insect strikes rather than invariant airborne background.
* **WHAT:** Recompute $d$ after excluding known insect-symbiotic Gammaproteobacteria genera and compare it against total-read or TMM (trimmed mean of M-values) normalization across all bacterial classes.
* **HOW:** Report the interquartile range of $B/A$ across the selected bacterial genera in Supplemental Table 1 and show how the list of significant taxa in Table 2 changes across the 25th, 50th ($d=0.32$), and 75th percentiles of $d$.

#### 3. Technical, Mathematical, and Editorial Corrections
* **WHY:** A reversed inequality in the pipeline description, missing equations in the Methods, and taxonomic spelling errors could confuse readers attempting to replicate or adapt the workflow.
* **WHAT & HOW:**
  1. **Reversed filtering inequality (line 101):** The text states *"it is simple to filter suboptimal hits by retaining those reads that satisfy the c5/c15 <= 0.5 condition... Here, we defined suboptimal hits as those in which an alignment... covers less than 50% of the read's length."* To retain high-quality alignments covering at least 50% of the read, the retained set must satisfy `c5/c15 >= 0.5` (or suboptimal hits satisfying `c5/c15 < 0.5` must be removed). Correct the inequality sign in line 101.
  2. **Missing Z-score equations (line 141):** In the "Testing for abundance differences" section of Methods, the two Huffman Poisson $Z$-score equations following *"we used two formulae to calculate Z-scores, and corresponding P-values from a standard normal distribution:"* are missing from the rendered text (`|  |`). Insert the explicit algebraic expressions for both $Z_1$ and $Z_2$ as functions of $X$, $Y$, and $d$.
  3. **Taxonomic typos (line 79):** Correct *"Preudomonadaceae"* to *Pseudomonadaceae* and *"Enterobacteriacaea"* to *Enterobacteriaceae*.
