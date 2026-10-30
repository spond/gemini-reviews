# Review of AN_ANON_064

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This community server and software framework update describes two years of architectural, user-interface, and community developments in the `[WORKFLOW_PLATFORM]` (Galaxy) biomedical analysis workbench. The manuscript details four main pillars of engineering progress: (1) frontend UI modernization, replacing server-side Mako templates with client-side RESTful components and `Vue.js`, adding hash-prefixed propagating "named-tags" (`#`), a pluggable Webhook extension mechanism, and an interactive Tour Builder; (2) backend scalability and distributed execution on the main public server (>124,000 registered users running ~245,000 monthly jobs), adopting `uWSGI`, dynamic job routing via `[SOFTWARE_PACKAGE]` (Pulsar) and `RabbitMQ` to national cyberinfrastructure (XSEDE `Bridges`, `Stampede`, and `Jetstream`), and distributing 5 TB of versioned reference indices via CernVM-FS (CVMFS) Stratum 0/1 Squid replicas; (3) tool ecosystem and reproducibility infrastructure, reaching 5,628 ToolShed wrappers, introducing `tool profile versions` and no-restart tool installation, defaulting to `Conda`/`Bioconda`/`BioContainers` (`Docker` and `Singularity`), and adding `CloudBridge`/`CloudLaunch` and `Ansible` playbooks; and (4) workflow enhancements including sub-workflow embedding, background workflow scheduling, and initial Common Workflow Language (CWL) support.

The infrastructure engineering described in this update—particularly CVMFS Stratum 0/1 reference data synchronization, automated `Bioconda`/`BioContainers` dependency resolution, `Ansible` deployment playbooks, and dynamic routing of heavy jobs to XSEDE resources—represents solid systems architecture that directly benefits reproducible bioinformatics. However, every performance and scalability claim in the manuscript is presented qualitatively without supporting numerical data: the single-cell RNA-seq frontend benchmark (11,872 history items across 64,000 transcripts), the claim of running jobs "up to an order of magnitude larger than before" on `Bridges` and `Stampede` (Figure 3), and the claim of background scheduling of workflows "generating tens of thousands of jobs, while providing instant feedback" lack wall-clock timings, memory/CPU metrics, or quantitative comparisons against prior versions. Additionally, the abstract's claim of "ensuring analyses are completely reproducible" is not reconciled with the introduction of ad hoc scripting in Galaxy Interactive Environments (`Jupyter`) and custom Webhooks until a brief acknowledgment in the closing paragraph.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **CVMFS Stratum 0/1 distribution of 5 TB of reference data, `Bioconda`/`BioContainers` dependency resolution, and `Ansible` playbooks standardize tool execution across public, local, and cloud deployments: [Well Supported].**  
  Figure 2 and lines 72–79 document a clear, verifiable architecture where read-only versioned reference genomes (via CVMFS + Squid HTTP proxies) and immutable software containers (`Docker`/`Singularity` built from `Bioconda`) eliminate administrative drift across federated servers.

* **ToolShed enhancements (`tool profile versions`, automated missing-tool installation for imported workflows, and hot reloading without server restarts) improve backward compatibility and administration: [Well Supported].**  
  These software engineering mechanisms (lines 48–49) directly address long-standing pain points in maintaining multi-version bioinformatics pipelines on production servers.

* **UI and workflow engine optimizations seamlessly scale to single-cell experiments with 11,872 history items and workflows generating tens of thousands of jobs, while XSEDE integration supports jobs "an order of magnitude larger than before": [Moderately Supported].**  
  While the architectural migration from server-side Mako rendering and synchronous workflow queuing to client-side `Vue.js`, `uWSGI`, and asynchronous background scheduling logically improves responsiveness, the manuscript reports zero quantitative benchmark numbers—no response latencies, memory footprints, job scheduling rates (jobs/sec), or before-and-after resource limits in Figure 3 or lines 32–40 and 66.

* **The platform ensures that "analyses are completely reproducible" while integrating Interactive Environments (`Jupyter`) for ad hoc scripting and dynamic UI Webhooks: [Overstated].**  
  In the Abstract (line 6) and Introduction (line 12), complete reproducibility is presented as a core guarantee of the platform. Yet line 50 introduces Galaxy Interactive Environments (`Jupyter`) for "ad hoc scripting" at the beginning and end of analyses, and line 62 introduces Webhooks that trigger custom client- and server-side code. Ad hoc interactive cells executed inside a live `Jupyter` session are not automatically captured in Galaxy's deterministic workflow provenance model—a limitation the authors implicitly concede only in the final sentence of the paper (line 93), which lists *"tighter coupling of Interactive Environments with provenance and reuse"* as future work.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Quantitative Metrics for the 11,872-Item Single-Cell Benchmark and Workflow Scheduler
* **WHY:** Lines 32 and 66 claim major scalability gains on a replicated hematopoietic stem cell dataset (11,872 history items) and workflows generating tens of thousands of jobs, stating that "earlier versions of Galaxy would not have been able to support this analysis," without reporting any timing or resource measurements.
* **WHAT:** Provide a quantitative comparison table of frontend rendering latency, API response time, and backend workflow scheduling throughput across Galaxy release versions.
* **HOW:** Measure and report (1) browser DOM load time and API payload size for loading the 11,872-item history before vs. after the Mako-to-client-side/Vue.js refactoring, and (2) total time required by the background workflow scheduler to enqueue 1,000 and 10,000 collection jobs.

#### 2. Add Numerical Axes and Resource Specifications to the XSEDE Cyberinfrastructure Comparison (Figure 3)
* **WHY:** The caption to Figure 3 (line 40) states that routing jobs to `Bridges` and `Stampede` makes it possible to "run jobs that are up to an order of magnitude larger than before" and "concurrently run more jobs," but no numerical limits (RAM, core counts, wall-clock limits, or monthly XSEDE job volumes) are given in the text.
* **WHAT:** Quantify the exact hardware envelopes and job routing thresholds used on Galaxy Main to dispatch jobs to local Slurm nodes vs. `Jetstream`, `Bridges`, and `Stampede`.
* **HOW:** Specify in the text or a summary table the maximum RAM per job (e.g., local 64–128 GB vs. `Bridges` large-memory nodes up to 3 TB), CPU core allocations, and the proportion of monthly Galaxy Main compute hours executed on XSEDE resources.

#### 3. Clearly Delineate Provenance Guarantees Between Standard Workflows and Interactive Environments
* **WHY:** Claiming that analyses are "completely reproducible" (line 6) while encouraging users to perform data preparation and summarization via ad hoc scripting in `Jupyter` Interactive Environments (line 50) can mislead users into assuming that manual interactive edits inside a notebook are tracked with the same parameter-level provenance as standard Galaxy tools.
* **WHAT & HOW:** Revise lines 50–51 to explicitly explain what is and is not recorded when a user runs a `Jupyter` Interactive Environment (e.g., whether the `.ipynb` notebook file must be manually saved back to the history), and connect this directly to the future roadmap item on line 93 regarding Interactive Environment provenance capture.
