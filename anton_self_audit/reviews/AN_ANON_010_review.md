# Review of AN_ANON_010

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.2 / 10.0** (Strong / Sound)  
**Scientific Core Score:** **5.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript proposes a modular reference architecture and open-source orchestration framework (`[SOFTWARE_PACKAGE]` / CloudMan) for deploying scientific applications onto Infrastructure-as-a-Service (IaaS) clouds while providing Software-as-a-Service (SaaS) usability without modifying the hosted application. To avoid the maintenance and versioning bottlenecks of monolithic ("fat") virtual machine images, the architecture decouples a cloud deployment into three low-level IaaS primitives (Section 2.1, Figure 2): (1) a minimal base Machine Image containing only the operating system, basic daemon accounts, a RabbitMQ (AMQP) message broker, and a bootstrap hook; (2) an external Persistent Data Repository (e.g., an AWS S3 bucket) storing runtime contextualization scripts and cluster manifests; and (3) modular Persistent Storage Resources (e.g., AWS Elastic Block Store [EBS] volumes instantiated from public snapshots and shared across worker nodes via NFS) partitioned into three logical units: read-only application/tool binaries, read-only reference datasets/indices, and persistent read-write user data (including the PostgreSQL database). Upon cluster termination, the read-only tool and index volumes are deleted to save storage costs while the user data volume and S3 manifest are retained for exact re-instantiation. Source code is publicly available on Bitbucket (`bitbucket.org/[AUTHOR]/[SOFTWARE_PACKAGE]/`).

The architectural decomposition—separating immutable, snapshot-backed application binaries and reference indices from mutable user data and boot-time S3 contextualization—is clean, practical, and directly solves the "fat image" update problem for cloud bioinformatics platforms. However, the manuscript is purely qualitative and contains **no quantitative benchmarks or empirical measurements** to substantiate its systems performance claims. Specifically, the paper provides no timing measurements for cluster instantiation and EBS snapshot attachment ("in a matter of minutes," line 151; "nearly instantaneously," line 69), no evaluation of NFS and EBS cold-snapshot I/O bottlenecks as worker node counts scale, and no formal mechanism for handling schema/dependency incompatibilities when an updated application snapshot is mounted against an older persistent user database volume (acknowledged as future work in Section 3.3, line 107). Adding a concise quantitative benchmark of boot latency, storage footprint savings, and NFS/worker scaling would substantially strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Decomposing a cloud deployment into a minimal base image, an S3-hosted contextualization repository, and logical EBS volume snapshots eliminates the need to rebuild monolithic machine images for software or reference-data updates: [Well Supported].**  
  Sections 2.1 and 3.1–3.3 clearly demonstrate how separating the deployment into three orthogonal storage volumes (tools, reference indices, and user data) allows developers to publish updated tool or reference snapshots and update the central contextualization manifest without touching the base AMI or overwriting user data.

* **Deleting read-only application and reference-index volumes upon cluster termination while retaining only the user data volume and S3 manifest reduces ongoing storage overhead while preserving full state persistence: [Well Supported].**  
  Because the tool and reference genome volumes are mounted strictly as read-only filesystems derived from public snapshots, destroying those volumes when the cluster is stopped and re-instantiating them from their recorded snapshot IDs at next boot avoids billing every user for redundant terabytes of static reference genomes between runs.

* **The framework instantiates a complete cluster "in a matter of minutes" (line 151) with external storage attachment happening "nearly instantaneously" (line 69) and "minimal overhead" (line 27): [Fragile].**  
  While plausible, the manuscript presents zero empirical timing data, tables, or plots to support these performance claims:
  1. *Unmeasured instantiation and EBS snapshot lazy-loading latency:* No wall-clock measurements are reported for the 9-step boot sequence in Section 4 (lines 129–146: VM launch, RabbitMQ start, S3 code fetch, EBS volume creation from snapshots and attachment, NFS export, SGE unpacking, user volume formatting, PostgreSQL initialization, and application startup). Furthermore, on AWS EC2, EBS volumes instantiated from S3-backed snapshots experience high first-read latency ("cold snapshot penalty") when large reference genome indices are first read by worker nodes.
  2. *Unmeasured NFS master-node I/O scaling:* In Section 4 (lines 118, 135), the master instance exports the attached EBS volumes to all worker instances over a single Network File System (NFS) server. No throughput or scaling tests are presented to show how many concurrent worker nodes can execute data-intensive genomic tools before saturating the master instance's network interface and EBS bandwidth.

* **Existing applications can be deployed into the framework "without any modifications" (lines 27, 42) while transparently supporting independent component updates and versioning (Sections 3.2–3.3): [Moderately Supported].**  
  This claim holds only for applications that cleanly separate read-only code/configuration directories from a single read-write user data directory. Moreover, in the `[AUTHOR]` implementation (Section 4, lines 120 and 143), the application code resides on the read-only application snapshot while the PostgreSQL database resides on the persistent read-write user volume. If a user upgrades their cluster to a newer application snapshot whose code expects an updated PostgreSQL database schema—or if updated tool wrappers depend on newer reference index formats—mounting the new application snapshot against the old user volume will fail unless automated database schema migrations and cross-volume dependency constraints are enforced (as the authors candidly note is not yet implemented in Section 3.3, line 107).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Quantitative Benchmark of Cluster Instantiation Latency and Storage Cost Savings
* **WHY:** A systems architecture paper claiming rapid deployment ("in a matter of minutes," line 151; "nearly instantaneously," line 69) and reduced storage footprint (line 87) needs empirical measurements comparing the proposed modular contextualization model against a monolithic ("fat") AMI baseline.
* **WHAT:** Measure and report a breakdown of wall-clock startup latency across steps (1)–(10) of Figure 5 (across $N = 10$ independent launches), alongside a comparison of dormant storage footprint (GB retained on EBS when terminated) with and without read-only volume deletion.
* **HOW:** Instrument the `[SOFTWARE_PACKAGE]` contextualization log on AWS EC2 to record timestamps for each boot phase (AMI boot $\to$ S3 fetch $\to$ EBS snapshot-to-volume creation and attachment $\to$ NFS/SGE configuration $\to$ PostgreSQL/application ready), and add a summary table in Section 4 reporting the mean $\pm$ SD duration of each phase and the exact GB of read-only tool/index snapshots spared from persistent billing upon termination.

#### 2. Evaluate Master-Node NFS I/O Scaling and First-Access EBS Snapshot Throughput Across Worker Counts
* **WHY:** Sharing all application binaries, reference genome indices, and user data from EBS volumes attached to a single master node over NFS (lines 85, 135) creates a central I/O bottleneck as worker nodes scale up, compounded by AWS EBS lazy-loading from snapshots on initial reads.
* **WHAT:** Benchmark a representative I/O- and compute-intensive workflow (e.g., short-read alignment against a reference genome index stored on the read-only index volume) across increasing worker cluster sizes (e.g., 1, 4, 8, and 16 worker nodes) to characterize parallel efficiency and NFS saturation.
* **HOW:** Run an identical batch of alignment jobs on 1, 4, 8, and 16 worker instances managed by `[SOFTWARE_PACKAGE]` SGE, comparing first-run runtime (cold EBS snapshot blocks) against second-run runtime (warmed EBS blocks) to document both scaling behavior and snapshot warming effects.

#### 3. Address Database Schema Migration and Cross-Snapshot Compatibility Between Logical Units
* **WHY:** Storing PostgreSQL on the persistent user data volume (line 143) while swapping the read-only `[AUTHOR]` application volume via new snapshots (Section 3.2) creates a state-coupling boundary whenever a new application version introduces database schema changes or updated tool-data table schemas.
* **WHAT:** Document how `[SOFTWARE_PACKAGE]` handles PostgreSQL schema migrations and snapshot compatibility when an existing user data volume is mounted with an updated application snapshot.
* **HOW:** In Section 4 (lines 143–145), explain whether `[SOFTWARE_PACKAGE]` invokes the application's database migration script (`manage_db.sh upgrade`) automatically before starting the web server when an application snapshot version changes, and specify how snapshot compatibility pairs `(app_snapshot_id, index_snapshot_id)` are validated in the S3 manifest.

#### 4. Technical and Editorial Corrections
* **WHY:** Several URL, figure-numbering, and spelling errors appear in the manuscript text.
* **WHAT & HOW:**
  1. *Broken Public Server URL (Section 4, line 112):* `http://usegalay.org` is missing the letter `x`; correct to `http://usegalaxy.org` (or the blinded placeholder).
  2. *Missing Step (7) in Figure 5 Caption (Section 4, line 125):* The caption text lists steps `(1)` through `(6)` and then jumps directly to `(8)` (`"User provides needed configuration information through [SOFTWARE_PACKAGE]'s web interface (6) and [SOFTWARE_PACKAGE] configures and starts the [AUTHOR] application. The user then specifies the desired size of the cluster (8)..."`). Insert `(7)` after `"starts the [AUTHOR] application"`.
  3. *Grammar Typo (Section 1, line 36):* Change `"This makes it is possible for a user"` to `"This makes it possible for a user"`.
  4. *Spelling Typo (Section 4, line 151):* Change `"without needing to posses any technical knowledge"` to `"without needing to possess any technical knowledge"`.
