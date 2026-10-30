# Review of AN_ANON_050

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript characterizes an in vivo SARS-CoV-2 superinfection from New York City involving an Alpha (B.1.1.7, ~75% allele frequency) and an Epsilon (B.1.429, ~20% allele frequency) variant (`NYCPHL-002461`), linked via contact tracing and travel history to an Alpha-infected index case (`NYCPHL-002130`). The authors perform four independent RNA extractions and ARTIC V3 whole-genome sequencing runs across two specimen aliquots, infer maximum-likelihood and molecular-clock phylogenies (`n = 3,655` Alpha and `n = 2,275` Epsilon genomes), apply three four-gamete recombination tests across 15 short-read fragments in S and N, sequence cloned PCR amplicons across three genomic regions (947 nt and 657 nt in S, and 476 nt in ORF8; `n = 104`, `93`, and `36` clones), and screen 27,806 NYC surveillance genomes using `3SEQ` for onward recombinant transmission. Sequencing accessions, an interactive notebook, and tool versions are documented.

The evidence for authentic Alpha/Epsilon co-infection is solid, supported by TaqPath S-gene Ct shifts (~2.5–3 cycles higher than ORF1ab/N), consistent allele frequency distributions across four independent extractions, and phylogenetic placement showing the major strain is identical to the contact-traced index case and contemporaneous Ghanaian sequences while the minor strain has no close relatives in the sequencing laboratory. However, the inference that all observed mosaic haplotypes reflect in vivo recombination rather than in vitro RT-PCR template switching rests on a flawed statistical premise: at high viral load ($Ct \approx 15\text{--}16$), deterministic chimera formation rates during 35-cycle PCR can produce reproducible recombinant frequencies across technical replicates of the same specimen without requiring stochastic divergence. An artificial mixture control (mixing pure Alpha and Epsilon RNA at 75:25) is needed to quantify baseline in vitro chimera rates, alongside corrections for primer-induced allele dropout at S:$\Delta 69\text{--}70$/$\Delta 144$ and minor internal numerical inconsistencies.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Co-infection of patient `NYCPHL-002461` with Alpha (B.1.1.7) and Epsilon (B.1.429) variants: [Well Supported].**  
  Four independent extractions from two aliquots reproducibly recover 21 Alpha-defining substitutions at median 74.1% frequency and 11 Epsilon-defining substitutions at 10–25% frequency. The TaqPath assay confirms S-gene amplification delayed by ~2.6 cycles relative to ORF1ab/N (consistent with an ~18–20% non-deleted Epsilon template), and phylogenetic clock regressions confirm both lineages match mid-January evolutionary expectations without matching intra-laboratory Epsilon sequences.

* **Absence of onward transmission of an Alpha/Epsilon recombinant in NYC surveillance (`n = 27,806` genomes): [Well Supported].**  
  Screening 27,806 NYC genomes with `3SEQ` under both conservative ($\alpha = 0.05$) and permissive ($\alpha = 0.25$) Dunn-Sidak thresholds identifies no descendants of the `NYCPHL-002461` parental strains, and reveals a separate putative Alpha/Iota (`B.1.526`) mosaic (`EPI_ISL_2965250`).

* **Reproducible haplotype frequencies across four extractions rule out in vitro RT-PCR recombination as a major contributor: [Overstated].**  
  The authors argue that in vitro recombination has a strong stochastic component that would yield substantially different haplotype frequencies across independent extractions (`p = 0.19–0.41`, Fisher's exact test between clones and extracts). While this is true at limiting dilution, `NYCPHL-002461` had a very high viral load ($Ct \approx 14.9\text{--}16.1$, corresponding to $>10^6$ template copies per reaction). At high template copy numbers, the law of large numbers ensures that sequence-specific RT and PCR template-switching probabilities converge to reproducible mean frequencies across technical replicates of the same RNA ratio. Without an empirical 75:25 synthetic mixture control of pure Alpha and Epsilon clinical extracts processed through the exact RT, 35-cycle PCR, and TOPO TA cloning protocols, the fraction of observed mosaic clones (e.g., 29.8% in the 947 nt S amplicon) attributable to in vivo vs. in vitro recombination cannot be separated quantitatively.

* **Four-gamete tests on 15 short-read fragments demonstrate statistically significant recombination across S and N: [Fragile].**  
  Table 3 applies three tests (`PHI`, `MCL`, and $R^2$ vs. Dist) across 15 fragments (45 tests total) without multiple-testing correction, yielding strong discordance among methods (e.g., S fragments 6 and 11 have `PHI` $p < 0.001$ but `MCL` and $R^2$ $p \ge 0.071$; S fragments 7, 9, and 10 have `PHI` $p > 0.9$ but `MCL` and $R^2$ $p \le 0.047$). Because short ARTIC amplicons undergo 35 PCR cycles, low-frequency chimeric reads (>1% MAF threshold) can trigger four-gamete incompatibility even in the absence of in vivo recombination.

* **Classification of S:$\Delta 69\text{--}70$ and S:$\Delta 144$ as "shared" alleles between major and minor strains: [Methodologically Flawed].**  
  In Results (lines 82–83) and Table 2, S:$\Delta 69\text{--}70$ (98.3%) and S:$\Delta 144$ (97.8%) are categorized as "shared" alleles in `NYCPHL-002461`. However, both the TaqPath S-gene Ct value (17.34–18.68, proving intact 69–70 target in ~20% of templates) and the 657 nt cloning assay (showing $\Delta 69\text{--}70$ in 77.4% and $\Delta 144$ in 76.3% of clones, matching the Alpha major strain frequency) demonstrate that the minor Epsilon strain does not carry these deletions, and that their >97% frequency in ARTIC V3 sequencing is an amplicon/mapping artifact.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Benchmark In Vitro RT-PCR Chimera Rates Using an Empirical Mixture Control (or Calibrate Claims)
* **WHY:** High-titer RNA mixtures ($Ct \approx 15$) subjected to SuperScript IV RT and 35 cycles of PCR generate deterministic rates of template switching at specific secondary-structure hotspots, making cross-replicate consistency insufficient to exclude in vitro artifacts.
* **WHAT:** Quantify the empirical baseline rate of artificial recombinant haplotypes generated by the ARTIC V3 and TOPO TA cloning protocols, or reframe the quantitative attribution if wet-lab experiments are not feasible.
* **HOW:** Mix RNA from the pure Alpha index case (`NYCPHL-002130`) and a pure Epsilon clinical specimen at a 75:25 ratio (matched to `Ct ~ 15.5`), run the same RT-PCR protocol, and measure the resulting mosaic read frequencies at positions `23604/23709` and `27972–28111`. If new wet-lab runs cannot be performed, explicitly model the expected binomial/multinomial variance of PCR chimeras at high template copy number ($N > 10^5$) and temper the conclusion in lines 144–150 to acknowledge that reproducible frequencies across technical replicates do not exclude deterministic sequence-specific RT-PCR template switching.

#### 2. Reconcile ARTIC V3 Allele Frequencies at S:$\Delta 69\text{--}70$ and S:$\Delta 144$
* **WHY:** Categorizing $\Delta 69\text{--}70$ and $\Delta 144$ as "shared" alleles in the main text and Figure 1 contradicts the TaqPath RT-PCR data and the 657 nt cloning results.
* **WHAT:** Reclassify S:$\Delta 69\text{--}70$ and S:$\Delta 144$ as Alpha (major strain) alleles affected by ARTIC V3 amplicon bias or short-read indel alignment bias, and check whether soft-clipped wild-type reads spanning these deletions were filtered out during `BWA-mem` / `lofreq` processing.
* **HOW:** Inspect the unclipped BAM alignments in ARTIC amplicons 72 and 73 around positions `21765–21770` and `21991–21993` in `NYCPHL-002461-A/B/C/D` to determine whether Epsilon wild-type reads were dropped due to primer mismatch or dropped by `lofreq` indel calling, and annotate S:$\Delta 69\text{--}70$ and $\Delta 144$ in Table 2 and Figure 1 accordingly.

#### 3. Apply Multiple-Testing Correction and Concordance Criteria to Table 3
* **WHY:** Running 45 tests across 15 fragments in Table 3 without family-wise or FDR control inflates false positives, and `PHI` vs. `LDHat` (`MCL`, $R^2$ vs. Dist) show opposing results on fragments 6, 7, 9, 10, and 11.
* **WHAT:** Report Benjamini-Hochberg FDR-adjusted $p$-values in Table 3 and explain why `PHI` (which tests spatial clustering of incompatible sites) returns $p > 0.9$ on fragments 7, 9, and 10 where `MCL` and $R^2$ return $p < 0.05$ (e.g., when only a single pair of variant-defining sites exists in the fragment).
* **HOW:** Compute BH-adjusted $q$-values across the 15 fragments for each test, add the number of polymorphic sites ($S$) per fragment as a column in Table 3, and restrict claims of short-read incompatibility to fragments with $\ge 2$ diagnostic parental sites that survive FDR correction.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several numerical values, genomic coordinates, and accession IDs conflict between sections.
* **WHAT & HOW:**
  1. **Index case `C23099A` frequency discrepancy:** Line 23 states `C23099A` has "C in 20.4% of reads and A in 79.6% of reads" in `NYCPHL-002130`, whereas line 90 states `C23099A` "was present at 88.1% in NYCPHL-002130." Reconcile to the exact `lofreq` output value.
  2. **Cloned 657 nt S-fragment coordinates:** Line 132 reports positions `21442–22098` ($22098 - 21442 + 1 = 657\text{ nt}$), whereas Methods line 187 reports `21421–22098` ($678\text{ nt}$). Verify against the forward primer `5'-AGGGGTACTGCTGTTATGTCT` (which maps to Wuhan-Hu-1 `21442–21462`) and correct line 187 to `21442–22098`.
  3. **Epsilon synapomorphy position typo:** Line 92 lists `C8947T, C12100T, and C10641T`, whereas Methods line 197 lists `C8947T, C12110T, and C10641T`. Correct to the actual position (`C12100T`).
  4. **GISAID accession prefix typos (Line 99):** Change `EPI_ILS_1254173` and `EPI_ILS_873881` to `EPI_ISL_1254173` and `EPI_ISL_873881`.
  5. **Ct value clarification (Line 183 vs. Table 1):** Clarify in Methods line 183 that the initial screening Ct values of 19 and 20 came from the diagnostic COVID Express assay, whereas Table 1 reports the subsequent TaqPath RT-PCR Ct values (14.86–16.25).
