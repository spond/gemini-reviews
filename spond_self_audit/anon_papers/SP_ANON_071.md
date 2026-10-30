# De-Identified Manuscript: SP_ANON_071

> **Blinding Note:** All title, author, affiliation, journal, and identifier metadata have been scrubbed for unbiased methodological review.

## Abstract & Main Text

## Christoph C Carter


## Gabriel A Wagner


## George K Hightower


## Gemma Caballero


## Pham Phung


## Douglas D Richman


## Sergei L [AUTHOR]


## Davey M Smith

Corresponding author. Tel.: +1 216 789 7059; fax: +1 858 552 7445. [EMAIL_REDACTED] (G.A. Wagner)

Contributed equally to this study.

Issue date 2015 Jan 1.


## Abstract

To better understand the dynamics of HIV-specific neutralizing antibody (NAb), we examined associations between viral genetic diversity and the NAb response against a multi-subtype panel of heterologous viruses in a well-characterized, therapy-naïve primary infection cohort. Using next generation sequencing (NGS), we computed sequence-based measures of diversity within HIV-1 env , gag and pol , and compared them to NAb breadth and potency as calculated by a neutralization score. Contemporaneous env diversity and the neutralization score were positively correlated ( p =0.0033), as were the neutralization score and estimated duration of infection (EDI) ( p =0.0038), and env diversity and EDI ( p =0.0005). Neither early env diversity nor baseline viral load correlated with future NAb breadth and potency ( p >0.05). Taken together, it is unlikely that neutralizing capability in our cohort was conditioned on viral diversity, but rather that env evolution was driven by the level of NAb selective pressure.

Keywords: HIV-1 genetic diversity, Neutralizing antibody, Next generation sequencing, Neutralizing antibody breadth and potency, Viral evolution


## Introduction

Following primary HIV infection, the immune system exerts considerable selection pressure on viral populations ( Bailey et al., 2004 ; Albert et al., 1990 ; Phillips et al., 1991 ). Neutralizing antibodies (NAb) against autologous virus arise early in the course of infection ( Moore et al., 1994 ; Richman et al., 2003 ), leading to the rapid development of viral escape mutants ( Albert et al., 1990 ; Richman et al., 2003 ; Wei et al., 2003 ). A small subset of HIV-infected individuals (10–30%) go on to develop antibodies capable of potently neutralizing a broad array of heterologous HIV isolates ( Mascola and Haynes 2013 ). Although the benefit of a broad and potent NAb response on disease course remains uncertain ( Geffin et al., 2003 ; Carotenuto et al., 1998 ; Piantadosi et al., 2009a ; Doria-Rose et al., 2010 ), animal studies of passive immunity ( Klein et al., 2012 ; Barouch et al., 2013 ) and the isolation of highly broad and potent monoclonal NAb ( Walker et al., 2012 ) have renewed interest in the design of an effective NAb-based HIV vaccine and underscores the need for a better understanding of the natural development of NAb breadth and potency.

The presence and magnitude of the HIV-directed NAb response varies between individuals, and the determinants of this variation remain elusive ( Richman et al., 2003 ; Frost et al., 2005 ). Some studies have suggested that higher viral load may promote a broader NAb response due to greater antigen exposure ( Piantadosi et al., 2009a ; Doria-Rose et al., 2010 ; Deeks et al., 2006 ). Similarly, another study demonstrated a modest correlation between duration of infection and NAb breadth ( Sather et al., 2009 ). Yet another interesting possibility is that greater viral diversity within the host could drive the development of NAb breadth. Using single-copy sequencing to characterize intrasample viral diversity, Piantadosi et al. demonstrated a positive correlation between early-infection env diversity and late-infection NAb breadth ( Piantadosi et al., 2009a ), but not between contemporaneous env diversity and NAb breadth ( Piantadosi et al., 2009c ). Conversely, peak NAb breadth has also been positively correlated with contemporaneous gp160 clonal diversity ( Euler et al., 2012 ). A positive correlation has also been reported between HIV-1 dual infection (which greatly increases env population diversity) and the development of NAb breadth ( Cortez et al., 2012 ). In the present study, we leveraged the greater resolution of next generation sequencing (NGS) to examine the associations between viral genetic diversity and NAb breadth and potency in a well-characterized, antiretroviral therapy (ART)-naive cohort of individuals followed after primary infection.


## Methods


## Study participants and measurement of clinical parameters

This study included participants from the San Diego Primary Infection Cohort between January 1998 and January 2007 who were ART naïve. At all timepoints, CD4 T-cell cell counts (LabCorp) and blood plasma HIV-1 RNA levels (Amplicor HIV-1 Monitor Test; Roche Molecular Systems, Inc.) were quantified. The estimated duration of infection (EDI) was calculated at baseline for each participant, per established protocols ( Barouch et al., 2013 ).


## RNA extraction and viral sequencing

Viral RNA was isolated from cryopreserved plasma, and cDNA was generated as previously described ( Gianella et al., 2011 ; Pacold et al., 2012 ). HIV-1 env C2-V3 (HXB coordinates 6928-7344), gag p24 (HXB coordinates 1366-1618), and pol reverse transcriptase (RT) (HXB coordinates 2709-3242) were PCR amplified with region-specific primers ( Gianella et al., 2011 ; Pacold et al., 2010 , 2012 ). NGS was performed in batches of 16 on a single 454 GS FLX Titanium picoliter plate (454 Life Sciences, Roche, Branford, Connecticut, USA), and each sample was physically separated by rubber gaskets ( Pacold et al., 2012 ; Wagner et al., 2013 , 2014 ). Reads were checked for intersample and lab strain contamination by performing homology searches against each other and against the online public Los Alamos HIV sequence database ( http://www.hiv.lanl.gov/content/sequence/BASIC_BLAST/basic_blast.html ), as previously described ( Butler et al., 2010 ). The cDNA template input into the sequencing reaction was quantified and validated as previously described ( Gianella et al., 2011 ).


## Sequence analysis and bioinformatics

Raw NGS reads were filtered and processed using an updated version of the bioinformatics pipeline described previously ( Pacold et al., 2012 ). Briefly, homology mapping and homopolymer correction was carried out using a codon-aware extension of the Smith–Waterman pairwise alignment algorithm. To distinguish biological variation from sequencing artifacts, we fitted a multinomial mixture model, which allowed us to infer a sample-specific background error rate, and call biological variant as those whose posterior probability of observing a particular configuration of A, C, G and T counts at a site using under the error model was less than 0.001. Having thus filtered instrument errors out, we performed a sliding window phylogenetic analysis (width 210 nt; stride 30 nt), considering only reads which spanned at least 95% of the window (i.e. no haplotype phasing). The MG94xREV codon model was fitted to a neighbor-joining tree inferred for each sliding window, and the mean pairwise synonymous (S) and non-synonymous (NS) diversity (measured as expected substitutions per codon) was measured along this tree ( Noviello et al., 2007 ), in the [SOFTWARE] package ( [AUTHOR] et al., 2005 ). For each NGS sample, we computed the maximum value of S and NS over all sliding windows with median per-position coverage of 500 or greater, and defined the corresponding maximal diversity measures. Assessment of intrasubtype HIV-1 dual infection was performed by NGS using divergence and phylogenetic analysis as previously described ( Pacold et al., 2010 ; Simek et al., 2009 ), and was detected in 2 subjects.


## Neutralizing antibody assays

NAb activity assays were performed by Monogram Biosciences (San Francisco, CA, USA) using a previously-reported in vitro viral neutralization assay ( Richman et al., 2003 ; Deeks et al., 2006 ; Walker et al., 2009 ). Briefly, a firefly luciferase env -null HIV-1 was pseudotyped with each of 6 clinical isolate-derived HIV-1 envelopes representing the major circulating global subtypes (94UG103 [C], 92BR020 [B], JRCSF [B], 93IN905 [A], MGRM-C-026 [C], and 92TH021 [CRF_01 AE]). This cross-clade heterologous panel has been shown to be highly predictive of neutralization breadth on a larger panel ( Simek et al., 2009 ). The same virus was also pseudotyped with the neutralization susceptible lab strain NL4-3 as a positive control and the irrelevant amphotropic Murine Leukemia Virus (aMLV) strain as a negative control. For the neutralization component of the assay, cryopreserved participant serum samples were subjected to serial dilution and incubated with each virus in the panel, as previously described( Walker et al., 2009 ). Viral infectivity was measured by luciferase activity, and titers were calculated as the reciprocal of the plasma dilution conferring 50% inhibition (IC 50 ). Neutralization scores were derived for each plasma sample as the mean of log-transformed IC 50 titers, a measure of both breadth and potency against heterologous viruses ( Simek et al., 2009 ).


## Statistical analysis

For single variable comparisons, p -values were calculated using 2-sided Student’s t -test. Graphs are displayed with one standard deviation error bars. To examine associations between two variables, we performed a two-sided non-parametric Kendall rank correlation tests. This test was selected over other statistical tests (such as Spearman’s rho) due to its more reliable confidence intervals ( Kendall, 1990 ). Parallel analysis using two-sided Spearman’s test yielded identical statistical conclusions with correlation coefficients that were equivalent or higher than those obtained with Kendall’s rank correlation test (data not shown).


## Results

This study included a total of 35 ART-naive subjects, with a median EDI at the time of sampling of 495 days (IQR: 337–932 days). The median CD4 T-cell count at time of sampling was 435 cells/ml (IQR: 314–630 cells/ml), and the median HIV-1 RNA viral load was 4.84log 10 copies/ml (IQR: 4.43 –5.44 log 10 copies/ml). The median calculated cDNA input in the first-round nested PCR was 3.51log 10 copies/10 μl (IQR: 3.10–4.10log 10 copies), and the median coverage of NGS windows yielding the highest divergence estimate with a median nucleotide coverage for gag p24 of 6848 (IQR 578–11,274), pol RT 1881 (IQR 589-3825), and env C2-V3 4170 (IQR 2803-6736). All participants were infected with HIV-1 subtype B virus.

Viral population maximal diversity was significantly higher within env than within gag or pol ( Fig. 1A ). Mean env non-synonymous (NS) diversity was significantly greater than env synonymous (S) diversity, and was also greater than gag or pol-rt NS diversity ( Fig. 1B ). Nucleotide coverage was variable between subjects, but there was no association between median per-position coverage and either max (S) or max (NS) (data not shown, p >0.05 for env C2-V3, gag p24 and pol RT). To assess the validity of the computational diversity metric, we generated neighbor-joining phylogenetic trees from a representative high calculated diversity subject ( Fig. 1C ) and low calculated diversity subject ( Fig. 1D ). This analysis revealed phylogenetic tree morphology congruent with the calculated diversity.


## Fig. 1.

HIV diversity as assessed by next generation sequencing. (A) Maximal sequence diversity across three HIV-1 coding regions. Error bars represent one standard deviation. p -values are reported for 2-sided Student’s t test, with solid lines connecting the compared data items. (B) Mean synonymous (S) and non-synonymous (NS) diversity within three HIV-1 coding regions, with statistics performed as in (A). (C,D) Representative neighbor-joining phylogenetic trees constructed from unique haplotypes within the maximum diversity sliding window for (B) high max (NS) (0.08) and (C) low max (NS) (0.009) within env . The trees are scaled on expected substitutions per nucleotide site. The total proportions of reads represented by a particular haplotype are shown as leaf labels, and also as the area of the node symbol.

To assess the relationship between viral genetic diversity and NAb breadth and potency, we first quantified the neutralization capacity of patient sera against a multi-subtype panel of heterologous HIV primary isolates by computing the neutralization score, which mathematically incorporates the number of viruses neutralized (breadth) and the IC 50 titer level against each heterologous virus (potency) ( Simek et al., 2009 ). We then compared the viral diversity within env , gag , and pol to the neutralization score measured from the same study timepoint, or a timepoint in the course of infection no more than 2 months apart ( N =32, median 0 days, IQR: 0–36.5 days). Comparisons included maximal diversity, mean synonymous diversity (S) and mean non-synonymous diversity (NS). A significant positive correlation was observed between env maximal diversity and neutralization score ( Fig. 2A , τ correlation coefficient=0.36, p =0.0081). NS env diversity was also positively correlated with neutralization score ( Figs. 2B , τ =0.38, p =0.0033), as was S env diversity, albeit to a lesser degree ( Figs. 2B , τ =0.28, p =0.029). No significant association was observed between maximal diversity, NS diversity or S diversity in gag or pol-rt and NAb breadth and potency ( Fig. 2C–F ). To determine whether HIV-1 dual infection confounded the positive associations, we repeated the analysis excluding the two dually infected subjects, and found no major change in the correlations between NS env diversity and neutralization score ( τ =0.36, p =0.007); or S env diversity and neutralization score ( τ =0.30, p =0.025).


## Fig. 2.

Comparison of NAb breadth and potency and contemporaneous gene diversity within three HIV-1 coding regions. (A,C,E) Comparison of 6-virus panel neutralization score versus maximal diversity within env (A), gag (C), and pol (E). (B,D,F) Comparison of neutralization score versus mean pairwise non-synonymous diversity (NS, closed circles) and mean pairwise synonymous diversity (S, open circles) within env (B), gag (D), and pol (F). Correlation coefficients and p -values are derived from a two-sided Kendall rank correlation test. NAb: neutralizing antibody.

To assess whether higher diversity within env earlier in infection would correlate with the development of a broader and more potent NAb response later in the course of infection, env maximal diversity early in infection (mean EDI 1.7 months, IQR: 1.5 – 2.8 months) was compared to the 6-virus panel neutralization score later in infection (median EDI 26.2 months, IQR: 21.5–35.6 months) in a subset of the analyzed cohort ( n =10). This analysis revealed no correlation between future NAb breadth and potency and the baseline env maximal diversity ( Fig. 3A , τ =0.066, p =0.86). Since the subset of subjects analyzed was small, we also analyzed the relationship between env diversity and the contemporaneous neutralization score within the same subset, which mirrored the correlation demonstrated in Fig. 2 ( Figs. 3B , τ =0.78, p =0.0027). Comparing the baseline NS and S env diversity to subsequent NAb breadth and potency revealed no significant associations ( Fig. 3C , NS correlate τ =0.29, p =0.28, S correlate τ =0.37, p =0.37); furthermore, NAb activity was positively correlated with contemporaneous and the NS env diversity ( Fig. 3D , NS correlate τ =0.60, p =0.023), but not with S diversity ( Fig. 3D , S correlate τ =0.36, p =0.17). One subject included in this analysis was confirmed as having HIV dual infection, however exclusion of this subject did not alter the results noted above (baseline env diversity-neutralization score correlate τ =0.087, p =0.83, contemporaneous env diversity-neutralization score correlate τ =0.73, p =0.011).


## Fig. 3.

Comparison of NAb breadth and potency to baseline sequence diversity within env. (A) Comparison of early env maximal diversity and the 6-virus panel neutralization score at a median of 26 months. (B) Comparison of contemporaneous env maximal diversity to the 6-virus neutralization score in the same subjects depicted in (A). (C) Comparison between baseline env mean non-synonymous diversity (NS, closed circles) and baseline mean synonymous diversity (S, open circles) to the neutralization score at a median of 26 months. (D) Comparison of contemporaneous env mean non-synonymous diversity (NS, closed circles) and baseline mean synonymous diversity (S, open circles) to the neutralization score within the same subjects depicted in (C). Tau correlation coefficients and p -values are derived from a two-sided Kendall rank correlation test. NAb: neutralizing antibody.

We next sought to determine whether other clinical variables correlated with the development of NAb breadth and potency as well as the development of env diversity. Comparison of EDI and neutralization score revealed a modest positive correlation ( Figs. 4A , τ =0.28, p =0.038), however exclusion of dual-infected subjects reduced the strength and statistical significance of this correlation ( τ =0.24, p =0.097, data not shown). Similar analyses comparing CD4+ T-cell count and NAb breadth and potency revealed no association ( Fig. 4B ). We also analyzed the relationship between contemporaneous viral load and neutralization score and found no correlation ( Fig. 4C ). To assess whether baseline viral load was predictive of subsequent development of NAb breadth and potency, we compared baseline viral load to neutralization score later in infection (median EDI 27.3 months, IQR 15.5–45.7), and found no correlation ( Figs. 4D , τ =0.023, p =0.88). We performed similar analysis including only subjects with EDI >24 months ( n =18, median EDI 37.6 months IQR 27.3–59.7), and again saw no significant association ( τ =0.21, p =0.25, data not shown). Analysis comparing EDI to the levels of env diversity revealed a significant positive association between maximal diversity and EDI ( Figs. 4E , τ =0.46, p =0.00052). Similarly, EDI was positively correlated with NS env diversity ( figs. 4F , τ =0.31, p =0.019), but not with S env diversity ( τ =0.20, p =0.13).


## Fig. 4.

Comparison of NAb breadth and potency and env diversity to clinical variables. (A–D) Comparison of 6-virus panel neutralization score to estimated duration of infection (A), CD4 T-cell count (B), contemporaneous viral load (C), and baseline viral load (D). (E) Comparison of env maximal diversity to estimated duration of infection. (F) Comparison of env mean non-synonymous diversity (NS, closed circles) and mean synonymous diversity (S, open circles) to estimated duration of infection. Tau correlation coefficients and p -values are derived from a two-sided Kendall rank correlation test. NAb: neutralizing antibody, EDI: estimated duration of infection.


## Discussion

This study utilized NGS to characterize the viral genetic diversity in high resolution from a cohort of individuals followed longitudinally from primary infection. The strongest correlate of the development of HIV-1-specific NAb breadth and potency was contemporaneous non-synonymous viral env sequence diversity, implicating diversifying positive selection of env. As might be expected ( Piantadosi et al., 2009a , 2009b ), there was no evidence of similar selective pressures on gag and pol . Interestingly, we also found that the diversity of env early in the course of infection did not predict subsequent NAb breadth and potency. Although the number of subjects for whom longitudinal analysis could be performed was small, the persistence of a strong association between contemporaneous env diversity and the neutralization score within this subgroup makes lack of sampling power an unlikely explanation for the lack of an association between early env diversity and later NAb breadth and potency.

The data presented here are most consistent with the rapid evolution of env in response to the development of the NAb response ( Richman et al., 2003 ; Frost et al., 2005 ), rather than the development of NAb breadth in response to env diversity. Two participants in this study acquired HIV dual infection which may contribute to viral genetic diversity; however parallel analysis with these subjects excluded did not alter the main observations (except for a decrease in the association between duration of infection and neutralization score). Another potential confounder is selective pressure from the cytotoxic T lymphocyte (CTL) response, but the higher diversity in env compared to gag and pol in this study in combination with the positive association between NAb breadth and potency and env diversity alone suggest a unique selective pressure exerted by the NAb response on env .

Our findings differ from previously reported studies which proposed that NAb development is conditioned upon early env diversity ( Piantadosi et al., 2009a ), however there are key differences between these studies. Firstly, the follow-up for our cohort fell mostly within the first 3 years post-infection before censoring due to ART initiation, while the ART-naive Kenyan cohort ( Piantadosi et al., 2009a ) underwent sampling five years after seroconversion. This could suggest that participants of the present study did not have adequate time for NAb breadth to develop; however this duration of follow-up falls within the timeframe needed for broad NAb development in most individuals ( Mikell et al., 2011 ). Furthermore, seven (24%) participants displayed broad and potent NAb activity (neutralization score >1.0; neutralization of 5–6 out of 6 viruses) at the timepoints studied, similar to the frequency of broadly cross-reactive NAb development reported in other cohorts at later timepoints ( Doria-Rose et al., 2010 ; Sather et al., 2009 ; Mikell et al., 2011 ). A second major difference is the env region characterized in the studies. Our study used NGS with a shorter region of analysis (C2-V3 region, 416 bp) compared to the ~1.2-kb sequences generated with single-copy sequencing in the Kenya study. The region we chose to analyze encompasses key epitopes recognized by highly broad and potent monoclonal NAbs such as 10-1074, VRC24 and the PGT121-like series ( Walker et al., 2010 ; Klein et al., 2013 ). Using a limited region of env allowed for a far more detailed assessment of diversity owing to the greater depth of coverage in the present study (median of 4170 sequences per sample versus 7 sequences in the previous study). One significant limitation in this approach is the exclusion of other major env epitopes targeted by highly broad and potent monoclonal NAbs, including the V1/V2 region and the gp41 membrane proximal external region (MPER). NGS methods capable of accurate sequencing of longer viral genome regions will be needed to better define the relative roles of these regions in NAb breadth development.

Another unexpected finding in this cohort was the absence of an association between the level of HIV RNA or CD4 count and NAb breadth and potency. The literature is inconclusive with regards to the relationship between NAb breadth and CD4 counts, with some studies showing a relationship ( Carotenuto et al., 1998 ), and others not ( Piantadosi et al., 2009a ; Doria-Rose et al., 2010 ). The absence of an association between early viral load and later NAb breadth was unexpected, as several studies have documented such a relationship ( Piantadosi et al., 2009a ; Doria-Rose et al., 2010 ; Sather et al., 2009 ). Interestingly, one study demonstrated the emergence of NAb in patients on ART with suppressed viremia, suggesting that high antigenic stimulus may not be the only driving force behind NAb development ( Medina-Ramirez et al., 2011 ). Our findings suggest that while it is certainly possible that high antigenic exposure can contribute to the development of NAb breadth in some individuals, NAb selective pressure is likewise a potent modulator of viral genetic diversity.

This work was supported by the U.S. Department of Veterans Affairs and grants from the National Institutes of Health: AI090970, AI100665, MH097520, DA034978, AI036214, AI007384, AI047745, AI106039; the International AIDS Vaccine Initiative (IAVI); the National Science Foundation DMS0714991; the James B. Pendleton Charitable Trust.

The funders had no role in the study design, data collection and analysis, decision to publish, or preparation of the manuscript.

We are grateful to all the participants in the San Diego Primary Infection Research Consortium, to Elise Landais and Pascal Poignard for their collaborative insights, to Caroline Ignacio for technical support, and to Demetrius Dela Cruz for his administrative assistance.


## Footnotes

Chaillon et al. (2013) .
