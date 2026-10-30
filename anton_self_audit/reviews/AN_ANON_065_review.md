# Review of AN_ANON_065

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `RASCL` (Rapid Assessment of Selection within CLades), an automated phylogenetic pipeline and web workflow for characterizing gene- and codon-level natural selection within rapidly expanding viral lineages using large surveillance repositories. Given a "query" whole-genome FASTA set (e.g., a SARS-CoV-2 PANGO lineage) and a "background" reference diversity set (from ViPR or Nextstrain), `RASCL` splits genomes into individual coding sequences, compresses each alignment via complete-linkage `TN93` genetic-distance clustering (`tn93-cluster`) to a target size $D$ (typically $300\text{--}1,000$ sequences), infers maximum-likelihood gene trees (`RAxML-NG` or `IQ-TREE`) with parsimony-labeled internal branches, and executes nine `[SOFTWARE_PACKAGE]` selection analyses (`BUSTED[S]`, `SLAC`, `BGM`, `FEL`, `MEME`, `RELAX`, `Contrast-FEL`, `FADE`, and `FitMultiModel`) restricted to internal tree branches. Results are compiled into JSON reports and rendered in an interactive `ObservableHQ` dashboard. The authors apply `RASCL` to SARS-CoV-2 VOC/VOI clades including BA.1 ($N=112,017$ compressed to a median of 524 sequences), BA.2, BA.5, Delta, Mu (B.1.621), Lambda, Gamma, and Alpha. Source code (`Snakemake`), `[SOFTWARE]` workflows, background sequences, and interactive dashboards are publicly available.

`RASCL` provides a practical, well-engineered workflow that makes sophisticated codon-based phylogenetic selection models operational at genomic surveillance scales, and its restriction of inference to internal branches is a sensible safeguard against singleton sequencing errors and transient within-host mutations. However, several methodological and reporting issues weaken the quantitative claims: (1) complete-linkage diversity-maximizing clustering (`tn93-cluster`) preferentially retains divergent outlier sequences—including recurrent amplicon-dropout and alignment-gap artifacts (visible in Table 3, where all five highlighted BA.5 Spike sites carry `-8` to `-9` gap states)—while collapsing high-frequency clonal lineages, distorting branch-length distributions without a subsampling sensitivity control; (2) `BUSTED[S]` parameter estimates in Table 2 display severe boundary/identifiability pathologies (e.g., Spike $\omega_3 = 64,042.59$ with weight $p_3 = 0.00$ and leader $\omega_3 = 8,003.48$ with $p_3 = 0.00$) that are reported at face value without discussion; (3) no empirical wall-clock runtime or parallel scaling benchmarks are provided to substantiate the headline claim that reports are generated "within hours"; and (4) multiple supplementary table captions (S8–S14) are mislabeled as "BA.1 clade" when describing BA.5 and B.1.621 analyses. All of these issues can be resolved through subsampling sensitivity controls, numerical reporting cleanups, and a runtime benchmark table.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Modular `Snakemake` and `[SOFTWARE]` workflow integration with `JSON`/`ObservableHQ` reporting standardizes multi-model codon selection screens: [Well Supported].**  
  The pipeline architecture (Figure 1), combining automated coordinate extraction, `TN93` clustering, tree inference, nine `[SOFTWARE_PACKAGE]` models on internal branches, and interactive web notebooks (Figure 2), is fully implemented, open-source, and documented with live dashboards.

* **Diversity-based `tn93-cluster` subsampling compressing $>10^5$ genomes by $>99\%$ preserves evolutionary signal while mitigating sequencing errors via internal-branch restriction: [Moderately Supported].**  
  Restricting tests to internal branches removes singleton tip errors, and distance clustering preserves rare divergent haplotypes. However, maximizing pairwise `TN93` distance across $>10^5$ consensus genomes inevitably enriches for shared bioinformatic artifacts (such as recurrent primer/amplicon dropouts or frameshift indels shared by $\ge 2$ sequences, which form artificial internal branches). Indeed, in Table 3 (BA.5 Spike), every highlighted site (`Codons 339, 371, 440, 764, 1162`) contains $8\text{--}9$ gap characters (`-8`, `-9`) in the compressed BA.5 alignment. Furthermore, the manuscript provides no stability analysis across different target sample sizes $D$ or across alternative subsampling schemes (e.g., temporal/geographic stratification vs. `tn93-cluster`).

* **`BUSTED[S]` identifies gene-wide episodic diversifying selection across 14/21 BA.5 segments, including Spike ($\omega_3 = 64,042.59$, $p_3 = 0$) and leader ($\omega_3 = 8,003.48$, $p_3 = 0$): [Fragile].**  
  In Table 2, both Spike (`S`) and `leader` have an inferred positive selection rate class $\omega_3 > 8,000$ assigned to a rounded proportion of sites/branches $p_3 = 0.00$ ($<0.005$), with $p = 0$ and $p = 0.0002$, respectively. In random-effects branch-site models, $\hat{\omega}_3 \to \infty$ as $\hat{p}_3 \to 0$ is a well-known boundary pathology caused by one or a few branch-site combinations having zero inferred synonymous substitutions (or multinucleotide mutations/alignment gaps). Presenting $\omega_3 = 64,042.59$ without noting boundary non-identifiability or cross-checking whether the signal disappears under `FitMultiModel` (which accounts for multi-nucleotide substitutions and is listed in Methods on Line 47 but never reported in Results) overstates the robustness of the gene-wide test.

* **`RASCL` yields selection reports "within hours of being deployed" and its 4-point heuristic ranking (Table 4) prioritizes emergent adaptive sites: [Moderately Supported].**  
  While plausible on multi-core clusters, the manuscript presents zero runtime or computational resource measurements (wall-clock hours, CPU core-hours, memory usage per gene for $D=300$ vs. $D=1,000$). Likewise, the 4-point site ranking protocol for B.1.621 (Table 4, Lines 139–147) uses an uncalibrated sum of four binary criteria (with `MEME` thresholded at a permissive $q \le 0.20$) without retrospective validation showing that Rank 4 sites have higher predictive value for future clade expansion than lower-ranked sites.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Subsampling Sensitivity Analysis and Filter Amplicon-Dropout Gap Artifacts
* **WHY:** Complete-linkage distance clustering (`tn93-cluster`) enriches for outlier sequences, including shared sequencing/assembly gap artifacts (evidenced by the `-8` and `-9` gap counts at all five highlighted BA.5 Spike sites in Table 3).
* **WHAT:** Quantify the stability of site-level (`MEME`/`FEL`) and gene-level (`BUSTED[S]`) detections across varying cluster targets ($D \in \{200, 500, 1000\}$) and after masking/filtering sequences with局部 amplicon dropout gaps.
* **HOW:** Re-run the BA.5 Spike analysis at $D = 250, 500, \text{ and } 1000$ with and without pre-filtering sequences containing $>1\%$ ambiguous/gap bases in Spike, and report the Jaccard overlap of significant sites ($p \le 0.05$ and $q \le 0.10$) and the resulting Table 3 site profiles.

#### 2. Report `FitMultiModel` (`FMM`) Results and Flag Boundary $\omega_3$ Estimates in Table 2
* **WHY:** `FitMultiModel` is explicitly included in the `RASCL` methods list (Line 47) to detect multi-nucleotide instantaneous substitutions, which are a major source of false-positive $\omega_3 \gg 1, p_3 \approx 0$ boundary estimates in `BUSTED[S]` (Table 2: Spike $\omega_3 = 64,042.59, p_3 = 0$; leader $\omega_3 = 8,003.48, p_3 = 0$).
* **WHAT:** Report the `FMM` test results alongside `BUSTED[S]` in Table 2, format $p_3$ and $p$-values in scientific notation (e.g., $p_3 = 1.2 \times 10^{-4}$, $p < 10^{-16}$ rather than `0`), and add a footnote explaining that $\omega_3 > 1,000$ at $p_3 \approx 0$ reflects boundary optimization where local synonymous rate approaches zero.
* **HOW:** Extract the `FMM` JSON outputs already generated by the BA.5 `RASCL` run, add an `FMM p-value` column to Table 2, and replace exact `0` entries in `p3`, `p`, and `q` with exact scientific notation or `< 1e-4`.

#### 3. Provide an Empirical Wall-Clock Runtime and Hardware Benchmark Table
* **WHY:** The Abstract and Conclusions emphasize that `RASCL` overcomes the computational bottleneck of phylogenetic selection models and delivers results "within hours," but no timing data are provided.
* **WHAT:** Add a table reporting the wall-clock runtime (broken down by Phase 1: Map/Compress, Phase 2: Tree Inference, and Phase 3: each `[SOFTWARE_PACKAGE]` selection method) and CPU core allocation for at least two lineages in Table 1 (e.g., BA.1 at median $N=524$ and Delta at median $N=59$).
* **HOW:** Summarize the `Snakemake` benchmark logs (`--benchmarks`) from the BA.1 and BA.5 runs on a specified CPU architecture (e.g., 32 or 64 cores).

#### 4. Standardize Multiple-Testing Thresholds and Fix Copy-Pasted Supplementary Table Captions
* **WHY:** Significance thresholds shift across sections without justification ($p \le 0.05$ and $p \le 0.0001$ in Table 1; $q \le 0.10$ for `BUSTED[S]` in Table 2; $q \le 0.20$ for `MEME` in Table 4), and Supporting Information captions S8–S14 contain copy-paste errors referring to "BA.1 clade" for BA.5 and B.1.621 results.
* **WHAT & HOW:**
  * **Supporting Information Captions (S8 Table, S9 Table, S10 Table, S12 Table, S14 Table):** Correct *"internal branches BA.1 clade"* and *"Ratio of omega (BA.1: background)"* to refer to **BA.5** (for S8–S12) and **B.1.621 (Mu)** (for S14).
  * **Main Text (Line 208):** Change *"rendered uncapable of providing results"* to *"rendered incapable of providing results"*.
  * **Supporting Information (Line 251):** Change *"Segment corresponds to the gene or ORF does under analysis. Omega1 refers to the first omega rate class... Omega2 refers to the first omega rate class... Omega3 refers to the first omega rate class"* to *"first"*, *"second"*, and *"third omega rate class"*.
