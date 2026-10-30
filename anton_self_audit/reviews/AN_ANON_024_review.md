# Review of AN_ANON_024

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.7 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates machine learning methods to predict job walltime and peak memory consumption on a public bioinformatics workflow platform, using 5 years of historical runtime logs and 1 month of memory usage logs ($N = 1,399$ to $3,985$ jobs across `bowtie2`, `hisat2`, `bwa mem`, and `stringtie`). The authors compare Random Forest (RF), Extremely Randomized Trees (Extra Trees), and Gradient Boosting regressors under 3-fold cross-validation, finding that RF achieves slightly higher mean $R^2$ across tools with $>100$ runs. To generate actionable scheduling intervals, they compare a Standard Deviation Random Forest ($\hat{y} \pm k\hat{\sigma}$ for $k \in \{1, 2, 3\}$) against a Random Forest Classifier trained on recursively defined median runtime buckets, and discuss how predicted limits can enable Slurm backfill scheduling.

Leveraging large-scale production telemetry from bioinformatics workflows to replace static over-allocation heuristics (e.g., 30–32 GB RAM and 36–72 h walltime) is a practical operational goal, and the authors candidly document real-world data caveats (untracked heterogeneous cluster routing, concurrent node load, and silent zero-input job successes). However, the evaluation suffers from three methodological weaknesses: (1) cross-validation is performed on a randomly shuffled dataset (and after global target-bucket construction and feature scaling), which leaks multi-job user batches and workflow collections across train and test splits; (2) the interval evaluation conflates two-sided confidence interval inclusion ($\hat{y} - k\hat{\sigma} \le y \le \hat{y} + k\hat{\sigma}$) with operational scheduling success, where only under-prediction ($y > \text{walltime}$ or $y > \text{RAM limit}$) causes job failure while over-prediction wastes capacity; and (3) the Slurm backfill scheduling section is a purely hypothetical 4-job hand-worked example rather than a trace-driven simulation using the model's predictions. All three issues can be addressed computationally using the existing dataset and codebase.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Random Forest regression slightly outperforms Extra Trees and Gradient Boosting for predicting bioinformatics tool runtimes from job parameters and input file sizes: [Moderately Supported].**  
  Across tools with $>100$ runs (Figure 2 and Supplementary Table S1), RF yields the highest mean and median $R^2$. However, the manuscript omits simple baseline models in the main text (such as ordinary/log-linear regression on total input file size alone) and evaluates on randomly shuffled 3-fold splits, where identical tool invocations from the same user workflow collection can appear in both training and test folds, inflating $R^2$.

* **Standard Deviation Random Forests and Random Forest Classifiers provide comparable runtime range accuracy at 1 SD, while SD Forests achieve higher coverage at 2–3 SD: [Moderately Supported].**  
  While the empirical comparison in Figures 3–4 supports this trend, the comparison is not symmetric: for the classifier, the recursive median buckets (`(0, 155.0, 592.5, ...)` in Section 4.4) were defined on the full dataset prior to cross-validation, and evaluating two-sided interval inclusion ($\hat{y} \pm k\hat{\sigma}$) penalizes jobs that finish *faster* than $\hat{y} - k\hat{\sigma}$, even though early completion never causes a scheduler timeout.

* **Peak memory usage can be predicted with ~90% coverage at 2 SD across major alignment and assembly tools (`bowtie2`, `hisat2`, `bwa mem`, `stringtie`): [Fragile].**  
  Table 2 reports high $R^2$ (0.78–0.96) and 89%–95% 2-SD coverage on an 80/20 random split of 1 month of data. As the authors note, a 1-month window combined with a random 80/20 split is highly susceptible to batch leakage (e.g., a single user running `bowtie2` against the same reference genome across 500 samples). In addition, for aligners like `bowtie2`, `hisat2`, and `bwa mem`, peak memory is dominated by the static size of the reference genome index (`dbkey`) rather than FASTQ read count, a distinction that is not quantified via feature importance analysis.

* **Deploying these runtime and memory predictions enables Slurm backfill scheduling that substantially increases cluster throughput and reduces queue wait times: [Overstated].**  
  Section 2.7 presents only a toy textbook illustration of 4 synthetic jobs (Jobs A–D) on a hypothetical 12-core node, without running a scheduler simulation on the actual historical job trace to quantify wait-time reduction vs. timeout/OOM kill rates under the predicted allocations.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate Models Under Chronological (Time-Split) Validation and Prevent Preprocessing Leakage
* **WHY:** In production scheduling, a model trained on past job logs must predict resource usage for *future* jobs submitted by new users. Shuffling the dataset before 3-fold CV (Section 4.7) splits multi-sample workflow collections across train and test sets, while computing classifier runtime buckets (Section 4.4) and `MinMaxScaler` (Section 4.6) on the whole dataset leaks test-set distribution statistics.
* **WHAT:** Re-evaluate the runtime and memory models using a strict chronological split (e.g., training on the first 80% of jobs ordered by `create_time` and testing on the final 20%), fitting all scalers, binarizers, and classifier quantile buckets strictly inside the training split.
* **HOW:** Sort the job dataframe by `create_time`, partition into sequential train/test sets (or rolling time windows), fit `MinMaxScaler`, `LabelBinarizer`, and the recursive median buckets on `X_train`/`y_train` only, and report the chronological $R^2$ and coverage metrics alongside the shuffled CV results in Table 2 and Figure 2.

#### 2. Replace Two-Sided Interval "Accuracy" with Operational Asymmetric Scheduling Metrics
* **WHY:** A job scheduler only requires an *upper bound* $U(x) = \hat{y}(x) + k\hat{\sigma}(x)$ for walltime and RAM. If actual usage $y < \hat{y}(x) - k\hat{\sigma}(x)$, the job succeeds and releases resources early; calling this an "inaccurate" prediction (as in the two-sided $\hat{y} \pm k\hat{\sigma}$ check) misaligns the metric with cluster operations.
* **WHAT:** Report the two operational metrics that directly govern scheduling: (i) **Under-allocation (Kill) Rate**, the fraction of test jobs where $y_{\text{actual}} > U(x)$ (causing timeout or OOM failure), and (ii) **Slack / Over-allocation Ratio**, the mean wasted reservation $\frac{1}{N}\sum_{y \le U(x)} (U(x) - y)$ compared to the current static heuristic (36–72 h walltime and 30–32 GB RAM).
* **HOW:** Using the existing test-set predictions $\hat{y}$ and $\hat{\sigma}$ for $k \in \{1, 2, 3\}$, compute the empirical one-sided exceedance rate $\Pr(y > \hat{y} + k\hat{\sigma})$ and the total GB-hours / core-hours saved relative to the static baseline.

#### 3. Add a File-Size / Reference-Index Baseline and Report Feature Importances
* **WHY:** Readers cannot tell how much predictive power comes from complex parameter interactions versus simply knowing input file size (for runtime) or reference genome index `dbkey` (for aligner memory).
* **WHAT:** Include a baseline regressor using only total input `file_size` (and `dbkey` for aligners), and report the top 5 Random Forest feature importances for `bowtie2`, `hisat2`, `bwa mem`, and `stringtie`.
* **HOW:** Extract `model.feature_importances_` from the trained `scikit-learn` Random Forest models and add a small table or bar chart showing the variance explained by input file size, reference genome, and tool flags.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Truncated sentences, percentage typos, and conflicting server allocation numbers in the text reduce clarity and reproducibility.
* **WHAT & HOW:**
  * **Section 2.5 (line 153):** Change `"achieving about 0.9% accuracy"` to `"achieving about 90% (0.90) accuracy"` to match Table 2 (`0.89`–`0.95`).
  * **Section 1.1 (line 52) vs. Section 2.7 (line 180):** Reconcile the conflicting descriptions of the default server allocation (line 52 states `"32 Gb of RAM and a walltime of 72 h"`, whereas line 180 states `"walltime of 36 h, and are allocated six CPU cores and 30 GB of memory"`).
  * **Section 4.5 (lines 253 and 259):** Restore the missing code tokens at the end of the truncated bullet points: `"parameters whose name begins with [missing string, e.g., __]"` and `"parameters whose names end with [missing string, e.g., _id]"`.
  * **Section 2.4 (lines 136 and 140):** Fix grammatical typos (`"It is also be of interest"` $\rightarrow$ `"It is also of interest"`; `"Average size of on standard deviation predicted the random forest"` $\rightarrow$ `"Average size of one standard deviation predicted by the random forest"`).
