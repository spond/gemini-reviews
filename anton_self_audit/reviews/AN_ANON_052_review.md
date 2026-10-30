# Review of AN_ANON_052

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.1 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript develops and validates an empirical pipeline for detecting low-frequency mitochondrial DNA (mtDNA) heteroplasmy from deep Illumina sequencing (`32` datasets across blood and buccal tissues from `9` individuals in `3` families spanning `6` maternal transmissions), accompanied by a fully reproducible 45-step workflow and cloud-deployable data/compute environment. To calibrate false-positive and false-negative rates, the authors combine simulations at `1,170x` coverage, ultra-deep sequencing (`1,157,250x` median coverage) and Sanger subcloning (`377` clones) of a clonal `pUC18` plasmid, duplicate long-range mtDNA PCR amplifications, a `49:1` two-individual positive-control DNA mixture across `24` fixed SNPs, `GATK` quality-score recalibration ANOVA, and allele-specific PCR. Applying their threshold (Phred $\ge 30$ and minor allele frequency $\ge 0.02$ on both forward and reverse strands, excluding low-complexity poly-C tracts) identifies four heteroplasmic sites (`5063`, `7028`, and `8992` in Family F4; `14053` in Family F7) and demonstrates that previously published heteroplasmies at `16,186–16,187` in CEPH family 1377 were short-read misalignment artifacts caused by fixed indels near the `16,184–16,193` poly-C stretch.

The experimental control design (`pUC18` clonal negative control, `49:1` spike-in positive control, strand-concordance filtering, and poly-C indel re-alignment) and open-science infrastructure (`SRA` accession `DRA000390` plus workflow and cloud images) are strong contributions. However, three technical issues require correction: (1) testing maternal transmission and inter-tissue allele frequency shifts at site `8,992` via binomial read resampling / Fisher's exact test treats up to `52,519` PCR-amplified reads as independent biological draws rather than accounting for between-PCR amplification variance; (2) the Abstract claim that heteroplasmy incidence is lower than prior estimates is underpowered with only $n = 3$ independent maternal lineages; and (3) a column-header swap between `T` and `G` in Tables 1 and 2 introduces direct contradictions with the main text and Table 3 regarding the major and minor alleles at positions `5,063` and `14,053`.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Double-stranded frequency thresholding ($\ge 0.02$ per strand at Phred $\ge 30$) eliminates sequencing and PCR-duplicate false positives while recovering ~2–5% true variants: [Well Supported].**  
  In the clonal `pUC18` control (`1.16M×` median depth), single-strand Phred $\ge 30$ filtering leaves a false-positive variant at site `880` (`2.5%` frequency) and extreme PCR duplicate stacks (`>50,000` identical reads), both of which are completely removed by requiring $\ge 0.01$ frequency on both strands. Conversely, in the `49:1` positive-control mixture of `M4` and `M10C1`, all `24` known SNPs are recovered on both strands (`4.70%` mean in amplicon A, `2.91%` in amplicon B), and a three-factor ANOVA confirms that `GATK` base quality recalibration does not significantly alter variant recovery ($P > 0.10$).

* **Apparent SNP heteroplasmies around `16,186–16,187` (including CEPH family 1377 in prior literature) are short-read indel misalignment artifacts: [Well Supported].**  
  By stratifying reads spanning the `16,184–16,193` homopolymeric tract into unfiltered reads, bridging reads, and reads anchored by $\ge 10$ Phred $\ge 30$ flanking bases on both sides (Figure 4 and Figure S5), the authors convincingly show that fixed indel polymorphisms (`16183A` insertion and `C` deletion) cause 3'-terminal base-calling and alignment errors that mimic SNP heteroplasmy.

* **Significant allele frequency shifts occur between tissues and across maternal transmission events at site `8,992`: [Moderately Supported].**  
  Allele frequencies at `8,992` vary between `0.526` and `0.686` across Family F4 and are qualitatively corroborated by allele-specific PCR (Figure S4). However, the statistical tests reported in lines 66 and 111 (odds ratio test, Fisher's exact test, and 10,000-iteration read resampling where $N$ equals sequencing read coverage up to `52,519`) treat every sequencing read from a 30-cycle PCR amplicon as an independent biological sample of mtDNA molecules. Because binomial sampling error at $N = 15,000\text{--}50,000$ reads is tiny ($\text{SE} \approx 0.2\%\text{--}0.4\%$), whereas empirical pipetting and PCR amplification variance is ~1–2% (as seen in the `49:1` mix where amplicon A and B differed by `4.70%` vs. `2.91%`), read-level tests severely overstate statistical significance by ignoring inter-PCR technical variance.

* **Incidence of mtDNA heteroplasmy is lower than estimated in recent re-sequencing studies: [Overstated].**  
  While the Abstract states that the incidence of heteroplasmy may be lower than estimated in recent studies, the dataset contains only `3` independent maternal lineages (`F4`, `F7`, `F11`). As the authors themselves acknowledge in the Conclusions (line 109), comparing `1/3` individuals (at the 10% threshold) against Li et al. (`37/131`, $P = 0.84$) or `4/3` sites (at the 2% threshold) against He et al. (`10/4`, $P = 0.50$) shows no statistically significant difference because $n = 3$ families has negligible statistical power.

* **Nucleotide identities and coverage adequacy at reported heteroplasmic sites `5,063` and `14,053` in Tables 1–3: [Fragile].**  
  First, at site `14,053` (Table 2), read depth is only `380x–527x` (roughly 3-fold below the `1,170x` coverage used to calibrate the false-positive simulation), and in `M10 blood` the minor allele frequency (`0.010` / `0.012`) fails the $\ge 0.02$ threshold. Second, in Table 1 (`cheek`, line 62) and Table 2 (line 73), the column headers for `T` and `G` are transposed (`A | C | T | G` instead of `A | C | G | T`), creating direct conflicts with the main text (line 66 claiming `G` is the major allele at `5,063` when `Ref = T`) and Table 3 (listing `14,053` as an `A -> C` `acc -> ccc` Thr-to-Pro substitution when Table 2 places the `0.023` / `0.026` minor allele under the `T` column).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Incorporate Between-PCR Technical Variance When Testing Tissue and Maternal Transmission Shifts
* **WHY:** Treating `15,000–52,000` sequencing reads from amplified DNA as independent binomial trials underestimates variance by ignoring PCR amplification drift between replicates.
* **WHAT:** Use the duplicate independent PCR amplifications (`PCR1` and `PCR2`, generated for 7 of the 9 individuals) to estimate the empirical between-PCR dispersion, and re-evaluate tissue (`blood` vs. `cheek`) and maternal transmission (`M5G -> M9`, `M5G -> M4`, `M4 -> M4-C1`, `M4 -> M4-C3`) differences at site `8,992` relative to between-PCR variance.
* **HOW:** Fit a beta-binomial model (or a mixed-effects logistic regression with a random intercept per PCR replicate) to the `PCR1` and `PCR2` read counts at site `8,992`, and report the resulting dispersion-adjusted $p$-values and 95% confidence intervals alongside the pooled read counts in Table 1.

#### 2. Temper the Abstract Conclusion Regarding Population Heteroplasmy Incidence
* **WHY:** With $n = 3$ unrelated maternal lineages, the study cannot statistically distinguish its per-individual heteroplasmy rate from either Li et al. ($P = 0.84$) or He et al. ($P = 0.50$).
* **WHAT:** Align the Abstract with the nuanced discussion in the Conclusions (line 109) by emphasizing that apparent excesses in prior uncalibrated studies were driven by poly-C indel misalignment artifacts (`16,186–16,187`) and single-strand noise rather than claiming a statistically distinct population incidence from $n = 3$ families.
* **HOW:** Revise the Abstract sentence *"Our results suggest that the incidence of heteroplasmy may be lower than estimated in some other recent re-sequencing studies"* to *"Our re-analysis demonstrates that stringent double-stranded filtering and indel-aware alignment eliminate false-positive heteroplasmies in homopolymeric tracts that inflated some prior estimates."*

#### 3. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Transposed table headers, contradictory nucleotide assignments, and volume unit typos (`mL` instead of `μL`) compromise the clarity of the benchmark tables and protocol.
* **WHAT & HOW:**
  1. **Fix `T` and `G` column header transposition in Tables 1 and 2 (Lines 62 and 73) and main text (Line 66):** In Table 1, the `blood` sub-table header is `A | C | G | T | cvrg`, whereas the `cheek` sub-table header (line 62) is `A | C | T | G | cvrg`, yet the numerical columns were not reordered (e.g., at `5063`, `Ref = T`, the `0.999` major allele is in the 4th column). Correct the `cheek` header in Table 1 to `A | C | G | T | cvrg`, and correct line 66 from *"C is the minor allele, G is the major allele"* to *"C is the minor allele, T is the major allele"*. Similarly, verify the column order in Table 2 (`14,053`) so that the minor allele column matches the `acc -> ccc` (`A -> C`) substitution reported in Table 3.
  2. **Fix DNA resuspension volume units (Lines 122 and 124):** Change *"200 mL Tris-EDTA (TE) buffer"* (line 122) and *"250 ml of TE buffer"* (line 124) to `200 μl` and `250 μl`.
  3. **Fix swapped citation attributions for He et al. [16] and Li et al. [17] (Line 77):** Line 77 refers to *"CEPH family 1377 published by Li et al. [ 16 ]... (Table 3 in He et al. [ 17 ])"*. Restore the correct mapping (`He et al. [16]` for CEPH family 1377 Table 3, and `Li et al. [17]`).
  4. **Fix inequality wording in positive-control mix (Line 43):** Change *"are below our 2% threshold, arguing for the threshold validity: fragment A differences were, on average, 4.70%... fragment B differences were, on average, 2.91%"* to *"are above our 2% threshold"*.
  5. **Fix Table 3 title (Line 83):** Change *"observed in the six heteroplasmic sites"* to *"observed in the four heteroplasmic sites"*.
