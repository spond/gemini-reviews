# Review of AN_ANON_074

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This web server application note presents `ETOPE`, a Perl/Apache comparative genomics tool designed to validate *ab initio* computationally predicted exons and gene models (such as `Genscan` predictions) that lack supporting EST or experimental expression evidence. Given either a single coding nucleotide sequence (with user-specified reading-frame offset $0, 1, \text{or } 2$) or raw `Genscan` output, `ETOPE` searches a user-selected database of coding, `Genscan`, `UniGene`, or `FANTOM2` sequences from a suitably diverged species ($10\text{–}30\%$ coding nucleotide divergence; 9 databases totaling $499,732$ sequences summarized in Table 1) using discontiguous `MEGABLAST`. The program selects the highest-scoring alignment devoid of internal stop codons, translates both sequences, globally realigns the amino acid sequences using `ClustalW 1.8` to enforce codon-to-codon nucleotide alignment, estimates nonsynonymous ($K_A$) and synonymous ($K_S$) substitution rates via the approximate method of Yang and Nielsen (`PAML`), and tests $K_A/K_S < 1$ ($P < 0.05$) using a $2\times 2$ Fisher's exact test on changed versus unchanged synonymous and nonsynonymous sites. The authors demonstrate the utility of `ETOPE` on a $150\text{-kb}$ rat chromosome 1 candidate interval (`chr1:38,050,000–38,200,000`) containing $15$ unsupported gene predictions, confirming $8$ predictions via human homology ($K_A/K_S = 0.1487, P < 0.0005$ for `chr1_8.30`).

`ETOPE` provides a practical, accessible web workflow for filtering false-positive *ab initio* gene predictions in newly sequenced mammalian genomes (such as rat, dog, cow, and pig) where species-specific EST coverage is sparse or biased toward highly expressed transcripts. While the overall comparative genomics rationale is sound and builds on established simulation benchmarks ([AUTHOR_HANDLE] et al.; Guigó et al.), several technical and mathematical details in the pipeline specification require correction or clarification: (1) the discontiguous `MEGABLAST` command-line parameters on line 36 (`-W 16 -t 11`) transpose the word weight (`-W`) and template length (`-t`); (2) the description of the $2\times 2$ Fisher's exact test on line 40 conflates multiple-hit-corrected substitution rates ($K_S, K_A$) from `yn00` with bounded integer site counts ($S_S \le L_S$) required for a contingency table; (3) statistical power limits on short individual exons ($<100\text{ bp}$) and multiple-testing adjustments across multi-exon `Genscan` outputs are not discussed; and (4) line 82 misstates the $150\text{-kb}$ rat interval as `"150 000 kb"`.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Testing $K_A/K_S < 1$ between homologous reading frames at $10\text{–}30\%$ sequence divergence validates genuine protein-coding predictions independently of species-specific EST coverage: [Well Supported].**  
  By conditioning on evolutionary purifying selection ($K_A < K_S$) rather than sequence similarity alone, `ETOPE` distinguishes conserved protein-coding exons from conserved non-coding elements or spurious pattern-recognition matches, as illustrated by the rat `Genscan` prediction `chr1_8.30` matched against human `UniGene` `ug_hs_158` ($K_A/K_S = 0.1487, P < 0.0005$).

* **The `ETOPE` web interface streamlines exon-by-exon validation of `Genscan` outputs by highlighting suboptimal exons ($P < 75\%$) for targeted $K_A/K_S$ testing across nine curated mammalian databases: [Well Supported].**  
  Table 1 documents exact builds and sequence counts across `Ensembl` (`10.30` human, `10.3` mouse), `UniGene` (`158` human, `119` mouse), and `RIKEN FANTOM2` cDNAs, and the `Genscan` parser directly extracts and frames individual predicted exons for one-click analysis.

* **Constructing a $2\times 2$ Fisher's exact contingency table directly from Yang–Nielsen (`yn00`) $L_S, L_N$ and $S_S = K_S L_S, S_N = K_A L_N$ outputs provides an exact test of $K_A/K_S < 1$ (line 40): [Fragile].**  
  In the Yang–Nielsen (2000) approximate method (`yn00`), $L_S$ and $L_N$ are fractional expected site counts weighted by transition/transversion and codon frequencies, and $K_S$ and $K_A$ are Markov-model-corrected substitution distances per site rather than binomial proportions ($K_S = S_S / L_S$ only holds for uncorrected counts or when $S_S$ is defined as the expected substitution count, which is non-integer and can exceed $L_S$ when $K_S > 1$). Entering rounded continuous estimates into a $2\times 2$ Fisher's exact table of "changed" ($S_S$) and "unchanged" ($L_S - S_S$) sites is an approximation to the normal/likelihood-ratio $Z$-test ($Z = (K_S - K_A)/\sqrt{\text{Var}(K_S) + \text{Var}(K_A)}$) and lacks power on very short exons ($<30$ codons).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Clarify the Contingency Table Rounding and Supplement Fisher's Exact Test with the Yang–Nielsen Standard-Error Test
* **WHY:** Line 40 writes $K_S = S_S / L_S$ and $K_A = S_N / L_N$ and forms a $2\times 2$ Fisher's exact table of changed ($S_S, S_N$) versus unchanged ($L_S - S_S, L_N - S_N$) sites. Because `PAML` `yn00` outputs fractional $L_S, L_N$ and multiple-hit-corrected $K_S, K_A$ (along with their analytical standard errors $\text{SE}(K_S), \text{SE}(K_A)$), readers need to know whether `ETOPE` uses the raw uncorrected fractional differences or `K_S * L_S` rounded to the nearest integer, and how cases with $K_S \ge 1.0$ are handled.
* **WHAT:** Explicitly state how $L_S, L_N, S_S, S_N$ are extracted and rounded from `yn00`, and report the minimum exon length required to achieve $\ge 80\%$ power at $10\text{–}30\%$ divergence.
* **HOW:** Update line 40 to specify whether $S_S$ and $S_N$ are the pre-correction fractional counts from `yn00` (rounded to integers) or `K_S * L_S`, and add a note warning users that single exons shorter than $\sim 90\text{–}120\text{ bp}$ may fail to reach $P < 0.05$ due to small synonymous site counts ($L_S < 25$).

#### 2. Correct the Discontiguous `MEGABLAST` Parameter Specification on Line 36
* **WHY:** Line 36 states that `MEGABLAST` is executed with `-W 16 -t 11 -q -2`. In NCBI `megablast`, `-W` specifies the word size (number of matched bases, typically $11$ or $12$ for discontiguous words) and `-t` specifies the discontiguous template length ($16, 18, \text{or } 21$, which must be strictly greater than `-W`). Writing `-W 16 -t 11` transposes the two flags.
* **WHAT & HOW:** Correct line 36 to `-W 11 -t 16 -q -2` (weight $11$, template length $16$).

#### 3. Provide Downloadable Perl Source Code for Local Installation
* **WHY:** Line 34 notes that `ETOPE` is implemented in Perl on top of `NCBI BLAST`, `ClustalW 1.8`, and a modified `PAML` package, and that hardware limitations currently restrict the public server (Pentium III 450 MHz, 771 MB RAM) to single-best hits and transcript/prediction databases. Making the Perl CGI/command-line scripts downloadable would allow users to run batch genome-wide analyses locally.
* **WHAT & HOW:** Package the `ETOPE` Perl modules and the `PAML` patch into a downloadable `.tar.gz` archive on the `ETOPE` web page and cite the download link in the `"THE ETOPE PROGRAM"` section.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** A unit conversion error and a spelling error appear in the text.
* **WHAT & HOW:**
  * **Line 82:** Change `"identified a 150 000 kb candidate locus on rat chromosome 1 between positions 38 050 000 and 38 200 000"` to `"identified a 150 kb (150 000 bp) candidate locus..."` ($38,200,000 - 38,050,000 = 150,000\text{ bp} = 150\text{ kb}$, not $150,000\text{ kb}$).
  * **Line 29:** Correct `"Yang and Neilsen ( 5 )"` to `"Yang and Nielsen ( 5 )"` to match line 40.
