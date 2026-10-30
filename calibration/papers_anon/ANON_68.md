# De-Identified Manuscript `ANON_68`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

The distribution of fitness effects (DFE) defines how new mutations spread through an evolving population. The ratio of non-synonymous to synonymous mutations (dN/dS) has become a popular method to detect selection in somatic cells. However the link, in somatic evolution, between dN/dS values and fitness coefficients is missing. Here we present a quantitative model of somatic evolutionary dynamics that determines the selective coefficients of individual driver mutations from dN/dS estimates. We then measure the DFE for somatic mutant clones in ostensibly normal oesophagus and skin. We reveal a broad distribution of fitness effects, with the largest fitness increases found for TP53 and NOTCH1 mutants (proliferative bias 1–5%). This study provides the theoretical link between dN/dS values and selective coefficients in somatic evolution, and measures the DFE of mutations in human tissues.

Research organism: Human


## Introduction

One of the principal goals of large-scale genome sequencing of somatic tissues is to uncover genetic loci under positive selection, so-called ‘driver’ genes, that lead to clonal expansions. Measurement of the selective advantage of each driver mutation enables prediction of future evolutionary dynamics ( [AUTHOR] et al., 2019 ), provided the selective regime remains constant. In evolutionary biology, the distribution of fitness effects (DFE) is a fundamental entity that describes the selective consequences of a (large) number of individual mutations of an ancestral genome ( Eyre-Walker and Keightley, 2007 ). In somatic evolution, particularly in cancer genomes, we have an extensive knowledge of the catalogue of recurrent, and likely positively selected, somatic mutations ( Martincorena et al., 2017 ), but the fitness changes associated with each mutation remain largely unquantified.

Extensive experimental effort is ongoing to determine the fitness effects of mutations. Most prominently is lineage tracing of mutations in mouse models ( Vermeulen et al., 2013 ; Rogers et al., 2018 ), but these methods are not sufficiently high-throughput to produce the DFE for all somatic mutations. Other studies have estimated the selective coefficient of somatic mutations by measuring their frequency over time in the same individual using longitudinal sampling ( Körber et al., 2019 ), however this method is broadly limited to somatic evolution in the blood ( Gibson and Steensma, 2018 ) (where it is feasible to take samples from healthy individuals over time) and in rare cases of patients under active surveillance.

An alternative approach is to infer selective coefficients directly from genome sequencing data. Methods to identify positively-selected (driver) mutations rely on finding genes that have significantly more mutational ‘hits’ (typically hits are non-synonymous mutations) than would be expected by chance, after correction for factors known to influence the mutation rate across the genome ( Bailey et al., 2018 ). Conversely, negatively selected genes are expected to show a paucity of mutations ( Weghorn and Sunyaev, 2017 ; [AUTHOR] et al., 2018 ). This idea is formalised in the calculation of the dN/dS ratio – a method originally developed in molecular species evolution – that has recently been adapted to study somatic evolution (both cancer and normal tissue) ( Martincorena et al., 2017 ; Weghorn and Sunyaev, 2017 ; [AUTHOR] et al., 2018 ; Wu et al., 2016 ; Greenman et al., 2006 ; Yang et al., 2003 ; Martincorena et al., 2018 ; Lee-Six et al., 2018 ). The intuitive idea behind dN/dS is to measure the rate of non-synonymous (dN) mutations (possibly under selection) and compare that to the rate of synonymous (dS) mutations (presumed neutral). The ratio of these two numbers, each normalised for the local sequence-specific biases in the mutation rate, putatively identifies a signature of selection: dN/dS >1 indicating positive selection, dN/dS = 1 indicating neutral evolution and dN/dS <1 indicating negative selection.

Transforming dN/dS values to selective coefficients in somatic evolution is an unaddressed problem. dN/dS was originally developed in the context of species evolution using the Wright-Fisher process, a classical population genetics model that assumes that evolution occurs over very long timescales, which permits new mutations to fix within lineages. The Wright-Fisher model assumes constant population sizes, non-overlapping generations and that all individuals have equal potency. Under the Wright-Fisher model, the dN/dS of a locus is related to its selective coefficient by the relation ( Nielsen and Yang, 2003 ):



| d N d S = 2 N s 1 − e − 2 N s |
| --- |


Where N is the effective population size and s the selection coefficient.

However, in somatic evolution the assumptions of the Fisher-Wright model are violated. Somatic evolution is rapid and new mutations are infrequently fixed in the population ( McGranahan and Swanton, 2017 ), clonal dynamics are complex ( [AUTHOR] et al., 2019 ), and population sizes unlikely to be constant ( [AUTHOR] et al., 2015 ). Further, the lack of recombination in somatic evolution can result in strong hitchhiking effects ( Tilk et al., 2019 ). In addition, since in somatic evolution, the ancestral genome is known, the need to measure dN/dS across a phylogeny is circumvented (a necessary step for dN/dS analysis in species evolution). Violations of some of these assumptions was previously recognised to make the interpretation of dN/dS problematic ( Kryazhimskiy and Plotkin, 2008 ; Mugal et al., 2014 ), and consequently the relationship between selective coefficients and dN/dS values is uncertain.

The size distribution of clones (called the site frequency spectrum in population genetics nomenclature) also contains information on the selective coefficients of newly arising mutations. Mathematical descriptions of the dynamics of populations of cells can make predictions on the shape of the clone size distribution under different demographic and evolutionary models ( Simons, 2016a ; Durrett, 2013 ). This approach has been used to quantify the dynamics and cell fate properties of stem cells across many tissues in model systems ( Klein et al., 2010 ; Lopez-Garcia et al., 2010 ; Vermeulen et al., 2013 ). We and others have also used similar approaches applied to deep sequencing data to infer the evolutionary dynamics of tumours ( [AUTHOR] et al., 2016 ; [AUTHOR] et al., 2018 ; Bozic et al., 2016 ; Ling et al., 2015 ) and of clonal haematopoiesis in the blood ( Watson et al., 2019 ).

To date, dN/dS analysis and the analysis of the clone size distribution have been performed independently, with conflictual results ( Simons, 2016b ; Martincorena et al., 2016 ). Here we develop the mathematical population genetics theory necessary to combine these approaches and explore how the inter-individual measure of selection at a locus as provided by dN/dS values, is related to the underlying cell population dynamics that generate intra-individual clone size distributions. This approach naturally accounts for the nuances in somatic evolution that can make the interpretation of dN/dS difficult. We show how this unified approach allows for greater insight into patterns of selection than either method in isolation, and importantly reveal the precise mathematical relationship between dN/dS values and selective coefficients in somatic evolution. We use this approach to infer the selective advantage of mutations in normal tissue.


## Results


### A general approach to integrate dN/dS and clone size distributions

We present a general mathematical framework for the interpretation of frequency-dependent dN/dS values in somatic evolution. First, we construct null models of the evolutionary dynamics in the absence of selection, and then augment these models to incorporate the consequences of selection. Evolutionary dynamics differ between normal tissues and cancer cells: in normal tissues maintained by stem cells, the long-term population dynamics is controlled by an approximately fixed-size set of equipotent stem cells undergoing a process of neutral competition ( Klein and Simons, 2011 ), whereas in tumour growth the overall population increases over time. We develop a null model to predict the expected genetic diversity in the population in the absence of selection. Positive selection causes selected variants to rise to higher frequency than expected under neutral evolution ( Figure 1a ), and negative selection has the opposite effect. This insight guides how we model the effects of selection, namely the diversity of non-synonymous mutations.


#### Figure 1. dN/dS in somatic evolution depends on the frequency of clones.


> **Figure/Table Caption:** ( a ) Variants under positive selection are enriched at high frequency, this means dN/dS estimates are dependent on the frequency of mutation, ( b ). The strength of selection influences the degree to which positively selected variants are enriched at high frequencies ( c ).

Specifically, we defined the function g ( θ , μ , s , f ) as the expected number of mutations with selective (dis)advantage s found at a frequency f , for a given evolutionary dynamics scenario, where mutations accumulate at a rate µ per division. For the remainder of the paper we use passenger mutations to refer to those mutations that have no functional effect (s=0) and driver mutations those that have s>0. When comparing to data, driver mutations are taken as equivalent to non-synonymous mutations and passengers equivalent to synonymous mutations.

The functional form of g ( θ , μ , s , f ) encapsulates the population dynamics of the system with parameter vector θ , which may, for example, include the growth rate of a tumour, or loss replacement rate of stem cells in normal tissue. The direct interpretation of s depends on the system under question. Following the logic of the effect of selection above, for s ′ > s we have that:



| g ( θ , μ , s ′ , f ) > g ( θ , μ , s , f ) |
| --- |


Since dN/dS measures the excess or deficiency of mutations due to selection, taking the ratio of g ( θ , μ , s , f ) when s ≠ 0 to s = 0 and normalizing for the mutation rates, which may differ for passenger ( μ p ) and driver ( μ d ) mutations respectively, informs how dN/dS is expected to change as a function of the frequency f of mutations in the population ( Equation 1 ).



| d N d S = μ p μ d g ( θ , μ d , s , f ) g ( θ , μ p , s = 0 , f ) | (1) |
| --- | --- |


We discuss the general properties of this model. Firstly, when s = 0 (neutral evolution), and provided that the mutation rates are correctly normalised, the numerator and denominator are equal resulting in d N d S = 1 , as expected. Secondly, dN/dS increases as a function of frequency f (clone size) for positive selection, and decreases as a function of f for negative selection ( Figure 1b ), for all g ( θ , μ , s , f ) that we explored. Thirdly, the shape of the curves predicted by the underlying population model encodes the value of the selection coefficient; for example the steepness of the increase is proportional to the selection coefficient s ( Figure 1c ). These observations are a natural consequence of positive selection driving selected mutations to higher frequency ( Figure 1a ).

Unfortunately, directly using Equation (1) to measure selective coefficients from the slope of the dN/dS curve as function of frequency is often impractical. Real sequencing data often suffers from a limited number of mutations detected at any particular frequency and measurement uncertainties in these frequencies. To circumvent these issues, we introduce ‘interval dN/dS’ (i-dN/dS) that aggregates over a frequency range to reduce the influence of these sources of noise. Interval dN/dS is defined as:



| i d N d S = μ p μ d ∫ f m i n f m a x g ( θ , μ d , s , f ) d f ∫ f m i n f m a x g ( θ , μ p , s = 0 , f ) d f | (2) |
| --- | --- |


Fixing the integration range [ f m i n , f m a x ] allows for robust inference of s in potentially sparse and noisy sequencing data using maximum likelihood methods (see Materials and methods).


### Frequency-dependent dN/dS values in stem cell populations

In healthy tissue, only mutations that are acquired in the stem cells will persist over long times, and so we restrict our attention to these cells. Quantitative analysis of lineage tracing data has shown that the stem cell dynamics of many tissues conform to a process of population asymmetry ( Klein and Simons, 2011 ). In this paradigm, under homeostasis, the loss of stem cells through differentiation is compensated by the replication of a neighbouring stem cell, thus maintaining an approximately constant number of stem cells. These dynamics are represented by the rate equations:



| S C → 2 r λ S C + S C D + D { p = ( 1 + Δ ) / 2 p = ( 1 − Δ ) / 2 | (3) |
| --- | --- |


where SC refers to a single stem cell which divides symmetrically to produce either two stem cells or two differentiated cells (denoted as D above), λ is the rate of cell division per unit time, and r is the probability of a symmetric divisions. The product r λ is referred to as the loss/replacement rate. Differentiated cells will ultimately be lost from the population over long time scales. Under homeostasis, loss and replacement should be exactly balanced, so Δ = 0. With Δ ≠ 0, the fate of a stem cell is ‘biased’, introducing positive or negative selection into the model. Previous mathematical analysis shows that this model is a good description of the clonal dynamics in the oesophagus and skin ( Klein et al., 2010 ; Doupé et al., 2012 ; Alcolea et al., 2014 ). Using previous analytical results describing the temporal evolution of the clone size distribution (see methods for detailed discussion) we derive the frequency distribution g θ , μ , s , A for oesophagus and skin as ( Simons, 2016a ; Klein et al., 2010 ; Nicholson and Antal, 2016 ):



| g ( θ , μ , s , A ) = μ n 0 r λ ρ A e - ρ A N ( t ) | (4) |
| --- | --- |


Where A is the area of the clone, ρ is density of stem cells per mm 2 , n 0 is the starting population size and μ the mutation rate, which may be different for drivers ( s > 0 ) and passenger mutations ( s = 0 ) , ie drivers and passengers may accumulate at different rates. N ( t ) is a scaling factor that depends on Δ, the bias toward self-renewal, which we interpret as our selection coefficient in this system. Specifically:



| N Δ = 0 t = 1 + r λ t | (5) |
| --- | --- |




| N Δ t = 1 + Δ e 2 r λ Δ t - ( 1 - Δ ) 2 Δ | (6) |
| --- | --- |


N ( t ) can be interpreted as the average size of a labelled clone after time t , which even under homeostasis grows over time and compensates for some clones being lost due to drift. From these expressions, we can then write down an expression for i-dN/dS as a function of clone frequency (see Materials and methods) that allows for maximum likelihood estimation of parameter values (Δ). We confirmed the accuracy of our derivation using simulations ( Figure 2a ), and performed power calculations to determine the minimum number of mutations required to correctly infer the underlying population dynamics: we determined that 8 mutations per gene was sufficient to accurately recover Δ ( Figure 2b ) with accuracy increasing for higher mutation burdens ( Figure 2c ). We also performed simulations where Δ was itself a random variable, simulating the effect of different sites within the gene having different fitness effects. We assumed Δ was exponentially distributed and generated 500 simulated cohorts. Fitting i-dN/dS demonstrated that on average we infer the mean value of the exponential distribution, Figure 2—figure supplement 1 .


#### Figure 2. Theoretical model of interval dN-dS fitted to simulated data and data from deep sequencing of the oesophagus.


> **Figure/Table Caption:** ( a ) Interval dN/dS as a function of clone area for 2 simulated cohorts where driver mutations induce different biases, theoretical model captures the dynamics well and enables us to recover the bias ∆, accurately. As the number of mutations increases ability to recover the correct ∆ and the model fit (measured using R 2 ) improves ( b ) and ( c ). ( d ) Data and model fit for all neutral genes, shows i-dN/dS = 1 across the frequency range and inferred bias of 0. Data and model fit for ( e ) NOTCH1 missense mutations in patient PD31182, ( f ) missense TP53 mutations in PD30273 and NOTCH1 nonsense mutations in PD31182 ( g ). Data are black points and model fits are solid lines with shaded areas denoting 95% CI.


> **Figure/Table Caption:** For each panel the mean of the exponential distribution used for Δ is stated above and illustrated by the red dashed lines.


> **Figure/Table Caption:** Purple points are data and red lines model fits, shaded areas denote 95% confidence intervals. Fits were performed separately for missense, ( a ) and nonsense mutations, ( b ). Each plot is annotated with the inferred bias ∆ and the R 2 value.


> **Figure/Table Caption:** Inferred loss replacement rates, rλ for each patient based on missense, ( c ) and nonsense mutations, ( d ).


> **Figure/Table Caption:** Points are data and lines are model fits. Analysis performed separately for nonsense, a and missense, b.


### Selection advantages in histopathologically-normal human oesophagus

We inferred the selective advantage of driver mutations in human oesophagus using published deep sequencing data from Martincorena and colleagues ( Martincorena et al., 2018 ) that documents the clonal expansion of a panel of putative driver mutations in histopathologically-normal oesophageal biopsies.

We used the dndscv bioinformatics tool ( Martincorena et al., 2017 ) to calculate frequency-dependent dN/dS values from these data (clone size measured in fraction of mutant reads multiplied by 2 mm 2 – the area of the biopsy – and assuming 5000 stem cells per mm 2 ( Eyre-Walker and Keightley, 2007 ) tissue). dN/dS values varied considerably as a function of mutation area ( Figure 1—figure supplement 1 ).

We considered the average frequency-dependent dN/dS values simultaneously across all genes in the panel, on a patient-by-patient basis. Our theoretical model of i-dN/dS calculated from these data fitted strikingly well ( Figure 2—figure supplement 2 ). Estimates of the loss/replacement rate r λ of the stem cell population were in the range 1.2-5.0 per year ( Figure 2—figure supplements 2 and 3 ). Inference of the selective advantage s (measured in terms of the bias towards self renewal Δ) revealed an average bias of 0.004 (0.002 – 0.005 95% CI) per missense mutation ( Figure 2—figure supplement 3 ). Nonsense mutations caused a five-fold greater bias towards self-renewal of 0.021 (0.008 – 0.032 95% CI) ( Figure 2—figure supplement 3 ). After removal of all genes that are strongly selected, global dN/dS values on the remaining 48 genes show dN/dS of approximately 1 across the frequency range ( Figure 2d ), and i-dN/dS analysis revealed that these somatic mutations do not associate with a proliferative bias (Δ=0).

We then fitted the data on a gene-by-gene and patient-by-patient basis for cases where sufficient mutations were available to perform the fit ( Figure 2e–g ; Figure 2—figure supplement 4 ). A broad range of selective advantages were inferred ( Figure 3 and Figure 3—figure supplement 1 ). Mutations in TP53 showed large biases across all patients for both missense, Δ = 0.057 (0.05–0.068 95% CI) and nonsense mutations, Δ = 0.094 (0.091–0.097 95% CI) ( Figure 3a–b ). This was also true for mutations in NOTCH1 with Δ = 0.029 (0.019–0.036 95% CI) for missense and Δ = 0.072 (0.034–0.089 95% CI) for nonsense mutations. NOTCH2 , PIK3CA , CREBBP and FAT1 also showed a bias toward self-proliferation in multiple patients ( Figure 3a–b ), though most had a small effect on fitness (range 0.003–0.029 for missense mutations and 0.030–0.041 for nonsense mutations). Together these data suggest a distribution of fitness effects (DFE) characterized by many small effect mutations with few large effect mutations ( Figure 3c–d ), as is seen in organismal evolution ( Eyre-Walker and Keightley, 2007 ). We recognize that there may be intra-gene variation of selection coefficients, that is, some sites within genes may have stronger fitness effects than others. This is supported by clustering of mutations within particular domains and hotspots of mutations as documented in the original study ( Martincorena et al., 2018 ). In future, larger cohorts and methods to estimate site level dN/dS values would allow this approach to be extended to the site level.


#### Figure 3. Summary of model fits across all patients for normal oesophagus data.


> **Figure/Table Caption:** Inferred biases ∆ for genes where at least 2 patients had good model fits (R 2 > 0.6 & >7 mutations) for missense mutations ( a ), and nonsense mutations ( b ). Inferred distribution of fitness effects for all genes across all patients for missense mutations ( c ), and nonsense mutations ( d ).


> **Figure/Table Caption:** Left hand plot shows inferred loss replacement rates λ and right hand plot inferred biases ∆.

As our model assumes that clones emerge and expand independently we checked that the data is not overly influenced by hitchhiking mutations,which would violate these assumptions. For this, we leveraged the spatial sampling of tissue pieces. Approximately 90 patches were sampled from each patient. We reasoned that patches with selected clones might be expected to have more hitchhiking mutations, and for those mutations to be at a higher frequency when compared to patches without selected clones. To test this hypothesis, we counted the number of non-synonymous NOTCH1 and TP53 mutations and the number of synonymous mutations in each patch. If the synonymous mutations we observe in the data are largely due to hitchhiking effects we would expect the number and size of synonymous variants to correlate with the number of driver mutations per patch. While there =was a statistically significant correlation for both NOTCH1 (linear regression, p<0.001) and TP53 mutations (p=0.031), the effect was small ( Figure 5—figure supplement 1 ): for each additional driver there was on average 0.05 additional synonymous variants (0.047 for NOTCH1 and 0.056 for TP53). We note too that the correlation was very noisy (R 2 < 0.02) and we observed no statistically significant relationship between VAF of synonymous mutations and the number of TP53 or NOTCH1 mutations (linear regression, p>0.1). This analysis suggests that the majority of synonymous mutations are not hitchhikers, and consequently that assuming the independence of clones isreasonable.


### Driver mutation selective advantage in normal skin

Martincorena and colleagues had also published data on the expansion of driver mutations in ostensibly normal human skin ( Martincorena et al., 2015 ). Analyses of these data with interval dN/dS revealed a per-patient average selective advantage per mutation (again measured in terms of the bias towards self renewal) of Δ = 0.001 for missense mutations and four-fold higher (Δ = ﻿0.004) for nonsense mutations ( Figure 4a-c ). Performing the analysis on a gene-by-gene basis was limited by the lower number of detected mutations, and the limited frequency range (clone size range) compared to the oesophagus dataset. Good fits to the data were obtainable for NOTCH1 missense mutations in patient PD18003 with fitness estimated to be Δ = 0.0149 (0.0148-0.0150 95% CI), and TP53 missense mutations also in patient PD18003, Δ = 0.0054 (0.0051-0.0058 95% CI) Figure 4 . These fitness coefficients were similar to the oesophagus data. For missense mutations we were also able to produce the distribution of fitness effects across the skin cohort, which showed similar characteristics to the oesophagus data of a small number of high effect mutations and a larger number of smaller effect mutations, Figure 4f .


#### Figure 4. Analysis of skin dataset shows similar DFE to oesophagus.


> **Figure/Table Caption:** Model fits per patient and per gene per patient when there were sufficient mutations in the skin dataset. Points are data and lines are model fits, ( a-e ). ( f ) Shows the distributions of fitness effects for missense mutations across the cohort. There were insufficient nonsense mutations in the majority of genes to draw the equivalent plot for nonsense mutations.


### Site frequency spectra

We next sought to challenge our model by directly fitting the site frequency spectra across ages, taking a similar approach to studies of the blood ( Watson et al., 2019 ), colon ( Lopez-Garcia et al., 2010 ), skin ( Simons, 2016a ) and other tissues ( Klein and Simons, 2011 ). Our model of stem cell dynamics makes predictions on the properties of these distributions as a function of the age of donors. In particular, Equations (5) and (6) predict that the characteristic frequency N(t) increases exponentially for non-neutral mutations and linearly for neutral mutations as a function of time. Plotting the distribution of clone size areas showed a widening of the distribution as a function of age, which was particularly striking for mutations in the NOTCH1 and TP53 genes, consistent with these genes conferring large selective advantages ( Figure 5a ).


#### Figure 5. Directly fitting site frequency specta supports interval dN/dS inferences.


> **Figure/Table Caption:** ( a ) Site frequency spectra become wider for older donors, with increases in the median clone area which is more pronounced for mutations in TP53 and NOTCH1. ( b ) Using WAIC to perform model selection, we found a model with an exponential term and a power law to be the best fitting model (lowest WAIC). ( c ) Posterior parameter estimates for n 0 μ . ( d ). The characteristic frequency N ( t ) / ρ , Interval represent 66% and 95% credible intervals respectively. ( e ) Site frequency spectra from data (black dots) and posterior predictive fits for 50, 80% and 95% credible intervals (blue ribbons) for non-synonymous mutations in each don or.


> **Figure/Table Caption:** The mean VAF of synonymous mutations as a function of the number of NOTCH1 ( c ) and TP53 ( d ) mutations per tissue piece.


> **Figure/Table Caption:** Inferred values for n 0 μ , ( a ) and N(t)/ρ , ( b ). Red points are true values, black points are median posterior values and whiskers are 66% and 95% credible intervals. Example fits across ages for Δ = 0.1. Individual fits across different age cohorts ( c ), black dots are data points (from simulation) and blue shaded areas are 50%, 80% and 95% credible intervals.


> **Figure/Table Caption:** Posterior values for N(t)/ρ showing large uncertainty in these values ( b ).


> **Figure/Table Caption:** ( a ) Summary of all posterior regression coefficients for all genes showing TP53 and NOTCH1 cause the largest increase in frequency as a function of age. ( b ) Regression coefficients with inferred selection coefficients from interval-dN/dS are positively correlated.


> **Figure/Table Caption:** Fit for TP53 missense mutations in donor PD30273 using SSB-dN/dS results ( a ). Comparison of inferred Δ values for NOTCH1 and TP53 mutations ( b ). Comparison of global dN/dS values for all mutations, missense and nonsense mutations ( c ).

To quantitively test the predictions of the model and to infer parameters of interest we implemented a Bayesian non-linear fitting method (see methods) to fit the following model:



| y = α A e - A e x p ⁡ ( β ) | (7) |
| --- | --- |


With the parameters α = μ n 0 / r λ ρ , and β = l o g ⁡ ( N t / ρ ) to be estimated. We first validated that the approach could correctly infer known parameters from synthetic data generated from our simulation framework, Figure 5—figure supplement 2 . Next, we fitted the model to the oesophagus dataset, separately for non-synonymous and synonymous mutations and across ages, Figure 5e . Posterior estimates of the compound parameter μ n 0 / r λ ρ showed consistent estimates for both non-synonymous and synonymous mutations (taking into account the approximate 3:1 ratio of mutable sites), Figure 5c . Unfortunately decoupling μ n 0 / r λ ρ directly from the data is not possible and requires independent estimates of either the mutation rate or number of stem cells. Posterior estimates of the characteristic frequency N(t) showed an increase as a function of age for non-synonymous mutations and a more modest increase for synonymous as would be predicted from theory, Figure 5d .

As another challenge to the proposed model, we also fitted the following two models which are simpler subsets of the full model we derive theoretically, thus testing two alternate decay functions.



| y = α A |
| --- |




| y = α e - A β |
| --- |


Here, α and β are parameters to be estimated. Comparison of the fits using the widely applicable information criteria, WAIC (a generalized version of information criteria such as AIC and BIC) found that our theoretical model with an exponential term and a power law term ( Equation 7 ) provided the best predictive accuracy (lowest WAIC), Figure 5b. Bayes factors for the proposed theoretical model also strongly supported this as the best model (BF > 10 3 for both models).

We also attempted to fit the model on a gene by gene basis. However due to the limited data points at the gene level we found that our posterior estimates for the parameters were very wide, precluding further insight from the site frequency spectrum at the gene level, Figure 5—figure supplement 3 . This reveals one of the strengths of our i-dN/dS approach, which by leveraging information across genes to infer the background mutation model and integrating over clone sizes we can perform the inference with a limited number of data points. As an alternative to fitting the full clone size distribution, we performed a Bayesian multi-level regression to assess which mutations showed the largest increase in clone size as a function of age. This analysis revealed that TP53 and NOTCH1 had the largest regression coefficients, consistent with these genes having the largest selection coefficients, Figure 5—figure supplement 4 , providing qualitative support for our approach. Our inferred selection coefficients from i-dN/dS were also correlated with the regression coefficients from the statistical model (linear regression, p=0.004, R 2 = 0.47). Taken together, analysis of the site frequency spectrum on a patient by patient basis and a gene level statistical model are consistent with our inferences from i-dN/dS. We find that the proposed model provides the best fit to data when compared to other similar models, that the characteristic frequency of non-synonymous mutations increases rapidly with age and that NOTCH1 and TP53 exhibit the largest increase in clone size as a function of age.


## Discussion

Here we have shown that the combination of dN/dS values with mutation frequency-based information provides additional quantitative insight into dynamics of somatic evolution than either method alone. Specifically, the combined approach enables direct inference of the selection coefficients of mutations in somatic tissues. We note that our study also shows that the magnitude of the selection coefficient is not necessarily represented by simply calculating a ‘point estimate’ of dN/dS that neglects mutation subclonal frequency information.

Using this methodology, we have begun the construction of the distribution of fitness effects (DFE) in somatic evolution, observing a distribution where most mutations that we analysed were near-neutral, with a tail of highly selected variants. In both skin and oesophagus, the most highly selected mutant genes were NOTCH1 and TP53 (increased proliferative bias of >1% and>5% respectively). We observed that values of selective coefficients of individual genes varies between patients, likely because of inter-patient difference in the precise location of point mutations, but potentially also because of inter-patient variation in selective pressure from the microenvironment. Nevertheless, the comparative rank of per-gene fitness coefficients was broadly consistent across patients (e.g. for missense mutations across patients, TP53 mutations always had the highest fitness, followed by NOTCH1 mutations). This consistency in selective coefficients is in agreement with the observation of highly recurrent gene mutations in cancer ( Lawrence et al., 2013 ) and evidence of repeatability in cancer evolution ( Caravagna et al., 2018 ).

Non-synonymous NOTCH1 mutations were observed approximately 3-fold more frequently that non-synonymous TP53 mutations in oesophagus, and approximately 5-fold more frequently in skin, suggesting that the mutation rate of NOTCH1 is greater than for TP53 . Coupling these data with our quantitative measurements of the fitness coefficients leads to the prediction that the oesophagus will become transiently repopulated by NOTCH1- mutant cells during ageing, before subsequent replacement by fitter mutant- TP53 clones.

On a cautionary note, our theoretical work shows that the clonality of mutations strongly determine the observed value of dN/dS, and so a misleading picture of the selective forces will be produced if dN/dS frequency-dependent effects are not corrected for. The accuracy of any estimate of evolutionary dynamics from dN/dS values is of course dependent on the underlying accuracy of the dN/dS measure itself, which is compromised by uncharacterised variability in the mutation rate across the genome ( Van den Eynden and Larsson, 2017 ) and in the uncertain pathogenicity of individual single nucleotide variants (extensions to estimate site level selection coefficients may circumvent some of these issues [ Cannataro et al., 2018 ; Temko et al., 2018 ]). We also recognize that our model assumes a well-mixed population, while the data used in our study is from spatially structured epithelia. Spatial structure influences the distribution of clone sizes. Effects include: the influence of the boundary that enable rapid growth of mutants on the expanding front and conversely ‘encapsulation’ within a growing mass that slows clone growth ( Fusco et al., 2016 ; Chkhaidze et al., 2019 ), and clonal interference that slows the growth of two similarly fit competing clones ( Martens et al., 2011 ; Hall et al., 2019 ).

Combining population genetics methods with comparative genomics is a powerful way to infer selection pressures in human somatic evolution, giving new insight into the fundamental parameters that determine evolutionary dynamics in health and disease.


## Materials and methods


### Oesophagus and skin data

For the oesophagus and skin data we used mutation calls provided by the original studies. In the oesophagus data when a mutation was present in multiple adjacent biopsies we used the sum of the mutation frequency times the area of the biopsies (2 mm 2 ) as our readout of clone size and performed the dN/dS analysis on a patient by patient basis.


### dN/dS calculations

For calculating dN/dS ratios the dndscv R package was used, which calculates both global dN/dS ratios across the whole exome or a panel of genes as well as per gene dN/dS ratios using a covariate based model to infer dN/dS values with a limited number of mutations ( Martincorena et al., 2017 ). We used the default settings of dndscv, using the default hg19 transcript reference provided by the package. dndscv can also take into account small insertions and deletions, which we included in our analysis. Therefore, where we refer to mutation this includes indels in addition to SNVs.

To calculate the interval dN/dS measure we took the clone size measurements and determined a low cutoff f m i n based on the minimum clone size. We then created a vector of clone sizes that covered the total range and calculated dN/dS between f m i n and all values of f m a x . This allowed us to plot dN/dS as a function of f m a x and fit our interval dN/dS models. In our data, clone size is measured in units of area (mm 2 ).

Accurately estimating dN/dS from sequencing data of somatic tissues can be challenging due to the strong sequence context dependence of mutations and variability of mutation rates across the genome. To confirm our inferences were not dependent on the choice of dN/dS methodology we calculated dN/dS values using SSB-dNdS and then fitted our model ( [AUTHOR] et al., 2018 ). As SSB-dNdS only uses SNVs, we reran dndscv after removing indels. Inferences on a patient by patient basis were highly consistent between the methods, see Figure 5—figure supplement 4 . There was more variability at the gene level, perhaps due to differences in the approaches used to control for variability in mutation rates across the genome.


### Model fitting

We used a maximum likelihood approach to fit our models to the data. Defining the observed interval dN/dS as y and the model dN/dS as y ^ ( θ ) = μ p μ d ∫ f m i n f m a x g ( θ , μ d , s , f ) d f ∫ f m i n f m a x g ( θ , μ p , s = 0 , f ) d f . First of all we define the residuals between the data and the model as R = y − y ^ ( θ ) . Assuming that the residuals are normally distributed with mean 0 we can write down the negative log likelihood (NLL) as



| N L L ( θ ) = − ∑ y − y ^ ( θ ) l o g N ( y − y ^ ( θ ) , μ = 0 , σ ) |
| --- |


where N denotes the normal probability density function. We can then find the parameters θ that minimize the NLL and calculate confidence intervals on these estimates using the Fisher information matrix. When fitting to data we ensured that there were a minimum of 8 mutations and only included model fits with R 2 > 0.6 for downstream analysis. We used a maximum likelihood approach over a Bayesian approach to fit the model because the integral of the clone size distribution does not have a closed form solution, making it unfeasible to use readily available MCMC samplers which we adopt later.


### Interval dN/dS model

For the stem cell model, using Equations 2, 3, 4, 5, 6 in the main text, interval dN/dS is given by:



| i d N d S = 1 1 + Δ [ E i ( − ρ A m a x N Δ ( t ) ) − E i ( − ρ A m i n N Δ ( t ) ) + 1 2 ( e − ρ A m a x N Δ ( t ) ρ A m a x + e − ρ A m i n N Δ ( t ) ρ A m i n ) ] [ E i ( − ρ A m a x N ( t ) ) − E i ( − ρ A m a x N ( t ) ) + 1 2 ( e − ρ A m a x N ( t ) ρ A m a x + e − ρ A m i n N ( t ) ρ A m i n ) ] |
| --- |


Where E i is the exponential integral E i x = - ∫ x ∞ e - n n d n . ρ is density of stem cells per mm 2 , which we set to 5,000 cells /mm 2 for fitting ( Hall et al., 2019 ).


### Simulations

To confirm the accuracy of our analytical model and investigate the influence of uncertainty in mutation frequencies due to sequencing noise and to challenge some of the underlying assumptions of our theoretical approach, we developed a simulation based model.

We seed a population of N s stem cells that then undergo loss/replacement as described by the following rate equations



| S C → 2 r λ S C + S C D + D { p = ( 1 + Δ ) / 2 p = ( 1 − Δ ) / 2 |
| --- |


As only the stem cells are long lived the differentiated cells are not explicitly modelled such that when a stem cell 'differentiates' it is effectively lost from the population. During division, daughter cells acquire mutations with a fitness effect at rate μ d and passenger mutations at rate μ p . Fitness increases the bias toward self-proliferation Δ of a stem cell lineage. Additional driver mutations do not further increase the fitness of stem cells.

To calculate dN/dS across a cohort of tissue biopsies we count the number of driver mutations N d and the number of passenger mutations, N p and then normalize by their respective mutation rates. In our model drivers = non-synonymous and thus every driver has an effect on fitness. Then the ratio of these two numbers gives us the excess or deficit of mutations due to selection – ie the dN/dS ratio.



| d N d S = N d / μ d N p / μ p |
| --- |


For the interval dN/dS we simply calculate the N x between f m i n and f m a x .

To introduce uncertainty into mutation frequencies we perform a process of empirically motivated sampling to the true underlying frequency f . Firstly, we specify the average depth of sequencing D, then the depth of sequencing for mutation i is given by



| D i = P o i s s o n ( D ) |
| --- |


The sampled number of read counts is then



| n s = B i n o m i a l ( n = D i , p = f ) |
| --- |


And the sampled variant frequency is then f s = n s / D i .

The simulation framework was written in Julia ( Bezanson et al., 2017 ) and is available at [GITHUB_REPO_REDACTED] .


### Fitting site frequency spectra

To fit the site frequency spectra we first removed mutations with clone size area < 0.008. This cutoff was determined by inspection of the point of highest density of the clone size area histograms, reasoning that below this frequency the data was limited due to the resolution of the sequencing assay. We then binned the data using a bin size of 0.005 and counted the number of mutations in each bin. We did this for each donor and separately for non-synonymous and synonymous mutations. We then used the brms (Bayesian Regression Modeling with Stan) R package ( Bürkner, 2017 ) to fit the following non-linear model jointly across all patients:



| C = α A e − A e x p ( β ) |
| --- |


With the parameters α = μ n 0 r λ ρ , and α = μ n 0 to be estimated and C being the number of mutations and A the area. We used the following priors for the parameters:



| β = l o g ⁡ ( N t ) |
| --- |




| A ~ N o r m a l ( 5,2 ) |
| --- |


We ran 4 chains with 5000 iterations with the first 2500 used as warmup. To assess convergence we ensured that the scale reduction factor R ^ (a measure of mixing of chains) was < 1.01 as recommended.

We also fitted the following two models:



| C = α A |
| --- |




| C = α A |
| --- |


We used the same prior distributions as above. We then compared the predictive accuracy of the different models using the widely applicable information criteria (WAIC) ( Vehtari et al., 2017 ). This found that the functional form derived from theory provided the best fit, Figure 5b . Bayes factors to compare models were calculated using the bayestestR package ( Makowski et al., 2019 ). The log10(BF) of the proposed theoretical model vs the power law was 52 and 44 when compared against the exponential model.


### Bayesian multi-level regression

We performed a Bayesian multi-level regression of clone size ~ age with the gene as a random effect. This allowed us to determine which genes cause the largest increase in frequency as a function of age. This was done using brms in R with default priors, 4 chains and 5000 iterations. Using R’s statistical modelling syntax the model is given by clone size ~age + (1 + age|gene) . We fit the model assuming a normal distribution as well as a log-normal distribution, finding the latter to provide the best predictive accuracy (lowest WAIC) and superior posterior predictive check.


### Site frequency spectra for a model of stem cell proliferation

Our mathematical model of stem cell proliferation drew on results from a range of studies analysing the clone size distribution from lineage tracing experiments. Particularly useful are the results from Klein et al. (2010) , which we took as a starting point for our model. We follow the notation used in this study to a large extent. Other studies that are also illuminating and relevant are the theoretical work of Nicholson and Antal (2016) , while similar theoretical models have also been applied to the oesophagus ( Doupé et al., 2012 ), airway epithelia ( Teixeira et al., 2013 ) and the blood ( Watson et al., 2019 ) amongst others. In this section we outline the key results relevant to our approach.

We begin with the set of rate equations presented in the main text:



| S C → 2 r λ S C + S C D + D { p = ( 1 + Δ ) / 2 p = ( 1 − Δ ) / 2 |
| --- |


From this we are interested in the clone size distribution, that is, the probability of observing a clone of size n after time t. In other fields such as population genetics, this distribution is equivalent to the site frequency spectrum. Given the above rate equations, we can express the dynamics as a birth-death process with birth rate b = r λ ( 1 + Δ ) and death rate d = r λ ( 1 − Δ ) which allows us to write down the master equation for the probability of observing a clone of size n at time t, b = r λ ( 1 - Δ ) .



| p n |
| --- |




| d p n d t = b n - 1 p n - 1 - b + d n p n + d ( n + 1 ) p n + 1 |
| --- |


This has the following solution (see Bailey, 1990 p92)



| d p 0 d t = d p 1 |
| --- |




| p n t = 1 - α ( t ) 1 - β t β ( t ) n - 1 |
| --- |


With p 0 t = α ( t ) and α ( t ) defined as follows:



| β ( t ) |
| --- |




| a t = d e b - d t - 1 b e b - d t - d |
| --- |


From these results we can obtain the average size of surviving clones, β t = b e b - d t - 1 b e b - d t - d :



| N ( t ) |
| --- |


Which, as will become apparent, gives a characteristic scale for the distribution.

Thus far we have only considered a single mutant at time 0, while we are interested in the case when mutants continually enter the population at a rate N t = ∑ n = 0 ∞ n × p n 1 - p 0 = 1 1 - β ( t ) = 1 + Δ e 2 r λ Δ t - ( 1 - Δ ) 2 Δ where µ is the mutation rate per cell division and n 0 is the number of stem cells. To derive the clone size distribution in this case, we take the integral over time multiplied by the mutation rate.



| n 0 |
| --- |


We can approximate g n = μ n 0 r λ ∫ 0 t p n τ d τ = μ n 0 r λ n β ( t ) n which gives



| β ( t ) n = 1 - 1 / N ( t ) n ≈ e - n N ( t ) |
| --- |


The data we make use of doesn’t provide integer clone sizes but rather area of clones, so we can make the transformation g n ≈ μ n 0 r λ n e - n N ( t ) :



| n = ρ A |
| --- |


This is the result presented in the main text.


### Code and data availability

Code to reproduce all the figures in the manuscript (using a snakemake [ Köster and Rahmann, 2012 ] workflow) is available at [GITHUB_REPO_REDACTED] ( [AUTHOR], 2020 ; copy archived at https://elifesciences-publications/dnds-clonesize ). We also created a singularity image with all software dependencies which is available at shub://marcjwilliams1/dnds-clonesize-R-container. Julia ( Bezanson et al., 2017 ) was used for the simulations and R ( R Development Core Team, 2019 ) was used to analyse the data and generate the figures. Some of the analysis rely in bespoke packages written for this study which are freely available under an open source licence.


## Acknowledgements

AS is supported by the Wellcome Trust (202778/B/16/Z) and Cancer Research UK (A22909). TG is supported by the Wellcome Trust (202778/Z/16/Z) and Cancer Research UK (A19771). We acknowledge funding from the National Institute of Health (NCI U54 CA217376) to AS and TG This work was also supported a Wellcome Trust award to the Centre for Evolution and Cancer (105104/Z/14/Z). CPB is supported by the Wellcome Trust (209409/Z/17/Z).


## Funding Statement

The funders had no role in study design, data collection and interpretation, or the decision to submit the work for publication.


## Contributor Information

Marc J [AUTHOR], Email: [EMAIL_REDACTED].

Andrea [AUTHOR], Email: [EMAIL_REDACTED].

Trevor A [AUTHOR], Email: [EMAIL_REDACTED].

Patricia J Wittkopp, University of Michigan, United States.

Alfonso Valencia, Barcelona Supercomputing Center - BSC, Spain.


## Funding Information

This paper was supported by the following grants:

Wellcome 202778/B/16/Z to Andrea [AUTHOR].

Wellcome 202778/Z/16/Z to Trevor A [AUTHOR].

Wellcome 209409/Z/17/Z to Chris P [AUTHOR].

Wellcome 105104/Z/14/Z to Andrea [AUTHOR].

Cancer Research UK A22909 to Andrea [AUTHOR].

Cancer Research UK A19771 to Trevor A [AUTHOR].

H2020 Marie Skłodowska-Curie Actions 846614 to Luis [AUTHOR].

National Institutes of Health CA217376 to Andrea [AUTHOR], Trevor A [AUTHOR].


## Additional information


### Competing interests

No competing interests declared.



Conceptualization, Data curation, Software, Formal analysis, Investigation, Visualization, Methodology.

Formal analysis, Investigation, Methodology.

Formal analysis, Investigation, Methodology.

Conceptualization, Software, Formal analysis, Supervision, Funding acquisition, Investigation, Methodology.

Conceptualization, Formal analysis, Supervision, Funding acquisition, Investigation, Methodology, Project administration.

Conceptualization, Resources, Formal analysis, Supervision, Funding acquisition, Investigation, Methodology, Project administration.


## Additional files


## Data availability

No new data was generated in this; only previously published data is reanalysed. Computer code implementing the new mathematical theory we developed is available here: [GITHUB_REPO_REDACTED] (copy archived at [GITHUB_REPO_REDACTED] ).

The following previously published datasets were used:

Martincorena I, Fowler JC Wabik A, Lawson AAR, Abascal F, Michael Hall WJ, Cagan A, Murai k, Mahbubani K, Stratton MR, Fitzgerald RC, Handford PA, Campbell PJ, Saeb-Parsy K, Jones PH. 2018. EGAD00001004158. European Genome-phenome Archive. EGAD00001004158

Martincorena I, Fowler JC Wabik A, Lawson AAR, Abascal F, Michael Hall WJ, Cagan A, Murai k, Mahbubani K, Stratton MR, Fitzgerald RC, Handford PA, Campbell PJ, Saeb-Parsy K, Jones PH. 2018. EGAD00001004159. European Genome-phenome Archive. EGAD00001004159

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000860. European Genome-phenome Archive. EGAS00001000860

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000515. European Genome-phenome Archive. EGAS00001000515

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000603. European Genome-phenome Archive. EGAS00001000603


# Decision letter


#### Roles

In the interests of transparency, [REDACTED_VENUE] publishes the most substantive revision requests and the accompanying author responses.

The paper represents first a new contribution to the methodology to infer selection coefficients associated of mutations, and, second, the application of the methodology to the comparative study of mutations in normal versus cancer sub-clones. The general findings contribute to our understanding of somatic mutations and tumor evolution, as well as to the ongoing discussion on the role of potential cancer-related mutations in normal tissues.

Decision letter after peer review:

Thank you for submitting your article "[REDACTED_TITLE]" for consideration by [REDACTED_VENUE] . Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Ferran Muinos (Reviewer #1); Jamie Blundell (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper deals with the important issue of understanding how selection of quantifying the selective advantage provided by somatic mutations as a key element to understand tumor evolution.

The proposed method infers selection coefficients associated with mutations that expand in normal tissues as well as subclonal mutations in oesophageal and skin data set (Martincorena et al.,) linking dN/dS and clone size and provides a model of somatic evolution in normal tissues, applying it to the and infer selective advantages for specific genetic loci in normal and cancer tissues, effectively linking SFS and dN/dS ratios..

The paper is timely, since a number of intriguing reports have detected somatic evolution (potential positive selection) in normal tissues that should not be pathogenic. It also aligns well with previous publications; bioRxiv 569566; doi: https://doi.org/10.1101/569566

The referees and editors truly appreciate the approach and consider it an important contribution to the field. Still, we find that it is important to validate the main hypothesis on the estimation of the selection coefficient on mutations in normal tissues.

We will also ask you to consider if the section on cancer is essential for the paper, as it is it is problematic in terms reproducibility and seems rather a distraction of the main argument.

During the revision, you will have the opportunity to address following issues related with clarifications and additional information. We find particularly important to address the ones related with the importance of different mutations in the same gene and the influence of history, e.g. influence of germline mutations in clonal evolution and the potentially transient nature of fitness gains.

Limited applicability questioning the application to cancer cases.

- The method for inferring selective advantages in tumors has one important limitation which is made very clear in the text: the method is not ready for the commonly available data sets. Remarkably, it is apparent that even in the case of high-quality histopathologically-normal tissue data the method has still limited resolution. I wonder whether this low resolution may compromise some of the conclusions drawn after the analysis.

- It is very reassuring from the modeling perspective that the model and subsequent fitting approach yields consistent results with the simulations when applied to the normal tissue data. However, the validation in tumors is lacking. Simulation analyses only confirm that the implementation of the fitting method correctly reflects the model, regardless of the validity of the model.

- The method heavily resorts to the estimation of mutation frequencies. However, this estimation may be difficult, particularly from tumor data with complex chromosomal architectures.

- In summary, there is not enough data for cancer. It is unclear if the section of application to cancer adds much, given the clear statement that there is not enough subclonal recurrence to say very much.

Different mutations in the same gene

- Although it may not affect the validity of the method, the conceptualization of driver mutation presented in the manuscript may obfuscate the interpretation of the results. It is very likely that any mutation found in a gene subject to high selective pressure confers a selective advantage itself, but for genes under mild positive selection this may not be true, whence not all mutations may be bound to drive. Moreover, different driver mutations may confer distinct selective advantages.

- A challenge in using the skin / esophagus data is that the lack of large numbers of people sampled means data is rather sparse. Our experience looking at the blood makes clear that there is often a wide spectrum of fitness effects even for non-syn mutations within the same gene. This effect is not discussed here. Can the authors present an analysis of say the bottom few genes in Figure 3A to test whether there is evidence that the Δ are the same or whether some of the wide variation could be attributable to a variation of Δ even within the gene? I appreciate the data might not be there for a thorough analysis of this though.

- To easily track all the assumptions implied by the models it would be very beneficial for the manuscript to include sketches of the proofs that formally derive the two main functional forms adopted for the mutation density g. This would make the line of reasoning much more transparent and spare the reader the time for literature scrapping.

- Although from the text it seems that the variants implied under the term "mutation" are just coding SNVs, the analysis may well be valid for other types of mutations such as small insertions and deletions or splicing affecting SNVs, as the dN/dS method of choice is equipped to handle them. Please, clarify. Moreover, dNdScv is dependent on the choice of a transcript for the genes analyzed: this choice should be pointed out somewhere in the manuscript.

- The method heavily resorts to the availability of a sufficiently robust method to estimate dN/dS at genetic loci from mutational data. Thus, all the caveats of the method of choice may propagate downstream onto the method described, it is good that these limitations are discussed in the text.

- Motivated by (Introduction) "Enumeration of the selective advantage of each driver mutation enables prediction of future evolutionary dynamics". This claim is more difficult to interpret in the light of your own findings, namely, that there are somatic mutations showing a very significant fitness gain in normal tissues. Consider that those mutations may confer a transient fitness gain until a new homeostatic equilibrium is attained.

- How are the step-sizes of the clone size intervals decided? How coarse these bins can be while still rendering a meaningful fit for the selective coefficients?

- The Discussion section is mainly descriptive and methodological. What can be concluded about the role of NOTCH1 and TP53 in aging and/or tumor initiation in the light of the results in normal tissues?

- The methods are essentially the same (e.g. Equation 4 in this work is Equation 1 in Watson et al., except Watson et al., focusses on SFS view whereas [AUTHOR] et al. focus on the frequency-dependent dN/dS view – though, as the authors know well, these are different ways of viewing exactly the same info!). It should be made very clear that this has been independently developed by Watson et al. This is especially true since the way Watson et al., is cited at the moment is wholly incorrect!

- Internal consistency between syn and non-syn mutations and validating N. The framework presented here, at its heart, analyses the SFS of two classes of mutations (syn vs non-syn) and takes the ratio of these in bins of increasing frequency. However, taking the ratio of the SFS for these classes of mutation throws away important information and means the authors lose the ability to validate N. If instead of taking the ratios they simply plot the SFS for both the syn and nonsyn variants independently then the amplitude of these curves at low frequency will be given by Nμ, which given one can estimate μ enables one to calculate N, which serves as an important validation since you can check agreement with known estimates of 5000/mm2 (as quoted in the text). I would strongly suggest plotting the SFS of each class of mutation independently as outlined in Watson et al., since this does not throw out the N dependence. Furthermore, this inference of N from the amplitude provides an important internal consistency check on characteristic frequency of the clones (what the authors term N(t) in their main text – although as outlined at the end of my review there is a minor error in their equation). The value of N enables one to predict where the synonynous variants should appear as outlined in (Watson et al. bioRxiv 569566; doi: https://doi.org/10.1101/569566). This analysis would greatly strengthen this work as it would challenge the model more substantially.

- Validation of Δ. One major flaw of the work as presented is that the inferences for Δ are not validated or challenged. One approach we found useful is that the Δ make clear predictions for how the SFS should evolve with age. Even though there is no longitudinal sampling, there is a very wide range of ages in the esophagus data and reasonably wide range in the skin data. The authors should check whether the Δ inferred is consistent with how the SFS changes with age. i.e there should be a wider spectrum of frequencies in the older people and a narrower spectrum in younger people. In fact, the characteristic frequency of the clones should increase exponentially with age since the N(t) (characteristic size of the extant non-syn clones) increases exponentially with age so this makes a clear prediction to be checked. Including this analysis would strengthen the manuscript considerably.

- Spatial effects. A challenge with using data from skin and esophagus to check this theoretical framework is that these tissues evolve on a 2D spatially constrained sheet of cells. There was no development or real discussion of how this might affect the theory (which has no explicit spatial effects built in). While a full theoretical treatment of this does seem beyond the scope of this work, it would be nice to see a thorough discussion of it, especially relating to some of the findings in the recent literature e.g. Hall et al., bioRxiv 480756; doi: https://doi.org/10.1101/480756 and Fusco et al., 2016, neither of which were cited.

- High frequency synonymous variants are likely to be genetic hitchhikers. While there was a short discussion of hitchhikers at the end, it was somewhat cursory and not quantitative. Given the theory, the authors can predict what fraction of syn variants are expected to be hitchhikers in the skin / esophagus data and their frequency distribution (this analysis has been performed in Supplementary note 7 of Watson et al., 2019). It would be an important check on the inferences to perform a similar analysis and see if there is agreement with predictions.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "[REDACTED_TITLE]" for further consideration by [REDACTED_VENUE] . Your revised article has been evaluated by Patricia Wittkopp (Senior Editor), a Reviewing Editor, and the original reviewers.

The manuscript has been improved but the two referees still have a number of points that require additional clarification or a better explanation. The one that I find compulsory is a better description of Figure 5, as detailed by the second referee.

- From this reviewer's perspective, the main concerns raised during the first round of reviews have been addressed. The authors have conceded to reshape the paper so as to exclude the cancer part in the interest of applicability and reproducibility.

- The authors have thoroughly addressed all the comments including additional explanations and new figures for the sake of completeness and clarification. In particular, the authors have now conducted a supplementary analysis of the impact of the dN/dS calculation method of choice; have completed the methodological description; have added clarification to the relationship between predictiveness and selective regime; have completed the discussion hypothesizing a temporal dynamics for the expansion of NOTCH1 vs TP53 variants in histopathologically normal oesophageal tissue; have tackled the relevance and limitations of the study regarding the per-site inference of selective advantages; have clarified the impact of bin-sizes at model fitting; and have carried an important new analysis suggested by one of the reviewers to validate Δ.

- The manuscript has clearly improved and feels to have reached a point so that exposure to public scientific debate cannot wait anymore.

Generally I find the manuscript improved relative to the first draft. However there remain a few issues that I believe need to be addressed to really demonstrate whether the numbers inferred using this method are meaningful.

I am glad to see the suggestion made in my first review on ways to challenge the inferred Δ was used by the authors as the basis for the substantial new analysis resulting in Figure 5. I believe the additional analysis strengthens the manuscript. Given that the idea for this analysis comes from an analysis performed in Watson et al., it would be appropriate to clearly acknowledge this in the main text e.g. words to the effect of "Following closely the analysis laid out in Watson et al. we reasoned…" subsection “Site frequency spectra”.

I also have a few questions about this current analysis. First, as mentioned by the authors, the theoretical prediction is that N(t) should increase exponentially with age with the gradient being approximately Δ. In Figure 5D it is not clear to me what data has been used for this plot and how numbers were estimated. If this data is grouped across many genes the predicted increase should not be exponential at all, so it is not clear if this fit is appropriate. The authors need to clarify this. It is more appropriate to perform the analysis on a gene-by-gene basis as shown in Figure 5—figure supplement 1 but this figure highlights that the agreement between the values of Δ using the two methods are not very good (e.g. TP53 is inferred to be ~0.018 on basis of age change vs 0.06 on basis of dN/dS). The log scale on Figure 5—figure supplement 1B obfuscates this. Is the correlation between the methods still significant on a (more standard) linear scale? The y-axis scale on Figure 5C is incorrect: there is a missing factor of rλ (see below too). Generally I think this new analysis is encouraging but would benefit from a more cautionary telling: highlighting how the agreement between inferred values of Δ is far from perfect and might point to more complex dynamics e.g. environmental effects which alter Δ.

There remains an error in Equation. 4. The units are not correct. The density is dimensionless while at present it is proportional to mutation rate (units of 1/time). There is a timescale missing from the expression: which I believe is r \λ and should be in the denominator. The authors should check this.

I am still not convinced the authors have satisfactorily addressed the issue of sites within a gene having different Δ values. While I accept that the current data sets do not have the power to resolve Δ on a site by site basis they can, and in my opinion should, simulate this with some parameterised distribution and test what value of Δ they would infer using their grouped method. Because, if there is a range of Δ for mutations within the same gene, and a single value is inferred, it is not clear that the value inferred represents the average value of Δ across the gene as the authors claim in their rebuttal. This claim should be backed up with simulations if the data do not exist.



Collection date 2020.

The paper deals with the important issue of understanding how selection of quantifying the selective advantage provided by somatic mutations as a key element to understand tumor evolution.

The proposed method infers selection coefficients associated with mutations that expand in normal tissues as well as subclonal mutations in oesophageal and skin data set (Martincorena et al.,) linking dN/dS and clone size and provides a model of somatic evolution in normal tissues, applying it to the and infer selective advantages for specific genetic loci in normal and cancer tissues, effectively linking SFS and dN/dS ratios..

The paper is timely, since a number of intriguing reports have detected somatic evolution (potential positive selection) in normal tissues that should not be pathogenic. It also aligns well with previous publications; bioRxiv 569566; doi: https://doi.org/10.1101/569566

We thank the reviewers and editor for this accurate summary and their constructive and thorough critique of our study. We are glad that our paper is judged important and timely.

The referees and editors truly appreciate the approach and consider it an important contribution to the field. Still, we find that it is important to validate the main hypothesis on the estimation of the selection coefficient on mutations in normal tissues.

We will also ask you to consider if the section on cancer is essential for the paper, as it is it is problematic in terms reproducibility and seems rather a distraction of the main argument.

During the revision, you will have the opportunity to address following issues related with clarifications and additional information. We find particularly important to address the ones related with the importance of different mutations in the same gene and the influence of history, e.g. influence of germline mutations in clonal evolution and the potentially transient nature of fitness gains.

We are glad that the editor and reviewers judge our study favourably. Below, we have addressed the various specific points that challenge (and thus serve to help verify) the main findings of the paper. We have also attempted to refine our analysis as suggested, wherever was feasible to do so. Major changes to the manuscript include validation of the selection coefficients by directly fitting the site frequency spectrum, implementing an alternative dN/dS method and checking that the choice of bin size has limited influence on inferred selection coefficients. Details are provided below.

We have now restricted the manuscript and removed the section on cancer. We agree that the lack of sufficient data in cancer diminishes interest in that section of the manuscript. We would, of course, intend to revisit this as sufficient data become available.

Limited applicability questioning the application to cancer cases.

- The method for inferring selective advantages in tumors has one important limitation which is made very clear in the text: the method is not ready for the commonly available data sets. Remarkably, it is apparent that even in the case of high-quality histopathologically-normal tissue data the method has still limited resolution. I wonder whether this low resolution may compromise some of the conclusions drawn after the analysis.

- It is very reassuring from the modeling perspective that the model and subsequent fitting approach yields consistent results with the simulations when applied to the normal tissue data. However, the validation in tumors is lacking. Simulation analyses only confirm that the implementation of the fitting method correctly reflects the model, regardless of the validity of the model.

- The method heavily resorts to the estimation of mutation frequencies. However, this estimation may be difficult, particularly from tumor data with complex chromosomal architectures.

- In summary, there is not enough data for cancer. It is unclear if the section of application to cancer adds much, given the clear statement that there is not enough subclonal recurrence to say very much.

We agree with this assessment and have now removed the cancer section from the paper.

We also agree that accurate determination of mutant allele frequency is much more problematic in tumour data compared to the ostensibly normal tissue data from Martincorena et al., largely due to copy number alterations and tumour purity. This is a major reason why the cancer data, despite the large number of samples, cannot be analysed with our method.

Different mutations in the same gene

- Although it may not affect the validity of the method, the conceptualization of driver mutation presented in the manuscript may obfuscate the interpretation of the results. It is very likely that any mutation found in a gene subject to high selective pressure confers a selective advantage itself, but for genes under mild positive selection this may not be true, whence not all mutations may be bound to drive. Moreover, different driver mutations may confer distinct selective advantages.

- A challenge in using the skin / esophagus data is that the lack of large numbers of people sampled means data is rather sparse. Our experience looking at the blood makes clear that there is often a wide spectrum of fitness effects even for non-syn mutations within the same gene. This effect is not discussed here. Can the authors present an analysis of say the bottom few genes in Figure 3A to test whether there is evidence that the Δ are the same or whether some of the wide variation could be attributable to a variation of Δ even within the gene? I appreciate the data might not be there for a thorough analysis of this though.

We entirely agree that different mutations in the same gene may have different selective advantages. Indeed, this hypothesis partially explains the phenomenon of ‘hotspot’ mutations (mutations always in the same site(s)) in cancer-associated genes. Consequently, we recognize that a selection coefficient per site would be the most informative way to characterize selection in somatic genomes.

While in theory the approach we have developed could be applied at a site-specific level, we are limited by both the data at hand and methods to evaluate dN/dS at the site level. In terms of the data we used for this study, in some donors in the oesophagus dataset the same mutation appears to arise multiple times independently, but the frequency of these events is always below the 8 mutations necessary to apply our approach (maximum 6 repeated occurrences of the same mutation observed). The reviewer will appreciate that normalising for underlying mutation rate at a site by site level (as opposed to the average rate across a larger locus) is also problematic.

Unfortunately, we are therefore unable to assess selection coefficients at the site level in the available data. We have added sentences to the main text making clear that the inferences we draw are effectively average selection coefficients across the whole gene. We also discuss in more detail how this approach could be extended to the site level with larger cohorts and improved methods to estimate site level dN/dS (Discussion section).

- To easily track all the assumptions implied by the models it would be very beneficial for the manuscript to include sketches of the proofs that formally derive the two main functional forms adopted for the mutation density g. This would make the line of reasoning much more transparent and spare the reader the time for literature scrapping.

We have now included more detail on the proofs at the end of the Materials and methods section.

- Although from the text it seems that the variants implied under the term "mutation" are just coding SNVs, the analysis may well be valid for other types of mutations such as small insertions and deletions or splicing affecting SNVs, as the dN/dS method of choice is equipped to handle them. Please, clarify. Moreover, dNdScv is dependent on the choice of a transcript for the genes analyzed: this choice should be pointed out somewhere in the manuscript.

We have now included more details on the mutations used and the references used to annotate transcript in the subsection “dN/dS calculations”. The reviewer is correct that in principle any type of mutation can be used for the analysis, provided that there is a good null model for the underlying variation in mutation rate across sites/loci.

- The method heavily resorts to the availability of a sufficiently robust method to estimate dN/dS at genetic loci from mutational data. Thus, all the caveats of the method of choice may propagate downstream onto the method described, it is good that these limitations are discussed in the text.

This is an important point, and we are grateful to the reviewers for raising it. To examine the impact of dN/dS calculation methodology, we have now compared the results using a distinct dN/dS method, called SSB-dNdS from Zapataet al., (10.1186/s13059-018-1434-0). This showed consistent results with dndscv. Specifically, we observed the same shape curve in the analysis (Figure 5—figure supplement 1A) and also very consistent results for global dN/dS values for each patient (Figure 5—figure supplement 1C). Gene level values show some variability between the methods, likely due differences between the two methodologies in normalising for local variations in the mutation rate (Figure 5—figure supplement 1B).

We now discuss this issue at greater length (Materials and methods section).

- Motivated by (Introduction) "Enumeration of the selective advantage of each driver mutation enables prediction of future evolutionary dynamics". This claim is more difficult to interpret in the light of your own findings, namely, that there are somatic mutations showing a very significant fitness gain in normal tissues. Consider that those mutations may confer a transient fitness gain until a new homeostatic equilibrium is attained.

We agree that selective regimes can change over time, due to changes in the microenvironmental context (indeed, in the case that the reviewer suggests it is the changing degree of competition with neighbouring cells). Nevertheless, we maintain that quantitative knowledge of the evolutionary dynamics allows for predictions about the future, but that these predictions are only valid for the duration of the selective regime where the measurement was made. We have added this caveat (Introduction).

- How are the step-sizes of the clone size intervals decided? How coarse these bins can be while still rendering a meaningful fit for the selective coefficients?

We used a binsize of 0.025 (area of clone in mm 2 ) for our inferences, however the size of bins makes little difference to the inferences as we integrate over bins in our interval-dN/dS method. Indeed, this is one of the reasons we fitted our model using the integral, as this avoids the trade-offs between binsize and the number of data points in each bin.





> **Figure/Table Caption:** ( a ) Fits to simulation with different bin sizes ( b ) Summary of inferred ∆ for the different bin sizes shows highly consistent results with a small increase in variance at larger bin sizes.

- The Discussion section is mainly descriptive and methodological. What can be concluded about the role of NOTCH1 and TP53 in aging and/or tumor initiation in the light of the results in normal tissues?

We have now broadly revised the discussion following the removal of the cancer section. Following the reviewers’ suggestion, we have also now included a discussion of the hypothesised temporal dynamics of NOTCH1 and TP53 mutation accumulation: we suppose that mutationally-likely NOTCH1-mutants initially repopulate the oesophagus before being replaced by the later arising (mutationally less likely) but fitter TP53-mutant clones (Discussion section).

- The methods are essentially the same (e.g. Equation 4 in this work is Equation 1 in Watson et al., except Watson et al., focusses on SFS view whereas [AUTHOR] et al. focus on the frequency-dependent dN/dS view – though, as the authors know well, these are different ways of viewing exactly the same info!). It should be made very clear that this has been independently developed by Watson et al. This is especially true since the way Watson et al., is cited at the moment is wholly incorrect!

We apologise for mis-citing the Watson et al., study, it is now referred to appropriately (Introduction).

We feel that here it is important to note that the mathematical foundations of our study and that of Watson et al., have long routes in the literature (indeed, the fundamentals go back to Luria and Delbruck and more general classical branching process theory). Moreover, the application of these mathematical ideas to problems in biology is also a well-trodden path, with the large body of work from Benjamin Simons over the past decade being exemplary of this. Thus, with respect, we do not think it appropriate to attribute the mathematical foundations of our study to Watson and colleagues’ paper. We have explained the background of the ‘clonal dynamics inference’ approach in general and in biology in the revised main manuscript (Introduction and Materials and methods section).

- Internal consistency between syn and non-syn mutations and validating N. The framework presented here, at its heart, analyses the SFS of two classes of mutations (syn vs non-syn) and takes the ratio of these in bins of increasing frequency. However, taking the ratio of the SFS for these classes of mutation throws away important information and means the authors lose the ability to validate N. If instead of taking the ratios they simply plot the SFS for both the syn and nonsyn variants independently then the amplitude of these curves at low frequency will be given by Nμ, which given one can estimate μ enables one to calculate N, which serves as an important validation since you can check agreement with known estimates of 5000/mm2 (as quoted in the text). I would strongly suggest plotting the SFS of each class of mutation independently as outlined in Watson et al., since this does not throw out the N dependence. Furthermore, this inference of N from the amplitude provides an important internal consistency check on characteristic frequency of the clones (what the authors term N(t) in their main text – although as outlined at the end of my review there is a minor error in their equation). The value of N enables one to predict where the synonynous variants should appear as outlined in (Watson et al., bioRxiv 569566; doi: https://doi.org/10.1101/569566). This analysis would greatly strengthen this work as it would challenge the model more substantially.

We are grateful for this suggestion, and have considered it in some detail. However, we do not think that the approach is feasible in our current study. Watson et al., used an orthogonal dataset (whole genome sequencing of multiple samples from a single individual) to estimate the mutation rate, which they could then use to decouple the mutation rate from the number of stem cells. However, we do not think that there exists a suitable dataset derived from oesophagus or skin where we could do similar.

Alternatively, we could try and estimate the mutation rate from the Martincorena data itself, however there is the obvious risk of making a circular argument. These data are targeted sequencing of a panel of 72 genes. Our analysis, and indeed the original study too, demonstrate that many of these genes are under strong positive selection, rendering inference of mutation rates problematic.

We do however recognize that directly fitting the site frequency spectrum can provide additional ways to validate our approach, we discuss this in more detail in the next point.

- Validation of Δ. One major flaw of the work as presented is that the inferences for Δ are not validated or challenged. One approach we found useful is that the Δ make clear predictions for how the SFS should evolve with age. Even though there is no longitudinal sampling, there is a very wide range of ages in the esophagus data and reasonably wide range in the skin data. The authors should check whether the Δ inferred is consistent with how the SFS changes with age. i.e there should be a wider spectrum of frequencies in the older people and a narrower spectrum in younger people. In fact, the characteristic frequency of the clones should increase exponentially with age since the N(t) (characteristic size of the extant non-syn clones) increases exponentially with age so this makes a clear prediction to be checked. Including this analysis would strengthen the manuscript considerably.

This is an excellent point and we thank the reviewer for highlighting the additional information provided by the site frequency spectrum and the ways it could be used to validate the results from our interval-dN/dS approach. We have now added a new Figure 5 where we analyse the site frequency spectrum directly to attempt to validate our interval-dN/dS derived conclusions.

Analysis of the SFS reveals the age-dependent trends that the reviewer expects, namely larger clones and greater variability in clone size in older people (Figure 5A). We also observe the prediction that the characteristic frequency of non-synonymous mutations should increase markedly with age and a more modest increase for synonymous mutations (Figure 5D).

We also now challenge the underlying theoretical model of clonal expansion dynamics by fitting two alternate models of clonal dynamics directly to the site frequency spectrum. The three models we fit are as follows (y is clone size and A and B are parameters to be inferred):

Here model 1 is the “correct” model and models 2 and 3 are simplifications which only include the exponential decay or a power law. Using the widely applicable information criteria (WAIC), we find that the ‘correct’ model 1 provides the best predictive power (lowest WAIC) (Figure 5B).

We also performed the fit of the clonal dynamics model on a gene-by-gene basis, however due to limited data points we found the uncertainty in our posterior estimates of the parameters to be large, precluding further insight at the gene level with this approach. Figure 5—figure supplement 3 shows the fits for NOTCH1 and TP53 and posterior estimates of the characteristic frequency.

As an alternative method to ‘validate’ our gene-level selective coefficients, we therefore turned to a purely statistical model and performed a Bayesian multi-level regression on area~age with genes as random effects. This analysis found that TP53 and NOTCH1 were the genes with the highest coefficients for the slopes (ie mutations in genes increase in clone size as a function of age to a greater extent than all other genes (Figure 5—figure supplement 5A)). Further, these regression coefficients were correlated with our inferred selection coefficients, supporting the conclusions from our interval dN/dS method (Figure 5—figure supplement 4B).

In summary, direct analysis of the site frequency spectrum data support our original conclusions.

- Spatial effects. A challenge with using data from skin and esophagus to check this theoretical framework is that these tissues evolve on a 2D spatially constrained sheet of cells. There was no development or real discussion of how this might affect the theory (which has no explicit spatial effects built in). While a full theoretical treatment of this does seem beyond the scope of this work, it would be nice to see a thorough discussion of it, especially relating to some of the findings in the recent literature e.g. Hall et al., bioRxiv 480756; doi: https://doi.org/10.1101/480756 and Fusco et al., 2016, neither of which were cited.

We agree that spatial effects can be important, we have added a note about this and cited both papers in the Discussion section. We have assumed that clones experience minimal interference from other clones and so spatial effects are minimised. There is some supporting evidence for the reasonableness of this assumption that is provided below in response to the hitchhiker comment.

- High frequency synonymous variants are likely to be genetic hitchhikers. While there was a short discussion of hitchhikers at the end, it was somewhat cursory and not quantitative. Given the theory, the authors can predict what fraction of syn variants are expected to be hitchhikers in the skin / esophagus data and their frequency distribution (this analysis has been performed in Supplementary note 7 of Watson et al., 2019). It would be an important check on the inferences to perform a similar analysis and see if there is agreement with predictions.

To look at the influence of hitchhikers in the oesophagus dataset we leveraged the spatial information in the sequenced patches. In the dataset each donor had approximately 90 distinct small pieces of tissue that were sequenced, and we note that each of these pieces contained multiple clones. We reasoned that pieces containing selected clones would be expected to have a larger number of detectable synonymous mutations if hitchhiking was common. We also expect the hitchhiking synonymous mutations to have larger clone size than non-hitchhikers. To test these hypotheses we counted the number of non-synonymous NOTCH1 and TP53 mutations (these being the clones with the highest fitness) as well as the number of synonymous mutations (and their VAF) in each piece of tissue.

Figure 5—figure supplement 1A,B shows the number of synonymous mutations as a function of the number of nonsynonymous NOTCH1 and TP53 mutations in a patch. Figure 5—figure supplement 1C,D shows the VAF of synonymous mutations as a function of the number of non-synonymous NOTCH1 and TP53 mutations in a patch. There was no relationship between the number of selected clones and synonymous mutation VAF (by linear regression). A significant correlation between the number of selected clones and synonymous mutation burden was observed (p=0.0002 for NOTCH1, p=0.031 for TP53) suggesting the presence of a small number of synonymous hitchhikers in the dataset. The regression coefficients show that for each additional nonsynonymous mutation we get ~0.05 (0.047 for NOTCH1 and 0.057 for TP53) additional synonymous mutations. We note too that the correlation is very noisy (R 2 <0.02). Thus, we conclude that the number of hitchhiking synonymous mutations is minimal.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

- From this reviewer's perspective, the main concerns raised during the first round of reviews have been addressed. The authors have conceded to reshape the paper so as to exclude the cancer part in the interest of applicability and reproducibility.

- The authors have thoroughly addressed all the comments including additional explanations and new figures for the sake of completeness and clarification. In particular, the authors have now conducted a supplementary analysis of the impact of the dN/dS calculation method of choice; have completed the methodological description; have added clarification to the relationship between predictiveness and selective regime; have completed the discussion hypothesizing a temporal dynamics for the expansion of NOTCH1 vs TP53 variants in histopathologically normal oesophageal tissue; have tackled the relevance and limitations of the study regarding the per-site inference of selective advantages; have clarified the impact of bin-sizes at model fitting; and have carried an important new analysis suggested by one of the reviewers to validate Δ.

- The manuscript has clearly improved and feels to have reached a point so that exposure to public scientific debate cannot wait anymore.

We thank the reviewer for the positive assessment of our manuscript.

Generally I find the manuscript improved relative to the first draft. However there remain a few issues that I believe need to be addressed to really demonstrate whether the numbers inferred using this method are meaningful.

I am glad to see the suggestion made in my first review on ways to challenge the inferred Δ was used by the authors as the basis for the substantial new analysis resulting in Figure 5. I believe the additional analysis strengthens the manuscript. Given that the idea for this analysis comes from an analysis performed in Watson et al. it would be appropriate to clearly acknowledge this in the main text e.g. words to the effect of "Following closely the analysis laid out in Watson et al. we reasoned…" subsection “Site frequency spectra”.

We thank the reviewer for recognizing that the new analysis strengthens the manuscript and for motivating us to perform this analysis. We have added the reference to Watson et al., and also to the other earlier papers that perform a similar analysis.

I also have a few questions about this current analysis. First, as mentioned by the authors, the theoretical prediction is that N(t) should increase exponentially with age with the gradient being approximately Δ. In Figure 5D it is not clear to me what data has been used for this plot and how numbers were estimated. If this data is grouped across many genes the predicted increase should not be exponential at all, so it is not clear if this fit is appropriate.





> **Figure/Table Caption:** ( a ) Inferred N(t) as a function for age in a simulated cohort, equivalent to Figure 5D. ( b ) Posterior estimates for inferred values in black, with ground truth shown with red circular points, for this “ground truth” we calculated N(t) using Δ=0.05, the mean of the exponential distribution used in the simulations..

We also note that a large proportion of the non-synonymous mutations are in NOTCH1 and TP53 meaning that these genes are likely responsible for a large proportion of the effect we observe. Out of 813 nonsense mutations 36% (300) are in the NOTCH1 gene and 7% (59) are in TP53, of the 3558 missense mutations 27% (951) are in NOTCH1 and 11% (392) are in TP53.

The authors need to clarify this. It is more appropriate to perform the analysis on a gene-by-gene basis as shown in Figure 5—figure supplement 1 but this figure highlights that the agreement between the values of Δ using the two methods are not very good (e.g. TP53 is inferred to be ~0.018 on basis of age change vs 0.06 on basis of dN/dS). The log scale on Figure 5—figure supplement 1B obfuscates this. Is the correlation between the methods still significant on a (more standard) linear scale? The y-axis scale on Figure 5C is incorrect: there is a missing factor of rλ (see below too). Generally, I think this new analysis is encouraging but would benefit from a more cautionary telling: highlighting how the agreement between inferred values of Δ is far from perfect and might point to more complex dynamics e.g. environmental effects which alter Δ.

We apologise if some of the details of our approach were unclear, we have made some changes to the manuscript that we hope highlights the following points.

Firstly, we highlight that we attempted to fit the distribution per gene but found there were too few data points per gene which resulted in large (3 orders of magnitude) posterior estimates of parameters, see Figure 5—figure supplement 2.

As we could not fit the distributions per gene directly we resorted to a statistical model to assess which genes showed the largest increases in clone size as a function of age, reasoning that this would be a qualitative rather than quantitative validation of the fitness estimates (Figure 5—figure supplement 1). We have added this qualifier in subsection “Site frequency spectra” (“…providing qualitative support for our approach”). We therefore note that we would not expect the regression coefficients to match those values we infer from our i-dN/dS method. We do however observe that those genes with the largest fitness effects also have the largest regression coefficients, in line with predictions (in other words the bias is systematic, not random, and therefore we think the regression approach is provides useful insight).





> **Figure/Table Caption:** Dark blue density labelled y is the real data and lighter blue lines labelled yrep are datasets simulated from the posterior.

We note that one option to attempt to validate Δ is noting that the mean clone size, x as a function of age is given by (see Klein et al., equation S12 for derivation):





> **Figure/Table Caption:** Points represent the mean values and lines show 95% intervals.

In summary therefore, we believe this analysis serves as qualitative rather than quantitative support for our approach.

We have also changed the plot to be on a linear scale, the statistics we reported originally were on the linear scale so remain valid.

There remains an error in Equation. 4. The units are not correct. The density is dimensionless while at present it is proportional to mutation rate (units of 1/time). There is a timescale missing from the expression: which I believe is r \λ and should be in the denominator. The authors should check this.

We previously defined the mutation rate as mutations per symmetric division which is equivalent to the mutation rate per division scaled by the turnover rate, 𝑟𝜆. This definition was buried in the methods however, in order to clarify we now use 𝜇 for mutations per division and therefore include 𝑟𝜆 in the denominator in all relevant equations. We thank the reviewer for highlighting this potential source of confusion. We have therefore changed the Materials and methods section to reflect this.

I am still not convinced the authors have satisfactorily addressed the issue of sites within a gene having different Δ values. While I accept that the current data sets do not have the power to resolve Δ on a site by site basis they can, and in my opinion should, simulate this with some parameterised distribution and test what value of Δ they would infer using their grouped method. Because, if there is a range of Δ for mutations within the same gene, and a single value is inferred, it is not clear that the value inferred represents the average value of Δ across the gene as the authors claim in their rebuttal. This claim should be backed up with simulations if the data do not exist.

Using the same approach, we described above we have now performed these suggested simulations. The simulations provide confirmation that if there is a range of Δ for mutations within the same gene then the inferred Δ is an average effect for that gene.

To perform these simulations we assumed Δ was exponentially distributed, and generated 500 synthetic cohorts. Every new mutation entering the population in the simulations has an exponentially distributed fitness effect, and thus each cohort has a range of different fitness effects. We applied our method to estimate Δ for every cohort and assessed the values we estimated. Below is a histogram of these values for 3 different mean values of the exponential distribution, demonstrating that the value we estimate is consistent with the mean of the distribution of Δ. Median values and 95% intervals of these histograms are 0.078 (0.014 – 0.338), 0.114 (0.0224 – 0.382), 0.203 (0.0643 – 0.503). We have added Figure 2 —figure supplement 1 and included a description of these results in lines the Results section.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Data Citations


## Supplementary Materials


## Data Availability Statement

Code to reproduce all the figures in the manuscript (using a snakemake [ Köster and Rahmann, 2012 ] workflow) is available at [GITHUB_REPO_REDACTED] ( [AUTHOR], 2020 ; copy archived at https://elifesciences-publications/dnds-clonesize ). We also created a singularity image with all software dependencies which is available at shub://marcjwilliams1/dnds-clonesize-R-container. Julia ( Bezanson et al., 2017 ) was used for the simulations and R ( R Development Core Team, 2019 ) was used to analyse the data and generate the figures. Some of the analysis rely in bespoke packages written for this study which are freely available under an open source licence.

No new data was generated in this; only previously published data is reanalysed. Computer code implementing the new mathematical theory we developed is available here: [GITHUB_REPO_REDACTED] (copy archived at [GITHUB_REPO_REDACTED] ).

The following previously published datasets were used:

Martincorena I, Fowler JC Wabik A, Lawson AAR, Abascal F, Michael Hall WJ, Cagan A, Murai k, Mahbubani K, Stratton MR, Fitzgerald RC, Handford PA, Campbell PJ, Saeb-Parsy K, Jones PH. 2018. EGAD00001004158. European Genome-phenome Archive. EGAD00001004158

Martincorena I, Fowler JC Wabik A, Lawson AAR, Abascal F, Michael Hall WJ, Cagan A, Murai k, Mahbubani K, Stratton MR, Fitzgerald RC, Handford PA, Campbell PJ, Saeb-Parsy K, Jones PH. 2018. EGAD00001004159. European Genome-phenome Archive. EGAD00001004159

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000860. European Genome-phenome Archive. EGAS00001000860

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000515. European Genome-phenome Archive. EGAS00001000515

Martincorena I, Roshan A, Gerstung M, Ellis P, Van Loo P, McLaren S, Wedge DC, Fullam A, Alexandrov LB, Tubio JM, Stebbings L, Menzies A, Widaa S, Stratton MR, Jones PH, Campbell PJ. 2016. EGAS00001000603. European Genome-phenome Archive. EGAS00001000603
