# De-Identified Manuscript `OOD_ANON_22`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Grasslands represent a biodiversity hotspot in the European agricultural landscape, their restoration is necessary and offers a great opportunity to mitigate or halt harmful processes. These measures require a comprehensive knowledge of historical landscape changes, but also adequate management strategies. The required data was gathered from the sand grasslands of northern Serbia, as this habitat is of high conservation priority. This area also has a long history of different habitat management approaches (grazing and mowing versus unmanaged), which has been documented over of the last two decades. This dataset enabled us to quantify the effects of different measures across multiple taxa (plants, insect pollinators, and birds). We linked the gathered data on plants, pollinators, and birds with habitat management measures. Our results show that, at the taxon level, the adopted management strategies were beneficial for species richness, abundance, and composition, as the highest diversity of plant, insect pollinator, and bird species was found in managed areas. Thus, an innovative modelling approach was adopted in this work to identify and explain the effects of management practices on changes in habitat communities. The findings yielded can be used in the decision making as well as development of new management programmes. We thus posit that, when restoring and establishing particular communities, priority needs to be given to species with a broad ecological response. We recommend using the decision tree as a suitable machine learning model for this purpose.


## Introduction

As the natural vegetation of the forest-steppe biome in Central and Eastern Europe, Pannonian grasslands represent an important semi-natural habitat and biodiversity hotspot in the European agricultural landscape [ 1 , 2 ]. Since the Anthropocene, as a result of human activities (e.g. grazing, mowing, burning) grasslands have expanded across Europe [ 3 , 4 ]. However, land use changes that culminated in the intensification of agriculture in 20th century, triggered the abandonment of grassland, afforestation, or conversion into arable land. Consequently, in the late 20th century, grassland ecosystems became habitats of high conservation value [ 5 , 6 ].

Given the recent focus on biodiversity changes, grassland conservation offers a great opportunity to introduce innovative biodiversity management measures that can be implemented in the timeframe and conditions under which native species have evolved a mechanism to survive [ 7 ]. However, their design and implementation requires a comprehensive knowledge of the history of grasslands and their management, as well as its impact on the community composition of different taxa. For example, it has been established that preserved ancient grasslands are highly organised in terms of species composition and show a high degree of stability in relation to small-scale species fluctuations, while secondary grasslands are less resilient and their species pool is thus vulnerable to disturbances and immigration of other species [ 8 – 10 ]. Therefore, the species composition of these habitats is expected to respond differently to afforestation, and understanding this causality is crucial for the conservation and restoration of grassland biodiversity. Recent studies further highlight the importance of studying and monitoring different trophic groups, rather than basing management decisions on individual taxa [ 11 – 13 ]. Yet, despite the growing popularity and complexity of biodiversity research, most conservation efforts tend to neglect the role of different land uses in the biodiversity within these habitats. In recognition of this shortcoming, several authors have proposed development of conservation strategies for grassland working landscapes, i.e., ecosystems that are specifically managed with biological objectives [ 14 , 15 ].

This proposal is justified, as grasslands play a vital role in providing a diverse range of ecosystem services essential for strengthening conservation efforts, actively involving local communities. These conservation initiatives encompass various ecosystem services, including biomass production and the provision of food for grazing animals and other herbivores, carbon storage and sequestration, as well as the creation of habitats for pollinators, migratory and breeding birds, among others [ 16 ]. They also highlight the importance of grasslands as a nesting and foraging habitat for solitary bees. Since numerous solitary bee species are currently facing threats, existing evidence suggests that generalist and highly mobile species may adapt to habitat loss by expanding their foraging ranges and utilizing alternative habitats and resources within the agricultural landscape [ 2 , 17 ].

When developing these strategies, however, it is essential to recognise the role of controlled human activities—especially grazing and mowing [ 18 – 22 ] in maintaining the species richness and abundance of many taxa in grasslands [ 11 , 23 – 25 ]. Still, extant management policies and conservation measures give precedence to the identification and analysis of rare or threatened species in protected areas, thus overlooking the fact that, in any process of natural habitat restoration through succession, it is the species with a broad ecological response that first conquer the habitat and form communities that create the micro-conditions for the specialists to enter. Consequently, their importance as precursors in natural succession processes is rarely examined in scientific studies.

This perspective adopted in both research and practice has created the need for decision makers to be actively involved from the beginning of the restoration process and to prioritise the habitat types to be restored and the species that should be returned to their original habitat. To exemplify how this strategy is adopted in practice, we have conducted our investigation in the Pannonian biogeographical region. This region has a complex, long, and documented history of landscape changes and thus provides a suitable site for biodiversity analyses guided by the following aims: (i) to investigate how management measures and habitat heterogeneity impact on grassland biodiversity; (ii) to evaluate the role of grazing and mowing in the restoration, development, and heterogeneity of semi-natural grasslands; and (iii) to assess the suitability of machine learning models for decision-making processes and management programs.


## Materials and methods

The data for testing the study hypotheses was gathered from the information sources on the state of nature in the Pannonian biogeographical region over a 300-year period. Plants, insect pollinators (wild bees and hoverflies), and birds were selected as model organisms, with the view that, while all taxa differ greatly in their resource use and mobility, they are equally important for the sustainability of grassland ecosystems [ 26 ].


### Study area

Subotica Sands which served as the study site is located in the far north of the Republic of Serbia, along the state border with Hungary ( Fig 1 ). It is the southernmost part of sandy areas between the Danube and Tisa rivers [ 27 ] characterised by forest-steppes as the main native habitat type, with open grasslands—including sands, steppes, meadows, and marshes—intersected by woodlands and forests. As established by Butorac and Panjković [ 28 ], Aceri tatarici-Quercion and Festucion rupicolae mosaics have historically formed the climate-zonal vegetation of this area. However, Convallario-Quercetum roboris woods are currently present as remnants of former woodlands, while its secondary developed scrub ( Pruno spinosae - Crataegetum ) predominated [ 29 ]. Due to the vicinity of groundwater, continental saturation of soil with moisture, and specific relief with many micro-depressions, riparian forests and thickets, such as white poplar (ass. Populetum albae ) or grey sallow (ass. Salicetum cinereae ) stands, as well as marsh vegetation (ass. Carici elatae-Fraxinetum angustifoliae ), remain in small fragments [ 29 , 30 ].


#### Fig 1. Location of the study area and specific sites (blue square− mowing, black square − control, red square −grazing) within the Subotica Sands (Serbia).


> **Figure/Table Caption:** Land-use data were obtained from Copernicus Land Monitoring Service ( https://land.copernicus.eu/ ).

Despite this evident decline in native habitats, it took almost two decades of work and harmonisation of conservation policies to finally have this area protected as a region of forest conservation value in 1982. Subsequent scientific research has shown that the area is home not only to forest species, but also to extremely small populations of species of international importance (spring meadow saffron Colchicum bulbocodium subsp. Versicolor , lesser blind mole-rat Spalax leucodon ) that are restricted to small areas. In line with the latest trends in nature conservation and guided by the advances in scientific knowledge, part of the area that had previously been converted into orchards and vineyards was ploughed up in 2002. This provided an opportunity to revise the protection status and in 2003 the area was declared an Outstanding natural landscape. Active management measures were then developed and successively introduced. In the subsequent period, undergrowth was removed and large areas of Subotica Sands were mowed and levelled. Alongside these measures, in 2017, sheep and goat herds were allowed to actively graze in this area. In an event of a long winter, grazing was supplemented by regular mowing. Currently, this area serves as pasture for about 270 sheep per 230 ha, which are guided by shepherds and are permitted to roam freely. After two decades, the aforementioned active management measures were successful in the restoration of the populations of the most endangered species, thus creating the conditions for the reintroduction of some species that have previously thrived in this area (e.g., European ground squirrel Spermophilus citellus ). Thus, this study site was not only suitable for the current investigation, it is also in line with the EU regulations, within which Pannonian sands and steppes are described as natural habitats with priority [ 28 ].


### Study design

For the present investigation, we selected seven sampling sites, each covering an area of one hectare, all situated within the Level I: Total/Strict protection regime (constituting 8.32% of the Subotica Sands area). However, these sites varied in terms of the management practices they had experienced in the past two decades. To provide more insight into the habitat characteristics, we categorized them into three groups: three sites were subject to mowing (M), three to grazing (G), and one served as a control site ©, having no history of specific management measures. During our fieldwork, we employed habitat classification to further specify the characteristics of each site according to National classification of Republic of Serbia ( Table 1 ). Additionally, we established a buffer zone, extending 150 meters from the boundaries of each sampling site. This buffer zone provided a broader-scale perspective, allowing us to assess the impact of habitat features on bird and pollinator diversity. Furthermore, this approach allowed us to quantify parameters such as distance to the nearest trees, overall tree and shrub coverage, and the proportion of tree and shrub coverage within and outside of the study sites. The information required for these calculations was obtained by interpreting orthophoto images sourced from Google Earth Pro version 7.3.3.7786.


#### Table 1. Habitat types at investigated sites in the study area.



| Site | Habitat type according to the National classification of Republic of Serbia (Official Gazette 2010/35) |
| --- | --- |
| Grazing 1 | Panonian steppes on the sand * |
| Grazing 2 |
| Grazing 3 |
| Mowing 1 |
| Mowing 2 |
| Mowing 3 |
| Control | Deciduous and xerophilous scrub of Hawthorn and Blackthorn |
| Buffer zone | Pannonian forest of Peduculate oak and Narrow-leaved ash |


*6260 NATURA 2000 habitat type

In the study area, two primary management practices were implemented. Mowing was conducted twice a year, which typically occurred in June and September. In addition, the grasslands experienced moderate grazing, with an average stocking density of 0.6 ewe/lamb pairs per hectare. These grazing activities were carried out under the supervision of shepherds, who ensured that the herds were led to designated pasture locations for specific periods of the year. At the control site C, no management measures have been carried out for 20 years, and the process of secondary succession has led to the formation of the forest-steppe. During 2021 in focus of this investigation, five field trips (in March, April, May, June, and September) were conducted.

For plants, eight quadratic plots (1×1 m) were designated at each site during the first field trip, resulting in 224 plots in total. At each plot, we recorded maximum vegetation height (MVH), total vegetation cover (TVC), and coverage percentage for each flowering species. Flowering plants were collected, labelled, and identified in laboratory by consulting relevant literature [ 30 – 37 ]. In addition, in order to gain insights into community dynamics and ecological characteristics, we employed Social Behavior Types (SBT) for all plant species. SBT categorizes plant species based on their roles in the community and provides valuable information about community richness, stability, naturalness, niche occupancy, and response to disturbances or deviations from the natural state [ 38 ]. All plant material was deposited at Herbarium BUNS, University of Novi Sad, Faculty of Sciences.

During all field visits, diversity and population abundance of pollinators (wild bees and hoverflies) were observed and samples were collected for 60 minutes per site, along two transects of 500 m length. Transect walks were conducted between 9:30 AM and 5:00 PM on sunny days (with over 30% sunlight) when wind speeds were low, and temperatures were above 13°C if it was sunny and above 17°C if it was cloudy. During the summer, transect walks and observations were conducted between 7:00 AM and 12:00 PM to avoid high temperatures that reduce bee activity levels [ 39 ]. All pollinators were identified to the species level in the field, while some of them were captured using a net and were transported to the laboratory in vials filled with ethyl acetate for identification to the species level. For the identification of solitary bees, we used the following resources: Mauss [ 40 ], Amiet [ 41 ], Schmid-Egger [ 42 ], Scheuchl [ 43 ] and for hoverflies, we referred to the following publications: Vujić [ 44 ], Speight and Sarthou [ 45 ], Likov et al. [ 46 ]. The captured specimens were subsequently deposited at the Department of Biology and Ecology, University of Novi Sad, Faculty of Sciences.

The diversity and abundance of birds breeding on the surveyed sites were assessed based on territory mapping. For this purpose, sites were visited on four occasions during the breeding season, between April 15th and June 15th. Visits were conducted at the peak of daily bird activity (from 6 to 10 AM). Birds were mapped during a 5- to 15-minute walk around the site perimeters (100 × 100 m). All recorded (observed or heard) individuals, pairs, nests, or families with fledglings were precisely mapped using an orthophoto map of the landscape where individual trees, bushes, or other structural features were clearly visible. Only records within a 100 m buffer from site boundaries were included in the analysis. Atlas codes that describe breeding probability [ 47 ] were attributed to all records. Migrating species and species observed only overflying were excluded from the analysis.


### Data analysis

Species diversity were calculated as Shannon-Weaver index and was analysed for all study sites, while differences across sites and between management measures were tested through one-way ANOVA using Duncan’s test (P ≤ 0.05).

To assess the species similarity among sites grouped by management measures, Jaccard similarity index was adopted, whereby a value in the 0−0.25 range indicates small similarity of species composition between sets, 0.25−0.5 is interpreted as medium dissimilarity, 0.5−0.75 indicates medium similarity, and 0.75−1 is indicative of high similarity. In other words, values close to zero are associated with heterogeneous structures, while those close to unity imply homogenisation.

To investigate the relationship between species (pollinator and bird) diversity and habitat variables (including plant diversity), we employed generalised linear models (GLMs), based on the Gaussian distribution family. Separate models were constructed for the responses of pollinators and birds, and the best model for each response variable was selected based on Akaike’s information criterion corrected for small sample size (AICc) [ 48 ]. The AICc considers both the goodness of fit of the model and the number of parameters used, with lower values indicating a better trade-off between model complexity and fit to the data.

Linear discriminant analysis (LDA) was performed to quantify and describe sites under different management measures, with maximum vegetation height, total vegetation cover, and Shannon-Weaver index treated as predictor variables. Before performing the LDA analysis, data were pre-processed by scaling all the predictor variables. The dataset was then partitioned into a training set (consisting of 75% of all available observations) and a testing set (comprising the remaining 25%). The training set was used to fit the LDA model, while the testing set was used to evaluate the model performance. A ten-fold cross-validation method was adopted during the training process to tune the model hyperparameters and prevent overfitting. Finally, the accuracy of the LDA model was measured by computing the proportion of correctly classified observations in the testing set.

Statistical analyses (ANOVA, GLM, and LDA) were performed in R version 4.2.2 [ 49 ] using dedicated packages “vegan” [ 50 ], “agricolae” [ 51 ], “dplyr” [ 52 ], “ggplot2” [ 53 ] and “MASS” [ 54 ].

A decision tree for plants (as habitat builders) was developed in order to analyse species frequency and their causal relationship at three levels: individual plots, site level, a habitat management measure (G, M, or C). This method aimed to pinpoint vital plant species linked with various habitat management approaches. Decision trees are popular in ecological modeling, providing a visual representation of decision-making processes, particularly valuable for researchers and conservationists. These hierarchical structures involve attribute tests, branching for outcomes, and leaf nodes for predictions [ 55 ]. In ecology, they aid in tasks like species classification, habitat assessments, and biodiversity analyses, known for their interpretability even for non-experts. This interpretability is vital for informed conservation and management decisions, allowing stakeholders to comprehend strategies. By identifying key species, habitat preferences, and ecological connections, decision trees facilitate ecosystem management, bridging the gap between research and practical conservation efforts, ultimately supporting biodiversity preservation and ecological sustainability. In the field of computer science, decision trees are artificial intelligence models which belong to the machine learning subbranch of the artificial intelligence field. They are not hand-made, but rather trained on our data in order to give us meaningful insights and predictions. From the inputs and outputs of setup decision tree model, thresholds for decision making inside the model are automatically learned to minimize error which in our case is classification loss.

For this analysis, as described later, we used Python programming language. As the dataset used in this study exhibits class imbalance, several methods were explored to overcome this issue. The imbalance comes from the nature of the study, with one control set of observations compared to three for the other output classes (mowing, grazing). In the process of training our Decision Tree model, we tested various approaches to overcome the class imbalance of the data. Initially, we attempted using the Decision Tree classifier’s inherent feature to apply class weights, assigning more weight to the minority class. This was achieved by controlling the ’class_weight’ parameter in the ’scikit-learn’ library implementation of the Decision Tree Classifier. In the model setup, we assigned three times the weight to the Control output class compared to the other two classes. Unfortunately, this adjustment did not lead to improved performance. To overcome this problem, we explored both undersampling and oversampling techniques. Undersampling posed a risk of losing crucial information necessary for effective model learning due to the dataset’s limited size. To address the class imbalance, we employed the SMOTE [ 56 ] oversampling technique from the ’imblearn’ Python library. Given the restricted variety in the control data, obtaining more diverse and substantial data in the future would be advantageous in alleviating the class imbalance issue. We adopted the decision tree implementation from the “scikit-learn” [ 57 ] package and relied on the “pandas” [ 58 ] and “numpy” [ 59 ] libraries for data preprocessing. In addition, for exploratory data analysis in preparation for model training, “ydata_profiling” package [ 60 ] was adopted. Due to the tabular nature of our dataset, we opted for decision tree-based algorithms as they provide good balance between performance and interpretability. These models were used as classifiers, whereby the training phase allows the utility of certain species for segregation of different habitats to be ascertained. During the learning process, as will be described in the sections that follow, we monitored model accuracy, as well as assessed the importance of different features and their gini values for identifying the species that are most relevant for differentiating habitat types.


## Results

We observed variations in biodiversity depending on the management measures adopted at a particular site. In total, we recorded presence of 164 vascular plant species, 31 insect pollinator species, and 61 bird species ( S1 Table ). At 85, 14, and 26 (G), and 115, 21, and 19 (M), the greatest number of plant, pollinator, and bird species was found at the grazed and mowed sites, respectively, while at unmanaged site (C), only 59, 9, and 18 species were recorded.

The greatest differences between the sites were found in the plant species, namely the shrubs such as Cornus mas , Crataegus monogyna , Rosa canina , Prunus spinosa , and Fraxinus ornus , which dominated within the unmanaged area, while in the grazed and mown areas they appeared only sporadically and mainly as young plants. At all sites (especially those under grazing), prevalence of species from the Poaceae family was noted, and Festuca was the predominant plant genus. Maximum vegetation height (MVH) ranged from 12 to 80 cm, while total vegetation cover (TVC) ranged from 10% to 100%. The G sites exhibited the significantly lowest values for both MVH and TVC, whereas the C site recorded the significantly highest values ( Fig 2 ).


### Fig 2. Vegetation height and total vegetation cover on the study sites (M − mowing, C − control, G − grazing).


> **Figure/Table Caption:** *Different lowercase letters indicate significant differences between sites (one-way ANOVA; p < 0.05); Different uppercase letters indicate significant differences between management practices (one-way ANOVA; p < 0.05).

Most of the plants found at all sites belonged to disturbance-tolerant and generalist SBTs, while specialist species and IAS were represented with a small share, approx. 7% and 5%, respectively ( Table 2 ). Greater percentages of natural pioneers were found at managed compared to unmanaged sites.


### Table 2. Relative cover (%) of each social behaviour type (SBT) for plants found within management practices (G–grazed, M–mowed, and C–control).

S–specialists; G–generalists; DT–disturbance-tolerant species; NP–natural pioneers; IAS–invasive alien species.



| SBT | G | M | C |
| --- | --- | --- | --- |
| S | 7.06 | 7.82 | 3.39 |
| G | 14.12 | 25.22 | 27.12 |
| DT | 25.88 | 24.35 | 32.20 |
| NP | 12.94 | 10.43 | 8.47 |
| IAS | 5.88 | 5.22 | 1.69 |


The recorded 32 pollinator species (20 wild bees and 12 hoverflies) consisted of 290 individuals (269 wild bees and 21 hoverflies). The most common wild bee families were Apidae and Megachilidae, while only one species was detected from the family Halictidae. Most of the species had a very low abundance, with 25 species having 10 or fewer individuals, five species having 10 to 30 individuals, and only one species having over 100 individuals.

In total, 46 species of birds were possibly breeding on the surveyed sites, 31 of which were confirmed or probable breeders. Passerines were the dominant group with 33 species. Bird assemblage was dominated by species typically inhabiting forests, woodlands, or shrubs (28 species), while grassland birds were significantly less abundant (six species). Twelve species were present at most study sites, while 13 species were recorded at only one site.

The Shannon-Weaver index for plants was significantly higher at mowed sites than at grazed and unmanaged sites ( Table 3 ). Its values also varied among sites, whereby the lowest value was recorded at the G1 site and the C site (0.96 and 0.97, respectively), while the highest value was associated with the G3 site (1.28). In general, no significant differences in the Shannon-Weaver index for plants were noted between mowed and grazed sites, or for pollinators and birds across any sites, suggesting that there are no consistent differences in diversity within taxa that could potentially be attributed to the adopted management measures.


### Table 3. Mean values of the Shannon-Weaver index for plants, pollinators, and birds at study sites (G–grazed, M–mowed, and C–control).



| Site | Plants |  | Pollinators |  | Birds |  |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | 0.96 b |  | 0.94 a |  | 0.85 a | A |
| G2 | 1.09 ab | AB | 0.44 a | A | 1.91 a |  |
| G3 | 1.28 a |  | 0.93 a |  | 1.76 a |  |
| M1 | 1.19 ab |  | 0.92 a | A | 1.75 a |  |
| M2 | 1.06 ab | A | 0.52 a |  | 1.68 a | A |
| M3 | 1.30 a |  | 1.36 a |  | 1.65 a |  |
| C | 0.97 b | B | 0.70 a | A | 2.00 a | A |


* Different lowercase letters indicate significant differences between sites (one-way ANOVA; p < 0.05); Different uppercase letters indicate significant differences between management practices (one-way ANOVA; p < 0.05)

Our investigation based on the total species diversity findings and the analysis of recorded species by site according to management type revealed that the community similarity among G, M, and C sites is small. Among the investigated groups, birds were found to be the least heterogeneous (with the highest index of community similarity, i.e., above 0.5), while for plants and pollinators this index ranged from 0.25 to 0.5 ( Table 4 ). When similarities at the group level were examined, a clear pattern was established for each group. Specifically, the greatest similarity among plants was noted between G and M, while pollinators were most similar at G and C sites, and M and C emerged as most similar in terms of bird populations. Plant analyses further revealed that at the G and M sites grassland was the predominant floristic structure, while the C site was characterised by forest degradation. According to the findings related to pollinators, community similarity index is uniform across the entire study area.


### Table 4. Community similarity for plants, pollinators, and birds at study sites (G–grazed, M–mowed, and C–control).



|  | Plants | Pollinators | Birds |
| --- | --- | --- | --- |
|  | G | C | G | C | G | C |
| C | 0.26 |  | 0.29 |  | 0.46 |  |
| M | 0.36 | 0.28 | 0.24 | 0.24 | 0.62 | 0.64 |


According to the GLMs, no significant trends can be established for pollinator diversity and habitat parameters. On the other hand, GLM findings related to bird species revealed that their diversity was primarily affected by diversity of plants within the sites and the percentage of trees outside the site boundaries ( Table 5 ).


### Table 5. Results yielded by GLM analysis of the effect of habitat characteristics on the pollinator and bird species diversity within the study area.



|  | Estimated parameter | Standard error | t value | p value |
| --- | --- | --- | --- | --- |
| Diversity of pollinators |  |  |  |  |
| Intercept | 5.52 | 1.33 | 4.16 | 0.000328 *** |
| Distance to the nearest tree (m) | -0.0038 | 0.0019 | -2.01 | 0.055 |
| Trees outside sites | -0.043 | 0.0259 | -1.69 | 0.101 |
| Diversity of birds |  |  |  |  |
| Intercept | -0.72 | 0.66 | -1.08 | 0.29 |
| Trees outside sites (%) | 0.02 | 0.009 | 2.28 | 0.03 * |
| Vegetation height | -0.01 | 0.0076 | -1.67 | 0.11 |
| Plant diversity | 2.10 | 0.50 | 4.15 | 0.00035 *** |


Significance is expressed as

The LDA results facilitated a separation of the three habitat management types. The first axis of the discriminant analysis explained over 95% of the total dispersion, while the combination of the first two axes accounted for 100% of the variability ( Table 6 ). All variables were more closely related to sites managed through mowing. While a small overlap was detected between grazed and mowed sites, it was much broader between mowed and unmanaged sites ( Fig 3 ). It is also worth noting that the unmanaged area was relatively uniform compared to others, as much greater variability can be observed in the results related to both M and G sites. Among the predictor variables, total vegetation cover and diversity of plant species had the highest factor scores on the first axis, and according to this decision tree model was trained only on data related to plants.


### Table 6. LDA results with proportion of dispersion and variable scores on the first two axes.



|  | LD1 | LD2 |
| --- | --- | --- |
| Proportion of total dispersion | 97.18 | 2.82 |
| Maximum vegetation height (VG) | -0.2862 | -0.4852 |
| Total vegetation cover (TVC) | -2.6927 | 0.3609 |
| Diversity of plants (DPl) | 0.4876 | 1.2224 |
| Diversity of pollinators (DPo) | 0.0495 | 0.1797 |
| Diversity of birds (DB) | -0.1617 | -0.5275 |



### Fig 3. Plots of the first two discriminant functions (LD1, LD2) yielded by Linear Discriminant Analysis (LDA).


> **Figure/Table Caption:** M − mowing, C − control, G − grazing. TVC − Total vegetation cover; DPl − Diversity of plants; VG − Maximum vegetation height; DPo − Diversity of pollinators; DB − Diversity of birds.

The decision tree model was trained in a classification setting where the habitat management measure labels were used as the algorithm output and the remaining dataset was used as the input. By conducting post-training analysis, we were able to extract and rank features by their relative importance, allowing us to determine which plant species are most relevant for different habitats. Although several model were trained and used during our experiments—including Random Forest and XGBoost [ 61 ] Gradient Boosted Tree models—Decision Tree Classifier model with maximum tree depth set to 30 proved most useful. While the two ensemble models provided a slight increase in accuracy, we opted for the Decision Tree Classifier as it is fully interpretable and provided good validation accuracy (71%). When applying this model, the data was split into training and validation sets at a standard 80/20 ratio. For all model hyperparameters, a combination of manual tuning and grid search was used to find the most optimal values. Data was not normalised as all tested models performed well when applied to raw data.

According to the obtained findings, Galium verum was the most frequent plant species, as it occurred in 179 of the 224 sample units. The dichotomous branching emanating from this species clearly shows the separation of the G site in relation to the M and C sites ( Fig 4 ). Depending on whether it occurs in a community with the species Dactylis glomerata or Eryngium campestre , the branch is recognised as G or M, respectively. Following D . glomerata , G is characterised by the presence of Veronica arvensis , Taraxacum officinale , Phragmites communis , Rumex acetosa , Crataegus monogyna , Bromus ramossus , Carex caryophyllea , V . verna , and V . vindobonensis . On the other hand, following Eryngium campestre , M is characterised by Falcaria vulgaris , Rubus sp., Fraxinus ornus , Knautia drymeia , Teucrium chamaedrys , Thalictrum elata , and Calamagrostis epigeios . Counter to the bilinear distinction of G and M, C is not recognised as a single strong branch, but rather consists of semi-branches that have emerged mainly from M branches. It is defined by three herbaceous species: Lamium amplexicaule , Salvia austriaca , and Festuca ovina .


### Fig 4. Visualisation of the decision tree model for plant species observed and collected in the Subotica Sands study area.


> **Figure/Table Caption:** Green, purple, and orange colour correspond to grazed, mowed, and control site, respectively. Colour intensity indicates stronger support of the selected branch (management measure) by the included plant species.


## Discussion

Understanding the relationship between biodiversity and management practices can provide valuable insights for improving monitoring strategies, as well as for developing early warning systems and management strategies for In-situ conservation [ 62 – 65 ].

In our study area, the management measures that have been adopted in the last two decades (mowing and grazing) proved to be most significant for plants comparing to pollinators and birds. This is not surprising, given that in grasslands, grazing and trampling prevent secondary succession and the formation of monodominant shrub stands to the detriment of other steppe species [ 66 ]. In our study area, small trees and shrubs ( Cornus mas , Crataegus monogyna , Rosa canina , and Prunus spinosa ) were only recorded as individual juvenile plants. However, as the presence of shrub species is beneficial for pollinators and birds, individual specimens should be preserved in managed areas, as they are not only an important food source for pollinators in spring, but are also a natural component of these habitats. Similar conclusions were reached by other authors based on their experimental studies [ 67 – 69 ]. Available evidence also indicates that cattle grazing creates and maintains an open soil in the sandy grassland, which is an ideal substrate for the formation of wild bee nests, as it warms up quickly in spring and retains heat for a long time. Within the area in focus of the present study, with the shrub species and the plant species that flower in late winter and early spring ( Colchicum bulbocodium subsp. versicolor , Gagea spp., Muscari neglectum , Veronica arvensis , etc.), two conditions for the presence of wild bees are already fulfilled: a suitable place to nest and a food source. Therefore, we can expect a greater number of species (including specialists) to occur within the managed areas over time, especially on the grazed sites.

We also noted that the adopted management measures affected the occurrence of species characteristic of the habitat, especially the plant species. At the grazing sites, we found most of the plant species from the Poaceae family, the genera Festuca , Bromus and Poa in particular. These results may indicate that sheep favour herbs, due to which grazing is beneficial for the proliferation of grasses [ 70 ]. This assertion, if true, could explain the negative impact of grazing on nectar-dependent pollinators, even if it may facilitate restoration and maintenance of natural habitat types. According to Hellström et al. [ 71 ], sheep grazing may be an efficient strategy in the initial stages of restoration, since these animals preferentially feed on leaves and young saplings of trees and shrubs.

Our analyses focusing on insect pollinators showed a similar pattern of presence in relation to management measures and habitat type. Contrary to expectations, the abundance of pollinators, especially hoverflies, was low at all sites. This can be explained primarily by the dominance of Poaceae species in the study area, which are not important either as a food source or as a host for this group. Insect pollinator diversity is strongly linked to the availability and amount of floral resources which are in their foraging range, as well as the composition of floral communities, the shape and size of the fragment, and the availability of nesting sites. In areas with a low share of semi-natural habitats, pollinator abundance in isolated fragments is higher, which indicates that the source of pollen is limited in simpler areas [ 72 ]. As previously noted, habitats with open ground surfaces, such as those found at the studied sites, are optimal for wild bees. The presence of plants from the Asteraceae and Fabaceae families is also considered important for pollinators, as their flowers represent a high-quality resource. Indeed, this has been demonstrated at the mowed sites included in our investigation, where the highest numbers of plant species from these families as well as the highest number of pollinators were recorded. However, some authors have found that having cattle or horses as the main grazers yields better results in terms of plant and pollinator diversity, suggesting that this may be a viable habitat management strategy [ 73 ]. Moreover, the pollinator species that were registered in the study area are very important for the pollination of agricultural crops located in its vicinity [ 74 ].

Compared to plants and pollinators, birds use habitats on a larger spatial scale. We recorded presence of bird communities that are typical of semi-open landscapes dominated by forests and shrubs (forest and shrub generalists). Although the grassland patches may not have been sufficient for establishing a grassland bird community, certain species, such as Coracias garrulus , Lanius collurio , and Saxicola torquata , were identified as potentially benefiting from grassland management due to their foraging habits. Our study highlights the significance of the Subotica Sands landscape for Coracias garrulous , a species that faced population decline in the past [ 75 ]. The mosaic landscapes of Subotica Sands remain among the few sites where this secondary cavity-nesting bird is not completely dependent on artificial nest boxes. Grassland management provides a unique opportunity for focusing on some species of conservation concern, even though management is not the main factor determining bird communities at the grassland level. The presence of species like Alauda arvensis , Anthus campestris , and Coturnix coturnix exclusively in grazed areas suggests that grazing may be more effective than mowing in restoring suitable vegetation structure, emphasizing the importance of adopting grazing as the primary management measure for habitat restoration. As birds are the most sensitive to changes in grassland management strategies [ 11 ], the presence of unique and more specialised species thus confirmed the importance of grazing, suggesting that it should be adopted as the main management measure for the restoration of mosaic habitat.

Although habitat heterogeneity is a mirror of the ancient natural vegetation, today it is a consequence of the long-term agricultural landscape changes. Thus, it is useful for describing spatial and temporal differences for different taxonomic groups from a historical perspective. Our analyses confirmed that some taxonomic groups (plants and pollinators) exhibit similar species structure patterns in differently managed habitats (based on a relatively low community similarity value), concurring with the previously reported findings [ 76 ]. These observations can be ascribed to more rapid changes in unmanaged grasslands, followed by general deterioration of this habitat. As birds are highly sensitive to changes in grasslands, these findings were expected and can also be explained by the landscape changes that began long ago, given that most of the semi-natural grassland areas have been fragmented in the last 50 years [ 29 , 77 , 78 ]. The results yielded by our LDA model further indicate a gradual change in the species structure in Subotica Sands, from unmanaged sites, through mowing, to grazed areas. This model also allowed us to determine that grazed areas are noticeably separated from mown and unmanaged areas. Similar patterns were previously confirmed in other study areas [ 12 , 79 – 81 ], indicating that good habitat management is beneficial for biodiversity, and has the capacity to influence species richness, abundance, and community composition.

Our analyses further revealed that areas that have been under constant human pressure for a long time can be relatively quickly restored with appropriate protection measures. We noted many beneficial effects of such practices, including dominant presence of generalists, disturbance-tolerant plants, and natural pioneers, but also significant occurrence of specialists. The presence of first three SBTs in Subotica Sands in the timeframe of 20 years is attributed to the ploughing performed in 2002, followed by continued grazing and mowing. As pointed out by Kapás et al. [ 82 ], grazing supports the establishment of grassland species on restored sites, which will subsequently serve as dispersal vectors for seeds. Therefore, they will assist plant species establishment by generating disturbances on the surface, and will restrict and/or favour other plant species, as confirmed in our research. Our findings also concur with the view put forward by Littlewood et al. [ 83 ], who argued that, without the help of grazers, it is difficult for specialists to gain space in the dense vegetation dominated by non-specialist grassland species. The small number of specialists and a high percentage of disturbance-tolerant species in unmanaged site compared to managed sites also points towards a general deterioration of grassland species composition in abandoned grasslands and possibly a lack of remnant populations [ 84 – 86 ]. Although specialists are important habitat edificators, extant research suggests that habitat restoration initiatives must primarily consider species with a broad ecological response.

While these outcomes can be extracted from the existing biodiversity databases, as they are usually large repositories of different data types, including different taxa and investigated territory, they are difficult to analyse without extensive support from latest technological tools. With the advent of artificial intelligence and machine learning, these drawbacks have been mitigated, and in this study, we adopted the Decision Tree Machine Learning Model, as we hope that such innovative approaches will soon become the norm in the ecological restoration process and will be used by decision makers in the design of different management strategies. This particular model allows researchers to visualise scientific data and propose explainable relationships between species, which could be further incorporated into management policies. From a conservation perspective, this model was particularly useful in establishing that generalist and disturbance-tolerant species are habitat builders, thus confirming their vital role in the restoration of a particular habitat type. Furthermore, this analysis has shown that, although different species occur at different sites, they all have the same ecological preferences, and are well known and easily recognised in the field. Since woody species were found mostly within unmanaged sites (which in this study correspond to forest-steppes) and specialists were recorded only at individual locations (mainly within managed sites, i.e., restored open grasslands), the decision tree model was appropriate for the analyses, as it allowed us to focus on herbaceous and shrubby species only.


## Conclusions

The present study has confirmed that clear differentiation of grazing areas (in terms of structure and number of species) remains the most important management measure, as it leads to the formation of the desired habitat types (open grass habitats of the Pannonian biogeographical region). We also conclude that the cattle used for habitat management today are an adequate substitute for the former cattle species ( Bos primigenius , Bos taurus ) that colonised the Pannonian Plain together with humans in the Anthropocene. Therefore, modern management measures should follow this practice, i.e., depending on the type of habitat and the desired outcome, focus should be given to measures that are a modern substitute for former natural activities if these are not feasible.


## Supporting information


## Acknowledgments

The authors gratefully acknowledge the support of Sandra Čokić Reh, Tamas Vinko, Otto Szekeres, Ivan Laslo Pajić, and Saša Vujić from Outstanding natural landscape Subotica sands during fieldtrips. We also wish to thank Zsolt Molnár from Centre for Ecological Research, Institute of Ecology and Botany, Vácrátót, Hungary, for his assistance with botany research, and express our gratitude to Klára Szabados from Institute for Nature Conservation of Vojvodina province for her endorsement of this research project.


## Data Availability

All relevant data are within the manuscript and its Supporting Information files.


## Funding Statement

This work was supported by the Ministry of Science, Technological Development and Innovation of the Republic of Serbia [grant number 451-03-66/2024-03/ 200125 & 451-03-65/2024-03/200125]; Provincial Secretariat for Higher Education and Scientific Research,Autonomous Province of Vojvodina [grant number 142-451-3485/2023-01]. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.


# Decision Letter 0


### Tzen-Yuh Chiang


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PONE-D-23-26216[REDACTED_TITLE][REDACTED_VENUE]

Thank you for submitting your manuscript to [REDACTED_VENUE]. After careful consideration, we feel that it has merit but does not fully meet [REDACTED_VENUE]’s publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript by Dec 03 2023 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at [EMAIL_REDACTED] . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pone/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

A rebuttal letter that responds to each point raised by the academic editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'.

A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, please include your updated statement in your cover letter. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

If applicable, we recommend that you deposit your laboratory protocols in protocols.io to enhance the reproducibility of your results. Protocols.io assigns your protocol its own identifier (DOI) so that it can be cited independently in the future. For instructions see: https://journals.plos.org/plosone/s/submission-guidelines#loc-laboratory-protocols . Additionally, [REDACTED_VENUE] offers an option for publishing peer-reviewed Lab Protocol articles, which describe protocols hosted on protocols.io. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols .

We look forward to receiving your revised manuscript.

Journal Requirements:

When submitting your revision, we need you to address these additional requirements.

1. Please ensure that your manuscript meets [REDACTED_VENUE]'s style requirements, including those for file naming. The [REDACTED_VENUE] style templates can be found at

https://journals.plos.org/plosone/s/file?id=wjVg/PLOSOne_formatting_sample_main_body.pdf and

https://journals.plos.org/plosone/s/file?id=ba62/PLOSOne_formatting_sample_title_authors_affiliations.pdf

2. Note from Emily Chenette, Editor in Chief of [REDACTED_VENUE], and Iain Hrynaszkiewicz, Director of Open Research Solutions at PLOS: Did you know that depositing data in a repository is associated with up to a 25% citation advantage ( https://doi.org/10.1371/journal.pone.0230416 )? If you’ve not already done so, consider depositing your raw data in a repository to ensure your work is read, appreciated and cited by the largest possible audience. You’ll also earn an Accessible Data icon on your published paper if you deposit your data in any participating repository ( https://plos.org/open-science/open-data/#accessible-data ).

3. We note that the grant information you provided in the ‘Funding Information’ and ‘Financial Disclosure’ sections do not match.

When you resubmit, please ensure that you provide the correct grant numbers for the awards you received for your study in the ‘Funding Information’ section.

4. Thank you for stating the following financial disclosure:

"This work was supported by the Ministry of Science, Technological Development and Innovation of the Republic of Serbia [grant number 451-03-47/2023-01/200125]; Provincial Secretariat for Higher Education and Scientific Research,Autonomous Province of Vojvodina [grant number 142-451-3161/2022-01]"

Please state what role the funders took in the study. If the funders had no role, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript."

If this statement is not correct you must amend it as needed.

Please include this amended Role of Funder statement in your cover letter; we will change the online submission form on your behalf.

5. We note that you have stated that you will provide repository information for your data at acceptance. Should your manuscript be accepted for publication, we will hold it until you provide the relevant accession numbers or DOIs necessary to access your data. If you wish to make changes to your Data Availability statement, please describe these changes in your cover letter and we will update your Data Availability statement to reflect the information you provide.

6. We note that [Figure 1] in your submission contain [map/satellite] images which may be copyrighted. All PLOS content is published under the Creative Commons Attribution License (CC BY 4.0), which means that the manuscript, images, and Supporting Information files will be freely available online, and any third party is permitted to access, download, copy, distribute, and use these materials in any way, even commercially, with proper attribution. For these reasons, we cannot publish previously copyrighted maps or satellite images created using proprietary data, such as Google software (Google Maps, Street View, and Earth). For more information, see our copyright guidelines: http://journals.plos.org/plosone/s/licenses-and-copyright .

We require you to either (1) present written permission from the copyright holder to publish these figures specifically under the CC BY 4.0 license, or (2) remove the figures from your submission:

a. You may seek permission from the original copyright holder of Figure 1 to publish the content specifically under the CC BY 4.0 license.

We recommend that you contact the original copyright holder with the Content Permission Form ( http://journals.plos.org/plosone/s/file?id=7c09/content-permission-form.pdf ) and the following text:

“I request permission for the open-access journal [REDACTED_VENUE] to publish XXX under the Creative Commons Attribution License (CCAL) CC BY 4.0 ( http://creativecommons.org/licenses/by/4.0/ ). Please be aware that this license allows unrestricted use and distribution, even commercially, by third parties. Please reply and provide explicit written permission to publish XXX under a CC BY license and complete the attached form.”

Please upload the completed Content Permission Form or other proof of granted permissions as an "Other" file with your submission.

In the figure caption of the copyrighted figure, please include the following text: “Reprinted from [ref] under a CC BY license, with permission from [name of publisher], original copyright [original copyright year].”

b. If you are unable to obtain permission from the original copyright holder to publish these figures under the CC BY 4.0 license or if the copyright holder’s requirements are incompatible with the CC BY 4.0 license, please either i) remove the figure or ii) supply a replacement figure that complies with the CC BY 4.0 license. Please check copyright information on all replacement figures and update the figure caption with source information. If applicable, please specify in the figure caption text when a figure is similar but not identical to the original image and is therefore for illustrative purposes only.

The following resources for replacing copyrighted map figures may be helpful:

USGS National Map Viewer (public domain): http://viewer.nationalmap.gov/viewer/

The Gateway to Astronaut Photography of Earth (public domain): http://eol.jsc.nasa.gov/sseop/clickmap/

Maps at the CIA (public domain): https://www.cia.gov/library/publications/the-world-factbook/index.html and https://www.cia.gov/library/publications/cia-maps-publications/index.html

NASA Earth Observatory (public domain): http://earthobservatory.nasa.gov/

Landsat: http://landsat.visibleearth.nasa.gov/

USGS EROS (Earth Resources Observatory and Science (EROS) Center) (public domain): http://eros.usgs.gov/#

Natural Earth (public domain): http://www.naturalearthdata.com/

[Note: HTML markup is below. Please do not edit.]

Reviewer's Responses to Questions

Comments to the Author

1. Is the manuscript technically sound, and do the data support the conclusions?

The manuscript must describe a technically sound piece of scientific research with data that supports the conclusions. Experiments must have been conducted rigorously, with appropriate controls, replication, and sample sizes. The conclusions must be drawn appropriately based on the data presented.

2. Has the statistical analysis been performed appropriately and rigorously?

Reviewer #1: I Don't Know

3. Have the authors made all data underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data—e.g. participant privacy or use of data from a third party—those must be specified.

4. Is the manuscript presented in an intelligible fashion and written in standard English?

[REDACTED_VENUE] does not copyedit accepted manuscripts, so the language in submitted articles must be clear, correct, and unambiguous. Any typographical or grammatical errors should be corrected at revision, so please note any specific errors here.

5. Review Comments to the Author

Please use the space provided to explain your answers to the questions above. You may also include additional comments for the author, including concerns about dual publication, research ethics, or publication ethics. (Please upload your review as an attachment if it exceeds 20,000 characters)

Reviewer #1: This study focuses on the effects of different grassland management types, specifically grazing and mowing compared to control, on the diversity of three different groups: plants, pollinators, and birds. They show differences in the diversity of these three groups in response to management. In my specific comments on the paper I've highlighted places where I think additional methodological details are needed.

Reviewer #2: [REDACTED_TITLE]

This an interesting study presenting the effect of grassland management (mowing and grazing) on different biodiversity taxa. Although the study is valuable, it could be much improved. Some parts of the manuscript are not easy to follow, especially the introduction, due to poor writing. And the discussion section is too lengthy, should be shortened and more focused to the main questions assessed in the study. But the main concern is the sampling design, which is unbalanced (only 1 control site vs. 3 grazing and 3 mowing sites) and this should be acknowledged and dealt with proper statistical analysis in the study.

L81: I recommend changing the sentence to make it clearer. By “initiatives” you refer to the conservation strategies? Something like “these conservation initiatives cover ecosystem services such as biomass production and…”, as you are referring here to the ecosystem services grasslands provide

L84 To what species you are referring to by “as many species are presently threatened”? Of solitary bees?

L83-87 the whole sentence would benefit from some rephrasing

L86. Fix typo, forging should be “foraging”

L167: fix typo, nearest tree (NOT three)

L171-175: treatments could be explained in a more structured and clear way, without mixing information

L186-192: no information on time of the day when pollinator sampling was conducted, please add

L205: I suggest rephrasing, species diversity was "calculated" instead of interpreted.

L249: In the study area is not needed, I suggest to delete that

L250. Please rephrase. Recorded instead of “noted presence”

L253: Please correct. Unmanaged site, singular as there was only one site.

Table 1. Are those numbers mean % across sites? Please specify. Also, would be better if the description of social behaviour types in table legend text follows the order of appearance of the table, starting with S, D, DT, NP and IAS

Table 4. Fix typo, distance to nearest TREE

Fig. 3. IT would help to add the full name of management type in the legend in the figure: Control, Grazing, and Mowing. Also Variat should be replaced by Management.

Discussion could be shortened in order to improve flow and focus on main messages.

6. PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at [EMAIL_REDACTED] . Please note that Supporting Information files do not need this step.

Submitted filename: my comments.docx



Collection date 2024.

I have received the reports of you and two reviewers on the manuscript “[REDACTED_TITLE]”. I am glad to see that manuscript could be reconsidered for publication if revisions were prepared. Following reviewer’s comments strictly, we made certain changes in the manuscript.

The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Land-use data for Figure 1. were obtained from Copernicus Global Land Service ( https://land.copernicus.eu/ ). According to 4.1 Terms of Use of Copernicus Global Land Service: The product(s) described in this document is/are created in the frame of the Copernicus programme of the European Union by the European Environment Agency (product custodian) and is/are owned by the European Union. The product(s) can be used following Copernicus full free and open data policy, which allows the use of the product(s) also for any commercial purpose. Derived products created by end users from the product(s) described in this document are owned by the end users, who have all intellectual rights to the derived products ( https://land.copernicus.eu/ en/technical-library/product-user-manual-for-clc-backbone-raster-only/@@download/file). The sources of the layers used for map creation, including cities, are specified in the caption of Figure 1. Furthermore, the map has not been previously copyrighted to our knowledge.

Together with the revised manuscript, we are sending a list of responses to the comments. We have endeavored to respond to all the points raised. As detailed below, we have checked all the general and specific comments provided by the Referees and have made the necessary changes according to their recommendations.

The authors would like to express their appreciation to the reviewers and editors for their help and useful comments.

Reviewer #1: This study focuses on the effects of different grassland management types, specifically grazing and mowing compared to control, on the diversity of three different groups: plants, pollinators, and birds. They show differences in the diversity of these three groups in response to management. In my specific comments on the paper I've highlighted places where I think additional methodological details are needed.

Line-by-line comments:

Reviewer comment: Line 86: change “forging” to “foraging”

[AUTHOR] et al.: corrected. We accept the Reviewer's remark.

Reviewer comment: Line 124: I’m not sure what is meant by “degradation stadium”

[AUTHOR] et al.: Pruno spinosae-Crataegetum is degradation stadium of Convallario-Quercetum roboris. We rephrased the sentence to provide a clearer explanation.

Reviewer comment: Figure 1: It’s difficult to see the labels in the figure that show where the 3 different treatments are located. Can the figure be edited to make these more readable?

[AUTHOR] et al.: We modified Figure 1 to align with the journal's requirements and enhance its readability.

Reviewer comment: Line 167: The “nearest three” what? Nearest three other sites?

[AUTHOR] et al.: It was our mistake, we should have written “the nearest trees”. We have corrected in our manuscript.

Reviewer comment: Lines 162-170: I would like to see more detail here because I don’t think these methods are clear as currently written. How were the habitats characterized? It sounds like there is some focal habitat that was characterized, as well as a 150 m buffer zone that presumably was also characterized by habitat type. Did the measures of tree/shrub cover determine the characterization of habitat types? How large is the focal study area at each of the sites?

[AUTHOR] et al.: We accept the Reviewer's remark. Throughout the 'Study Area' section, we have made modifications to the text and added an additional table. In this table, we have categorized the habitat types according to our National classification of Republic of Serbia and mark which habitat type corresponds to NATURA 2000 habitat type. This was done to facilitate the identification of habitat types within the research area. Furthermore, we wrote that each sampling site covering an area of 1 hectare.

Reviewer comment: Line 183: I’m not familiar with “social behavior types” for plants. What is this?

[AUTHOR] et al.: Social behavior types (SBT) are defined by the role that a plant species plays within its community. These categories represent how a particular plant is interconnected with its habitat, conveying valuable information about the naturalness of this connection. The presence of these SBTs within a community can provide insights into various aspects, such as the ecological richness of the community, its stability, its natural state, niche occupancy, regenerative potential, and the degree of disturbance, transformation, or deviation from the natural state. According to Borhidi (1995), these categories include specialists (S), generalists (G), disturbance tolerants (DT), natural pioneers (NP), natural competitors (C), indigenous ruderal competitors (RC), and alien competitors and introduced species (AC + I).

We have added the paragraph: In addition, in order to gain insights into community dynamics and ecological characteristics, we employed Social Behavior Types (SBT) for all plant species. SBT categorizes plant species based on their roles in the community and provides valuable information about community richness, stability, naturalness, niche occupancy, and response to disturbances or deviations from the natural state [38].”

Reviewer comment: Lines 190-192: How were the bee identifications conducted, and by whom? The person who did the work should be named, and the taxonomic keys that were used to identify bees should be named and cited. (See Packer et al. 2018. Validating taxonomic identifications in entomological research. Insect Conservation and Diversity 11: 1-12 for more information.)

[AUTHOR] et al.: Thank you for your comment; it was an oversight on our part. The author of this manuscript, Sonja [AUTHOR], was responsible for identifying bee species and Tamara Tot for hoverflies. We have included the taxonomic keys that were used for bee species as well as for hoverflies identification.

Reviewer comment: Lines 234-236: It would be great to see a little more detail about what decision trees are in a general sense and what benefit the authors think they bring to this research.

[AUTHOR] et al.: We added a paragraph in section Materials and methods discussing the general concept and benefits of the decision tree.

Reviewer comment: Lines 260-262: It is not easy to see this point in Figure 2, especially for vegetation height (Fig. 2A). Can the authors revise this sentence to better summarize the figure?

[AUTHOR] et al.: We accept the Reviewer's remark. We have revised the sentence and also made correction on Figure 2.

Reviewer comment: Figure 2: It’s very difficult to tell which parts of the figure the uppercase letters A, B, and C are referring to. Can the authors make this clearer? Are the uppercase letters just pointing out that management type was significant across sites in their ANOVA analysis?

[AUTHOR] et al.: Yes, uppercase letters indicate significant differences between grazing, mowing and control (different management practice). We also have made clearer Figure 2.

Reviewer comment: Lines 282-283: Some of these numbers don’t make sense: “four species with >10 and 103 individuals”

[AUTHOR] et al.: corrected. We have changed the sentence: “Most of the species had a very low abundance, with 25 species having 10 or fewer individuals, five species having 10 to 30 individuals, and only one species having over 100 individuals.”

Reviewer #2: [REDACTED_TITLE].

This an interesting study presenting the effect of grassland management (mowing and grazing) on different biodiversity taxa. Although the study is valuable, it could be much improved. Some parts of the manuscript are not easy to follow, especially the introduction, due to poor writing. And the discussion section is too lengthy, should be shortened and more focused to the main questions assessed in the study. But the main concern is the sampling design, which is unbalanced (only 1 control site vs. 3 grazing and 3 mowing sites) and this should be acknowledged and dealt with proper statistical analysis in the study.

[AUTHOR] et al.: We made some modifications to the Introduction section and condensed the discussion, aligning it more closely with the questions addressed in the study based on the reviewer's suggestions. Additionally, we included a paragraph detailing the statistical analysis employed to address the issue of imbalance in study sites.

Reviewer comment: L81: I recommend changing the sentence to make it clearer. By “initiatives” you refer to the conservation strategies? Something like “these conservation initiatives cover ecosystem services such as biomass production and…”, as you are referring here to the ecosystem services grasslands provide

[AUTHOR] et al.: We have changed the sentence according Reviewer’s recommendation.

Reviewer comment: L84 To what species you are referring to by “as many species are presently threatened”? Of solitary bees

[AUTHOR] et al.: Yes, we meant on solitary bees. We have changed the sentence to make it clearer.

Reviewer comment: L83-87 the whole sentence would benefit from some rephrasing

[AUTHOR] et al.: We have rephrased whole sentence.

Reviewer comment: L86. Fix typo, forging should be “foraging”

[AUTHOR] et al.: corrected

Reviewer comment: L167: fix typo, nearest tree (NOT three)

[AUTHOR] et al.: corrected

Reviewer comment: L171-175: treatments could be explained in a more structured and clear way, without mixing information

[AUTHOR] et al.: We have restructured and clarified the presentation in this paragraph, separating the information more distinctly.

Reviewer comment: L186-192: no information on time of the day when pollinator sampling was conducted, please add

[AUTHOR] et al.: We added information about the time of day and weather conditions during which the transect walks were conducted.

Reviewer comment: L205: I suggest rephrasing, species diversity was "calculated" instead of interpreted.

[AUTHOR] et al.: corrected

Reviewer comment: L249: In the study area is not needed, I suggest to delete that

[AUTHOR] et al.: corrected

Reviewer comment: L250. Please rephrase. Recorded instead of “noted presence”

[AUTHOR] et al.: corrected

Reviewer comment: L253: Please correct. Unmanaged site, singular as there was only one site.

[AUTHOR] et al.: corrected

Reviewer comment: Table 1. Are those numbers mean % across sites? Please specify. Also, would be better if the description of social behaviour types in table legend text follows the order of appearance of the table, starting with S, D, DT, NP and IAS

[AUTHOR] et al.: We accept the Reviewer's remark. We have changed the title of the table to be more specified and have changed legend text follows the order of appearance of the table.

Reviewer comment: Table 4. Fix typo, distance to nearest TREE

[AUTHOR] et al.: corrected

Reviewer comment: Fig. 3. IT would help to add the full name of management type in the legend in the figure: Control, Grazing, and Mowing. Also Variat should be replaced by Management.

[AUTHOR] et al.: In Figure 3 we have added the full name of the management practice and replaced 'Variat' with 'Management' according Reviewer’s suggestion.

Reviewer comment: Discussion could be shortened in order to improve flow and focus on main messages.

[AUTHOR] et al.: We made the Discussion section shortened, focusing on the main messages in our research. We hope that we have successfully conveyed our key findings and insights.

Submitted filename: Response to reviewer comments_Milic et al..docx


# Decision Letter 1


### Tzen-Yuh Chiang


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

[REDACTED_TITLE]

We’re pleased to inform you that your manuscript has been judged scientifically suitable for publication and will be formally accepted for publication once it meets all outstanding technical requirements.

Within one week, you’ll receive an e-mail detailing the required amendments. When these have been addressed, you’ll receive a formal acceptance letter and your manuscript will be scheduled for publication.


If your institution or institutions have a press office, please notify them about your upcoming paper to help maximize its impact. If they’ll be preparing press materials, please inform our press team as soon as possible -- no later than 48 hours after receiving the formal acceptance. Your manuscript will remain under strict press embargo until 2 pm Eastern Time on the date of publication. For more information, please contact [EMAIL_REDACTED] .

Additional Editor Comments (optional):

Reviewer's Responses to Questions

Comments to the Author

1. If the authors have adequately addressed your comments raised in a previous round of review and you feel that this manuscript is now acceptable for publication, you may indicate that here to bypass the “Comments to the Author” section, enter your conflict of interest statement in the “Confidential to Editor” section, and submit your "Accept" recommendation.

Reviewer #1: All comments have been addressed

Reviewer #2: All comments have been addressed

2. Is the manuscript technically sound, and do the data support the conclusions?

The manuscript must describe a technically sound piece of scientific research with data that supports the conclusions. Experiments must have been conducted rigorously, with appropriate controls, replication, and sample sizes. The conclusions must be drawn appropriately based on the data presented.

3. Has the statistical analysis been performed appropriately and rigorously?

4. Have the authors made all data underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data—e.g. participant privacy or use of data from a third party—those must be specified.

Reviewer #1: (No Response)

5. Is the manuscript presented in an intelligible fashion and written in standard English?

[REDACTED_VENUE] does not copyedit accepted manuscripts, so the language in submitted articles must be clear, correct, and unambiguous. Any typographical or grammatical errors should be corrected at revision, so please note any specific errors here.

6. Review Comments to the Author

Please use the space provided to explain your answers to the questions above. You may also include additional comments for the author, including concerns about dual publication, research ethics, or publication ethics. (Please upload your review as an attachment if it exceeds 20,000 characters)

Reviewer #1: The authors have addressed my comments on the original manuscript, and I commend them for their attention to detail in responding to my comments and the comments of the other reviewer.

Reviewer #2: I thank the authors for addressing the comments raised, although I would appreciate that they would have made reference to the specific lines where changes have taken place in the new version of the manuscript. Yet, having the tracked changes version at the end helped.

I think the current manuscript has improved substantially and I recommend it for publication. I particularly appreciate the additional information regarding on the statistical methods used to account for the imbalance study design.

I have only 2 minor comments on the current version:

- Lines 299-302. Please rephrase as current form it's not clear. Something similar to:

“Greatest number of plant, pollinator and bird species was found at the grazed (G) and mowed sites (M) with 85, 14, and 26 species and 115, 21, and 19 species respectively, while at unmanaged… “

- Conclusions. I would suggest to modify slightly the conclusions to strengthen the main findings of the work. What do you mean by “clear differentiation”? Also the role of mowing, in addition to grazing, could be highlighted as for example the highest number of Asteraceae and Fabaceae plant species, together with highest number of pollinators, were recorded in mowed sites.

Lines 651-653 are not very clear, I suggest rephrasing. For instance, when you say “modern management measures should follow this practice…“ which practice do you refer to? grazing with ruminants?

7. PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .


# Acceptance letter


### Tzen-Yuh Chiang


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

I'm pleased to inform you that your manuscript has been deemed suitable for publication in [REDACTED_VENUE]. Congratulations! Your manuscript is now being handed over to our production team.

At this stage, our production department will prepare your paper for publication. This includes ensuring the following:

* All references, tables, and figures are properly cited

* All relevant supporting information is included in the manuscript submission,

* There are no issues that prevent the paper from being properly typeset

If revisions are needed, the production department will contact you directly to resolve them. If no revisions are needed, you will receive an email when the publication date has been set. At this time, we do not offer pre-publication proofs to authors during production of the accepted work. Please keep in mind that we are working through a large volume of accepted articles, so please give us a few weeks to review your paper and let you know the next and final steps.

Lastly, if your institution or institutions have a press office, please let them know about your upcoming paper now to help maximize its impact. If they'll be preparing press materials, please inform our press team within the next 48 hours. Your manuscript will remain under strict press embargo until 2 pm Eastern Time on the date of publication. For more information, please contact [EMAIL_REDACTED] .

If we can help with anything else, please email us at [EMAIL_REDACTED] .

Thank you for submitting your work to [REDACTED_VENUE] and supporting open access.

[REDACTED_VENUE] Editorial Office Staff

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Submitted filename: my comments.docx

Submitted filename: Response to reviewer comments_Milic et al..docx


## Data Availability Statement

All relevant data are within the manuscript and its Supporting Information files.
