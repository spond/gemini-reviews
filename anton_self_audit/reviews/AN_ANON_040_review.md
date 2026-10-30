# Review of AN_ANON_040

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This perspective manuscript describes the architecture, governance, and interoperability ecosystem of the NHGRI Genomic Data Science Analysis, Visualization, and Informatics Lab-space (AnVIL), a federated cloud platform hosted on the Google Cloud Platform (GCP) under a FedRAMP-certified (NIST-800-53) security perimeter. To address the petabyte-scale bottleneck of copying large human genomics cohorts across institutional clusters (e.g., 73 TB for 3,202 1000 Genomes CRAM files and ~2 PB for 53,831 TOPMed whole genomes), AnVIL inverts the data-sharing model by bringing elastic batch and interactive compute to centralized cloud storage. The platform integrates Gen3 (data commons, Windmill graph database cohort builder, and GA4GH Data Repository Service [DRS] endpoints), Terra (workspace management and Cromwell-executed Workflow Description Language [WDL] batch pipelines), Dockstore (745 WDL containerized workflows with DOI versioning via GA4GH Tool Registry Service [TRS]), and interactive analysis environments including Jupyter Notebooks, RStudio/Bioconductor (`AnVIL` Bioconductor package), and isolated per-user Galaxy deployments orchestrated via Kubernetes and Helm charts. At the time of reporting, AnVIL hosts >280,000 human genomes across >240 cohorts (including CCDG, CMG, eMERGE, GTEx v8, and 1000 Genomes) and interoperates with peer NIH cloud platforms (BDCat, CRDC, GMKF) through the NIH Cloud Platform Interoperability (NCPI) initiative using NIH Research Auth Service (RAS), Portable Format for Bioinformatics (PFB), HL7 FHIR, and pilot semi-automated Data Access Request (DAR) adjudication via the Data Use Oversight System (DUOS) and GA4GH Data Use Ontology (DUO).

As a resource perspective, the manuscript presents a well-engineered, standards-driven architecture that solves major practical barriers in human genomics—specifically enabling isolated, compliant execution of interactive tools like Galaxy and Bioconductor on controlled-access human data without local data egress. The primary limitations lie in the lack of empirical performance distributions behind several headline cost and scalability assertions (such as constant wall-clock execution time and `<$5.00` per-genome GATK4 processing in Note S1), unquantified concordance metrics for the DUOS DAR decision-support algorithm pilot, and an unexplained discrepancy in reported user adoption counts across sections (`>15,000 users` vs. `>1,950 users`). These issues can be resolved through straightforward reporting of empirical benchmark distributions and textual clarification without altering the platform architecture.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Inverting the genomic data-sharing model via a FedRAMP-compliant cloud ecosystem eliminates redundant multi-petabyte data transfers and enables secure analysis of >280,000 genomes: [Well Supported].**  
  The architectural integration of Gen3, Terra, Dockstore, Bioconductor, and Kubernetes-isolated Galaxy instances within a NIST-800-53 boundary directly addresses the bandwidth, storage duplication, and security auditing limitations of institutional HPC clusters while hosting >240 flagship NHGRI and open-access cohorts.

* **Cross-platform federation across NIH data commons (AnVIL, BDCat, CRDC, GMKF) is achievable through GA4GH standards (DRS, TRS, Passports) and HL7 FHIR, though bottlenecked by semantic metadata heterogeneity: [Well Supported].**  
  The manuscript demonstrates concrete cross-platform NCPI use cases (e.g., joint analysis of CPTAC, TCGA, and GTEx; 1000 Genomes with GMKF TARGET Neuroblastoma; PCGC with BDCat cohorts) and candidly documents the real-world semantic obstacles encountered during dashboard harmonization, including inconsistent disease ontology mappings, missing specimen keys, and mismatched measurement units.

* **Germline variant calling (GATK4 on 30x short-read WGS) executes in `<1 day` for `<$5.00` per sample with constant wall-clock time across hundreds or thousands of samples (Note S1): [Moderately Supported].**  
  While cloud elasticity enables massive parallelization, the manuscript provides only a point assertion without empirical distributions of wall-clock runtime, preemptible/spot VM preemption and retry overhead, cloud region quota ceilings, or persistent storage and intermediate file costs when scaling to thousands of concurrent whole genomes.

* **The DUOS decision-support algorithm leveraging GA4GH DUO expedites and standardizes controlled-access Data Access Request (DAR) adjudication: [Moderately Supported].**  
  The conceptual framework of matching ontology-coded dataset consent terms against proposed research terms via GA4GH DUO and Passports/Library Cards is sound, but the pilot is described qualitatively without reporting empirical validation metrics (e.g., agreement rate between the DUOS algorithm's recommendations and human NIH DAC decisions, or reductions in turnaround time).

* **Platform adoption metrics (`>15,000 users` in Architecture vs. `>1,950 users` in Community): [Fragile].**  
  The manuscript states in the *AnVIL system architecture* section that "more than 15,000 users have used the AnVIL," but subsequently states in the *AnVIL community* section that "As of August [YEAR], the AnVIL has supported computation from more than 1,950 users running more than 775 workflows and launching more than 240 workspaces." Presenting both figures without defining the denominator (e.g., unique web portal visitors vs. authenticated Terra compute accounts) creates internal ambiguity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Empirical Runtime and Cost Distributions for the Flagship Workspace Benchmarks
* **WHY:** Point claims that 30x WGS GATK4 germline calling costs `<$5.00` per sample in `<1 day` and maintains constant wall-clock duration across thousands of samples omit variance from spot/preemptible instance revocations, I/O throttling, and cloud quota limits.
* **WHAT:** Supplement the Note S1–S3 workspace descriptions with summary statistics (median, interquartile range, and 95th percentile) of compute cost, storage overhead, and wall-clock time across varying batch sizes.
* **HOW:** Extract historical Cromwell job metadata from Terra for the GATK4 germline workflow across single-sample, 100-sample, and 1,000-sample runs, tabulating CPU-hours, RAM-hours, preemptible retry rates, and total billed GCP cost per sample.

#### 2. Quantify Concordance and Turnaround Metrics from the DUOS / GA4GH DUO Pilot
* **WHY:** Because automated or semi-automated governance of human subjects data requires high fidelity to patient consent constraints, evaluating the DUOS decision-support algorithm requires empirical accuracy metrics against human Data Access Committees (DACs).
* **WHAT:** Report preliminary pilot performance statistics comparing DUOS ontology-based recommendations to final NIH DAC determinations.
* **HOW:** Across the DARs processed in the multi-DAC pilot to date, report the sample size of requests evaluated, the concordance rate (sensitivity and specificity for flagging out-of-bounds research uses), and the median days-to-decision before and after DUOS deployment.

#### 3. Reconcile User Adoption Metrics and Define Activity Tiers
* **WHY:** Unexplained tenfold differences between `>15,000 users` (line 61) and `>1,950 users` (line 101) weaken the precision of the resource report.
* **WHAT:** Explicitly stratify user statistics by interaction tier and synchronize the reporting cutoff date.
* **HOW:** Specify whether the 15,000 figure represents cumulative unique visitors to `anvilproject.org` (or course trainees via GDSCN/Galaxy) and the 1,950 figure represents unique NIH RAS/Terra-authenticated researchers executing billed cloud workflows as of August `[YEAR]`.

#### 4. Document Cross-Cloud Egress Implications for Federated NCPI Analyses
* **WHY:** The manuscript notes that DRS URIs pass references rather than files and that GTEx v8 enjoys free egress via Internet2 mirroring, but cross-cloud co-analysis (e.g., pulling AWS-hosted or external commons data into GCP-hosted Terra workspaces) can incur substantial cloud provider data egress charges.
* **WHAT:** Clarify how data egress fees and network transfer latencies are handled during federated NCPI analyses across heterogeneous cloud backends (GCP vs. AWS).
* **HOW:** Add a brief technical note in the *Interoperability with other cloud platforms* section detailing whether NCPI use cases rely on dual-cloud mirroring, STRIDES-negotiated egress waivers, or local pre-aggregation prior to cross-platform handoff.
