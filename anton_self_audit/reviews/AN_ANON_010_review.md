# Review of AN_ANON_010

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript proposes a modular reference architecture and open-source implementation (`[SOFTWARE_PACKAGE]`, deployed for the `[AUTHOR]` bioinformatics platform on Amazon Web Services EC2, EBS, and S3) that bridges Infrastructure-as-a-Service (IaaS) cloud primitives with Software-as-a-Service (SaaS) end-user usability without requiring source-code modifications to the hosted scientific application. The architecture decouples cloud deployment into three distinct layers: (1) a minimal, generic base virtual machine image (AMI) containing only the operating system, Python, an AMQP message broker (RabbitMQ), user accounts, and a bootstrap contextualization hook; (2) an external persistent data repository (S3) storing boot-time contextualization scripts, cluster configuration manifests, and the `[SOFTWARE_PACKAGE]` controller; and (3) separate persistent block-storage volumes/snapshots (EBS) partitioned into read-only application/tool binaries, read-only reference genome indexes, and persistent read-write user data (including the PostgreSQL database), exported across master and worker nodes via NFS and scheduled via Sun Grid Engine (SGE). Source code for the implementation is publicly available on Bitbucket (`bitbucket.org/[AUTHOR]/[SOFTWARE_PACKAGE]/`).

The architectural design is well-motivated and cleanly solves a major operational weakness of monolithic "fat" virtual machine images by allowing application binaries, reference genome indexes, and boot scripts to be updated and versioned independently via EBS snapshots and S3 contextualization while preserving user data across transient instances. However, as a systems and cloud engineering manuscript, its primary limitation is the complete absence of quantitative empirical evaluation: no measurements of instance contextualization and boot latency, EBS snapshot attachment overhead, NFS shared-storage I/O scaling across worker nodes, SGE cluster startup time, or quantitative comparisons against monolithic VM images are presented. In addition, architectural failure modes—most notably single-master NFS I/O contention under data-intensive bioinformatics workloads and potential schema/version incompatibilities when mixing independent snapshots—are not empirically tested or bounded. Adding concrete performance benchmarks and addressing shared-filesystem bottlenecks would substantially strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Separating the base machine image, S3 contextualization repository, and logical EBS storage volumes enables unmodified applications to run with persistent state on transient IaaS instances: [Well Supported].**  
  Sections 2.1, 3.1, and 4 provide a coherent, end-to-end systems design (Figures 2–5) demonstrating how mounting read-only EBS snapshots for `[AUTHOR]` binaries and reference indexes alongside a persistent read-write user EBS volume (housing PostgreSQL and user files) over NFS presents a standard POSIX filesystem to the unmodified `[AUTHOR]` application.

* **Decoupling logical storage snapshots from the machine image simplifies managed software updates without disrupting user routines: [Well Supported].**  
  Unlike monolithic "fat" VM images (Nishimura et al. `[26]`, Krsul et al. `[27]`), publishing updated EBS snapshots for tools or reference indexes and updating the S3 contextualization manifest allows new cluster instantiations to mount updated read-only volumes automatically while releasing them upon termination to minimize storage costs (Section 3.2, Figure 3).

* **The framework delivers a functional cluster "in a matter of minutes" with "minimal overhead" and scales transparently across worker nodes: [Fragile].**  
  Although these performance claims appear in the Summary, Section 4 (line 151), and Conclusions, the manuscript contains zero quantitative benchmarks—no tables, plots, or timing measurements reporting master/worker boot times, EBS volume creation and mount latency, S3 contextualization time, or throughput scaling across 1 to $N$ worker nodes.

* **Runtime composition of multiple snapshot versions provides reliable application and dataset versioning for existing user data: [Moderately Supported].**  
  While Section 3.3 (Figure 4) describes how users can either pin previous snapshot versions or upgrade to newer snapshots, the manuscript acknowledges (line 107) that no component dependency harness exists yet. If a user mounts an updated `[AUTHOR]` application snapshot whose ORM expects a newer PostgreSQL database schema than the one stored on their persistent user-data EBS volume, or mismatches tool binaries and reference index formats (e.g., BWA index version changes), runtime failures can occur unless schema migration and version constraints are enforced.

* **The architecture is portable across diverse IaaS providers (AWS, Eucalyptus, OpenNebula, Nimbus): [Moderately Supported].**  
  Relying on generic IaaS primitives (VM images, block storage, object store) promotes conceptual portability, and Eucalyptus/OpenNebula/Nimbus support AWS-compatible EC2/S3/EBS APIs; however, the implementation in Section 4 is only verified on AWS, and provider-specific differences in snapshot semantics (e.g., copy-on-write latency from public snapshots) are not empirically tested on non-AWS clouds.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add Quantitative Benchmarks of Contextualization Latency and Cluster Startup Overhead
* **WHY:** A systems paper claiming "minimal overhead" and deployment "in a matter of minutes" requires empirical timing measurements to validate its engineering trade-offs against traditional "fat image" deployments.
* **WHAT:** Measure and report a breakdown of instantiation latency across each step of the 9-step boot sequence in Section 4 (Figure 5) and compare total startup time against a monolithic AMI containing the full software stack.
* **HOW:** Run 10 repeated cluster instantiations on AWS EC2 and report the mean and standard deviation (in seconds) for: (1) base AMI boot to RabbitMQ startup, (2) S3 `[SOFTWARE_PACKAGE]` download and contextualization, (3) EBS volume creation and attachment from snapshots for tools and reference indexes, (4) NFS export and SGE configuration, (5) PostgreSQL initialization on the user volume, and (6) worker node join latency as cluster size scales from 1 to 16 nodes.

#### 2. Evaluate and Mitigate Single-Master NFS I/O Contention Under Concurrent Genomic Workloads
* **WHY:** In Section 4 (lines 133–135), the master instance attaches the EBS volumes for tools, reference indexes, and user data and exports them to all worker instances over a single Network File System (NFS) server. In bioinformatics workflows (such as concurrent short-read mapping or variant calling across many workers), simultaneous reads of multi-gigabyte reference indexes and heavy writes of intermediate SAM/BAM files over a single virtualized NFS master frequently saturate network bandwidth and EBS IOPS.
* **WHAT:** Quantify the NFS I/O scaling limit as worker counts increase, and describe architectural mitigations (such as mounting read-only reference index EBS snapshots directly onto each worker node rather than exporting indexes over NFS).
* **HOW:** Because reference index snapshots are read-only (Section 3.1, line 87), update or document how `[SOFTWARE_PACKAGE]` can attach a local read-only EBS index snapshot (or cache indexes on local ephemeral instance storage) on each worker node at boot time, reserving NFS strictly for shared job scripts and final outputs, and benchmark job runtime across 1, 4, 8, and 16 workers.

#### 3. Specify How Database Schema Migrations and Snapshot Compatibility Are Handled Across Updates
* **WHY:** Because the PostgreSQL database resides on the persistent user-data EBS volume (Section 4, line 143) while the `[AUTHOR]` application resides on an independently updated read-only EBS snapshot (line 133), upgrading the application snapshot while re-attaching an older user-data volume can cause schema mismatches.
* **WHAT:** Explain how `[SOFTWARE_PACKAGE]` handles database schema versioning and tool-to-index compatibility when a user boots an existing data volume against a newly published application snapshot.
* **HOW:** Add a paragraph in Section 3.3 or Section 4 detailing whether the boot contextualization script automatically executes `[AUTHOR]` database schema migration scripts (`manage_db.sh upgrade`) upon mounting an older user-data volume and how snapshot compatibility metadata is recorded in the user's S3 manifest.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor typographical errors appear in the manuscript.
* **WHAT & HOW:**
  1. **Section 1 (line 36):** Change `"This makes it is possible for a user"` to `"This makes it possible for a user"`.
  2. **Section 4 (line 112):** Correct the URL typo `http://usegalay.org` to `http://[WORKFLOW_SERVER]` (or `http://[WORKFLOW_PLATFORM]` per blinding conventions).
  3. **Section 4 (line 151):** Change `"without needing to posses any technical knowledge"` to `"without needing to possess any technical knowledge"`.
  4. **Figure 5 Caption (line 125):** Step `(7)` is skipped in the numbered sequence (`...(6) and [SOFTWARE_PACKAGE] configures and starts the [AUTHOR] application. The user then specifies the desired size of the cluster (8)...`). Insert `(7)` at the appropriate clause to match Figure 5.
