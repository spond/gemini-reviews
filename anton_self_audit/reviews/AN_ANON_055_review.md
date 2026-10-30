# Review of AN_ANON_055

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.3 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.6 / 8.0**  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces a reference-guided paired-end read overlap assay to retroactively estimate instrument-level sequencing error rates and sequence-context biases across 1,126 public Illumina sequencing runs of *Escherichia coli* from the Sequence Read Archive (SRA), spanning seven platforms (`MiSeq` $n=212$, `MiniSeq` $n=40$, `NextSeq 500` $n=160$, `NextSeq 550` $n=171$, `HiSeq 2500` $n=141$, `NovaSeq 6000` $n=239$, and `HiSeq X Ten` $n=163$). By restricting mismatches between overlapping paired-end mates to the 50–60% read-length bin (requiring $\ge 2.5\text{ Mb}$ of overlap per run), the authors control for read-cycle position and pre-sequencing library/PCR errors, reporting median platform error rates from 0.087% (`HiSeq X Ten`) to 0.613% (`MiniSeq`), substantial lab-group effects via ordinary least squares (OLS) regression, and analyses of surrounding base context, trimer enrichment, and post-homopolymer substitutions. Analysis scripts, Jupyter notebooks, and 1.8 TB of intermediate alignments are publicly provided.

Using paired-end overlaps within a fixed fractional read-length bin (50–60%) to isolate post-cluster instrument errors across $>1,100$ public SRA runs is a sound, scalable concept that reveals striking inter-laboratory variability within platforms. However, the downstream analyses of sequence context, trimer motifs, and post-homopolymer errors suffer from three methodological flaws that invalidate several headline conclusions about platform-specific chemistry biases: (1) sequence context and "preceding" bases were extracted from the reference genome (`+` strand) at the error coordinate without determining *which mate* (`R1` vs. `R2`, forward vs. reverse strand) contained the error and reverse-complementing reverse-strand errors into the $5' \to 3'$ sequencing synthesis direction; (2) trimer and context counts were collapsed across "the set of unique error loci" in the ~5 Mb *E. coli* genome without weighting by error count or local overlap depth, causing platforms with more runs/reads (`NovaSeq 6000`, `HiSeq X Ten`) to saturate the genome and regress toward the null ratio of 1.0; and (3) the null expectation for post-homopolymer errors divides by 4 instead of 3, inflating all enrichment ratios in Figure 6 by 33%. Re-running the context and homopolymer scripts on strand-oriented, coverage-normalized read coordinates will be necessary to salvage the sequence-bias claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Public production datasets on `HiSeq 2500`, `HiSeq X Ten`, and `NovaSeq 6000` exhibit lower median sequencing error rates (~0.09–0.11%) than benchtop/mid-scale platforms (`MiSeq`, `MiniSeq`, `NextSeq 500/550`, ~0.43–0.61%), with large variation driven by submitting laboratory: [Well Supported].**  
  Restricting comparisons to the 50–60% read-length bin with $\ge 2.5\text{ Mb}$ of paired-end overlap cleanly isolates instrument base-calling errors from library preparation artifacts and cycle-position confounding. The platform medians and the group-level clustering (such as the 23 GEO ChIP-seq runs on `NovaSeq 6000` clustering at 0.683% vs. 0.106% for the rest of `NovaSeq 6000`) are convincingly demonstrated.

* **Sample-handling oxidative DNA damage (`Ma et al.`) explains part of the intra-platform variation in overlap-derived error rates: [Methodologically Flawed].**  
  In line 56, the authors cite `Ma et al.` to suggest that variation in their overlap error rates may stem from *"oxidative damage introduced by differential sample handling."* This directly contradicts the manuscript's own Figure 1 and Introduction (line 20): oxidative damage during sample handling/shearing occurs *prior* to PCR and flowcell cluster generation, meaning both mates (`R1` and `R2`) derived from that single ancestor DNA molecule share the damage-induced mutation and will *agree* in the overlap region. Only errors occurring during or after bridge amplification/sequencing-by-synthesis on the flowcell can create discordant overlapping bases.

* **`HiSeq X Ten` and `NovaSeq 6000` show notable exceptions to the preceding-base substitution bias and lack expected 2-dye (`poly-G`) chemistry signatures: [Methodologically Flawed].**  
  As described in Materials and Methods (lines 40, 42, 46), the authors identified the erroneous base by comparing overlapping mates to the majority sample allele at a genomic locus, and then extracted the "preceding" bases directly from the reference genome coordinate without orienting by the $5' \to 3'$ sequencing strand of the erroneous mate. In paired-end sequencing, one mate maps to the reverse (`-`) strand; an error on the reverse-strand mate was synthesized $5' \to 3'$ in the *opposite* genomic direction (so its true preceding base on the flowcell is at genomic coordinate $+1$, not $-1$) and its incorporated fluorophore corresponds to the *complement* of the reference `+` strand base (e.g., an unlabeled `G` dropout in 2-dye chemistry on the reverse strand appears as a `C` call on the `+` strand preceded at $+1$ by `C`). Mixing un-oriented forward and reverse-strand errors, combined with collapsing errors to unweighted "unique error loci" (line 42) across a 5 Mb genome (which saturates toward uniform genomic background in deep datasets like `NovaSeq 6000`), distorts both the preceding-base profiles (Fig. 3) and trimer enrichments (Fig. 4).

* **Post-homopolymer substitution rates relative to random expectation are accurately quantified across platforms in Figure 6 (showing `G/C` post-homopolymer errors occurring less often than random chance on `NovaSeq 6000`): [Methodologically Flawed].**  
  In addition to the strand-orientation flaw above, the null model in line 46 computes the expected number of random post-homopolymer errors by multiplying the genomic homopolymer frequency by total errors *"and divided by four."* However, at the base immediately following a homopolymer of base $X$ of exact length $k$, the reference base $Y$ is necessarily not $X$ ($Y \ne X$). Because $Y \to Y$ is a match rather than a substitution error, there are only **3** possible substitution outcomes at that site ($X$, and the two other non-$Y$ bases), not 4. Under a random substitution null, the probability that an error at a post-$X$-homopolymer site substitutes base $X$ is $1/3$, not $1/4$. Dividing the expected value by 4 underestimates the null expectation by 25% and inflates every enrichment value in Figure 6 by a factor of $4/3$ (1.33×); conversely, failing to normalize by the actual overlapping read coverage at homopolymer loci (which varies with GC content and insert size) biases the numerator.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Orient All Context, Trimer, and Post-Homopolymer Analyses to the $5' \to 3'$ Synthesized Strand of the Erroneous Read
* **WHY:** Phasing, pre-phasing, and two-dye/four-dye optical crosstalk occur in the $5' \to 3'$ direction of the sequencing read being synthesized on the flowcell. Extracting genomic `+` strand bases to the left of an error site treats reverse-strand (`flag 16`) errors backwards and complements their base and dye identities.
* **WHAT:** Attribute each overlap mismatch to the specific mate (`R1` or `R2`) that disagrees with the consensus/reference base at that locus, and if that mate is mapped to the reverse strand (`SAM flag 16`), reverse-complement both the 20 bp surrounding sequence context and the substitution call before tabulating preceding bases (Fig. 3), trimers (Fig. 4), and post-homopolymer runs (Figs. 5–6).
* **HOW:** Using the existing intermediate alignment data, for each mismatch where one read matches the reference/major allele $M$ and the other read carries error base $E \ne M$:
  1. Check `flag & 16` on the read carrying $E$.
  2. If `flag & 16 == 0` (forward strand), record substitution $M \to E$ and preceding context `ref[pos-10 : pos+10]`.
  3. If `flag & 16 != 0` (reverse strand), record the reverse-complemented substitution $\bar{M} \to \bar{E}$ and the reverse-complemented context `revcomp(ref[pos-10 : pos+10])` so that $-1$ always denotes the base synthesized immediately *before* the error cycle.

#### 2. Weight Trimer and Context Analyses by Per-Read Error Instances Divided by Overlapping Read Depth Rather Than Unweighted Unique Genomic Loci
* **WHY:** Counting each mutated genomic position only once across an entire platform (*"counted how many trimers of each type were present in the set of unique error loci"*, line 42) causes common error motifs and deep platforms (`NovaSeq 6000`, 239 runs across a 5 Mb genome) to saturate, compressing enrichment ratios toward 1.0.
* **WHAT:** Compute trimer and post-homopolymer error rates per overlapping sequenced base (total strand-oriented errors occurring at trimer $T$ divided by total overlapping read pairs covering trimer $T$), normalized by the overall dataset error rate.
* **HOW:** Sum the total number of strand-oriented errors at trimer $T$ across all runs of a platform, divide by the total number of overlapping read-pair bases covering trimer $T$ in those same runs, and divide that motif-specific error rate by the platform's global overlap error rate.

#### 3. Correct the Post-Homopolymer Null Expectation Factor from $1/4$ to $1/3$
* **WHY:** At the base immediately following a homopolymer of base $X$, the reference base $Y$ cannot be $X$. Among the 3 possible substitution errors away from $Y$, a random substitution produces base $X$ with probability $1/3$ (or, more precisely, the empirical global substitution fraction $P(\text{error} = X \mid \text{ref} = Y)$), not $1/4$.
* **WHAT:** Replace the division by 4 in the post-homopolymer null calculation (line 46 and Fig. 6) with division by 3 (or condition on the empirical transition/transversion matrix).
* **HOW:** Update the Jupyter notebook generating Figure 6 to compute expected random post-homopolymer errors using $1/3$ (or the platform-specific marginal probability of substituting base $X$ given $Y \ne X$) and re-plot Figure 6.

#### 4. Remove the Contradictory Oxidative Damage Explanation and Fix SAM Flag Descriptions
* **WHY:** Citing sample-handling oxidative damage (`Ma et al.`) to explain overlap mismatch variation contradicts Figure 1, and the SAM flag descriptions in line 32 state the opposite of standard SAM specifications.
* **WHAT & HOW:**
  1. **Oxidative damage (line 56):** Revise line 56 to clarify that unlike reference-comparison studies (such as `Ma et al.`), the paired-end overlap method ignores pre-PCR oxidative sample damage (as shown in Fig. 1), meaning the observed inter-lab variation must arise from flowcell/instrument factors (e.g., cluster density, loading concentration, reagent kit age, or optical calibration) rather than DNA extraction damage.
  2. **SAM flags (line 32):** Correct *"We only counted primary alignments (SAM flag 256) which were mapped (flag 4)"* to *"We only counted primary alignments (excluding secondary alignments, SAM flag 256) which were mapped (excluding unmapped reads, flag 4)"*, matching line 34.
  3. **Robust dispersion metrics in Table 1:** Because platform error rates are strongly right-skewed with outlier clusters, add the **Interquartile Range (IQR)** or **Median Absolute Deviation (MAD)** alongside the Median and Standard Deviation in Table 1, and verify the OLS regression results (lines 38, 74) using $\log_{10}(\text{error rate})$.
