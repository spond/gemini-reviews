# Review of AN_ANON_057

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a browser-native molecular evolution platform (`[SOFTWARE_PACKAGE] 3`) that compiles its statistical inference engine to WebAssembly (`wasm32` via `Aioli`) for asynchronous execution inside a client-side Web Worker, paired with local `IndexedDB` persistence, a Svelte 5 / TailwindCSS progressive-disclosure UI, optional `Socket.IO` offloading to backend HPC clusters for datasets exceeding browser limits, and a Model Context Protocol (`MCP`) server for programmatic/AI-agent workflows. The platform exposes 13 codon- and nucleotide-level evolutionary analyses (`SLAC`, `FEL`, `FUBAR`, `MEME`, `PRIME`, `aBSREL`, `BUSTED`, `RELAX`, `Contrast-FEL`, `GARD`, `MULTI-HIT`, `BGM`, and `B-STILL`) alongside automated `FASTA`/`NEXUS` validation (`FASTA-001` to `FASTA-007`). The authors benchmark single-threaded and multi-threaded native binaries (`v2.5.93`, ARM NEON SIMD) against headless Chromium WebAssembly (`v2.5.96`) on a 128-core ARM Neoverse-N1 node across 6 canonical alignments and an independent stratified corpus of 100 real-world alignments (`n = 75–87` completed datasets per method). Source code is released under the MIT license.

The engineering and benchmarking are well executed: compiling a full suite of maximum-likelihood and Bayesian codon models to run client-side with a `1.67x–1.93x` single-thread overhead for likelihood methods (`aBSREL`, `BUSTED`, `FEL`, `MEME`) eliminates upload queues and preserves sequence privacy for standard gene alignments (`<50,000` to `200,000` sequence $\times$ site products). A few methodological and reporting refinements would strengthen the paper: (1) Table 2 computes `WASM overhead` from the ratio of arithmetic mean runtimes across a heavily right-skewed alignment corpus rather than reporting the median and interquartile range (`IQR`) of per-dataset overhead ratios, and does not include the multi-core native baseline column; (2) the anomalous `5.06x` (`+405.9%`) slowdown for the counting-based `SLAC` method is reported without diagnosing its technical cause; and (3) the claim of "precise runtime estimation" (lines 14, 50) lacks empirical calibration metrics ($R^2$ or prediction error), and the privacy boundary between local browser execution and the hosted remote `MCP` endpoint should be explicitly stated.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Browser-native WebAssembly execution of maximum-likelihood selection models incurs a modest (<2x) single-core overhead on standard alignments: [Well Supported].**  
  Across `75–84` completed real-world alignments on matched hardware (ARM Neoverse-N1), the four likelihood-intensive methods (`aBSREL`, `BUSTED`, `FEL`, `MEME`) exhibit mean single-threaded overheads of `+67.1%` (`1.67x`), `+85.7%` (`1.86x`), `+93.2%` (`1.93x`), and `+72.8%` (`1.73x`), completing in under 30 minutes for alignments below `50,000` sequence $\times$ site products.

* **Empirical memory and size operating boundaries for `wasm32` client-side inference: [Well Supported].**  
  The authors clearly document the `4 GB` `wasm32` address-space limit (`300–500 MB` on mobile browsers), linear memory scaling (`100–200 MB` per `10,000` sequence $\times$ site products for site-level models; `200–400 MB` for branch-site models), and the `13%–25%` attrition rate on the largest alignments in the 100-dataset corpus, motivating the hybrid `Socket.IO` HPC fallback.

* **Counting-based `SLAC` exhibits a `5.06x` (`+405.9%`) WebAssembly slowdown with `30%` IQR/median consistency: [Moderately Supported].**  
  While the runtime measurement itself (`101.7s` CLI vs. `514.5s` WASM across `87` datasets) is clear, the manuscript offers no profiling or architectural explanation for why a lightweight ancestral counting method experiences a $5\times$ penalty when compute-bound matrix-exponential likelihood methods slow down by $<2\times$ (e.g., whether `SLAC` is bottlenecked by frequent `wasm32` heap allocations, dictionary/string manipulations, or synchronous console/Web Worker message serialization during site-by-site counting).

* **Data-driven runtime estimation provides precise completion time predictions prior to execution (Lines 14, 50): [Overstated].**  
  Although the UI incorporates a runtime predictor calibrated on historical production runs, the manuscript presents no model specification, features, or out-of-sample accuracy metrics (e.g., mean absolute percentage error or calibration across heterogeneous client CPUs), and notes in line 84 that even on a fixed server CPU the WASM-to-CLI ratio varies with `44%–63%` IQR/median.

* **End-to-end data sovereignty across all platform interfaces: [Moderately Supported].**  
  Client-side WebAssembly execution in the browser guarantees that sequences never leave the user's device. However, the hosted Model Context Protocol (`MCP`) server (`https://mcp.[SOFTWARE_PACKAGE].org/mcp` over Streamable HTTP with OAuth, lines 86–89) accepts `FASTA` alignments over the network for remote job execution, which does transfer sequence data off-device unless the user runs a local MCP server instance.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Per-Dataset Median and IQR Runtimes/Overheads and Multi-Core Native Baselines in Table 2
* **WHY:** Because the 100-alignment corpus spans over two orders of magnitude in size (`<10,000` to `>500,000` sequence $\times$ site products), arithmetic mean runtimes (`CLI runtime(s)` and `WASM runtime(s)` in Table 2) are dominated by the largest few alignments, and excluding multi-core native times from Table 2 omits the practical speed advantage of native execution on multi-core hardware.
* **WHAT:** Expand Table 2 to report the median and IQR of the per-dataset overhead ratio ($T_{\text{WASM}, i} / T_{\text{CLI-1core}, i}$), add a column for multi-threaded native CLI runtime, and specify the exact timeout limit and OOM vs. timeout failure counts for the `13–25` excluded datasets.
* **HOW:** From the existing 100-alignment benchmark logs, compute `median (IQR)` of per-dataset runtimes and overhead percentages alongside the means in Table 2, and state the exact headless Chromium timeout threshold (e.g., `3,600s` or `7,200s`) in the Table 2 legend.

#### 2. Diagnose and Explain the `5.06x` WebAssembly Overhead in `SLAC`
* **WHY:** Readers and bioinformatics tool developers using WebAssembly as a blueprint (Abstract) need to know why the simplest method (`SLAC`) suffers the highest Wasm penalty (`+405.9%`).
* **WHAT:** Profile a representative `SLAC` run in native vs. `wasm32` execution and add 2–3 sentences in Section 2 explaining the bottleneck.
* **HOW:** Check whether `SLAC`'s slowdown stems from initial NJ/GTR tree/branch optimization, frequent small memory allocations in codon ancestral state tables, or high-frequency stdout/progress callback bridging between `Aioli` Wasm and the Web Worker thread, and document the cause in lines 24 and 84.

#### 3. Quantify Runtime Estimator Accuracy and Clarify the Privacy Boundary of the Hosted MCP Server
* **WHY:** Claiming "precise runtime estimation" (line 14) requires an accuracy metric, and promoting strict data sovereignty requires distinguishing local browser Wasm from remote HTTP MCP calls.
* **WHAT:** Report the prediction error of the runtime estimator on the 100-alignment corpus (or temper "precise" to "approximate order-of-magnitude"), and clarify data routing for the MCP server.
* **HOW:** Compare the UI's predicted runtime against observed WASM runtime across the 100 benchmark datasets (reporting $R^2$ or median relative error), and add a sentence in Section 2.6 noting that while browser execution is 100% local, using the hosted `https://mcp.[SOFTWARE_PACKAGE].org/mcp` endpoint transmits alignments to the remote server unless deployed locally.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor text encoding artifacts appear in Section 2.5.
* **WHAT & HOW:**
  1. **Fix multiplication symbol encoding typos (Line 84):** Change `"<10,000 sequence bisite products"` and `">500,000 sequence itsite products"` to `"<10,000 sequence × site products"` and `">500,000 sequence × site products"` to match line 90.
