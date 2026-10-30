# Review of AN_ANON_008

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence introduces `[SOFTWARE]` Cloud, an on-demand cloud deployment of the `[SOFTWARE]` web-based bioinformatics platform managed by `[SOFTWARE_PACKAGE]` on Amazon Web Services (AWS) and compatible with Eucalyptus. `[SOFTWARE]` Cloud allows researchers to launch private, customizable `[SOFTWARE]` instances preloaded with reference genomes, aligner indexes, and analysis tools, backed by elastic cluster auto-scaling and persistent storage across sessions. To demonstrate its utility, the authors analyze 45 GB of mitochondrial DNA (mtDNA) next-generation sequencing data from nine individuals across three families to detect mitochondrial heteroplasmy. Uploading the 45 GB dataset to AWS S3 took 9 hours (1.5 MB/s, $5), and executing a strand-aware variant-calling workflow on an auto-scaled cluster of 1–16 nodes completed in ~6 hours for $20—matching the 6-hour runtime of a fixed 20-node cluster ($50) at the $20 cost of a slower 5-node cluster (9 hours). The workflow identified four heteroplasmic sites across two of the three families, and all input datasets and workflows are publicly archived on AWS S3 and `[WORKFLOW_PLATFORM]`.

The letter presents a practical, reproducible cloud computing solution for laboratories lacking local high-performance computing infrastructure, and the open availability of the 45 GB benchmark dataset and exact workflow is commendable. However, several technical and biological details needed to evaluate the case study and cloud performance claims are omitted from the main text: (1) the heteroplasmy calling criteria (minimum minor allele frequency threshold, per-strand read depth, base/mapping quality cutoffs, and control for nuclear mitochondrial DNA segments [NUMTs] or PCR/sequencing error) and any orthogonal validation of the four reported heteroplasmic sites are not stated; (2) the auto-scaling runtime and cost comparison reports single point estimates without specifying the AWS EC2 instance types or run-to-run variability; and (3) the claim that clinical samples with strict privacy concerns can be safely analyzed on a public cloud is presented without detailing encryption or access-control safeguards. These points can be addressed through concise textual additions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`[SOFTWARE]` Cloud coupled with `[SOFTWARE_PACKAGE]` enables browser-based instantiation and persistent management of private elastic `[SOFTWARE]` clusters on AWS: [Well Supported].**  
  The architectural integration of `[SOFTWARE]` with `[SOFTWARE_PACKAGE]` for dynamic compute node provisioning, persistent EBS/S3 storage of tools, reference indexes, and user data, and complete workflow provenance is clearly demonstrated and backed by live public images and documentation (`[WORKFLOW_PLATFORM]/cloud`).

* **Auto-scaling (1–16 nodes) achieves the 6-hour runtime of a 20-node fixed cluster at the $20 cost of a 5-node fixed cluster on the 45 GB mtDNA workflow: [Moderately Supported].**  
  The empirical comparison (auto-scaled 1–16 nodes: 6 h, $20; fixed 5 nodes: 9 h, $20; fixed 20 nodes: 6 h, $50) illustrates how elasticity avoids paying for idle nodes during serial workflow stages. However, the main text does not specify which EC2 instance type (e.g., `m1.large`, `c1.xlarge`) was used, whether EBS storage/I/O fees were included in the $20 total, or whether timings reflect single runs or averages across replicates.

* **The `[SOFTWARE]` Cloud workflow accurately identifies four mtDNA heteroplasmic sites across two of the three studied families: [Fragile].**  
  While the full workflow is shared online (`s3.amazonaws.com/heteroplasmy/index.html`), the letter itself omits the quantitative thresholds used to distinguish true mtDNA heteroplasmy from sequencing errors, strand bias, or paralogous nuclear mitochondrial pseudogenes (NUMTs), and does not state whether the four sites were validated by maternal transmission within the three-family pedigrees or by orthogonal assays.

* **`[SOFTWARE]` Cloud resolves clinical data privacy concerns by running on a "secure public or private cloud resource": [Moderately Supported].**  
  Although running a private instance avoids uploading sensitive clinical reads to a multi-tenant public `[SOFTWARE]` web server, deploying on a public cloud (AWS) still requires specific technical safeguards (encrypted EBS volumes, S3 server-side encryption, HTTPS/SSL data transfer, and restricted security group ports) that are not described in the text.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Specify the Quantitative Thresholds and Validation Support for the Four mtDNA Heteroplasmic Sites
* **WHY:** As the authors note, heteroplasmy detection is notorious for false positives arising from sequencing errors, PCR amplification artifacts, and co-amplified or mis-mapped NUMTs. Reporting "four heteroplasmic sites in two of the three examined families" without stating the minor allele frequency cutoff, coverage depth, or validation status leaves the biological case study incomplete.
* **WHAT:** State the exact filtering thresholds implemented in the workflow and summarize the read depth, minor allele frequencies, and pedigree concordance of the four detected sites.
* **HOW:** Add 2–3 sentences to paragraph 7 (line 58) specifying the minimum Phred base quality, minimum coverage per strand, minor allele frequency threshold (e.g., $\ge 1\%$ or $\ge 2\%$ on both forward and reverse strands), and whether the four calls were consistent with maternal inheritance across the three families `[14]`.

#### 2. Document AWS EC2 Instance Types and Cost Breakdown for the Auto-Scaling Benchmark
* **WHY:** Cloud runtimes (6 h vs. 9 h) and dollar costs ($20 vs. $50) cannot be interpreted or reproduced over time without knowing the exact hardware configuration (CPU cores, RAM, instance family) and hourly unit price used in the benchmark.
* **WHAT:** Report the EC2 instance type(s) allocated for the master and worker nodes and clarify what cost components are included in the $5 transfer and $20–$50 compute figures.
* **HOW:** In paragraph 9 (line 62), insert the specific AWS instance type (e.g., `m1.large` at $\$X/\text{hour}$) and state whether the $20 figure includes EBS volume provisioning and S3 storage costs alongside EC2 instance hours.

#### 3. Clarify Security and Encryption Mechanisms for Clinical Samples on Public Clouds
* **WHY:** Motivation (1) for `[SOFTWARE]` Cloud (line 56) highlights clinical samples with strict privacy requirements, which readers may interpret as implying out-of-the-box regulatory (e.g., HIPAA) compliance on public AWS.
* **WHAT:** Explicitly state what security controls `[SOFTWARE]` Cloud configures by default (e.g., SSH key-pair authentication, firewall security groups) and what additional steps (SSL/TLS, disk encryption, institutional Business Associate Agreements) users must enable for protected health information.
* **HOW:** Add a qualifying sentence in paragraph 6 or 10 noting that while `[SOFTWARE]` Cloud isolates compute and storage to the user's own AWS account, analyzing regulated clinical data on public clouds requires enabling encrypted storage volumes and encrypted data transfer.

#### 4. Technical and Editorial Cleanup
* **WHY:** Two minor grammatical errors appear in the main text.
* **WHAT & HOW:**
  1. **Paragraph 4 (line 52):** Change `"is installed an available for immediate use"` to `"is installed and available for immediate use"`.
  2. **Paragraph 6 (line 56):** Change `"4) There is currently has no commonly accepted approach"` to `"4) There is currently no commonly accepted approach"`.
