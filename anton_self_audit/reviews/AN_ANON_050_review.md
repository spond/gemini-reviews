# Review of AN_ANON_050

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript characterizes a human SARS-CoV-2 superinfection sampled in New York City in January [YEAR] (`NYCPHL-002461`), linked via contact tracing and shared travel history to Ghana with an Alpha (B.1.1.7) index case (`NYCPHL-002130`). Across four independent RNA extractions from two specimen aliquots sequenced with the ARTIC V3 amplicon protocol, the authors show that the contact partner harbored a major Alpha lineage (~74% median allele frequency) identical to the index case and contemporary Ghanaian sequences, alongside a minor Epsilon (B.1.429) lineage (~12–21% allele frequency) absent from the laboratory's prior sequencing runs. Using four-gamete tests (PHI, MCL, and $R^2$ vs. Distance) on 15 short-read windows in the S and N genes, together with RT-PCR, TOPO TA cloning, and Sanger sequencing of three longer amplicons (947 nt in S, $n=104$ clones; 657 nt in S, $n=93$; 476 nt in ORF8, $n=36$), the authors report multiple recombinant haplotypes (up to 29.8% of clones in the 947 nt S fragment) and screen 27,806 NYC surveillance genomes with 3SEQ to confirm no onward transmission of an Alpha/Epsilon recombinant. Variant calls and visualizations are shared via GISAID and an interactive ObservableHQ notebook.

The evidence for genuine in vivo co-infection with Alpha and Epsilon variants is thorough, combining epidemiological contact tracing, TaqPath RT-PCR cycle threshold (Ct) shifts, four independent re-extractions across two aliquots, and molecular-clock phylogenetic placement. However, the manuscript's secondary conclusion—that the observed recombinant haplotypes predominantly reflect in vivo viral recombination rather than in vitro reverse-transcription (RT) or PCR template switching—rests on a flawed statistical premise and lacks an essential experimental control: artificial mixing of pure Alpha and Epsilon RNA templates. Because the clinical specimen had a very high viral load (ORF1ab/N Ct 14.86–16.25, corresponding to $>10^6$ templates) and the cloning PCR used 35 cycles with only a 15-second extension step for amplicons up to 947 bp, bulk template switching during RT and PCR will deterministically generate consistent percentages of chimeric molecules across technical replicates. While the absence of an experimental mixed-RNA control requires tempering the in vivo recombination claims, the superinfection characterization and surveillance screen are solid.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Individual `NYCPHL-002461` was contemporaneously superinfected with SARS-CoV-2 Alpha (B.1.1.7, ~75%) and Epsilon (B.1.429, ~15–20%) variants: [Well Supported].**  
  The presence of both variants is replicated across four independent extractions from two separate specimen aliquots (A/B and C/D), matches the partial S-gene Ct delay of 2–3 cycles in the TaqPath assay (Ct 17.34–18.68 vs. 14.86–16.06 for ORF1ab), shares the index partner's exact Alpha haplotype and polymorphic C23099A site, and rules out within-lab contamination because no closely related Epsilon genome had been sequenced by NYC DOHMH.

* **No Alpha/Epsilon recombinant lineage achieved onward community transmission in New York City: [Well Supported].**  
  Screening all 27,806 NYC surveillance genomes through September [YEAR] with 3SEQ (under both strict $\alpha = 0.05$ and permissive $\alpha = 0.25$ Dunn–Sidak family-wise error thresholds) and scanning for shared diagnostic synapomorphies identified zero descendants of the `NYCPHL-002461` major/minor pair, while incidentally recovering a distinct Alpha/Iota (B.1.526) putative recombinant (`EPI_ISL_2965250`).

* **Reproducible recombinant haplotype frequencies across the four extractions and cloned amplicons rule out in vitro RT or PCR chimerism as the dominant source of recombinants: [Overstated].**  
  The authors argue (Results, lines 144–150; Methods, line 185) that in vitro recombination is stochastic and would yield substantially different haplotype frequencies across independent extractions. That assumption only holds when chimeric events occur as rare early-cycle jackpots in low-template reactions. At Ct ~15 ($>10^6$ input RNA copies), bulk RT and 35-cycle PCR template switching acts as a deterministic mass-action process: given the same ~75%:20% parental template ratio and identical primer/cycling conditions, in vitro jumping PCR will reproducibly yield the same ~4% chimeric fraction across replicate extractions. Furthermore, the cloning protocol used a 15-second extension at 68°C across 35 cycles for a 947 nt fragment (line 191); incomplete strand extension in short-extension, high-cycle PCR strongly promotes chimera formation, explaining why recombinant clones jump from 7.5% (657 nt fragment) and 11.1% (476 nt fragment) to 29.8% (including 2- and 3-breakpoint chimeras) in the 947 nt fragment.

* **S-gene deletions $\Delta 69\text{–}70$ and $\Delta 144$ are "shared" between the major and minor strains in primary sequencing (>97%) due to ARTIC V3 amplification bias: [Moderately Supported].**  
  While Results (line 82 and Fig. 1) initially groups $\Delta 69\text{–}70$ (98.3%) and $\Delta 144$ (97.8%) into the "shared" allele category, the cloning of the 657 nt S region recovers them at 77.4% (72/93) and 76.3% (71/93)—matching the other Alpha substitutions (~74%) and the TaqPath S-gene Ct shift. The Discussion (line 168) appropriately notes that ARTIC V3 preferential amplification of deleted templates likely caused this discrepancy, though labelling them as "shared" in the Results and Figure 1 is misleading.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Benchmark Baseline In Vitro RT-PCR Chimera Rates or Temper In Vivo Recombination Claims
* **WHY:** Without a synthetic mixture control of pure Alpha and pure Epsilon RNA (e.g., mixing index case `NYCPHL-002130` RNA at 75–80% with an unmixed Epsilon isolate at 20–25% at Ct 15), consistency across technical replicates cannot separate deterministic bulk RT-PCR template switching from true in vivo recombination.
* **WHAT:** If archival RNA from `NYCPHL-002130` and an Epsilon specimen is available, run a 75:25 artificial mixture control through the ARTIC V3 and 947 nt cloning protocols to measure the baseline in vitro chimera rate; if wet-lab experiments are no longer feasible, explicitly reframe the Results and Discussion to acknowledge that bulk RT-PCR template switching at high template copy number (Ct ~15) produces reproducible equilibrium chimera rates across technical replicates.
* **HOW:** Compare the 29.8% recombinant fraction in the 947 nt clone library against the ~8.2% total reciprocal recombinant read fraction (`23604A/23709C` at 3.9% + `23604C/23709T` at 4.3%) in the short-read extracts (which actually rejects homogeneity when pooling the 31/104 recombinant clones against ~8.2% in deep sequencing), and note that the 15-second PCR extension step for the 947 bp amplicon likely inflated multi-breakpoint chimeras during cloning.

#### 2. Correct the Statistical Comparison Between Cloned Amplicons and Short-Read Extracts
* **WHY:** In lines 146–147, the authors report non-significant Fisher's exact test $p$-values ($p = 0.190$ to $0.357$) comparing the cloning experiment to extracts A–D for individual two-site haplotypes (`23604A/23709C` at 3.9% and `23604C/23709T` at 4.3%), yet fail to report the exact clone counts for those specific two-site pairs in the main text while reporting 31/104 (29.8%) total recombinant clones across the 947 nt locus.
* **WHAT:** Report the exact count and percentage of the 104 clones carrying `23604A/23709C` and `23604C/23709T` alongside the short-read frequencies in the main text, and explain why the overall 947 nt clone recombination rate (29.8% across 5 differentiating sites) is ~3.6-fold higher than the two-site short-read recombinant frequency (8.2%).
* **HOW:** Add a summary table in the main text listing, for each adjacent pair of differentiating sites in the 947 nt, 657 nt, and 476 nt regions, the exact number of recombinant clones ($k / n$) alongside the corresponding short-read haplotype frequencies in Extracts A, B, C, and D.

#### 3. Reclassify $\Delta 69\text{–}70$ and $\Delta 144$ as Amplicon-Biased Alpha Alleles Rather Than "Shared" Alleles
* **WHY:** Labelling $\Delta 69\text{–}70$ and $\Delta 144$ as "Shared" alleles in the Results (line 82) and Figure 1 contradicts both the TaqPath S-gene amplification (Ct 17.34–18.68) and the 657 nt cloning assay (77.4% and 76.3% deletion frequency).
* **WHAT:** Reclassify $\Delta 69\text{–}70$ and $\Delta 144$ in the Results text and Figure 1 legend as Alpha-specific deletions that suffered from ARTIC V3 allelic dropout/amplification bias in the Epsilon background.
* **HOW:** Update line 82 and the Figure 1 caption to state that only the four ancestral B.1 substitutions (`C241T`, `C3037T`, `C14408T`, `A23403G`) are genuinely shared between both parental strains, while $\Delta 69\text{–}70$ and $\Delta 144$ appear at >97% in ARTIC V3 reads due to primer/amplicon bias.

#### 4. Resolve Internal Numerical, Table, and Coordinate Discrepancies
* **WHY:** Several numbers, mutation lists, and genomic coordinates conflict across sections of the manuscript.
* **WHAT & HOW:**
  1. **Index case `C23099A` frequency:** Reconcile line 23 (*"with C in 20.4% of reads and A in 79.6% of reads"*) with line 90 (*"The C23099A mutation... was present at 88.1% in NYCPHL-002130"*).
  2. **Missing Epsilon mutations in Table 2:** Line 86 states *"All but one of the 12 diagnostic Epsilon mutations was found in this set: A28272T is absent"*, and line 99 cites `(Table 2)` for `T28272A`, but Table 2 lists only 5 Epsilon mutations (`C1059T`, `A12878G`, `G17014T`, `G21600T`, `G22018T`). Add the remaining 7 diagnostic Epsilon sites (including position 28272 and S `L452R` / `T22917G` and `S13I` / `W152C`) to Table 2.
  3. **Mutation coordinate typo:** Reconcile `C12100T` (line 92) vs. `C12110T` (line 197) for the Epsilon subclade synapomorphy.
  4. **Cloned S-fragment coordinates:** Reconcile line 132 (*"657 nt in the S gene (positions 21442–22098)"*) with line 187 (*"657 nt fragment (positions 21421–22098)"*, which spans 678 nt).
  5. **GISAID accession typos:** Correct `EPI_ILS_1254173` and `EPI_ILS_873881` in line 99 to `EPI_ISL_1254173` and `EPI_ISL_873881`.
