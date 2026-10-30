# Review of AN_ANON_046

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This software architecture commentary describes the design principles and implementation of `[SOFTWARE]`, an open-source web-based "application meta-server" aimed at overcoming format heterogeneity and lack of workflow transparency in translational genomic research. Rather than constructing a monolithic application or relying on tightly coupled semantic web-service protocols (such as BioMoby or Taverna), `[SOFTWARE]` wraps arbitrary non-interactive command-line executables (compiled binaries or R, Python, Perl, shell, and SAS scripts) using declarative XML tool descriptors that specify input parameters, validation rules, command syntax, documentation, and automated functional tests. External genomic databases (such as the UCSC Table Browser and BioMart) integrate via a lightweight URL callback mechanism that deposits user-selected tables directly into persistent `[SOFTWARE]` workspace histories. The authors recount the migration of the codebase from Perl to Python, describe how the server scales from a zero-configuration local daemon (built-in HTTP server, embedded database, local threads) to a production cluster architecture (remote web server, PostgreSQL/MySQL backend, HPC job offloading), and note their use of Subversion, Trac (`http://g2.trac.bx.psu.edu`), and daily Buildbot regression testing.

The manuscript makes a clear, pragmatic software-engineering case for loose coupling: pushing web-service and tool-specific complexities out of the core server into declarative XML wrappers and standalone command-line scripts has proven far more resilient than heavy web-service ontologies. However, as a scientific manuscript focused on translational genomics, its primary limitations are a complete absence of technical diagrams, concrete XML/protocol specifications, or quantitative server benchmarks, an idealized claim that private instances can be installed "in minutes" (which ignores the provisioning of underlying third-party executables and reference genome databases), and the lack of a concrete translational genomics use case (such as a HapMap or dbGaP analysis workflow) to illustrate the claims made in the Introduction.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Loosely coupled XML "meta-server" architecture for wrapping command-line tools and integrating external data repositories (UCSC Table Browser, BioMart): [Well Supported].**  
  Extending the Pise XML interface descriptor paradigm to support multi-page parameter forms, embedded functional regression tests (executed daily via Buildbot), and asynchronous URL callbacks from external genome browsers is a sound, extensible design that avoids brittle core dependencies on external web-service schemas.

* **Scalable Python server architecture supporting both standalone local execution and production HPC offloading: [Moderately Supported].**  
  The separation of the web/metadata orchestration layer (in Python with PostgreSQL/MySQL) from compute execution (offloaded to an HPC cluster) is architecturally sound, and the authors report that the public server handles "hundreds of researchers and... thousands of jobs every day." However, no architectural diagram, schema, or empirical performance statistics (e.g., job concurrency, database throughput, or cluster scheduling latency) are presented to substantiate the scalability discussion.

* **Claim that "installation and configuration of a private instance can be completed in minutes rather than hours or days": [Overstated].**  
  While checking out the core Python framework from Subversion and launching the default built-in web server and embedded database takes minutes, deploying a functional private instance for translational genomics requires installing and configuring the underlying third-party command-line tools (R/Bioconductor packages, C/C++ aligners, Perl/Python libraries) and downloading terabytes of local reference genomes and annotation indices, which remains a multi-hour to multi-day systems administration task.

* **Applicability to translational human disease genomics and protected cohorts (HapMap, dbGaP): [Moderately Supported].**  
  Although the Introduction motivates the platform with "billions of genotypes from large publicly funded studies available through dbGaP" and human subjects privacy, the body of the paper describes only generic UCSC/BioMart imports and provides no example workflow or security specification (such as user authentication, role-based access control, or encrypted transport/storage) for handling dbGaP or HIPAA-protected translational datasets.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Include a Concrete XML Tool Descriptor Listing and an Architectural Diagram of the Data Callback Protocol
* **WHY:** Describing the XML tool wrapper and the UCSC/BioMart URL callback mechanism purely in prose makes it difficult for tool developers and repository maintainers to evaluate the actual implementation effort.
* **WHAT:** Add a two-panel figure showing (A) the system architecture and asynchronous URL callback handshake with UCSC/BioMart, and (B) a concise, real XML tool definition file.
* **HOW:** Show a 20–30 line XML snippet demonstrating `<command>`, `<inputs>`, `<outputs>`, and `<tests>` tags for a representative genomics tool, alongside a sequence diagram illustrating how the user browser, external data source (UCSC Table Browser), and `[SOFTWARE]` server exchange the data retrieval URL.

#### 2. Qualify Local Installation Effort and Discuss Third-Party Tool/Data Provisioning
* **WHY:** Stating that a private instance can be installed and configured "in minutes" misleads groups planning to deploy a private server for protected human subjects data, where the main effort lies in installing third-party dependencies and reference datasets.
* **WHAT & HOW:** Revise the "Design issues for users and uses" section to distinguish between bootstrapping the core Python web application (which takes minutes) and provisioning third-party command-line executables and local genome build indices required by the wrapped tools.

#### 3. Demonstrate a Concrete Translational Genomics Workflow
* **WHY:** The Introduction and Conclusion frame the paper around translational genomic research (HapMap, dbGaP, human disease genotypes), but no translational example is shown.
* **WHAT & HOW:** In "Proof of the pudding," walk through one concrete multi-step translational workflow executed in `[SOFTWARE]` (for example, importing disease-associated SNPs or linkage intervals, intersecting with UCSC/BioMart gene and regulatory annotations, and running a statistical association or enrichment script).

#### 4. Minor Editorial Corrections
* **WHY:** A few typographical and grammatical errors appear in the text.
* **WHAT & HOW:**
  * In "Implementation lessons and features," change `"PostgresSQL"` to `"PostgreSQL"`.
  * In "Proof of the pudding," add a missing period at the end of the first paragraph (`"...intermediate outputs."`) and revise `"so data to be easily imported"` to `"allowing data to be easily imported"`.
