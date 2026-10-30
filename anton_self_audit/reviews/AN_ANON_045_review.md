# Review of AN_ANON_045

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This educational perspective outlines a framework for delivering remote and hybrid bioinformatics instruction using `[SOFTWARE]`, the `[WORKFLOW_PLATFORM]` Training Network (GTN; >150 community-curated hands-on tutorials), and Training Infrastructure as a Service (TIaaS; dedicated HPC training queues and a GDPR-compliant instructor progress dashboard across public `[SOFTWARE]` servers). Drawing on social constructivist pedagogy, the authors propose a four-part instructional design that pairs synchronous communication (video conferencing via Jitsi, BigBlueButton, or commercial equivalents) with asynchronous channels (recorded lectures, persistent Q&A documents, forums, and shared `[SOFTWARE]` histories): (1) a 30–60 minute recorded theoretical introduction, (2) an optional live demonstration, (3) self-paced hands-on execution incorporating deliberate error-injection exercises to build debugging skills, and (4) homework assessment on new datasets (such as Personal Genome Project data) evaluated via shared `[SOFTWARE]` histories. Four qualitative instructor case studies ("User stories") illustrate the transition of MSc dry-lab projects, multi-classroom hybrid workshops (Gallantries), proteomics courses, and epigenomics courses to online delivery during the COVID-19 pandemic.

The manuscript provides practical, well-structured guidance for bioinformatics educators, demonstrating how browser-based execution, pre-loaded Data Libraries, and dedicated TIaaS queues eliminate local software installation barriers and student hardware inequities. Its primary limitations are the absence of quantitative evaluation metrics in the four User Stories (relying on qualitative assertions such as "fewer errors occurred than in offline courses" and "unanimously positive feedback" without reporting server-side job error rates, completion statistics, or survey data) and an overstatement that dataset timestamps and metadata in shared `[SOFTWARE]` histories are sufficient to "prove authorship" on student homework.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Elimination of local installation barriers and HPC queue contention via browser-based `[SOFTWARE]`, Data Libraries, and TIaaS: [Well Supported].**  
  The infrastructure capabilities are concretely documented, including pre-staged GTN Data Libraries (`github.com/[WORKFLOW_PLATFORM]-eu/shared-data/`) that avoid redundant student file uploads and TIaaS queue isolation that supported >150 training events (>4,500 trainees) on the European server without disrupting >23,000 regular research users.

* **Four-stage hybrid synchronous/asynchronous pedagogical model incorporating constructivist error-provoking exercises: [Well Supported].**  
  The instructional design is well grounded in online education literature, thoughtfully addressing student bandwidth dropouts, time-zone differences, single-monitor constraints on the learner side, and active problem-solving through intentional parameter/format troubleshooting tasks.

* **Claims in the User Stories that online delivery produced "fewer errors... than in offline courses" and "unanimously positive feedback": [Fragile].**  
  While plausible, these claims in User Story 3 are presented purely as qualitative anecdotes without supporting summary statistics (such as sample sizes, pre-/post-transition error counts from `[SOFTWARE]` history logs, completion rates, or structured course evaluation distributions).

* **Claim that "Time stamps and metadata on every dataset are particularly useful to prove authorship" in student homework submissions: [Overstated].**  
  While dataset timestamps and parameter provenance help instructors inspect when and how a history was run, they do not prove independent student authorship: a student can import a peer's shared history or execute an exported `.ga` workflow file from a classmate within their own account, generating new job execution timestamps and metadata under their own username.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Include Quantitative Server Telemetry and Course Survey Summaries in the User Stories
* **WHY:** Assertions that fewer errors occurred online than offline and that student feedback was unanimously positive carry much greater evidentiary weight when backed by basic descriptive statistics from the courses described.
* **WHAT:** Add a summary table or quantitative metrics for the four User Stories.
* **HOW:** Report for each User Story the number of enrolled students, completion rate of the assigned GTN histories, basic summary statistics from post-course student evaluations (e.g., Likert scale distributions and response rates), and, where available from `[SOFTWARE]`/TIaaS logs, the average number of failed vs. successful tool executions per student.

#### 2. Qualify the Authorship Verification Claim for Shared `[SOFTWARE]` Histories
* **WHY:** Because `[SOFTWARE]` makes sharing histories and workflows effortless among peers, relying solely on dataset timestamps to verify independent homework completion is vulnerable to workflow sharing or history re-execution.
* **WHAT:** Revise the homework assessment discussion to describe robust practices for verifying individual student work.
* **HOW:** Note that because workflows and histories can be cloned and re-run to produce new timestamps, instructors should pair shared `[SOFTWARE]` histories with individualized input dataset subsets, unique parameter exploration tasks, or short written biological interpretations (as already practiced in User Story 4).

#### 3. Minor Editorial Cleanup
* **WHY:** Figure 1's caption contains a grammatical omission.
* **WHAT & HOW:** Revise the Figure 1 caption from `"Proposed teaching format including theoretical using [SOFTWARE] features and external communication channels"` to `"Proposed teaching format combining theoretical lectures, [SOFTWARE] features, and external communication channels."`
