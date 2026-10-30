# Review of AN_ANON_008

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound)  
**Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence presents `Galaxy Cloud`, a cloud-computing deployment framework that couples the open-source `[WORKFLOW_PLATFORM]` (Galaxy) web workbench with `[SOFTWARE_PACKAGE]` (CloudMan) resource orchestration on Amazon Web Services (AWS) and Eucalyptus clouds. To overcome the queue limits, data-transfer bottlenecks, and privacy constraints of shared public Galaxy servers without requiring users to maintain local high-performance computing clusters, `Galaxy Cloud` provisions private, pre-configured Galaxy instances backed by persistent cloud storage volumes (containing pre-built reference genomes, aligner indices, and bioinformatics tools) and elastic worker-node auto-scaling. The authors demonstrate the system using a clinical mitochondrial DNA (mtDNA) heteroplasmy detection workflow across nine individuals from three families (`[14]`, 45 GB of raw sequencing data), showing that dynamic auto-scaling (ranging from 1 to 16 worker nodes) completes the analysis in 6 hours for $20 in compute costs (plus 9 hours and $5 for S3 data upload), matching the 6-hour speed of a fixed 20-node cluster ($50) at the $20 cost of a fixed 5-node cluster (9 hours). All input datasets, heteroplasmy workflows, and step-by-step cloud launch instructions are publicly archived via AWS S3 (`s3.amazonaws.com/heteroplasmy/index.html`) and a dedicated Galaxy Page.

The manuscript is concise, well-balanced, and unusually transparent in both its empirical cost/runtime benchmarking against fixed-size cluster baselines and its candid discussion of cloud limitations (such as reduced cost-effectiveness during interactive trial-and-error workflow design and cloud instance RAM ceilings for de novo assembly, line 64). Only minor technical and reporting clarifications are needed: (1) specifying the exact EC2 instance types, per-hour pricing, and ongoing persistent storage costs (EBS/S3) when compute nodes are terminated; (2) stating the quantitative filtering thresholds (minimum variant frequency, base quality, and per-strand read depth) and concordance with reference `[14]` for the four reported heteroplasmic sites; and (3) qualifying the clinical privacy claim (line 56) by noting the encryption and access-control configurations required when handling clinical sequencing data on public clouds.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Dynamic cluster auto-scaling via `[SOFTWARE_PACKAGE]` optimizes the runtime-versus-cost trade-off compared with static cluster allocations for multi-step NGS workflows: [Well Supported].**  
  The benchmark on 45 GB of mtDNA sequencing data (line 62) compares dynamic auto-scaling (1–16 nodes: 6 hours, $20) directly against two static baselines with auto-scaling disabled (5 nodes: 9 hours, $20; 20 nodes: 6 hours, $50), demonstrating a 33% reduction in wall-clock time at identical cost relative to the small static cluster and a 60% cost reduction at identical wall-clock time relative to the large static cluster.

* **The mtDNA heteroplasmy workflow identifies four heteroplasmic sites across two of the three examined families and is fully reproducible from cloud-hosted artifacts: [Well Supported].**  
  By hosting both the 45 GB raw sequencing dataset on AWS S3 and the exact strand-separated mapping and filtering workflow on a public Galaxy Page (line 60), the authors enable exact replication of the four heteroplasmy calls (`[14]`).

* **Releasing compute resources when an analysis finishes preserves user data and instance state while eliminating compute charges: [Moderately Supported].**  
  While terminating EC2 worker and master compute instances stops hourly compute billing and preserves user datasets on persistent storage volumes (lines 52, 54, 62), the cost discussion does not mention that preserved Elastic Block Store (EBS) volumes and S3 buckets continue to accrue monthly storage charges while the instance is dormant, nor does it report the specific EC2 instance types used in the benchmark.

* **Clinical samples with strict privacy concerns "can be analyzed on a secure public or private cloud resource" using `Galaxy Cloud`: [Moderately Supported].**  
  In contrast to uploading patient reads to a shared multi-tenant academic web server, a dedicated cloud instance isolates tenant compute and storage. However, running default cloud instances on a public cloud provider (AWS) does not by itself guarantee clinical data compliance (e.g., HIPAA/IRB protections) unless HTTPS/TLS encryption in transit, EBS/S3 encryption at rest, and restricted security-group authentication are explicitly enabled.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Exact EC2 Instance Types, Instance-Hours, and Persistent Storage Retention Costs
* **WHY:** Dollar figures alone ($20 for compute, $5 for transfer, line 62) depend on provider pricing tiers at the time of execution and cannot be directly translated into computational work (CPU-hours / RAM-hours) by future readers. Furthermore, users preserving inactive instances on AWS need to know the ongoing monthly storage cost of their retained EBS/S3 volumes.
* **WHAT:** Specify the AWS EC2 instance type(s) (e.g., `m1.large` or `c1.xlarge` with CPU core and RAM counts), total instance-hours consumed under the 1–16 node auto-scaling run vs. the 5-node and 20-node static runs, and the monthly EBS/S3 storage rate for preserving the 45 GB dataset between sessions.
* **HOW:** Update the benchmark paragraph (line 62) to include parenthetical hardware specifications (instance type, vCPUs, RAM per node, and total node-hours) alongside the dollar costs, and add one sentence noting the monthly storage cost ($/GB-month) when compute nodes are terminated.

#### 2. State the Numerical Thresholds and Validation Concordance for the Heteroplasmy Case Study
* **WHY:** Line 58 states that the workflow identifies *"allelic variants above a certain frequency supported by high quality reads on both strands,"* yielding four heteroplasmic sites across two families, without stating the numerical thresholds or whether these four sites match the validated heteroplasmies reported in study `[14]`.
* **WHAT:** State the exact Phred base quality threshold, minimum minor allele frequency cutoff, and per-strand coverage requirement in line 58, and confirm concordance with `[14]`.
* **HOW:** Revise the final two sentences of line 58 to specify the exact parameter cutoffs (e.g., Phred score $\ge Q$, minor allele frequency $\ge f\%$, and $\ge k$ reads per forward/reverse strand) and note that the four identified sites reproduce the findings of `[14]`.

#### 3. Qualify the Clinical Privacy Statement with Required Cloud Security Controls
* **WHY:** Line 56 cites clinical sample privacy as Motivation #1 for `Galaxy Cloud`. Biomedical users unfamiliar with cloud administration may assume a freshly launched public cloud instance is encrypted by default.
* **WHAT:** Briefly note that analyzing sensitive clinical samples on a public cloud requires enabling encrypted storage and secure network access controls.
* **HOW:** Add a clause to Motivation #1 (line 56) or Supplemental Notes clarifying that for protected clinical samples on public clouds, users should enable HTTPS access, encrypted storage volumes, and institutional cloud compliance agreements, or deploy `Galaxy Cloud` on an on-premise private cloud (e.g., Eucalyptus).

#### 4. Minor Editorial Corrections
* **WHY:** Three minor grammatical typos appear in the main text.
* **WHAT & HOW:**
  1. *Line 52:* Change `"is installed an available for immediate use"` to `"is installed and available for immediate use"`.
  2. *Line 56:* Change `"4) There is currently has no commonly accepted approach"` to `"4) There is currently no commonly accepted approach"`.
  3. *Line 66:* Change `"Galaxy Cloud instance are owned"` to `"Galaxy Cloud instances are owned"`.
