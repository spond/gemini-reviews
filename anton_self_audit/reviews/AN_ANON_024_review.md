# Review of AN_ANON_024

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.2 / 8.0**  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates machine learning models for predicting the runtime and peak memory usage of bioinformatics jobs executed on a major public workflow server. Using a 5-year historical dataset of job executions (and a 1-month subset of cgroup memory logs for four tools: `bowtie2` [$n=3,985$], `hisat2` [$n=2,811$], `bwa mem` [$n=2,199$], and `stringtie` [$n=1,399$]), the authors compare Random Forest (RF), Extra Trees (ET), and Gradient Boosting (GB) regressors (100 trees, max depth 12 for RF/ET and 3 for GB) via 3-fold cross-validation. They then evaluate a Standard Deviation Random Forest (`scikit-garden`) and a median-bucketed Random Forest Classifier to construct prediction intervals for Slurm walltime and memory allocation. Source code and preprocessed training tables are provided via GitHub and Supplementary Materials 1–2.

While leveraging historical workflow telemetry to optimize HPC backfill scheduling is a practical engineering goal, the machine learning pipeline contains several methodological flaws that invalidate or inflate the reported performance metrics: (1) Table 1 (`ob_id`, `dataset_id`, `file_size`, `type (input or output)`, `end_epoch`, `cpuacct.usage`, `memory.max_usage_in_bytes`) includes *output* dataset sizes and post-execution metrics in the attribute schema without explicitly excluding output files from the pre-execution feature matrix; (2) feature scaling (`MinMaxScaler`), categorical binarization, and recursive median class bucketing are performed on the full dataset *before* 3-fold random cross-validation, causing preprocessing and target-discretization leakage; (3) evaluating on a randomly shuffled 3-fold split rather than a temporal split leaks concurrent multi-step user workflows and server-load states between train and test sets; and (4) the operational definition of "Accuracy: 1SD / 2SD / 3SD" in Table 2 is never mathematically defined in the text, and for `bwa mem` in Section 4.4 the top classifier bucket spans 10,523 s to 60,409 s (nearly 14 hours), which is too wide to improve short-job backfill. All of these issues can be fixed via a clean computational re-analysis on the existing dataset.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Random forest regressors slightly outperform Extra Trees and Gradient Boosting on historical runtime prediction across tools with $>100$ runs: [Moderately Supported].**  
  The comparative evaluation across tools with $>100$ runs shows similar mean and median $R^2$ across the three tree ensembles, with Random Forests slightly ahead. However, all three models were fixed at arbitrary hyperparameters (100 trees, depth 12 for RF/ET vs. depth 3 for GB) without hyperparameter tuning, and the absolute mean/median $R^2$ values are omitted from the main text and Figure 2 caption.

* **Standard Deviation Random Forests predict peak memory usage with $R^2 = 0.78\text{–}0.96$ and "0.9% [sic: 90%] accuracy" within a 2 SD confidence interval across `bowtie2`, `hisat2`, `bwa mem`, and `stringtie`: [Fragile].**  
  First, Table 1 lists Datasets attributes with `type (input or output)` and `file_size`, and Section 4.5 does not state that *output* dataset sizes or post-run attributes (`cpuacct.usage`, `end_epoch`) were stripped before training; if output file sizes are present in the feature matrix, they represent severe target leakage because output size is unknown prior to job execution. Second, as the authors acknowledge in Section 2.5 (line 153), memory logs were collected over just one month and evaluated via a random 80/20 split (and 3-fold shuffled CV). Because users frequently run batches of identical tools on similar samples (or workflow collections) within the same day or week, random shuffling places nearly identical jobs from the same user batch into both training and test sets.

* **Quantile regression forests vs. Standard Deviation Random Forests and recursive-median Random Forest Classifiers provide controllable prediction intervals for walltime scheduling: [Methodologically Flawed].**  
  First, the Abstract (line 32) and Section 2.4 (line 142) claim results for "Quantile regression forests," whereas Section 4.3 (lines 217–219) admits that quantile regression forests were *not* actually run due to memory usage, and a parametric Gaussian-like standard deviation forest (`scikit-garden`) was substituted instead. Second, the manuscript never defines what "Accuracy" means for a continuous regression interval (`1SD`, `2SD`, `3SD`): whether a prediction is scored as "accurate" if $\hat{y} - k\sigma \le y \le \hat{y} + k\sigma$ (two-sided coverage) or if $y \le \hat{y} + k\sigma$ (one-sided walltime bound, where under-prediction kills the job in Slurm). Third, in Section 4.4, the classifier buckets $(0, \text{median}, \dots)$ were constructed on the entire dataset prior to cross-validation, leaking the test target distribution, and yielding exponentially wider upper buckets (e.g., 2.9 to 16.8 hours for `bwa mem`) where precision is poorest precisely on the longest jobs.

* **Undetected job execution errors (such as `bwa mem` completing in 0 seconds without input files) do not bias model evaluation because removing Isolation Forest outliers did not change $R^2$: [Methodologically Flawed].**  
  In Section 4.2 (line 202), the authors note that corrupted jobs without requisite inputs are mislabeled as "successfully completed" in both training and testing folds, and that Isolation Forests failed to remove them visually. Leaving corrupted zero-input/instant-exit jobs in *both* the training and test partitions allows the decision trees to trivially predict near-zero runtime whenever input features are missing/zero, artificially inflating test $R^2$ rather than demonstrating model robustness.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Explicitly Restrict Features to Pre-Submission (Launch-Time) Attributes Only
* **WHY:** In Slurm scheduling, walltime and memory must be requested *before* a job starts. Table 1 lists `type (input or output)` under Datasets alongside post-execution cgroup metrics (`cpuacct.usage`, `end_epoch`, `runtime_seconds`, `memory.max_usage_in_bytes`). Including output dataset sizes or post-launch metrics in the predictor matrix causes severe lookahead leakage.
* **WHAT:** Explicitly list the exact pre-execution predictor variables retained for each tool and verify that all `output` dataset records and post-execution metrics are excluded prior to feature engineering.
* **HOW:** Filter the dataset join in the preprocessing script to `dataset.type == 'input'` only, drop all runtime/cgroup execution columns from $X$, and publish the exact feature list and feature importances (Gini / permutation importance) for the top 10 tools in a main-text table.

#### 2. Replace Shuffled Cross-Validation with Out-of-Time (Chronological) Validation and Pipeline-Scoped Preprocessing
* **WHY:** Shuffling 5 years (or 1 month) of job logs mixes concurrent jobs from the same user workflow collection and identical server-load windows across train and test folds, while applying `MinMaxScaler`, `LabelBinarizer`, and recursive median bucketing before splitting leaks test-set statistics.
* **WHAT:** Evaluate all models using chronological train/test splits (e.g., train on the first 80% of calendar time, test on the final 20% future window) and encapsulate all scaling, encoding, and target bucketing strictly inside `sklearn.pipeline.Pipeline` fit only on the training fold.
* **HOW:** Sort jobs by `create_time`, use `TimeSeriesSplit` (or a strict chronological 80/20 cutoff), fit `MinMaxScaler` and median bucket thresholds exclusively on `X_train`/`y_train`, and report both shuffled CV and chronological test metrics side by side.

#### 3. Define Asymmetric Walltime/Memory Loss Metrics Aligned with HPC Job Termination
* **WHY:** In Slurm (Section 2.7), under-predicting walltime or memory causes the job to be killed (`TIMEOUT` or `OOM`), wasting 100% of elapsed compute time, whereas over-predicting merely delays backfill. A symmetric $\pm k\text{ SD}$ interval does not distinguish fatal under-allocation from safe over-allocation.
* **WHAT:** Explicitly define the mathematical formula for "Accuracy" in Table 2 and Figures 3–4, and report separate rates for **Job Kill Rate (Under-allocation Rate: $y_{\text{actual}} > \hat{y}_{\text{allocated}}$)** and **Resource Waste (Mean Over-allocation: $\hat{y}_{\text{allocated}} - y_{\text{actual}}$ given $y_{\text{actual}} \le \hat{y}_{\text{allocated}}$)**.
* **HOW:** Compute $\hat{y}_{\text{allocated}} = \hat{\mu} + k\hat{\sigma}$ for $k \in \{1, 2, 3\}$ (and actual empirical quantiles from a true Quantile Regression Forest using `scikit-garden`'s `RandomForestQuantileRegressor` at the 90th, 95th, and 99th percentiles), and compare total wasted core-hours and job kill percentages against the current static Galaxy heuristic (36 h / 72 h walltime and 30 GB / 32 GB RAM).

#### 4. Reconcile Textual Contradictions and Fix Typographical Errors
* **WHY:** Multiple numerical and methodological statements contradict each other across sections:
  1. Line 32 & 142 refer to "Quantile regression forests," whereas Line 219 states quantile regression forests were not used and a standard deviation forest was used instead.
  2. Line 52 states the default Galaxy Main allocation is "32 Gb of RAM and a walltime of 72 h," whereas Line 180 states it is "a walltime of 36 h, and are allocated six CPU cores and 30 GB of memory."
  3. Line 153 states "achieving about 0.9% accuracy," when Table 2 reports `0.89`–`0.95` (i.e., 89%–95%, a 100-fold typo).
  4. Lines 253 & 259 have truncated sentences ("parameters whose name begins with [blank]" and "parameters whose names end with [blank]").
* **WHAT & HOW:** Correct all four discrepancies in the text: replace "quantile regression forest" with "standard deviation random forest" in the Abstract and Section 2.4; clarify the exact Slurm default limits (e.g., single-core vs. multi-core queues in lines 52 and 180); fix `0.9%` to `90%` (or `0.90`) on line 153; and restore the missing prefix/suffix strings on lines 253 and 259.
