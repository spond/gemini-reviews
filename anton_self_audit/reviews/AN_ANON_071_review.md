# Review of AN_ANON_071

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This evolutionary genomics study investigates the selective regime acting on the mammalian *INK4a/ARF* (*CDKN2A*) tumor suppressor locus—which encodes two structurally unrelated proteins, $\text{p16}^{\text{INK4a}}$ (RB pathway) and $\text{p14}^{\text{ARF}}/\text{p19}^{\text{ARF}}$ (p53/MDM2 pathway), via alternative $5'$ exons ($1\alpha$ and $1\beta$) spliced into a shared out-of-phase dual-coding exon 2 ($67\text{–}68$ codons)—and compares it against $8,467$ human–mouse orthologs, RB/p53 pathway members, and $90$ newly identified mammalian-conserved dual-coding exons mined from `altGraphX` splicing graphs and `UniGene` di-tags. Using codon-based maximum-likelihood models (`MG94xHKY85`) and phylogenetic relative-ratio tests across seven mammalian species, the authors show that (1) conservation of the intact $67\text{–}68$ codon ARF reading frame within exon 2 across seven mammals is unlikely to occur by chance under human codon usage ($P \approx 0.04$ by $10^6$-replicate permutation test); (2) *INK4a* and *ARF* evolve substantially faster at the nonsynonymous level than their interacting partners in the RB (*CDK4*, *CDK6*, *RB*) and p53 (*MDM2*, *p53*) pathways; and (3) across $90$ mammalian-conserved alternatively spliced dual-coding exons, the constitutive reading frame is under purifying selection ($d_{N,\text{const}} \ll d_{N,\text{alt}}$) whereas the alternative reading frame accumulates nonsynonymous substitutions at a rate ($\text{DC } d_{N,\text{alt}}$) indistinguishable from an untranslated out-of-phase background control in single-coding exons ($\text{SC } d_{N,\text{alt}}$). The $8,467$ human–mouse ortholog alignments are made publicly available via a direct URL alongside online supporting information.

The manuscript makes a valuable empirical contribution by demonstrating that asymmetric evolution—a constrained primary frame paired with a permissive alternative frame evolving near the neutral frame-shifted background rate—is a general feature of mammalian alternatively spliced dual-coding exons rather than an anomaly of *INK4a/ARF*. Furthermore, the $\text{SC } d_{N,\text{alt}}$ versus $\text{DC } d_{N,\text{alt}}$ comparison (Figure 5B) is a well-designed internal control. However, the statistical analysis of exon 2 in Table 1 suffers from a model misspecification: fitting a standard single-frame codon model (`MG94xHKY85`) independently to out-of-phase overlapping reading frames ignores frame coupling, where purifying selection on second-codon positions of `INK4a/2` ($d_N = 0.13$) directly suppresses third-codon (synonymous) substitutions in `ARF/2` ($d_S = 0.08$), generating an artifactual signature of positive selection ($\omega = 7.54, P < 0.01$). In addition, pairwise human–mouse $d_S$ estimates in Table 1 for the short `INK4a` exons suffer from saturation ($95\%$ confidence intervals extending to $\infty$), and the narrative conflates germline substitution rates with the high prevalence of somatic *INK4a/ARF* mutations in human cancers. These issues can be resolved through joint dual-coding model re-analysis across the 7-species tree and tempered framing of the cancer mutation claim.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Mammalian alternatively spliced dual-coding exons ($N=90$), including *INK4a/ARF*, evolve strongly asymmetrically, with a constrained constitutive frame and a rapidly evolving alternative frame whose $d_N$ matches the untranslated frame-shifted background rate: [Well Supported].**  
  The splicing-graph traversal and cross-species 40-nt di-tag conservation pipeline stringently identifies $90$ dual-coding regions conserved between human and at least one other mammal. Figure 5A,B convincingly demonstrates both the strong asymmetry ($d_{N,\text{const}} < d_{N,\text{alt}}$) and the tight linear correlation between $\text{DC } d_{N,\text{alt}}$ and the untranslated single-coding control $\text{SC } d_{N,\text{alt}}$ ($0.45$ vs. $0.48$ for *INK4a/ARF*).

* **Both *INK4a* and *ARF* evolve disproportionately faster at the amino acid level than their physical interaction partners in the RB (*CDK4*, *CDK6*, *RB*) and p53 (*MDM2*, *p53*) tumor suppressor pathways: [Well Supported].**  
  Using likelihood-ratio relative-ratio tests ($H_0, H_R, H_A$ with Bonferroni correction across branches of the 7-mammal phylogeny), the authors show that even the single-coding exon $1\beta$ of *ARF* accumulates nonsynonymous substitutions $5\times$ faster than *MDM2*, and *INK4a* exon 2 evolves $3.2\times$ faster than *CDK4* and $3\times$ faster than its paralog *INK4b* ($d_N = 0.12$ vs. $0.04$).

* **The preservation of an open $67\text{–}68$ codon alternative reading frame for *ARF* within exon 2 across seven mammalian species exceeds neutral expectation conditioned on the *INK4a* amino acid sequence: [Well Supported].**  
  The $10^6$-replicate synonymous codon permutation test (drawing codons from human genome-wide codon usage while holding the `INK4a` polypeptide fixed) shows that only $\sim 4\%$ of random synonymous encodings maintain an uninterrupted `ARF` reading frame across exon 2, supporting purifying selection against premature stop codons in `ARF/2`.

* **The exon 2 portion of *ARF* (`ARF/2`) is under diversifying/positive selection ($\omega = 7.54, P < 0.01$ in Table 1): [Methodologically Flawed].**  
  Applying a single-frame codon model (`MG94xHKY85`) to an out-of-phase overlapping reading frame violates the model's core assumption that synonymous sites evolve free of protein-coding constraint in another reading frame. Because `ARF/2` is shifted relative to `INK4a/2`, third-codon (synonymous) positions of `ARF/2` correspond to second-codon (strictly nonsynonymous) positions of `INK4a/2`. Strong purifying selection on `INK4a/2` ($d_N = 0.13$) depresses $d_S$ in `ARF/2` to $0.08$ (compared to $d_S = 0.51$ in the non-overlapping `ARF/1β`), while $d_N$ in `ARF/2` ($0.41$) is actually slightly lower than in single-coding `ARF/1β` ($0.46$, where $\omega = 0.86, P = 0.73$). Thus, $\omega = 7.54$ in `ARF/2` is an artifact of suppressed $d_S$ due to `INK4a/2` purifying selection, not diversifying selection on `ARF/2`.

* **The high frequency of *INK4a/ARF* mutations in human cancers is driven by a high intrinsic mutation rate and the evolutionary architecture of the locus: [Overstated].**  
  First, in the non-overlapping `ARF/1β` exon (105 codons), human–mouse synonymous divergence is $d_S = 0.51\ (0.34\text{–}0.81)$, which is entirely typical of average mammalian neutral divergence ($\sim 0.5$), whereas the elevated point estimates of $d_S$ in `INK4a/1α` ($1.14$) and `INK4a/2` ($1.15$) are estimated from short sequences (50 and 68 codons) with saturated confidence intervals extending to $\infty$ and without controlling for CpG dinucleotide hypermutability. Second, the high frequency of *INK4a/ARF* alterations in human tumors ($30\text{–}100\%$) primarily reflects strong somatic positive selection for inactivating both the RB and p53 checkpoints via a single locus deletion or point mutation, rather than an elevated germline substitution rate.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Fit an Explicit Joint Dual-Coding Codon Substitution Model to Exon 2
* **WHY:** Standard single-frame `MG94xHKY85` likelihood ratio tests (`ARF/2` $\omega = 7.54, P < 0.01$ in Table 1) are invalid on overlapping reading frames because synonymous substitutions in Frame 2 are nonsynonymous in Frame 1.
* **WHAT:** Replace or supplement the single-frame exon 2 estimates in Table 1 with a joint dual-coding Markov model (e.g., the Pedersen–Jensen 2001 or Hein–Støvlbæk 1995 model cited in refs. 21–22) that simultaneously parameterizes $\omega_{\text{INK4a}}$ and $\omega_{\text{ARF}}$ on the 68-codon overlap.
* **HOW:** Implement the 64-state (or stop-codon-excluded) transition rate matrix $Q_{uv}$ for the $206\text{-bp}$ overlap where a nucleotide substitution at position $k$ is weighted by $\omega_{\text{INK4a}}$ if it is nonsynonymous in frame 1 and by $\omega_{\text{ARF}}$ if it is nonsynonymous in frame 2, and test $\omega_{\text{ARF}} = 1$ via a 1-df likelihood ratio test in `[SOFTWARE_PACKAGE]`.

#### 2. Use the 7-Species Mammalian Phylogeny Instead of Pairwise Human–Mouse Comparisons to Avoid $d_S$ Saturation
* **WHY:** In Table 1, pairwise human–mouse maximum-likelihood estimates on 50-codon (`INK4a/1α`) and 68-codon (`INK4a/2`) partitions suffer from severe synonymous saturation, yielding $95\%$ profile-likelihood intervals of $d_S \in (0.5, \infty)$ and $(0.63, \infty)$.
* **WHAT:** Estimate tree-wide $d_N$, $d_S$, and $\omega$ across all seven aligned mammalian species (human, chimpanzee, macaque, mouse, rat, dog, cow) already assembled for the study (line 57), and control for CpG dinucleotide content when testing whether `INK4a` has an elevated neutral mutation rate.
* **HOW:** Fit the codon model jointly across the 7-taxon tree in `[SOFTWARE_PACKAGE]` (breaking the long human–mouse branch with primate and laurasiatherian outgroups to eliminate $\infty$ upper bounds), and repeat the $d_S$ comparison against the $8,467$ orthologs after masking CpG dinucleotides.

#### 3. Reframe the Discussion of Diversifying Selection and Somatic Cancer Mutation Rates
* **WHY:** Line 101 states that *"ARF is under diversifying selection ($d_N > d_S$)"*, which contradicts Figure 5B ($\text{DC } d_{N,\text{alt}} \approx \text{SC } d_{N,\text{alt}}$) and `ARF/1β` ($\omega = 0.86$), and lines 31 and 105 attribute somatic tumor mutation prevalence to a high intrinsic mutation rate.
* **WHAT:** Revise the Abstract and Discussion ("The INK4a/ARF Paradox") to state clearly that `ARF` evolves under relaxed purifying selection (near neutrality at the primary sequence level while preserving arginine-rich charge and reading-frame integrity), and distinguish somatic selective advantage (simultaneous disruption of RB and p53 pathways) from germline substitution rates.
* **HOW:** Edit lines 31, 64, 101, and 105 to note that the apparent $\omega > 1$ in `ARF/2` is a mathematical consequence of purifying selection on the overlapping `INK4a/2` frame suppressing synonymous sites in `ARF/2`.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several typographical and numerical inconsistencies appear in the text and section headers.
* **WHAT & HOW:**
  * **Line 101:** Change `"( P ≪ 0, Fisher's exact test)"` to the exact $P$-value threshold (e.g., `"( P < 10^{-4}, Fisher's exact test)"`), as a probability cannot be less than zero.
  * **Line 116:** Correct the section heading `"## RB and p51 Pathway Analysis."` to `"## RB and p53 Pathway Analysis."`
  * **Lines 70, 77, and 94:** Reconcile the human–mouse $d_N$ values for `INK4a/2` and `ARF/2` across the text and Table 1 (Table 1 reports `INK4a/2` $d_N = 0.13$ and `ARF/2` $d_N = 0.41$, whereas line 77 reports `dN = 0.12` for `INK4a/ARF` exon 2 and line 94 reports `dN_const = 0.12` and `dN_alt = 0.45`).
