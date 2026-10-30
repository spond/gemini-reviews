# Review of AN_ANON_072

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.9 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This bioinformatics resource and software manuscript introduces `[SOFTWARE]`, an interactive web-based platform (`http://g2.bx.psu.edu`) that bridges genome annotation databases (such as the UCSC Table Browser) with coordinate-based set operations, sequence analysis modules, and genome browser visualization tracks. Architecturally, `[SOFTWARE]` decouples a C-based core engine and genomic interval operation library (built on UCSC codebase conventions and backed by a local MySQL database for storing user histories and precomputed datasets) from a lightweight Perl CGI History User Interface (`HUI`) communicating via HTTP GET/POST requests. The authors benchmark query and operation execution times ($44\text{ sec}$ average for UCSC Table Browser retrieval; $53\text{ sec}$ average and $8\text{ min}$ typical maximum for interval set operations) and demonstrate the platform through three applications: (1) intersecting *IGF-II* coding exons with dbSNP variants to recover six coding SNPs; (2) intersecting $289$ experimentally validated ENCODE promoters against six experimental and comparative genomic tracks (DNase I hypersensitivity, RNA Pol II ChIP, TAF1 ChIP in HeLa cells, multispecies conserved sequences, `phastConsElements`, and regulatory potential; Table 1); and (3) whole-gene and sliding-window $K_a/K_s$ estimation via the Yang–Nielsen method.

`[SOFTWARE]` addresses a genuine bottleneck for experimental biologists by enabling multi-step genomic interval algebra (unions, intersections, subtractions, proximity filtering) and persistent query histories without requiring command-line scripting or SQL fluency. The modular HTTP API separation between the C interval engine and the web interface is well engineered, and the ENCODE promoter case study provides clear biological examples of how comparative conservation (`phastCons`) and cell-type-specific ChIP binding (HeLa TAF1/Pol II) capture complementary subsets of functional elements (e.g., the muscle-specific *PYGM* promoter vs. the poorly conserved *LOC85865* promoter). The primary issues requiring attention are (1) a numerical discrepancy between the main text (line 77) and Table 1 regarding the counts of ENCODE promoters overlapping `phastConsElements` and `TAF1` binding regions; (2) the absence of multiple-testing and small-window variance controls in the sliding-window $K_a/K_s$ tool description; and (3) the lack of a public source-code repository link for deploying the C core and Perl UI locally.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The `[SOFTWARE]` history system and HTTP API architecture enable non-programmers to execute multi-step coordinate set operations across UCSC Table Browser tracks with sub-minute average response times: [Well Supported].**  
  The manuscript clearly documents the bidirectional integration with the UCSC Table Browser (`"Send Results to [SOFTWARE]"`), asynchronous job status tracking (`in queue`, `running`, `N regions`, `error`), BED/AXT/MAF format handling, and empirical response-time distributions ($44\text{ sec}$ average retrieval; $53\text{ sec}$ average interval operation).

* **Combining comparative conservation tracks with HeLa ChIP-chip data across 289 experimentally verified ENCODE promoters distinguishes constitutively bound conserved promoters (*CAV1*), lineage-specific unbound conserved promoters (*PYGM*), and non-conserved active promoters (*LOC85865*): [Well Supported].**  
  Table 1 and Figure 3A–C effectively demonstrate that neither sequence conservation (`phastConsElements`, $48\%$; `MCS`, $62\%$) nor single-cell-type transcription factor binding (`TAF1` in HeLa, $53\%$; `RNA Pol II`, $61\%$) alone captures all $289$ functional promoters, motivating integrative multi-track intersections.

* **Of the 289 ENCODE promoters, 95 overlap both `phastConsElements` and `TAF1`, while of the remaining 194 promoters, 52 overlap `TAF1` and 66 overlap `phastConsElements` (line 77): [Methodologically Flawed].**  
  The numbers reported in the prose on line 77 contradict Table 1. Summing the prose counts yields $95 + 52 = 147$ promoters overlapping `TAF1` and $95 + 66 = 161$ promoters overlapping `phastConsElements`. However, Table 1 reports $153$ promoters overlapping `TAF1` (line 85) and $139$ promoters overlapping `phastConsElements` (line 87), whereas $161$ is the count for `RP` (Regulatory Potential, line 88, where $161 - 95 = 66$). Thus, the prose in line 77 inadvertently substitutes the `RP` overlap total ($161$) for `phastConsElements` ($139$) and undercounts `TAF1` by $6$ promoters ($147$ vs. $153$).

* **The sliding-window $K_a/K_s$ module provides significantly greater resolution for detecting deviations from purifying selection than whole-gene $K_a/K_s$ tests: [Overstated].**  
  While whole-gene $K_a/K_s$ averages across sites, uncalibrated sliding-window $K_a/K_s$ scans using the pairwise Yang–Nielsen approximation suffer from high estimation variance in short windows (especially when window $K_s$ is small) and severe multiple-testing inflation across overlapping windows, which are not addressed in the tool description.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the ENCODE Promoter Intersection Counts Between Line 77 and Table 1
* **WHY:** In line 77, the intersections of the $289$ promoters with `TAF1` and `phastConsElements` sum to $95 + 52 = 147$ (`TAF1`) and $95 + 66 = 161$ (`phastConsElements`), directly conflicting with Table 1 (`Bound by TAF1` = $153$; `phastConsElements` = $139$; `RP` = $161$).
* **WHAT:** Re-check the history items (queries 34, 35, and 36 in Figure 3) and correct the numbers in line 77 so that the mutually exclusive subsets sum exactly to the marginal totals in Table 1.
* **HOW:** If $95$ promoters overlap both `TAF1` ($153$ total) and `phastConsElements` ($139$ total), update line 77 to state that of the remaining $194$ promoters, $153 - 95 = 58$ intersect with `TAF1` alone and $139 - 95 = 44$ intersect with a `phastConsElement` alone (leaving $194 - 58 - 44 = 92$ with neither). Alternatively, if $95$ was computed against `RP` ($161$), update the text to specify `RP` vs. `phastConsElements` explicitly.

#### 2. Add Statistical Guardrails and Parameter Documentation for the Sliding-Window $K_a/K_s$ Tool
* **WHY:** Running pairwise Yang–Nielsen $K_a/K_s$ across sliding windows without minimum synonymous-site thresholds or multiple-hypothesis correction generates frequent false-positive spikes ($K_a/K_s > 1$) driven by stochastic $K_s$ depletion in short windows.
* **WHAT:** Document the default window size and step size, enforce a minimum number of synonymous sites per window, and warn users about multiple testing across windows.
* **HOW:** Update the `"Evolutionary analyses with [SOFTWARE]"` section (line 94) to specify the default codon window/step lengths, cap or mask windows where $K_s \to 0$, and provide confidence intervals or Bonferroni/FDR-adjusted $P$-values across windows.

#### 3. Provide Open-Source Code Access for the C Core and Perl History User Interface
* **WHY:** The Methods section states that the operation libraries are available for use by other projects (line 107) and that any site can set up its own UI or run `[SOFTWARE]` functions locally (lines 109–114), but no source repository or download archive URL is provided.
* **WHAT:** Publish a tarball or version-controlled repository link containing the C core, interval operation libraries, MySQL schema, and Perl `HUI` scripts.
* **HOW:** Host the source code archive on `http://www.g2.bx.psu.edu` (and in the online supplement) under an open-source license and include the direct download URL in the Abstract and Methods.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor spelling errors appear in the text.
* **WHAT & HOW:**
  * **Line 94:** Correct `"Yang-Neilsen algorithm"` to `"Yang-Nielsen algorithm"` to match the citation `(Yang and Nielsen [YEAR])`.
