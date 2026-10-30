# Review of AN_ANON_021

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.9 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the prevalence of overlapping protein-coding reading frames (dual coding, where a +1 or +2 alternative reading frame [ARF] overlaps the canonical ORF in the same orientation) across mammalian genomes. Using 14,159 human–mouse orthologous coding alignments, the authors first perform codon-column resampling and phylogenetic codon simulations to establish a 500 bp length threshold ($\le 0.1\%$–$0.3\%$ false-positive rate in simulated 5,000-codon alignments), identifying 149 candidate conserved human–mouse ARFs. They then introduce the Codon Column Replacement Test (CCRT), which resamples empirical human–mouse codon alignments while preserving the canonical amino acid sequence, reducing the candidate set to 66 ARFs ($p \le 0.05$), and filter for conservation in rat and/or dog to yield 40 candidates. Finally, they develop a context-dependent dual-frame codon substitution model (testing $\beta_{\text{STOP}} = 0$) and a codon-position transition/transversion ratio test ($\kappa_{12} = \kappa_3$), intersecting them to highlight 15 candidate dual-coding genes.

The comparative screen and the CCRT conditional resampling test provide a creative control for amino acid composition and codon usage bias in the canonical reading frame. However, the two downstream substitution tests used to validate the 15 "high-confidence" candidates suffer from fundamental statistical flaws: both tests place the functional dual-coding hypothesis in the null hypothesis ($H_0: \beta_{\text{STOP}} = 0$ and $H_0: \kappa_{12} = \kappa_3$) and treat failure to reject $H_0$ ($p > 0.05$) in 4-species alignments as positive evidence of dual coding. Because candidate regions were already selected for having zero stop codons in the ARF across all four species, $\beta_{\text{STOP}} = 0$ is pre-conditioned by ascertainment, and with only four closely related mammals, failing to reject $\kappa_{12} = \kappa_3$ primarily reflects low statistical power rather than purifying selection on a second polypeptide. Furthermore, the dual-frame Markov model multiplies the marginal likelihoods of frame 0 and frame +1 together, double-counting the same nucleotide alignment. These issues can be resolved through computational re-analysis by inverting the hypothesis tests to test against a single-frame null and correcting for ascertainment.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Long conserved overlapping open reading frames ($\ge 500$ bp) occur in mammalian transcripts far more often than expected from canonical amino acid composition and codon usage alone (40 conserved candidates): [Moderately Supported].**  
  The CCRT approach—resampling empirical human–mouse orthologous codon columns conditional on the exact canonical amino acid sequence—directly controls for amino acid composition and species-specific dicodon usage bias. However, the 149 initial human–mouse candidates were tested at a nominal $p \le 0.05$ without multiple-testing correction (where $\sim 7.5$ false positives are expected by chance), and the initial 500 bp cutoff was derived from fixed 5,000-codon simulated alignments rather than being calibrated to the empirical length distribution of the 14,159 human–mouse transcripts.

* **The codon substitution model ($\beta_{\text{STOP}}$ test) and transition/transversion ratio test ($\kappa_{12} = \kappa_3$) independently confirm 15 high-confidence functional dual-coding genes: [Methodologically Flawed].**  
  Both tests invert standard hypothesis testing by placing the biological signal of interest (dual-coding constraint) in the null hypothesis ($H_0: \beta_{\text{STOP}} = 0$ and $H_0: \kappa_{12} = \kappa_3$) and declaring candidates "confirmed" when $H_0$ is not rejected ($p > 0.05$). In a 4-species alignment of $\sim 500$ bp, statistical power is low—as the authors themselves note when explaining why other candidates failed—meaning that low-divergence or short alignments naturally fail to reject $\kappa_{12} = \kappa_3$. Moreover, because the 40 candidates were explicitly filtered to contain no stop codons in the ARF across human, mouse, and rat/dog, terminal branches cannot exhibit stop-introducing substitutions in the ARF, inducing severe post-selection circularity in testing $\beta_{\text{STOP}} = 0$.

* **The context-dependent dual-frame codon substitution model accurately captures the joint phylogenetic likelihood of overlapping reading frames: [Methodologically Flawed].**  
  In Materials and Methods, the authors define separate rate matrices for frame $F_0$ (conditioned on $u_1, u_2, d_1$) and frame $F_1$ (conditioned on $u_1, d_1, d_2$), marginalize each codon over empirical alignment-wide flanking frequencies $\pi_{12}$ and $\pi_3$, and then define the joint dataset likelihood as the product of the $F_0$ likelihood and the $F_1$ likelihood. Multiplying the likelihood of $F_0$ and $F_1$ evaluates the exact same nucleotide substitutions twice, violating conditional independence and invalidating the asymptotic $\chi^2$ distribution of the likelihood ratio test.

* **Conserved ARFs in genes such as *ADCY8*, *MINK1*, and *RXR$\beta$* encode functional polypeptides rather than reflecting non-coding nucleotide constraints: [Fragile].**  
  While *RXR$\beta$* has prior transcript evidence of an alternative N-terminus via exon skipping, comparative conservation of an ARF and suppressed third-position substitution rates in the canonical frame can also arise from overlapping *cis*-regulatory elements, splicing enhancers, antisense transcripts, or RNA secondary structures that constrain synonymous sites and coincidentally preserve an open reading frame, without translation of a functional second protein.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Invert the Substitution Hypothesis Tests to Test Against a Single-Frame Null
* **WHY:** Treating failure to reject $H_0: \kappa_{12} = \kappa_3$ or $H_0: \beta_{\text{STOP}} = 0$ as positive confirmation conflates low statistical power (only 4 species) with purifying selection in the alternative reading frame.
* **WHAT:** Reformulate the substitution tests so that single-frame evolution (with canonical synonymous/nonsynonymous rates and unconstrained ARF stop codons conditional on canonical amino acid conservation) is the null hypothesis $H_0$, and purifying selection on the ARF ($\beta_{01} < \alpha$ in $F_0$, i.e., suppression of substitutions that are synonymous in $F_0$ but nonsynonymous in $F_1$) is the alternative hypothesis $H_A$.
* **HOW:** Using the existing four-species alignments, fit a nested codon model in $F_0$ where $H_0$ constrains $\beta_{01} = \alpha$ (synonymous changes in $F_0$ evolve neutrally regardless of whether they are nonsynonymous in $F_1$) and $H_A$ allows $\beta_{01} < \alpha$. Require significant rejection of $H_0$ ($p < 0.05$ after Benjamini–Hochberg FDR correction) to call high-confidence dual coding.

#### 2. Eliminate Double-Counting in the Dual-Frame Likelihood Function
* **WHY:** Multiplying the unconditional likelihood of codon $c$ in frame $F_0$ by its likelihood in frame $F_1$ counts every nucleotide site twice, inflating log-likelihood differences by roughly a factor of two.
* **WHAT:** Formulate the likelihood strictly in the canonical frame $F_0$ conditioned on flanking nucleotides (which already fully specifies whether each single-nucleotide change in $F_0$ is synonymous, nonsynonymous, or stop-inducing in $F_1$), without multiplying by a redundant $F_1$ likelihood term.
* **HOW:** Retain only the $F_0$ conditional rate matrix $Q(u_1, u_2, d_1)$ in the likelihood product over codons $c = 2, \dots, S-1$, since the four rate parameters ($\alpha, \beta_{01}, \beta_{10}, \beta_{11}$) and $\beta_{\text{STOP}}$ already partition substitutions by their joint effect in both $F_0$ and $F_1$.

#### 3. Correct for Stop-Free Ascertainment Bias and Multiple Testing in the Screen
* **WHY:** Conditioning on uninterrupted $\ge 500$ bp ARFs across four species guarantees zero observed stop codons at the tips, biasing $\hat{\beta}_{\text{STOP}}$ toward zero, while applying an unadjusted $p \le 0.05$ CCRT threshold across 149 candidates admits false positives.
* **WHAT:** Apply false discovery rate (FDR) correction to the CCRT empirical $p$-values across all 149 candidates, and calibrate the substitution LRT null distribution by conditioning simulated single-frame alignments on having an uninterrupted $\ge 500$ bp ARF across all four species.
* **HOW:** From the parametric single-frame codon simulations (Figure S2), retain only the subset of simulated alignments that happen to preserve an uninterrupted $\ge 500$ bp ARF across the four taxa, and use the distribution of LRT statistics on those ascertained null alignments to compute empirical $p$-values.

#### 4. Control for Synonymous Constraint and RNA Structure Confounders
* **WHY:** Ultra-conserved coding exons (e.g., due to exonic splicing enhancers or RNA secondary structure) have very low synonymous substitution rates ($d_S \approx 0$), which passively preserves long open reading frames in shifted frames across mammals without encoding a second protein.
* **WHAT:** Stratify or normalize the CCRT and substitution tests by the local synonymous substitution rate ($d_S$) of the canonical reading frame relative to the rest of the same gene.
* **HOW:** For each of the 40 candidates, compare $d_S$ (and specific $\beta_{10}$ vs. $\beta_{01}$ asymmetry) inside the ARF overlap against the non-overlapping canonical coding region of the same transcript, demonstrating that substitutions that are synonymous in $F_1$ but nonsynonymous in $F_0$ or vice versa show frame-specific purifying selection rather than uniform nucleotide conservation.
