# Review of AN_ANON_021

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.6/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the prevalence and evolutionary conservation of overlapping protein-coding reading frames (dual coding) in mammalian transcripts. Starting from 14,159 orthologous human and mouse canonical coding regions, the authors use column-shuffling and parametric codon simulations to establish a 500 bp minimum length threshold for alternative reading frames (ARFs), identifying 149 initial human-mouse candidates. They then apply a non-parametric Codon Column Replacement Test (CCRT) constructed from ~9,000 orthologous alignments ($p \le 0.05$, retaining 66 candidates), require conservation in rat and/or dog (retaining 40 candidates), and evaluate nucleotide substitution patterns using a context-dependent dual-frame codon substitution model ($\beta_{\text{STOP}} = 0$ likelihood ratio test, passed by 34 candidates) and a position-specific transition/transversion ratio test ($\kappa_{12} = \kappa_3$, passed by 18 candidates), yielding an intersection of 15 high-confidence candidates. Alignments and custom genome browser tracks are hosted on an institutional website, though several mathematical equations in the Materials and Methods are missing from the text.

The study introduces an interesting comparative genomics pipeline and a context-conditioned Markov codon model for overlapping reading frames, addressing a genuine biological question. However, the statistical inference for the 15 "high-confidence" candidates suffers from an inverted hypothesis-testing logic in both secondary evolutionary filters: in four-taxon alignments with low divergence, the authors treat *failure to reject* a constrained null hypothesis ($H_0: \beta_{\text{STOP}} = 0$ and $H_0: \kappa_{12} = \kappa_3$) as positive proof of dual-frame purifying selection. Because statistical power in four mammalian sequences over ~500 bp is low, failing to reject these nulls confounds true dual coding with sparse substitution counts. These limitations can be resolved computationally by reformulating the likelihood ratio tests to reject single-frame neutral evolution in favor of dual-frame constraint, explicitly reporting false discovery rates across the multi-stage scan, and restoring the omitted mathematical expressions in the Methods.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Random overlapping reading frames $\ge 500$ bp in length rarely arise by chance under single-frame evolution (0.1%–0.3%), and 40 mammal-conserved ARFs exceed both this threshold and the CCRT compositional control ($p \le 0.05$): [Well Supported].**  
  The authors combine empirical column-sampling of 14,159 human-mouse alignments with three-taxon parametric codon simulations to account for first-order Markovian hexamer/codon dependencies, showing that $\ge 500$ bp conserved +1/+2 ORFs occur in only 0.1% to 0.29%–0.3% of replicates. The CCRT properly conditions on the exact canonical amino acid sequence and empirical human-mouse codon-pair substitution frequencies, controlling for local amino acid composition and codon usage bias.

* **The codon-based ($\beta_{\text{STOP}} = 0$) and nucleotide-based ($\kappa_{12} = \kappa_3$) likelihood ratio tests positively validate 15 high-confidence functional dual-coding genes: [Methodologically Flawed].**  
  Both tests invert standard frequentist hypothesis testing by placing the biological claim of interest (functional ARF constraint) in the null hypothesis ($H_0: \beta_{\text{STOP}} = 0$ and $H_0: \kappa_{12} = \kappa_3$) and claiming confirmation when the test *fails to reject* $H_0$. With only four mammalian taxa (human, mouse, rat, dog) and regions around 500 bp, total branch length and stop-inducing substitution opportunities are small. Consequently, failing to reject $\beta_{\text{STOP}} = 0$ or $\kappa_{12} = \kappa_3$ primarily reflects a lack of statistical power (Type II error) rather than evidence of purifying selection in the alternative frame. The authors note that under single-frame parametric simulations, the $\beta_{\text{STOP}}$ test rejected $H_0$ in 94% of datasets (6% failure-to-reject), yet they do not report the tree lengths or sequence lengths of those simulations relative to the 40 empirical four-taxon candidates.

* **Composite marginalization over flanking nucleotides in the dual-frame codon model yields a valid joint phylogenetic likelihood across overlapping frames: [Fragile].**  
  In a +1 overlapping reading frame, substitutions at codon $c$ are coupled across the entire transcript because codon $c$ in frame F1 spans codon $c$ and $c+1$ in frame F0. The authors approximate this intractably large state space by conditioning each F0 codon on empirical dinucleotide/nucleotide frequencies ($\pi_{12}, \pi_3$) of its flanking nucleotides ($u_1, u_2, d_1$) and multiplying conditional expectations across codons, and even appear to multiply F0 and F1 likelihoods. This pseudo-likelihood double-counts nucleotide data and ignores evolutionary changes in the flanking context along internal tree branches, which can distort the asymptotic $\chi^2$ distribution of the likelihood ratio test statistic.

* **Specific biological roles for ARF-encoded polypeptides in ADCY8 (mediating $\text{Ca}^{2+}$/calmodulin binding) and MINK1 (driving intermediate domain hypervariability): [Overstated].**  
  In ADCY8, the mutagenesis variant W38A alters a conserved tryptophan in the canonical protein and simultaneously introduces a stop codon in the +1 ARF; attributing the loss of calmodulin binding to the ARF polypeptide rather than the canonical W38A substitution is speculative given no evidence of ARF translation. Similarly, arguing that high cross-species variability in the MINK1 intermediate domain supports dual coding confuses relaxed purifying selection in an unstructured linker domain with compensatory dual-frame acceleration.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Invert the Hypothesis Testing Framework for $\beta_{\text{STOP}}$ and $\kappa_{12}/\kappa_3$
* **WHY:** Accepting $H_0: \beta_{\text{STOP}} = 0$ or $H_0: \kappa_{12} = \kappa_3$ when $p > 0.05$ conflates low tree divergence (sparse substitutions in four species) with active purifying selection against stop codons or third-position transitions in the ARF.
* **WHAT:** Formulate the tests so that the null hypothesis represents standard single-frame evolution ($H_0: \beta_{\text{STOP}} = \beta_{\text{single-frame}}$ or $H_0: \kappa_3 / \kappa_{12} = r_{\text{canonical}}$ estimated from the non-overlapping canonical CDS of the same gene), and require statistically significant rejection ($p < 0.05$) toward $\beta_{\text{STOP}} < \beta_{\text{single-frame}}$ and $\kappa_3 / \kappa_{12} < r_{\text{canonical}}$.
* **HOW:** For each of the 40 candidate transcripts, use the non-overlapping portion of the canonical ORF to estimate baseline $\beta_{\text{STOP}}$ (rate of substitutions that would create stop codons in the shifted frame if it were unconstrained) and the gene-specific $\kappa_3 / \kappa_{12}$ ratio. Perform a one-sided likelihood ratio test comparing the ARF overlap region against these single-frame empirical baselines, and report the exact MLEs, profile likelihood confidence intervals, and $p$-values in Table 1.

#### 2. Calibrate the Dual-Frame Pseudo-Likelihood via Parametric Bootstrap
* **WHY:** Multiplying codon likelihoods conditioned on static extant flanking frequencies ($\pi_{12}, \pi_3$) across F0 and F1 violates conditional independence and invalidates standard asymptotic $\chi^2$ critical values for the LRT.
* **WHAT:** Replace the asymptotic $\chi^2$ approximation for the dual-frame codon model with a sequence-level parametric bootstrap that evolves the entire nucleotide sequence under a single-frame codon model.
* **HOW:** For each of the 40 candidate genes, simulate 1,000 full-length alignments along the inferred four-species tree under a standard single-frame MG94/GY94 model preserving the canonical protein constraint and empirical codon frequencies. Fit the dual-frame composite likelihood model to each simulated alignment to obtain the exact null distribution of the LRT statistic and report calibrated empirical $p$-values.

#### 3. Account for Multiple Testing Across the Genome-Wide Scan
* **WHY:** Scanning 14,159 human-mouse alignments at a 0.1%–0.3% length false-positive rate is expected to yield 14 to 42 false positives by chance alone ($14,159 \times 0.003 \approx 42.5$), which is on the same order as the 149 initial hits and 40 conserved hits.
* **WHAT:** Quantify the genome-wide False Discovery Rate (FDR) after chaining the length filter, the 5% CCRT filter, and the rat/dog conservation filter.
* **HOW:** Apply the Benjamini-Hochberg procedure to the empirical CCRT $p$-values across all 149 candidate ARFs (using 100,000 CCRT permutations so $p$-values have sufficient resolution below $10^{-3}$), and report both raw $p$-values and $q$-values for every gene in Table 1.

#### 4. Temper Speculative Functional Claims in the Discussion
* **WHY:** Without ribosome profiling, mass spectrometry, or canonical-silent / ARF-nonsense mutagenesis, attributing ADCY8 calmodulin binding or MINK1 domain divergence to translated ARF peptides overstates the computational findings.
* **WHAT:** Reframe the ADCY8, MINK1, and RXR$\beta$ narratives as testable experimental hypotheses and explicitly note alternative explanations (canonical missense disruption for ADCY8 W38A; relaxed constraint in disordered linkers for MINK1).
* **HOW:** Revise the Discussion paragraphs on ADCY8 and MINK1 to state that distinguishing canonical residue function from ARF peptide function requires introducing synonymous mutations in the canonical reading frame that create premature stop codons specifically in the +1 ARF.

#### 5. Restore Missing Mathematical Equations and Table Data in the Manuscript Text
* **WHY:** In the Materials and Methods (lines 67–69), every mathematical formula for the instantaneous rate matrix $Q$, equilibrium distribution, conditional phylogenetic likelihood, unconditional expectation, joint likelihood, and null hypothesis is blank/omitted in the text, and Table 1's contents are missing.
* **WHAT & HOW:** Insert the explicit mathematical equations in lines 67–69: (i) $Q_{xy | u_1 u_2 d_1}$ showing how $\alpha, \beta_{01}, \beta_{10}, \beta_{11}, \beta_{\text{STOP}}, R_{nm}$ and codon frequencies are parameterized; (ii) the stationary distribution $\pi_x$; (iii) the marginalization sum $\sum_{u_1, u_2, d_1} \pi_{12}(u_1, u_2) \pi_3(d_1) L_c(x | u_1, u_2, d_1)$; (iv) the full-alignment composite log-likelihood; and (v) include the full 40-gene table in the main text.
