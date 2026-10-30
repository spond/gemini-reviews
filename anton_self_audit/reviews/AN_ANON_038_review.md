# Review of AN_ANON_038

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.1 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the evolutionary conservation and mutational dynamics of the coronavirus programmed frameshift element (PFE), which directs $-1$ programmed ribosomal frameshifting from `ORF1a` to `ORF1b` across a slippery heptamer (`UUUAAAC`) and downstream RNA pseudoknot. The authors combine two comparative scales: (1) a macroevolutionary survey of $4,904$ `Coronaviridae` genomes filtered from $35,152$ NCBI entries ($\ge 14,945\text{ nt}$), classifying the `ORF1a`–`ORF1b` reading-frame overlap into five discrete length groups ($7, 16, 22, 25,$ and $31\text{ nt}$) and proposing a stepwise indel/substitution model for `ORF1a` stop-codon repositioning from an ancestral $7\text{-nt}$ ($\delta$-coronavirus) state to $31\text{ nt}$ ($\alpha$- and $\gamma$-coronavirus) and subsequently to $25, 22,$ and $16\text{ nt}$ ($\beta$-coronavirus subgenera); and (2) a microevolutionary analysis of SARS-CoV-2 PFE variation across $>1,550,000$ assembled GISAID consensus genomes and $>55,000$ raw intrahost sequencing datasets from COG-UK, supplemented by site-level Fixed Effects Likelihood (`FEL`) $dN/dS$ selection analysis on internal phylogeny branches.

The comparative survey of `Coronaviridae` overlap lengths ($7, 16, 22, 25, 31\text{ nt}$) and the integration of consensus (GISAID) and intrahost (COG-UK) SARS-CoV-2 polymorphism data provide a compact, biologically informative overview of PFE sequence constraint. However, the manuscript suffers from severe numerical and statistical inconsistencies in its SARS-CoV-2 selection analysis (Table 2 vs. Main Text) and several methodological gaps in its evolutionary reconstruction. Most critically, in the main text (line 66), the authors claim that `RdRp: 1` (`A13,443>C/G`) is subject to **purifying selection**, whereas Table 2 (line 72) reports $\alpha = 0, \beta = 0, \omega = 4.286$ ($p = 0.002$)—a mathematically impossible combination ($\beta/\alpha = 0/0 \ne 4.286$, where $\omega = 4.286 > 1$ would indicate positive rather than purifying selection). Furthermore, Table 2 contains a nucleotide coordinate typo (`13,352` instead of `13,532` for codon 31), Table 1 truncates coordinate `13,435` (or `13,436`) to `13,43`, and the application of standard single-reading-frame `FEL` ($\alpha, \beta$) across an overlapping dual-coding / RNA-secondary-structure region confounds synonymous rates in `ORF1b` with nonsynonymous changes in `ORF1a` and pseudoknot base-pairing constraints. These issues require re-checking the `FEL` output files and correcting the tables and text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Across $4,904$ `Coronaviridae` genomes, the `ORF1a`–`ORF1b` overlap falls into five discrete, clade-specific length classes ($7, 16, 22, 25,$ and $31\text{ nt}$): [Well Supported].**  
  Comprehensive curation of all complete and near-complete NCBI `Coronaviridae` records confirms strict taxonomic partitioning of the distance from the slippery heptamer `C` to the `ORF1a` stop codon across $\delta$- ($7\text{ nt}$), $\alpha$/$\gamma$- ($31\text{ nt}$), and $\beta$-coronavirus lineages ($25\text{ nt}$ in *Nobecovirus*, $22\text{ nt}$ in *Embecovirus*/*Merbecovirus*, and $16\text{ nt}$ in *Hibecovirus*/*Sarbecovirus*; Figures 1–3).

* **The `ORF1a`–`ORF1b` overlap evolved stepwise from an ancestral $7\text{-nt}$ state ($\delta$-CoV) to $31\text{ nt}$ ($\alpha$/$\gamma$-CoV) and then shortened to $25, 22,$ and $16\text{ nt}$ in $\beta$-CoV via three independent `"GTA"` insertions and a `"TCT"` deletion: [Moderately Supported].**  
  The comparative alignment in Figure 3 nicely highlights how in-frame stop codons (`TAA`/`TAG`) are created or abolished at positions `5–7`, `17–19`, `23–25`, `29–31`, and `38–40`. However, because $\alpha$-, $\beta$-, and $\gamma$-coronaviruses are treated as an unresolved trifurcation (Figure 1) and no formal ancestral state reconstruction (parsimony or maximum likelihood over an explicit tree) is performed, the directionality of the three separate `"GTA"` insertions vs. deletions (and why $\alpha$- and $\gamma$-coronaviruses share the $31\text{-nt}$ state while $\beta$-coronaviruses have $16, 22,$ and $25\text{ nt}$ despite $\alpha + \beta$ clustering in `RdRp`/`3CLpro`/`HEL` trees; line 13) remains a qualitative narrative rather than a statistically tested reconstruction.

* **The SARS-CoV-2 PFE region exhibits low population and intrahost diversity dominated by APOBEC/ADAR-compatible transitions and loop mutations: [Well Supported].**  
  Across $>1.55$ million GISAID sequences and $>55,000$ COG-UK raw read datasets (Table 1), only 33 variable positions pass filtering, with 30 of 36 substitution types matching `C>T`, `G>A`, `A>G`, or `T>C` transitions characteristic of host RNA editing or polymerase transition bias, and transversions largely restricted to unpaired loop bases.

* **Site-level `FEL` analysis identifies purifying selection at `RdRp` codons `1`, `31`, and `32` and pervasive positive selection at `RdRp: T26I` (`13,516`): [Methodologically Flawed].**  
  This conclusion is undermined by three technical problems in Table 2 and the accompanying text (lines 66–75):
  1. **Internal Contradiction and Mathematical Impossibility at Codon 1 (`13,443`):** The main text (line 66) states that `RdRp: 1 (A13,443>C/G)` is subject to **purifying selection**, and Table 1 (line 42) marks `13,443` with a downward arrow `↓`. Yet Table 2 (line 72) reports $\alpha = 0, \beta = 0, \omega = 4.286, p = 0.002$. First, if $\alpha = 0$ and $\beta = 0$, the ratio $\omega = \beta/\alpha$ is $0/0$ (undefined), not $4.286$, and an LRT with zero substitutions cannot yield $p = 0.002$. Second, $\omega = 4.286 > 1$ corresponds to positive selection, directly contradicting both the text ("purifying selection") and the `↓` symbol in Table 1.
  2. **Direction of Nucleotide Change at `13,516` (`RdRp: T26I`):** Line 66 writes `RdRp: T26I (13,516 T>C)`, whereas Table 1 (line 61) shows that the reference base at `13,516` is `C` and the alternate allele is `T` (`C>T`, which changes `ACA`/`ACT`/`ACC`/`ACG` Thr to `ATA`/`ATT`/`ATC` Ile in the $+1/-1$ shifted frame). Thus `13,516 T>C` in the text is inverted relative to the reference genome (`C>T`).
  3. **Confounding of Single-Frame $dN/dS$ (`FEL`) with Overlapping Reading Frames (`ORF1a`/`ORF1b`) and RNA Secondary Structure:** `RdRp` codon 1 (`13,443`) lies directly inside the dual-coding `ORF1a`/`ORF1b` overlap (`13,441–13,468` in `NC_045512.2`), and codons 1–32 all reside within the structured PFE pseudoknot. Standard `FEL` assumes that synonymous substitutions ($\alpha$) are selectively neutral and reflect the baseline mutation rate; in a dual-coding overlap and critical RNA pseudoknot, "synonymous" third-position changes in `ORF1b` alter amino acids in `ORF1a` and disrupt Watson–Crick stem pairing in the frameshift pseudoknot, suppressing $\alpha$ to $0$ (as seen at Codon 26 where $\alpha = 0, \beta = 4.722, \omega = \infty$) and creating spurious positive selection calls when a single `C>T` APOBEC/deamination hotspot occurs at a nonsynonymous position (`13,516 C>T`).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Correct the `FEL` Parameter Estimates in Table 2
* **WHY:** Reporting $\alpha = 0, \beta = 0, \omega = 4.286, p = 0.002$ for Codon 1 (`13,443`) in Table 2 while calling it "purifying selection" in the text is a clear transcription or parsing error from the raw JSON output file.
* **WHAT:** Re-inspect the raw `FEL` JSON output for `nsp12`/`RdRp` codon 1 (`13,443`) and replace the erroneous $\alpha, \beta, \omega$ entries in Table 2.
* **HOW:** Check whether $\alpha = 4.286, \beta = 0, \omega = 0$ were shifted by one column to the right in Table 2 row 1 (which would explain why $\alpha = 4.286 > \beta = 0$ yielded $p = 0.002$ for purifying selection!). Correct the column alignment for row 1 of Table 2 accordingly.

#### 2. Account for Dual-Coding (`ORF1a`/`ORF1b`) and RNA Structure Constraints When Interpreting `FEL` $\omega$ Estimates
* **WHY:** Applying a standard single-ORF codon model (`FEL`) to the `ORF1a`/`ORF1b` overlap and PFE pseudoknot violates the neutrality assumption of synonymous substitutions ($\alpha$), because third-codon-position changes in `ORF1b` are first/second-codon-position nonsynonymous changes in `ORF1a` and stem-loop base-pairing mutations in the RNA pseudoknot.
* **WHAT:** Add an explicit caveat in the Results/Discussion noting how RNA secondary structure and dual coding affect $\alpha$ and $\beta$, particularly for `RdRp: T26I` (`13,516 C>T`) where $\alpha = 0$.
* **HOW:** Clarify whether `13,516 C>T` sits in an unpaired loop or stem region of the pseudoknot and note that because recurrent `C>T` transitions are driven by host APOBEC/deamination mutational bias in SARS-CoV-2 while synonymous transitions at that codon may be purged by RNA secondary structure pairing, $\beta > \alpha = 0$ at site `13,516` can reflect mutational hotspot bias + structural constraint on synonymous sites rather than adaptive protein-level selection on `RdRp`.

#### 3. Fix Coordinate Typos and Missing Footnote Definitions in Tables 1 and 2
* **WHY:** Coordinate typos and undefined column headers/footnotes impede verification of the SARS-CoV-2 variant calls.
* **WHAT & HOW:**
  1. **Table 1 Row 7 (Line 39):** The genomic coordinate is truncated to `13,43 a` (missing the last digit between `13,434` and `13,437`, i.e., `13,435` or `13,436`). Restore the full 5-digit coordinate.
  2. **Table 1 Header & Footnotes:** Define the column headers `H` and `B` (presumably Huston et al. and Bhatt et al. secondary structure annotations, `S` = Stem, `L` = Loop) and include the text for footnotes `a`, `b`, `c`, `d`, `↑`, and `↓` directly below Table 1.
  3. **Table 2 Row 2 (Line 73):** Codon 31 has nucleotide coordinate `13,352` (a digit transposition of `13,532`, as correctly written in Table 1 line 64 and main text line 66). Change `13,352` to `13,532`.
  4. **Main Text Line 66 (`13,516 T>C`):** Change `13,516 T>C` to `13,516 C>T` to match the `NC_045512.2` reference nucleotide (`C`) and the `T26I` (`ACA -> ATA`) amino acid substitution.
