# Review of AN_ANON_072

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `Galaxy` (`http://g2.bx.psu.edu`), a web-based interactive platform that integrates genomic coordinate retrieval (from resources such as the UCSC Table Browser) with a persistent user history system, genomic interval set operations (intersection, union, subtraction, complement, size/proximity filtering, and distance clustering), sequence/evolutionary analysis modules (such as orthologous region lookup and Yang–Nielsen $K_a/K_s$ estimation), and visualization output back to the UCSC and Ensembl Genome Browsers. The authors illustrate the system through three biological use cases: (1) intersecting human `IGF-II` coding exons with dbSNP variants to identify 6 coding SNPs, (2) intersecting 289 experimentally verified ENCODE promoters against five experimental and computational regulatory tracks (`DNase HSs`, `RNA polymerase II`, `TAF1`, `MCS`, `phastConsElements`, and `Regulatory Potential` [RP]; Table 1), and (3) computing whole-gene and sliding-window $K_a/K_s$ profiles. The software architecture (a C core built on UCSC utility libraries, a MySQL local history/cache database, and a Perl CGI user interface communicating via HTTP GET/POST requests) and empirical query response times (mean 44 s for Table Browser queries and 53 s for interval operations) are documented.

As a bioinformatics infrastructure contribution, the history-based genomic interval manipulation paradigm is well-designed, modular, and directly empowers experimentalists without command-line or SQL training to perform reproducible multi-track coordinate queries. However, the manuscript has three notable weaknesses: (1) direct numerical contradictions between the main text (line 77) and Table 1 in the ENCODE promoter intersection analysis, (2) absence of background coverage normalization or statistical enrichment testing when comparing ENCODE regulatory tracks of vastly different genomic footprints (ranging from 230 `DNase HS` intervals to 23,148 `MCS` intervals), and (3) uncritical promotion of uncalibrated sliding-window $K_a/K_s$ scans without warning users about small-window $K_s$ variance or multiple testing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The `Galaxy` architecture enables interactive, no-code execution of multi-step genomic interval operations (intersection, union, subtraction, proximity filtering) with persistent history tracking and ~1-minute average execution times: [Well Supported].**  
  The HTTP API separation between the C computation engine and the Perl History User Interface (HUI), direct bidirectional integration with the UCSC Table Browser and Genome Browser custom tracks, and empirical response-time benchmarks (44 s average for queries, 53 s average and 8 min typical maximum for interval operations) clearly support the platform's usability and engineering design.

* **Intersection of 289 experimentally verified ENCODE promoters with biochemical (`TAF1`, `RNA Pol II`, `DNase HS`) and comparative genomic (`MCS`, `phastConsElements`, `RP`) tracks reveals distinct classes of conserved and tissue-specific promoters (Table 1 and line 77): [Fragile].**  
  First, the numbers reported in the main text (line 77) do not match Table 1: line 77 states that out of the 289 promoters, `95` overlap both `phastConsElements` and `TAF1`, and that of the remaining 194 promoters, `52` overlap `TAF1` and `66` overlap `phastConsElements`. Summing these gives $95 + 52 = 147$ promoters overlapping `TAF1` and $95 + 66 = 161$ promoters overlapping `phastConsElements`. However, Table 1 reports `153` promoters overlapping `TAF1` (line 85) and `139` promoters overlapping `phastConsElements` (line 87), while `161` is the Table 1 count for `RP` (Regulatory Potential, line 88). Second, Table 1 compares raw percentages of promoter overlap across tracks whose total interval counts across the ENCODE regions differ by two orders of magnitude (`230` intervals for `DNase HSs` vs. `23,148` intervals for `MCS` and `16,170` for `RP`), without reporting the fraction of base pairs covered by each track or testing whether the observed overlaps exceed random expectation.

* **The sliding-window $K_a/K_s$ test implemented in `Galaxy` provides "significantly greater resolution" than whole-gene $K_a/K_s$ estimation for detecting selection regimes (line 94): [Overstated].**  
  While averaging $K_a$ and $K_s$ across an entire gene can mask localized adaptive evolution, computing the Yang–Nielsen $K_a/K_s$ ratio in short sliding windows along a pairwise alignment introduces severe estimation variance (especially when the denominator $K_s$ approaches zero in a short window) and creates a substantial multiple-testing burden across overlapping windows. Presenting sliding-window $K_a/K_s$ ratios without confidence intervals, minimum $K_s$ thresholds, or multiple-hypothesis correction frequently leads users to misinterpret stochastic synonymous rate fluctuations as localized positive selection.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Numerical Contradictions Between Line 77 and Table 1
* **WHY:** In line 77, the marginal sums for `TAF1` ($95 + 52 = 147$) and `phastConsElements` ($95 + 66 = 161$) contradict Table 1 (`153` for `TAF1` and `139` for `phastConsElements`, whereas `161` is the count for `RP`). In a manuscript introducing a tool for exact set intersections and subtractions, arithmetic discrepancies between the text and Table 1 undermine confidence in the example workflow.
* **WHAT:** Audit queries 34, 35, and 36 in the ENCODE promoter history and correct either line 77 or Table 1 so that the pairwise intersection counts (`A ∩ B`, `A \ B`, `B \ A`) sum exactly to the marginal totals in Table 1.
* **HOW:** Re-run the exact two-way intersection and subtraction operations on the 289 ENCODE promoters against the `TAF1`, `phastConsElements`, and `RP` tracks, verify whether query 36 used `RP` (161) instead of `phastConsElements` (139), and update line 77 and Table 1 with the exact matching integers.

#### 2. Add Genomic Coverage Baselines and Fold-Enrichment Statistics to Table 1
* **WHY:** In Table 1, `MCS` (23,148 regions) overlaps 62% of promoters whereas `DNase HSs` (230 regions) overlaps 25% of promoters; without knowing how much of the 30 Mb ENCODE target space each track covers, a reader cannot tell whether `DNase HSs` is actually much more specific per kilobase than `MCS`.
* **WHAT:** Add three columns to Table 1: (1) total base pairs (or % of ENCODE target space) covered by each track, (2) expected number of overlapping promoters under uniform random placement within the ENCODE regions, and (3) fold enrichment with an empirical permutation or binomial $P$-value.
* **HOW:** Use `Galaxy`'s own interval tools to compute the total base-pair span of each of the six tracks within the 44 ENCODE regions, calculate the fold-enrichment over the genomic background fraction, and add these metrics to Table 1.

#### 3. Add Variance Warnings and Statistical Safeguards to the Sliding-Window $K_a/K_s$ Module
* **WHY:** Short coding windows often contain very few synonymous substitutions, causing unstable $K_a/K_s$ spikes that naive users interpret as positive selection.
* **WHAT:** Incorporate window-level uncertainty bounds or a Fisher's exact / likelihood ratio test $P$-value with multiple-testing correction in the sliding-window $K_a/K_s$ output, and note these statistical caveats in line 94.
* **HOW:** Modify the `Galaxy` $K_a/K_s$ wrapper to display the standard error of $K_a/K_s$ (from PAML `yn00`) or flag windows with fewer than a minimum number of synonymous sites/substitutions ($S_s < 3$), and add a brief cautionary note in the "Evolutionary analyses with Galaxy" section.

#### 4. Provide Direct Source Code Availability for Local Installation
* **WHY:** In the Methods ("Language", line 114), the authors note that the C core and Perl HUI are portable and could be run at UCSC or other sites, and that external sites can set up their own UIs, but no source code repository or tarball URL is given.
* **WHAT:** Provide an open-source archive or version-control URL for the C core library, interval operation binaries, and Perl HUI scripts.
* **HOW:** Add a link on `http://g2.bx.psu.edu` (and in the Methods section) to download the C source code and schema definitions under an open-source license, and fix the typo `"Yang-Neilsen"` in line 94 to `"Yang-Nielsen"`.
