# Review of AN_ANON_026

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates why coadaptation between bacterial hosts and small multicopy nonconjugative plasmids typically leaves the plasmid sequence unchanged while adaptive mutations fix on the host chromosome. The authors evolve *Escherichia coli* DH5$\alpha$ (`recA1`) carrying plasmid pBR322 in a turbidostat under tetracycline selection across two short-term (60 h; R1, R2) and two long-term (318 h; R6, R7) replicates, applying duplex sequencing across 24 longitudinal plasmid samples alongside whole-genome sequencing of the host chromosome and plasmid-curing growth assays. Duplex sequencing reveals that low-frequency (<1%) de novo variants arise rapidly and reproducibly at 10 sites in the ColE1 replication origin (bases 3,027–3,035 in loop II' of RNAI and base 3,118 in the $-35$ promoter of RNAII, both known to increase copy number), track across intermediate time points, and then crash to extinction (R6) or near-extinction (R7) as chromosomal mutations in `treB` (Val112Glu) and `recA` (Asp161Gly) sweep through the host population. The authors formulate a 7-parameter mathematical model of intracellular plasmid segregation, replication, mutation, and copy-number-dependent selection to interpret these dynamics.

The experimental design—combining turbidostat selection, ultra-sensitive duplex sequencing, host whole-genome sequencing, and single-colony plasmid curing—provides direct empirical resolution of transient sub-1% adaptive plasmid trajectories that were invisible to conventional sequencing. However, the mathematical modeling component has notable limitations: fitting 7 free parameters to a single summed allele-frequency trajectory results in biologically implausible mutation rate estimates ($\hat{\mu} = 5.09 \times 10^{-5}$ per plasmid across just 10 sites, roughly $10^3$–$10^4$-fold higher than the empirical *E. coli* mutation rate, and $\hat{\gamma} = 1.55 \times 10^{-3}$ for beneficial chromosomal mutations), and because chromosomal mutation is modeled as a continuous deterministic flux into a background where plasmid copy number is neutral ($S = 1$ for all $1 \le w+m < \kappa_T$), the best-fit simulation plateaus at $\sim 0.4\%$ rather than recapitulating the observed extinction of plasmid variants. Constraining mutation rates to empirical priors and modeling the chromosomal sweep as a discrete clonal origin on a wild-type plasmid background will resolve this discrepancy without requiring new experiments.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Sub-1% adaptive mutations in the pBR322 ColE1 replication control region (RNAI loop II' bases 3,027–3,035 and the RNAII $-35$ promoter base 3,118) emerge reproducibly early in selection before declining: [Well Supported].**  
  Duplex sequencing across four independent turbidostat runs (R1, R2, R6, R7) consistently detects the same 10 replication-origin sites rising from 0% at $t=0$ to $\sim 0.1\%$–$0.9\%$ before declining, whereas non-origin variants behave as transient single-family "flickering" neutral drift sites.

* **Long-term fitness gains are driven by chromosomal mutations (`treB` Val112Glu and `recA` Asp161Gly) that adapt the host to the growth environment and sweep the wild-type plasmid background to fixation: [Well Supported].**  
  Whole-genome sequencing, population vs. single-colony growth rate measurements before and after Bochner/Maloy plasmid curing (Table 1), and Sanger verification of cured R7 clones (Figure S6) convincingly demonstrate that the `treB` and `recA` mutations double host growth rate independently of pBR322 carriage, explicarly accounting for the population-vs.-clone growth rate difference between R6-S27 (91–92% mutant) and R7-S27 (7–39% mutant).

* **Stochastic intracellular segregation and the trade-off between tetracycline efflux benefit and metabolic/membrane-potential cost prevent copy-number mutations from fixing: [Moderately Supported].**  
  The biological mechanism—balancing *trans*-acting RNAI / *cis*-acting RNAII copy number control against the toxicity of TetA efflux pump overexpression and segregational dilution at cell division—is biophysically sound and consistent with prior literature.

* **The 7-parameter optimization model accurately estimates the evolutionary parameters governing plasmid heteroplasmy and explains the trajectory of mutant plasmids: [Fragile].**  
  While the model reproduces an initial rise followed by a reduction in mutant plasmid frequency (Figure 2), two issues undermine the parameter estimates in Table 2: (1) the inferred plasmid mutation rate ($\hat{\mu} = 5.09 \times 10^{-5}$ per plasmid per generation into the 10 *ori* sites, or $\sim 5 \times 10^{-6}$ per base) and beneficial chromosomal mutation rate ($\hat{\gamma} = 1.55 \times 10^{-3}$ per generation) exceed known *E. coli* beneficial mutation rates by 3–4 orders of magnitude; and (2) as the authors candidly note, the model fails to reproduce the empirical crash of plasmid variants to zero, instead stabilizing at a $\sim 0.4\%$ mutation-selection plateau because $\hat{\mu}$ is artificially high and $S(1, w+m) = 1$ imposes no cost on elevated plasmid copy number once $g = 1$.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Modify the Fitness Function on the Chromosomal-Mutant ($g=1$) Background and Constrain Mutation Rates to Empirical Priors
* **WHY:** In the current piecewise fitness function $S(g, w+m)$, cells with the chromosomal mutation ($g=1$) have survival probability $1.0$ for all plasmid copy numbers $1 \le w+m < \kappa_T = 25$. Because mutant plasmids replicate faster ($R = 3.417 > r = 1.539$) and arise at an inflated rate ($\hat{\mu} = 5.09 \times 10^{-5}$), mutant plasmids continuously accumulate inside $g=1$ cells until hitting the $\kappa_T$ cliff, creating the artificial $\sim 0.4\%$ plateau in Figure 2 rather than crashing to 0% as observed in R6. Moreover, metabolic burden for $w+m > \kappa^*$ still applies in $g=1$ cells in reality.
* **WHAT:** Re-fit the model with (i) the metabolic cost for $w+m > \kappa^*$ preserved on the $g=1$ background, and (ii) $\mu$ and $\gamma$ constrained to biologically realistic *E. coli* bounds ($\mu \in [10^{-9}, 10^{-7}]$ for the 10-bp target; chromosomal sweep initiated as a single mutant lineage at generation $t_{\text{sweep}}$ or low $\gamma$).
* **HOW:** In the Jupyter notebook optimization (`optim`), update the first branch of $S(1, w+m)$ so that copy numbers exceeding $\kappa^*$ incur the same linear metabolic penalty $\frac{\kappa_T - (w+m)}{\kappa_T - \kappa^*}$ (scaled by the chromosomal fitness advantage), restrict the upper bound of $\mu$ to $10^{-7}$, and re-run the trajectory simulation to verify that the plasmid variant frequency decays to zero after the chromosomal sweep fixes.

#### 2. Assess Parameter Identifiability and Report Confidence Intervals from the 1,863 Converged Runs
* **WHY:** Fitting 7 parameters to a single 1D time series of 11 time points is underdetermined, and Table 2 reports only the single best point estimate without uncertainty intervals or correlation structure among parameters.
* **WHAT:** Quantify parameter uncertainty and collinearity across the top-performing converged optimization runs (e.g., the top 5% lowest-cost solutions out of the 1,863 runs).
* **HOW:** Using the existing 1,863 optimization outputs already generated for Figure S7, report the median and interquartile range (or 95% profile intervals) for each parameter in Table 2, and include a pairwise scatter/correlation matrix in the Supplement to show trade-offs between $(r, R)$ and $(\kappa^*, \kappa_T)$.

#### 3. Provide Direct SRA/ENA Accession Numbers for the Raw Duplex and Whole-Genome Sequencing Reads
* **WHY:** The Data Availability section links to the GitHub repository containing the Jupyter notebooks and optimization data, and Materials and Methods links to the variant-calling workflows, but no NCBI SRA or ENA accession numbers are listed for the 24 raw duplex-sequencing FASTQ datasets or the host whole-genome sequencing reads.
* **WHAT:** Add the public sequence read archive accession numbers to the Data Availability section.
* **HOW:** Deposit the raw MiSeq FASTQ files for the 24 plasmid duplex libraries and 4 chromosomal WGS libraries in NCBI SRA / ENA and list the BioProject accession in Data Availability.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several minor typographical errors and duplicated sentences appear in the Materials and Methods and Results sections.
* **WHAT & HOW:**
  * **Introduction (line 18):** Change `"a mutation rate of 10^5 per plasmid per generation"` to `"10^-5 per plasmid per generation"` to match line 16.
  * **Materials and Methods (line 83):** Delete the duplicated sentence (`"At each of these empirically determined generations, we computed the empirical mutant frequency as the sum of frequencies of mutations in bases 3,027–3,035 and 3,118 determined in turbidostat experiments."`), which is repeated verbatim twice in a row.
  * **Materials and Methods (line 85):** Fix typo `"nad infer the model parameters"` $\rightarrow$ `"and infer the model parameters"`.
  * **Materials and Methods (lines 67–68):** Explicitly state how continuous non-integer replication products ($r \cdot w$ and $R \cdot m$ when $r=1.539, R=3.417$) are mapped or rounded onto discrete integer plasmid states $(w, m) \in \{0, \dots, \kappa_T - 1\}$.
