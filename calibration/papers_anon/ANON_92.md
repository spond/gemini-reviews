# De-Identified Manuscript `ANON_92`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## ABSTRACT

Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) has had an unprecedented impact on human health and highlights the need for genomic epidemiology studies to increase our understanding of virus evolution and spread and to inform policy decisions. We sequenced viral genomes from over 22,000 patient samples tested at Mayo Clinic Laboratories between 2020 and 2022 and used Bayesian phylodynamics to describe county and regional spread in Minnesota. The earliest calculated introduction into Minnesota was to Hennepin County from a domestic source around 22 January 2020; 6 weeks before the first confirmed case in the state. This led to the virus spreading to Northern Minnesota and, eventually, the rest of the state. International introductions were most abundant in Hennepin (home to the Minneapolis/St. Paul International Airport) totaling 45 (out of 107) over the 2-year period. Southern Minnesota counties were most common for domestic introductions, with 19 (out of 64), potentially driven by bordering states such as Iowa and Wisconsin as well as Illinois, which is nearby. Hennepin also was, by far, the most dominant source of in-state transmissions to other Minnesota locations ( n = 772) over the 2-year period. We also analyzed the diversity of the location source of SARS-CoV-2 viruses in each county and noted the timing of state-wide policies as well as trends in clinical cases. Neither the number of clinical cases nor the major policy decisions, such as the end of the lockdown period in 2020 or the end of all restrictions in 2021, appeared to have an impact on virus diversity across each individual county.


### IMPORTANCE

We analyzed over 22,000 severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) genomes of patient samples tested at Mayo Clinic Laboratories during a 2-year period in the COVID-19 pandemic, which included Alpha, Delta, and Omicron variants of concern to examine the roles and relationships of Minnesota virus transmission. We found that Hennepin County, the most populous county, drove the transmission of SARS-CoV-2 viruses in the state after including the formation of earlier clades including 20A, 20C, and 20G, as well as variants of concern Alpha and Delta. We also found that Hennepin County was the source for most of the county-to-county introductions after an initial predicted introduction with the virus in early 2020 from an international source, while other counties acted as transmission “sinks.” In addition, major policies, such as the end of the lockdown period in 2020 or the end of all restrictions in 2021, did not appear to have an impact on virus diversity across individual counties.

KEYWORDS: epidemiology, computational biology, SARS-CoV-2, Minnesota, high-throughput nucleotide sequencing


## INTRODUCTION

Genomic epidemiology has provided valuable insight into the transmission, evolution, and public health surveillance of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), the cause of coronavirus disease 2019 (COVID-19). This has been feasible, in large part, due to unprecedented viral genomic sequencing efforts across the globe. As of 29 July 2023, there are over 15.8 M virus sequences in GISAID ( 1 ) and over 8.1 M in NCBI Virus ( 2 ) and GenBank ( 3 ). Studies that focus on localized spread such as counties or regions within a state or province can highlight and uncover transmission events that could inform statewide surveillance and prevention efforts. However, there have been limited SARS-CoV-2 genomic epidemiology studies at this geographic level in the United States. Work by Moreno et al. ( 4 ) examined the evolution and spread of SARS-CoV-2 among two counties (Dane and Milwaukee) in Wisconsin, from the start of the pandemic until the end of April 2020, based on the analysis of 247 new full-length SARS-CoV-2 genomes combined with sequences in GISAID. Using this data, they derived county data on synonymous and non-synonymous single nucleotide variants (SNVs), performed a variety of phylogenetic analyses (using Nextstrain [ 5 ] and BEAST2 [ 6 ]), determined R0 for their region, and examined the number and timing of introductions to the two counties and how each introduction subsequently impacted the local transmission ( 4 ). The authors were ultimately able to conclude that early transmission within Dane County was not due to its initial introduction followed by local spread, but rather multiple later introductions into the region ( 4 ). In other work, Deng et al. ( 7 ) sequenced 36 clinical samples from different counties in Northern California, sourced from the California Department of Public Health, Santa Clara County Public Health Department, and the University of California San Francisco. Their phylogenetic analysis revealed multiple California clusters including Santa Clara County, Solano County, and San Benito County, as well as lineages from Washington State and Europe ( 7 ). They also identified several early notable SNVs including D614G in the Spike protein ( 7 ). Work by Müller et al. ( 8 ) examined SARS-CoV-2 introduction and spread in the State of Washington including at the county level early in the pandemic from February to July 2020 with a focus on the 614G variant and Google workplace mobility data. Alpert et al. ( 9 ) created county-level risk maps for international importation of early Alpha variants via air transport. More recently, Smith et al. ( 10 ) examined the transmission of the Omicron variant among four counties in Arizona. Other works such as Valesano et al. ( 11 ), Holland et al. ( 12 ), Currie et al. ( 13 ), and Srinivasa et al. ( 14 ) examined spread on college campuses.

Although these studies have provided within-state snapshots into the genomic epidemiology of SARS-CoV-2, they did not consider how localized evolution and spread within a state changed over multiple years of the pandemic with the introduction and circulation of different variants of concern such as Alpha, Delta, and Omicron. Here, we leveraged amplicon-based high-throughput sequencing and Bayesian phylodynamics to analyze the evolution and spread of SARS-CoV-2 into, and within, the State of Minnesota to understand the roles of specific counties and regions in the transmission of the virus over a 2-year period and across different viral clades, variants of concern (VoC), and state-wide mandates and policies.


## MATERIALS AND METHODS


### RNA extraction, library preparation, and next-generation sequencing

From March 2020 to March 2022, we analyzed patient nasopharyngeal or mid-nasal turbinate swabs that tested positive for COVID-19 via RT-qPCR at Mayo Clinic Laboratories and had a Ct value of 28 or lower. We extracted viral RNA on the Hamilton Microlab STAR Automated Liquid Handler system (Hamilton Company, Reno, NV, USA) with the use of Promega Maxwell HT Viral TNA Kit (Fitchburg, WI, USA). We generated libraries using the COVIDSeq Test reagent kit from Illumina (San Diego, CA, USA) following the manufacturer’s instructions. We sequenced the pooled libraries as 100 × 2 paired-end reads using the NovaSeq SP sequencing kit and Xp 2-Lane kit with NovaSeq Control Software v1.6.0. We used the Illumina RTA version 3.4.4 for base-calling.

We de-multiplexed raw sequence data into individual sample fastq files using bcl2fastq2-v2.19.0 ( 15 ). We used Illumina’s Dynamic Read Analysis for GENomics (DRAGEN) COVID Lineage software and pipeline ( 16 ) (versions 3.5.1, 3.5.3, and 3.5.6) for reference-based alignment to Wuhan-1 ( 17 ), quality assessment, variant calling, and generation of consensus sequences. We excluded sequences from downstream analysis if they met any of the following criteria, including: (i) given an overall score of fail by the DRAGEN pipeline due to having an insufficient amount of detectable viral reads; (ii) given an overall quality score by Nextclade ( 18 ) as bad; (iii) potentially contaminated based on the presence of unusual allele frequencies (<0.9); (iv) duplicate runs; and (v) positive or negative controls.


### Phylogenetic analysis of SARS-CoV-2

We assembled a representative data set ( n = 6,188; Fig. S1) that included SARS-CoV-2 genome sequences from the 20 counties with the greatest number of reported COVID-19 cases as of 28 February 2022 as well as a global representation of sequences available via GenBank as part of an open access data set from Nextstrain (Table S1) ( 19 ). We used the list of accessions to download sequences from NCBI Virus ( 2 ). All but two of the genomes were ≥ 29,000 nucleotides in length. We also removed duplicates.

We included sequences from December 2019 (including Wuhan-1) to 28 February 2022, as well as their sampling location and collection date metadata. To partially address sampling bias, we sampled at a rate of five sequences per 1,000 county cases and used the filter module in augur ( 20 ) to distribute (as equally as possible) our heterochronous sequences by month (Fig. S1). For each county, we attempted to include SARS-CoV-2 genomes across the 2-year timeframe by supplementing our data set with sequences provided by the Minnesota Department of Health (MDH) (and available in GISAID). The MDH sequences were produced from randomly selected samples from clinics and community testing sites. Sample Ct values were equal to or below 30.

We aligned all sequences using MAFFT ( 21 ) and used trimAl v1.4.rev22 ( 22 ) to remove columns that contained more than 70% gaps. We created an initial phylogenetic tree via Nextstrain’s augur tree command ( 20 ) with IQTree and rooted the tree based on Wuhan-1 ( 17 ). We used TempEST ( 23 ) to examine the temporal signal of our heterochronous samples, which suggested the use of a strict molecular clock (correlation coefficient = 0.958) for our phylogenetic analysis. We also removed one sequence as an outlier. We used augur refine and the keep-root option to modify our tree with sequence metadata. We removed additional sequences that had potentially misassigned clades or produced inconsistencies with the phylogenetic structure as shown in Nextstrain’s global all-time subsampled data set ( 24 ).


### Phylodynamics of SARS-CoV-2 in Minnesota

We used R package ape (30) to confirm that our starting tree was rooted and non-bifurcating in order to comply with our downstream inferencing framework. For Bayesian inference, we leveraged a pre-release of BEAST v1.10.5 (ThorneyTreeLikelihood v0.1.1) and BEASTGen v0.3 (pre-thorney) to specify a more efficient likelihood function intended for larger sequence data sets ( 25 , 26 ). We used our starting tree, a non-parametric Bayesian SkyGrid coalescent model for our tree prior ( 27 ), and a strict molecular clock. We ran two Markov-chain Monte Carlo (MCMC) simulations each for 5 × 10 8 steps and sampling every 5 × 10 4 steps. We combined these two runs via LogCombiner v.10.4 ( 28 ) after removing 10% burn-in. We checked for convergence of model parameters via Tracer v1.7.1 ( 29 ) with an ideal effective sample size threshold of 200. We generated log marginal likelihoods and evaluated population growth priors via a stepping stone and path sampling procedure ( 30 ). Our results suggested the use of the non-parametric Skygrid tree prior over a constant growth model (Table S2).

We used LogCombiner to sample 1,000 trees from the posterior distribution and used this as empirical data for ancestral state reconstruction of our location trait. We specified all non-U.S. sequences as “international” and non-Minnesota U.S. states as “USA.” For computational efficiency, we kept the five counties with the greatest number of cases as independent locations and grouped the remaining 15 counties into three discrete regions including southern, central, and northern Minnesota (Table S1). In BEAUti ( 28 ), we specified an asymmetric transmission rate matrix of K ( K *1), where K is equivalent to the number of discrete locations ( n = 10 for our data set). We recorded Markov jumps ( 31 ) between locations to estimate the timing and source of introductions and specified an MCMC of 5 × 10 6 sampling every 5 × 10 2 steps. We used TreeAnnotator v.10.4 ( 28 ) to create a single maximum clade credibility (MCC) tree after a 10% burn-in. We used Baltic ( 32 ) for tree visualization and to extract the timing of discrete location transitions along the branches of the MCC for our estimates of introductions. For the latter, we estimated the time-point of the middle of the branch between the current node and its parent for any change in location state. We excluded transmission chains with low support of discrete origin and destination names by including only nodes with a posterior probability of ≥0.90 for the location state. We used SpreadD3 ( 33 ) to calculate the Bayes factors to identify the most parsimonious origin-destination scenarios (Table S3; Fig. S2). We used two programs of the BEAST library ( 28 ), introduced in reference ( 34 ), as part of our Bayesian phylodynamic analyses. TreeMarkovJumpHistoryAnalyzer samples from the posterior distribution of trees to collect the timing and location of each Markov jump ( 34 ). We used the output from this program to calculate the ratio of introductions to total viral flow into and out of each county [number of introductions/(number of introductions + number of exports)] as described in Lemey et al. ( 34 ) as well as the visualization of the weights of pairwise transmission between counties via a chord diagram. TreeStateTimeSummarizer, which also samples from the posterior distribution of trees, notes the contiguous partitions for a given discrete state ( 17 ). We used the output from this program to calculate the normalized Shannon diversity metric ( 34 ). We used this measure to assess the level of location diversity for the viruses within each county during a specified time period. For our analysis, we used the NormShannon method in the R package QSutils ( 35 ) to calculate normalized monthly diversity metrics for each county and HDinterval ( 36 ) for the corresponding 95% highest posterior density region.


## RESULTS

We sequenced SARS-CoV-2 genomes from genomic material collected from clinical samples of patients tested for SARS-CoV-2 infection at Mayo Clinic Laboratories ( Fig. 1 ; Fig. S3) over a 2-year period from March 2020 to March 2022. We combined these sequences with additional genomes generated for surveillance purposes by the MDH and performed Bayesian phylodynamics to understand in-state spread as well as the impact and timing of introductions into the State of Minnesota (see Materials and Methods).


### Fig 1.


> **Figure/Table Caption:** County map of Minnesota with number of sequences ( N = 76,875) eligible for analysis by source. ( A ) New sequences ( N = 21,669) generated from this study at Mayo Clinic Laboratories with a known sampling location in a Minnesota county. Olmsted County in Southeast Minnesota (where the Mayo Clinic Rochester campus is located) has the largest number of sequences. ( B ) Sequences ( N = 55,206) available on GISAID with county metadata provided by the MDH. Hennepin County (the most populated county), north of Olmsted, has the largest number of sequences.

Most of the patients from whom we collected a biological specimen and generated a SARS-CoV-2 genome resided in the state of Minnesota (96%) (Table S4). The breakdown by gender was nearly 50/50 between males and females, while 50% of the patients was between 18 and 45. Fifteen percent was under 18, while 11% was 65 or older.


### Hennepin County consistently drives in-state transmission

We down-sampled our genomes from Minnesota nearly proportional to the number of COVID-19 cases per county and then added additional genomes from NCBI GenBank ( 3 ) as part of an international data set used in Nextstrain ( 5 ) (see Materials and Methods). To address the computational burden of adding sequences to our already large data set, we aggregated the additional samples into discrete traits international and USA and grouped counties with less sequences into areas in the state such as southern, central, and northern Minnesota (Fig. S4; Table S1).

We implemented Bayesian phylodynamic models to examine the transmissions in Minnesota from early 2020 to early 2022 (see Materials and Methods). We recorded Markov jumps ( 31 ) to estimate the timing of introductions and their directionality. After introductions from domestic and international locations, our analysis shows that Hennepin County, the most populous county which includes Minneapolis, the most populated city, drove the transmission of SARS-CoV-2 viruses in the state ( Fig. 2 ). This includes the formation of earlier clades including 20C and 20G, as well as variants of concern Alpha and Delta ( Fig. 2A ). The counties in central Minnesota contributed to spread including 20C, Alpha, and Delta, while southern Minnesota contributed mostly to 20G. Markov jump estimates ( Fig. 2B ) as shown via a Chord diagram suggest that transmission of SARS-CoV-2 within the state largely originated from Hennepin County (thick arcs and wider fragments at the outer circle). However, we also note the existence of transmission back to these areas (white space between arc points and outer fragment) from nearby counties in central Minnesota.


#### Fig 2.


> **Figure/Table Caption:** SARS-CoV-2 evolution and spread to and within the state of Minnesota. ( A ) MCC tree of 6,188 SARS-CoV-2 genomes from Minnesota counties and regions as well as international locations and other domestic locations in the United States, with manually annotated clades by Nextclade-assigned names or VoCs ( 18 ) using lowercase Greek letters. Less well represented VoCs in the tree (e.g., Gamma or Epsilon) are unlabeled. For clades (e.g., 20A) that are not monophyletic in the tree, the most populous clade is labeled. ( B ) Markov jumps between locations represented as a Chord diagram. Colors for both panels represent locations depicted in the legend. Central MN includes seven Minnesota counties: Benton, Carver, Chisago, Kandiyohi, Sherburne, Stearns, and Wright. Northern MN includes three counties: Clay, Crow Wing, and Saint Louis. Southern MN includes five counties: Blue Earth, Goodhue, Olmsted, Rice, and Scott. USA includes all states except for Minnesota. MN, Minnesota; α , alpha; δ , delta; and O , omicron. Panels A and B, legend, and text labels were recreated in Adobe Illustrator for visualization purposes.

We measured the ratio of introductions to total viral flow into and out of each county by month from March 2020 to January 2022. A value of 1 suggests a county as solely being a “sink” (accepts SARS-CoV-2 lineages but never exports them to other counties), while a value of 0 indicates a county as solely being a “source.” Anoka, Dakota, Ramsey, northern Minnesota, southern Minnesota, and Washington were fueled by introductions mostly throughout the pandemic ( Fig. 3 ). Meanwhile, central Minnesota (outside of Hennepin and Ramsey) was dominated by introductions early in the pandemic but later in 2020 experienced brief trends of higher virus exportation. Hennepin County showed a drastically different trend than all others as it consistently acted as a source for other Minnesota counties over the nearly 2-year period. However, it did experience brief periods of fluctuation such as a spike in the ratio of introductions towards the end of 2020 and early 2021, potentially driven by the dominance of out-of-state introductions.


#### Fig 3.


> **Figure/Table Caption:** Ratio of introductions to total viral flow into and out of each discrete location by month from March 2020 to January 2022. The posterior mean ratio and 95% Bayesian highest posterior density interval are shown. Anoka, Dakota, Ramsey, and Washington have wider intervals during certain months, such as January 2022, due to a decrease in local sampling.


### Low-to-intermediate spatial mixing within the state of Minnesota

We assessed county-specific virus diversity via a normalized Shannon diversity index (Fig. S5) that we computed based on the duration of time associated with continuous partitions of the phylogeographic tree as determined by Markov jumps ( 34 ). The index, in this context, measures the degree of spatial structure (based on counties) during the evolution and spread of SARS-CoV-2 viruses in Minnesota. A value of 0 indicates an exclusive spatial structure such as an outbreak contained to only one county ( 34 ). Conversely, a value of 1, suggests significant spatial mixing of SARS-CoV-2 between counties ( 34 ). The counties and regions show low-to-intermediate (0.25–0.5 Shannon) spatial mixing with brief periods of waxing and waning. The two dotted vertical lines indicate changes in state-wide policy. The first vertical line indicates the end of lockdown in Minnesota on 18 May 2020 ( 37 ). The second line on 28 May 2021 indicates the end of all COVID-19 restrictions in the state ( 38 ). Neither of these policy decisions appeared to have a significant impact on virus diversity across each individual county. Anecdotally (looking at the trends of each graph), the changes in case counts over time do not appear to have a relationship with county-specific diversity.


### Hennepin County received the vast majority of out-of-state introductions and was the dominant source for in-state transmission

We focused on the timing and source of introductions into the state during the pandemic ( Fig. 4 ) as estimated from our maximum clade credibility tree ( Fig. 2A ). The earliest estimated introduction into Minnesota was to Hennepin County from an international source on around 22 January 2020 (depicted with an arrow in Fig. 4 ). This is about 1 month before the first patient in the state, a man from Ramsey County (which borders Hennepin), developed symptoms and around 6 weeks before (6 March 2020) the Department of Health confirmed the infection ( 39 ). The first county-to-county introductions were estimated to originate from Hennepin to somewhere in northern Minnesota around 22 February and from Hennepin to Washington County (also in the northern part of the state) around 24 February. International introductions were most abundant in Hennepin (home to the Minneapolis/St. Paul International airport) totaling 45 (out of 107) over the 2-year period. Southern Minnesota counties were most common for domestic introductions, with 19 (out of 64), potentially driven by bordering states such as Iowa and Wisconsin as well as Illinois, which is nearby. Hennepin also was, by far, the most dominant source of in-state transmissions to other Minnesota locations ( n = 772) over the 2-year period.


#### Fig 4.


> **Figure/Table Caption:** Timing and source of international, domestic, and within-state introductions for each discrete location. Colors correspond to the source location. An arrow shows the first predicted introduction into Minnesota, which is estimated to have occurred in Hennepin County at around 22 January 2020 (from an international location). We used Baltic to extract introductions (migration events) along the annotated branches of the phylogeographic tree for node states with a posterior probability of ≥ 0.90. Location panels were combined into one figure in R and original month labels ( x -axis) were generated in Adobe Illustrator for visualization purposes.


## DISCUSSION

We analyzed over 22,000 new genomes of patients tested at Mayo Clinic Laboratories during a 2-year period in the COVID-19 pandemic. We focused our analysis on in-state transmission of SARS-CoV-2, mostly at the county (second administrative boundary) level, to describe the spread into and within Minnesota. Despite numerous efforts in genomic epidemiology, few studies have focused on county-to-county transmission in the United States over most of the pandemic (including different VoCs). We expand on earlier efforts such Moreno et al. ( 4 ) and Deng et al. ( 7 ) but include multiple variants and an extensive timeframe. We found that spread in the state was dominated by viruses from Hennepin County, which contains the largest metropolis, and that other regions including Northern and Southern Minnesota acted mainly as “sinks” for in-state transmission.

The earliest estimated introduction into Minnesota was to Hennepin from an international source about 6 weeks before the first confirmed case in the state. This suggests that earlier (and likely milder) infections of SARS-CoV-2 occurred before the first documented case. Interestingly, while Hennepin drove in-state transmission, it did not result in variations of location-specific spatial diversity. We found that all counties and regions had low-to-intermediate (0.25–0.5 Shannon) spatial mixing with brief periods of waxing and waning. The fluctuation in spatial diversity over time (that did exist) did not appear to be impacted by key state-mandated policies nor did it appear to have any relationship with reported clinical cases (Fig. S5).

As the virus continues to evolve, more within-state genomic epidemiology studies are needed to inform local and state public health response by highlighting the roles of various counties in state-wide transmission. In addition, they can elucidate the impact of out-of-state introductions on local spread which can inform policies such as travel.

We note several limitations in the study including the likelihood of location-specific sampling bias. We attempted to supplement the known locations of patients in our study (biased towards southeastern Minnesota) with existing sequences provided via the Minnesota Department of Health. We initially scaled our number of sequences to the rate of known COVID-19 cases, and, after doing so, omitted counties with a limited number of sequences (as well as outliers of sequences from included counties). Thus, we are unable to account for virus spread from less-populated areas of the state. We also attempted to include a representative sample of USA and international sequences. However, it is possible that additional sequences (context) might change the distribution of virus clades and the timing of introductions into the state, which could alter our interpretations of SARS-CoV-2 spread. We also only included early Omicron sequences and thus we are unable to describe an informed picture of its evolutionary diffusion in the state. In addition, our use of different versions of the DRAGEN pipeline over the course of our 2-year study period likely led to differences in variant frequencies across virus lineages/VoCs.


## ACKNOWLEDGMENTS

The authors would like to thank Gytis Dudas for his assistance with the Baltic Python library. The authors would also like to thank Scott Lunt and Rob Timmer for their assistance with the mforge high-performance computing environment. The authors acknowledge the laboratories that submitted the SARS-CoV-2 genome data to GISAID, which were used in this work.

This article is dedicated to Dr. Peter T. [AUTHOR], who sadly passed away during the writing of this manuscript.

This publication was supported by funding from the Center for Individualized Medicine-Mayo Clinic Research. The research reported in this publication was also supported by the National Institute of Allergy and Infectious Diseases (NIAID) of the National Institutes of Health (NIH) under Award Number R01AI164481 (to M.S.). The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.


## Contributor Information

Andrew P. [AUTHOR], Email: [AUTHOR][EMAIL_REDACTED].

Nicole M. Bouvier, Icahn School of Medicine at Mount Sinai, New York, USA


## DATA AVAILABILITY

We have deposited the SARS-CoV-2 genomes and metadata from this study in GISAID with a list available at 10.55876/gis8.220720me and in GenBank with a list available at 10.6084/m9.figshare.23802735 . We randomly shifted the collection day by ±31 days for privacy protection. The Minnesota Department of Health sequences used in this study are available on GISAID with acknowledgments at 10.55876/gis8.220709mv. Our GenBank international sequences were identified via the Nextstrain ( 5 , 2 ) site and obtained from NCBI Virus ( 2 ). We have deposited our BEAST XML files, empirical set of posterior trees, and our introductions to figshare at 10.6084/m9.figshare.22679449, 10.6084/m9.figshare.21777995 , 10.6084/m9.figshare.21777998 , and 10.6084/m9.figshare.21778004 .


## ETHICS APPROVAL

This research was conducted under the approval of ethics by the Mayo Clinic Institutional Review Board and assigned a study ID IRB#: 20-005896 under the application title Large Scale Whole Genome Sequencing of SARS-CoV-2.


## SUPPLEMENTAL MATERIAL

The following material is available online at https://doi.org/[REDACTED_DOI] .

Captions for supplemental figures.

Sequence distribution (n = 6,188) by Minnesota county/region by month for our phylodynamic analysis.

Supported routes of pairwise SARs-CoV-2 transmission as determined by the Bayes factor (BF) statistic.

Phylogeny of 24,070 full genome SARS-CoV-2 sequences generated for this study from 2020-2022 via Nextstrain (augur v15.0.2).

Map of Minnesota counties included in the phylodynamic analysis.

Virus diversity and cases per county/location.

ASM does not own the copyrights to Supplemental Material that may be linked to, or accessed through, an article. The authors have granted ASM a non-exclusive, world-wide license to publish the Supplemental Material files. Please contact the corresponding author directly for reuse.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials

Captions for supplemental figures.

Sequence distribution (n = 6,188) by Minnesota county/region by month for our phylodynamic analysis.

Supported routes of pairwise SARs-CoV-2 transmission as determined by the Bayes factor (BF) statistic.

Phylogeny of 24,070 full genome SARS-CoV-2 sequences generated for this study from 2020-2022 via Nextstrain (augur v15.0.2).

Map of Minnesota counties included in the phylodynamic analysis.

Virus diversity and cases per county/location.


### Data Availability Statement

We have deposited the SARS-CoV-2 genomes and metadata from this study in GISAID with a list available at 10.55876/gis8.220720me and in GenBank with a list available at 10.6084/m9.figshare.23802735 . We randomly shifted the collection day by ±31 days for privacy protection. The Minnesota Department of Health sequences used in this study are available on GISAID with acknowledgments at 10.55876/gis8.220709mv. Our GenBank international sequences were identified via the Nextstrain ( 5 , 2 ) site and obtained from NCBI Virus ( 2 ). We have deposited our BEAST XML files, empirical set of posterior trees, and our introductions to figshare at 10.6084/m9.figshare.22679449, 10.6084/m9.figshare.21777995 , 10.6084/m9.figshare.21777998 , and 10.6084/m9.figshare.21778004 .
