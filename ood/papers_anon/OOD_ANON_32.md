# De-Identified Manuscript `OOD_ANON_32`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Climate change is altering the timing of species’ life-cycle events (i.e., phenology), but the rates of phenological shifts vary across taxa. These mismatches in phenological response may disrupt interactions between interdependent species, such as plants and their pollinators, which may lead to reduced plant reproduction via pollen limitation and thus contribute to secondary extinction risks for plants. However, secondary extinction risk is rarely assessed under future climate-change scenarios. Here, we used ca. 15,000 crowdsourced specimen records of Viola species and their solitary bee pollinators, spanning 120 y across the eastern United States, and integrated climate data, phenological information, and species distribution models to quantify the risk of secondary plant extinction associated with phenological mismatch with their bee pollinators. We further examined geographical patterns in secondary extinction risk for plants and explored how their interactions between plants and generalist versus specialist pollinators influence such risk. Secondary local extinction risk of Viola spp. increases with latitude, indicating that future climate change will pose a greater threat to plant–bee pollinator networks at northern latitudes. Additionally, the sensitivity of secondary local extinction risk to phenological mismatch with both generalist and specialist bee pollinators varies by latitude, with specialist bees showing a sharper decline at higher latitudes. Our findings demonstrate that existing conservation priorities based solely on primary extinction risk directly caused by climate change may be insufficient to support self-sustaining populations of plants. Thus, incorporating secondary extinction risk resulting from ecological mismatches between plants and pollinators into future global conservation frameworks should be carefully considered.

Phenology—the timing of species’ life-cycles—plays a critical role in the survival and reproductive success of species ( 1 , 2 ). In recent decades, it has become increasingly clear that anthropogenic climate change has driven significant shifts in the phenology of many organisms in all environments worldwide. Global meta-analyses ( 3 , 4 ) and regional case studies ( 5 , 6 ) consistently have demonstrated that numerous species are advancing their phenological activities (e.g., plant flowering, bird migration) by several days to weeks, largely in response to rising temperatures. However, species are rarely isolated; their survival and reproduction depend on interactions with other organisms including mutualists, competitors, and predators. Variation in the direction and magnitude of phenological shifts across taxa has raised concerns that ecological interactions are becoming increasingly asynchronous, leading to “phenological mismatches” ( 2 , 7 , 8 ). For example, the timing and fidelity of interactions between plants and pollinators may become destabilized, such as when bees emerge before flowers bloom, resulting in a mismatch between pollinator availability and floral resources ( 9 – 11 ).

Phenological mismatch remains poorly understood even though it has been widely hypothesized because most studies of this phenomenon have been done only on small temporal, spatial, and taxonomic scales ( 12 – 14 ). The lack of long-term, multispecies datasets across broad spatial extents has limited our ability to fully explore and predict phenological mismatches at larger spatiotemporal scales. Such small-scale studies also have further hindered our understanding of the consequences of asynchronous phenological shifts between species and their downstream influences on species fitness and population dynamics ( 2 , 15 ), both of which are crucial for assessing the long-term implications of biodiversity loss, especially as the climate continues to change rapidly.

These issues are pressing for many North American plants, which have experienced large-scale phenological shifts in recent decades ( 5 , 16 , 17 ). In particular, findings that pollinator occurrences are diverging from plant flowering times in response to climatic changes have raised concerns that elevated extinction risk of plants may result, at least in part, from disruptions in pollination services ( 18 – 20 ). However, existing studies have mostly focused on “primary” extinction risk directly caused by climate change ( 5 , 20 , 21 ). The “secondary” extinction risk associated with pollination disruptions—and phenological mismatch more generally—has seldom been assessed quantitatively, and the geographic pattern of such risk also is poorly understood.

To estimate the secondary extinction risk of plants resulting from phenological mismatches with their pollinators, we integrate three essential components ( Fig. 1 ): assessments of the influence of climate change on plant and pollinator phenology (i.e., we construct a phenology–climate relationship); joint evaluation of phenological mismatches between interacting species (i.e., we calculate the number of nonoverlapping days between the flowering period of plants and the activity period of their pollinators); and incorporation of phenological mismatch into species distribution models (SDMs). SDMs are tools that are commonly used for estimating probability of occurrence of one or more species (and by inference, their fitness) as a function of environmental variables ( 22 , 23 ). Our analytical approach adjusts the probability of occurrence of a plant species in a favorable habitat by incorporating the temporal difference between flowering time and pollinator occurrence time. As phenological mismatch increases, the final probability of occurrence of plants decreases proportionally, thereby raising the extinction risk for the plant ( Fig. 2 A ).


## Fig. 1.


> **Figure/Table Caption:** Conceptual figure linking species’ phenological response, phenological mismatch, and fitness. The diagram illustrates the interconnectedness of these three components in shaping secondary extinction risk. Species’ phenological response, represented by the green block, refers to how species’ phenological events (e.g., flowering, pollination) shift in response to climate change. Variation in the direction and magnitude of these phenological shifts leads to asynchronous ecological interactions between plants and their pollinator bees, known as phenological mismatch, depicted by the orange block. SDMs, represented by the light purple block, estimate the probability of occurrence of plants in a given environment. This probability is adjusted by the amount of phenological mismatch (i.e., the difference in nonoverlapping days between the plant flowering duration and bee occurrence duration), ultimately estimating the secondary extinction risk. The intersection of all three components represents the potential for secondary extinction, highlighting the cascading effects of ecological disruption in pollination services on plant survival under changing climatic conditions.


## Fig. 2.


> **Figure/Table Caption:** Conceptual diagram showing hypothesized effects of the impacts of phenological mismatch between plants and pollinator bees on plants’ secondary local extinction risk. Standard models of how secondary local extinction risk of plants is related monotonically to phenological mismatch with pollinator bees ( A ). The relationship can be fit with a general exponential model ( y = a x b ; dashed purple line: 0 < b < 1; orange line: b > 1) or a logistic model ( y = L 1 + e - k ( x - x 0 ) ; dot-dashed blue line). If the plants located in low-latitude regions are more dependent on specialist bees for pollination due to high specialization at low-latitudes whereas plants at high latitudes rely more on generalist bees, the sensitivity of secondary local extinction risk to phenological mismatch could either decrease from low to high latitudes for plants interacting with specialist pollinators (dashed red line) or increase for plants interacting with generalist pollinators (dark blue line) ( B ).

Our study focuses on the plant genus Viola and takes advantage of ca. 120 y of historical data on these plants and their principal bee pollinators in the eastern United States ( Fig. 3 and SI Appendix , Tables S1 and S2 ). Viola species are typical early-spring flowering plants with a wide geographic distribution. We explore the phenological mismatch between Viola spp. and both generalist and specialist pollinator bees, and test whether the secondary extinction risk of plants is more sensitive to phenological mismatch with one group versus the other ( Fig. 2 B ). For example, generalist pollinators can obtain floral resources from multiple plant taxa, which may reduce the likelihood of pollination disruptions due to phenological mismatch. As a result, plants are likely to experience a mitigated secondary extinction risk linked to mismatch with generalist pollinators. In contrast, given the same extent of phenological mismatch, plants that depend on specialist pollinators (i.e., pollinators that visit only one or a few closely related plant taxa) are likely to experience greater negative impacts than those associated with generalist pollinators ( 24 ). Based on these data, we aim to 1) examine and forecast the geographical patterns of the plants’ secondary extinction risk related to phenological mismatch with pollinator bees under future climate change scenarios, and 2) document how interactions between plants and generalist versus specialist pollinators influence such risk.


## Fig. 3.


> **Figure/Table Caption:** Occurrence records and herbarium specimens separately collected for seven pollinator bee species ( A ) for the Viola genus and 23 Viola plant species ( B ) used in our study across the eastern United States.

By shifting the focus from individual species assessments to also include their ecological interactions, our work overcomes the limitation of most previous studies that consider only primary extinction risk. Instead, we address and forecast biodiversity loss in mutualistic networks through an integrated approach to phenological studies in the face of increasingly severe effects of climate change. Importantly, digitized natural history collections, which enable the integration of climate change data, phenological information, and species distributions, represent an invaluable resource for better assessing biodiversity patterns and forecasting their changes at large taxonomic, temporal, and spatial scales ( 25 , 26 ). The exponential growth and expanding utility of these collections are crucial but they remain relatively underexplored compared to other data sources in current research ( 27 ). Predicting species responses to rapid climate change is crucial for understanding biodiversity loss and guiding effective conservation strategies ( 21 , 28 , 29 ). Since we evaluate secondary risks from disrupted interactions, we anticipate that our results will offer insights into conservation strategies for mitigating the broader impacts of climate change on ecosystems.


## Results


### Phenological Responses of Plants and Bees Along Climatic Gradients.

To predict and forecast plant flowering time and bee occurrence time under current and future climatic conditions, we built separate models for plants and bees to examine the relationship between phenology and climate ( Materials and Methods ). Phenology models for both plants and pollinator bees showed good performance, with leave-one-out cross validation (LOOCV) yielding an R 2 value of 0.796, 0.697, and 0.590 for plants, generalist bees, and specialist bees, respectively ( SI Appendix , Tables S3–S5 ). The flowering times of Viola species were significantly affected by both the long-term average and anomaly of mean annual temperature (MAT), and by the interaction between MAT and annual precipitation anomalies. Holding other variables constant, an increase of 1 SD in long-term average of MAT (i.e., 4 °C) advanced flowering by 14 ± 1.0 d across all species. An increase of 1 SD in MAT anomaly (i.e., 0.7 °C) advanced flowering by 2 ± 0.3 d on average. Our model also identified a positive interaction between MAT and annual precipitation anomalies: Increased annual precipitation was associated with delayed flowering during warmer years (For statistical details, see SI Appendix , Table S3 ).

The mean activity time of pollinator bees for Viola was also influenced by climate. For both generalist and specialist bees, their mean activity time was affected only by long-term averages of MAT, but not by any climate-anomaly variable. An increase of 1 SD in long-term average of MAT (i.e., 3.2 °C) advanced the mean activity time of generalist bees by 17 ± 0.8 d. For the specialist bee, an increase of 1 SD in long-term average of MAT (i.e., 1.7 °C) advanced activity time by 8 ± 1.4 d on average (for statistical details, see SI Appendix , Tables S4 and S5 ).


### SDMs and Primary Local Extinction Risk.

We divided the eastern United States into 20 × 20 km grid cells. We then built SDMs for each of the plant species using three algorithms and calculated the probability of occurrence at each grid cell. Most of the SDMs for Viola had high predictive power, with mean TSS values of 0.7, 0.73, and 0.76 for GAM, GLM, and MaxEnt, respectively. Fewer than 5% of models were excluded due to insufficient predictive power (TSS < 0.5). The probabilities of occurrence calculated by the three different SDM algorithms were highly correlated under both current and most future conditions estimated by three GCMs (mean r > 0.7 across all species; SI Appendix , Tables S6 and S7 ), suggesting that our results were not affected by the choice of SDM algorithm or GCM. Therefore, in the following sections we present only our results from MaxEnt and the median of all GCMs.


### Secondary Local Extinction Risk.

We fit the relationship between estimated secondary local extinction risk and the phenological mismatch under current climatic conditions using both a power and a logistic function. The secondary local extinction risk of Viola spp. was estimated to monotonically increase with phenological mismatch with their bee pollinators (fitted parameters in SI Appendix , Tables S8 and S9 ). Approximately 66% (i.e., 106 out of 161) of plant–pollinator pairs had R 2 values > 0.2, and 37% (i.e., 60 out of 161) of pairs had R 2 values > 0.5 for the power function fitting ( SI Appendix , Table S10 ). For the logistic function fitting, approximately 61% (99 out of 161) and 32% (53 out of 161) of pairs had R 2 values exceeding 0.2 and 0.5, respectively ( SI Appendix , Table S11 ). The geographic patterns in secondary local extinction risks forecast for the 2070s significantly differed from the patterns in primary local extinction risk (i.e., mean Pearson’s r between primary and secondary local risks across all plant–pollinator pairs < 0.3; Fig. 4 ; SI Appendix , Tables S12 and S13 ).


#### Fig. 4.


> **Figure/Table Caption:** The relationship between the primary local extinction risk directly caused by climate change and the secondary local extinction risk indirectly resulting from phenological mismatch with pollinator bees for Viola spp. Pearson’s correlation coefficients (r) are shown for each panel, with each panel representing one of the seven bee species (generalists, A – F ; specialist, G ) in interaction with all Viola species across all grid cells.

In general, future secondary local extinction risk of Viola spp. increased with latitude as a function of their phenological mismatch with both specialist and generalist bees ( Fig. 5 ). The phenological mismatch with generalist bees contributed more markedly to future secondary local extinction risk in high-latitude regions than did the mismatch with the specialist bee ( Fig. 5 B – D and Table 1 ). The sensitivity of plants’ secondary local extinction risk to phenological mismatch was significantly lower at high latitudes than at low latitudes for interactions with the specialist bee ( Fig. 6 ). However, the latitudinal pattern of sensitivity to phenological mismatch with generalist bees depended on the functional form used. Specifically, when fitted with a power function, the sensitivity also decreased with latitude, but the decline at high latitudes was more gradual compared to that with the specialist bee ( Fig. 6 A and B and Table 2 ). In contrast, the logistic function suggested an increased sensitivity with latitude ( Fig. 6 C and D ). These results were basically consistent across different R 2 thresholds used for filtering plant–bee pairs with low model fit ( SI Appendix , Tables S14–S23 ) and across different GCMs ( SI Appendix , Figs. S1 and S2 ).


#### Fig. 5.


> **Figure/Table Caption:** The relationship between latitude and ( A ) flowering duration; ( B ) phenological mismatch (separately for interactions with generalist and specialist pollinator bees); ( C and D ) secondary local extinction risks of plants (separately due to phenological mismatch with generalist and specialist pollinator bees) in the 2070s. Flowering duration (days) was approximated by the 95% CI of the predicted day of year of flowering. Phenological mismatch (%) was calculated as the number of nonoverlapping days between the plant flowering duration and bee activity duration, expressed as a percentage of the plant flowering duration. The secondary local extinction risks were predicted from the functional relationship with phenological mismatch. We included 60 plant–bee pairs with power model fits ( C ) and 53 plant–bee pairs with logistic model fits ( D ) greater than 0.5 for the regression of plants’ secondary local extinction risk on phenological mismatch. Median values of plants’ secondary local extinction risk and phenological mismatch at each grid cell are calculated across three General Circulation Models (GCMs, GISS-E2-1-G, HadGEM3, INM-CM4-8).


#### Table 1.

Summary of mixed-effects beta regression for secondary local extinction risk of Viola associated with phenological mismatch with six generalist and a specialist pollinator bee across latitudes



| Variable | Estimate ± SE | Z -value | P -value |
| --- | --- | --- | --- |
| Intercept | −3.028 ± 0.183 | −16.58 | <0.001*** |
| Scale(latitude) | 0.413 ± 0.003 | 131.61 | <0.001*** |
| Specialist | −1.027 ± 0.398 | −2.58 | 0.009** |
| Scale(latitude): Specialist | −0.044 ± 0.011 | 3.91 | <0.001*** |


* P < 0.05; ** P < 0.01; *** P < 0.001.

The secondary local extinction risks were predicted from the functional relationship with phenological mismatch. We included 60 plant–bee pairs with power model fits greater than 0.5 for the regression of secondary local extinction risk on phenological mismatch. Median phenological mismatch value derived from three GCMs was used to calculate the secondary local extinction risk of plants for each grid cell.


#### Fig. 6.


> **Figure/Table Caption:** Sensitivity of secondary local extinction risk for Viola spp. to phenological mismatch across latitudes in the 2070s. Phenological mismatch (%) was calculated as the number of nonoverlapping days between the plant flowering duration and bee activity duration, expressed as a percentage of the plant flowering duration. The secondary local extinction risks were predicted from the functional relationship with phenological mismatch. We included 60 plant–bee pairs with power model fits greater than 0.5: ( A ) generalist bees and ( B ) a specialist bee; and 53 plant-bee pairs with logistic model fits greater than 0.5: ( C ) generalist bees and ( D ) a specialist bee. Median values of plants’ secondary extinction risk and phenological mismatch at each grid cell are calculated across three GCMs (GISS-E2-1-G, HadGEM3, INM-CM4-8).


#### Table 2.

Summary of mixed-effects beta regression for the sensitivity of secondary local extinction risk of Viola to phenological mismatch across latitudes



|  | Variable | Estimate ± SE | Z -value | P -value |
| --- | --- | --- | --- | --- |
| Generalists | Intercept | −3.007 ± 0.122 | −24.7 | <0.001*** |
| Phenological mismatch | 0.761 ± 0.002 | 382.4 | <0.001*** |
| Latitude | 0.174 ± 0.002 | 95.8 | <0.001*** |
| Phenological mismatch: Latitude | −0.051 ± 0.002 | −34.1 | <0.001*** |
| Specialist | Intercept | −4.149 ± 0.137 | −30.33 | <0.001*** |
| Phenological mismatch | 1.073 ± 0.006 | 179.64 | <0.001*** |
| Latitude | 0.155 ± 0.006 | 25.63 | <0.001*** |
| Phenological mismatch: Latitude | −0.205 ± 0.006 | −36.22 | <0.001*** |


* P < 0.05; ** P < 0.01; *** P < 0.001.

Beta regressions were constructed separately for plants pollinated by generalist bees and those pollinated by the specialist bee. The secondary local extinction risks were predicted from the functional relationship with phenological mismatch. We included 60 plant-bee pairs with power model fits greater than 0.5 for the regression of secondary local extinction risk on phenological mismatch. Median phenological mismatch value derived from three GCMs was used to calculate the secondary local extinction risk of plants for each grid cell.

After accounting for potential buffering effects using the minimum phenological mismatch across all generalist bees for each plant species at each grid cell, we still observed a significant increase in the future secondary local extinction risk of Viola spp. with latitude ( SI Appendix, Tables S24 and S25 ). The sensitivity of plants’ secondary local extinction risk to phenological mismatch decreased with latitude for interactions with the specialist bee. Likewise, when fitting a power function, the sensitivity to phenological mismatch with generalist bees showed a milder decline in high-latitude regions relative to that with the specialist bee, whereas logistic fitting indicated an increased sensitivity with latitude ( SI Appendix , Tables S26 and S27 ). These results suggest that generalist bees have no significant buffering effects on our conclusions.


## Discussion

It is well documented that many plant species are being negatively affected by climate change ( 5 , 21 ). However, their potential extinction risk might be especially severe for those that have lost their principal pollinators or for species whose phenological responses to climate change lead to temporal mismatches with their pollinators ( 18 , 19 , 30 – 32 ). This mismatch can effectively create a “secondary extinction vortex” ( 20 ). Although relatively little is known about the prevalence of such ecological mismatches, even less is known about the geographical mosaic of the risks of secondary extinctions for plants. Our results clearly demonstrate increased risks of secondary extinctions for Viola species with latitude and reveal how interactions between plants and their generalist versus specialist pollinators influence secondary extinction risk across latitudes. Our findings will help to better inform conservation policies to mitigate further extinction risks resulting from disrupted plant–pollinator interactions under future climate change.


### Secondary Local Extinction Risk Increases with Latitude.

We identified a significant increase in secondary local extinction risk of Viola spp. with latitude that appears to be driven by phenological mismatch with generalist bees ( Fig. 5 ). Although both plant flowering time and the activity of generalist pollinators respond strongly to long-term average of MAT, this apparent synchrony reflects similar spatial variation in phenological timing across different climate regimes rather than temporal shifts in response to climate change. The observed mismatches are more likely attributable to accelerated warming (i.e., increasing MAT anomalies) and the high climatic variability observed at higher latitudes ( 33 , 34 ), and to the differing phenological sensitivities of plants and pollinators to climate change. A high degree of warming and high climatic variability often lead to an acceleration in phenology ( 5 ). The different sensitivities of plants and pollinators result in increasing asymmetry in phenological responses between these groups, thereby increasing the likelihood of phenological mismatch ( 35 , 36 ). Our results demonstrate that the flowering time of Viola spp. is predominantly influenced by temperature anomalies. However, generalist bees were not significantly affected by any of the climate anomaly variables included in our models ( SI Appendix , Tables S3–S5 ). This indicates that phenological (mis)matches between plants and pollinators likely depend on species (or taxon)-specific responses to climatic cues that vary with latitude.

Another potential contributor to the forecasted elevated secondary local extinction risk at higher latitudes may be flowering duration. Longer flowering duration can buffer against phenological mismatches by increasing the likelihood of pollinator activity overlap. Li et al. ( 37 ) demonstrated longer flowering duration in warmer areas. This suggests that shorter flowering durations at higher latitudes could constrain opportunities for interaction with pollinators, thus compounding the effects of phenological mismatch and contributing to the more severe secondary local extinction risk observed at high latitudes. Our study applied the 95% CI of predicted flowering DOY as a proxy for flowering duration and also identified that both flowering duration and overlap with bee activity periods decreased with latitude ( Fig. 5 ). The limited number of specimens at each location constrains our ability to directly estimate the duration of plant flowering and bee activity. Moving forward, new observations and specimen collections will be essential for better understanding the mechanisms driving geographical patterns in phenological mismatch and the resulting secondary local extinction risk between plants and pollinators.

It is worth noting that plants’ secondary local extinction risks may be ameliorated by reproductive strategies or other traits that may buffer against phenological mismatches with pollinators or their loss altogether. Potentially most relevant here is that the self-pollinating cleistogamous flowers of Viola spp. ensure reproductive success especially in environments such as high-latitude regions with unstable conditions, short growing seasons, and a lack of pollinators, albeit with a potential cost of inbreeding depression resulting from reduced genetic variability and fitness of offspring ( 38 , 39 ). Other species may also evolve the ability for self-pollination, thereby achieving self-sustaining or even short-term expansion of plant populations during periods of rapid climate change (e.g., Capsella rubella ) ( 40 ). However, inbreeding depression associated with self-pollination may severely limit the ability of plants to adapt to novel environmental conditions expected to occur under different climate change scenarios, ultimately increasing both primary and secondary local extinction risks. Limited detection by crowdsourcers precluded our ability to include cleistogamous flowers in our analysis, but future research should assess whether there is any association between the relative proportion of cleistogamous and chasmogamous flowers, climate change, and phenological mismatch.

More generally, our results indicate that climate change likely poses a more serious threat to plant–pollinator networks at higher latitudes, with expected negative effects on ecosystem stability, gene flow, population maintenance, and biodiversity in these areas ( 9 , 41 ). This may be further exacerbated by the tremendous acceleration of warming in arctic biomes relative to other biomes ( 42 ). Future studies should explore mechanisms behind the different phenological responses of plants and insects to climate change, such as phenotypic plasticity, local adaptation, and evolutionary change in reaction norms ( 17 ), and assess the potential impacts of these changes on other important ecological interactions (e.g., seed dispersal, vegetation regeneration).


### The Sensitivity of Secondary Local Extinction Risks to Phenological Mismatch.

The secondary local extinction risk for plants depends on the type of pollinator group they interact with. In some regions, plants have evolved to rely on just one or a few pollinators, which can help them avoid competition with other plants for the same resources, a phenomenon known as “biotic specialization” ( 43 , 44 ). Several studies have reported increasing biotic specialization in the tropics toward the equator. Because resources are divided more finely among many plant species at lower latitudes, each species tends to rely on specific resources to reduce interspecific competition ( 44 – 46 ). Therefore, plant secondary local extinction risks should be more sensitive to phenological mismatches with specialist bees at lower latitudes. Our results that the sensitivity to phenological mismatch with the specialist bee decreases with latitude support this hypothesis. However, the sensitivity to phenological mismatch with generalist bees is more complex. Plants show high sensitivity at low latitudes, but when fitted with a power function, the sensitivity decreases more mildly than with the higher latitude specialist bee. In contrast, the sensitivity increases significantly at high latitudes when fitted with a logistic function.

Different functional forms used to model the relationship between plants’ secondary local extinction risk and phenological mismatch may capture differences in the responses of plant–pollinator systems to environmental pressures. The fit of the power function implies a gradual decline in the plants’ sensitivity to mismatch with generalist bees as latitude increases, which may reflect redundancy and a buffering capacity within a system under unfavorable conditions ( 47 ). Conversely, the fit of the logistic function may reveal a stronger dependence on pollinators and system vulnerability. When phenological mismatches increase sharply beyond a critical point at higher latitudes, it can lead to a rapid rise in extinction risk ( 48 ). However, the fits of both functions illustrate a qualitatively common pattern: Plants rely on both specialists and generalists for pollination at low latitudes but may depend more heavily on generalist bees at high latitudes.

This pattern may reflect the strategies of plant individuals at different latitudes to mitigate the risks of secondary extinction. Although higher diversity at low latitudes leads to greater specialization among individuals ( 43 ), the high resource diversity at low latitudes also requires pollinator bees to generalize their diet ( 49 ). Pollinator bees must therefore diversify their food sources to meet the needs of various plants ( 50 ). Thus, it appears the high dependency of Viola on both specialist and generalist bees increases pollination efficiency and reduces secondary local extinction risk in environments with high competition at low latitudes.

At high latitudes, in contrast, shorter growing seasons require plants to maximize pollination efficiency to ensure successful reproduction ( 51 ). Generalists associated with many partners may have distinct selective advantages compared to specialists because of sampling, complementarity, and portfolio effects, enabling these generalists to visit a variety of plants within a short time frame ( 52 ). Generalized pollination at higher latitudes is likely to increase functional redundancy and resistance of plant communities to secondary extinctions ( 9 , 53 ).

Because our study incorporates only one plant taxon, our understanding of the evolutionary strategies behind variations in the sensitivity of secondary local extinction risk to phenological mismatch with generalist and specialist bees across latitudes remains somewhat limited. Future research should seek to include multiple plant taxa at larger spatial and phylogenetic scales to gain a deeper insight into mechanisms driving these variations and make the relevant conclusions more broadly applicable.


### Implications for Future Conservation Planning.

Although the protection of individual species remains the fundamental premise of conservation biology, conservation biologists (and ecologists) have evolved from their early emphasis on preserving individual species to a broader remit that now includes the maintenance of interaction networks and ecosystem services that improve human well-being (e.g., food and fruit supply) ( 54 ). For example, it is estimated that 5 to 8% of global crop production would be lost without effective pollination, especially by insects ( 55 , 56 ).

Here, we identified that the geographical patterns in primary local extinction risk of Viola spp. resulting from climate change were not strongly correlated with secondary local extinction risk associated with phenological mismatch with bees ( Fig. 4 and SI Appendix , Tables S12 and S13 ). This suggests that conservation priorities identified based solely on primary extinction risks as is commonly done is likely insufficient to address the multivalent complexities of extinction risk and could fail to support self-sustaining populations of either the plants or their mutualist bee pollinators ( 57 ). Our results underscore the importance for future conservation planning of addressing secondary extinction risks caused by asynchrony between plants and pollinators. These conservation strategies may include establishing effective pollinator corridors, long-term phenological monitoring of both plants and pollinators, protecting climate-sensitive pollinator habitats, and integrating secondary extinction risk into global conservation frameworks. Of course, continued basic science research into the nature, timing, and disposition of plants and associated pollinator interactions needs greater focus and emphasis in the coming years. Natural history collections remain an essential resource for such efforts ( 58 , 59 ).

Our study assumed that all bee species occurred across the entire eastern United States and focused only on the risks of secondary extinctions for plants. However, reduced floral resources could also cause the activity periods of bees to decline when food plants are unavailable, leading to decreased diet breadth and subsequent secondary extinction risks for pollinators ( 19 ). Future studies should further develop modeling frameworks to comprehensively consider the impacts of climate change on the secondary extinction of both plants and pollinators.

It is worth noting that spatial biases in specimen records may influence the robustness of phenological estimates ( 60 ). For example, certain regions, including the state of New York, have substantially fewer herbarium specimens than neighboring states. Several grid cells across the study area also lack sufficient sample sizes to reliably estimate phenological metrics (e.g., onset, offset, and duration of phenological events), especially for pollinator bees. We acknowledge that these uneven sampling efforts, combined with limited data availability in some grid cells may introduce uncertainty into our estimates of phenological mismatch and secondary local extinction risk. Moreover, our study only focused on bees that are well documented as primary pollinators of Viola species; other insect groups such as butterflies and moths also pollinate species within this genus. If other pollinators can functionally compensate for phenological mismatches between bees and Viola , our narrow focus on well-studied bees may have led us to underestimate the resilience of Viola to shift in their phenology. Future work leading to greater data availability could use our framework with more pollinators and increase understanding of plant–pollinator interactions under climate change.


## Materials and Methods


### Study System.

We focused on 23 Viola plant species and 7 solitary bee species ( SI Appendix , Tables S1 and S2 ) in the eastern United States (i.e., coastal states from Maine in the north to Florida, and also westward to West Virginia). We chose this system for several reasons. First, there is reliable, published information on generalist versus specialist bees that pollinate Viola spp. in this large geographic region. Second, both Viola and its pollinators have been widely collected, and abundant historical specimen records are available and digitized as part of the global metamuseum ( 27 ). Herbarium specimens for Viola spp. have easily identifiable chasmogamous flowers, enabling us to estimate their corresponding flowering times using previously published methods ( 16 , 25 , 26 ). Finally, both Viola and its pollinators have large geographic ranges across the eastern United States ( Fig. 3 ), which allow us to examine phenological shifts across latitudes.

Viola is a large genus of flowering plants in the family Violaceae. Many species of Viola have a dual reproductive strategy, which involves two distinct flower types: the early-stage floral bud is predetermined to develop into either a chasmogamous (open and outcrossing) or cleistogamous (closed, and self-pollinating) flower ( 61 ). Among the 73 species of Viola in the US north of Mexico, 60 are reported to have cleistogamous flowers ( https://beta.floranorthamerica.org/Viola ).

Solitary bees in the families Andrenidae, Anthophoridae, and Megachilidae are among the most important pollinators of chasmogamous Viola flowers ( 62 ). Andrena violae (Andrenidae) is a genus-level specialist pollinator of Viola in the eastern United States ( https://jarrodfowler.com/specialist_bees.html ). The other six bee species we studied are genus-level generalist pollinators with contrasting natural histories (solitary ground nesting Andrena spp. [Andrenidae] and solitary above-ground cavity nesting Osmia spp. [Megachilidae]; SI Appendix , Table S2 ). These generalist bee species are reported to pollinate plants belonging to genera other than Viola . For example, Andrena carlini is known to visit flowers from genera such as Taraxacum , Rubus , and Vaccinium . We follow the coding by Bartomeus et al. ( 53 ) of pollination relationships between Viola and these generalist bees. These bee species are known to emerge in early spring, which is a particularly important time period in terms of organismal response to climate change ( 63 ) and can be compared with early-flowering plants such as Viola spp.


### Viola Occurrence Data.

We derived occurrence and phenology data for Viola spp. from herbarium specimens digitized by the Consortium of Northeastern Herbaria (CNH; https://portal.neherbaria.org/portal/ ) and the Southeast Regional Network of Expertise and Collections (SERNEC; https://sernecportal.org/portal/index.php ). The 23 Viola species we used for our study ( SI Appendix , Table S1 ) met the following criteria: 1) there were at least 50 unique specimens per species across the eastern United States; 2) the specimens had both an exact collection date (which we expressed as day of year [DOY] ranging from 1 to 365) and either exact or county-level location information (the latter were georeferenced to the geographic centroid of the county); and 3) the specimens included reproductive structures that were easily identifiable and countable (i.e., buds, flowers, and fruits).

For SDM, we augmented the occurrence data of the 23 Viola species from CNH and SERNEC with county-level distribution data (i.e., presence/absence data) from the Biota of North America Program’s (BONAP; http://www.bonap.org/ ) North America Plant Atlas (NAPA) ( 64 ) and from the Global Biodiversity Information Facility (GBIF; https://gbif.org/ ). County-level occurrence data were then overlaid onto 40×40-km grid cells (Mercator projection EPSG 3857) covering the eastern United States. As some grid cells were located on the borders and along the coasts of the eastern United States, we removed incomplete grid cells (i.e., those with an area smaller than 800 km 2 ). If more than half of a grid cell was covered by one or several counties with the occurrence of a species, it was considered to be present in that grid cell ( 65 ).


### Viola Phenology.

We hired crowdsourcers through Amazon’s Mechanical Turk service (MTURK; https://www.mturk.com/ ) to count the number of buds, flowers, and fruits of each digitized herbarium specimen from CNH and SERNEC using the CROWDCURIO platform ( 25 ) following well established protocols ( 66 , 67 ). Each specimen was independently evaluated by three individuals (on average), and we used a reliability score to assess the reliability of each individual and their data. Specifically, each 10-image set, in random order and scored by one person, included nine unique images and one duplicate image. This duplicate image was randomly selected from the remaining nine images. The reliability scores were calculated as the absolute difference in counts of buds, flowers, and fruits between the two duplicate specimens, divided by the total counts for each phenological state separately, and then subtracted from 1 ( 67 ). Specimen observations scored by crowdsourcers with a reliability score of zero were excluded from our analyses following Park et al. ( 16 ). If an individual received a reliability score of zero for one organ, all organs would be assigned a score of zero and thus excluded from our analyses.

In total, the crowdsourcers provided reliable data on Viola flowering phenology from 8,200 specimens spanning 124 y (i.e., 1895 to 2018). Of these, ≈50% (4,075 specimens) were considered to represent the main flowering period following ( 67 ) of the Viola spp. and were used in subsequent analyses. That is, each of these 4,075 specimens: i) contained at least one open flower; ii) contained more open flowers than the combined number of buds and fruits; iii) contained a number of flowers representing at least 5% of the maximum number of flowers observed on a given species; and iv) had collection dates between the 5 and 95% quantile of observed flowering dates (DOYs).


### Bee Occurrence Data.

Approximately 80% of the occurrence records of the seven bee pollinator species (henceforth “bees”) were gathered from the online Symbiota Collections of Arthropods Network (SCAN) ( 68 ); additional collection records of preserved specimens were obtained from GBIF. Only SCAN and GBIF records that included an exact date and location (i.e., latitude and longitude or county information that could be assigned to its centroid) were included in our analysis. To prevent bias introduced by different collection efforts, only one record representing a certain collection event was retained; occurrence records were considered to be from the same collection event if they had both the same date and coordinates of collection ( 8 ). The 6,714 bee occurrence records that met the above criteria were collected in the eastern United States between 1900 and 2022. Bee occurrence data were mapped onto the same 40×40-km grid cells covering the eastern United States that we used to map the Viola occurrence data.


### Bee Phenology.

We used DOY of the collection date of each unique bee occurrence record as a proxy for a day on which it was actively foraging. To estimate the main occurrence time of each bee species, we used MaxLike, a formal likelihood model that explicitly estimates the probability of species occurrence given presence-only data and a set of environmental covariates ( 69 ). Here, we assume that specimen records with a high probability of occurrence, generated by MaxLike, represent those periods when the focal bee species is most likely active. This is because MaxLike models are trained on presence-only data and can capture the temporal and environmental preferences associated with species’ activity patterns. Although this approach ignores finer-scale behavioral variations, it provides a relatively reliable proxy for the main activity periods in MaxLike. We initially chose six bioclimatic variables relevant to bee distributions to build the models: temperature seasonality (bio4, the corresponding WorldClim variable code), mean temperature of the warmest quarter (bio10), mean temperature of the coldest quarter (bio11), precipitation seasonality (bio15), precipitation of the wettest quarter (bio16) and precipitation of the driest quarter (bio17). We excluded mean temperature of the coldest quarter due to its high correlation with other variables (r > 0.7). Climatic data for each year-locality combination were obtained from PRISM database (see the detailed description in Environmental Data ).

For each bee species, we randomly selected 80% of the occurrence data as the training dataset, and this process was replicated 100 times. To evaluate the predictive accuracy of each model, we first identified the minimum predicted area (MPA) ( 70 ), which is the proportion of the study area predicted as present based on the probability threshold that ensures a user-defined percentage of the test data is correctly classified as present. Here, we set the threshold to 0.9, which means the minimum proportion of the study area required to predict 90% of the test-presence records. Models yielding a low MPA are considered superior, as they provide more spatially specific predictions. Following Engler et al. ( 70 ), we excluded models with an MPA > 0.7 (i.e., 70% of the study area is predicted suitable to capture 90% of the occurrences). We calculated the median probability of occurrence value from the remaining models for each species and extracted the 95% CI to present their main activity periods. However, it is worth noting that these data points do not fully represent the complete grid-cell level distributions of bee species when we overlap data points with 40 km grid cells. Therefore, we did not construct SDMs for bee species and assumed that all bee species occurred over the entire eastern United States when calculating the secondary extinction risk of plant species.


### Environmental Data.


#### Climatic and geographic data of specimen localities for plants and bees.

We used estimates of historic (1895 to 2022) average monthly air temperature and precipitation data at a 4-km resolution from PRISM (product AN81m; https://prism.oregonstate.edu/ ). For each specimen with a specific location and year combination, we estimated the MAT and annual precipitation and assigned these values to the corresponding specimens for both plants and bees. For each collection site, we first calculated the long-term mean temperature and precipitation conditions separately for plants and for bees. We then calculated the temperature and precipitation anomalies, which we defined as the difference in climatic conditions between the year of collection and the long-term mean for the entire collection range (i.e., 1895 to 2018 for plants and 1900 to 2022 for bees), for each record location, following Munson and Long ( 71 ) and Pearson et al. ( 72 ). Climatic anomalies have been shown to be associated with plant flowering time and are used widely in modeling phenology–climate relationships ( 36 , 71 ).


#### Environmental data used for modeling plant distributions.

Recent (1970 to 2000) and future forecasted (2061 to 2080; henceforth referred to as “2070s”) climatic data at a resolution of 2.5-arc-min were obtained from WorldClim ( https://www.worldclim.org/ , ver. 2.1; all 19 climatic variables, bio1 to bio19) and climate values assigned to each grid cell were the means of all data points within it. We also included five soil variables (i.e., sand content, clay content, silt content, bulk density, and coarse fragments) in the SDMs for plants ( 73 ). We assumed these soil variables were constant through time, and calculated their within-grid-cell mean values at two soil depths (0 to 5 cm and 5 to 15 cm) using data from the SoilGrid250m database ( https://www.soilgrids.org/ ).

We reduced the number of environmental and climatic variables using principal component analysis (PCA) on 24 soil and climatic variables ( SI Appendix , Table S28 ). The eigenvectors were used to calculate the scores of the first seven derived principal components, which represent 97.3% of the total variance and were used as new predictors for creating the SDMs for all Viola species. The same eigenvectors were used to calculate the scores of the principal components for future environmental scenarios.

Future climatic projections were derived from three GCMs—GISS-E2-1-G, HadGEM3, and INM-CM4-8—run for the most extreme shared socio-economic pathways (SSPs)—SSP5-8.5 ( 74 ).


### Statistical Modeling.


#### Relationships between climate and phenology.

We applied linear mixed-effect models (LMMs) to examine the phenological sensitivities of plants and occurrence of bees to current and future climates across the eastern United States. This model framework allowed us to hierarchically incorporate the variation in phenological responses to climate across multiple species ( 75 ). The same structure and predictor variables were used for separate models fitted for Viola , the six generalist bees, and the specialist bee. All predictor variables were centered and scaled to a mean value of 0 and a SD of 1 to avoid introducing bias. Correlation coefficients among all selected predictor variables were <0.1, limiting the effects of collinearity.

For the full Viola model, the response variable was the DOY for each specimen (as representing its mean flowering time). Predictor variables included as fixed effects the long-term average (1895 to 2018) and interannual anomalies of mean temperature and total precipitation, the interaction between temperature and precipitation anomalies. The full model also included a random-intercept term for plant species and random slopes for plant species responses to temperature and precipitation anomalies. The random slopes are interpreted as species-specific phenological sensitivities to interannual climate change.

For the full model for generalist bees, the response variable was the DOY for each collection record (as representing its mean activity time). Fixed predictor variables included long-term average (1900 to 2022) and interannual anomalies of mean temperature and total precipitation, the interaction between temperature and precipitation anomalies. The full model also included a random-intercept term for generalist bee species and random slopes for the responses of generalist bee species to temperature and precipitation anomalies. Since the dataset included only one specialist bee, the model for the specialist bee did not incorporate any random components.

Given the broad spatial and temporal extent of our dataset, we additionally accounted for spatial and temporal autocorrelation by separately incorporating a spatial random component “~Matern (1|longitude + latitude)” and a first-order autoregressive temporal structure “~AR1(1|year)” in the model. All models were fitted using the “fitme” function in the “spaMM” package (ver. 4.4.16) ( 76 ) of the R software system (ver. 4.2.1). The significance of the predictor variables was evaluated using Wald statistics (reported as “ t values”) provided by the “fitme” model output. To evaluate model performance and the explanatory power of fixed and random effects, we calculated marginal R 2 , conditional R 2 , and performed leave-one-out cross-validation (LOOCV). LOOCV iteratively evaluates model performance by fitting the model to all but one observation and using the excluded data point for validation ( 77 ).

To predict the mean flowering time for each plant species and mean activity time for each bee species in each grid cell under recent (i.e., 1970 to 2000) and future (2070s) conditions, we applied the “predict” function in the “stats” package (ver. 4.0.0) to the fits of the LMMs. The associated SE allowed us to calculate 95% CI around these predictions. These CI represent the uncertainty bounds of both plant and pollinator phenology and were used to approximate the duration of each phenophase as well as the potential temporal overlap between plant flowering and bee activity (Eqs. 1 – 5 ). Recent and future temperature anomalies for each grid cell were estimated as differences from its long-term mean temperature, whereas precipitation anomalies were calculated as a proportion of its long-term mean precipitation.


#### SDMs to estimate the primary extinction risk of Viola species.

As our Viola dataset lacked true absences, we generated random pseudoabsences (i.e., randomly selected grid cells that were considered as species absences) ( 78 ). For each species, twice as many pseudoabsences as real presences were generated; the entire procedure was repeated 10 times, each time with a new set of pseudoabsences. SDMs were calibrated for each species using three algorithms: generalized linear models (GLMs), generalized additive models (GAMs), and Maximum Entropy (MaxEnt). We used a repeated data-splitting procedure to evaluate the predictive power of each individual model. Each model was trained on 80% of the distribution data of each species before being assessed against the remaining 20% using the true skill statistic (TSS) ( 79 ). This data-splitting procedure was also repeated 10 times (resulting in a total of 100 individual models for each algorithm and species). Those models with TSS > 0.5 were adopted to project the probability of occurrence of each plant species per grid cell under both current and future conditions. Model projections were carried out over the entire eastern United States and all models were projected at the same spatial resolution as the distribution data (i.e., 40-km). We used the median value of all model predictions as the final forecast of occurrence probability for each Viola species. In the context of extinction, the local primary extinction risk ( P e ) of plant species within each grid cell was simply calculated as 1 − the probability of occurrence ( 80 ).


#### Calculation of secondary local extinction risk of Viola species.

We inferred the secondary local extinction risk of Viola spp. for each grid cell based on their predicted probability of occurrence from SDMs and their predicted phenological mismatch with bees. Phenological mismatch between plants and pollinator bees was quantified for each plant–bee pair at each grid cell under both recent (1970 to 2000) and future (2070s) climatic conditions. Specifically, we calculated the proportion of overlap between the 95% CI of predicted flowering DOY and bee activity DOY. This overlap was then standardized by the length of the plant’s predicted flowering DOY CI, and phenological mismatch was defined as one minus this standardized proportion.

Since phenological events are cyclical and repeat annually, the entire year can be represented as a 360-degree circle. To account for the circular nature of the phenological year, we first converted the 95% CI of predicted flowering DOY for plants and activity DOY for bees into angular degrees (Eq. 1 ). We then calculated phenological mismatch between plants and pollinator bees directly on a circular scale ( 81 , 82 ).



| deg = DOY 365 ∗ 360 , | [1] |
| --- | --- |


where DOY represents the lower or upper bounds of the CI. For each plant–bee pair at each grid cell, we calculated the proportion of overlap between their respective 95% CI in angular space. Let the plant interval be CI p = [ L p , U p ] , and the bee interval be CI b = [ L b , U b ] , where all bounds are in degrees. If either the plant or bee CI spanned across year-end, we treated it as a union of two intervals (Eq. 2 ):



| split L , U = L , U L ≤ U L , 360 , 0 , U L > U . | [2] |
| --- | --- |


We then calculated the total phenological overlap O by summing the pairwise overlaps between all subintervals of plant and bee phenological periods (Eq. 3 ).



| O = ∑ i ∑ j max ( 0 , min ( U p i , U b j ) - max ( L p i , L b j ) ) , | [3] |
| --- | --- |


where i and j iterate over the subintervals of plant and bee phenology, respectively. Since each phenological CI can be represented by one or two subintervals, therefore, the total number of pairwise comparisons ranges from one to four. The phenological mismatch between plant flowering and bee activity was then calculated as one minus the ratio of the overlap between their 95% CIs to the total length of the plant’s flowering CI ( D p ) (Eqs. 4 and 5 ).



| D p = U p - L p L p ≤ U p 360 - L p + U p L p > U p , | [4] |
| --- | --- |




| Phenological mismatch = 1 - O D p . | [5] |
| --- | --- |


We assumed that the phenological mismatch between plants and bees would lead to a proportional decrease in probability of occurrence of plant species (as in Fig. 2 A ). Therefore, the secondary local extinction risk of each plant species at each grid cell could be estimated approximately as follows (Eqs. 6 and 7 ):



| P ( mismatch ) = P ( occurrence ) ∗ O D p , | [6] |
| --- | --- |




| S e = P ( occurrence ) - P ( mismatch ) , | [7] |
| --- | --- |


where P ( m i s m a t c h ) represents the adjusted probability of occurrence of each Viola species in each grid cell after accounting for the phenological mismatch with each bee species; P ( o c c u r r e n c e ) was the original probability of occurrence of each Viola species in each grid cell inferred from the SDMs; and S e was the estimated secondary local extinction risk (i.e., decreases in probability of occurrence) of each Viola species at each grid cell. As the phenological mismatch increases, the adjusted probability of occurrence decreases, leading to a greater increase in potential secondary local extinction risk.

To more intuitively and mechanistically describe the relationship between the S e of each Viola species and its phenological mismatch with the bees, we fitted S e to the phenological mismatch estimated under current conditions using both a power and a logistic function ( Fig. 2 A ) to capture both monotonic and saturating responses. These two functional forms were chosen because both theoretical and empirical studies suggest that the nonlinear species loss in pollination system driven by stressors including phenological mismatch may induce threshold-like or tipping-point responses, rather than simple linear trends ( 83 ), particularly in communities characterized by high interdependence between plants and pollinators ( 84 ). This approach enabled us to isolate and quantify the contribution of phenological mismatch to S e , independent of other climate-driven or environmental factors captured by SDMs. To ensure robustness of the fitted relationships, we used three different R -squared thresholds (i.e., R 2 = 0.2, 0.3, 0.5) to exclude plant–bee pairs with poor model fit.

The phenological mismatch for the 2070s of each plant–bee pair with a high model fit was then substituted into the power function to obtain future S e of each Viola species. Since we used the median value of the species’ probability of occurrence at each grid cell across three GCMs, we extracted the median phenological mismatch across these GCMs to minimize the impact of extreme climate values on the mismatch and used it to estimate the future S e . This approach allowed for a more robust representation of climate conditions by mitigating the influences of outliers that may skew the phenological mismatch estimates. We also reported the results from each GCM for the subsequent analysis ( SI Appendix , Figs. S1 and S2 ).

Finally, we compared the geographical patterns in P e and S e of each plant species. We then compared S e of plant species resulting from its phenological mismatch with generalists and specialist bee species across latitudes. We used mixed-effects beta regression for this comparison; latitude, pollinator type (generalists vs. specialist), and their interactions were considered to be fixed factors, and individual plant and bee species were treated as separate random factors. To further examine how plant S e changed with latitude under equivalent phenological mismatches and how this relationship varied between plants pollinated by generalists and a specialist, we fitted two additional models: the first was a mixed-effects beta-regression model with S e as the response variable, latitude and phenological mismatch of each plant–generalist pair as fixed factors, and plant and bee species as separate random factors. For the second one, we did not include a random component for bees because we only had a single specialist species. Since beta regression is designed for continuous outcomes strictly within the (0, 1) interval, it is not suitable when the response variable includes exact zero values. Therefore, we used alternative zero-inflated beta regression models to account for the presence of zeros in the S e data. All these analyses were carried out using the “glmmTMB” function in the “glmmTMB” package (ver. 1.1.9) ( 85 ).

Because plant species depend on multiple generalist pollinators, they may still be able to rely on the most temporally aligned pollinator even in the presence of significant phenological mismatches with other generalist bees. To account for this buffering effect, we extracted the minimum phenological mismatch value across all generalist bees for each plant species at each grid cell and built two beta-regression models to separately explore the latitudinal patterns in S e of plant species and the sensitivity of plant S e to phenological mismatch across latitude. The beta-regression model structure is the same as the model described above, which included all generalist bee species within each grid cell.

The flowchart illustrating the analytical framework is shown ( SI Appendix , Fig. S3 ).


## Acknowledgments

We acknowledge Professor Jiajia Liu from Fudan University for his constructive suggestions. We also acknowledge funding from Harvard University and by NSF Funding Grants: DEB 1754584, EF1208835, DEB 2101884, DEB 1802209, and MRA 2105903.



S.P. and A.M.E. designed research; S.P. performed research; S.P. contributed new reagents/analytic tools; S.P. analyzed data; C.C.D. funding support; and S.P., A.M.E., and C.C.D. wrote the paper.


### Competing interests

The authors declare no competing interest.


## Footnotes

Preprint servers: This manuscript was deposited as a preprint on EcoEvoRxiv [license type: CC-BY Attribution-NonCommercial 4.0 International]. Doi: https://doi.org/10.32942/X2VH1X .

This article is a PNAS Direct Submission. D.W.I. is a guest editor invited by the Editorial Board.


## Contributor Information

Shijia Peng, Email: [EMAIL_REDACTED].

Charles C. [AUTHOR], Email: [EMAIL_REDACTED].


## Data, Materials, and Software Availability

All codes and data used in the analyses are available on GitHub ( [GITHUB_REPO_REDACTED] ) ( 86 ).


## Supporting Information

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Supplementary Materials


### Data Availability Statement

All codes and data used in the analyses are available on GitHub ( [GITHUB_REPO_REDACTED] ) ( 86 ).
