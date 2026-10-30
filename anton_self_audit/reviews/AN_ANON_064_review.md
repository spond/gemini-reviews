# Review of AN_ANON_064

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This server and platform update manuscript details architectural, user-interface, tool-management, and community advancements in `[SOFTWARE]` (focusing on the flagship public server `[SOFTWARE]` Main and its open-source ecosystem) over a two-year period. Key engineering developments include: (1) frontend refactoring from server-side Mako templates to client-side RESTful API views and `Vue.js` components, validated on a single-cell RNA-seq workflow generating 11,872 history items across 64,000 transcripts; (2) backend federated job routing from `[SOFTWARE]` Main (via `Slurm`, `RabbitMQ`, and `[SOFTWARE_PACKAGE]`) to national cyberinfrastructure resources (`XSEDE` `Bridges`, `Stampede`, and `Jetstream` cloud); (3) global read-only distribution of 5 TB of versioned reference and index data via CernVM-FS (`CVMFS` Stratum 0/1 replica servers with `Squid` caches); (4) reproducible tool dependency resolution via `Conda`/`Bioconda` and `Docker`/`Singularity` (`BioContainers`) across 5,628 ToolShed tools; and (5) automated production deployment via open-source `Ansible` playbooks, `CloudBridge`/`CloudLaunch`, and `[SOFTWARE]`-Docker flavors. All source code, deployment playbooks, and training materials are openly available on GitHub.

The manuscript provides a transparent systems-level blueprint (especially Figure 2's infrastructure schematic and open `Ansible` playbooks) that enables external institutions to replicate the exact production architecture of `[SOFTWARE]` Main. The primary limitations are: (1) the frontend and backend scalability claims—handling 11,872 history items "seamlessly" and running jobs "up to an order of magnitude larger than before" on `Bridges`/`Stampede` (Figure 3)—are presented without quantitative timing, latency, memory, or job-throughput tables; and (2) while the Abstract states that `[SOFTWARE]` ensures "analyses are completely reproducible," the newly integrated Interactive Environments (`Jupyter`) allow ad hoc scripting whose provenance is not automatically captured in workflows (as acknowledged briefly in the concluding future-directions paragraph). Adding basic quantitative systems metrics and qualifying the provenance scope of Interactive Environments would tighten the alignment between the architectural claims and empirical evidence.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Production infrastructure reproducibility via `CVMFS` (5 TB reference data), `Bioconda`/`BioContainers`, and open `Ansible` playbooks: [Well Supported].**  
  The combination of Stratum 0/1 `CVMFS` reference data distribution (Figure 2D), `Bioconda`/`BioContainers` dependency isolation, `[SOFTWARE_PACKAGE]` tool verification, and published `Ansible` playbooks for `[SOFTWARE]` Main provides a complete, auditable stack for deterministic tool execution and server replication.

* **Frontend refactoring (RESTful API, `Vue.js`, named-tag propagation, nested collection operators) supports large single-cell RNA-seq histories (11,872 items): [Moderately Supported].**  
  Replicating a single-cell hematopoietic stem cell RNA-seq experiment (Ref. 4) generating 11,872 history items across 64,000 transcripts demonstrates functional capability where legacy Mako-rendered pages failed. However, the manuscript reports no quantitative frontend performance metrics (e.g., page load latency, REST payload size, browser memory footprint, or collection operation execution time) comparing the new client-side architecture against the previous release.

* **Dynamic job routing to `XSEDE` (`Bridges`, `Stampede`, `Jetstream`) via `[SOFTWARE_PACKAGE]` enables jobs "up to an order of magnitude larger than before" and higher concurrency: [Moderately Supported].**  
  The architectural integration of `Slurm`, `RabbitMQ`, and `[SOFTWARE_PACKAGE]` across `TACC` and `PSC` (Figure 2A) clearly expands compute and memory capacity beyond the 15 local dedicated nodes. Nevertheless, Figure 3 is a qualitative conceptual schematic rather than an empirical plot: no data are provided on maximum memory/core allocations, WAN file-staging overhead via `[SOFTWARE_PACKAGE]`, queue wait times, or monthly job throughput on `Bridges`/`Stampede` versus local nodes.

* **Interactive Environments (`Jupyter`) seamlessly combine graphical UI and ad hoc scripting while "ensuring analyses are completely reproducible": [Overstated].**  
  In the Abstract and Introduction, complete reproducibility is stated as an unconditional property of `[SOFTWARE]`. However, Interactive Environments (Line 50) permit arbitrary ad hoc scripting inside containers without automatic parameter/dependency capture in the `[SOFTWARE]` workflow graph, a limitation the authors acknowledge only at the very end of the manuscript (Line 93: *"Current future directions include... tighter coupling of Interactive Environments with provenance and reuse"*).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace or Supplement the Conceptual Figure 3 Schematic with Empirical Job-Scaling and Frontend Benchmarks
* **WHY:** Figure 3 visually depicts job size and concurrency gains on `Bridges`, `Stampede`, and `Jetstream`, and Line 32 cites a 11,872-item scRNA-seq benchmark, but neither is accompanied by numerical measurements.
* **WHAT:** Provide a concise summary table or empirical panel in Figure 3 reporting (a) frontend response time and browser memory usage as a function of history/collection size ($10^2, 10^3, \text{ and } 11,872$ items), and (b) job execution statistics on `[SOFTWARE]` Main across local nodes vs. `Bridges`/`Stampede`/`Jetstream` (allocated cores/RAM per job, `[SOFTWARE_PACKAGE]` data-staging transfer rates, and monthly job counts per resource).
* **HOW:** Extract historical job logs from `[SOFTWARE]` Main's `PostgreSQL` database and browser timing profiles from the 11,872-item scRNA-seq test history to populate quantitative axes in Figure 3.

#### 2. Explicitly Qualify Reproducibility Guarantees When Using Interactive Environments (`Jupyter`)
* **WHY:** Readers and reviewers benefit from a clear distinction between declarative ToolShed tools (where inputs, parameters, and `BioContainer` versions are locked in the workflow graph) and interactive `Jupyter` sessions.
* **WHAT:** State in the "NEW FEATURES" section (Line 50) how users should persist `Jupyter` notebooks into their `[SOFTWARE]` history and note that fully automated provenance capture for interactive sessions is under active development.
* **HOW:** Add two sentences at Line 50 cross-referencing the provenance roadmap item on Line 93 and recommending that users export executed notebooks back to the history for archival reproducibility.

#### 3. Technical and Editorial Cleanup
* **WHY:** Minor typographical errors in the text should be cleaned up for publication accuracy.
* **WHAT & HOW:**
  * **Main Text (Line 14):** Change *"124,000 registered users whom run ∼245,000 analysis jobs"* to *"124,000 registered users who run ∼245,000 analysis jobs"*.
  * **Main Text (Line 46):** Change *"explorative analysis of deeply sequence data"* to *"explorative analysis of deeply sequenced data"*.
  * **Main Text (Line 66):** Change *"existed in in standalone workflow systems"* to *"existed in standalone workflow systems"*.
  * **Main Text (Line 72):** Change *"5TB of pre-build reference data"* to *"5 TB of pre-built reference data"*.
