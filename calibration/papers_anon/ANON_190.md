# De-Identified Manuscript `ANON_190`
**Title:** [REDACTED FOR BLINDED REVIEW]
**Authors:** [REDACTED FOR BLINDED REVIEW]
**Venue / Year:** [REDACTED FOR BLINDED REVIEW]

## Abstract

Highly pathogenic avian influenza (HPAI) virus presents a serious threat to poultry and public health worldwide, with transmission dynamics shaped by avian migration patterns and environmental conditions. Recent outbreaks in the Philippines highlight the urgent need for effective control measures. While previous studies have shown the importance of waterfowl‐to‐poultry transmission and farm‐to‐farm spread, the spillover risk to local avian species remains underexplored. This study aimed to examine H5N1‐HPAI outbreaks in poultry in relation to environmental factors and local avian species in the Philippines. We applied a two‐step ecological niche modelling approach using maximum entropy algorithms. First, environmental variables from remote sensing images were used to predict the distribution of 10 common avian species based on citizen science data from the eBird platform. Next, these avian distribution data were combined with environmental variables to create a risk map for H5N1‐HPAI outbreaks in the Philippines. The H5N1‐HPAI risk model demonstrated strong predictive performance, with an AUCROC value of 0.936 ± 0.026. Key factors contributing to predicted H5N1‐HPAI risk included precipitation levels, population density, and avian species such as the Eurasian Tree Sparrow and Zebra Dove. The higher risk of spillover for the two local avian species may be due to their shared similar environmental signatures with outbreak poultries. The risk map highlighted Metro Manila and Central Luzon as high‐risk regions of H5N1‐HPAI. This study identified the main clusters and environmental factors associated with avian influenza outbreaks in poultry in the Philippines. Additionally, the transmission risk may threaten the local avian population.

Keywords: avian influenza virus, eBird, remote sensing, Maxent


## Key Points

The integration of eBird and satellite remote sensing data enhances models for avian distributions and H5N1 cluster detection

Precipitation displayed a nonlinear relationship with the risk of H5N1 transmission in poultry

The Eurasian Tree Sparrow and Zebra Dove present a higher spillover risk associated with H5N1‐HPAI outbreaks in the Philippines


## 1. Introduction

The avian influenza, caused by influenza type A viruses, is a highly transmissible infection that affects both domestic and wild bird populations globally. Wild birds, particularly waterfowl, serve as natural reservoirs for these viruses, facilitating transmission to domestic poultry and, on occasion, other animals, including humans (Blagodatski et al., 2021 ). The virus spreads primarily through fecal and respiratory secretions, although direct transmission from wild birds to other animals is also possible (Yamaji et al., 2020 ). Influenza type A viruses are characterized by two surface glycoproteins: hemagglutinin (HA) and neuraminidase (NA). HA is responsible for virus attachment to host cells via sialic acid linkages, initiating infection, while NA cleaves these linkages to release newly formed viruses (Kosik & Yewdell, 2019 ). These glycoproteins are classified into 18 HA (H1‐H18) and 9 NA (N1‐N9) subtypes, with additional subtypes (H17, H18, N10, and N11) found exclusively in bats (Tong et al., 2012 ; Tong et al., 2013 ). Among these, the H5 subtype has been responsible for numerous outbreaks in both wild and domesticated birds globally (Harfoot & Webby, 2017 ), including the H5N8 (clade 2.3.4.4b) and H5N1 (clade 2.3.2.1c) viruses, which spread across Eurasia, the Middle East, and Africa in 2014 (Kwon et al., 2016 ; Shittu et al., 2017 ). New variants such as H5N8 (clade 2.3.4.4c) have emerged, spreading from South Korea to Eurasia, Africa, and North America. It reassorted with Low Pathogenic Avian Influenza (LPAI) viruses, giving rise to H5N2, which circulated in the United States (Bevins et al., 2016 ; Dargatz et al., 2016 ). By 2020, H5N1 had become globally predominant (Cui, Shi et al., 2022 ; Cui, Zeng et al., 2022 ; Engelsma et al., 2022 ; Lewis et al., 2021 ; Tian et al., 2023 ). While avian influenza viruses can be classified based on their HA and NA subtypes, infections in birds are further distinguished by their pathogenicity: low pathogenicity avian influenza (LPAI) or highly pathogenic avian influenza (HPAI). Pathogenicity is determined by the intravenous pathogenicity index (IVPI) (Liu et al., 2017 , 2021). In Southeast Asia, H5N1‐HPAI has been endemic in several countries, with Indonesia reporting the highest number of human cases (Henning et al., 2019 ; Rehman et al., 2022 ). In the past few decades, H5N1‐HPAI outbreaks have been recorded in Indonesian poultry farms and livestock markets and Thailand, Vietnam, and the Philippines (Karo‐Karo et al., 2022 ; Keawcharoen et al., 2011 ; Nguyen et al., 2020 ; Salvador et al., 2020 ; Tiensin et al., 2005 ). Although studies have focused on waterfowl as primary carriers, the role of local bird species in HPAI transmission, particularly through spillover, has received less attention.

HPAI transmission is influenced by various factors, including bird migration and environmental conditions. Species such as wild geese and swans have been identified as major sources of HPAI spread, particularly through migration across the Pacific and Atlantic Rims (Hill et al., 2022 ; Yoo et al., 2022 ). Other species, such as Columbidae and Passerines, may also play a role in transmission, with HPAI viruses being isolated from species like the Eurasian tree sparrow and rock pigeon (Ellis et al., 2004 ). House sparrows have shown varying susceptibility, with more recent isolates causing high mortality but no transmission to contact birds. Pigeons have generally been resistant, though high concentrations of the virus can cause infrequent morbidity and mortality (Brown et al., 2009 ; Klopfleisch et al., 2006 ). Environmental factors, including population density, temperature, crop densities, and land cover (e.g., wetlands), further contribute to HPAI transmission dynamics (Hubbard et al., 2023 ; Islam et al., 2023 ; Min & Yoo, 2023 ; Morin et al., 2018 ). While much attention has been focused on wild bird transmission, farm‐to‐farm transmission, often facilitated by contaminated equipment or human activity, also plays a significant role (Rossi et al., 2017 ) (Figure 1 ).


### Figure 1.


> **Figure/Table Caption:** Overview ofH5N1‐HPAI transmission.

The intersection of human activity, industrial agriculture, and disease dynamics underscores the importance of examining the political economy of agribusiness, which significantly influences the spatial distribution of large‐scale poultry operations—often situated in areas with dense human populations. The Structural One Health framework offers a critical lens through which to investigate the root causes of disease emergence, particularly in regions where industrial farming is heavily concentrated. By integrating perspectives from ecology, political economy, and epidemiology, this framework addresses the broader social and structural determinants of epizootic spillover, thereby advancing a more comprehensive understanding of zoonotic disease risk and its prevention (Wallace, 2009 ; Wallace et al., 2015 ).

In the Philippines, the 2017 outbreaks of H5N6 in poultry farms in Pampanga and Nueva Ecija caused significant economic losses (Salvador et al., 2020 ). The initial cases of avian influenza, H5N6 strain was reported in commercial poultry farms in barangays San Carlos and Santa Rita, San Luis, Pampanga, and spread to Nueva Ecija within a week. By November 12, a second wave emerged in Cabiao, Nueva Ecija. A total of 23 farms in both provinces were affected from July to November 2017, including 16 farms in Pampanga and 7 in Nueva Ecija. The outbreak impacted various farm types, including layer chicken, duck, and quail farms (Salvador et al., 2020 ; Silvano, 2023 ). Further outbreaks in January 2022 highlighted the ongoing risk to the poultry industry, despite the absence of human infections in the country. Hence, the Department of Agriculture (DA) has issued Memorandum Circular No. 5, regulating the movement of domestic and wild birds and poultry products during the avian influenza surveillance period (DA‐AFID, 2022 ; Department of Agriculture, 2022 ; Montemayor, 2023 ; WHO, 2023 ). Given the geographic and ecological diversity of the Philippines, understanding the environmental drivers of HPAI outbreaks is essential for predicting high‐risk areas and implementing effective control measures.

This study aims to identify key environmental factors and local avian species associated with H5N1‐HPAI outbreaks in the Philippines. By using ecological niche modeling (ENM) with maximum entropy (MaxEnt) algorithms (Phillips et al., 2004 ), this research integrates environmental covariates from satellite remote sensing with avian species data from the citizen science platform eBird. The algorithms have been applied in various ecological studies, including those predicting the distribution of disease vectors such as Haemagogus janthinomys , implicated in yellow fever and Mayaro virus transmission in South America (Celone et al., 2022 ). They have also been used to determine the geographic distribution of pathogens such as the human sporotrichosis agent in Venezuela (Barreto et al., 2021 ), and construct ENM for Bacillus cereus Group Isolates harboring homologues of the pXO1 Anthrax Toxin Genes (Deka et al., 2022 ).This approach will generate risk maps for H5N1‐HPAI outbreaks, providing valuable insights into potential transmission hotspots. These findings are expected to inform disease management strategies, contributing to the protection of both the poultry industry and public health in the Philippines (Alders et al., 2014 ).


## 2. Materials and Methods


### 2.1. Hotspot Detection of H5N1‐HPAI Poultry Outbreak

We utilized the SaTScanTM 10.1 space‐time permutation method to detect spatial and temporal clusters of H5N1‐HPAI outbreaks in the Philippines. This method analyses case data with spatial and temporal information, detecting clusters by comparing observed case frequencies to expected frequencies while accounting for spatial and temporal independence. It combines spatial and temporal aspects to identify regions with significantly higher case proportions during specific time intervals (Kulldorff, 2022 ; Kulldorff et al., 2005 ).

We applied Kulldorff's method to leverage space‐time permutation scan statistics to identify the H5N1‐HPAI hotspot locations in the Philippines (Kulldorff et al., 2005 ).


### 2.2. Multi‐Distance Spatial Cluster Analysis of H5N1‐HPAI Clusters

To explore the spatial dynamic patterns of H5N1‐HPAI poultry outbreaks, a multi‐distance spatial cluster analysis using Ripley's K function was conducted. The analysis was performed using the H5N1‐HPAI outbreak poultries within the three clusters and two regions (Luzon and Mindanao), where each poultry was geocoded into an XY point. A total of 20 distance bands were selected to examine the clustering at various spatial scales. Confidence envelopes were computed using 999 permutations to ensure robust statistical significance. The study area was defined using the minimum enclosing rectangle method, with no additional boundary correction methods applied. This approach enabled the revelation of spatial dynamics of outbreaks and the evaluation of whether the observed distribution deviated from complete spatial randomness (CSR).


### 2.3. Ecological Niche Modelling Procedure

Ecological niche modelling (ENM) techniques are invaluable for predicting species distributions and disease spread, contributing significantly to both ecosystem and disease prediction (Coro, 2020 ; Escobar, 2020 ; Sara M. Melo‐Merino & Andrés Lira‐Noriega, 2020 ). In this study, we implemented the widely recognized MaxEnt machine learning algorithm. We executed a two‐step ENM procedure to forecast potential avian spatial distributions at the first stage and to construct an H5N1‐HPAI risk map utilizing presence‐only data at the second stage (Figure 2 ).


#### Figure 2.


> **Figure/Table Caption:** Conceptual framework for MaxEnt modelling.

To train and evaluate the MaxEnt model, we randomly partitioned the unique occurrence cases of avian species and H5N1‐HPAI into an 80% training data set and a 20% testing data set. Key parameters were set, including a regularized multiplier of 1, a maximum of 10,000 background points, 10 replicates, and a maximum of 500 iterations. A convergence threshold of 0.00001 was applied to ensure model stability.

For feature selection and model validation, we adopted permutation importance measure to assess variable importance in the final model. We evaluated model performance using the area under the receiver operating characteristic curve (AUC ROC ). We employed a backward stepwise elimination approach to iteratively remove covariates with the lowest percent contribution to the models until all remaining covariates reached a percent contribution threshold of ≥1%. We evaluated model performance using the area under the receiver operating characteristic curve (AUC ROC ). The modelling procedure was carried out by MaxEnt 3.4.4 ( Steven J. Phillips ). All the covariates and model outputs were visualized using ArcGIS Pro 3.2.1 (Esri, Redlands, CA, USA).


## 3. Data


### 3.1. Geographic Location and Demographics of the Philippines

The Philippines, located in Southeast Asia, encompasses a vast archipelago between 12.8797°N latitude and 121.7740°E longitude (Figure 3a ). The full names of each province are listed in Figure S1 in Supporting Information S1 . Spanning approximately 300,000 km 2 , the country comprises more than 7,600 islands, with a population of more than 100 million in 82 provinces (Authority, 1991 , 2021 (NAMRIA) 2017). The nation's tropical maritime climate features high temperatures, high humidity, and frequent rainfall. Annual temperatures average 26.6°C, with minimal regional variation. Baguio, at a 1,500‐m elevation, experiences an annual mean temperature of 18.3°C, resembling temperate climates. Humidity levels fluctuate between 71% in March and 85% in September. Rainfall ranges from 965 to 4,064 mm annually, with distinct rainy (June‐November) and dry (December‐May) seasons. Typhoons originating in the Pacific Ocean heavily influence rainfall patterns. However, the southern Philippines is often spared from these storms, fostering favorable conditions for agriculture and industrial development (Department of Science and Technology, 2024 ).


#### Figure 3.


> **Figure/Table Caption:** Geographic overview and avian observation locations in the Philippines. (a) Philippine Archipelago Location and Administrative Boundaries, (b) The distribution of 10 common avian species locations.

The Philippine provincial administrative boundary was obtained from the Humanitarian Data Exchange (HDX), managed by the Centre for Humanitarian Data of the United Nations Office for the Coordination of Humanitarian Affairs (OCHA) (Figure A) (HDX, 2023 ). A population density data set provided population density per grid‐cell estimations, with a spatial resolution of 30 arc s (approximately 1 km at the equator) (Figure S2 in Supporting Information S1 ). This data set is sourced from the WorldPop project, a renowned demographic and spatial population data provider. The units represent the number of people per square kilometer, derived from country totals adjusted to align with the official United Nations population estimates prepared by the Population Division of the Department of Economic and Social Affairs of the United Nations Secretariat (WorldPop, 2020 ).


### 3.2. Avian Observations, Poultry Density, and H5N1‐HPAI Poultry Outbreak Data

We gathered avian species data from the Global Biodiversity Information Facility (GBIF)‐EOD–eBird Observation data, 2010–2022 (GBIF, 2023 ). This data set includes precise coordinates and corresponding dates of 10 common avian species observations, ensuring a comprehensive representation of the avifauna in the Philippines (Figure 3b ). eBird, a citizen‐science project operated by the Cornell Lab of Ornithology and the National Audubon Society, not only records and quantifies bird observations, but also provides valuable insights into avian habitat preferences and population dynamics. Operating within a robust scientific framework, eBird enables global bird enthusiasts and experts to collaboratively collect checklists (eBird, 2022 ). The data set from eBird comprises more than 700 hundred avian species. For our study, we selected the 10 avian species with the highest number of observations. Wherein in our final model Eurasian Tree Sparrow and Zebra dove among these 10 common avian species deemed to have an impact in our final model.

Poultry density data for ducks and chickens was obtained from the Harvard Dataverse. The data set provides the global distribution of chickens and ducks in 2015, expressed as the total number of chickens per pixel (at a spatial resolution of 5 arc‐minutes, approximately 10 km) based on the Gridded Livestock of the World database (v4). The poultry density data were processed in ArcGIS Pro to ensure spatial consistency with other input layers. Specifically, the data were reprojected to the World Geodetic System (WGS) 84/UTM Zone 51N (Luzon) to match the coordinate reference system used for all other raster data sets. Subsequently, the data were resampled to a resolution of 1 × 1 km 2 using bilinear interpolation to align with the final spatial resolution. (Gilbert, Cinardi et al., 2022a , 2022b ) (Figure S3 in Supporting Information S1 ).

We obtained H5N1‐HPAI poultry outbreak data in the Philippines for 2022–2023 from the Emergency Prevention System Global Animal Disease Information System (EMPRES‐i+) of the Food and Agriculture Organization (FAO) of the United Nations (FAO, 2023 ). The data set comprises confirmed cases of avian influenza and their corresponding geo‐graphic coordinates. Initially, the data set encompassed a total of n = 303 avian influenza outbreak reports, with H5N1‐HPAI cases constituting the majority. After eliminating duplicate coordinates from the same farms, the refined data set contained n = 188 unique H5N1‐HPAI reports (Table S1 in Supporting Information S1 ).


### 3.3. Satellite Remotely Sensed Environmental Parameters

We collected a diverse set of monthly environmental covariates from 2010 to 2021, including precipitation data from the Climate Hazards Group InfraRed Precipitation with Station (CHIRPS); land surface temperature (LST) and normalized difference vegetation index (NDVI) from the Moderate Resolution Imaging Spectroradiometer (MODIS) (Table S1 in Supporting Information S1 ). The majority of LCLU in the Philippines is tree‐based cover (72.87%), followed by grassland (8.44%) and cropland (8.2%) (Figure S4 and Table S2 in Supporting Information S1 ). Detailed environmental parameters are listed in the supplementary materials (Tables S1, S2, and Figures S4–S7 in Supporting Information S1 ). All the monthly historical climate indexes were summarized using 2010–2021 data to fit the ecological niche model's analytical framework. A total of 38 covariates were incorporated into each of the 10 avian species distribution models in the first stage. The distribution maps of 10 avian species were added to the H5N1‐HPAI risk mapping, resulting in a total of 48 covariates. All raster layers were reprojected to the WGS 84/UTM Zone Luzon 51 using ArcGIS Pro 3.4 (ESRI, Redland, CA). To ensure consistency across data sets, all layers were resampled to a uniform spatial resolution of 1 × 1 km 2 using the bilinear interpolation method. This approach maintained spatial accuracy while minimizing distortions in the environmental covariates used for analysis.


## 4. Results


### 4.1. Ecological Niche Modelling of Avian Species in the Philippine Archipelago

More than 700 avian species were identified in the Philippines from 2010 to 2022. Among these, the 10 species with the most located occurrences were included in this study. Notably, the Eurasian Tree Sparrow was the most prevalent species, with 4,950 occurrences, followed closely by the Yellow‐vented Bulbul, with 4,671 occurrences (Table S3 in Supporting Information S1 ). Other notable species included the Collared Kingfisher, Olive‐backed Sunbird, Zebra Dove, Brown Shrike, Philippine Pied‐Fantail, Pacific Swallow, Large‐billed Crow, and Little Egret. Utilizing the occurrence data from these 10 avian species, we conducted ENM using environmental covariates to predict the distribution of each species across the Philippines.

Our analysis highlights a slight difference in the avian distribution across the study area. We found an elevated probability of these avian species in the National Capital Region (NCR)‐Metro Manila area, encompassing the adjacent provinces Pampanga and Bulacan. We observed significant avian concentrations in parts of Pangasinan, Tarlac, and Zambales in Central Luzon and Cavite, Laguna, Batangas, Quezon, Rizal, and Palawan in Southern Luzon (Figures 4 and S10 in Supporting Information S1 ). Notably, we predicted that avian species such as the Large‐billed Crow, Olive‐backed Sunbird, and Yellow‐vented Bulbul would be more widely distributed across the Philippine Islands, including provinces in Visayas and Mindanao, compared to other species (Figures S10d and S10f in Supporting Information S1 ). Additionally, Eurasian Tree Sparrow and Zebra dove are the two avian species to have more impact in the H5N1‐HPAI risk model (Figure 4 ).


#### Figure 4.


> **Figure/Table Caption:** Predicted spatial distribution patterns of avian species of importance in H5N1‐HPAI risk model. (a) Eurasian Tree Sparrow distribution across the Philppines (b) Eurasian Tree Sparrow distribution in central luzon, NCR and adjacent provinces. (c) Zebra Dove distribution across the Philppines (d) Zebra Dove distribution in central luzon, NCR and adjacent provinces.

We evaluated the model's performance using AUC ROC. Strong predictive accuracies across avian species were indicated with AUC ROC scores ranging from 0.759 to 0.820. The Philippine Pied‐Fantail exhibited the highest accuracy (0.820 ± 0.011), closely followed by the Little Egret (0.812 ± 0.022) and Zebra Dove (0.811 ± 0.017) (Figure S8 and Table S4 in Supporting Information S1 ). Subsequently, a permutation importance analysis revealed five key environmental covariates significantly influencing avian distribution patterns. Notably, NDVI (in July and August), population density, and precipitation (in March and June) affected nine of the species, emphasizing the crucial roles of these factors in shaping avian habitat preferences and distributions (Table 1 and Table S5 in Supporting Information S1 ).


#### Table 1.

Important Environmental Covariates for Avian Species Distribution



| Environmental covariates | No. of avian species |
| --- | --- |
| Vegetation Index in July | 10 |
| Vegetation Index in August | 10 |
| Population Density | 10 |
| Precipitation in March | 9 |
| Precipitation in June | 9 |



### 4.2. H5N1‐HPAI Disease Distribution in Poultries and Risk Map in the Philippines

The H5N1‐HPAI poultry outbreaks were predominantly concentrated in the central Luzon region, such as Pampanga and the adjacent provinces in the Northern region (Benguet, Isabela, Kalinga, Ilocos Sur, Ilocos Norte, and Cagayan), Manila City, and Southern Luzon (Laguna, Rizal, Quezon, Batangas, and Camarines Sur). Moreover, the disease was identified in Capiz, a province in the Visayas, and several provinces in Mindanao, such as Cotabato, Maguindanao, Sultan Kudarat, South Cotabato, and Davao Del Sur (Figure 5a ).


#### Figure 5.


> **Figure/Table Caption:** H5N1‐HPAI distribution across poultries in the Philippines. (a) Hotspot analysis across the Philippines (b) Three significant clusters of H5N1‐HPAI central luzon, NCR and adjacent provinces. (c) ENM risk map of the whole Philippines. (d) Highest predicted ENM risk concentration of H5N1‐HPAI in the Philippines.

We used space‐time permutation to detect space‐time H5N1‐HPAI clusters in the study area. The first cluster was centered at 14.601°N, 120.996°E and spanned 43.41 square kilometers, including Metro Manila, extending to Bulacan, Rizal, Cavite, and Laguna (1 February 2023, to 7 March 2023) ( p < 0.001). Cluster 2, positioned at 15.67°N, 120.780°E, covered 28.51 square kilometers and reached parts of the Pangasinan, Tarlac, and Nueva Ecija provinces (2 March 2022, to 19 April 2022) ( p < 0.001). Cluster 3, located at 15.287°N, 120.860°E, encompassed 21.50 square kilometers, including parts of the Pampanga, Tarlac, Nueva Ecija, and Bulacan provinces. This cluster displayed significant clustering between 20 July 2022, and 30 August 2022 ( p < 0.001) (Figures S9a and S9b, Table S6 in Supporting Information S1 ).

The final model highlighted Metro Manila and its neighboring provinces in northern Luzon, including Bulacan, Pampanga, Nueva Ecija, Pangasinan, and southern Luzon, such as Cavite, Rizal, and Laguna, as having a heightened risk of H5N1‐HPAI transmission (Figures S9c and S9d in Supporting Information S1 ). Additionally, elevated risks of H5N1‐HPAI were identified in the northern, central, southern Luzon regions. This encompassed Ilocos Norte, Abra, Ilocos Sur, La Union, Zambales, Bataan, Batangas, Camarines Sur, and Albay. Province of Iloilo and southern Mindanao provinces, such as Bukidnon, Sultan Kudarat, Maguindanao, Cotabato, South Cotabato, and Davao Del Norte, demonstrated a moderate disease transmission risk among poultry populations (Figures S9c and S9d in Supporting Information S1 ).

Ripley's K analysis was used to assess the spatial distribution patterns of H5N1‐HPAI cases within the identified clusters, revealing distinct patterns of clustering and randomness. For cluster 1, the observed K function consistently exceeded the expected K function and the confidence envelopes, indicating significant clustering of H5N1‐HPAI cases (Figure S9a in Supporting Information S1 ). In contrast, cluster 2 and cluster 3 exhibited cluster pattern close to complete spatial randomness (Figures S9b and S9c in Supporting Information S1 ). The Luzon region exhibited a significant clustering pattern, while the spatial pattern in the Mindanao region appeared to be close to complete spatial randomness. (Figures S9d and S9e in Supporting Information S1 ). These results highlight the varying spatial dynamic patterns of H5N1‐HPAI cases across different regions.

We performed an analysis of variable contribution and permutation importance to evaluate the complex interplay of environmental covariates in influencing the H5N1‐HPAI distribution in the Philippines. Precipitation in December demonstrated a very important role in the spatial distribution of H5N1‐HPAI. This was followed by the spatial distributions of the Eurasian Tree Sparrow and Zebra Dove. Furthermore, population density and precipitation in June also influenced H5N1‐HPAI risk (Table 2 ).


#### Table 2.

Important Environmental Covariates in H5N1‐HPAI Risk Modelling Based on MaxEnt Model Permutation Importance



| Variable | Permutation importance |
| --- | --- |
| Precipitation in December | 19.9 |
| Eurarsian Tree Sparrow | 18.1 |
| Zebra Dove | 12 |
| Population Density | 5.7 |
| Precipitation in June | 4.7 |


Our evaluation of the H5N1‐HPAI risk model using AUC ROC demonstrates robust predictive accuracy, with an AUC ROC of 0.936 ± 0.026. This indicates good model performance of the H5N1‐HPAI transmission risk (Figure 6a ). We observed an inverse correlation between precipitation levels in December and June, population density, and the risk of H5N1‐HPAI transmission (Figures 6b, 6e , and 6f ). In contrast, we identified a positive correlation between the presence of the Eurasian Tree Sparrow, Zebra Dove, and precipitation levels in June in response to H5N1‐HPAI outbreak (Figures 6d and 6e ). This suggests that precipitation patterns and the presence of the Zebra Dove and Eurasian Tree Sparrow potentially associated with H5N1 outbreaks.


#### Figure 6.


> **Figure/Table Caption:** H5N1‐HPAI model performance and important environmental covariates. (a) AUCROC, (b) Precipitation in December, (c) Response of H5N1‐HPAI to Eurasian Tree Sparrow, (d) Response of H5N1‐HPAI to Zebra Dove, (e) Population Density, and (f) Precipitation in June.

Furthermore, our findings highlight the potential spillover risk to local avian populations warrants further investigation. The association of Eurasian Tree Sparrows and Zebra Doves with outbreak locations suggests that these species may pose a higher risk of spillover or act as mechanical vectors for H5N1. This highlights the need for further research into their role in the disease's ecology.


## 5. Discussion

Our study aimed to identify the H5N1 poultry outbreak hotspots and important local avian species and environmental covariates of avian influenza transmission through a two‐step ENM approach in the Philippines. The Maxent model predicted the spatial distribution patterns of the dominant avian species in the Philippines based on various environmental covariates. The analysis revealed elevated concentrations of these avian species in the Metro Manila area and adjacent provinces, with significant distributions in other provinces as well. An evaluation using AUC ROC showed good predictive accuracies across avian species, with NDVI values in August and June and precipitation in June and March emerging as significant contributors to avian distribution patterns. H5N1‐HPAI poultry outbreaks predominantly in central Luzon, with significant clusters identified in various geographical locations. Evaluation of the complex interplay of environmental covariates and avian species on the H5N1‐HPAI distribution highlighted the significant role of precipitation in December, population density, and Zebra Dove presence.

Several significant H5N1‐HPAI outbreaks have been recorded in Southeast Asia, posing considerable challenges to both the poultry industry and public health. The introduction of H5N1 to Vietnam in 2003 resulted in multiple poultry outbreaks and established endemicity, with significant human infections reported between 2004 and 2005 (Li et al., 2004 ; Smith et al., 2006 ; Wang et al., 2008 ). Despite vaccination campaigns and surveillance efforts that temporarily halted the viral spread in 2006, intermittent poultry and human outbreaks were recorded in 2007 (Gutierrez et al., 2009 ; Wan et al., 2008 ). In March 2024, Vietnam confirmed its first human death from H5N1 (News, 2024 ). Similarly, Indonesia faced numerous human infections and endemicity on several islands in 2005 (Butler, 2006 ; Kandun et al., 2006 ). In 2023, the country raised H5N1‐HPAI 2.3.4.4b awareness following a case on a poultry farm in South Kalimantan (Piri, 2023 ). Additionally, Cambodia and Laos experienced sporadic outbreaks, with some human cases reported (Boltz et al., 2010 ; Desvaux et al., 2006 ; Ly et al., 2007 ; Vong et al., 2006 ). In January 2024, Cambodia recorded two confirmed cases of H5N1 (WHO, 2024 ). Likewise, the Philippines has implemented strict measures since a viral reemergence in 2022 (Lagare, 2024 ). Overall, these countries in Southeast Asia have faced challenges in restricting H5N1, highlighting the importance of ongoing surveillance and risk awareness measures.

Previous studies have underscored the significance of environmental factors like precipitation, vegetation index, temperature, and land cover in avian influenza transmission dynamics (Ferenczi et al., 2021 ; Guerrini et al., 2014 ; Huang et al., 2021 ; Islam et al., 2023 ; Ruiz et al., 2021 ). While rainfall's role in avian influenza virus dynamics is typically considered less significant in the northern hemisphere, some studies have shown its influence on AIV prevalence in both wild and domestic birds (East et al., 2008 ; Hu et al., 2015 ; Si et al., 2013 ). A study in Australia suggests a correlation between avian influenza virus (AIV) outbreaks in poultry and regional rainfall patterns since 1970. This is particularly evident in the Murray‐Darling basin, where peak AIV risk is observed 2 years after periods of high rainfall, likely due to increased waterbird breeding rates and subsequent aggregation near permanent water bodies during drier periods (Ferenczi et al., 2021 ). Similarly, our study found that precipitation was the most significant environmental variable influencing H5N1‐HPAI outbreaks in the Philippines. Vegetation index, land cover, and land surface temperature also contributed to our model's performance, albeit to a lesser extent than precipitation (Table S7 in Supporting Information S1 ). Furthermore, population density emerged as another important factor affecting model performance, consistent with findings from studies on H5N1‐HPAI risk factors in Indonesia and environmentally driven zoonoses (Loth et al., 2011 ; Proboste et al., 2022 ).

Avian abundance plays a crucial role in influencing H5N1‐HPAI transmission, as evidenced by several analyses of avian influenza dynamics emphasizing the significance of migratory bird routes and environmental conditions (Charostad et al., 2023 ; Yang et al., 2023 ). Additionally, previous studies have underscored the crucial role of wild birds, especially migratory species, as vectors capable of disseminating the virus over extensive distances, revealing a direct correlation between migratory routes and H5N1 dispersal patterns (Martelli et al., 2023 ; Tian et al., 2015 ). These insights are supported by research implicating specific wild bird species, such as tufted ducks, Eurasian pochards, and mallards, in the expansion of H5N1‐HPAI outbreaks across Asia, the Middle East, Europe, and Africa. Some species excrete significantly more viruses than others, suggesting their potential role as long‐distance vectors or viral sentinels (Sonnberg et al., 2013 ).

One study in Thailand revealed that a significant number of wild bird species, including little grebe ( Tachybaptus ruficollis ), open‐bill stork ( Anastomus oscitans ), tree sparrow ( Passer montanus ), and brown‐headed gull ( Larus brunnicephalus ), were infected with H5N1. Some studies suggesting a positive association between the presence of infected wild birds and poultry outbreaks (Keawcharoen et al., 2008 ; Songserm et al., 2006 ; Sonnberg et al., 2013 ; Uchida et al., 2008 ). In Vietnam, ducks and wild waterfowl birds are key contributors to H5N1 and H5N6 transmission, particularly in southern and central regions (Nguyen et al., 2023 ). Similarly, in Indonesia, unrestricted interaction between free‐range birds and migratory species has been implicated in the spread of H5N1 (Rehman et al., 2022 ). Poultry density and farm‐to‐farm transmission play crucial roles in the spread of avian influenza. High‐density poultry farming can facilitate the rapid spread of the virus within and between farms through fomites (Rossi et al., 2017 ).

In this context, the occurrence of HPAI outbreaks in large‐scale poultry farms is closely linked to the economic geographies of agribusiness and global finance—what Wallace aptly describes as “big farms make big flu.” These industrial farms, frequently situated in densely populated or economically strategic areas, function as hubs for disease transmission, illustrating how structural factors—such as the political economy and the organization of industrial agriculture—contribute to the emergence and spread of zoonotic diseases (Wallace, 2016 ).The Structural One Health framework offers a compelling analytical lens for understanding these dynamics. In contrast to conventional One Health approaches, which often prioritize biological and veterinary mechanisms of disease transmission, Structural One Health emphasizes the upstream social, economic, and political determinants of health (Wallace et al., 2015 ).

This includes the impacts of neoliberal agricultural policies, land‐use changes driven by agribusiness expansion, labor precarity, and environmental degradation. Such structural factors not only shape the ecological contexts that facilitate disease emergence but also influence the vulnerability of affected populations and the institutional capacity to respond effectively to outbreaks. For example, the geographic concentration of vertically integrated poultry operations may reflect not only environmental suitability but also broader socio‐economic considerations, such as land access, infrastructure availability, and policy incentives that promote export‐oriented production. These dynamics can inadvertently generate disease hotspots, particularly in regions where biosafety regulations are weakly enforced and surveillance systems remain underfunded. Furthermore, high‐density poultry farming environments can promote viral amplification and genetic diversification, thereby increasing the risk of highly pathogenic strains emerging and spilling over into other species. (Gilbert & Pfeiffer, 2012 ; Wallace, 2009 ; Wallace et al., 2015 ).

Our research further advances this understanding by integrating fine‐scale environmental covariates and eBird data, offering localized insights into H5N1‐HPAI risk specifically within the Philippines. We identified the Eurasian Tree Sparrow and Zebra Dove as potentially playing an important role once AIV spills over from poultry due to their abundance and proximity to poultry environments. Species within the Columbidae family, including the African Rock Pigeon, Rock Pigeon, Common Wood Pigeon, Laughing Dove, Inca Dove, and Eurasian Collared Dove as well as species in the Passeriformes family, have been implicated in the potential zoonotic transmission of avian influenza viruses in the recent 2024 situation updates by the FAO of the United Nations (States‐FAO, 2024 ). This is in contrast with the previous study in 2014 stating that Columbidae as “dead end” hosts for avian influenza viruses (Abolnik, 2014 ).The Zebra Dove has tested positive for H5N1‐ HPAI infection in Thailand [22]. However, we exercise caution in extrapolating this finding to imply a direct transmission link between Zebra Doves and poultry in the Philippines. The dynamics of AIV transmission are highly intricate, involving factors such as migratory bird routes and interactions between resident birds and local poultry populations. The evolution and emergence of HPAI can occur within such ecosystems. While the role of migratory birds in AIV transmission is well‐documented, the contribution of local resident birds may vary across different regions. Hence, our primary objective is to provide insights aimed at improving the avian surveillance system for AIV detection in the Philippines by identifying potential target local avian species. Our analysis does not intentionally exclude species from the Anseriformes and Charadriiformes . Our decision to prioritize certain avian species for analysis was primarily based on their abundance and frequency of occurrence within the Philippines. While Anseriformes and Charadriiformes are commonly associated with long‐distance HPAI transmission, their representation in the eBird data set for the Philippines may be comparatively limited compared to other regions. Therefore, monitoring and surveillance efforts should encompass not only known reservoir species but also those with potential interactions or overlapping habitats with infected birds.

The DA‐Philippines have issued the Memorandum Circular No. 49, which outlines targeted vaccination guidelines to control avian influenza (Agriculture, 2023 ; DA‐AFID, 2022 ). However, the Philippine Food and Drug Administration has not yet issued Certificates of Product Registration or special import permits for any avian influenza vaccines. The vaccination program aims to reduce the viral spread, prevent outbreaks, minimize economic losses, and reduce human exposure to AIV. The guidelines specify the avian types eligible for vaccination, priority groups, vaccination types, and distribution and monitoring rules for avian influenza vaccines (Agriculture, 2023 ). While vaccination efforts are underway, improving farm management and biosecurity practices is crucial for disease control in poultry operations and live bird markets. Limited awareness and inadequate biosecurity among poultry raisers and traders contribute to AIV prevalence (Biswas et al., 2017 ; Sayeed et al., 2017 ; Turner et al., 2017 ). This study highlights risk mitigation interventions for H5N1‐HPAI transmission in the Philippines, including enhanced surveillance systems, strict biosecurity measures, public awareness campaigns, wildlife management strategies, international cooperation programs, and investment in research regarding innovative control strategies.

Despite the comprehensive nature of our study, several limitations should be considered when interpreting the results. The predictive models relied mainly on environmental covariates, which limited our inference to non‐environmental factors. Moreover, citizen science projects like eBird inherited sampling variability, leading to potential observation bias (Isaac & Pocock, 2015 ; Ruete, 2015 ). This bias can arise in several ways, including uneven geographic coverage, where bird observations are more frequently reported from densely populated and easily accessible areas, such as urban centers and near roadways, rather than remote or less‐visited regions (Zhang, 2020 ). Additionally, observer expertise and effort can vary, with experienced birdwatchers more likely to identify and report certain species accurately, while less experienced participants may underreport or misidentify birds. These factors may affect data accuracy and representativeness, potentially influencing species distribution estimates and their association with H5N1‐HPAI outbreaks.

Our study utilized MaxEnt, which, while widely used in species distribution modeling, presents certain limitations. MaxEnt is a presence‐only model that does not incorporate absence data, which may impact predictive accuracy in certain contexts. Recent studies have emphasized the advantages of ensemble modeling approaches, which integrate multiple algorithms (including MaxEnt) to improve predictive robustness and reduce biases associated with any single modeling technique (e.g., ensemble species distribution modeling of Anopheles albimanus and Culex tarsalis ) (Rhodes, Chaves et al., 2023 ; Rhodes, Loaiza et al., 2022 ) Future research could benefit from implementing ensemble models to enhance predictive performance by combining different modeling techniques, thereby reducing model‐specific biases and improving the reliability of risk assessments.

Additionally, our study examined a wider array of avian species, which may dilute the focus compared to studies solely targeting the Anatidae family, a well‐acknowledged primary AIV reservoir. Finally, the AIV serotype information is not available in the avian population, and no causal relationship can be inferred. Instead, we employed an ecological niche modelling approach to identify environmental similarities or suitability between poultry outbreak locations and local avian species. This study uncovered AIV poultry hotspots and showed that specific local avian species might contribute to AIV transmission due to their abundance and proximity to poultry establishments, particularly when the virus is introduced by migratory waterfowl. The information revealed the necessity to strength avian surveillance system to monitor the dynamics of AIV in the Philippines. Obtaining AIV sequence data from wild birds is also crucial for gaining deeper insights into the transmission dynamics of AIV within the Philippines.


## 6. Conclusion

Our study identified key environmental factors—such as precipitation levels and population density—as well as avian species, including the Eurasian Tree Sparrow and Zebra Dove, that are associated with H5N1‐HPAI outbreak risk in the Philippines. The ecological niche modeling approach demonstrated strong predictive performance and identified Metro Manila and Central Luzon as high‐risk regions for H5N1‐HPAI outbreaks. Although the Eurasian Tree Sparrow and Zebra Dove inhabit environmental conditions similar to those of outbreak‐affected poultry, their biological traits suggest a limited role in direct virus transmission. Nevertheless, their presence in high‐risk areas highlights the potential for spillover and underscores the need for further research into their role in the disease's ecology.

The integration of avian species distribution data into ecological niche modeling offers valuable insights for H5N1‐HPAI risk assessment and surveillance. These findings underscore the importance of incorporating biological, environmental, and epidemiological factors to inform and strengthen disease management strategies. Enhancing avian influenza surveillance, particularly in high‐risk regions, will be essential for mitigating future outbreaks and advancing our understanding of H5N1 transmission dynamics in both poultry and wild bird populations. Within the Structural One Health framework, it is also critical to assess the influence of global capital flows, agricultural industrialization, land use changes, and socio‐political inequalities on the ecological and social systems that shape avian influenza transmission.


## Conflict of Interest

The authors declare no conflicts of interest relevant to this study.


## Supporting information

Supporting Information S1


## Acknowledgments

We acknowledge the support of the Pathways Collaborative Research Actions (CRA) from the Belmont Forum in framing the study concept. We also thank the Taiwan National Science and Technology Council (NSTC 113‐2314‐B‐038‐088‐MY2) for funding support.

[AUTHOR], J. O. , & [AUTHOR], T.‐W. (2025). [REDACTED_TITLE]. [REDACTED_VENUE], 9, e2025GH001405. 10.1029/2025GH001405


## Contributor Information

John Oliver [AUTHOR], Email: [EMAIL_REDACTED].

Ting‐Wu [AUTHOR], Email: [EMAIL_REDACTED].


## Data Availability Statement

The data sources for eBird data are detailed in the Methods section and in Supporting Information Table S1 in Supporting Information S1 (GBIF, 2023 ; eBird, 2022 ). FAO. (2023). H5N1‐HPAI poultry outbreak data in the Philippines for 2022–2023 was acquired from the Food and Agriculture Organization of the United Nations Phillips. (2004). The ecological niche models were developed using the freely available software “Maxent” (version 3.4.4). All maps in this study were created using ArcGIS Pro 3.2.1.

This section collects any data citations, data availability statements, or supplementary materials included in this article.


### Data Citations


### Supplementary Materials

Supporting Information S1


### Data Availability Statement

The data sources for eBird data are detailed in the Methods section and in Supporting Information Table S1 in Supporting Information S1 (GBIF, 2023 ; eBird, 2022 ). FAO. (2023). H5N1‐HPAI poultry outbreak data in the Philippines for 2022–2023 was acquired from the Food and Agriculture Organization of the United Nations Phillips. (2004). The ecological niche models were developed using the freely available software “Maxent” (version 3.4.4). All maps in this study were created using ArcGIS Pro 3.2.1.
