# Review of AN_ANON_068

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.7 / 8.0**  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the evolutionary origins and selective architecture of the 30 nonsynonymous Spike (S-gene) substitutions defining the SARS-CoV-2 Omicron (BA.1) lineage. Combining codon-level selection scans (FEL and MEME in 3-month sliding windows across pre-Omicron GISAID sequences), intrahost variant calling across >230,000 raw sequencing datasets, recombination-aware comparative phylogenetics across 167 sarbecoviruses (GARD, IQ-TREE2, FEL, MEME), haplotype co-occurrence odds ratios, and Bayesian Graphical Model (BGM) coevolution analyses across 135,247 BA.1 S-gene sequences, the authors partition BA.1 Spike mutations into two groups: 16 sites previously evolving under positive selection in non-Omicron lineages, and 14 sites previously evolving neutrally or under purifying selection. Thirteen of the 14 conserved/neutral sites cluster into three structural regions on the Spike trimer (Cluster 1: RBD codons 339, 371, 373, 375; Cluster 2: RBM codons 493, 496, 498, 505; Cluster 3: fusion domain codons 764, 856, 954, 969, 981). Data, interactive ObservableHQ notebooks, BioProject accessions, and analysis scripts are thoroughly documented.

The study is notable for its multi-scale integration of population, intrahost, and deep sarbecovirus evolutionary data, and especially for its rigorous self-audit of within-BA.1 evolutionary signals (Table 2 and Figure 10), where the authors demonstrate that apparent within-BA.1 reversion mutations and BGM coevolution signals are heavily confounded by amplicon primer dropout and laboratory contamination ($R^2 = 0.773$ between missing data percentage and reversion counts; permutation $P < 0.001$ for contiguous reversion clustering). The primary limitation is that the central claim of positive compensatory epistasis among the 13 clustered mutations rests on an indirect inference from their individual rarity rather than direct statistical detection of epistatic co-occurrence, and does not formally separate intrinsic pairwise epistasis from a shift in the external selective environment (such as chronic-infection antibody maturation or altered cellular entry tropism).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Prior to the emergence of Omicron, 16 of the 30 BA.1 Spike nonsynonymous substitutions occurred at sites under positive selection in SARS-CoV-2, whereas 14 occurred at sites under purifying selection or evolving neutrally: [Well Supported].**  
  This classification is backed by internal-branch FEL and MEME analyses across 3-month windows of pre-Omicron GISAID genomes (Table 1, Figure 2), intrahost subconsensus allele frequencies showing that most of the 14 mutations arise de novo within hosts but fail to reach consensus or transmit (Figure 4), and recombination-partitioned FEL analyses across the nCoV clade of 167 sarbecoviruses confirming purifying selection favoring the Wuhan-Hu-1 state at 8 of the 13 clustered sites (lines 93–98).

* **Apparent signals of positive selection and coevolving reversions within the diversifying BA.1 clade are largely sequencing artifacts caused by primer dropout and template contamination: [Well Supported].**  
  Rather than taking their initial BGM coevolution results (6 coevolving pairs at $\text{PP} \ge 0.9$, Figure 8) and within-BA.1 FEL positive selection calls (20/28 sites, Table 2) at face value, the authors perform a forensic quality-control analysis showing that site-level missing data explains 77.3% of the variance in inferred reversion counts ($R^2 = 0.773, P < 0.01$; Figure 10) and that 9.0% (13/144) of reversions occur in contiguous 3–4 codon stretches ($P < 0.001$). This is an exemplary demonstration of controlling for bioinformatic and sequencing artifacts in genomic surveillance.

* **The 13 rarely seen BA.1 Spike mutations in Cluster Regions 1, 2, and 3 cooperatively interact via positive epistasis to mitigate their individual fitness costs: [Moderately Supported].**  
  While prior experimental deep mutational scanning and structural data directly confirm pairwise positive epistasis for specific pairs (notably Q498R and G496S with N501Y, lines 110–112), the broader claim that all three structural clusters assemble via compensatory intra- and inter-cluster epistasis is inferred indirectly from the juxtaposition of single-mutation purifying selection before Omicron and high epidemic fitness in BA.1. The authors' direct tests for co-occurrence in pre-Omicron haplotypes (Figure 7) found no systematic positive associations among cluster 1–3 sites, and the within-BA.1 BGM coevolution signals (Figure 8) were invalidated by primer dropout artifacts. Furthermore, as noted in lines 150–151, a change in selective regime (e.g., relaxed purifying selection or strong neutralizing antibody pressure during a chronic infection, or endosomal entry shift) can render previously deleterious mutations individually advantageous without requiring compensatory epistasis among all 13 sites.

* **The 13 rare mutations are non-randomly clustered into three functional 3D structural regions of the Spike trimer: [Moderately Supported].**  
  The structural mapping onto the Spike trimer (Figures 3 and 5) is biologically coherent and aligns with cryo-EM and functional evidence (RBD down-state stabilization in Cluster 1, ACE2 salt bridges and class 1/2 antibody escape in Cluster 2, and S1/S2 subunit interaction in Cluster 3). However, the definition of the three clusters is visual and qualitative; the manuscript does not report a formal spatial permutation test on the 3D protein structure (e.g., comparing mean pairwise $\text{C}_\alpha$ distances among the 13 negatively/neutrally selected sites against random draws of 13 surface/domain residues).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Formal 3D Spatial Permutation Test for Mutation Clustering
* **WHY:** A central premise of the manuscript is that the 13 neutral/negatively selected mutations form three non-random 3D clusters on the Spike structure, but no statistical test of spatial clustering is presented.
* **WHAT:** Quantify the 3D spatial clustering of the 13 sites on the closed and open Spike trimer structures (e.g., PDB `7TF8` / Xu et al.) against a null distribution of random codon placements.
* **HOW:** Compute the distribution of nearest-neighbor or within-cluster pairwise $\text{C}_\alpha$ Euclidean distances (both intra-protomer and inter-protomer) for the 13 sites, and compare this statistic against 10,000 random draws of 13 codons (either uniformly across Spike or stratified by domain/solvent accessibility) to report an exact empirical $P$-value.

#### 2. Re-Run Within-BA.1 Selection and BGM Coevolution After Filtering Amplicon-Dropout Genomes
* **WHY:** In Table 2 and Figure 10, the authors show that up to 65.5% of BA.1 sequences have missing data (`N`s) at RBD sites (e.g., S/417, S/440, S/446) and that low-coverage amplicon dropout drives spurious reversion calls along internal branches. However, the BGM coevolution analysis (Figure 8) and Table 2 selection scans were run on consensus clusters built from sequences that permitted unresolved nucleotides (`tn93-cluster` on `S.mapped.fasta`).
* **WHAT:** Perform a sensitivity re-analysis of within-BA.1 FEL/MEME and BGM coevolution restricted strictly to high-coverage BA.1 S-gene sequences with zero ambiguous bases (`N`s) across the Spike coding region (or sequenced with updated primer schemes).
* **HOW:** Filter `S.mapped.fasta` to retain only sequences with 0% missing data across all 30 BA.1 Spike focal codons prior to `tn93-cluster` haplotype collapsing, rebuild the `raxml-ng` phylogeny, and report whether any of the 6 BGM coevolving pairs or the Table 2 reversion counts persist when primer-dropout sequences are excluded.

#### 3. Reconcile Sample Sizes and Missing Table 2 Sites Across the Manuscript
* **WHY:** There are unexplained numerical discrepancies between the main text, tables, and methods that affect auditability.
* **WHAT & HOW:**  
  1. **Intrapatient sample count:** Reconcile the Figure 4 caption (line 74, which states `230,506 samples`) with Materials and Methods (chunk 2, line 64, which states `282,788 annotated ... raw sequencing data sets`). Explicitly state the filtering criteria that reduced 282,788 to 230,506.  
  2. **Missing BA.1 sites in Table 2:** Table 1 lists 30 nonsynonymous Spike substitutions in BA.1, whereas Table 2 and the accompanying text (chunk 2, line 5) analyze only 28 sites, omitting `S/212I` and `S/981F` without explanation. Either add positions 212 and 981 to Table 2 or state why they were excluded (e.g., alignment masking near the 211 deletion / 214 insertion for site 212, and clarify why 981 was dropped).

#### 4. Temper Abstract Claims Regarding Predictive Fitness Costs and Mandatory Epistasis
* **WHY:** The Abstract states that "prior to the emergence of Omicron the mutations would have been predicted to decrease the fitness of any virus within which they occurred" and that they "therefore cooperatively interact". Yet 4 of the 13 cluster sites (S/493R, S/496S, S/505H, S/981F) were evolving neutrally rather than under statistically significant negative selection in pre-Omicron SARS-CoV-2 (Table 1), and environmental/host-context shifts can alter single-site fitness effects independently of epistasis.
* **WHAT:** Refine the Abstract and Discussion to distinguish between the 9 cluster sites under detectable purifying selection and the 4 neutrally evolving sites, and frame compensatory epistasis alongside host-environment shifts (chronic infection antibody pressure or altered entry pathway) as complementary hypotheses.
* **HOW:** Revise the Abstract to note that 9 of the 13 clustered sites were under purifying selection and 4 were evolving neutrally prior to Omicron, and state that their co-assembly reflects either compensatory epistatic interactions, a major shift in selective pressures within the progenitor host environment, or both.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Factual inversions and codon typos in the main text conflict with Table 1 and known VOC definitions.
* **WHAT & HOW:**  
  1. **Line 91 (`S371L` vs. `S371F` inversion):** Correct `"In cluster region 1, BA.2 has a S/S371L mutation instead of a S/S371F"` to `"In cluster region 1, BA.2 has a S/S371F mutation instead of a S/S371L"`, consistent with lines 74 and 80.  
  2. **Line 91 (`S/L891F` typo):** Correct `"missing the S/N856K and S/L891F mutations"` to `"missing the S/N856K and S/L981F mutations"`, matching Table 1 (line 58) and line 84 (`S/981`).
