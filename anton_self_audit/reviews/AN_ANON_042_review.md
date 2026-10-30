# Review of AN_ANON_042

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.2 / 10.0** (Exemplary) | **Scientific Core Score:** **7.4 / 8.0**  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This resource and comparative genomics manuscript presents the 28-way vertebrate whole-genome multiple sequence alignment (`multiz28way` on human NCBI Build 36 / hg18) and associated `phastCons` conservation tracks for the UCSC Genome Browser, expanding the previous 17-way alignment with 11 additional species and 6 updated assemblies (spanning 2 finished genomes, 16 high-depth 5.1$\times$–8.5$\times$ shotgun assemblies, and 10 ~2$\times$ mammalian assemblies). Pairwise `BLASTZ` alignments are linked via `axtChain` and `axtNet` (using syntenic filtering for high-coverage mammals and reciprocal-best filtering for 2$\times$ mammals), progressively aligned with `MULTIZ` along a 28-species phylogeny with `phyloFit` REV branch lengths estimated from GENCODE fourfold degenerate (4D) sites, and indexed with LZO chunk compression in `bx-python` for rapid regional queries. The authors demonstrate the utility of the alignment across three biological investigations: (1) polarizing 209 coding indels along the human placental lineage, examining 11 human-specific coding indels (highlighting *SULF1* and *GFM2*), and testing conservation at *PAH* in-frame deletion sites; (2) dissecting why human start codons align less frequently than stop codons across 11,729 reviewed RefSeq genes; and (3) quantifying the decay of alignability with phylogenetic distance across 251,000 RefSeq coding exons, 481 ultraconserved elements (UCEs), ~92,269 predicted regulatory regions (PRPs), and 3,900 ENCODE ChIP-chip putative transcriptional regulatory regions (pTRRs).

The manuscript is an exemplary genomic resource paper characterized by careful algorithmic engineering—most notably its distinction between syntenic and reciprocal-best net filtering by assembly depth and its gap-annotation-aware alignability metric (`maf_interval_alignability.py`), which excludes unsequenced draft gaps from non-aligned denominators—and by unusually candid, self-critical reporting of negative and caveated results. The main analytical points that could be further strengthened are: (1) testing whether the apparent 2-fold slowdown in coding indel accumulation along the human lineage persists when normalized against neutral 4D substitution branch lengths rather than point-estimate fossil divergence times, (2) explicitly controlling for the ascertainment circularity of PRPs when comparing their eutherian alignability decay to biochemically identified ENCODE pTRRs, and (3) documenting the coordinate conversion of hg17-derived PRPs to hg18 and reconciling the PRP count between Results and Methods.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Construction, indexing, and gap-aware alignability scoring of the 28-way vertebrate alignment (`BLASTZ`/`axtChain`/`axtNet`/`MULTIZ`/`phastCons` and `bx-python` LZO indexing): [Well Supported].**  
  The alignment pipeline appropriately adapts filtering stringency to assembly quality (synteny filtering for high-coverage assemblies vs. reciprocal-best for 2$\times$ shotgun assemblies to suppress paralog/pseudogene misalignment), and `maf_interval_alignability.py` uses `axtNet`/`MULTIZ` gap annotations to distinguish true sequence non-alignment (contiguous sequence in the target species lacking local alignment) from missing draft sequence (excluded from the denominator, with all 10 low-coverage 2$\times$ species omitted from the exponential decay fits in Figure 7C).

* **Higher evolutionary drift / lower alignability of human start codons relative to stop codons driven by draft-genome CpG island bias and short initial coding exons (Application 2, Tables 1 and 3): [Well Supported].**  
  The observation that mouse (the only finished comparison genome) shows no deficit in start-codon alignability (97.7% starts vs. 96.8% stops), whereas all 26 draft assemblies show lower start than stop alignability, motivated three direct stratified tests in Table 3. The data cleanly show that within placental mammals, removing genes overlapping CpG islands eliminates the start/stop alignability gap ($P = 0.16$), while at deeper vertebrate distances, restricting to initial coding exons $\ge 100$ bp substantially narrows the gap ($P < 10^{-3}$).

* **Differential modes and rates of alignability decay across coding exons, UCEs, PRPs, and biochemical ENCODE pTRRs (Application 3, Figure 7): [Well Supported].**  
  Plotting mean alignability against 4D substitution distance demonstrates distinct constraint regimes: coding exons remain >80% alignable through eutherians and decay slowly thereafter; UCEs remain nearly fully aligned through amniotes before decaying quadratically; and noncoding regulatory elements decay exponentially like neutral background DNA but with a rightward lag. Including biochemically defined ENCODE ChIP-chip pTRRs and 13,000 CTCF binding sites provides an essential sequence-independent benchmark showing ~70% conservation within eutherians and rapid turnover (~30% alignability) outside eutherians.

* **Non-uniform chronological rate of coding indel fixation along the human placental lineage (~4 indels/Myr in early placental evolution vs. <2 indels/Myr recently, $P < 10^{-3}$; Application 1, Figure 3): [Moderately Supported].**  
  While the parametric bootstrap test rejects a constant rate per million years across the 209 unambiguously assigned coding indels, two confounding factors are not ruled out: (1) branch durations in millions of years rely on point estimates from molecular/fossil calibrations of the early placental radiation, which carry large credible intervals, and neutral substitution rates themselves slowed along the hominoid lineage ("hominoid slowdown"); and (2) requiring unambiguous parsimony assignment across 16 placental comparison genomes (10 of which are 2$\times$ draft assemblies) creates differential branch-ascertainment sensitivity depending on node topology and terminal polymorphism (e.g., 1 of the 11 terminal human indels, *GFM2*, is polymorphic within humans).

* **Exploratory vignettes on human-specific indels (*SULF1*, *GFM2*) and *PAH* disease-associated in-frame deletions (Application 1, Table 2, Figures 4–6): [Well Supported].**  
  The authors carefully refrain from overclaiming phenotypic causality, explicitly noting that *GFM2* is polymorphic in humans and structurally benign in homology models, and transparently reporting that the *PAH* deletion conservation permutation test was non-significant ($P \approx 0.69$) due to small sample size and a single deletion at a site variable across non-mammalian vertebrates.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Normalize Branch-Specific Coding Indel Counts by Neutral 4D Substitutions per Site
* **WHY:** Testing coding indel uniformity solely against fossil-calibrated millions of years (Figure 3) conflates changes in the ratio of indels to nucleotide substitutions with overall generation-time/molecular-clock slowdowns (such as the hominoid slowdown) and fossil calibration uncertainty in early Eutheria.
* **WHAT:** Test whether the 209 coding indels accumulate uniformly relative to neutral 4D substitution branch lengths estimated by `phyloFit`.
* **HOW:** Using the `phyloFit` REV 4D branch lengths already computed for the 28-way tree (Figure 1 / Supplemental material), run the same parametric bootstrap test comparing observed coding indels per branch against expectations proportional to 4D substitutions per site along the human lineage, and report both the chronological (indels/Myr) and molecular (indels/4D substitution) tests.

#### 2. Quantify Ascertainment Circularity in PRPs Relative to Biochemical ENCODE pTRRs
* **WHY:** PRPs were constructed by intersecting PReMods with intervals having 7-way mammalian Regulatory Potential $\ge 0.05$ across human, chimpanzee, macaque, mouse, rat, dog, and cow. Because alignment across those 7 eutherians was required to define PRPs, their near-100% alignability across eutherians in Figure 7B–C is partly guaranteed by ascertainment.
* **WHAT:** Explicitly separate the alignability evaluation of PRPs into training clades (the 7 eutherian species used in RP/PReMod definition) and out-of-sample clades (additional eutherians, marsupials, monotremes, birds, amphibians, and fish).
* **HOW:** In the text and Figure 7 legend, annotate which comparison species were included in the 7-way RP training alignment and emphasize that out-of-sample clades (e.g., horse, elephant, tenrec, opossum, platypus, chicken) and alignment-independent ChIP-chip tracks (pTRRs and CTCF) provide the non-circular estimates of regulatory turnover.

#### 3. Document the Coordinate Conversion of PRPs from hg17 to hg18 and Reconcile Total Counts
* **WHY:** The Methods section states that the 118,402 PReMods and the 7-way RP scores were computed on human assembly `hg17`, yielding `92,269 PRPs`, whereas the 28-way alignment is on `hg18` and Results (Application 3) states that `94,000 predicted regulatory regions, which we call PRPs`, were examined.
* **WHAT & HOW:** Specify in the Methods section how the hg17 PRP coordinates were mapped to hg18 (e.g., `liftOver` parameters and how many intervals were split or lost during conversion), and reconcile the `92,269` figure in Methods with the `94,000` figure in Results.
