# Review of AN_ANON_071

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript examines the molecular evolutionary dynamics of the mammalian `INK4a/ARF` (`CDKN2A`) tumor suppressor locus, which encodes two functionally distinct proteins (`p16INK4a` and `p14ARF`/`p19ARF`) via alternative splicing of upstream exons (`1α` and `1β`) into a shared, out-of-phase dual-coding exon (`exon 2`, 206 bp overlap). Analyzing orthologous coding alignments across seven mammals (human, chimpanzee, macaque, mouse, rat, dog, and cow), comparing human–mouse divergence against 8,467 orthologous gene pairs using `MG94×HKY85` codon models, and performing relative ratio tests across the RB (`INK4a`, `CDK4`, `CDK6`, `RB`) and p53 (`ARF`, `MDM2`, `p53`) pathways, the authors show that `INK4a/ARF` evolves faster than background mammalian genes and its pathway partners, and evolves asymmetrically between the two reading frames. They then mine human (`altGraphX`) and mouse (`UniGene` 40-nt di-tags) transcriptome splicing graphs to identify 90 conserved mammalian dual-coding exons, demonstrating that asymmetric evolution (a conserved constitutive frame paired with a rapidly changing alternative frame evolving near the non-coding background rate) is a general property of dual-coding exons. The 8,467 human–mouse ortholog alignments are provided via a public URL.

The comparative discovery of 90 conserved mammalian dual-coding exons and the empirical demonstration in Figure 5B that alternative reading frames in dual-coding exons evolve at virtually the same nonsynonymous rate as untranslated out-of-frame control segments ($\text{DC } d_{N,\text{alt}} = 0.45$ vs. $\text{SC } d_{N,\text{alt}} = 0.48$ for `INK4a/ARF`) are valuable contributions. However, the evolutionary analysis of the overlapping `exon 2` region suffers from a fundamental model misspecification: fitting a standard single-frame codon model (`MG94×HKY85`) independently to each frame of an overlapping coding region treats purifying selection on `INK4a` third codon positions as positive diversifying selection on `ARF` ($\omega = 7.54, P < 0.01$ in Table 1), leading the authors to invert the causal relationship between the two reading frames in the Discussion.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Conservation of the 67–68 codon overlap length in exon 2 across seven mammals is not a passive byproduct of `INK4a` amino acid composition and human codon usage bias ($P \approx 0.04$ by permutation): [Well Supported].**  
  Simulating 1,000,000 synonymous nucleotide sequences preserving the exact `INK4a` exon 2 polypeptide under empirical human codon usage shows that ~96% of random synonymous encodings introduce premature stop codons into the `ARF` reading frame (line 60). Together with cross-mammalian splicing conservation, this provides solid statistical support that purifying selection maintains an open reading frame in `ARF` across exon 2.

* **Across 90 conserved mammalian dual-coding exons as well as `INK4a/ARF`, the constitutive reading frame is under purifying selection while the alternative frame accumulates nonsynonymous substitutions at a rate indistinguishable from untranslated out-of-frame sequence: [Well Supported].**  
  Figure 5A and 5B provide an elegant internal control: comparing $d_N$ in the alternative frame of the dual-coding region ($\text{DC } d_{N,\text{alt}}$) against $d_N$ in the corresponding out-of-frame shift of the single-coding region of the very same gene ($\text{SC } d_{N,\text{alt}}$, which is never translated in vivo) reveals a strong linear correlation across the 90 genes and near-identity in `INK4a/ARF` (`0.45` vs. `0.48`). This demonstrates that the elevated $d_N$ in `ARF` exon 2 matches the expected rate of frame-shifted sequence constrained primarily by the `INK4a` reading frame.

* **`ARF` exon 2 is evolving under positive diversifying selection ($\omega = d_N/d_S = 7.54$, $P < 0.01$ in Table 1), and `INK4a`'s high synonymous substitution rate ($d_S = 1.15$) is a byproduct of codependency with a rapidly adapting `ARF`: [Methodologically Flawed].**  
  In Table 1, the authors apply a standard single-reading-frame `MG94×HKY85` model independently to `INK4a/2` ($d_S = 1.15, d_N = 0.13, \omega = 0.09$) and `ARF/2` ($d_S = 0.08, d_N = 0.41, \omega = 7.54$), and write in line 101 that `"INK4a is under purifying selection (dN < dS) and ARF is under diversifying selection (dN > dS), whereas an unusually high dS within INK4a is likely a byproduct of its codependency with the rapidly changing ARF."` Because the two frames are shifted out of phase in exon 2, synonymous third-codon positions in `ARF/2` correspond to nonsynonymous first/second-codon positions in `INK4a/2`. Strong purifying selection on the `INK4a` protein ($d_N = 0.13$) therefore directly suppresses synonymous changes in `ARF/2` ($d_S = 0.08$), artificially inflating the single-frame ratio $\omega(\text{ARF/2}) = 0.41 / 0.08 = 7.54$. Conversely, in the non-overlapping exon `ARF/1β`, $d_S = 0.51$ and $d_N = 0.46$ ($\omega = 0.86, P = 0.73$), and in `INK4a` the non-overlapping exon `1α` has the exact same elevated synonymous rate ($d_S = 1.14$) as the overlapping exon `2` ($d_S = 1.15$). Thus, `INK4a`'s high $d_S$ (1.14–1.15) is a locus-wide neutral mutation rate property (present equally in single-coding exon `1α`), which feeds into `ARF/2` as nonsynonymous changes ($d_N = 0.41$), while purifying selection on `INK4a/2` depresses $d_S(\text{ARF/2})$ to 0.08. Single-frame $\omega > 1$ in `ARF/2` is an artifact of ignoring reading-frame overlap in the likelihood model, not diversifying selection on `ARF`.

* **`INK4a` and `ARF` accumulate nonsynonymous substitutions significantly faster than their interacting partners in the RB (`CDK4`, `CDK6`, `RB`) and p53 (`MDM2`, `p53`) pathways: [Well Supported].**  
  The multi-species relative ratio likelihood tests (lines 82–84 and 118; Figure 4) across the seven-mammal phylogenies properly account for branch lengths and multiple testing (Bonferroni correction), showing that even the non-overlapping `ARF/1β` exon accumulates nonsynonymous changes ~5-fold faster than `MDM2` and that `INK4a` exon 2 evolves 3.2-fold faster than `CDK4`.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Fit an Explicit Dual-Coding Codon Substitution Model to Exon 2
* **WHY:** Applying a single-reading-frame `MG94×HKY85` model (`Table 1`) to an overlapping reading frame violates the fundamental independence assumption between synonymous and nonsynonymous sites, generating a spurious $\omega = 7.54$ ($P < 0.01$) call in `ARF/2` simply because purifying selection on `INK4a/2` suppresses third-position substitutions in `ARF/2`.
* **WHAT:** Replace or supplement the single-frame Table 1 estimates for exon 2 with a joint dual-coding codon model (e.g., Hein & Støvlbæk 1995; Pedersen & Jensen 2001, cited as refs. 21–22) that simultaneously parameterizes selection on both reading frames ($\omega_{\text{INK4a}}, \omega_{\text{ARF}}$) conditioned on the phase offset.
* **HOW:** Implement the joint transition rate matrix $Q_{ij}$ for the 68 overlapping codons in exon 2 where a nucleotide substitution from state $i$ to $j$ is weighted by $\omega_{\text{INK4a}}$ if nonsynonymous in frame 1, $\omega_{\text{ARF}}$ if nonsynonymous in frame 2, and $\omega_{\text{INK4a}}\omega_{\text{ARF}}$ if nonsynonymous in both. Test the null hypothesis $\omega_{\text{ARF}} = 1$ via a 1-df likelihood ratio test; based on Figure 5B ($\text{DC } d_{N,\text{alt}} = 0.45 \approx \text{SC } d_{N,\text{alt}} = 0.48$) and `ARF/1β` ($\omega = 0.86$), $\omega_{\text{ARF}}$ in exon 2 will be close to $0.4$–$0.9$ rather than $7.54$.

#### 2. Correct the Causal Interpretation of $d_S(\text{INK4a})$ vs. $d_N(\text{ARF})$ in the Discussion
* **WHY:** Line 101 argues that `"an unusually high dS within INK4a is likely a byproduct of its codependency with the rapidly changing ARF"`, overlooking Table 1's own finding that non-overlapping exon `INK4a/1α` has the exact same $d_S$ (`1.14`) as overlapping exon `INK4a/2` (`1.15`).
* **WHAT:** Revise the "INK4a/ARF Paradox" section (line 101) to reflect that high $d_S$ (`1.14–1.15`) is an intrinsic mutational property of the `INK4a` exons (both `1α` and `2`), and that neutral synonymous substitutions in `INK4a/2` drive nonsynonymous substitutions in the permissive `ARF/2` frame rather than vice versa.
* **HOW:** Explicitly compare $d_S(\text{INK4a/1α}) = 1.14$ with $d_S(\text{INK4a/2}) = 1.15$ in the text to show that overlapping with `ARF` does not inflate `INK4a`'s synonymous rate relative to single-coding exon `1α`.

#### 3. Use Multi-Species Tree Lengths Instead of Saturated Pairwise Human–Mouse $d_S$ Estimates
* **WHY:** In Table 1, pairwise human–mouse $d_S$ estimates for `INK4a/1α` (50 codons, $d_S = 1.14$) and `INK4a/2` (68 codons, $d_S = 1.15$) have upper 95% profile likelihood bounds of $\infty$, indicating synonymous saturation in short two-sequence alignments.
* **WHAT:** Estimate $d_S$, $d_N$, and $\omega$ across the full 7-mammal phylogeny (already assembled in line 57) rather than relying solely on the saturated pairwise human–mouse comparison in Table 1.
* **HOW:** Fit the `MG94×HKY85` model across the 7-species tree in `HyPhy` to break up the long human–rodent branch, yielding finite, well-bounded 95% confidence intervals for $d_S$ in exons `1α` and `2`.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Mathematical impossibilities and heading typos detract from the rigor of the manuscript.
* **WHAT & HOW:**  
  1. **Line 101 ($P \ll 0$ typo):** Correct `"significantly ( P ≪ 0, Fisher's exact test)"` to report the actual non-negative $P$-value (e.g., $P < 10^{-4}$, since a probability cannot be less than zero).  
  2. **Line 116 (Section heading typo):** Correct `"## RB and p51 Pathway Analysis."` to `"## RB and p53 Pathway Analysis."`  
  3. **Line 113 (One-sided vs. two-sided LRT notation):** In Materials and Methods, the text states that the null $d_{S1} = d_{S2}$ was tested against the one-sided alternative $d_{S1} \ge d_{S2}$ using $\frac{1}{2}\chi_0^2 + \frac{1}{2}\chi_1^2$, which is appropriate when $d_{S1}$ is the fixed focal exon rate and $d_{S2}$ is constrained to $\le d_{S1}$; explicitly clarify which gene is indexed as 1 (`INK4a/ARF`) and 2 (each of the 8,467 background orthologs).
