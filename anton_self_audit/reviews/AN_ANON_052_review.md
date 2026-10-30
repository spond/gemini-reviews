# Review of AN_ANON_052

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript develops and validates a next-generation sequencing (NGS) workflow for detecting mitochondrial DNA (mtDNA) heteroplasmy and applies it to 32 Illumina GA IIx datasets (blood and buccal swabs, mostly in duplicate long-range PCR reactions) from nine individuals across three multigenerational families (six mother–child transmissions). To calibrate false-positive and false-negative rates, the authors combine (1) coverage-based Python simulations (at 1,170× depth), (2) ultra-deep sequencing (median 1,157,250×) and Sanger subcloning (377 quality-trimmed clones) of a single-colony `pUC18` plasmid grown in recombination-deficient (`recA- endA-`) cells, (3) duplicate PCR amplification comparisons, and (4) a 49:1 artificial DNA mixture of two individuals (`M4` and `M10C1`) differing at 24 fixed mtDNA sites, evaluated with and without GATK base quality recalibration. Requiring a minor allele frequency (MAF) $\ge 0.02$ on each strand at Phred quality $\ge 30$ and excluding low-complexity poly-C tracts identifies four heteroplasmic sites across the three families (`5063`, `7028`, `8992`, and `14053`) and demonstrates that previously published CEPH heteroplasmies at positions `16,186–16,187` are alignment artifacts caused by a fixed indel flanking a poly-C stretch near the 3' end of short reads. All 32 raw sequence datasets, `pUC18` controls, simulation scripts, and the 45-step executable workflow are publicly deposited in the NCBI Sequence Read Archive (`DRA000390` / `DRP000396`), a public workflow server, and Amazon Web Services (AWS).

This is a well-controlled methodological and forensic study whose experimental controls (`pUC18`, 49:1 mixture, duplicate PCRs, and re-analysis of published CEPH reads) directly establish best practices for low-frequency variant detection and reproducibility. Its claims regarding population heteroplasmy prevalence are appropriately cautious, explicitly showing via Poisson resampling that its small sample of unrelated founders ($n=3$) is statistically compatible with prior studies. Two technical issues warrant correction: first, the resampling and Fisher's exact tests for inter-tissue and mother–child frequency shifts at site `8992` treat individual post-PCR sequencing reads ($N$ up to 81,207) as independent binomial draws, ignoring PCR amplification variance that can be directly estimated from the study's own PCR duplicates; second, swapped `T`/`G` column headers in the lower half of Table 1 and Table 2 caused the text to misstate the major allele at position `5063` as `G` rather than `T`.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Double-stranded filtering ($\text{MAF} \ge 0.02$ per strand at Phred $\ge 30$) and low-complexity masking eliminate Illumina sequencing and PCR-duplicate noise while recovering true 2% variants: [Well Supported].**  
  The `pUC18` clonal control demonstrates that a raw 0.01 threshold leaves a strand-biased false positive at site 880 (MAF 0.025) driven by >50,000× PCR duplicates, which is completely removed by requiring $\ge 0.01$ on both strands. Conversely, the 49:1 two-individual mixture experiment recovers all 24 known fixed differences on both amplicons A (mean 4.70%, range 4.02–5.10%) and B (mean 2.91%, range 2.19–3.55%), and an ANOVA confirms that GATK quality score recalibration does not significantly alter calls ($P > 0.10$).

* **Previously reported heteroplasmies in the `16,184–16,190` poly-C tract (including published CEPH family 1377 calls at `16,186–16,187`) are alignment artifacts of fixed indels near 3' read ends: [Well Supported].**  
  By stratifying reads into unfiltered alignments (Set A), bridging reads centered on `16,184–16,190` (Set B), and reads flanked by $\ge 10$ Phred $\ge 30$ bases on both sides of the gap (Set C, Fig. 4), as well as remapping raw reads from `He et al.`, the authors conclusively show that a fixed `16,183` `A` insertion and `C` deletion coupled with 3' read base-calling decay produce illusory substitution heteroplasmies.

* **Observed heteroplasmy incidence in these three families is statistically consistent with prior NGS surveys once matched for detection thresholds: [Well Supported].**  
  Rather than overclaiming from $n=3$ families, the authors subsample one unrelated individual per family (`M4`, `M10`, `M15`) and perform 10,000-draw Poisson comparisons at matched thresholds (10% and 2%), appropriately concluding that 1/3 ($\ge 10\%$) and 4/3 ($\ge 2\%$) are not significantly different from `Li et al.` ($37/131, P = 0.8375$) or `He et al.` ($10/4, P = 0.4992$).

* **Heteroplasmy allele frequencies at site `8992` differ significantly between tissues and across mother–child transmissions ($P < 0.0001$ to $P = 0.0006$): [Moderately Supported].**  
  While the large allele frequency shifts at site `8992` (e.g., 65.2% in `M5G` blood vs. 54.5% in `M5G` cheek, and 67.2% in `M4` blood vs. 52.6% in `M4-C1` blood) are almost certainly biologically real and are qualitatively corroborated by allele-specific PCR (Fig. S4), the reported $P$-values from binomial resampling of $N = \text{read coverage}$ (1,433 to 52,519 reads) and Fisher's exact test treat each sequencing read from a 30-cycle PCR amplicon as an independent sampling of a mitochondrial genome. This underestimates variance by ignoring PCR amplification and library dispersion, which should instead be estimated from the paired PCR1 and PCR2 technical replicates generated for seven of the nine individuals.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Incorporate Between-PCR Replicate Variance into the Statistical Tests for Allele Frequency Shifts
* **WHY:** Sampling $N$ alleles where $N$ equals sequencing depth (up to 52,519 reads at site `8992`) in a binomial resampling or Fisher's exact test assumes zero technical variance from DNA extraction, 30-cycle long-range PCR amplification, and sequencing library preparation. The authors' own 49:1 mixture experiment showed significant ~1.8% variance between amplicons ($P < 0.001$).
* **WHAT:** Use the duplicate PCR datasets (`PCR1` and `PCR2`, generated for 7 of 9 individuals) to estimate the technical overdispersion parameter and re-test inter-tissue and mother–offspring shifts using a beta-binomial model or replicate-level generalized linear model.
* **HOW:** Tabulate the allele counts at sites `5063`, `7028`, `8992`, and `14053` separately for `PCR1` and `PCR2` (rather than only reporting pooled coverage in Tables 1–2). Fit a beta-binomial likelihood ratio test (or quasibinomial GLM with `PCR_replicate` nested within `individual × tissue`) to compute overdispersion-corrected $P$-values for `M5G` blood vs. cheek and the four maternal transmissions at site `8992`.

#### 2. Clarify Low Coverage at Site `14,053` in Family F7 Relative to the Stated 1,170× Minimum Depth
* **WHY:** In lines 28–30, the authors state that they chose the dataset with the smallest number of reads (`M4`, cheek, PCR2, 584,539 reads, median coverage 1,170×) as a conservative lower bound for their simulation study. However, Table 2 reports read coverages of only 403× (`M10` blood), 527× (`M10` cheek), and 380× (`M10-C2` cheek) at site `14,053` in Family F7, and several entries in Tables 1 and 2 are listed as `"no data"`.
* **WHAT:** Explain why coverage at positions `7028` and `14053` fell below 550× (or yielded `"no data"`) and evaluate false-positive/false-negative rates in the Python simulation script at 380× coverage.
* **HOW:** Run the Python simulation script (Additional file 3) at `coverage = 380` with `error_rate = 0.001` and `MAF = 0.02` on each strand (~190× per strand) to confirm that the false-positive rate remains $\ll 1/16,569$ at the actual minimum depth observed in Table 2, and note in the caption of Tables 1–2 what minimum per-site coverage filter caused the `"no data"` entries.

#### 3. Correct Swapped Nucleotide Column Headers in Tables 1 and 2 and Fix the Table 3 Title
* **WHY:** Swapped column headers in Tables 1 and 2 led to a factual error in the main text regarding the identity of the major allele at position `5063`.
* **WHAT & HOW:**
  1. **Swapped `T` and `G` column headers in Table 1 (`cheek`, line 62) and Table 2 (line 73):** In the `blood` sub-table of Table 1 (line 57), the nucleotide columns are ordered `A | C | G | T | cvrg`. In the `cheek` sub-table (line 62), the header order was changed to `A | C | T | G | cvrg`, even though the underlying numeric columns remained in `A | C | G | T` order (so at site `5063`, Ref = `T`, the 0.980–0.999 major allele frequency in the 4th column is `T`, not `G`). Because of this header swap, line 66 erroneously states: *"Only one heteroplasmy (position 5,063; C is the minor allele, G is the major allele)..."* Correct the column headers in Table 1 (`cheek`) and Table 2 to `A | C | G | T | cvrg` (or reorder the cell entries to match), and correct line 66 to state that `T` is the major allele at position `5,063` (matching Ref = `T` and Table 3: `cct` $\to$ `ccc`).
  2. **Table 3 caption typo (line 83):** Change *"Context and effect of alleles observed in the six heteroplasmic sites"* to *"four heteroplasmic sites"*, matching the four sites (`5,063`, `7,028`, `8,992`, and `14,053`) listed in Table 3 and line 47.
  3. **Reagent volume typos in Materials and Methods (second part, lines 1 and 3):** Correct *"placed in 200 mL Tris-EDTA (TE) buffer"* and *"re-suspended in 250 ml of TE buffer"* to `200 μl` and `250 μl`.
