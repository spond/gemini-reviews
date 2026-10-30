# Review of AN_ANON_049

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the transmission dynamics, ontogenetic bottleneck sizes, maternal age effects, and purifying selection acting on human mitochondrial DNA (mtDNA) heteroplasmies across 96 multigenerational healthy families (345 individuals, 249 mother–child transmissions, and 690 blood and buccal tissue samples sequenced to a mean depth of ~11,400×). After quality filtering and removal of low-complexity regions following Sanger validation (133/150 confirmed at minor allele frequency [MAF] $\ge 0.1$), the authors identify 668 heteroplasmies (MAF $\ge 0.01$) representing 346 independent mutations at 312 sites. Using two population-genetic frameworks—an $F_{ST}$-based Branch-Length Statistic (BLS) and a Bayesian Ontogenetic Phylogeny Likelihood (OPL) method—they estimate an effective germline bottleneck of ~7.1 (BLS) to 10.3–13.4 (OPL) segregating units, show that >85% (BLS) to 99.1% (OPL) of germline drift occurs after oogonial lineage divergence, report increased mother–offspring divergence and putative de novo germline mutations with maternal age at childbirth, and infer purifying selection against pathogenic and nonsynonymous variants during germline transmission. While Dataset S1 and supplementary tables are referenced, no public repository accession (e.g., SRA or dbGaP) for the raw MiSeq reads or source code for the BLS pipeline is provided in the main text or Methods.

The multi-sibling, two-tissue pedigree design in healthy families avoids clinical ascertainment bias and provides strong resolution to separate pre- versus post-oogonial divergence and germline versus somatic drift. However, several statistical and modeling limitations affect the quantitative conclusions: (1) confounding between age-dependent germline genetic drift and the detection of putative "de novo" germline mutations, because pre-existing maternal variants below the 0.002 noise floor are more likely to drift above the 0.01 calling threshold in older mothers; (2) unmodeled family-level clustering in the maternal-age Poisson regressions across 249 transmissions from 96 mothers; (3) an unresolved contradiction between the heuristic regression and the OPL likelihood model regarding age-related somatic mutation accumulation in blood; and (4) frequency-matching and boundary-truncation biases in the BLS test for purifying selection. All four issues can be resolved through computational re-analysis and statistical conditioning using the existing dataset.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Effective human germline mtDNA bottleneck is ~7–13 segregating units and occurs predominantly (>85–99%) after the divergence of oogonial lineages: [Well Supported].**  
  Both BLS (7.1 units, 95% CI: 3.5–20.4; 85.3% post-oogonial split) and OPL (10.3 combined germline units, 95% HPD: 8.5–12.3; 99.1% post-oogonial split) yield concordant results, directly corroborated by weaker sibling–sibling allele frequency correlations ($r = 0.319$) compared to mother–child correlations ($r = 0.551$) and much smaller somatic drift between blood and buccal tissues ($r = 0.97$, effective bottleneck sizes of 134.9 and 262.9).

* **Germline heteroplasmy drift increases with maternal age at childbirth during oocyte meiotic arrest: [Well Supported].**  
  Mother–child somatic allele frequency correlation drops from $r = 0.92$ in younger mothers (<30 y) to $r = 0.67$ in older mothers ($\ge 30$ y), BLS mother–child divergence increases nearly fivefold (median 0.361 vs. 0.076 drift units with non-overlapping 95% bootstrap CIs), and OPL independently infers a positive drift accumulation rate during meiotic arrest ($0.001$ drift units/year, posterior $P[\text{drift} > 0] = 1.0$).

* **De novo germline mtDNA mutations increase significantly with maternal age at childbirth: [Fragile].**  
  The heuristic definition calls a mutation "de novo" when MAF $\ge 0.01$ in both offspring tissues and MAF $< 0.002$ in all other family members, yielding a non-significant maternal age trend ($\beta = 0.028, P = 0.087$). Statistical significance is achieved either by using OPL calls gated at an ad hoc "visually informed threshold of 0.8" ($\beta = 0.042, P = 0.015$) or by restricting to the 50-mutation intersection ($\beta = 0.049, P = 0.028$). Because germline drift increases substantially with maternal age (Fig. 2A), cryptic maternal heteroplasmies present at $0 < \text{MAF} < 0.002$ have a higher probability of drifting above the $\text{MAF} \ge 0.01$ detection threshold in the offspring of older mothers, confounding amplified drift with true de novo mutagenesis. Moreover, the Poisson regression across 249 transmissions treats multiple children of the same mother as independent without a family random effect.

* **De novo somatic mutations accumulate with age in blood, whereas somatic genetic drift does not increase with age: [Moderately Supported].**  
  While heuristic counts of tissue-restricted variants (MAF $\ge 0.01$ in blood, $<0.002$ elsewhere) increase with age ($\beta = 0.042, P = 8 \times 10^{-5}$), the OPL full-likelihood model simultaneously estimates zero opportunity for somatic mutation accumulation with age in adult tissues (posterior probability = 1.0; Fig. 1D). The authors report both results without reconciling why the likelihood model and heuristic counting reach opposite conclusions on the same dataset.

* **Purifying selection acts against pathogenic and nonsynonymous mutations specifically during germline transmission by reducing their branch-specific BLS divergence: [Moderately Supported].**  
  The depletion of protein-coding mutations ($P = 9.60 \times 10^{-7}$), reduced nonsynonymous-to-synonymous ratio ($0.43, P < 0.001$), and lower maximum MAF of pathogenic variants in blood (0.052 vs. 0.916, $P < 10^{-4}$) strongly support purifying selection. However, the branch-specific BLS permutation test (Fig. 3C–D) is confounded by initial allele frequency: because Hudson's $F_{ST}$ and the $\text{MAF} \ge 0.01$ detection floor truncate measurable downward shifts for variants that already segregate near the 0.01 boundary (median MAF = 0.029, and max blood MAF = 0.052 for pathogenic variants), lower BLS divergence on germline branches can arise mechanically from boundary truncation rather than directional selection alone.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Decouple Age-Related Germline Drift from Putative De Novo Mutation Counts and Account for Pedigree Clustering
* **WHY:** Because mother–offspring drift increases nearly fivefold in older mothers (Fig. 2A), pre-existing maternal variants segregating below the 0.002 noise threshold are more likely to drift above $\text{MAF} \ge 0.01$ in children born to older mothers, inflating apparent de novo counts. In addition, 249 transmissions come from 96 mothers, violating the independence assumption of standard Poisson regression.
* **WHAT:** Re-fit the maternal-age de novo mutation models as generalized linear mixed models (GLMMs) with a maternal random intercept, and perform forward-time Wright–Fisher/OPL simulations to quantify the false-positive "de novo" promotion rate of cryptic maternal heteroplasmies ($0.0001 \le \text{MAF} < 0.002$) as a function of maternal age-dependent drift.
* **HOW:** In R (`lme4::glmer`), fit `count ~ maternal_age + (1 | family_id)` with a Poisson link across the 249 transmissions for all three de novo definitions (heuristic $n=78$, OPL $n=86$, and intersection $n=50$), and report sensitivity across OPL posterior probability thresholds (0.5, 0.7, 0.8, 0.9, 0.95) rather than relying on a single visually chosen cutoff of 0.8.

#### 2. Frequency-Match the BLS Permutation Test for Germline Selection
* **WHY:** Pathogenic heteroplasmies segregate at much lower allele frequencies (blood maximum 0.052) than nonpathogenic heteroplasmies (maximum 0.916; Fig. 3A). Permuting pathogenicity labels uniformly across all sites conflates selective constraint during transmission with the mechanical boundary constraint on $D_{xy} = -2 \ln(1 - F_{ST})$ near the $\text{MAF} = 0.01$ calling threshold.
* **WHAT:** Repeat the BLS branch-length permutation tests (Fig. 3C–D) using MAF-stratified permutations that match the maternal allele frequency distribution between pathogenic/nonpathogenic and nonsynonymous/synonymous sets.
* **HOW:** Bin heteroplasmies by maternal somatic MAF (e.g., $[0.01, 0.02)$, $[0.02, 0.05)$, $[0.05, 0.15)$, $\ge 0.15$) or restrict the comparison to variants with maternal MAF $\le 0.10$, permute functional labels strictly within MAF bins 10,000 times, and report the frequency-matched empirical $P$-values alongside Fig. 3C–D.

#### 3. Reconcile the Contradiction Between OPL and Heuristic Somatic Mutation Accumulation
* **WHY:** Reporting that blood de novo mutations increase significantly with age ($\beta = 0.042, P = 8 \times 10^{-5}$) while simultaneously stating that OPL infers zero mutation accumulation with age in adult somatic tissues (posterior probability = 1.0) leaves an unexplained methodological contradiction.
* **WHAT:** Explain and test why OPL assigns zero posterior mass to adult somatic mutation accumulation despite 14 blood-only and 43 buccal-only heuristic mutations.
* **HOW:** Inspect the OPL likelihood transition density for branches representing adult hematopoiesis and buccal turnover: determine whether OPL absorbs singleton tissue-specific variants (MAF $\ge 0.01$ in one tissue, $<0.002$ in the other) into the pre-sampling embryonic somatic branch or sequencing error model, and report the posterior distribution when the fixed embryonic somatic mutation rate is constrained vs. free.

#### 4. Provide Public Raw Sequencing Accessions and Analysis Scripts
* **WHY:** High-depth mtDNA sequencing from 690 samples and custom BLS estimators cannot be independently verified without raw read archives and executable code.
* **WHAT:** Deposit the de-identified mtDNA amplicon sequencing reads in a public or controlled-access archive (e.g., NCBI SRA or dbGaP) and release the BLS calculation and permutation scripts.
* **HOW:** Add a formal Data and Code Availability statement to the Materials and Methods listing the SRA BioProject/dbGaP accession numbers for the 690 fastq/BAM files and a permanent repository link (e.g., GitHub/Zenodo) containing the BLS and Monte Carlo selection scripts.
