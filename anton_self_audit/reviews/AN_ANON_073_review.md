# Review of AN_ANON_073

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This comparative evolutionary genomics study investigates whether exon shuffling in metazoans primarily rearranges complete structural and functional protein domains rather than arbitrary sub-domain exons, and tests how intron phase combinations ($0\text{–}0$, $1\text{–}1$, $2\text{–}2$) vary with domain evolutionary age. Analyzing $14,728$ human genes ($92,052$ exons; $20,778$ Pfam domains from Ensembl 4.28) and $19,682$ *Caenorhabditis elegans* genes ($4,271$ Pfam-annotated genes from WormBase release 30), the authors identify $1,269$ human domains ($345$ single-exon Class 1 and $924$ multi-exon Class 2 domains across $226$ domain families) and $286$ *C. elegans* domains ($110$ families) whose flanking introns fall within $10\%$ of the Pfam domain boundaries ($\|dn - in\| + \|dc - ic\| < 0.1(dc - dn)$). By contrasting domain-boundary introns against internal non-boundary introns and controlling for gene-family expansion by weighting each domain family equally ($\text{weight} = 1.0$), the authors demonstrate that (1) internal non-boundary exons and multi-exon sets (1 to 6 exons) exhibit zero excess phase symmetry ($758$ observed vs. $770.3$ expected, $P = 0.57$; Table 2), whereas random draws of equivalent size from the human genomic background show excess symmetry in $9,939/10,000$ replicates; (2) domain-boundary introns of both Class 1 ($83\%$ symmetrical, $P < 10^{-7}$; family-weighted $P < 0.05$) and Class 2 domains of 2–4 exons ($P < 10^{-7}$ to $P < 10^{-3}$; 2-exon family-weighted $P < 0.05$) exhibit strong excess phase symmetry; and (3) $1\text{–}1$ symmetrical domains and families are significantly enriched among metazoan-specific extracellular domains ($P < 10^{-3}$ in human; $P < 10^{-4}$ in *C. elegans*). Public database versions (`Ensembl 4.28`, `WormBase 30`, `Pfam`/`InterPro`) and mathematical criteria are clearly documented.

The study is well designed and provides a compelling resolution to a longstanding debate in molecular evolution: by showing that phase symmetry excess resides exclusively at domain boundaries and vanishes for internal non-boundary exons, the authors demonstrate both that complete structural domains are the primary units of exon shuffling and that genome-wide exon phase symmetry is not merely a byproduct of purifying selection against frameshifts during erroneous splicing of constitutive internal exons. Furthermore, the family-weighted control effectively rules out the possibility that a handful of tandemly duplicated domain families (`Sushi`, `CUB`, `EGF-like`) entirely drive the signal. The primary limitations are minor: (1) the Abstract states that $0\text{–}0$ symmetrical domains are over-represented among ancient prokaryotic–eukaryotic domains, whereas the main text and Tables 6 and 8 show that this excess is not statistically significant in either human ($P = 0.19$ for domains; $P = 0.33$ for families) or *C. elegans* ($P = 0.34$ and $P = 0.63$); (2) applying standard Pearson $\chi^2$ tests directly to summed fractional family weights treats continuous proportions as discrete counts; and (3) the sensitivity of the results to the $10\%$ domain boundary tolerance is not reported.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Introns at the boundaries of both single-exon (Class 1) and multi-exon (Class 2, up to 4 exons) protein domains exhibit a highly significant excess of symmetrical phases, whereas internal non-boundary introns follow random phase expectations: [Well Supported].**  
  The contrast between Tables 2, 3, and 5 is sharp and internally consistent. Because sample sizes for internal non-boundary exons (Table 2) are larger than for boundary domains, and $99.39\%$ of size-matched random draws from the $92,052$-exon genome background show significant symmetry, the absence of symmetry in internal exons ($758$ vs. $770.3$, $P = 0.57$) cannot be attributed to low statistical power.

* **The excess of symmetrical boundary introns persists after collapsing expanded domain families to equal unit weight ($\text{weight} = 1.0$) and replicates in *C. elegans*: [Well Supported].**  
  Collapsing the $345$ Class 1 domains into $56$ families ($33.0$ observed vs. $23.8$ expected, $P < 0.05$; Table 3) and the $367$ two-exon Class 2 domains into $74$ families ($34.9$ vs. $26.6$, $P < 0.05$; Table 5)—along with replication in *C. elegans* (Table 7)—confirms that phase symmetry reflects widespread domain shuffling across diverse structural families rather than tandem expansion of a few prolific modules.

* **Phase $1\text{–}1$ symmetrical domains and families are strongly over-represented among metazoan-specific ("new") extracellular domains ($P < 10^{-3}$ in human; $P < 10^{-4}$ in *C. elegans*): [Well Supported].**  
  Both raw domain counts ($138$ observed vs. $109.5$ expected in human; $23$ vs. $11.4$ in *C. elegans*) and family-weighted counts ($15.4$ vs. $7.0$ in human, $P < 10^{-3}$) demonstrate a marked expansion of $1\text{–}1$ extracellular modules coinciding with metazoan multicellularity.

* **Ancient ("old") domains shared between eukaryotes and prokaryotes are over-represented among $0\text{–}0$ symmetrical domains, compatible with primordial domain shuffling in the progenote (Abstract, line 25): [Overstated].**  
  In the Results (line 243) and Discussion (line 323), the authors explicitly acknowledge that the excess of old $0\text{–}0$ domains is not statistically significant in humans ($80$ observed vs. $71.0$ expected, $P = 0.19$ for domains; $27.5$ vs. $23.4$, $P = 0.33$ for families; Table 6) or in *C. elegans* ($29$ vs. $24.7$, $P = 0.34$ for domains; $12.1$ vs. $10.7$, $P = 0.63$ for families; Table 8). Moreover, because expected counts in Tables 6 and 8 are conditioned on the overall fraction of $0\text{–}0$, $1\text{–}1$, and $2\text{–}2$ domains across the entire dataset (line 239)—and metazoan-specific (`New`) domains have a massive excess of $1\text{–}1$ modules—the deficit of $1\text{–}1$ among `Old` domains ($P < 0.02$) mechanically inflates the relative share of $0\text{–}0$ domains without requiring primordial $0\text{–}0$ exon shuffling.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Temper the Abstract Claim Regarding Ancient $0\text{–}0$ Domain Over-Representation and Decouple Marginal Age Expectations
* **WHY:** Stating in the Abstract (line 25) that *"0–0 symmetrical domains tend to be over-represented among ancient protein domains... compatible with the suggestion of primordial domain shuffling in the progenote"* overstates a non-significant result ($P = 0.19\text{–}0.63$ in Tables 6 and 8) that is further confounded by compositional closure against the metazoan $1\text{–}1$ expansion.
* **WHAT:** Revise the Abstract to reflect that the $0\text{–}0$ enrichment among ancient domains is a non-significant trend, and test whether `Old` domains exhibit an excess of $0\text{–}0$ boundary introns relative to the flanking intron phase frequencies within `Old` domains themselves (analogous to Tables 3 and 5) rather than relative to the metazoan-skewed dataset average.
* **HOW:** Compute $P_0^2 N_{\text{old}}$ using the $5'$ and $3'$ phase $0$ frequencies specifically within the $401$ human `Old` domains (and $134$ *C. elegans* `Old` domains), report this direct phase-independence test alongside Table 6 and Table 8, and qualify the sentence on line 25 of the Abstract.

#### 2. Replace Fractional-Count $\chi^2$ Approximations for Domain Families with an Exact Permutation Test
* **WHY:** In Tables 3, 5, 6, 7, and 8, summing within-family phase proportions yields non-integer counts (e.g., $8.5$, $24.3$, $0.2$) that are entered directly into a 1-df $\chi^2$ contingency test. Because families vary from $1$ to $144$ members, treating fractional family weights as independent Poisson/multinomial counts is an approximation.
* **WHAT:** Validate the family-level $P$-values using a non-parametric permutation test that preserves family membership and size.
* **HOW:** Across $10,000$ permutations, randomly permute the $3'$ boundary intron phases across domain families (or randomly draw 1 representative domain per family in each replicate and compute the exact integer $\chi^2$ / Fisher's exact statistic), and report the empirical permutation $P$-values in Tables 3, 5, 6, 7, and 8.

#### 3. Report a Sensitivity Analysis for the $10\%$ Domain-Boundary Intron Tolerance Criterion
* **WHY:** Boundary introns were defined using the heuristic threshold $\|dn - in\| + \|dc - ic\| < 0.1(dc - dn)$ (line 345). Showing that the phase-symmetry contrast between boundary and non-boundary introns holds across stricter and looser cutoffs would confirm robustness against Pfam boundary annotation noise.
* **WHAT:** Summarize the observed and expected symmetry counts at $5\%$, $10\%$, and $15\%$ domain-length tolerances.
* **HOW:** Re-run the MySQL/Perl boundary query at $0.05(dc - dn)$ and $0.15(dc - dn)$ and report the resulting Class 1 and Class 2 symmetry percentages and $P$-values in a brief paragraph in the Methods or Results.
