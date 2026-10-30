# De-Identified Manuscript `OPEN_ANON_014`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Genetic effects on complex traits may depend on context, such as age, sex, environmental exposures, or social settings. However, it remains often unclear if the extent of context dependency, or gene-by-environment interaction (GxE), merits more involved models than the additive model typically used to analyze data from genome-wide association studies (GWAS). Here, we suggest considering the utility of GxE models in GWAS as a trade-off between bias and variance parameters. In particular, we derive a decision rule for choosing between competing models for the estimation of allelic effects. The rule weighs the increased estimation noise when context is considered against the potential bias when context dependency is ignored. In the empirical example of GxSex in human physiology, the increased noise of context-specific estimation often outweighs the bias reduction, rendering GxE models less useful when variants are considered independently. However, for complex traits, we argue that the joint consideration of context dependency across many variants mitigates both noise and bias. As a result, polygenic GxE models can improve both estimation and trait prediction. Finally, we exemplify (using GxDiet effects on longevity in fruit flies) how analyses based on independently ascertained ‘top hits’ alone can be misleading, and that considering polygenic patterns of GxE can improve interpretation.

Research organism: D. melanogaster , Human


## Introduction

In organisms and study systems where the environment can be tractably manipulated, gene-by-environment interactions (GxE) are the rule, not the exception ( El Soda et al., 2014 ; Vieira et al., 2000 ; Des Marais et al., 2013 ; [AUTHOR] and Kruglyak, 2008 ; Paaby and Rockman, 2014 ). Yet, in complex (polygenic) human traits, there are but a few cases in which models that incorporate GxE explain data—such as genome-wide association study (GWAS) data—better than parsimonious models that assume additive contributions of genetic and environmental factors ( Munafò et al., 2014 ; Kraft and Aschard, 2015 ; Sella and Barton, 2019 ). This is true for both physical environments but also for other definitions of ‘E’, broadly construed to be any context that modifies genetic effects, such as age, sex, or social setting ( Zhu et al., 2023 ; Schwaba et al., 2023 ; Elgart et al., 2022 ; Duncan and Keller, 2011 ; Gibson and Lacek, 2020 ; Brown et al., 2016 ; Ge et al., 2017 ; Balliu et al., 2021 ). GWAS commonly estimate marginal additive effects of an allele on a trait. The estimand here can be thought of as the average effect of the allele over a distribution of multidimensional contexts ( Veller et al., 2023 ). With this view, some differences in allelic effects across contexts are likely omnipresent, but may very well be small, such that the cost of including additional parameters (for context-specific effects) outweighs the benefit of measuring heterogeneous effects. Here, we consider this problem and its connection to the currently underwhelming utility of GxE models in GWAS. First, we rigorously describe the statistical trade-off involved in estimating context specificity at the level of a single variant. Then, we highlight ways in which this trade-off might change as we consider GxE in complex traits, involving numerous genetic variants simultaneously. We begin by framing the problem of estimating context specificity at an individual variant as a bias-variance trade-off. For example, consider the estimation of an allelic effect on lung cancer risk that depends on smoking status. When the allelic effect is estimated from a sample without considering smoking status, the estimate would be biased with respect to the true effect in smokers. We can estimate the effect separately in smokers and non-smokers to eliminate the bias, but the consideration of the additional parameters—smoking status-specific effects—has an associated cost of increasing the estimation variance, compared to an estimator that ignores smoking status. This bias-variance trade-off is closely related to the ‘signal-to-noise’ ratio, where the signal of interest is the true difference in context-specific allelic effects. To demonstrate this trade-off in real data, we consider sex-specific effects on physiological traits in humans. We show that for the majority of traits, it is typically unhelpful to model sex dependency for individual sites since the increase in noise vastly outweighs the signal. We then consider the extension to GxE in complex traits. Complex trait variation is primarily due to numerous genetic variants of small effects distributed throughout the genome ( Fisher, 1930 ; Falconer and Mackay, 1996 ; Yengo et al., 2022 ; Zwick et al., 2000 ). Simultaneously considering GxE across multiple variants may decrease estimation noise if the extent and mode of context specificity is similar across numerous variants. This would tilt the scale in favor of context-dependent estimation. In addition, we show how conventional approaches for detecting and characterizing GxE, which focus on the most significant associations, may lead to erroneous conclusions. Finally, we discuss implications for complex trait prediction (with polygenic scores). We suggest a future focus on prediction methods that empirically learn the extent and nature of context dependency by simultaneously considering GxE across many variants.


## Results and discussion


### Modeling context-dependent effect estimation as a bias-variance trade-off


#### The problem setup

We consider a sample of n + m individuals characterized as being in one of two contexts, A or B of the individuals are in context A with the remaining m individuals in context B . We measure a continuous trait for each individual, denoted by



| y 1 , … , y n ⏞ A , y n + 1 , … , y n + m ⏞ B . |
| --- |


We begin by considering the estimation of the effect of a single variant on the continuous trait. We assume a generative model of the form



| y i ∼ { N ( α A + β A g i , σ A 2 ) if i ∈ { 1 , … , n } N ( α B + β B g i , σ B 2 ) if i ∈ { n + 1 , … , n + m } , | (1) |
| --- | --- |


where β A and β B are fixed, context-specific effects of a reference allele at a biallelic, autosomal variant i , g i ∈ { 0 , 1 , 2 } is the observed reference allele count. α A and α B are the context-specific intercepts, corresponding to the mean trait for individuals with zero reference alleles in context A and B , respectively. σ A 2 and σ B 2 are context-specific observation variances. We would like to estimate the allelic effects β A and β B .


#### Estimation approaches

We compare two approaches to this estimation problem. The first approach, which we refer to as GxE estimation, is to stratify the sample by context and separately perform an ordinary least squares (OLS) regression in each sample. This approach yields two estimates, β ^ A and β ^ B , the OLS estimates of β A and β B of the generative model in Equation 1 , respectively. This estimation model is equivalent to a linear model with a term for the interaction between context and reference allele count, in the sense that context-specific allelic effect estimators have the same maximum likelihood estimators in the two models (see Appendix 1). The second approach, which we refer to as additive estimation, is to perform an OLS regression on the entire sample and use the allelic effect estimate to estimate both β A and β B . We denote this estimator as β ^ A ∪ B , to emphasize that the regression is run on all individuals from context A and context B . This estimation model posits that for i = 1 , … , n + m ,



| y i ∼ N ( α A ∪ B + β A ∪ B g i , σ A ∪ B 2 ) , | (2) |
| --- | --- |


where α A ∪ B is the mean trait value for an individual with zero reference alleles, β A ∪ B is the additive allelic effect and σ A ∪ B 2 is the observation variance which is independent of context. Notably, this model differs from the generative model assumed above: β A ∪ B may not equal β A and β B ; in addition, this model ignores heteroskedasticity across contexts.


#### Error analysis

We focus on the mean squared error (MSE) of the additive and GxE estimators for the allelic effect in context A . The estimator minimizing the MSE may differ between contexts A and B , but the analysis for context B is analogous. When selecting between these two estimation approaches, a bias-variance decomposition of the MSE is useful. Based on OLS theory ( Casella and Berger, 2021 , Theorem 11.3.3), under the model specified above, we have



| β ^ A ∼ N ( β A , V A ) , |
| --- |


where V A = σ A 2 ∑ i = 1 n ( g i − g ¯ A ) 2 and g ¯ A is the mean genotype of individuals in context A . The unbiasedness of the GxE estimator implies



| M S E ( β ^ A , β A ) = V A , |
| --- |


where M S E ( β ^ A , β A ) is the mean squared error of estimating β A with β ^ A . The case of the additive estimator, β ^ A ∪ B , is a bit more involved. As we show in the Methods section, we can write



| β ^ A ∪ B = ω A β ^ A + ω B β ^ B | (3) |
| --- | --- |


for non-negative weights ω A and ω B (that need not sum to 1). Further, we show in Equation 7 of the Methods section that ω A ∝ n H A and ω B ∝ m H B , where H A and H B are the sample heterozygosities in contexts A and B , respectively. Using Equation 3 , we may write



| M S E ( β ^ A ∪ B , β A ) = B i a s 2 ( β ^ A ∪ B , β A ) + V a r ( β ^ A ∪ B ) = ( ( ω A − 1 ) β A + ω B β B ) 2 + ω A 2 V A + ω B 2 V B , |
| --- |


where V B is defined analogously to V A . Thus, with MSE as our metric for comparison, we prefer the GxE estimator in context A when



| M S E ( β ^ A ∪ B , β A ) > M S E ( β ^ A , β A ) , |
| --- |




| ( ( ω A − 1 ) β A + ω B β B ) 2 + ω A 2 V A + ω B 2 V B > V A . | (4) |
| --- | --- |


We refer to Equation 4 as the ‘decision rule’, since it guides us on the more accurate estimator; to minimize the MSE, we will use the context-specific estimator if and only if the inequality is satisfied. To gain some intuition about the important parameters here, we first consider the case of equal allele frequencies (and hence equal heterozygosities) in both contexts and equal estimation variance in both contexts. In this case, the GxE estimator is advantaged by larger context specificity (larger | β A − β B | ) and disadvantaged by larger estimation noise (larger V A = V B ) ( Figure 1 ). In fact, the decision boundary (i.e. the point at which the two models have equal MSE) can be written as a linear combination of | β A − β B | and V A ( Figure 1C ). In this special case, we show in the Methods section that Equation 4 is an equality when



| m 2 n / β A − β B / − V A = 0. | (5) |
| --- | --- |



> **Figure/Table Caption:** The x -axis shows the difference in context-specific effects, while the y -axis shows the standard deviation of the context-specific estimators—both in raw measurement units. The color on the plot indicates the difference between the additive and gene-by-environment interaction (GxE) estimators in bias ( A ), variance ( B ), or mean squared error (MSE) ( C ). ( A ) Only the additive estimator is potentially biased. The bias is proportional to the difference in context-specific effects and independent of the estimation noise. ( B ) The difference in variance is proportional to context-specific estimation noise and independent of the difference of context-specific effects. ( C ) The decision boundary is linear in both the estimation noise and the difference between context-specific effects.

More generally, in the case where H A = H B but V A ≠ V B , we show in the Methods section that we can write Equation 4 as



| ( β A − β B ) 2 V A > 1 + ω A 1 − ω A − V B V A . | (6) |
| --- | --- |


This dimensionless re-parameterization of the decision rule makes explicit its dependence on three factors. ( β A − β B ) 2 V A can be viewed as the ‘signal-to-noise’ ratio: it captures the degree of context specificity (the signal) relative to the estimation noise in the focal context, A 1 + ω A 1 − ω A is the relative contribution to heterozygosity, which equals the relative contribution to variance in the independent variable of the OLS regression of Equation 2 . V B V A is the ratio of context-specific estimation noises. In Appendix 1, we extend the decision rule for the case of a continuous context variable. For a given trait and context, we can consider the behavior of the decision rule across variants with variable allele frequencies and allelic effects. The ratio of estimation noises, r := V A V B , will not be constant. However, in some cases, considering a fixed r across variants is a good approximation. In GWAS of complex traits, each variant often explains a small fraction of trait variance. As a result, the estimation noise is effectively a matter of trait variance and heterozygosity alone. If per-site heterozygosity is similar in strata A and B , as it is, for example, for autosomal variants in biological males and females, r is approximately fixed across variants ( Zhu et al., 2023 ). Figure 2 illustrates the linearity of the decision boundary under the assumption that r is fixed across variants. It also shows that the slope of the decision boundary changes as a function of r . Intuitively, we are less likely to prefer GxE estimation for the noisier context. In fact, for sufficiently small values of r (e.g. r < 1 3 for ω A = 1 2 ), 1 + ω A 1 − ω A − V B V A will be negative. This corresponds to the situation where V A ≪ V B , in which case the additive estimator is never preferable to the GxE estimator in estimating β A , as the signal-to-noise ratio is always non-negative. Typically, this will also imply that the additive estimator is greatly preferable for estimating β B , as β ^ B will be extremely noisy.


> **Figure/Table Caption:** In all panels, the heterozygosity of the variant is assumed to be equal across contexts. The x and y axes are the same as in Figure 1 . ( A ) Estimation noise in the focal context, A , is half that of the other context, B . ( B ) Estimation noise is equal in both contexts. ( C ) Estimation noise in focal context is double that of the other context.

It is natural to ask where the decision rule of Equation 4 falls with respect to empirical GWAS data. We considered the example of biological sex as the context (GxSex), and examined sex-stratified GWAS data across 27 continuous physiological traits in the UK Biobank ( Bycroft et al., 2018 ; Zhu et al., 2023 ). For each of 9 million variants, we estimated the difference in sex-specific effects and the variance of each marginal effect estimator in males. Then, using an estimate of the ratio of sex-specific trait variances as a proxy for the ratio of estimation variances of males and females, we approximated the linear decision boundary between the additive and GxE estimators ( Figure 3A and B ; Appendix 1—figure 2 , Appendix 1—figure 3 ). To demonstrate the accuracy of our decision rule, we employed a data-splitting technique where we estimate the MSE difference between estimators in a training set and evaluate the accuracy in a holdout set ( Appendix 1—figure 1 ). For almost all traits examined, very few allelic effects in males are expected to be more accurately estimated using the male-specific estimator (usually between 0% and 0.1%). Notable exceptions to this rule are testosterone, sex hormone binding globulin (SHBG), and waist-to-hip ratio adjusted for body mass index, for which roughly 0.5% of allelic effects are expected to be better estimated with the GxE model ( Figure 3B ). However, when considering only SNPs that are genome-wide significant in males (marginal p-value < 5 × 10 − 8 in males), many traits show a much larger proportion of effects that would be better estimated by the GxE model. At an extreme, for testosterone, all genome-wide significant SNPs are expected to be better estimated by the GxE model. In addition, a large fraction of genome-wide significant effects are better estimated with the GxE model for creatinine (62%), arm fat-free mass (24%), waist-to-hip ratio (19%), and SHBG (18%) as well ( Figure 3D ).


> **Figure/Table Caption:** ( A, B ) The x -axis shows the estimated absolute difference between the effect of variants in males and females. The y -axis shows the measured standard error for each variant in males, the focal context here. The dashed line shows the decision boundary for effect estimation in males. The difference in mean squared error (MSE) between estimation methods increases linearly with distance from the dashed line, as in Figure 2 . If a variant falls above (below) the line, the additive (gene-by-environment interaction [GxE]) estimator has a lower MSE. ( A ) shows a random sample of 15K single nucleotide variants whereas ( B ) shows only variants with a marginal p-value less than 5 × 10 − 8 in males. ( C, D ) The percent of effects in males which would be better estimated by the GxE estimator, across continuous physiological traits. (Note the difference in scale between the two panels.) To estimate these percentages, one single nucleotide variant is sampled from each of 1700 approximately independent autosomal linkage blocks, and this procedure is repeated 10 times. Shown are average percentages across the 10 iterations.

The decision rule we derived could potentially guide more accurate allelic effect estimation approaches. However, the consideration of GxE pattern sharing across many variants (polygenic GxE) can alter both bias and variance and therefore the trade-off. In our discussion of complex traits that follows, we therefore expand on the rule through qualitative consequences of polygenic GxE, and no longer stick to the analytical single variant rule.


### Context dependency in complex traits

At the single variant level, and specifically when variants are considered independently from one another, we have discussed how the accurate estimation of allelic effects can be boiled down to a bias-variance trade-off. For complex traits, genetic variance is often dominated by the contribution of numerous variants of small effects that are best understood when analyzed jointly ( Sella and Barton, 2019 ; Sinnott-Armstrong et al., 2021 ; Shi et al., 2016 ; Boyle et al., 2017 ; Liu et al., 2019 ; Wray et al., 2018 ; Yengo et al., 2022 ). It stands to reason that to evaluate context dependence in complex traits, we would also want to jointly consider polygenic patterns, rather than just the patterns at the loci most strongly associated with a trait ( Urbut et al., 2019 ; Gibson and Lacek, 2020 ; Zhang et al., 2021 ; Paaby and Gibson, 2016 ; Aschard et al., 2017 ; Des Marais et al., 2013 ). Motivated by this rationale, we recently inferred polygenic GxSex patterns in human physiology ( Zhu et al., 2023 ). One pattern that emerged as a common mode of GxSex across complex physiological traits is ‘amplification’: a systematic difference in the magnitude of genetic effects between the sexes. Moving beyond sex and considering any context, amplification can happen if, for example, many variants regulate a shared pathway that is moderated by a factor—and that factor varies in its distribution among contexts. Amplification is but one possible mode of polygenic GxE, but can serve as a guiding example for ways in which GxE may be pervasive but difficult to characterize with existing approaches ( Zhu et al., 2023 ; Gibson and Dworkin, 2004 ; Miao et al., 2022 ; Balliu et al., 2021 ). In what follows, we will therefore use the example of pervasive amplification (across causal effects) to illustrate the interpretive advantage of considering context dependency across variants jointly, rather than independently.


#### A focus on ‘top hits’ may lead to mischaracterization of polygenic GxE

A common approach to the analysis of context dependency involves two steps. First, categorization of context dependency (or lack thereof) is performed for each variant independently. Second, variants falling under each category are counted and annotated across the genome. Some recent examples of this approach toward the characterization of GxE in complex traits include studies of GxSex effects on flight performance in Drosophila ( Spierer et al., 2021 ), GxSex effects on various traits in humans ( Traglia et al., 2022 ; Bernabeu et al., 2021 ), and GxDietxAge effects on body weight in mice ( Wright et al., 2022 ). Characterizing polygenic trends by summarizing many independent hypothesis tests may miss GxE signals that are subtle and statistically undetectable at each individual variant, yet pervasive and substantial cumulatively across the genome. To characterize polygenic GxE based on just the ‘top hits’ may lead to ascertainment biases, with respect to both the pervasiveness and the mode of GxE across the genome. Much like the heritability of complex traits is thought to be due to the contribution of many small (typically sub-significant) effects ( Boyle et al., 2017 ; Sinnott-Armstrong et al., 2021 ), when GxE is pervasive we may expect that the sum of many small differences in context-specific effects accounts for the majority of GxE variation. For concreteness, we consider in more depth one recent study characterizing GxDiet effects on longevity in Drosophila melanogaster ( Pallares et al., 2023 ). In this study, Pallares et al. tracked caged fly populations given one of two diets: a ‘control’ diet and a ‘high-sugar’ diet. Across 271K single nucleotide variants, the authors tested for association between alleles and their survival to a sampling point (thought of as a proxy for ‘lifespan’ or ‘longevity’) under each diet independently. Then, they classified variants according to whether or not their associations with survivorship were significant under each diet as follows:

Significant under neither diet → classify as no effect .

Significant when fed the high-sugar diet, but not when fed the control diet → classify as high-sugar-specific effect .

Significant when fed the control diet, but not when fed the high-sugar diet → classify as control-specific effect .

Significant under both diets → classify as shared effect .

This authors’ choice of four categories a variant may fall into may be motivated by the wish to test for the presence of ‘cryptic genetic variation’—genetic variation that is maintained in a context where it is functionally neutral but carries large effects in a new or stressful context ( Gibson and Dworkin, 2004 ; Paaby and Rockman, 2014 ; Young et al., 2016 ; Des Marais et al., 2013 ). Indeed, of the variants Pallares et al. classified as having an effect (one-hundredth of variants tested), approximately 31% were high-sugar specific, while the remaining 69% of the variants were shared. Fewer than 1% were labeled as having control-specific effects. They concluded that high-sugar-specific effects on longevity are pervasive, compatible with the hypothesis of widespread cryptic genetic variation for longevity. This characterization of GxE, based on ‘top hits’, places an emphasis on the context(s) in which trait associations are statistically significant, rather than on estimating how the context-specific effects covary. In addition, this particular classification system also does not cover all possible ways in which context-specific effects may differ. In Appendix 1, we discuss these interpretation difficulties further.

We next show that a generative model that differs qualitatively from the cryptic genetic variation model yields results that are highly similar to those observed by Pallares et al. We simulated data under pervasive amplification. Specifically, we sampled from a mixture of 40% of variants having no effect under either diet and 60% of variants having an effect under both diets—but exactly 1.4× larger under a high-sugar diet. We then simulated the noisy estimation of these effects and employed the classification approach of Pallares et al. to the simulated data (Methods). The patterns of allelic effects in the control compared to high-sugar contexts were qualitatively similar in the experimental data and our pervasive amplification simulation. This is true both genome-wide ( Figure 4A compared to Figure 4B ) and for the set of variants classified as significant with their classification approach ( Figure 4C compared to Figure 4D ). The similarity of ascertained variants further highlights caveats of interpretation based on the classification of ‘top hits’: despite the fact that we did not simulate any variants that only have an effect under the high-sugar diet, approximately 36% of significant variants were classified as specific to the high-sugar diet (green points in Figure 4D ), comparable to the 31% of variants classified as high-sugar specific in the experimental data ( Figure 4C ). These variants simply have sub-significant associations in the control group and significant associations in the high-sugar group. In addition, every variant in the shared category (blue points in Figure 4D ) in fact has a larger effect in the high-sugar diet than in the control diet, which cannot be captured by the classification system itself but represents the only mode of GxE in our simulation.


> **Figure/Table Caption:** ( A ) Data from an experiment measuring allelic effects on longevity in caged flies given one of two diets, ‘control’ and ‘high sugar’. Shown are allelic effect estimates under each diet for a random sample of approximately 12K variants. ( B ) Simulated data where all true allelic effects are exactly 1.4 times larger under a high-sugar diet. The effects are estimated with sampling noise mimicking the Pallares et al. data. ( C ) Allelic effect estimates of variants ascertained as significant and classified as ‘diet-specific’ or ‘shared’ by Pallares et al. ( D ) Simulated effects ascertained as significant and classified using a similar procedure to that applied in ( C ). While the generative mode of GxE we used in our simulations was not considered by Pallares et al., the simulation results (left panels) closely match the patterns observed in their data (right panels) across all effects (top panels) and as reflected via their classification approach (bottom panels).

To recap, we simulated a mode of GxE that is not considered in Pallares et al. (i.e. pervasive amplification) and that is at odds with their conclusions about evidence for a large discrete class of SNPs with diet-specific effects (i.e. cryptic genetic variation). The close match of our simulation to the empirical results of Pallares et al. therefore illustrates that the characterization of GxE via hypothesis testing and classification at each variant independently may lead to erroneous interpretation when applied to empirical complex trait data as well. In Appendix 1, we show that a reanalysis of the Pallares et al. data that is based on estimating the covariance of allelic effects is directly consistent with pervasive amplification as well ( Appendix 1—figure 4 ). In conclusion, the classification of ‘top hits’ alone may not be representative of the extent of GxE nor of the most pervasive modes of GxE.


#### The utility of modeling GxE for complex trait prediction

Modeling context dependency of genetic effects may hold the potential for constructing polygenic scores that are more accurate or improve their portability across contexts ( Patel et al., 2022 ; Miao et al., 2022 ; Turley et al., 2018 ; Spence et al., 2022 ; Wang et al., 2024 ; [AUTHOR et al.], 2025 ). Evidence for the utility of GxE models in polygenic score prediction, however, has been underwhelming and GxE models are still rarely applied ( Zhu et al., 2023 ; Schwaba et al., 2023 ). A key reason behind this apparent discrepancy is the bias-variance trade-off for individual variants discussed above. If context-specific effects are similar—a likely possibility for highly polygenic traits with the majority of heritability owing to small causal effects—then additive models will tend to outperform ( Fisher, 1930 ; Falconer and Mackay, 1996 ; Hill et al., 2008 ; Young, 2019 ). This is because the unbiasedness of GxE estimation does not make up for the cost of additional estimator variance, resulting from sample stratification by context or the addition of explicit interaction terms ( Schwaba et al., 2023 ). We exemplify the relative importance of variance compared to bias in polygenic scoring using simulations. We continue with the generative model of pervasive amplification as an example. Namely, we simulated a GWAS of a continuous trait with independent effects in 2500 variants (50% of variants included in the GWAS). Effects were either the same in two contexts, A and B , or 1.4 times larger in context B . The GWAS is conducted with either a small sample size or a large sample size, conferring low or high statistical power, respectively. We then constructed polygenic scores using 833 variants (corresponding to one-third of the causal variants), which were ascertained as most significantly associated with the trait according to either the additive model (orange and red in Figure 5 ) in or context-specific hypothesis tests (green and blue in Figure 5 ).


> **Figure/Table Caption:** In each simulation, a genome-wide association study (GWAS) is performed on 5000 biallelic variants, half of which have no effect in either context. Of the other half, some percent of the variants (indicated on the x -axis) had effects 1.4× larger in one of contexts and the remaining SNPs had equal effects in both contexts. The broad sense heritability was set to 0.4 in all simulations. The y -axis shows the average, over 11 , 000 simulations, of the out-of-sample Pearson correlation between polygenic score and trait value. ( A ) Results with a GWAS sample size of 1000 individuals. ( B ) Results with a GWAS size of 50 , 000 individuals.

Even in settings with pervasive GxE, additive polygenic scores (red lines in Figure 5 ) outperformed context-specific scores (green lines in Figure 5 ). The advantage of the additive model is manifested in two ways: more accurate estimation, as discussed above, but also better identification of true associations with the trait. We considered the two advantages separately. It is sometimes better to ascertain variants using the lower variance approach and estimate effects using the lower-bias approach. In our simulations, this strategy (orange lines in Figure 5 ) was preferable to using the GxE model for both ascertainment and estimation (green line). It was not preferable to using the additive model (red line) for both approaches, but it was the preferable strategy under a slightly different parametric regime, corresponding to more GxE ( Appendix 1—figure 5 ). Finally, we considered a polygenic GxE approach, as implemented in ‘multivariate adaptive shrinkage’ ( mash ) ( Urbut et al., 2019 ), a method to estimate context-specific effects by leveraging common patterns of effect covariance between contexts observed across the genome. mash models the underlying distribution of effects in all contexts as a mixture of zero-centered multivariate normal distributions with different covariance structures (as well as the null matrix, to induce additional shrinkage). After estimating this distribution via maximum likelihood, mash uses it as a prior to obtain posterior effect estimates for each variant in each context. As a result, posterior effect estimates across contexts regress toward commonly observed patterns of covariance of allelic effects across contexts. In our simulations, in the presence of substantial amplification, the polygenic adaptive shrinkage approach outperformed all other methods as long as the study was adequately powered ( Figure 5B ). This is thanks to the unique ability (compared to the three other approaches) to leverage the sharing of signals across variants, including the extent and nature of context dependency. With low power, however, the additive model performed best ( Figure 5A ). We attribute this to the variance cost associated with the polygenic adaptive shrinkage approach—driven by the estimation of additional parameters for capturing the genome-wide covariance relationships.


### Conclusion

When genetic variants are considered independently, the estimation of their effects in different contexts can be boiled down to a bias-variance trade-off. For complex traits, we show through example that further considering polygenic patterns of GxE can be key for understanding context-dependent genetic architecture and to aid in prediction. The notion that complex trait analyses should combine observations at top associated loci alongside polygenic trends has gained traction with additive models of trait variation; it may be similarly important in our understanding of context dependency.


## Methods


### Expressing the additive estimator as a linear combination of GxE estimators

In this section, we prove the result of Equation 3 , stating that



| β ^ A ∪ B = ω A β ^ A + ω B β ^ B |
| --- |


for some non-negative weights ω A and ω B . To do this, we will need some additional notation. Let g ¯ A denote the average number of effect alleles in individuals in context A , and let g ¯ A ∪ B denote the average effect allele count across all individuals. Similarly, let y ¯ A denote the average trait value in context A , and let y ¯ A ∪ B denote the average trait value across all individuals. As an OLS estimator, the context-specific estimator is defined as



| β ^ A = ∑ i = 1 n ( g i − g ¯ A ) ( y i − y ¯ A ) ∑ i = 1 n ( g i − g ¯ A ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i − ∑ i = 1 n ( g i − g ¯ A ) y ¯ A ∑ i = 1 n ( g i − g ¯ A ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i − y ¯ A ∑ i = 1 n ( g i − g ¯ A ) ∑ i = 1 n ( g i − g ¯ A ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i ∑ i = 1 n ( g i − g ¯ A ) 2 , since ∑ i = 1 n ( g i − g ¯ A ) = 0 . |
| --- |


Similarly, the additive estimator can be written as



| β ^ A ∪ B = ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) ( y i − y ¯ A ∪ B ) ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 (by the same logic as above) = ∑ i = 1 n ( g i − g ¯ A ∪ B ) y i + ∑ i = n + 1 n + m ( g i − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 . |
| --- |


We will show that the weights in Equation 3 depend on the effect allele frequency in the two contexts, f A and f B . We will assume mean-centered traits, such that ∑ i = 1 n y i = 0 and ∑ i = n + 1 n + m y i = 0 . We note that mean-centering is inconsequential for effect estimation. We can then write



| β ^ A ∪ B = ∑ i = 1 n ( g i − g ¯ A ∪ B ) y i + ∑ i = n + 1 n + m ( g i − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A + ( g ¯ A − g ¯ A ∪ B ) ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B + ( g ¯ B − g ¯ A ∪ B ) ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i + ∑ i = 1 n ( g ¯ A − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B ) y i + ∑ i = n + 1 n + m ( g ¯ B − g ¯ A ∪ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i + ( g ¯ A − g ¯ A ∪ B ) ∑ i = 1 n y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B ) y i + ( g ¯ B − g ¯ A ∪ B ) ∑ i = n + 1 n + m y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 (by our assumption of mean centered traits) = ∑ i = 1 n ( g i − g ¯ A ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 ⋅ ∑ i = 1 n ( g i − g ¯ A ) 2 ∑ i = 1 n ( g i − g ¯ A ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B ) y i ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 ⋅ ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ) y i ∑ i = 1 n ( g i − g ¯ A ) 2 ⋅ ∑ i = 1 n ( g i − g ¯ A ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 + ∑ i = n + 1 n + m ( g i − g ¯ B ) y i ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 ⋅ ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 = ∑ i = 1 n ( g i − g ¯ A ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 β ^ A + ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 β ^ B . |
| --- |


Thus, ω A = ∑ i = 1 n ( g i − g ¯ A ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 and ω B = ∑ i = n + 1 n + m ( g i − g ¯ B ) 2 ∑ i = 1 n + m ( g i − g ¯ A ∪ B ) 2 in Equation 3 . We note that the numerator of ω A is n times the sample heterozygosity in context A , and the numerator of ω B is m times the sample heterozygosity in context B . Thus, we have shown that



| ω A ∝ n H A and ω B ∝ m H B , | (7) |
| --- | --- |


where H A and H B are the sample heterozygosities in context A and B , respectively. And, in the special case where f A = f B , because this implies that the sample heterozygosities will be approximately equal across contexts, we have that



| ω A ∝ n H A and ω B ∝ m H B . | (8) |
| --- | --- |



### Linearity of the decision rule

In Equation 5 , under the assumption that V A = V B and H A = H B , the decision boundary is expressed as a linear function of | β A − β B | and V A as



| m 2 n / β A − β B / > V A . |
| --- |


Here, we prove that the linearity of the decision rule holds in the more general case where V A V B = r for some fixed value of r . Equation 5 then follows as a special case of this fact when r = 1 . Starting from Equation 4 , we prefer the GxE estimator to the additive estimator when estimating β A if



| V A < ω A 2 V A + ω B 2 V B + ( ( ω A − 1 ) β A + ω B β B ) 2 ⟺ V A < ω A 2 V A + ω B 2 r V A + ( ( ω A − 1 ) β A + ω B β B ) 2 ⟺ V A − ω A 2 V A − ω B 2 r V A < ( ( ω A − 1 ) β A + ω B β B ) 2 ⟺ ( 1 − ω A 2 − ω B 2 r ) V A < ( ( ω A − 1 ) β A + ω B β B ) 2 ⟺ V A < ( ( ω A − 1 ) β A + ω B β B ) 2 1 − ω A 2 − ω B 2 r (assuming 1 − ω A 2 − ω B 2 r > 0 ) ⟺ V A < / ( ω A − 1 ) β A + ω B β B / 1 − ω A 2 − ω B 2 r (again assuming 1 − ω A 2 − ω B 2 r > 0 ) |
| --- |


If our assumption that 1 − ω A 2 − ω B 2 r > 0 does not hold, we note that the GxE model is always preferable and technically speaking there exists no decision rule between the two models. Now, when heterozygosities (and thus minor allele frequencies) are equal across contexts, then Equation 8 implies ω A + ω B = 1 . Therefore, we may write the decision rule as



| V A < / ( 1 − ω B − 1 ) β A + ω B β B / 1 − ω A 2 − ω B 2 r ⟺ V A < / ω B ( β B − β A ) / 1 − ω A 2 − ω B 2 r ⟺ V A < ω B 1 − ω A 2 − ω B 2 r / β A − β B / (by properties of the absolute value) ⟺ V A < 1 − ω A 1 − ω A 2 − ( 1 − ω A ) 2 r / β A − β B / . |
| --- |


Here, we see that for any fixed r the decision rule is linear with a slope determined by r ( Figure 2 ). Now, in the special case where r = 1 , we have



| V A < 1 − ω A 1 − ω A 2 − ( 1 − ω A ) 2 / β A − β B / ⟺ V A < 1 − ω A 1 − ω A 2 − 1 − ω A 2 + 2 ω A / β A − β B / ⟺ V A < 1 − ω A 2 ω A ( 1 − ω A ) / β A − β B / ⟺ V A < 1 − ω A 2 ω A / β A − β B / |
| --- |


Now, substituting the definitions of ω A and ω B in the case of equal minor allele frequencies given in Equation 8 , we can write



| V A < 1 2 1 − n n + m n n + m / β A − β B / ⟺ V A < 1 2 m n + m n n + m / β A − β B / ⟺ V A < m 2 n / β A − β B / . |
| --- |


This inequality is instead an equality under the conditions stated in Equation 5 . Finally, again using the definition of ω A and ω B given in Equation 8 , we note that our assumption that 1 − ω A 2 − ω B 2 r > 0 will always hold in the case of equal minor allele frequencies and r = 1 , as



| 1 − ω A 2 − ω B 2 r = 1 − n 2 ( n + m ) 2 − m 2 ( n + m ) 2 = ( n + m ) 2 − n 2 − m 2 ( n + m ) 2 = 2 n m ( n + m ) 2 , |
| --- |


which is strictly positive.


### Re-parameterized decision rule in terms of unitless quantities

In Equation 6 , under the assumption that H A = H B , we re-state the decision rule in terms of the signal-to-noise ratio. Here, we prove this result. From Equation 4 , we have that we should select the GxE model to estimate β A if and only if



| V A < ω A 2 V A + ω B 2 V B + ( ( ω A − 1 ) β A + ω B β B ) 2 ⟺ 1 < ω A 2 + ω B 2 V B V A + ( ( ω A − 1 ) β A + ω B β B ) 2 V A ⟺ 1 − ω A 2 < ω B 2 V B V A + ( ( ω A − 1 ) β A + ω B β B ) 2 V A . |
| --- |


Now, because H A = H B , we know by Equation 8 that ω A + ω B = 1 . Then, we may write the decision rule as



| 1 − ω A 2 < ω B 2 V B V A + ( ( 1 − ω B − 1 ) β A + ω B β B ) 2 V A ⟺ 1 − ω A 2 < ω B 2 V B V A + ( ω B ( β B − β A ) ) 2 V A ⟺ 1 − ω A 2 < ω B 2 V B V A + ω B 2 ( β A − β B ) 2 V A ⟺ 1 − ω A 2 ω B 2 < V B V A + ( β A − β B ) 2 V A ⟺ 1 − ω A 2 ( 1 − ω A ) 2 < V B V A + ( β A − β B ) 2 V A ⟺ 1 − ω A 2 ( 1 − ω A ) 2 − V B V A < ( β A − β B ) 2 V A ⟺ ( 1 − ω A ) ( 1 + ω A ) ( 1 − ω A ) 2 − V B V A < ( β A − β B ) 2 V A ⟺ 1 + ω A 1 − ω A − V B V A < ( β A − β B ) 2 V A |
| --- |


as is stated in Equation 6 .


### Simulation of GxDiet effects on longevity in Drosophila

In Figure 4 , we compare the effect estimates of Pallares et al. to ones we got in simulations of pervasive amplification. Here, we detail the simulation approach. We first generated true effects under each diet. For variants j = 1 , … , 50 , 000 , we sampled a true effect under the high-sugar diet ( β h j ) and under the control diet ( β c j ). A random 60% of variants were set to have no effect under either diet, with the effects of the remaining 40% of variants sampled as



| [ β c j β h j ] ∼ N ( [ − 0.125 − 0.15 ] , 0.01 ⋅ [ 1 1.4 1.4 1.96 ] ) . |
| --- |


This corresponds to a systematic amplification of 1.4 × in the high-sugar compared to the control diet. We selected these parameters based on inspection of the resulting distribution of effects and their correspondence to the Pallares et al. data. We then simulated the effect estimation. For each variant, the effect estimate was simulated as normally distributed with mean equal to the true effect and standard deviation equal to a randomly sampled (with replacement) standard error from the effect estimates of Pallares et al. That is, given the simulated values of the true effect estimates β c j and β h j , we simulated effect estimates as



| [ β ^ c j β ^ h j ] ∼ N ( [ β c j β h j ] , [ s ^ c k 2 0 0 s ^ h k 2 ] ) , |
| --- |


where k represents the index of a randomly selected variant from the empirical data of Pallares et al. and s ^ c k and s ^ h k are the corresponding estimated standard errors for the effect estimates in the control and high-sugar groups, respectively. This process yielded vectors of estimated effects in the high-sugar group and control group, β ^ h and β ^ c , respectively, and vectors of estimated standard errors in the high-sugar group and control group, s ^ h and s ^ c , respectively. We then performed a Z-test for each variant under each diet, yielding two vectors of p-values, p h and p c , corresponding to the high-sugar and control diets, respectively. Using these p-values, we followed a similar approach to Pallares et al. to classify the variants ( Figure 4D ). First, as in Pallares et al., we computed q-values separately for each diet ( Storey, 2003 ), yielding q h and q c , corresponding to the q-values of non-zero effects in the high-sugar and control diets, respectively. Then, we employed the following classification scheme for each variant j = 1 , … , 50 , 000 :

If q h j ≥ 0.01 and q c j ≥ 0.01 → classify as no effect .

If q h j < 0.01 and p c j ≥ 0.1 → classify as high-sugar-specific effect .

If q c j < 0.01 and p h j ≥ 0.1 → classify as control-specific effect .

If q c j < 0.01 and q h j < 0.01 → classify as shared effect .

We note that p-value and q-value cutoffs used are nominally different than those used in the Pallares et al. study.


### Polygenic score simulations

In Figure 5 , we show the results of multiple simulations where we compute polygenic scores in each of two contexts under amplification. Here, we detail the generation of data in the simulations and the methods for constructing polygenic scores. As in Results and discussion, we assumed that we have n + m observations of a continuous trait, where the first n individuals are observed in context A and the final m are observed in context B . For convenience, in this case we assumed n = m . Now, for variants j = 1 , … , p we generated true effects in contexts A and B independently from the mixture model



| [ β A j β B j ] ∼ π 0 δ 0 + ( 1 − π 0 ) ( α N ( [ 0 0 ] , [ 1 1 1 1 ] ) ) + ( 1 − α ) N ( [ 0 0 ] , [ 3 2 1 1 2 3 ] ) ) , |
| --- |


where π 0 (which we set to 0.5 ) represents the proportion of SNPs with null effects in both contexts, α represents the proportion of non-null SNPs which have exactly equal effects in both contexts, and 1 − α is the proportion of non-null SNPs which are generated as perfectly correlated but with 1.5 × the standard deviation in context A . Let β → A and β → B represent the resulting p -vectors of true effects for contexts A and B , respectively. Next, we generated genotype counts for each of the n + m individuals at all p variants. Specifically, we independently generated genotypes as



| f j ∼ 1 2 B e t a ( s 1 , s 2 ) for j = 1 , … , p |
| --- |




| g i j ∼ B i n o m i a l ( 2 , f j ) for i = 1 , … , n + m , |
| --- |


where f j is the minor allele frequency at variant j in the population, s 1 and s 2 are parameters controlling the distribution of minor allele frequencies in the population, and g i j is the observed genotype for individual i at variant j . Here, we set s 1 = 1 and s 2 = 5 . Let G A and G B represent the generated n × p matrices of genotypes in contexts A and B , respectively. Finally, we generated the observed continuous traits for context A ( y → A ) and context B ( y → B ) as y → A ∼ N ( G A β → A , σ A 2 I n ) y → B ∼ N ( G B β → B , σ B 2 I m ) ,



| y → A ∼ N ( G A β → A , σ A 2 I n ) y → B ∼ N ( G B β → B , σ B 2 I m ) , |
| --- |


where σ A 2 and σ B 2 are the observation variances in contexts A and B , respectively, and I w is the w × w identity matrix. In our simulations, we set σ A 2 and σ B 2 such that the narrow sense heritability is 40% in each context. So that we may later test the accuracy of our polygenic scores, we generated both a training set (consisting of n individuals in each context, where n =1000 in the low power simulation and n = 50 , 000 in the high power simulation) for effect estimation and a test set (consisting of 3000 individuals in each context) using the above distributions. Figure 5 compares four distinct approaches for constructing polygenic scores, derived from three allelic effect estimation approaches: additive estimation with shrinkage, GxE estimation with shrinkage, and mash . First, the additive and GxE estimates are derived independently for each variant as described in Results and discussion. Let β ^ A and β ^ B be the p -vectors of GxE estimates of effects in context A and B , respectively. Similarly, let s ^ A and s ^ B be the p -vectors of the standard errors of GxE estimates of effects in context A and B , respectively. Finally, let β ^ A ∪ B be the p -vector of estimated effects from the additive model and s ^ A ∪ B be the p -vector of standard errors of estimated effects from the additive model. Using the GxE estimates, we also constructed estimates of the effects in each context using mash . Specifically, we ran mash on the n × 2 matrices [ β ^ A β ^ B ] (of effects) and [ s ^ A s ^ B ] (of standard errors). mash then yields p ( β → A | β ^ A , s ^ A ) and p ( β → B | β ^ B , s ^ B ) , the posterior distributions of the effects in contexts A and B , respectively. To construct each polygenic score, we made two choices. First, a choice between the three sets of p-values (or pseudo p-values, see below) for thresholding—we include the 833 (corresponding to one-third of the causal variants) most significant variants in the polygenic score. The second choice was between the three sets of effect estimates to be used as weights in the polygenic score ( Figure 5 ). For instance, when the GxE model was used for ascertainment, we selected the set of variants Ω A ⊂ { 1 , … , p } consisting of the variants with the 833 smallest p-values and Ω B ⊂ { 1 , … , p } consisting of the variants with the 833 smallest p-values (derived from β ^ B and s ^ B ). Then, we predicted trait values (out of sample) by multiplying the effect estimates of our chosen ‘estimation method’ (for mash we use the posterior mean) by the effect allele count at each of the selected variants for the individual in question.


## Appendix 1


### 1 Validating and applying the decision rule to real data

To validate the decision rule of Equations 4–6 of the main text, we considered the example of sex as a context for physiological traits using UK Biobank data ( Bycroft et al., 2018 ). For each of 27 physiological quantitative traits, we first split the sample by sex chromosome karyotypes into XX individuals (females) and XY individuals (males). For each sex, we randomly split the sample into a training set with 80% of the individuals and a test set with 20% of the individuals. We estimated within-sex GWAS in the training and test sets separately. We denote by β ^ Z i ( t ) the marginal effect estimate of the i th SNP in sex Z in set t , and by s ^ Z i ( t ) the corresponding standard error. We denote by β ^ M ∪ F i ( t r a i n ) the estimated effect of the i th SNP in the union of training sets (with both sexes included). In our validation procedure, we treated β ^ M i ( t e s t ) as the ‘ground-truth’, i.e., as the true effect. While β ^ M i ( t e s t ) is of course a very noisy estimate of β M i , it is an unbiased estimate, so we expect that estimates that are closer to β ^ M i ( t e s t ) in the aggregate will also be closer to β M i . Using this assumption, we define two empirical quantities,



| e r r o r ( β ^ M i ( t r a i n ) ) = ( β ^ M i ( t r a i n ) − β ^ M i ( t e s t ) ) 2 |
| --- |




| e r r o r ( β ^ M ∪ F i ( t r a i n ) ) = ( β ^ M ∪ F i ( t r a i n ) − β ^ M i ( t e s t ) ) 2 . |
| --- |


Given V M i and | β M i − β F i | , Equation 4 allows us to calculate the expected difference between e r r o r ( β ^ M i ( t r a i n ) ) and e r r o r ( β ^ M ∪ F i ( t r a i n ) ) . However, we do not observe V M i or | β M i − β F i | . Instead, we estimated these quantities and examined the agreement of the estimates in the two sets. We estimated V M i as s ^ M i ( t r a i n ) . Estimating | β M i − β F i | is more difficult, as the intuitive | β ^ M i ( t r a i n ) − β ^ F i ( t r a i n ) | is an upwardly biased estimator. Instead, we used an empirical shrinkage estimator ( ash Stephens, 2017 ) to estimate | β M i − β F i | . In essence, ash takes in a vector of effect estimates β ^ and a vector of corresponding standard errors s ^ , estimates a prior distribution of the true effects , and then uses this prior to obtain a posterior distribution of true effects. Specifically, for a large random sample of sites, i = 1 , … , p , we ran ash on the vectors



| β ^ = ( β ^ M 1 ( t r a i n ) − β ^ F 1 ( t r a i n ) , … , β ^ M p ( t r a i n ) − β ^ F p ( t r a i n ) ) s ^ = ( ( s ^ M 1 ( t r a i n ) ) 2 + ( s ^ F 1 ( t r a i n ) ) 2 , . . . , ( s ^ M p ( t r a i n ) ) 2 + ( s ^ F p ( t r a i n ) ) 2 ) . |
| --- |


and took the absolute value of ash ’s output posterior mean estimates of β M i − β F i as our estimate of | β M i − β F i | for each site. With our estimates of | β M i − β F i | and V M i in hand, we calculated the expected difference in squared errors using Equation 4 ( x -axis in Figure 3A ) and compared it with the actual difference between e r r o r ( β ^ M i ( t r a i n ) ) and e r r o r ( β ^ M ∪ F i ( t r a i n ) ) ( Figure 1 ). For Figure 3A and B , we used the same procedure as above to estimate the x and y axes, except we did not employ any data splitting.


### 2 Equivalence of regression coefficient estimates for explicit interaction term and stratified model

In the main text, we discuss the estimation of context-dependent effects through the estimation of two effects in subsamples stratified by context. The generative model defined in Equation 1 is



| y i ∼ { N ( α A + β A g i , σ A 2 ) if i ∈ { 1 , … , n } N ( α B + β B g i , σ B 2 ) if i ∈ { n + 1 , … , n + m } , | (S1) |
| --- | --- |


where β A and β B are fixed, context-specific effects of a reference allele at a biallelic, autosomal variant i , g i ∈ { 0 , 1 , 2 } is the observed reference allele count. α A and α B are the context-specific intercepts, corresponding to the mean trait value for individuals with zero reference alleles in context A and B , respectively. σ A 2 and σ B 2 are context-specific observation variances. Another common way to define a generative GxE model is with a linear genotype-by-context interaction term, namely,



| y i ∼ N ( α + β G g i + β E e i + β G x E g i e i , σ 2 ) independently for i = 1 , … , n + m , | (S2) |
| --- | --- |


where α is the mean trait value for individuals with zero reference alleles in context A , β G is the genetic effect, β E is the contextual effect, β G x E in the genotype-context interaction term, e i is the contextual covariate for individual i , defined to be 0 if the individual is in context A and 1 if the individual is in context B , and σ 2 is the homoskedastic noise term. Here, we show that least squares estimation of the two models above context-specific effect estimates. The OLS estimate of the intercept and context-specific allelic effects under the model described in Equation S1 are



| α ^ A , β ^ A = a r g m i n α A , β A ∑ i = 1 n ( y i − ( α A + β A g i ) ) 2 | (S3) |
| --- | --- |




| α ^ B , β ^ B = a r g m i n α B , β B ∑ i = n + 1 n + m ( y i − ( α B + β B g i ) ) 2 . | (S4) |
| --- | --- |


The OLS estimates under the model described in Equation S2 are



| α ^ , β ^ G , β ^ E , β ^ G x E = a r g m i n α , β G , β E , β G x E ∑ i = 1 n + m ( y i − ( α + β G g i + β E e i + β G x E g i e i ) ) 2 . | (S5) |
| --- | --- |


Since e i = 1 if individual i is in context B and 0 otherwise, we can re-write Equation S5 as



| . α ^ , β ^ G , β ^ E , β ^ G x E = a r g m i n α , β G , β E , β G x E ( ∑ i = 1 n ( y i − ( α + β G g i ) ) 2 + ∑ i = n + 1 n + m ( y i − ( α + β G g i + β E + β G x E g i ) ) 2 ) = a r g m i n α , β G , β E , β G x E ( ∑ i = 1 n ( y i − ( α + β G g i ) ) 2 + ∑ i = n + 1 n + m ( y i − ( ( α + β E ) + ( β G + β G x E ) g i ) ) 2 ) . |
| --- |


By Equation S3 we have that ∑ i = 1 n ( y i − ( α + β G g i ) ) 2 is minimized by setting α = α ^ A and β G = β ^ A . In turn, by Equation S4 we have that ∑ i = n + 1 n + m ( y i − ( ( α + β E ) + ( β G + β G x E ) g i ) ) 2 is minimized by setting α + β E = α ^ B and setting β G + β G x E = β ^ B . Thus, both terms are simultaneously minimized by setting



| α = α ^ A |
| --- |




| β G = β ^ A |
| --- |




| β E = α ^ B − α ^ A |
| --- |




| β G x E = β ^ B − β ^ A . |
| --- |


Then, under the explicit interaction model, for an individual in context A the estimated intercept is α ^ A and the estimated genetic effect is β ^ A . And, for an individual in context B , the estimated intercept is α ^ A + α ^ B − α ^ A = α ^ B and the estimated genetic effect is β ^ A + β ^ B − β ^ A = β ^ B . Thus, conditional on the context, both the explicit interaction model and the stratified model provide the same effect and intercept estimates. We note that there is still an important difference between the stratified and explicit interaction models, as the stratified model allows for heteroskedasticity between contexts where the explicit interaction model does not. We also note that the proof of equivalence relies on the context variable being binary.


### 3 Continuous context variable

Here, we extend our analysis of single-site estimation in a binary context to the case of a continuous context variable. Specifically, for individuals indexed by i = 1 , … , n , we consider the generative model



| y i ∼ N ( β 0 + β G g i + β E e i + β G × E g i e i , σ 2 ) , | (S6) |
| --- | --- |


where y i ∈ R is the continuous trait value for individual i , g i ∈ { 0 , 1 , 2 } is the number of reference alleles carried by a diploid individual i at a focal biallelic variant of interest, e i ∈ R is the continuous context for individual i , β 0 is the the mean trait value for individuals with the context variable value of zero and zero reference alleles, β G is the main (additive) allelic effect, β E is the effect of the context, β G × E is the main interaction effect, and σ 2 is the residual variance. For simplicity, we will assume β 0 = 0 . For a binary context, we considered the difference in MSE of the ‘additive model’ and ‘GxE model’ in estimating the context-specific genetic effect. Analogously, for a continuous context we will consider the difference in MSE in estimating the total genetic effect conditional on a particular value of the context variable. To perform this analysis, we will consider the estimation of two models. The first model, which we will call the ‘GxE’ model, is described in Equation S6 above (where we omit the intercept because we assume it is 0). For convenience, we will use the following matrix notation:



| y = [ y 1 ⋮ y n ] , X = [ g 1 e 1 g 1 e 1 ⋮ ⋮ ⋮ g n e n g n e n ] , β = [ β G β E β G × E ] . |
| --- |


Then, we consider the standard least squares estimate of β ^ = ( X T X ) − 1 X T y , for which



| β ^ ∼ N ( β , σ 2 ( X T X ) − 1 ) . | (S7) |
| --- | --- |


We will assume that the vector of genotypes g → and the vector of context covariates e → are orthogonal in our sample and are both mean centered. (In the following section, we discuss the case of gene-context correlation, where these assumptions are not met.) Then, the matrix X T X will be approximately diagonal. Under this approximation, we can write Equation S7 as



| β ^ ∼ N ( β , Σ ) , |
| --- |




| Σ ≈ σ 2 diag ( 1 ∑ i = 1 n g i 2 , 1 ∑ i = 1 n e i 2 , 1 ∑ i = 1 n g i 2 e i 2 ) . | (S8) |
| --- | --- |


Now, we are interested in the error of the GxE model in estimating the genetic effect conditional on a particular value of the context e . By Equation S6 , we define the true genetic effect conditional on a particular value of the context e as β G + β G × E e . Thus, to evaluate the error of the GxE model, the conditional expected error is



| E [ ( ( β ^ G + β ^ G × E e ) − ( β G + β G × E e ) ) 2 / e ] . | (S9) |
| --- | --- |


By the definition of conditional variance, we can write Equation S9 as



| V a r [ ( β G + β G × E e ) − ( β ^ G + β ^ G × E e ) / e ] + ( E [ ( β G + β G × E e ) − ( β ^ G + β ^ G × E e ) / e ] ) 2 = V a r [ ( β G + β G × E e ) − ( β ^ G + β ^ G × E e ) / e ] (since β ^ G and β ^ G × E are unbiased estimates) = V a r [ β ^ G + β ^ G × E e / e ] (since β G and β G × E are fixed parameters) |
| --- |




| ≈ σ 2 ∑ i = 1 n g i 2 + σ 2 ∑ i = 1 n g i 2 e i 2 e 2 |
| --- |


We will also consider the estimation error associated with the ‘additive model’, which in this case estimates the model described in Equation S6 assuming that β G × E = 0 . In effect, this assumes that the genetic effect is equal across all values of the context. Because X T X is approximately diagonal matrix, removing the G × E covariate and regression coefficient has a negligible effect on both the least squares estimates of β G and its sampling distribution. Thus, we can approximate the error of the additive model by calculating the conditional expectation



| E [ ( ( β G + β G × E e ) − β ^ G ) 2 / e ] | (S10) |
| --- | --- |


under the model in Equation S6 . Again, by the definition of the conditional expectation, we can write Equation S10 as



| V a r [ ( β G + β G × E e ) − β ^ G / e ] + ( E [ ( β G + β G × E e ) − β ^ G / e ] ) 2 = σ 2 ∑ i = 1 n g i 2 + β G × E 2 e 2 . |
| --- |


Thus, conditional on a particular value of e , we prefer the G × E estimator for estimating the genetic effect if and only if



| σ 2 ∑ i = 1 n g i 2 + σ 2 ∑ i = 1 n g i 2 e i 2 e 2 < σ 2 ∑ i = 1 n g i 2 + β G × E 2 e 2 | (S11) |
| --- | --- |




| ⟺ σ 2 ∑ i = 1 n g i 2 e i 2 e 2 − β G × E 2 e 2 < 0 | (S12) |
| --- | --- |




| . ⟺ σ 2 ∑ i = 1 n g i 2 e i 2 < β G × E 2 | (S13) |
| --- | --- |


This decision rule has a very intuitive interpretation: the G × E model is preferable when the estimation variance of the interaction term is smaller than the squared interaction effect size. While the exact difference in MSE between the additive and G × E models depends on the value of the context variable (see Equation S11 ), the decision rule ( Equation S13 ) does not.


### 4 Gene-context correlation

The simple decision rule given in Equation S13 was derived using the assumption that the observed genotype vector and the observed context vector were orthogonal. In statistical terms, one may expect this condition to approximately hold when sampling from a population where r ( G , E ) , the correlation between genotypes and the context, is 0. In general, this assumption may not be reasonable. When this assumption is violated, the design matrix X will no longer form a diagonal matrix when left-multiplied by its transpose. This results in both (a) larger standard errors for each of the marginal coefficients and (b) non-zero sampling covariance between the coefficients. In addition, | r ( G , E ) | > 0 may result in omitted variable bias in the additive model. As a result, the decision rule of Equation S13 will not hold exactly under conditions of | r ( G , E ) | > 0 , and in fact may be far from correct when | r ( G , E ) | is large. In general, creating a closed-form decision rule to choose between the GxE and additive models in this scenario is not possible. However, in this section we use a simulation study to gain intuition about the change in bias-variance trade-off in the presence of gene-context correlation. In our simulations, for a group of n individuals, we generate genotypes as



| g 1 , … , g n ∼ i i d B i n o m i a l ( 2 , p ) . |
| --- |


Then, for some constant c , we generate context covariates as



| e i ∼ N ( c ⋅ g i , σ E 2 ) |
| --- |


independently for i = 1 , … , n . Finally, we generate trait values y 1 , … , y n using Equation S6 for particular values of the remaining parameters. To explore how the bias-variance trade-off changes for different values of r ( G , E ) , we ran a set of simulations with different values of c in the range of − 3.5 to 3.5 . For each of these simulations, we generated a dataset of n = 250 individuals with σ E 2 = 1 , p = 0.1 , β 0 = 0 , β G = 0.25 , β E = 0 , β G × E = − .125 , and σ y 2 = 7 . The results of the simulation are shown in Appendix 1—figure 6 . Non-zero r ( G , E ) had a number of consequences. First, as the magnitude of r ( G , E ) increases, the magnitude of the bias of the genetic effect estimate of the additive model also increases ( Appendix 1—figure 6A ). In our simulation, we set the genetic effect and the interaction effect to have opposite signs. When r ( G , E ) is positive, it pulls the genetic effect estimate toward the interaction effect. In contrast, when r ( G , E ) is negative, it pulls the genetic effect estimate away from the interaction effect. Since the G × E model includes all causal variables, it is unbiased. Second, as the magnitude of r ( G , E ) increases, the variance of the genetic effect estimates of both the additive and G × E models increase ( Appendix 1—figure 6B ). This is because when variables in a regression are (positively or negatively) correlated, it is more difficult to distinguish between their effects. The G × E model appears to be affected more strongly here, which likely results from the inclusion of an additional interaction term that is highly correlated with both the genotype covariate and the context covariate. Third, the interaction term in the G × E model remains unbiased under r ( G , E ) , and increases in variance with larger magnitude of r ( G , E ) ( Appendix 1—figure 6C and D ).


### 5 Classification-based inference in Pallares et al., 2022

In the main text, we discuss the characterization of GxE by Pallares et al., based on significance testing under each of the diets. The authors classified variants according to whether or not their associations with survivorship were significant under each diet as follows:

Significant under neither diet → classify as no effect .

Significant when fed the high-sugar diet, but not when fed the control diet → classify as high-sugar-specific effect .

Significant when fed the control diet, but not when fed the high-sugar diet → classify as control-specific effect .

Significant under both diets → classify as shared effect .

Approximately 31% were high-sugar specific, while the remaining 69% of the variants were shared. Fewer than 1% were labeled as having control-specific effects. The authors concluded that high-sugar-specific effects on longevity are pervasive, compatible with the hypothesis of widespread cryptic genetic variation for longevity. This ‘top hits’ approach places an emphasis on the context(s) in which trait associations are statistically significant, rather than on estimating how the context-specific allelic effects covary. In addition, this particular classification system also does not cover all possible ways in which context-specific effects may differ. A key example is the case where true effects are concordant in sign but differ in magnitude. The strong positive covariance of estimated effects observed genome-wide ( Figure 4A ) suggests this case merits consideration. Such variants may fall into each of the existing categories, depending on the magnitude of effects and statistical power in each of the contexts. Three of the four possible classifications are clearly wrong, but what about the ‘shared’ category? The class ‘shared’ may be interpreted as suggesting lack of context dependency (Figure 1C in Pallares et al., 2023 ). However, it will tend to include variants having strong effects under both diets, regardless of whether or not the diet-specific effects are similar. As Pallares et al. also note, there are marked differences in the magnitude of diet-specific estimated effects of variants in the ‘shared’ category. Among the approximately 1500 variants labeled as shared, the estimated effect under the high-sugar diet is on average about 1.3 × that of the estimated effect in the control diet. Notably, the classification as diet-specific does not imply that a variant has an unusually large effect under this diet. On average, variants classified as shared actually have a slightly larger estimated effect under the high-sugar diet than variants classified as high-sugar specific (t-test p= 1.6 × 10 − 5 ). Thus, instead of suggesting little-to-no effect under the control diet and a large effect under the high-sugar diet (as predicted by the hypothesis that cryptic genetic variation is pervasive), the classification as high-sugar specific may commonly just point us to intermediate size effects—large enough to be significant in the systematically larger effects context (where power is higher) yet too small to be significant in the systematically smaller effects context (where power is lower).


### 6 Re-analysis of GxE in the Pallares et al. experiment

In the main text, we show that the classification of significantly associated variants in Pallares et al. is consistent with pervasive amplification, despite the fact that this mode of covariance was not one of the generative modes considered by the authors. Here, we re-estimate the modes of covariance of genetic effects under the two diets, using an approach adapted from the one we have previously used ( Zhu et al., 2023 ). Specifically, we used the framework of ‘multivariate adaptive shrinkage’ ( mash ) to model the covariance of effects between the high-sugar and control diets across all variants. We fit a multivariate normal mixture model to the summary statistics of Pallares et al. ( Urbut et al., 2019 ). In short, mash takes in a set of multidimensional effect estimates and standard errors and estimates the true underlying distribution of effects as a mixture of zero-centered multivariate normal distributions and a point mass at 0. Each mixture component in the model must be pre-specified before the fitting procedure. Following ( Zhu et al., 2023 ), we pre-specified a dense grid of covariance matrices to be input to mash. In particular, each covariance matrix is of the form



| [ σ c 2 ρ σ h s 2 σ c 2 ρ σ h s 2 σ c 2 σ h s 2 ] , |
| --- |


where σ c 2 is the variance of the true effects in the control group, σ h s 2 is the variance of the true effects in the high-sugar group, and ρ is the correlation between the effects in the high-sugar and control groups. To specify the set of covariance matrices, we formed a grid encompassing possible values of the correlation of allelic effects across diets and ratio of variances under each of the diets. Specifically, we varied ρ in the set of values ( − 1 , − 3 4 , − 1 2 , − 1 4 , 0 , 1 4 , 1 2 , 3 4 , 1 ) , and we varied the ratio of the variances, σ c 2 σ h s 2 on a logarithmic scale in the range 0.5 and 1.5. Taking the Cartesian product of these sets yielded a grid of covariance matrices. Because the number of pre-specified covariance matrices was large, and to avoid overfitting, we used a forward stepwise selection procedure ( Hastie et al., 2009 ). We first started with a model with only the null covariance matrix (i.e. no effect under either diet), and then added one covariance matrix to the mixture in a greedy manner in each step, by searching over the space of all covariance matrices for a matrix that maximally improves the likelihood of the mixture model. In each step, we either decide to include the new covariance matrix in the model and move to the next step, or instead stop the procedure and not include the new matrix, if the improvement in likelihood compared to the previous step was below a pre-specified threshold. This threshold was determined by conducting a level α = 0.05 likelihood-ratio test. To mitigate possible linkage disequilibrium among the input SNPs, we performed the procedure described above on a subset roughly 12K out of the roughly 270K variants in the data. These SNPs each came as a random sample from 12K roughly evenly spaced chromosomal blocks (in terms of physical distance). Based on the output of this procedure—the mixture weights in the model ultimately chosen—92% of variants have non-zero effects under both diets but larger effects under the high-sugar diet ( Figure 4 ). This suggests that instead of affecting just a small subset of variants, a high-sugar diet amplifies the effects of the vast majority of variants on lifespan. Moreover, mash assigned zero weight to covariance matrices where an effect is non-zero in one context but zero in another.


#### Appendix 1—figure 1. Out-of-sample validation of decision rule for sex-stratified genome-wide association studies (GWAS) for 27 complex traits.


> **Figure/Table Caption:** For each trait, we use the procedure specified in the section Validating and applying the decision rule to real data. The x -axis shows the expected mean squared error (MSE) advantage of the additive estimator in predicting the male effect based on the decision rule, where the y -axis shows the actual MSE advantage of the additive model in predicting the male effect calculated using an independent sample. Values on the x -axis are grouped into nine evenly spaced bins, and the y -axis shows bin averages (with error bars indicating 1 standard deviation, where the sample size is equal to the number of SNPs falling into each bin). For ease of viewing, data above the 99th percentile and below the 1st percentile on the x -axis are removed.


#### Appendix 1—figure 2. Bias-variance trade-off at random variants in a sex-stratified genome-wide association studies (GWAS).


> **Figure/Table Caption:** This figure extends Figure 3A of the main text to all physiological traits analyzed. The x -axis shows the estimated absolute difference between the effect of variants in males and females. The y -axis shows the measured standard error for each variant in males, the focal context here. The dashed line shows the decision boundary for effect estimation in males. The difference in mean squared error (MSE) between estimation methods increases linearly with distance from the dashed line, as in Figure 2 . If a variant falls above (below) the line, the additive (gene-by-environment interaction [GxE]) estimator has a lower MSE.


#### Appendix 1—figure 3. Bias-variance trade-off at genome-wide significant variants (p-value < 5 × 10 − 8 in males) in a sex-stratified genome-wide association studies (GWAS).


> **Figure/Table Caption:** This figure extends Figure 3B of the main text to all physiological traits analyzed. The x -axis shows the estimated absolute difference between the effect of variants in males and females. The y -axis shows the measured standard error for each variant in males, the focal context here. The dashed line shows the decision boundary for effect estimation in females. The difference in mean squared error (MSE) between estimation methods increases linearly with distance from the dashed line, as in Figure 2 . If a variant falls above (below) the line, the additive (gene-by-environment interaction [GxE]) estimator has a lower MSE.


#### Appendix 1—figure 4. Estimated mixture weights on covariance of true effects in Pallares et al.


> **Figure/Table Caption:** The x -axis shows (symmetric) variance-covariance matrices for true effects in the high-sugar and control diets. The variance-covariance matrices displayed are the only matrices to which mash assigned non-zero weight (from a much larger set of possible covariance matrices, following a variable selection procedure). Variance-covariance matrices are scaled by a constant for each of interpretability. Abbreviations: C–control diet; HS–high-sugar diet.


#### Appendix 1—figure 5. Polygenic score performance for context-aware models with greater amplification than in the main text.


> **Figure/Table Caption:** This figure uses the same simulation parameters as Figure 4 of the main text, except that variant effects are amplified 1.5 × instead of 1.4 × . In each simulation, a genome-wide association study (GWAS) is performed on 5000 biallelic variants, half of which have no effect in either context. Of the other half, some percent of the variants (indicated on the x -axis) had effects 1.5 × larger in one of contexts and the remaining SNPs had equal effects in both contexts. The broad sense heritability was set to 0.4 in all simulations. The y -axis shows the average, over 1000 simulations, of the out-of-sample Pearson correlation between polygenic score and trait value. ( A ) Results with a GWAS sample size of 1000 individuals. ( B ) Results with a GWAS size of 50 , 000 individuals. We note that unlike in Figure 5 , for amplification percentages greater than or equal to 75%, the strategy using ascertainment based on the additive model with gene-by-environment interactions (GxE) effect estimation (orange) outperforms the strategy of using the additive model for both tasks (red).


#### Appendix 1—figure 6. Model performance under correlation between genotype and context.


> **Figure/Table Caption:** ( A ) Bias of genetic effect estimate across different values of correlation. ( B ) Variance of genetic effect estimate across different values of correlation. ( C ) Bias of term estimating the interaction between genotype and context in an interaction model. ( D ) Variance of term estimating the interaction between genotype and context in an interaction model.


## Contributor Information

Arbel [AUTHOR], Email: [EMAIL_REDACTED].

George H Perry, Pennsylvania State University, United States.

George H Perry, Pennsylvania State University, United States.


## Additional information


## Additional files


## Data availability

All data used in this work was available via previously published studies.

The following previously published datasets were used:

Zhu C, Ming MJ, Cole JM, Edge MD, Kirkpatrick M, [AUTHOR] A. 2023. Additive summary statistics. Zenodo.

Pallares LF, Lea AJ, Han C, Filippova EV, Andolfatto P, Ayroles JF. 2022. Dietary stress remodels the genetic architecture of lifespan variation in outbred Drosophila. NCBI BioProject. PRJNA725602

Zhu C, Ming MJ, Cole JM, Edge MD, Kirkpatrick M, [AUTHOR] A. 2022. Sex-specific summary statistics. Zenodo.