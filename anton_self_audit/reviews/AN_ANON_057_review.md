# Review of AN_ANON_057

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.2 / 10.0** (Exemplary) | **Scientific Core Score:** **7.3 / 8.0**  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents `[SOFTWARE_PACKAGE] 3`, a browser-native platform for molecular evolutionary and selection inference that executes the `[SOFTWARE_PACKAGE]` maximum-likelihood engine locally on the client device via WebAssembly (`wasm32` managed through the `Aioli` runtime inside a dedicated Web Worker), paired with persistent local `IndexedDB` storage, a `Svelte 5` / `TailwindCSS` progressive-disclosure interface, automated sequence validation (`FASTA-001` to `FASTA-007` plus codon-alignment checks), data-driven runtime estimation, an optional `Socket.IO` bridge to remote HPC clusters for alignments exceeding browser limits, and a Model Context Protocol (MCP) server for programmatic and AI-assisted workflows. The authors benchmark single-threaded WebAssembly execution (`v2.5.96` in headless Chromium) against single-threaded and multi-threaded native binaries (`v2.5.93` with ARM NEON SIMD) on a dedicated 128-core ARM Neoverse-N1 node across six classic reference alignments (`bglobin`, `lysozyme`, `HIVvif`, `adh`, `HepatitisD`, `camelid`) and an independent stratified corpus of 100 real-world alignments (`aBSREL`, `BUSTED`, `FEL`, `MEME`, and `SLAC`). The web application and MIT-licensed source code are publicly available.

`[SOFTWARE_PACKAGE] 3` is a well-engineered bioinformatics resource whose performance evaluation is transparent and thoughtfully controlled: by restricting Table 2 averages to identical datasets completing in both environments ($n=75$ to $87$ per method), reporting both mean runtimes and interquartile-to-median overhead dispersion, and documenting hardware and mobile browser memory ceilings (4 GB `wasm32` limit, 300–500 MB on mobile, and Safari `IndexedDB` eviction caveats), the authors avoid overclaiming client-side capabilities. Three straightforward additions would make the benchmark and technical documentation even stronger: (1) reporting a numerical equivalence check ($\Delta \ln L$ and site/branch $p$-value concordance) between native `aarch64` NEON and `wasm32` across the 100-alignment corpus; (2) detailing the functional form and prediction error of the data-driven runtime estimator; and (3) specifying the timeout vs. out-of-memory breakdown for the 13–25 excluded datasets per method in Table 2.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Client-side WebAssembly execution of maximum-likelihood selection methods (`aBSREL`, `BUSTED`, `FEL`, `MEME`) incurs a modest 1.67×–1.93× overhead relative to single-threaded native execution, enabling interactive browser-based inference for alignments below 50,000–200,000 sequence $\times$ site products: [Well Supported].**  
  Across 75–84 matched real-world alignments on identical hardware (Table 2) and six curated benchmarks (Fig. 2), the four likelihood methods consistently complete within ~1.7×–1.9× of native single-core C++ execution, with mean Wasm runtimes of 580–1,261 seconds (under 25 minutes).

* **WebAssembly overhead is method-dependent, with the counting-based `SLAC` method exhibiting the highest relative slowdown (+405.9%, 5.06×) but the tightest relative predictability (30% IQR/median): [Well Supported].**  
  Table 2 and Figure 2 clearly demonstrate the divergence between `SLAC` (+405.9% mean overhead, 30% IQR/median across 87 datasets) and the iterative numerical optimization methods (`aBSREL`, `BUSTED`, `FEL`, `MEME`, +67.1% to +93.2% mean overhead, 44%–63% IQR/median).

* **Browser-native execution preserves data sovereignty and eliminates server queue latency while providing seamless fallback to HPC clusters and AI-agent orchestration via MCP: [Well Supported].**  
  Executing validation and `wasm32` inference inside a local Web Worker with `IndexedDB` persistence ensures sequences never leave the client device during standard runs, while the optional `Socket.IO` backend bridge and the six-tool MCP endpoint (`list_analyses`, `validate_alignment`, `spawn_analysis`, `get_job_status`, `get_job_results`, `cancel_job`) support heavy workloads and automated multi-step pipelines (such as `GARD` followed by partition-specific `FEL`).

* **Data-driven runtime estimation models accurately predict completion times and guide local vs. server offloading: [Moderately Supported].**  
  While the manuscript states that runtime estimation models are calibrated against historical production analyses using alignment characteristics (lines 6, 38, 50), it does not describe the predictive model's mathematical specification, input features, or out-of-sample accuracy (e.g., $R^2$ or median relative error on the 100-alignment benchmark set).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Numerical Equivalence ($\Delta \ln L$ and Parameter/P-Value Concordance) Between Native `aarch64` and `wasm32`
* **WHY:** Non-convex multi-parameter likelihood optimization in branch-site models (`aBSREL`, `BUSTED`, `MEME`) can be sensitive to floating-point instruction differences (e.g., fused multiply-add and NEON SIMD in native `aarch64` vs. strict IEEE-754 in `wasm32`). Verifying that both compilation targets converge to the same maximum-likelihood estimates and biological inferences is a core validation requirement for a numerical port.
* **WHAT:** Quantify the distribution of absolute differences in log-likelihood ($|\ln L_{\text{WASM}} - \ln L_{\text{CLI}}|$), key rate parameters ($\omega$), and site/branch $p$-values across the 75–87 completed datasets per method in Table 2.
* **HOW:** Parse the output JSON files already generated from the Table 2 benchmark runs for native (`2.5.93`) and Wasm (`2.5.96`), compute the median and maximum $|\Delta \ln L|$ and classification agreement (at $p \le 0.05$ or $p \le 0.10$) for each of the five methods, and add 2–3 sentences summarizing the numerical concordance in the benchmark section.

#### 2. Specify the Runtime Estimation Model and Document the Exclusion Criteria for the 13–25 Uncompleted Datasets in Table 2
* **WHY:** Readers and developers deploying `[SOFTWARE_PACKAGE] 3` need to know how runtime predictions are computed, what exact wall-clock timeout or memory threshold excluded the 13–25 most intensive alignments in Table 2, and why `SLAC` experiences a 5.06× Wasm slowdown compared to ~1.8× for likelihood methods.
* **WHAT:** State the exact timeout value used in the headless Chromium benchmark, break down how many excluded runs hit the timeout vs. the 4 GB `wasm32` memory limit, briefly explain the `SLAC` overhead mechanism, and state the runtime predictor's formula and accuracy.
* **HOW:**
  1. In §2.5 / Table 2, specify the wall-clock timeout threshold (e.g., 3,600 s) and how many of the excluded datasets (25 for `aBSREL`/`BUSTED`, 23 for `MEME`, 16 for `FEL`, 13 for `SLAC`) failed due to memory exhaustion vs. timeout.
  2. Briefly note why `SLAC` has a 5.06× relative overhead (e.g., short total runtime dominated by Wasm startup/tree-traversal/dictionary-lookup overhead or lack of SIMD vectorization compared to heavy floating-point matrix exponentiation in likelihood methods, and clarify whether `-msimd128` was enabled in the `wasm32` build).
  3. State the functional form of the runtime estimator (e.g., power-law regression on $N_{\text{seq}}$ and $N_{\text{sites}}$) and report its prediction error on the 100-alignment benchmark corpus.

#### 3. Clarify Data Sovereignty for the Remote MCP Server and Fix Minor Text Typos
* **WHY:** Because data sovereignty (sequences remaining on the client device) is a central theme of the paper, readers should understand that calling the hosted MCP server (`https://mcp.[SOFTWARE_PACKAGE].org/mcp`) transmits sequences to a remote server unless the MCP server is self-hosted locally.
* **WHAT & HOW:**
  1. **MCP privacy note (lines 86–88):** Add a brief clarification that while browser-based Wasm execution keeps data strictly local, jobs submitted through the hosted remote MCP server (`spawn_analysis`) are transmitted to and executed on the server (or a locally deployed MCP instance if data sovereignty is required).
  2. **Typographical fixes (line 84):** Correct *"sequence bisite products"* and *"sequence itsite products"* to *"sequence $\times$ site products"*.
