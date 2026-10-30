# Review of AN_ANON_040

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.0 / 10.0** (Exemplary) | **Scientific Core Score:** **7.1 / 8.0**  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This Perspective presents the architecture, governance model, dataset ecosystem, and cross-platform interoperability strategy of the NHGRI Genomic Data Science Analysis, Visualization, and Informatics Lab-space (AnVIL; `https://anvilproject.org`). To overcome the storage redundancy, bandwidth bottlenecks, and provenance fragmentation of copying petabyte-scale genomic cohorts across local institutional clusters, AnVIL implements an inverted cloud model on a FedRAMP-certified, NIST-800-53-compliant Google Cloud Platform (GCP) environment. The platform integrates Gen3 for graph-based metadata querying and cohort construction, Terra and Cromwell for batch Workflow Description Language (WDL) execution, Dockstore for containerized workflow distribution, and RStudio/Bioconductor, Jupyter Notebooks, and per-user Kubernetes-isolated `[SOFTWARE]` deployments for interactive analysis. At the time of reporting, AnVIL hosts >280,000 human genomes across >240 controlled- and open-access cohorts (including CCDG, CMG, eMERGE, GTEx v8, 1000 Genomes high-coverage WGS, and Telomere-to-Telomere CHM13 resources), interoperates with peer NIH cloud commons (BioData Catalyst, Cancer Research Data Commons, and Gabriella Miller Kids First) via GA4GH standards (DRS, TRS, Passports/RAS, DUO/DUOS, and HL7 FHIR), and provides three executable showcase workspaces (Notes S1–S3).

The manuscript provides a balanced, technically transparent overview of a major community genomics infrastructure. A particular strength is its candid discussion of current operational bottlenecks—including phenotypic metadata inconsistencies across cohorts, lack of automated cloud budget "bumpers" to prevent unexpected user expenditure, and the transitional reality of hybrid local/cloud workflows. The primary areas where the manuscript can be strengthened are clarifying the scaling and preemptible-VM assumptions behind the Note S1 GATK4 cost/wall-clock benchmark, addressing cross-cloud egress and latency when resolving GA4GH DRS URIs across different commercial cloud providers (e.g., AWS vs. GCP), and reconciling two different user-count statistics reported in the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Unified FedRAMP-compliant cloud architecture integrating batch (Terra/WDL/Dockstore), metadata (Gen3), and isolated interactive (`[SOFTWARE]`, Bioconductor, Jupyter) environments for protected human genomics data: [Well Supported].**  
  The architectural integration is thoroughly documented and operationalized across >240 cohorts. In particular, deploying isolated per-user `[SOFTWARE]` instances on Kubernetes via Helm charts within Terra workspaces solves a long-standing security barrier, enabling graphical workflow execution on dbGaP controlled-access human datasets.

* **GA4GH and NIH Cloud Platform Interoperability (NCPI) federated analysis across NIH cloud commons: [Moderately Supported].**  
  The implementation of GA4GH DRS, TRS, RAS/Passports, PFB handoffs, and FHIR data normalization is well documented through concrete multi-platform use cases (e.g., CPTAC/TCGA on CRDC with GTEx on AnVIL; 1000 Genomes on AnVIL with TARGET on GMKF). However, the statement that DRS enables cloud-agnostic access "because DRS Uniform Resource Identifiers (URIs), not actual data files, are passed between platforms" understates the physical data-plane constraint: when an analysis job executing on GCP (AnVIL) reads a multi-terabyte BAM/CRAM file hosted on AWS S3 (e.g., in another NCPI commons) via its DRS URI, the raw byte stream must still cross commercial cloud boundaries, incurring cloud egress charges and network latency unless compute is dispatched to the host cloud via WES/TES or the data are mirrored.

* **Linear cost scaling (<$5.00/sample) and constant wall-clock time (<1 day) for GATK4 WGS variant calling across hundreds to thousands of samples (Note S1): [Moderately Supported].**  
  For per-sample read alignment (`BWA-MEM`) and single-sample `HaplotypeCaller` GVCF generation, embarrassingly parallel cloud execution achieves near-constant wall-clock time and linear cost scaling. However, the text does not specify whether the <$5.00/sample figure depends on spot/preemptible instances, how GCP regional CPU/quota limits affect thousand-sample bursts, or how downstream joint cohort genotyping (`GenomicsDBImport` / `GenotypeGVCFs`), which scales super-linearly with cohort size and allele count, is factored into the cost model.

* **Streamlined controlled-access governance via DUOS, GA4GH DUO, and Library Card Passports: [Well Supported].**  
  The manuscript appropriately frames the Broad Institute's Data Use Oversight System (DUOS) and the GA4GH Passport "Library Card" as active pilots with NIH Data Access Committees (DACs) designed to semi-automate matching between consent ontology terms and Data Access Requests (DARs).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Specify Preemptible VM Assumptions and Joint-Genotyping Scaling in the Note S1 GATK4 Benchmark
* **WHY:** Readers budgeting population-scale WGS studies need to know whether the cited "<1 day and <$5.00 per sample" applies only to single-sample alignment + GVCF calling on preemptible VMs, or includes cohort-wide joint genotyping.
* **WHAT:** Expand the Note S1 summary in the main text to break down the parameters of the GATK4 benchmark.
* **HOW:** State (1) the exact workflow steps included in the <$5.00/sample figure (e.g., `BWA-MEM`, `MarkDuplicates`, `BaseRecalibrator`, and `HaplotypeCaller` in `-ERC GVCF` mode), (2) the fraction of tasks run on GCP preemptible/spot nodes and typical preemption retry rates at scale, and (3) the separate compute cost and wall-clock scaling of joint calling (`GenomicsDBImport` / `GenotypeGVCFs` or `Hail`) across $10^3$–$10^5$ samples.

#### 2. Clarify Cross-Cloud Data Egress and Compute Placement in DRS/NCPI Federated Queries
* **WHY:** Passing a GA4GH DRS URI between platforms standardizes metadata resolution, but dereferencing that URI during workflow execution still moves data across clouds if the storage bucket and compute engine reside on different commercial cloud providers (e.g., AWS S3 vs. Google Cloud Storage).
* **WHAT:** Clarify the distinction between control-plane URI resolution and data-plane byte transfer in the "Interoperability with other cloud platforms" section.
* **HOW:** Add a brief explanation noting that while DRS abstracts cloud storage locations, cross-cloud execution of large raw read files (BAM/CRAM) across AWS- and GCP-backed NCPI platforms still faces cross-provider egress fees and bandwidth limits unless workflows extract compact region slices, operate on summary/derived matrices, or dispatch compute directly to the storage host cloud via GA4GH WES/TES.

#### 3. Reconcile the Reported User Statistics Across Sections
* **WHY:** Under "AnVIL system architecture," the text states "Already more than 15,000 users have used the AnVIL," whereas under "AnVIL community" it states "As of August [YEAR], the AnVIL has supported computation from more than 1,950 users running more than 775 workflows and launching more than 240 workspaces."
* **WHAT & HOW:** Define both numbers explicitly (e.g., clarifying whether >15,000 represents unique web portal visitors or includes educational workshop accounts as of a later date, while >1,950 represents authenticated Terra compute users as of August [YEAR]).

#### 4. Minor Editorial Corrections
* **WHY:** A few typographical errors appear in acronyms and tool names.
* **WHAT & HOW:**
  * In "Interoperability with other cloud platforms," correct `"GMFK"` (two occurrences) to `"GMKF"` (Gabriella Miller Kids First) and `"tAnVIL"` to `"AnVIL"`.
  * In "AnVIL system architecture" (Bioconductor paragraph), correct `"Jupiter Notebooks"` to `"Jupyter Notebooks"`.
