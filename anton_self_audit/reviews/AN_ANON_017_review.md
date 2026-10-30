# Review of AN_ANON_017

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript audits the analytical transparency and data availability of the four initial genomic studies of SARS-CoV-2 and demonstrates a fully open, reproducible reanalysis pipeline executed on public high-throughput infrastructure using BioConda tools, a global web-based workflow platform, and Jupyter notebooks. Using the six raw sequencing read datasets publicly available as of February 19 of the outbreak year (updated to 28,973 raw datasets at proof stage), the authors perform five stages of analysis: (1) host/adapter read filtering and de novo assembly with SPAdes and Unicycler (recovering a 29,781-bp contig with 100% identity to `NC_045512`); (2) root-to-tip regression dating of the SARS-CoV-2 MRCA (estimating October 24 of the preceding year); (3) intrahost single-nucleotide variant (iSNV) calling at a $\ge 5\%$ minor allele frequency cutoff, identifying 39 SNVs across the six samples and highlighting a 38% allele-frequency Lys921Gln substitution in Spike HR1 (`SRR10903401`) predicted to disrupt a salt bridge with Gln1188 in HR2; (4) GARD recombination screening along the *S* gene (showing that breakpoints previously proposed by Wu et al. lack statistical support); and (5) branch-site positive selection testing (aBSREL), reporting diversifying selection on ~7% of *S* gene sites along the ancestral branch leading to SARS-CoV-2.

The manuscript's central message—that infectious disease emergencies require immediate deposition of raw sequencing reads and fully parameterized, version-locked open workflows—is timely, well-argued, and exemplary in its own reproducibility (providing live workflow histories across four international servers, GitHub repositories, and Zenodo DOIs). However, several of the illustrative evolutionary and structural analyses in the main text have methodological and biophysical flaws: (1) in the Spike HR1/HR2 analysis (line 30), the authors claim that Lys921 forms a "salt bridge with Gln1188 within HR2," which is biophysically incorrect because Glutamine (Gln) is a neutral polar amide residue incapable of forming an ionic salt bridge; (2) applying aBSREL across deeply diverged sarbecovirus lineages (SARS-CoV-2, SARS-Tor2, ZC45, ZXC21, Rp3) on the whole *S* gene without masking recombinant segments or accounting for synonymous substitution saturation ($d_S$ saturation) risks false-positive branch-site selection signals; and (3) the root-to-tip MRCA point estimate (October 24) is reported without a confidence interval or temporal signal ($R^2$) diagnostic. Correcting the biophysical description of the HR1/HR2 interaction and adding uncertainty bounds and recombination/saturation caveats to the evolutionary analyses will make the empirical case studies as rigorous as the reproducibility advocacy.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Early SARS-CoV-2 genomic publications lacked raw read sharing and parameter documentation, but end-to-end genome assembly and variation analysis can be fully reproduced on open public infrastructure: [Well Supported].**  
  Table 1 and S1 Table accurately document the missing raw reads, unstated parameters, and tool misdescriptions (such as listing FreeBayes as a de novo assembler in reference 4) across the initial reports. The authors' Unicycler/SPAdes assembly workflow reconstructs the full 29,781-bp genome with 100% identity to `NC_045512`, and all workflows, parameters, and histories are openly archived on GitHub and Zenodo.

* **Previously reported recombination breakpoints within the SARS-CoV-2 *S* gene between Bat ZC45/ZXC21 and SARS-Tor2/SZ3 lack robust statistical support under GARD: [Moderately Supported].**  
  Re-evaluating the specific 5-taxon alignment from Wu et al. [3] with GARD (Figure 3) appropriately shows that the proposed breakpoints in that specific alignment are not statistically supported, though broader sarbecovirus recombination across the RBD is not ruled out given the tiny taxon sample.

* **The intrahost Spike substitution Lys921Gln (38% frequency in `SRR10903401`) prevents the formation of a "salt bridge with Gln1188 within HR2": [Methodologically Flawed].**  
  While the detection of the A-to-C intrahost variant at 38% allele frequency in `SRR10903401` is supported by the read mapping workflow, the biophysical interpretation on line 30 ("The Lys 921 Gln substitution we observed is located in HR1 and forms a salt bridge with Gln 1188 within HR2... The Lys 921 Gln change would prevent the formation of the salt bridge with Gln 1188") is chemically inaccurate. A salt bridge requires two oppositely charged ionizable side chains (e.g., cationic Lys/Arg/His with anionic Asp/Glu). Glutamine (Gln) is uncharged at physiological pH; a Lys–Gln interaction is a hydrogen bond, not a salt bridge (and Gln921–Gln1188 can also form a side-chain hydrogen bond, as seen in the distantly related alphacoronaviruses TGEV, PRCV, CCV, FIPV, and PEDV cited by the authors themselves).

* **Statistically significant positive diversifying selection acted on ~7% of *S* gene sites along the ancestral branch leading to SARS-CoV-2 (aBSREL): [Fragile].**  
  In line 43 and Figure 4, the authors run aBSREL on a 5-taxon codon alignment (SARS-CoV-2, SARS-Tor2, Bat ZC45, ZXC21, and Rp3) across the entire *S* gene. However, ZC45/ZXC21 and SARS-Tor2/Rp3 have mosaic evolutionary histories across the S1/RBD versus S2 regions (violating the single-tree assumption of codon models) and exhibit substantial synonymous divergence ($d_S > 1$) along the internal branches separating SARS-CoV-1-like and SARS-CoV-2-like lineages. Running aBSREL on an unpartitioned *S* gene alignment with only 5 sequences without testing for recombination partitioning or $d_S$ saturation makes the inferred $\omega > 1$ class on the ancestral SARS-CoV-2 branch highly fragile.

* **Root-to-tip regression dates the SARS-CoV-2 MRCA to October 24: [Fragile].**  
  In line 26, the authors apply simple ordinary least squares root-to-tip regression to deduplicated sequences up to February 16 and report a single point estimate (October 24) with no 95% confidence interval, no regression slope (substitution rate), and no $R^2$ or date-randomization test to quantify clock-like temporal signal in an early, low-diversity alignment.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Biophysical Characterization of the Lys921–Gln1188 Interaction in Spike HR1/HR2
* **WHY:** Stating that Lys921 and Gln1188 form a "salt bridge" (line 30, Figure 2 legend) is a fundamental biochemistry error because Glutamine is neutral and cannot form an ionic bond; furthermore, reference 14 describes this position as forming a hydrogen-bonded polar contact (or salt bridge in coronaviruses where the partner residue is Glu/Asp, not Gln).
* **WHAT:** Revise line 30 and the Figure 2 caption to accurately describe the Lys921–Gln1188 contact as a hydrogen bond / polar interaction rather than a salt bridge, and note that a Lys-to-Gln substitution preserves hydrogen-bonding potential (consistent with the conserved Gln–Gln pair in alphacoronaviruses shown in Figure 2).
* **HOW:** Replace "salt bridge" with "hydrogen bond (polar contact)" on lines 30 and 36, and verify the exact atomic distance and hydrogen-bonding geometry in the prefusion and postfusion six-helix bundle structures of SARS-CoV-2 Spike (e.g., PDB 6VSB and 6LXT).

#### 2. Report Confidence Intervals and Temporal Signal Diagnostics for the MRCA Estimate
* **WHY:** A single root-to-tip regression point date ("October 24", line 26) calculated on sparse early pandemic genomes (up to Feb 16) carries wide statistical uncertainty that is hidden when no confidence interval or $R^2$ is reported.
* **WHAT:** Report the root-to-tip correlation coefficient ($R^2$), estimated evolutionary rate (substitutions per site per year), and 95% confidence interval around the October 24 MRCA date.
* **HOW:** Extract the regression statistics and parametric/bootstrap 95% CI directly from the root-to-tip regression notebook in directory `(3) estimation of MRCA timing` and include them in line 26.

#### 3. Partition the aBSREL Selection Analysis by Recombination Blocks and Report $p$-Values / $\omega$ Estimates
* **WHY:** Running aBSREL on the full-length *S* gene across 5 diverged sarbecoviruses (line 43) ignores known discordant phylogenetic histories between the RBD and the rest of Spike and does not report the actual likelihood ratio test (LRT) $p$-value or $\omega$ value in the text.
* **WHAT:** Partition the codon alignment according to the GARD recombination segments (or separate S1/RBD from S2) before running aBSREL, and report the exact LRT $p$-value, $\omega$ estimate, and branch length ($d_S$) for the ancestral SARS-CoV-2 branch.
* **HOW:** Run the GARD-partitioned alignment through aBSREL in [SELECTION_PACKAGE], report the Holm-Bonferroni corrected $p$-value and $\omega_2$ rate in line 43, and add a caveat noting that sparse taxon sampling (5 sequences) and deep divergence between ZC45/ZXC21 and SARS-CoV-2 in the RBD can inflate branch-site $\omega$ estimates.
