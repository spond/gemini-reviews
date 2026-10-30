# Review of AN_ANON_055

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces an automated reference-aligned paired-end read overlap method to estimate instrument-specific sequencing error rates across public Sequence Read Archive (`SRA`) datasets, applying it to `1,126` *Escherichia coli* runs across seven Illumina platforms (`MiSeq`, `MiniSeq`, `NextSeq 500`, `NextSeq 550`, `HiSeq 2500`, `NovaSeq 6000`, and `HiSeq X Ten`). By restricting comparisons to overlapping paired-end segments in the `50–60%` read-length bin (requiring $\ge 2.5\text{ Mb}$ of overlap per run), the authors report median discordance rates ranging from `0.087%` (`HiSeq X Ten`) and `0.109%` (`NovaSeq 6000`) to `0.593%` (`NextSeq 550`) and `0.613%` (`MiniSeq`), demonstrate via regression that submitting research group explains as much variance as instrument model, and profile sequence context, trimer motifs (`GGT`), and post-homopolymer substitution errors. Code and processed intermediate files are publicly archived.

The core study design—using paired-end overlap discordance at a standardized read-length bin to survey real-world sequencing accuracy across $>1,100$ public runs—is a useful empirical contribution, and the demonstration of massive inter-lab variability within each platform is convincing. However, three methodological issues affect the quantitative error rates and sequence-context conclusions: (1) in the sequence-context (Figure 3) and trimer (Figure 4) analyses, errors are collapsed to unweighted *unique genomic error loci* rather than weighted by error rate per overlapping read base, causing high-depth platforms (`NovaSeq 6000`, `HiSeq X Ten`) to saturate the `~5 Mb` *E. coli* genome and artificially flatten their motif enrichment toward the genomic background; (2) the null expectation for post-homopolymer errors (Figure 6, line 46) divides by `4` instead of `3` possible non-reference substitution bases, inflating all enrichment ratios by $4/3$ (`33%`); and (3) the main text (line 56) attributes inter-sample error variation to pre-sequencing oxidative DNA damage, directly contradicting the method's central premise (Figure 1, line 20) that pre-cluster DNA damage is fixed in both mates and invisible to read-overlap comparison. All three issues can be resolved by re-computing weighted error rates from the existing intermediate files and revising the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Large intra-platform and inter-laboratory variation in public Illumina dataset accuracy: [Well Supported].**  
  Across `1,126` runs with $\ge 2.5\text{ Mb}$ of overlap in the `50–60%` read-length bin, within-platform standard deviations (`0.126%` to `0.938%`) rival or exceed between-platform differences (`0.087%` to `0.613%` median), and specific outlier clusters (such as `23` `NovaSeq 6000` runs around `0.683%`) trace cleanly to specific submitting centers/groups.

* **`HiSeq X Ten` and `NovaSeq 6000` are largely exempt from preceding-base substitution bias and motif-dependent (`GGT`) errors (Figures 3 and 4): [Methodologically Flawed].**  
  In Materials and Methods (lines 40–42), context and trimer profiles are computed over the *set of unique genomic error loci* (taking only the single most common substitution at each genomic coordinate) rather than counting error events divided by the number of overlapping read pairs covering each genomic trimer. Because the *E. coli* genome has only $\sim 5 \times 10^6$ sites, pooling `163` `HiSeq X Ten` or `239` `NovaSeq 6000` high-coverage runs accumulates billions of overlapping bases, causing a large fraction of all genomic coordinates to experience at least one error. As the set of unique error loci approaches the full genome, unweighted locus counts mathematically converge toward the background genomic base and trimer composition (normalized ratio $\to 1.0$), creating an artificial appearance of context independence on high-throughput platforms.

* **Post-homopolymer substitution over-representation relative to random expectation (Figure 6): [Moderately Supported].**  
  The qualitative finding that post-homopolymer substitution rates increase with homopolymer length and differ between `G/C` and `A/T` runs across platforms is sound. However, the null expectation formula in line 46 (*"multiplied this frequency by the total number of errors detected, and divided by four"*) is mathematically miscalibrated: at any genomic site where a substitution error occurs, there are only **3** possible non-reference bases (not 4), and at the base immediately terminating a homopolymer of base $B$ of exact length $L$, the reference base cannot be $B$, so $B$ is always one of the 3 possible substitution outcomes (probability $1/3$ under uniform random substitution). Dividing by 4 instead of 3 inflates every enrichment value in Figure 6 by $33.3\%$, obscuring which `NovaSeq 6000` G/C points truly fall below neutral expectation (`1.0`).

* **Paired-end overlap discordance measures single-read error rate in the assigned bin: [Fragile].**  
  Dividing mismatching base pairs by the number of overlapping base pairs (line 36) measures the *combined* probability that either Read 1 or Read 2 suffered an error ($\epsilon_1 + \epsilon_2 - \frac{4}{3}\epsilon_1\epsilon_2 \approx \epsilon_1 + \epsilon_2$). Because errors assigned to the `50–60%` maximum-bin require both R1 and R2 to be at $\le 60\%$ of their read length (and thus both near `50–60%` for typical overlapping fragments), $\epsilon_1 \approx \epsilon_2$, meaning the reported discordance rate is nearly $2\times$ the single-read per-base error rate at cycle `50–60%`.

* **Oxidative DNA damage from sample handling explains inter-sample variation in overlap error rates (Line 56): [Methodologically Flawed].**  
  In Results (line 56), the authors cite Ma et al. (5) to suggest that variation in their measured error rates *"may come from oxidative damage introduced by differential sample handling."* This directly contradicts Figure 1 and the Introduction (line 20), which correctly establish that pre-sequencing DNA damage, PCR errors, and sample polymorphisms are present in the single ancestor molecule of an Illumina flowcell cluster and therefore appear identically in both Read 1 and Read 2 without generating overlap discordance.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Weight Sequence Context and Trimer Enrichment by Per-Read Error Rate Rather Than Unweighted Unique Genomic Loci
* **WHY:** Collapsing errors across hundreds of deep *E. coli* runs to unweighted unique genomic coordinates (lines 40–42) causes high-depth platforms (`NovaSeq 6000`, `HiSeq X Ten`) to saturate the 5 Mb genome, driving trimer and context ratios toward the genomic background (`1.0`).
* **WHAT:** Recompute Figure 3 (context base frequencies) and Figure 4 (trimer enrichment) using total error event counts normalized by total overlapping read depth covering each trimer/context (or compute per-run trimer enrichment ratios before taking the platform median).
* **HOW:** For each run $i$ and trimer $t$, compute the empirical error rate $r_{i,t} = \text{errors}_{i,t} / \text{overlap\_bases}_{i,t}$ and normalize by the run's overall error rate $\bar{r}_i$. Plot the distribution or median of $r_{i,t} / \bar{r}_i$ across runs for each platform in Figure 4, and verify whether `NovaSeq 6000` and `HiSeq X Ten` still lack preceding-base bias when weighted by event counts.

#### 2. Correct the Post-Homopolymer Null Model Denominator from 4 to 3 and Match Reference Genomes
* **WHY:** A substitution error away from the reference base has 3 possible mutant nucleotide outcomes, not 4; furthermore, computing background trimer and homopolymer counts from a single reference (`NZ_CP044311.1`) ignores genomic content differences across the `1,292` *E. coli* assemblies used for alignment, and ignores non-uniform overlap coverage across the genome.
* **WHAT:** Replace the factor of $1/4$ in line 46 with the exact conditional substitution probability ($1/3$ under uniform substitution, or empirical platform substitution matrix probabilities) and compute expected homopolymer counts directly from the overlapped read regions.
* **HOW:** Multiply all values in Figure 6 by $3/4$ (or normalize by the exact number of overlapped post-homopolymer bases sequenced in each run), and update line 46 and the discussion of `NovaSeq 6000` G/C post-homopolymer depletion in line 99.

#### 3. Clarify Pairwise Discordance ($\epsilon_1 + \epsilon_2$) vs. Single-Read Error Rate ($\epsilon$) and Remove the Contradictory DNA Damage Explanation
* **WHY:** An overlapping base pair mismatches if either Read 1 or Read 2 errs, and pre-cluster DNA damage affects both reads identically (except in rare PCR-free heteroduplex bridge-amplification events).
* **WHAT:** Explicitly state in Materials and Methods (line 36) and Table 1 that overlap discordance in symmetric mid-read bins equals $\approx 2\epsilon$, and reconcile line 56 with Figure 1.
* **HOW:** Add a note in line 36 explaining that when R1 and R2 overlap at `50–60%` of read length, the pairwise mismatch rate reflects the sum of R1 and R2 error rates ($\epsilon_{\text{R1}} + \epsilon_{\text{R2}}$). In line 56, replace the oxidative DNA damage explanation with factors that genuinely affect on-instrument cluster sequencing (e.g., cluster density/overclustering, library insert size distribution, reagent kit age, and flowcell loading concentration).

#### 4. Use Log-Transformed or Non-Parametric Regression for Skewed Error Rates with Collinear Group/Platform Predictors
* **WHY:** Error rates in Figure 2 and Table 1 are strongly right-skewed and heteroscedastic (`SD` up to twice the median), violating ordinary least squares (`OLS`) homoscedasticity assumptions, and many submitting groups only use a single instrument model.
* **WHAT:** Fit the regression in line 38 on $\log_{10}(\text{error rate})$ (or use a Gamma/beta GLM) and report partial $R^2$ (type II/III ANOVA variance explained) for `platform` vs. `group` restricted to groups that submitted data on $\ge 2$ platforms.
* **HOW:** In `statsmodels`, run `ols('np.log10(error_rate) ~ C(model) + C(group)', data=df).fit(cov_type='HC3')` and report the heteroscedasticity-robust $p$-values and partial $\eta^2$ in Supplementary Figures S1–S2.
