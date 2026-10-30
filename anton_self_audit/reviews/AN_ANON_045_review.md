# Review of AN_ANON_045

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This educational perspective presents a structured framework for delivering remote and hybrid bioinformatics instruction using the `[WORKFLOW_PLATFORM]` ecosystem, the community-curated Galaxy Training Network (GTN; >150 hands-on tutorials across omics, imaging, ecology, and climate science), and Training Infrastructure as a Service (TIaaS; providing dedicated HPC queues and GDPR-compliant real-time instructor dashboards across >150 training sessions and >4,500 trainees on the European server). Grounded in social constructivist pedagogy, the authors propose a four-stage remote teaching format combining synchronous and asynchronous communication channels: (1) a recorded 30–60 minute theoretical introduction with shared Q&A documents, (2) an optional live data analysis demonstration, (3) self-paced hands-on practice using GTN tutorials and shared Data Libraries supplemented by intentionally designed error-provoking tasks to build debugging skills, and (4) formative and summative assessment via shared `[WORKFLOW_PLATFORM]` histories and reusable workflows using real-world or Personal Genome Project datasets. The manuscript concludes with four qualitative instructor user stories describing the rapid transition of MSc dry-lab capstone projects, the multi-classroom Gallantries hybrid broadcast workshops, a Molecular Medicine proteomics course, and a Master Bioinformatics epigenomics course to online delivery during the COVID-19 pandemic.

The manuscript offers a practical, accessible blueprint for remote computational biology instruction that effectively leverages zero-install browser workspaces, pre-staged Data Libraries, TIaaS queue isolation, and history provenance sharing to eliminate local software installation barriers and reduce student cognitive load. Its primary methodological limitation is the absence of quantitative empirical evaluation: although the platform natively logs job execution states, error frequencies, completion timestamps, and TIaaS dashboard metrics—and although the user stories make explicit comparative claims (e.g., that "fewer errors occurred than in offline courses" and that feedback was "unanimously positive")—no cohort sample sizes, job error logs, completion rates, or structured survey data are reported. Adding basic quantitative metrics from the four featured courses and tempering unmeasured comparative assertions would substantially strengthen the evidentiary grounding of the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Browser-based `[WORKFLOW_PLATFORM]` workspaces coupled with GTN tutorials, shared Data Libraries, and TIaaS dedicated queues remove local hardware/software installation barriers and support scalable remote bioinformatics instruction: [Well Supported].**  
  The infrastructure is mature and battle-tested (>125 public servers, >150 GTN tutorials, >150 TIaaS training events with >4,500 trainees running alongside >23,000 regular users without cluster contention), directly solving the hardware equity and remote software troubleshooting challenges of online instruction.

* **Sharing `[WORKFLOW_PLATFORM]` histories and workflows provides transparent provenance for remote debugging, peer learning, and instructor assessment: [Well Supported].**  
  Because histories capture exact tool versions, parameter choices, timestamps, and intermediate datasets, sharing histories between students and instructors enables asynchronous troubleshooting of failed steps and verifiable homework submission without screen-sharing bottlenecks.

* **Fewer student analysis errors occurred in the online proteomics course than in prior offline courses ("probably because students could follow the training at their own pace"), and student feedback was unanimously positive: [Fragile].**  
  Reported in the third user story (line 105), this comparative claim is entirely anecdotal: no student counts ($N$), job failure logs from the server histories, comparison against historical offline cohorts, or standardized course evaluation survey metrics (response rates, Likert distributions) are presented. Lower apparent error reports in an asynchronous setting can equally reflect under-reporting of intermediate failures that students resolved or abandoned privately before submitting their final history.

* **The proposed four-stage online teaching format "requires very little teaching personnel" because self-study GTN sessions "rarely create problems": [Moderately Supported].**  
  While standardized GTN tutorials and pre-configured tools eliminate installation-related support tickets, the manuscript's own recommendations emphasize maintaining open communication channels throughout the semester, holding open video call hours, designing custom error-provoking tasks, and reviewing shared individual histories and written reports—activities whose actual instructor time per student is not quantified.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Quantitative Cohort and Job-Execution Metrics for the Four Featured User Stories
* **WHY:** The four user stories (MSc dry-lab conversion, Gallantries pilot workshops, Freiburg Molecular Medicine proteomics, and Master Bioinformatics epigenomics) currently read as qualitative narratives without basic sample sizes or outcome metrics, despite `[WORKFLOW_PLATFORM]` histories and TIaaS automatically recording execution telemetry.
* **WHAT:** Add a summary table characterizing the four instructional deployments with concrete numbers.
* **HOW:** For each of the four user stories, tabulate: (a) number of enrolled students and instructors/TAs, (b) course duration and GTN tutorials used, (c) percentage of students who successfully submitted completed histories, (d) total tool jobs executed vs. failed jobs recorded in TIaaS/histories, and (e) quantitative summary scores and response rates from post-course student feedback surveys.

#### 2. Substantiate or Temper the Online vs. Offline Error-Rate Comparison
* **WHY:** Claiming that "fewer errors occurred than in offline courses probably because students could follow the training at their own pace" (line 105) makes an empirical causal assertion without controlling for history pruning (students deleting failed dataset cards prior to sharing) or reporting job logs.
* **WHAT:** Either compare server-side job failure rates between the online and prior in-person offerings of the proteomics course or reframe the statement as a qualitative instructor impression of support requests.
* **HOW:** Query the backend database for the proteomics course TIaaS group to compute the ratio of `error` to `ok` dataset states per student (including deleted history items) compared to the previous year's in-person cohort; if historical server logs are unavailable, revise line 105 to state that *fewer live troubleshooting interventions were requested by students during the self-paced sessions*.

#### 3. Provide Concrete Examples of Constructivist "Erroneous Tasks" in the GTN Format
* **WHY:** A compelling pedagogical recommendation in the manuscript (line 76) is to "artificially create short erroneous tasks that are not covered by the GTN materials, with the purpose of provoking errors that force students to hypothesise about the issue and find out solutions themselves." However, no concrete example of such a task is provided for instructors to adopt.
* **WHAT:** Include 2–3 specific examples of intentional error-provocation exercises mapped to standard GTN workflows (e.g., RNA-seq, ChIP-seq/epigenomics, proteomics).
* **HOW:** Add a box or table illustrating concrete troubleshooting prompts—such as supplying an unstranded vs. reverse-stranded parameter mismatch in RNA-seq quantification, mismatched chromosome naming (`chr1` vs. `1`) between a BED file and reference genome, or an incompatible quality score encoding (`Phred+64` vs. `Phred+33`)—alongside the diagnostic signature students are expected to identify in their history.
