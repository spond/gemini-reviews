# Review of AN_ANON_016

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.5 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript describes the implementation of a genome-wide protein-protein interaction (PPI) prediction and multimeric structural modeling pipeline—based on the SPRING, HHsearch, PSI-BLAST, and TM-align tools—within a public web-based workflow platform. Using 170,860 PDB entries (988,784 interacting chain pairs mapped to 58,900 PDB70 monomeric entries), the pipeline threads query protein sequences against PDB70 and scores putative dimeric complexes using the minimum monomeric threading Z-score ($Z_{\text{com}}$) and an interface model score ($\text{SM-score}$, combining TM-score and a knowledge-based contact potential $E_{\text{contact}}$). The authors evaluate the pipeline on the human (20,610 genes; ~212 million pairs) and yeast (6,045 genes; ~18 million pairs) proteomes against 10 experimental BioGRID assays using Matthews correlation coefficient (MCC), and apply it to predict human interaction partners for SARS-CoV-2 Nsp3 papain-like protease (PLpro) and Spike (S) receptor-binding domain (RBD), highlighting putative complexes of S with myelin-oligodendrocyte glycoprotein (MOG) and dipeptidyl peptidase-4 (DPP4).

While packaging template-based docking tools into an accessible, shareable workflow is a useful software engineering contribution, the manuscript's validation design and biological claims regarding SARS-CoV-2 receptor binding suffer from major methodological flaws. First, the human and yeast BioGRID benchmark lacks any temporal or sequence-identity holdout between the PDB template library and the BioGRID test set, meaning that complexes already crystallized in the PDB (and deposited in BioGRID) are trivially recovered by self-matches. Second, the negative test set is constructed from proteins in different subcellular compartments while the authors explicitly refuse to filter SPRING predictions by subcellular localization (line 97), creating an asymmetric evaluation artifact. Third, the novel structural models of SARS-CoV-2 Spike RBD binding to MOG (Table 2, Figure 3) are built by threading MOG—an immunoglobulin V-set domain protein—onto anti-SARS-CoV-2 neutralizing antibodies (CC12.1, CC12.3, CB6/7C01, B38/7BZ5) and a synthetic nanobody (Sybody SR4, 7C8V) purely because they share a conserved immunoglobulin beta-sandwich fold, mistaking generic Ig-fold homology for specific receptor binding. Substantial re-analysis with strict sequence/template holdouts and careful reframing of the Ig-fold false-positive complexes are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The SPRING workflow achieves genome-wide PPI prediction performance on Human and Yeast comparable to or better than experimental methods in BioGRID: [Methodologically Flawed].**  
  First, the pipeline builds its multimeric template library from all 170,860 PDB entries up to November 29 (line 129) using PSI-BLAST ($E \le 0.001$) and HHsearch, and then evaluates MCC against BioGRID experimental subsets without holding out test pairs that are identical or closely homologous to the PDB templates used for prediction (data leakage). Second, to construct the negative non-interacting set, the SPRING MCC tool samples protein pairs from *different* subcellular regions (lines 17, 97, 144), whereas the positive BioGRID sets are predominantly co-localized proteins, and SPRING predictions are not filtered by localization (line 97). Third, the authors state on line 17 that they ran SPRING on "20,610 raw protein coding sequences without separating the individual proteins using the CDS record... In total the 20,610 protein coding genes encode for about 75,776 individual proteins," leaving it unclear whether isoforms were concatenated or how gene-level vs. isoform-level mappings were resolved against BioGRID UniProt IDs.

* **Identification of human ubiquitin-like substrates (ISG15, UBB, UBC, etc.) interacting with SARS-CoV-2 Nsp3 papain-like protease: [Well Supported].**  
  Table 1 recovers ISG15 ($\text{SM} = 1.11, \text{TM} = 0.96$) and ubiquitin/ubiquitin-like proteins (UBB, UBC, SUMO3, UBD, ELOB, MIDN) as top hits for Nsp3 PLpro. However, as Table 1 itself shows, these predictions directly use the co-crystal structures of SARS-CoV-2 PLpro bound to ISG15 and ubiquitin (PDB 6XAA and 6XA9, Klemm et al. [49]) and SARS-CoV-1 PLpro complexes (5TL7, 5W8T, 5WFI) as templates. Thus, for ISG15 and UBB/UBC, the pipeline is recovering known co-crystal templates already present in the PDB rather than performing de novo discovery, and for the remaining ubiquitin-domain proteins, it is detecting homology of their ubiquitin-like domains to ubiquitin.

* **SARS-CoV-2 Spike RBD forms high-confidence complexes with myelin-oligodendrocyte glycoprotein (MOG) via two distinct binding modes that may explain MOGAD relapse: [Methodologically Flawed].**  
  In Table 2 and Figure 3, all five multimeric templates used to model the Spike RBD–MOG interaction are crystal structures of SARS-CoV-2 RBD bound to neutralizing monoclonal antibodies (6XC2 = CC12.1; 6XC4 = CC12.3; 7C01 = CB6; 7BZ5 = B38) or a synthetic camelid nanobody (7C8V = Sybody SR4). MOG is an immunoglobulin (Ig) superfamily protein containing an extracellular Ig V-set beta-barrel domain. HHsearch threads MOG onto the variable heavy/light ($V_H / V_L$) Ig domains of these anti-SARS-CoV-2 antibodies because all Ig domains share a conserved beta-sandwich framework ($Z = 45.8$–$55.3$). However, antibody binding to SARS-CoV-2 RBD is mediated by hypervariable complementarity-determining region (CDR1–3) loops evolved specifically by somatic hypermutation/selection against Spike, which MOG does not possess. Confirming this, the interface contact energies ($E_{\text{contact}}$) for the antibody-templated MOG models in Table 2 are weak ($-2.54$ to $-3.53$, compared to $-15.07$ to $-24.14$ in Table 1). Treating generic Ig-framework threading onto affinity-matured anti-Spike antibodies as evidence of a physiological Spike–MOG receptor complex is a classic template-based docking artifact.

* **SARS-CoV-2 Spike RBD interacts with human DPP4 at shared MERS-CoV and novel binding sites: [Overstated].**  
  The pipeline generates a homology model of SARS-CoV-2 RBD on DPP4 using the MERS-CoV RBD–DPP4 co-crystal structures (PDB 4KR0 and 4L72; line 75). However, the structural alignment quality is low ($\text{TM-score} = 0.62$, $\text{SM-score} = 0.69$, $E_{\text{contact}} = -6.7$), reflecting the substantial structural divergence between the receptor-binding motifs of MERS-CoV and SARS-CoV-2. In the absence of experimental binding validation (where empirical studies have shown that SARS-CoV-2 RBD utilizes ACE2 and does not bind human DPP4 with physiological affinity), presenting residue-level contact predictions (T186, T282, S334 in Table 3) as established interactions is overstated.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Template Data Leakage in the Human and Yeast BioGRID Benchmarks
* **WHY:** Evaluating a template-based PPI predictor (built on the entire PDB up to Nov 2020) against BioGRID without removing test pairs that share high sequence identity with the PDB multimeric templates inflates the apparent MCC via memorization of known structures.
* **WHAT:** Re-run the Human and Yeast MCC benchmark under strict sequence-identity holdout thresholds (e.g., excluding any PDB multimeric template where both chains share $>30\%$ or $>40\%$ sequence identity with the query protein pair, or using a strict temporal split).
* **HOW:** Filter the 4-column lookup table generated by `SPRING Map` to remove homologous self-hits at $30\%$, $50\%$, and $70\%$ sequence identity cutoffs before running `SPRING Min-Z` and `SPRING MCC`, and plot the resulting MCC curves alongside the unfiltered curve in Figure 1.

#### 2. Symmetrize Subcellular Localization Filtering in the MCC Evaluation
* **WHY:** Constructing the negative test set exclusively from protein pairs localized in different subcellular compartments while leaving positive test sets and SPRING predictions unfiltered (lines 97, 144) confounds interaction prediction with compartment co-localization.
* **WHAT:** Evaluate MCC using both (a) uniformly sampled random negative pairs from the same subcellular compartments as the positive pairs and (b) compartment-stratified negative pairs with identical compartment filtering applied across all methods.
* **HOW:** Update the `SPRING MCC` evaluation script to report precision-recall (AUPRC), ROC-AUC, and MCC across multiple Z-score thresholds under matched intra-compartment negative sampling.

#### 3. Control for Immunoglobulin-Fold False Positives in the SARS-CoV-2 Spike–MOG Prediction
* **WHY:** Any human protein containing an immunoglobulin V-set or C-set domain (hundreds of human cell-surface proteins, including MOG, CD4, CD8, PD-1, and ICAMs) will align with high HHsearch Z-scores ($Z > 40$) to the $V_H/V_L$ framework of neutralizing antibodies crystallized with SARS-CoV-2 Spike RBD (6XC2, 6XC4, 7C01, 7BZ5).
* **WHAT:** Explicitly test how many other human Ig-superfamily proteins score similarly on these antibody templates, and reframe the MOG result as an illustrative structural homology match to Ig frameworks rather than a specific receptor interaction.
* **HOW:** Inspect the full list of human Spike interactors produced by the pipeline to count how many top hits use antibody-RBD templates (6XC2, 6XC4, 7C01, 7BZ5, 7C8V), exclude synthetic/antibody-antigen complexes (`REMARK` / SabDab annotation) when predicting endogenous host-receptor interactions, and revise the Abstract, Results (lines 54–68), and Discussion (line 95) accordingly.

#### 4. Restore the Missing SM-Score Equation and Clarify CDS Input Handling
* **WHY:** On line 149, the mathematical equation defining the SPRING model score (`SM-score`) is completely missing (blank line between line 148 and line 150), and line 17 states that 20,610 human genes encoding 75,776 proteins were parsed "without separating the individual proteins using the CDS record."
* **WHAT:** Insert the missing `SM-score` formula on line 149 and clarify exactly what FASTA sequences were fed into HHsearch for the 20,610 human genes.
* **HOW:** Add the explicit equation $\text{SM-score} = \text{TM-score} - w_0 E_{\text{contact}}$ (with $w_0 = 0.01$) on line 149, and specify in the Results/Methods whether one canonical UniProt isoform per gene (20,610 sequences) or concatenated multi-isoform sequences were threaded.
