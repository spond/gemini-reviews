# Anonymous Manuscript ID: MANUSCRIPT_META_01

*(All identifying metadata, author names, institutional affiliations, repository URLs, and lab software identifiers have been scrubbed for blinded review.)*

## Abstract

Biomedical publishing has grown more than elevenfold since 1991, overwhelming human peer review. Flawed studies now routinely enter the scientific record. Because human referees often rely on quick impressions and the prestige of famous authors or journals, broken statistical designs and unverified database analyses frequently pass review unchecked. Here, we introduce a blinded artificial intelligence (AI) peer-review system that strips out author names, institutions, journal titles, and publication dates before grading full-text papers on a 10-point scale covering methods, evidence, biology, and data sharing. Tested on 100 benchmark papers, our blinded reviewer passed 100\% of verified sound studies at our failure cutoff while catching up to 89\% of retracted or refuted papers with more than double the consistency of human referees. Auditing 1,076 everyday full-text papers from 1991 to 2025—including 915 date-blinded studies—showed that up to half of 2020--2025 papers fail on core rigor, driven by database mining and megajournals while established journals held much steadier. Across 20 preprint-to-published pairs and 100 open-review papers, selective peer review added nearly three times more value than megajournals while our AI recalled 98\% of unresolved human critiques (`[REDACTED_REPOSITORY_URL]`).




## Introduction


Modern science relies on a simple promise: before a study is published, independent experts check that its experiments, statistics, and conclusions hold up. Over the past 35 years, however, the volume of biomedical papers indexed each year in PubMed grew more than elevenfold, rising from roughly 58,000 articles in 1991 to nearly 650,000 in 2025. Open-access full-text papers grew nearly 300-fold over the same period. The pool of human peer reviewers cannot keep pace. Reviewers are stretched thin. Longstanding theoretical work warned that small sample size, flexible data mining, and pressure to publish positive results would make many published findings false \cite{Ioannidis2005}. Careful follow-up investigations have repeatedly confirmed that warning. In microbiome research, laboratory reagent contamination has been mistaken for tumor or placental bacteria \cite{Salter2014,deGoffau2019,Kennedy2023}. In human genetics, subtle geographic ancestry differences were misread as natural selection on human height \cite{Sohail2019,Berg2019,Zaidi2020}. In single-cell genomics, treating thousands of cells from just two or three patients as independent samples has produced waves of false discoveries \cite{Squair2021,Zimmerman2021,Li2022}.

Catching these errors after publication takes years of detective work by specialized teams. Discovering that human DNA contamination and database errors created false microbial signatures across dozens of cancer types required manual re-analysis of terabytes of raw sequencing reads \cite{Poore2020,Gihawi2023}. Proving that a faulty genotyping probe caused a spurious link between the human *CCR5*-$\Delta$32 mutation and mortality in the UK Biobank required digging into raw chip intensities \cite{Wei2019,Maier2020}. Everyday peer review rarely catches such problems because human referees often disagree—showing consistency scores of just 0.20 to 0.45 on a 0-to-1 scale \cite{Cicchetti1991,Marsh2008}—and are heavily swayed by reputation. Controlled experiments prove just how strong that prestige bias is \cite{Tomkins2017,Huber2022}. When over 3,300 referees reviewed the exact same manuscript, only 23\% recommended rejection when a Nobel laureate's name was on the cover page, compared to 48\% when the paper was anonymized and 65\% when attributed to an unknown junior author \cite{Huber2022}. When a manuscript carries famous names or appears in a flagship journal, human readers and unblinded AI tools alike give it the benefit of the doubt, overlooking missing controls or math errors in supplementary tables.

Previous efforts to automate scientific quality control have taken two paths, each with a major blind spot. The first path uses rule-based software to check specific reporting formulas. In psychology, the `statcheck` program scanned over 30,000 articles and found that half had at least one $p$-value that did not match its reported test statistic \cite{Nuijten2016}, while the `GRIM` test caught impossible sample averages in half of small-sample studies \cite{Brown2017}. In biomedicine, automated preprint screens such as `ScreenIT` flag missing reagent identifiers, bar graphs, or data statements \cite{Weissgerber2021}. While valuable, rule-based scripts only check surface syntax; they cannot tell whether a study forgot a negative extraction control or mistook batch effects for biology. The second path uses machine learning and large language models (LLMs) to mimic human peer review \cite{Checco2021,Liang2024,Brian2026}. A landmark study tested GPT-4 on over 3,000 *Nature*-family papers and 1,700 machine-learning submissions, finding that GPT-4 raised many of the same points as human referees ($\sim 31\%\text{--}39\%$ overlap, matching human-to-human agreement) and that 82\% of surveyed authors found the AI feedback more helpful than at least some human reviews \cite{Liang2024}. More recently, a benchmark of 15 LLMs on randomized clinical trials seeded with 14 artificial methodological flaws (modeled on classic British Medical Journal referee trials \cite{Schroter2008}) showed that LLMs caught 46\% to 93\% of planted flaws compared to just 27\% for historical human reviewers \cite{Brian2026}. Yet simply pasting a published paper into an uncalibrated chatbot fails as an objective audit for two reasons. First, if the AI can see the title, authors, journal, or workspace hints, it can recall from its training memory whether a paper was praised, cited, or retracted—or recall famous error checklists—and inherit human prestige biases \cite{Checco2021}. Second, without a calibrated scoring scale anchored against verified sound and flawed papers, open-ended ``find flaws'' prompts create a severe false-alarm trap: in the clinical-trial benchmark \cite{Brian2026}, the models that caught the most planted errors also falsely flagged 25\% to 29\% of those same error categories on clean, unmodified control trials ($r = -0.77$).

To solve both problems, we built a strictly blinded AI peer-review pipeline (`gemini-4-argon`) with internet search turned off. Before the AI reads a manuscript, an automated scrubber strips away the title, author names, universities, journal name, publication year, web links, and any retraction notices. The AI must judge the paper purely on its text, equations, figures, and tables across four plain-English questions totaling 10 points: Are the methods and statistics sound (3.5 points)? Do the data actually support the claims (2.5 points)? Are the assumptions biologically realistic (2.0 points)? Are the data and code openly shared (2.0 points)? For historical papers published before open-data mandates, we also track the 8-point Scientific Core covering just the first three questions. Across 1,580 full-text reviews of 1,466 unique papers spanning six experiments (Table~\ref{tab:overview}), our investigation establishes six clear take-home messages for scientists, editors, funders, and readers.

\begin{table}[t!]
\centering
\caption{Summary of the six blinded AI review experiments ($1,580$ total full-text reviews across $1,466$ unique papers) and their main take-home findings. Technical equations and full sensitivity tables appear in the Supplementary Information (Tables S1--S7), and all review dossiers are searchable at `[REDACTED_REPOSITORY_URL]`.}
\label{tab:overview}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{llp{8.8cm}}
\toprule
Experiment & Papers Reviewed & Main Take-Home Finding \\
\midrule
1. Calibration \& Blinding & 200 papers (50 retracted/refuted, 50 sound controls, 100 wild) & Blinded AI scores sound controls at $8.6/10$ with $0\%$ false rejections ($<5.0$), catches up to $89\%$ of flawed papers, and removes a $+0.35$-point prestige halo. \\
\addlinespace[3pt]
2. Repeatability & 30 papers $\times$ 3 blind runs (90 reviews) & Single-review consistency in everyday literature is $0.86$ ($0.95$ for a 3-run average), more than double human peer review ($0.20\text{--}0.45$). \\
\addlinespace[3pt]
3. Everyday Literature Across 8 Fields & 160 recent papers (2020--2025) across 8 subfields & Roughly half ($43\%\text{--}55\%$) fail on core rigor ($<5.0$). Mature quantitative fields score well ($6.9/10$), while template-driven fields average $4.3\text{--}4.8/10$. \\
\addlinespace[3pt]
4. Peer Review \& Human Concordance & 20 preprint-published pairs (40 texts) + 100 open-review papers (261 human referees) & Selective peer review adds $+0.59$ Core points ($p=0.013$) vs. $+0.22$ at megajournals ($p=0.12$). Across 100 open-review papers ($7.49$ selective vs. $5.01$ megajournal), AI recalls $97.9\%$ ($95/97$) of unresolved human critiques, catches 385 extra flaws, and exposes anomalies in $58\%$ of megajournal reviews. \\
\addlinespace[3pt]
5. 35-Year Trend \& Economics & 915 verified full-text date-blinded papers (1991--2025); 1,076 pooled wild papers & Quality fell from $7.6$ (1990s) to $5.8$ (2020s) largely via ecosystem shifts; research payoff peaks at $\sim\$0.95\text{M/yr}$ ($7.6/10$); $\$3.2\text{k}$ society journals beat $\$2.9\text{k}$ megajournals by $+0.72$ points. \\
\addlinespace[3pt]
6. Blinded Career Self-Audit & 164 papers by the senior author (2004--2026) & Overall average is $7.5/10$. The 42 papers led as First or Senior Author average $8.2/10$ with $0\%$ failures ($<5.0$), vs. $7.3/10$ for middle-author roles. \\
\bottomrule
\end{tabular}%
}
\end{table}


## Results



### Take-Home 1: Blinded AI Review Separates Sound Science From Flawed Papers and Removes Prestige Bias


Before using an AI reviewer to judge everyday papers, we must prove two things: it must not falsely condemn solid science, and it must reliably catch broken methods without peeking at who wrote the paper. We tested our reviewer on 100 benchmark papers across five core biomedical fields: viral evolution, cancer and microbiome studies, human statistical genetics, single-cell gene expression, and molecular evolution. Half of these papers (Cohort A, 50 papers) were formally retracted or disproven by later studies because of severe methodological errors \cite{Amendola2022,Tang2020,Forster2020,Poore2020,Aykut2019,Narayanan2022,Wei2019,Sebastiani2012,Turchin2012,Berg2014}. The other half (Cohort B, 50 papers) are verified benchmark controls—foundational methods and carefully validated discoveries in the exact same five fields \cite{Starr2020,Worobey2022,Gihawi2023,Sohail2019,Berg2019,Murrell2012,Murrell2015,KosakovskyPond2020,Minh2020,Love2014}.

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig1_calibration_repeatability.pdf}
\caption{Blinded AI review separates sound benchmark science from retracted or refuted papers with high repeatability. Panel A shows blinded review scores (/10) across 50 retracted or refuted papers (Cohort A, red), 50 verified sound benchmark controls (Cohort B, green), and 100 everyday published papers from 2020--2025 (Cohort C, blue). Dashed lines mark the $<5.0$ failure cutoff ($0\%$ false rejections among sound controls) and $<6.0$ major-flaw cutoff. Panel B shows test-retest consistency across 30 papers reviewed blind three separate times in fresh sessions, achieving a single-run reliability of $0.86$ in everyday papers ($0.97$ overall), more than double typical human referee reliability ($0.20\text{--}0.45$).}
\label{fig:calibration}
\end{figure}

First, we tested what happens when we hide author names, universities, journal titles, and retraction banners across a 75-paper pilot set. On everyday published papers, hiding author and journal names lowered average scores by 0.35 points (from 5.92 down to 5.57 out of 10). Famous institutions and prestigious journal headers buy a 0.35-point halo that disappears under blind review. Conversely, on retracted or refuted papers, hiding retraction banners raised average scores from 3.46 to 4.65. When the AI can see who wrote a retracted paper, it recognizes the retraction from memory and assigns a rock-bottom grade. When blinded, the AI has to find the flaws from scratch by reading the methods and tables.

Even working completely blind, the AI cleanly separated sound science from flawed papers across the full 200-paper calibration study (Figure~\ref{fig:calibration}A, Supplementary Table~S1). Sound benchmark controls (Cohort B) scored an average of $8.6 \pm 0.8$ out of 10 (median 8.9). Not a single sound control paper scored below our 5.0-point failure cutoff (100\% specificity, 50 out of 50 passed), and 98\% (49 out of 50) scored 6.0 or higher. Meanwhile, retracted and refuted papers (Cohort A) averaged just $4.4 \pm 2.0$ (median 4.2, $p = 2.4 \times 10^{-16}$), yielding an overall diagnostic accuracy (area under the receiver operating characteristic curve) of 0.97, and 0.98 on the 125-paper held-out validation wave. In 95\% of the flawed papers it flagged (38 of 40), the blinded AI pinpointed the exact statistical error, missing control, or contamination artifact described in the published retraction notice or refutation paper.

Looking closely at the five refuted papers that scored above 7.0 under blind review revealed an important boundary of text-only auditing. Three of those papers developed clever mathematical formulas to detect natural selection on human height and applied them to public summary tables from the GIANT genetics consortium \cite{Turchin2012,Berg2014,Field2016}. Years later, analyses of UK Biobank sibling data showed that the upstream GIANT summary tables contained hidden geographic bias \cite{Sohail2019,Berg2019}. The other two papers relied on external microbial databases or likelihood models whose flaws only appeared under outside simulation \cite{Nejman2020,Rabosky2014}. No reviewer reading a manuscript text alone can spot hidden biases inside an external consortium's database. When we set aside those five upstream-database cases, our blinded reviewer catches 76\% of internally flawed papers at the strict $<5.0$ cutoff, 89\% at $<6.0$, and 96\% at $<6.5$, with a diagnostic accuracy of 0.99 (Supplementary Table~S1).

To verify that the AI does not give erratic scores from run to run, we took 30 papers and had the AI review each one blind three separate times under fresh anonymous IDs (90 reviews total, Figure~\ref{fig:calibration}B). Across everyday published papers, single-review consistency was 0.86 on a 0-to-1 scale, rising to 0.95 when averaging three runs (and 0.97 across all 30 papers). That is more than double the 0.20-to-0.45 consistency reported for human peer reviewers \cite{Cicchetti1991,Marsh2008}.

As an independent cross-check, we also replicated the recent 15-model clinical-trial benchmark of Brian et al.\ \cite{Brian2026}. Because their study tested Google's lightweight `Gemini 3.8 Flash` model and omitted a flagship Pro model, we ran our blinded `gemini-4-argon` (`Gemini 3.1 Pro`) reviewer on three matched pairs of their 2026 *Nature Medicine* randomized trials (Supplementary Section~S4, Supplementary Table~S7). Each pair compared an unmodified control trial against its 14-error seeded counterpart. On the error-seeded trials, `gemini-4-argon` caught 84\% of planted major flaws, including 100\% of planted randomization, intention-to-treat, unvalidated-scale, and numerical-contradiction errors. At the same time, it kept false alarms on the unmodified control trials down to 2.4\% (97.6\% specificity vs.\ 71\%--86\% for the highest-sensitivity models in Brian et al.\ \cite{Brian2026}), achieving the highest net diagnostic accuracy of all tested models (Youden's $J = 0.82$). Our calibrated 10-point score separated the unmodified trials ($6.9 \pm 0.6$, 100\% passed) from the error-seeded versions ($3.0 \pm 0.5$, 100\% failed below 5.0) by nearly four points with zero overlap. Notably, it also caught a real, unplanted flaw in a published *Nature Medicine* trial—a registered primary-outcome variance promised in the Abstract and Methods but omitted from the Results—that human peer review had missed.


### Take-Home 2: Roughly Half of Recent Papers Fail on Scientific Rigor, With Wide Gaps Across Fields


Having verified that a score below 5.0 indicates severe methodological failure with zero false alarms on sound benchmark papers, we used our blinded reviewer to audit 160 uncurated, everyday open-access papers published between 2020 and 2025 across eight scientific fields (Figure~\ref{fig:ood}, Supplementary Table~S2). One hundred papers came from our five core biomedical fields (Cohort C, 20 per field), and 60 papers came from three additional fields never used during calibration: ecology and evolution, neuroscience and brain imaging, and AI-driven drug discovery (20 per field).

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig2_wild_ood_distributions.pdf}
\caption{Blinded review of 160 everyday papers (2020--2025) across eight fields reveals high failure rates and a strong gap across journal types. Panel A shows score distributions (/10) across five core biomedical fields (blue) and three additional out-of-distribution fields (orange). Quantitative fields with strict null models (such as Molecular Evolution, $6.9/10$, $5\%$ failed) score much higher than fields dominated by unverified data-mining templates or contamination-prone assays (such as Single-Cell Transcriptomics, $4.3/10$, $75\%$ failed). Panel B shows scores across journal types: selective flagship journals average $7.2/10$ ($14\%$ failed), specialist society journals average $5.2/10$ ($44\%$ failed), and open-access megajournals average $4.4/10$ ($65\%$ failed).}
\label{fig:ood}
\end{figure}

The results were sobering. Across the 100 everyday papers in our five core fields, the average score was $5.5 \pm 1.8$ out of 10, and 43\% scored below the 5.0-point failure cutoff (61\% scored below 6.0, and only 11\% reached 8.0 or above). Across the 60 papers in the three additional fields, the average score was $4.9 \pm 1.9$, with 48\% to 55\% failing below 5.0 (73\% to 78\% below 6.0). Adjusting for the fact that our reviewer catches about three-quarters of flawed papers implies that roughly 55\% to 65\% of recent open-access papers in these fields suffer from fundamental methodological flaws that undermine their main claims.

Paper quality varied dramatically by scientific area (Figure~\ref{fig:ood}A). Mature quantitative fields that require explicit mathematical null models performed best: molecular evolution averaged $6.9 \pm 1.5$ (only 5\% failed below 5.0), and viral evolution averaged $6.0 \pm 1.6$ (35\% failed). Statistical genetics sat in the middle at $5.4 \pm 1.6$ (40\% failed), dragged down by wave after wave of formulaic two-sample Mendelian randomization papers that violated basic genetic assumptions. At the bottom sat fields flooded by contamination-prone assays or cookie-cutter data mining. Ecology averaged $5.2$ (55\% failed), neuroscience and brain imaging averaged $4.9$ (50\% failed), and cancer and low-biomass microbiome studies averaged $4.8$ (60\% failed, routinely lacking negative extraction controls). Even lower scores appeared in AI drug discovery and docking at $4.6$ (60\% failed, claiming potent drug hits from computer docking alone) and single-cell transcriptomics at $4.3$ (75\% failed, treating thousands of cells from two or three patients as independent samples).

Scores also tracked closely with journal selectivity and downstream citations (Figure~\ref{fig:ood}B). Across all 160 recent papers, higher-scoring studies earned significantly more citations per year ($r = +0.45, p = 2.2 \times 10^{-9}$). Papers published in selective flagship journals ($n = 35$) averaged $7.2 \pm 1.6$ with only 14\% failing below 5.0. Papers in specialist society journals ($n = 48$) averaged $5.2 \pm 1.5$ (44\% failed). Papers in open-access megajournals ($n = 77$) averaged just $4.4 \pm 1.5$, with 65\% failing below 5.0. The AI did not know which journal any paper came from. That 2.8-point gap between flagship journals and megajournals reflects real differences in experimental design and statistical care.


### Take-Home 3: Peer Review Substantially Improves Papers at Selective Journals, but Not at Megajournals


Do selective journals score higher simply because better papers are submitted to them, or does rigorous peer review actually improve manuscripts before publication? To measure the real impact of peer review, we collected 20 matched pairs of initial preprints (from bioRxiv, medRxiv, and Research Square) and their final peer-reviewed journal versions. Half were published in selective flagship or society journals (such as *Nature*, *PLOS Biology*, *eLife*, and *PLOS Pathogens*), and half were published in open-access megajournals (such as *PLOS ONE*, *Scientific Reports*, and *PeerJ*). We stripped all formatting, version labels, and metadata from all 40 documents and had separate blinded AI agents review the preprint and published version of each study (Figure~\ref{fig:peerreview}, Supplementary Table~S3). To ensure that simple formatting differences in where journals place Data Availability statements could not skew the comparison, we measured improvement on the 8-point Scientific Core (methods, claim alignment, and biology).

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig3_peer_review_paired.pdf}
\caption{Peer review substantially improves manuscripts at selective journals, while open-review dossiers across 100 papers reveal high AI recall of human critiques and widespread megajournal referee anomalies. Panel A tracks the 8-point Scientific Core score from initial blinded Preprint to final blinded Published article across 20 matched pairs. Studies revised at selective flagship and society journals ($n=10$, green) gained an average of $+0.59$ points ($p=0.013$, with 9 of 10 improving), nearly three times the $+0.22$-point change at open-access megajournals ($n=10$, red, $p=0.12$, not significant). Panel B audits 100 open-review manuscripts (50 selective society/flagship averaging $7.5/10$ vs. 50 megajournal averaging $5.0/10$) alongside 4 version-blinded preprints: across 363 substantive critiques raised by 261 human referees, our blinded AI recalled $97.9\%$ ($95/97$) of all critiques remaining unresolved in the published text ($78.2\%$ overall including pre-publication edits) while catching 385 additional mathematical and design flaws.}
\label{fig:peerreview}
\end{figure}

Across all 20 studies, peer review improved the 8-point Scientific Core by an average of $+0.41$ points ($p = 0.0031$, equivalent to $+0.51$ points on a 10-point scale), with 16 of the 20 papers improving after review. However, splitting the sample by journal type revealed a striking divide (Figure~\ref{fig:peerreview}A). At selective flagship and society journals, peer review raised the Scientific Core by $+0.59$ points (rising from 5.70 to 6.29 out of 8.0, $p = 0.013$, with 9 of 10 papers improving). During revision at these selective journals, authors added independent validation experiments, fixed statistical controls, and toned down overstated claims. At open-access megajournals, by contrast, peer review raised the Scientific Core by only $+0.22$ points (rising from 4.72 to 4.94 out of 8.0, $p = 0.12$), a change statistically indistinguishable from zero. In short, peer review at selective journals adds nearly three times ($2.7\times$, and $3.4\times$ when excluding late-posted preprints) more scientific value than megajournal review.

To test on a larger scale whether our blinded AI spots the same flaws as human reviewers—and why megajournal peer review adds so little value—we audited a balanced cohort of 100 published open-review papers (`2020--2025`) whose verbatim human referee reports and editorial decision letters are publicly archived alongside the article (Figure~\ref{fig:peerreview}B, Supplementary Table~S3). Half ($n = 50$) came from selective flagship and society open-review journals (*eLife*, *PLOS Biology*, *PLOS Genetics*, *PLOS Pathogens*, and *PLOS Computational Biology*), and half ($n = 50$) came from open-review megajournals (*PLOS ONE*). In Stage~1, our blinded AI reviewed all 100 stripped manuscripts without access to the human peer-review files; in Stage~2, we compared the locked AI reviews against all 261 human referee reports (363 substantive technical critiques total). Three findings stood out.

-  **A 2.5-point quality gap between selective and megajournal open review.** Blinded AI scores averaged $7.49 \pm 1.38$ out of 10 at selective open-review journals ($5.87 / 8.0$ Core, median $7.75$), where only $8.0\%$ failed below $5.0$ and human referee reports averaged $3,977$ words. By contrast, open-review megajournal papers averaged $5.01 \pm 1.69$ out of 10 ($3.79 / 8.0$ Core, median $5.10$, $\Delta = +2.48$ points, $p = 2.1 \times 10^{-12}$), with $48.0\%$ failing below $5.0$, $76.0\%$ below $6.5$, and median referee reports of $2,462$ words.
-  **97.9\% AI recall of unresolved human critiques plus 385 AI-only forensic catches.** Across the 97 substantive human referee criticisms that authors left unresolved in the final published article, our single-pass blinded AI independently caught 95 (97.9\%: 85 exact matches and 10 partial matches). Even across all 363 human referee points—including 266 pre-publication issues that authors fixed or edited before the published version—the blinded AI recalled 78.2\% ($284 / 363$), matching its 83\% ($15/18$) recall on version-1 preprints. At the same time, the blinded AI caught 385 hard mathematical, statistical, and experimental design flaws ($3.85$ per paper) that escaped all 261 human referees and handling editors. For example, human referees missed inverted odds ratios in published regression tables (`OPEN\_ANON\_011`, where $1 / 0.475 = 2.1$ reversed the direction of effect for chronic disease and an adjusted odds ratio of $1.2$ lay outside its own 95\% confidence interval of $0.9\text{--}1.14$). Referees also missed physically impossible melanin ELISA concentrations exceeding 100\% of wet tissue weight (`OPEN\_ANON\_036`, $121.7\text{ mg/mL}$ melanin in $100\text{ mg/mL}$ chicken homogenate), human cells profiled on a rodent microRNA array (`OPEN\_ANON\_088`), pre-pandemic 2017--2018 UK Biobank cohorts used as COVID-19 outcomes (`OPEN\_ANON\_083`), and over 20 table errors in a 2026 *Nature* benchmark. Strikingly, the AI also caught numerous *revision-induced errors* where authors' changes during peer review introduced impossible negative $p$-values ($p = -0.006$ in `OPEN\_ANON\_035`) or corrupted table denominators (`OPEN\_ANON\_086`, `OPEN\_ANON\_096`) that referees never re-checked.
-  **Widespread human referee anomalies in megajournals (58\% vs. 2\%).** Inspecting the 261 verbatim human referee reports explained why so many flawed megajournal papers passed peer review. At selective open-review journals, 72.0\% ($36/50$) of referee dossiers provided thorough technical scrutiny, 0\% ($0/50$) were superficial boilerplate, and only 1 paper ($2.0\%$, `OPEN\_ANON\_015`) experienced a referee anomaly—an irrelevant citation demand that the *PLOS Computational Biology* editor explicitly stepped in to waive. At open-review megajournals, only 12.0\% ($6/50$) of referee dossiers provided thorough technical scrutiny, 38.0\% ($19/50$) consisted of superficial 3-to-6 sentence checklists, and 58.0\% ($29/50$) exhibited severe peer-review anomalies. Those 29 megajournal anomalies included 19 generic or suspect AI-generated boilerplate reviews. In `OPEN\_ANON\_049`, Reviewer~1 pasted raw LLM prompt instructions into Decision Letter~1 while missing 126.6 SNPs claimed per 100-bp tag; in `OPEN\_ANON\_019`, Reviewer~2 pasted a 19-citation word-count template demanding links to `indeed.com` and `scribbr.com` blogs. Another 6 megajournal papers suffered coercive citation demands. In `OPEN\_ANON\_001`, a named reviewer forced the authors to add 5 of his own fish papers; in `OPEN\_ANON\_011`, Reviewer~2 forced an online survey paper to add a speculative paragraph on amygdala and insula neuroimaging to cite 3 neuroscience papers—which our blinded AI independently flagged as an unsupported overstatement. The remaining 4 anomalies were single-reviewer acceptances on quantitatively flawed studies (`OPEN\_ANON\_036`, `OPEN\_ANON\_053`, `OPEN\_ANON\_083`, `OPEN\_ANON\_084`).



### Take-Home 4: Established Journals Kept Higher Standards Over 35 Years, While Overall Quality Fell in the 2020s as the Publishing Mix Shifted


Why do roughly half of recent 2020--2025 papers fail our quality screen? Did established journals lower their peer-review standards over the past three decades, or did the mix of what gets published change as publishing volume exploded? To find out without any bias toward older or newer eras, we sampled 1,000 open-access articles across seven 5-year windows from 1991 to 2025 and four core biomedical tracks (viral evolution, statistical genetics, gene expression, and molecular evolution). We strictly excluded 85 archival 1990s/early-2000s records whose Europe PMC XML contained only an abstract or PDF placeholder plus bibliography. We scrubbed every date, year, author name, and journal title from the remaining 915 verified full-text manuscripts ($226\text{--}233$ per track) and scored all 915 papers blind (Figure~\ref{fig:secular}A, Supplementary Table~S4).

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig4_secular_covariates.pdf}
\caption{A 35-year quality decline driven by the rise of open-access megajournals, secondary database mining, and formulaic study templates. Panel A shows date-blinded manuscript scores (/10, blue) across four decades from the 1990s to the 2020s ($N=915$ verified full-text papers), plotted alongside the 11-fold surge in annual PubMed biomedical paper volume (red dashed curve). Average scores fell from $7.63$ in the 1990s to $5.81$ in the 2020s ($34.8\%$ failed below 5.0 and $50.9\%$ below 6.0). Panel B compares study types across all 1,076 everyday full-text papers in our study: primary wet-lab experiments average $6.8/10$ ($16\%$ failed) and foundational methods average $6.6/10$ ($19\%$ failed), whereas pure secondary database mining averages $5.3/10$ ($43\%$ failed) and formulaic hype-cycle templates average $4.2/10$ ($74\%$ failed).}
\label{fig:secular}
\end{figure}

Across the 915-paper full-text cohort, overall quality fell sharply and monotonically over 35 years (Figure~\ref{fig:secular}A). In the 1990s ($n = 154$), full-text papers averaged $7.63 \pm 1.25$ out of 10 (median 7.95, with only 3.9\% failing below 5.0; $7.61 \pm 1.43$ in 1991--1995 and $7.47 \pm 1.22$ in 1996--2000). Average scores stepped down in the 2000s ($6.76 \pm 1.48$, median 7.0, 14.1\% failed, $n = 249$) and 2010s ($6.56 \pm 1.63$, median 6.8, 18.4\% failed, $n = 239$) before dropping sharply in the 2020s ($n = 273$) to $5.81 \pm 1.97$ (median 5.8, with 34.8\% failing below 5.0 and 50.9\% below 6.0; $5.79 \pm 1.83$ in 2021--2025). Across the full 35-year span, composite quality declined by $0.58$ points per decade ($r = -0.33, p = 1.2 \times 10^{-24}$), while the 8-point Scientific Core fell even faster at $0.68$ scaled points per decade ($0.54$ raw Core points, $r = -0.36, p = 8.7 \times 10^{-29}$). Every subfield track declined strongly ($p \le 3.1 \times 10^{-6}$): gene expression ($n = 227, r = -0.37$), viral evolution ($n = 226, r = -0.36$), statistical genetics ($n = 229, r = -0.31$), and molecular evolution ($n = 233, r = -0.30$). Although the blinded AI could infer a paper's decade from its laboratory techniques with 92.4\% accuracy ($n = 543$), the partial correlation between perceived decade and score holding true publication year constant was zero ($r = -0.009, p = 0.83$), ruling out nostalgia bias.

To separate within-journal drift from shifts in what gets published, we analyzed within-journal trends across the 915-paper cohort and compared study designs across all 1,076 everyday full-text papers in our study (Figure~\ref{fig:secular}B, Supplementary Table~S4). Three findings explain the 35-year drop.

-  **Ecosystem expansion and compositional shift explain the bulk of the decline.** Tracking 549 full-text papers across 30 recurring multi-year journals showed a modest within-journal slope of $-0.23$ points per decade ($r = -0.094, p = 0.027$), less than two-fifths of the $-0.58$-point-per-decade drop across the literature as a whole. An Oaxaca--Blinder decomposition confirmed that the majority ($54.1\%\text{--}58.3\%$, or $0.98$ points) of the drop from the 1990s ($7.63$) and 1996--2000 ($7.47$) to the 2020s ($5.81$) came directly from compositional shifts in the publishing ecosystem. Over that span, commercial APC megajournals expanded from 0\% of the cohort in the 1990s to 51\% in the 2020s, averaging $5.80 \pm 1.73$ ($n = 422$, 33.9\% failed) compared to $6.75 \pm 1.79$ at selective and society venues ($n = 654$, 17.3\% failed, $p = 1.3 \times 10^{-17}$).
-  **Wet-lab experiments vs. pure database mining.** Papers that generated primary laboratory data ($n = 408$) averaged $6.81 \pm 1.68$ (16.4\% failed below 5.0), and hybrid wet-lab/computational studies ($n = 351$) averaged $6.56 \pm 1.73$ (19.9\% failed). By contrast, purely computational papers that re-analyzed secondary public cohorts or databases ($n = 230$)—such as cancer registries, gene expression archives, or UK Biobank tables—without wet-lab validation averaged $5.33 \pm 1.78$ (42.6\% failed), a 1.48-point drop ($p = 5.5 \times 10^{-23}$).
-  **Foundational science vs. cookie-cutter templates and unedited AI text.** Studies using mid-stage high-throughput assays ($n = 348$, mean $6.65 \pm 1.65$, 17.0\% failed) or mature classical designs ($n = 616$, mean $6.62 \pm 1.71$, 18.5\% failed) performed well. Formulaic ``template'' papers ($n = 112$)—such as scripts fitting LASSO survival curves to public cancer genes, running default single-cell clustering on two patients, or running automated Mendelian randomization—averaged just $4.16 \pm 1.42$, with 74.1\% failing below 5.0 and 90.2\% below 6.0 ($p = 2.0 \times 10^{-44}$). In one 2025 paper (`PMC11992544`, scoring $1.2/10$), our blinded reviewer even caught an unedited AI chatbot response and internal `artifact\_id` UUID pasted verbatim inside the published Discussion alongside contradictory gene counts.



### Take-Home 5: A Brutally Honest Self-Audit of 164 Career Papers


Anyone proposing an automated critic of scientific papers should put their own career under the exact same microscope—and report the unflattering findings alongside the flattering ones. We downloaded every open-access paper in PubMed Central co-authored by our senior author ([REDACTED_AUTHOR]), totaling 164 papers published between 2004 and 2026 across 58 journals. We stripped out all author names, universities, journal titles, and recognizable lab software names (such as `[LAB_SOFTWARE]`, `[LAB_SOFTWARE]`, and `[LAB_SOFTWARE]`), assigned anonymous IDs, and had the AI review all 164 papers blind (Figure~\ref{fig:selfaudit}, Supplementary Table~S5).

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig5_self_audit_external_audit.pdf}
\caption{Blinded career self-audit of 164 open-access papers by the senior author (2004--2026) separates lead-author studies from middle-author collaborations. Panel A compares blinded scores (/10) when the senior author led the study as First or Senior Author ($n=42$, mean $8.2/10$, $0\%$ failed) versus Middle Co-Author collaborations ($n=122$, mean $7.3/10$, $6.6\%$ failed), alongside benchmark controls ($8.6/10$) and everyday literature ($5.5/10$). Panel B tracks scores over 22 years (2004--2026): lead-author papers (blue circles) stayed above $8.0$ across two decades, while middle-author service collaborations (orange triangles) drifted downward with the broader literature.}
\label{fig:selfaudit}
\end{figure}

At a high level, the 164 papers averaged $7.5 \pm 1.4$ out of 10 (median 7.9), and scores split sharply by authorship role (Figure~\ref{fig:selfaudit}A). Across the 42 papers where our senior author served as First Author ($n = 10$, mean $8.3$) or Senior/Last Author ($n = 32$, mean $8.2$), the combined average was $8.2 \pm 1.1$ (median 8.5), with zero papers below the strict 5.0 failure cutoff and 76\% scoring 8.0 or higher. Across the 122 papers where the senior author served as a Middle Co-Author—typically contributing a phylogenetic or bioinformatic analysis to a broader experimental team—the average dropped nearly a full point to $7.3 \pm 1.4$ ($p = 3.0 \times 10^{-5}$), including all 8 papers that failed below 5.0 and 20 of the 23 papers that scored below 6.0. Over 22 years (Figure~\ref{fig:selfaudit}B), lead-author studies stayed steady above 8.0, whereas middle-author collaborations drifted down from 7.6 in 2004--2010 to 6.8 in 2021--2026.

Yet the most instructive part of this self-audit is where our own papers fell short. Even among the 42 lead-author studies, the blinded AI flagged three papers (7.1\%) in the 5.0--5.4 major-flaw zone and uncovered embarrassing errors that had slipped past both our own proof-reading and journal peer review.

-  **Spreadsheet copy-paste errors and unvalidated heuristics (Score 5.0/10, Senior Author, 2024):** In a paper introducing an automated tool for choosing genetic distance cutoffs in HIV transmission networks (`[LAB_SOFTWARE]`, published in *Frontiers in Bioinformatics*), the blinded AI caught severe numerical contradictions across six tables. Two different regional cohorts in Table~2 (Tennessee with 2,750 sequences and Alberta with 808 sequences) had 100\% identical network counts due to a copy-paste error. Another row in Table~2 reported 1,364 connected network nodes for a dataset containing only 295 sequences. Tables~4 and 6 mixed substitutions-per-site with percentages (off by a factor of 100), two paragraphs of step-by-step instructions were pasted twice in the text, and the scoring heuristic relied on arbitrary constants tested without ground-truth epidemic simulations.
-  **A textbook base-rate fallacy on multiple testing (Score 5.2/10, First Author, 2006):** An early *PLOS Computational Biology* study compared HIV-1 evolution between Southern African and Ethiopian cohorts. The AI praised the core phylogenetic branch method, but flagged our claim that 7 out of 296 tested codons were under differential selection at unadjusted $p \le 0.05$. We had argued in the paper that multiple-testing correction was unnecessary because simulated positive predictive value was 98.8\%. The AI pointed out that our simulation planted a high rate of true positives, whereas under a null hypothesis across 296 codon tests, roughly 7 false positives are expected by pure chance—the exact number of sites we reported.
-  **Mistaking alignment gaps for conserved sites and comparing disordered protein tails (Score 5.4/10, Senior Author, 2024):** In a study of mammalian *Rem2* gene evolution in *Frontiers in Bioinformatics*, the AI noted that although human Rem2 is only 340 amino acids long, insertions across 175 mammals stretched the sequence alignment to 627 codons. Our paper misclassified 251 gap-dominated insertion columns as ``invariant nucleotide sites,'' compared full-length `AlphaFold2` models whose root-mean-square deviations were dominated by unaligned disordered tails rather than the folded core, and mixed human genome builds (`hg19` and `hg38`) in the same table column.


The eight middle-author papers that failed below 5.0 (2.2 to 4.8 out of 10) illustrate an equally uncomfortable truth about modern collaborative science: the ``specialist-in-a-silo'' trap. In large multi-center projects, a computational biologist is often handed a sequence alignment or summary table to run a specific tree or selection scan without auditing the upstream laboratory assay or overarching clinical claim. Our blinded AI reviewer ruthlessly flagged the consequences across our own co-authored papers.

-  **Laboratory PCR contamination misread as autumn 2019 SARS-CoV-2 in Italy (Score 2.2/10, Middle Co-Author, 2022):** Our lowest-scoring paper across all 164 studies screened archived rash swabs from Lombardy in *Environmental Research* \cite{Amendola2022}. The blinded AI pointed out that 100\% of the 11 claimed ``pre-pandemic'' 2019 positives tested negative by standard CDC quantitative PCR (`0/11`), had zero neutralizing antibodies (`0/9`), and amplified in only 1 of 4 nested-PCR fragments alongside a positive patient control. Those single amplicons carried derived 2020 European `B.1` mutations, pointing to laboratory amplicon carryover that was then extrapolated backward under a naive molecular clock.
-  **Early decay kinetics misread as ongoing HIV-1 replication under therapy (Score 4.1/10, Middle Co-Author, 2016):** A high-profile *Nature* paper claimed that HIV-1 continues to replicate in lymph nodes during antiretroviral therapy. The blinded AI noted that all three patients were sampled only during the first 6 months after starting treatment (when pre-existing viral diversity is still clearing), after 70 cycles of nested PCR without unique molecular identifiers. Worse, Extended Data Table~2 contained a statistically significant *negative* evolutionary rate and numbers that contradicted the main text.
-  **Circular rooting and epidemic momentum in pandemic genomic studies (Scores 4.2 and 4.5/10, Middle Co-Author, 2021--2022):** A 2021 *Molecular Biology and Evolution* paper on the SARS-CoV-2 progenitor scored 4.2 out of 10. The AI flagged the use of a tumor single-cell mutation-ordering algorithm on geographically skewed pandemic sequences, a $>1\%$ frequency filter that erased early Wuhan diversity, and circular flipping of outgroup states whenever they disagreed with the inferred trail. Similarly, a 2022 *Science Translational Medicine* study predicting future SARS-CoV-2 variants scored 4.5 out of 10. Forecasting whether a mutation will cross $0.1\%$ prevalence in the next 3 months from its current multi-country spread mostly measures ongoing epidemic momentum and passenger hitchhiking rather than *de novo* emergence, compounded by slicing data by retrospective collection dates rather than submission dates.


Running our blinded reviewer on our own 22-year publication record proved two points. Had we run this tool before submission on our own recent senior-author manuscripts, it would have caught every duplicated table row, unit-scaling mix-up, and alignment-gap denominator error before a journal editor ever saw them. And when invited to join a large collaborative study as a middle co-author, auditing the entire draft manuscript—not just one's own methods paragraph—is essential before lending one's name to the masthead.


### Take-Home 6: The Economics of Doing, Reviewing, and Publishing Science—From 4-Cent AI Audits to Billion-Dollar Failures


Four practical economic questions naturally follow from our findings. First, how does the money spent doing the science relate to paper quality—does our blinded AI favor expensive studies over cheap ones, and is there a point of diminishing returns where throwing more grant money at a project stops improving rigor? Second, how does the price of publishing—the Article Processing Charge (APC) billed by open-access journals—relate to the quality of the science inside the paper? Third, how much does it cost in tokens and API fees to review a paper with AI, how does that compare to the cost of human peer-review labor, and what would it cost to audit the entire biomedical literature? Fourth, how do those tiny review costs compare to the real-world financial and scientific waste caused by flawed and irreproducible papers? To answer these questions, we linked all 1,466 unique papers across our cohorts to US National Institutes of Health (NIH) grant records via NIH RePORTER (452 NIH-funded papers total, including 222 in our everyday corpus). We also estimated study production costs, mapped every journal to its open-access APC, and measured exact token counts across all 1,580 reviews (Figure~\ref{fig:economics}, Supplementary Table~S6).

\begin{figure}[t!]
\centering
\includegraphics[width=\textwidth]{figures/fig6_research_and_publishing_economics.pdf}
\caption{The economics of doing and publishing biomedical science across 1,076 everyday full-text papers. Panel A plots blinded quality scores (/10) across unfunded studies and annual NIH grant tiers. Quality reaches an inflection point at 2--3 focused grants (median $\$949\text{k/year}$, scoring $7.63/10$, median $8.00$) before plateauing in mega-grant consortia ($>\$1.5\text{M/year}$, scoring $7.46/10$). Low-cost mathematical and software benchmark controls (purple diamond) average $8.5/10$ ($0\%$ failed), showing no AI bias against inexpensive rigorous science. Panel B compares blinded scores across five journal Article Processing Charge (APC) tiers ($N=1,076$): commercial megajournals ($\sim\$2,880$ APC) average $5.76/10$ ($35\%$ failed), whereas similarly priced academic society journals ($\sim\$3,240$ APC) average $6.48/10$ ($21\%$ failed, $p = 1.1 \times 10^{-8}$).}
\label{fig:economics}
\end{figure}

First, we tested whether the AI is biased against cheap science. When a low-cost study is methodologically rigorous and aligns its claims with its evidence, the AI shows zero bias toward expensive wet-lab work. Within our 50 verified benchmark controls (Cohort B), 14 papers were low-cost mathematical, statistical, or software methods studies written by small teams of two to four researchers with zero wet-lab reagents. Those 14 low-cost controls averaged $8.5 \pm 1.0$ out of 10 (0\% failed), statistically indistinguishable from the 36 expensive multi-assay wet-lab and genomic benchmark studies ($8.7 \pm 0.8$, $p = 0.39$, Figure~\ref{fig:economics}A). Likewise, in our 164-paper career self-audit, low-cost theoretical and software studies led by our lab averaged $8.2$ out of 10, beating our collaborations on expensive clinical and wet-lab cohorts ($7.3/10$). Conversely, the AI does not give expensive studies a pass when their design is broken. In Cohort A (retracted or refuted papers), the 18 NIH-funded studies carried a median grant budget of $\$2.07\text{ million/year}$ (mean $\$3.76\text{ million/year}$), yet the blinded AI scored them at $5.3$ out of 10 ($4.4$ across all 50 Cohort A papers) because no amount of expensive sequencing can rescue missing negative controls.

In everyday empirical biology, however, study budget does matter up to a clear inflection point (Figure~\ref{fig:economics}A, Supplementary Table~S6). When an empirical biology paper makes a causal clinical or mechanistic claim, our rubric demands independent validation (such as a perturbation assay or biological replicates). Unfunded database scripts ($<\$25\text{k}$ cost, $n = 138$) and small dry-lab studies (\$25k--\$100k, $n = 162$) rarely include experimental validation, averaging $5.24 \pm 1.85$ and $5.25 \pm 1.89$ out of 10 ($46\%$ failed). Among the 222 NIH-funded everyday papers, studies supported by a single grant ($<\$600\text{k/year}$, median $\$305\text{k/year}$, $n = 80$) climb to $7.04 \pm 1.57$ (median 7.60, 12.5\% failed). Within that group, fellowships and R21 awards ($<\$250\text{k/year}$) average $6.93$, while a standard R01 (\$250k--\$600k/year) averages $7.11$. Quality reaches an inflection point of $7.63 \pm 1.45$ out of 10 (median 8.00, 9.2\% failed) for focused teams supported by two to three grants totaling $\$0.6\text{--}\$1.5\text{ million/year}$ (median $\$949,000\text{/year}$, $n = 76$). Beyond $\sim\$0.95\text{ million/year}$, throwing more grant money at a project yields zero increase in mean quality. Large center and multi-grant consortia ($>\$1.5\text{ million/year}$, median $\$3.20\text{ million/year}$, $n = 66$) plateau at $7.46 \pm 1.13$ out of 10 (median 7.80) and only trim tail failures (1.5\% failed). Counting total acknowledged grants across all 1,076 everyday papers shows the same plateau, climbing from $6.14$ (0 grants, $n = 615$) to $7.35$ (4--6 grants, $n = 51$) and staying flat at $7.35$ for 7 or more grants ($n = 13$).

Comparing journal publication fees (APCs) against paper quality across all 1,076 everyday papers (and 1,176 including calibration) revealed a sharp publisher business-model gap (Figure~\ref{fig:economics}B, Supplementary Table~S6).

-  **The $\$2,900$ megajournal trap vs. academic society value.** Across 459 everyday papers published in commercial APC-driven megajournals (mean APC $\$2,879$, including *PLOS ONE*, *Scientific Reports*, *Frontiers*, *MDPI*, and *BMC* series), the average quality score was $5.76 \pm 1.74$ out of 10. Fully 35.1\% failed below 5.0 and 52.7\% fell below 6.0 ($4.40 \pm 1.50$, 64.9\% failed, in the 2020--2025 Cohort C/OOD slice). Meanwhile, zero-fee diamond open-access journals ($n = 28$) averaged $4.99 \pm 2.11$ (50.0\% failed).
-  **Academic society journals are the best value in science.** Selective academic society and university press journals (mean APC $\$3,242$, $n = 361$, such as *Molecular Biology and Evolution*, *PNAS*, *PLOS Pathogens*, *PLOS Genetics*, *eLife*, and *Nucleic Acids Research*) charge nearly the same fee as commercial megajournals ($\$3,242$ vs.\ $\$2,879$). Yet society journals score $6.48 \pm 1.80$ out of 10 ($+0.72$ points higher, $p = 1.1 \times 10^{-8}$), cut the failure rate from 35.1\% down to 20.5\%, and provide nearly three times more peer-review improvement during revision.
-  **Diminishing returns at $\$11,500$ luxury flagships.** High-APC selective journals charging $\$4,500\text{--}\$7,000$ (mean APC $\$5,579$, $n = 216$, such as *Nature Communications*, *Science Advances*, *Journal of Experimental Medicine*, and *Genome Biology*) average $7.62 \pm 1.17$ out of 10 (3.2\% failed). Ultra-luxury commercial flagships charging $\$9,500\text{--}\$12,290$ (mean APC $\$11,528$, $n = 12$ in wild, $n = 51$ across all 1,176 papers, such as *Nature*, *Science*, and *Cell*) charge more than double that fee (an extra $\$5,950$ per paper) for a non-significant $+0.18$-point difference in the wild ($7.80 \pm 1.49/10$, $p = 0.69$, or $7.82 \pm 1.75$ across $n = 51$ overall). Even more telling, among our 50 verified benchmark controls (Cohort B), papers published in $\$3,230$-APC society journals scored $8.74 \pm 0.47$, slightly beating benchmark controls published in $\$11,738$-APC luxury flagships ($8.65 \pm 0.80$).


We next measured the exact token consumption and computational cost of our blinded AI reviewer across all 1,480 scrubbed manuscripts and 1,568 generated review dossiers, and compared those figures against human peer-review labor and the cost of auditing all of PubMed (Supplementary Table~S6).

-  **Token and API cost to AI-review a paper (4.1 to 8.7 cents) and extrapolation to all of PubMed.** Across our 1,480 scrubbed full-text manuscripts, the average input text contained $44,023$ characters ($6,958$ words, or $11,585$ tokens; median $10,760$ tokens), plus $3,807$ cacheable rubric tokens, for a mean input of $15,392$ tokens per review. Each generated review dossier averaged $8,083$ characters ($1,100$ words, or $2,127$ visible tokens) plus $\sim 4,600$ internal reasoning tokens, totaling $6,727$ output tokens and $22,119$ total tokens per review. At standard frontier pricing (\$1.25 per million input tokens and \$10.00 per million output tokens), a single-pass blinded review costs \$0.087 (8.65 cents) on-demand, or \$0.041 (4.14 cents) using Batch API with context caching. A 3-run consensus ensemble costs \$0.124 in Batch mode (\$0.260 on-demand), and our entire 1,580-review study cost \$65.41 in Batch mode (\$136.67 on-demand). Extrapolating to the biomedical literature, auditing every open-access paper deposited in PubMed Central in 2025 ($921,565$ articles, $20.4\text{ billion}$ tokens) would cost \$38,109 per year in Batch mode (\$79,727 on-demand). Auditing the entire annual flow of PubMed in 2025 ($1,965,335$ articles, $43.5\text{ billion}$ tokens) would cost just \$81,272 per year in Batch mode (\$170,025 on-demand)—roughly the APCs of seven luxury flagship papers ($7 \times \$11,528$, or \$243,815 for a 3-run Batch ensemble). Auditing the entire historical full-text archive of PubMed Central ($10.9\text{ million}$ articles, $241\text{ billion}$ tokens) would cost \$450,743 in Batch mode (\$942,982 on-demand). Even auditing all $39.4\text{ million}$ papers indexed in PubMed since 1781 ($872\text{ billion}$ tokens) would cost \$1.63 million in Batch mode (\$3.41 million on-demand), roughly the budget of one five-year NIH R01 grant.
-  **Human peer-review labor (15 hours and \$1,505 per paper vs. \$0.04 AI).** Across our 100 open-review papers, human peer review required an average of $2.61$ referees per published paper across revision rounds, producing a median of $3,213$ referee words. Anchored in published peer-review time surveys ($\sim 5.0\text{ hours}$ per referee plus $2.0\text{ hours}$ of editorial handling) \cite{Aczel2021}, a typical paper consumes $15.05\text{ hours}$ of senior researcher time. At a conservative loaded academic labor rate of \$100 per hour, human peer review costs \$1,505 per paper. Across the $1.97\text{ million}$ annual PubMed articles, human peer review consumes $29.6\text{ million hours}$, or \$2.96 billion per year (\$100/hour) \cite{Aczel2021}. A blinded AI pre-screen (\$0.041 to \$0.087, taking under three minutes) is $17,400\times$ to $36,400\times$ cheaper than human referee labor and $33,300\times$ to $69,500\times$ cheaper than a \$2,879 megajournal APC ($\sim\$3,000$). Yet it recalls 97.9\% of unresolved human critiques and catches $3.85$ additional quantitative flaws per paper.
-  **The billion-dollar cost of academic failures vs. a 4-cent pre-screen.** The tiny cost of automated methodological auditing stands in stark contrast to the financial and clinical waste of flawed science. Within our Cohort~A ($N = 50$ retracted or refuted papers), the 18 NIH-funded studies sat atop \$67.68 million per year in active NIH grant portfolios (mean \$3.76 million, median \$2.07 million across 73 NIH grants, or \$1.03M+ per grant). Four contaminated low-biomass tumor and placental microbiome papers (`A16`--`A18` and `A27`) sat atop \$31.85 million per year in NIH grant portfolios and spawned a \$17.5 million venture-backed cancer liquid-biopsy startup (*Micronoma*) before reanalysis revealed human genome mapping errors and reagent contamination \cite{Poore2020,Gihawi2023}. Across our 1,076 everyday papers, studies failing below 5.0 ($n = 256$) consumed \$42.4 million per year in linked NIH grant portfolios and \$830,000 in APCs inside our sample alone. Extrapolated across PubMed Central, funders spend \$0.9 billion to \$1.2 billion per year globally on APCs just to publish methodologically failing open-access papers. In the broader literature, 149 papers retracted for misconduct consumed \$58 million in direct NIH grant funds (\~{}\$392,500 per retracted paper) \cite{Stern2014}, and the retracted Anversa cardiac stem-cell franchise consumed over \$50 million in NIH funding and triggered a \$10 million federal fraud settlement. More broadly, irreproducible preclinical research wastes an estimated \$28.2 billion per year in the United States ($\sim 50\%$ irreproducibility rate, mirroring our $43\%\text{--}55\%$ contemporary failure rate, or \$14B+ in downstream clinical waste) and derails $89\%$ ($47/53$) of landmark oncology targets during pharmaceutical validation \cite{Begley2012,Freedman2015}.



## Discussion


Scientific publishing currently lacks an automated quality floor. Across 1,580 full-text reviews of 1,466 unique papers, we showed that a blinded AI reviewer—stripped of author names, institutions, journal titles, and dates—can separate verified sound science from retracted or refuted studies with 97\% to 99\% accuracy. It achieved zero false rejections of sound benchmark controls at the 5.0-point threshold and more than twice the test-retest consistency of human referees. Applying this calibrated yardstick to 1,176 everyday full-text biomedical papers published between 1991 and 2025 (1,076 longitudinal and cross-field papers plus 100 open-review papers) yielded six clear lessons.

-  **Blinding matters.** Famous authors and flagship journals enjoy a $+0.35$-point prestige halo that disappears when metadata are stripped.
-  **Roughly half of recent papers fail on rigor.** Between 35\% and 55\% of 2020--2025 papers across our cohorts score below 5.0 (and over half below 6.0), with the worst failure rates in fields dominated by unverified data-mining templates and contamination-prone assays.
-  **Peer review works at selective journals, not megajournals.** Revisions at selective flagship and society journals improve papers nearly three times more ($+0.59$ vs. $+0.22$ Core points) than revisions at open-access megajournals. Across 100 open-review papers ($7.49/10$ selective vs.\ $5.01/10$ megajournal), our blinded AI recalled 97.9\% ($95/97$) of unresolved human critiques while catching 385 additional flaws and exposing severe referee anomalies (boilerplate checklists, coercive citation demands, or single-reviewer acceptances) in 58\% of megajournal review files compared to just 2\% at selective journals.
-  **Ecosystem shifts drove the 35-year quality decline.** Across 915 verified full-text date-blinded papers from 1991 to 2025, overall literature quality dropped by $1.82$ points between the 1990s ($7.63$) and 2020s ($5.81$). Most of that decline ($54\%\text{--}58\%$) came from the expansion of commercial megajournals, secondary database mining, and formulaic study templates, whereas within-journal drift was modest ($-0.23$ points/decade).
-  **Self-auditing works.** On 164 papers by our senior author, blinded review clearly separated lead-author studies ($8.2/10$, 0\% failed) from middle-author service collaborations ($7.3/10$) while catching embarrassing table and multiple-testing errors in our own work.
-  **Smart funding, society journals, and 4-cent AI pre-screens beat mega-grants, luxury APCs, and billion-dollar failures.** Research quality reaches an inflection point at focused 2--3 grant support ($\sim\$0.95\text{M/year}$, scoring $7.63$) before plateauing in mega-consortia ($7.46/10$), while $\$3,242$ society journals achieve significantly higher rigor than $\$2,879$ commercial megajournals ($6.48$ vs. $5.76/10$) and match $\$11,500$ luxury flagships on benchmark science. Meanwhile, a blinded AI review requires $22,119$ tokens and costs $4.1$ to $8.7$ cents per paper—making it $\sim 17,400\times$ to $36,400\times$ cheaper than human peer-review labor (\$1,505 per paper) and enabling an audit of the entire annual flow of PubMed ($1.97\text{ million}$ papers) for \$81,272 per year.



### Why Do Some Flawed Papers Get Highly Cited? Four Archetypes of Highly Cited Failures


Although higher-scoring papers earn more citations on average, citation count alone is a poor proxy for technical validity. We set aside our 50 Cohort~A training negatives (which were deliberately chosen as famous retracted or refuted papers) and examined every paper across our remaining 1,416 unique manuscripts that failed below 5.0 out of 10 yet accumulated heavy citation counts. Twelve failing papers accumulated $\ge 100$ citations and 27 accumulated $\ge 50$ citations (all browsable via the ``Highly Cited Failures'' filter at `[REDACTED_REPOSITORY_URL]`). Almost every highly cited failing paper falls into one of four distinct archetypes:

-  **First-Wave Pandemic and Crisis Gold-Rush Papers ($100\text{--**156$ citations):} During the early months of a public-health emergency, any paper making a bold claim about viral origins or drug repurposing accumulates massive citations before its methods are scrutinized. For example, `TIME\_ANON\_0224` (*Pathogens* 2020, $3.7/10$, 156 citations) claimed that SARS-CoV-2 arose from recombination with MERS-CoV based on an unmasked 7-sequence ClustalW alignment without outgroups or recombination tests. Similarly, `TIME\_ANON\_0922` (*BMB Reports* 2020, $2.2/10$, 139 citations) docked Lopinavir and Ritonavir simultaneously into the SARS-CoV-2 protease pocket as if two bulky drugs ($\sim 1,350\text{ Da}$ combined) could bind the same active site at once, while `SP\_ANON\_103` (*Environmental Research* 2022, $2.2/10$, 55 citations) mistook nested-PCR carryover for autumn 2019 COVID-19 cases in Italy \cite{Amendola2022}.
-  **Useful Gene-Family Catalogs Paired With Broken Downstream Math ($73\text{--**158$ citations):} Many genome-era papers are cited not for their statistical conclusions, but because Table~1 provides the first convenient list or nomenclature of a gene family in a model organism. For example, `TIME\_ANON\_08` (*BMC Evolutionary Biology* 2005, $4.8/10$, 158 citations) cataloged vertebrate relaxin-family peptide genes—earning lasting citations for its sequence inventory—yet its evolutionary analysis plotted PAML's `dN/dS = 99` error code (which simply flags division by zero when synonymous divergence $d_S = 0$) as literal positive selection ($\omega = 99$). Likewise, `TIME\_ANON\_0105` (*BMC Genomics* 2008, $4.6/10$, 110 citations) and `TIME\_ANON\_0605` (*BMC Genomics* 2016, $4.9/10$, 73 citations) provided useful gene inventories while suffering from severe alignment-gap artifacts or even leaving a copy-pasted ``MAPK gene family'' sentence inside the conclusion of a foxtail millet *MYB* paper.
-  **Prestige-Halo Provocative Claims in Flagship or Early Specialist Venues ($62\text{--**556$ citations):} When a striking biological claim appears in a prestigious journal, it attracts hundreds of citations from both uncritical reviews and subsequent refutation studies. For instance, `SP\_ANON\_109` (*Nature* 2016, $4.1/10$, 556 citations) claimed ongoing HIV-1 replication under antiretroviral therapy based on early 6-month decay samples and a table containing a negative evolutionary rate. Similarly, `TIME\_ANON\_0867` (*Molecular Cancer* 2004, $4.5/10$, 111 citations) claimed in its title that cisplatin induces *de novo* promoter methylation in vivo, even though $0$ of $18$ genes became hypermethylated when cells were treated with cisplatin. Another example, `TIME\_ANON\_0493` (*Nature Communications* 2015, $4.5/10$, 62 citations), inferred brain-region adaptive evolution from 3-taxon branch tests without multiple-testing correction.
-  **Modern Buzzword-Combo Templates Cited by Other Template Papers ($15\text{--**39$ citations/year):} In the 2024--2025 literature, a new citation engine has emerged around papers that chain together single-cell RNA-seq, two-sample Mendelian randomization, LASSO Cox prognostic signatures, and molecular docking. Studies such as `C21` ($2.8/10$, 39 citations in one year) and `C86` ($4.4/10$, 36 citations) are rapidly cited as boilerplate introduction references by hundreds of other cookie-cutter papers running the exact same pipeline.



### Guardrails and a Three-Part Prescription for Scientific Publishing


At the same time, our study establishes three practical guardrails for using AI reviewers responsibly, building on recent studies of automated screening \cite{Nuijten2016,Brown2017,Weissgerber2021} and LLM peer-review benchmarks \cite{Checco2021,Liang2024,Brian2026}. First, previous LLM studies either evaluated unblinded manuscripts to see if AI comments resemble human referee prose \cite{Liang2024} or tested open-ended prompts on clinical trials seeded with checklist flaws \cite{Schroter2008,Brian2026}. Our results show that de-identification, workspace isolation, and benchmark calibration are mandatory whenever AI is used to score rigor; otherwise models reward author and journal prestige just as human referees do \cite{Tomkins2017,Huber2022} or over-flag 25\% to 29\% of clean control papers. Second, a text-only AI reviewer has clear blind spots: it cannot detect manipulated western blots or spliced microscopy images, and it cannot see hidden ancestry biases inside external consortium databases when a paper's internal math looks sound. Third, scoring rubrics and score cutoffs must be calibrated to domain norms and to each specific AI model. When an outside colleague tested an early version of our rubric (`v1.0`) on 10 human genome assembly papers using a different AI model (`Claude Opus`), the model unfairly penalized studies that placed human DNA reads in privacy-protected repositories (such as dbGaP or UK Biobank) or included small exploratory side analyses. We updated our rubric (`v1.1`) so that legally required controlled-access repositories receive full data-sharing credit and resource papers are judged on their primary technical product, and any team adopting a new AI model should re-anchor cutoffs against Cohort A and Cohort B benchmark controls before use.

Subject to those guardrails, our findings point to three concrete steps for authors, journals, and funders:

-  **For Authors—Pre-Submission Auditing and Co-Author Due Diligence:** Running a blinded AI audit on a draft manuscript takes less than three minutes and catches duplicated table rows, inverted odds ratios, degrees-of-freedom mismatches, and overstated titles before submission. Equally important, as our 164-paper self-audit showed, specialists invited to join a large collaboration as a middle co-author should run a full-text audit on the entire draft—not just their own methods section—before lending their name to a paper.
-  **For Journals and Scientific Societies—Automated Table/Math Verification and Referee Quality Control:** Human referees excel at judging conceptual novelty and experimental nuance, but they routinely miss arithmetic contradictions in tables and equations—and in megajournals, 58\% of review files suffer from boilerplate checklists, coercive citation demands, or single-reviewer sign-offs. Academic journals can pair human referees with a standardized, blinded AI pre-screen that checks internal table math, statistical degrees of freedom, and revision-induced errors while automatically flagging coercive self-citation demands or copy-pasted boilerplate in incoming human referee reports.
-  **For Funders and Universities—Rewarding Methodological Rigor Over Volume and Mega-Scale:** Research quality peaks at focused 2--3 grant support ($\sim\$0.95\text{M/year}$), and $\$3,242$ academic society journals outperform $\$2,879$ commercial megajournals by $+0.72$ points while matching $\$11,500$ luxury flagships on benchmark rigor. Funding agencies and hiring committees should stop counting raw paper volume or journal impact factors, and instead support a broader base of focused research teams publishing in rigorous academic society venues.



## Methods



### Study Design and Paper Sampling


We conducted six coordinated experiments totaling 1,580 full-text reviews of 1,466 unique open-access biomedical articles from PubMed Central and Europe PubMed Central (Table~\ref{tab:overview}). In Experiment~1 (Calibration), we assembled 200 papers across five core fields (viral evolution, cancer and microbiome, statistical genetics, single-cell transcriptomics, and molecular evolution): 50 papers retracted or refuted for documented methodological flaws (Cohort A), 50 verified sound benchmark controls (Cohort B), and 100 uncurated everyday papers published between 2020 and 2025 (Cohort C). We first ran a 75-paper pilot (in both unblinded and blinded modes) and then locked our scoring thresholds (`< 5.0` for fundamental flaws, `< 6.0` for major flaws) before testing on a strictly held-out 125-paper expansion set.

In Experiment~2 (Repeatability), 30 papers (10 each from Cohorts A, B, and C) were reviewed blind three separate times under fresh anonymous IDs (90 reviews). In Experiment~3 (Out-of-Distribution Generalization), we audited 60 recent papers (2020--2025, 20 per field) across three unseen fields: ecology and macroevolution, neuroscience and neuroimaging, and AI drug discovery. In Experiment~4 (Peer Review Value-Added and Open-Review Concordance), we first audited 20 matched pairs of version-1 preprints and their final published articles (40 blinded texts) across selective flagship journals ($n=5$), selective society journals ($n=5$), and open-access megajournals ($n=10$). We then expanded the human-vs.-AI comparison to a balanced cohort of 100 open-review articles published between 2020 and 2025 (`OPEN\_ANON\_001`--`OPEN\_ANON\_100`, 10 per subfield across our five core domains). Fifty articles came from selective flagship or society open-review venues (*eLife*, *PLOS Biology*, *PLOS Genetics*, *PLOS Pathogens*, and *PLOS Computational Biology*) and 50 came from open-review megajournals (*PLOS ONE*), each paired with its verbatim human referee reports ($\ge 2.5\text{ KB}$, 261 distinct human reviewers and 363 substantive critiques total). Blinded Stage~1 AI reviews were locked before Stage~2 concordance auditing against the human referee reports. In Experiment~5 (35-Year Secular Trend and Economics), we sampled 1,000 date-blinded papers across seven 5-year windows from 1991--1995 to 2021--2025 and four biomedical subfield tracks, and strictly excluded 85 archival 1990s/early-2000s records whose Europe PMC XML lacked main body text ($N = 915$ verified full-text articles, $226\text{--}233$ per track). We combined these 915 papers with our 161 recent wild papers to analyze study design drivers, within-journal fixed effects, Oaxaca--Blinder decompositions, NIH RePORTER grant awards, and journal APCs across 1,076 everyday full-text papers (and 1,176 including calibration controls). In Experiment~6 (Blinded Self-Audit), we audited all 164 open-access papers co-authored by the senior author between 2004 and 2026, comparing First/Senior lead-author papers ($n=42$) against middle-author collaborations ($n=122$).


### Blinding Pipeline, Scoring Rubric, and Statistical Summary


To guarantee strict blinding, our automated preprocessor extracts the full text, equations, and tables (including Data Availability notes in back-matter tags) from each manuscript's XML or HTML file and removes the article title, author names, affiliations, journal name, volume/page numbers, web identifiers (DOIs, PMIDs, PMCIDs, author GitHub links), and any retraction notices. For the 100 open-review manuscripts, decision letters and reviewer sub-articles are stripped prior to Stage~1 review. For the 35-year trend and career self-audit, the scrubber also strips all 4-digit years and recognizable lab software names. Each scrubbed document is graded by an isolated instance of `gemini-4-argon` with web search disabled using our standardized template (`REVIEW\_TEMPLATE.md` `v1.1`).

The rubric grades each paper out of 10.0 points across four categories: Methodological Rigor and Statistical Validity (3.5 points), Claim-Evidence Alignment (2.5 points), Biological Plausibility (2.0 points), and Reproducibility and Data Integrity (2.0 points). Summing the first three categories gives the 8.0-point Scientific Core, which measures scientific quality independently of modern open-data links. All statistical comparisons—including receiver operating characteristic curves, prevalence adjustments \cite{RoganGladen1978}, test-retest intraclass correlation coefficients \cite{ShroutFleiss1979}, paired preprint-to-published $t$-tests and Wilcoxon tests, within-journal fixed-effect regressions, and Oaxaca--Blinder decompositions—were run in Python 3.11. Complete mathematical equations, XML scrubber specifications, and full sensitivity tables (Tables S1--S7) are provided in the Supplementary Information.


### Data Availability and Ethics


This study analyzed only publicly available, open-access scientific texts from PubMed Central and Europe PubMed Central. No human subjects or biological samples were involved. All 1,580 review dossiers, verbatim human referee reports, Stage~2 concordance matrices, scrubbed inputs, metadata tables, and analysis scripts are openly available under MIT and CC-BY-4.0 licenses at `[REDACTED_REPOSITORY_URL]` and interactively searchable at `[REDACTED_REPOSITORY_URL]`.


### AI Disclosure Statement


Large language models are both the subject of this research and a tool used to conduct it. All 1,580 blinded manuscript evaluations and Stage~2 human-concordance audits were generated by isolated instances of `gemini-4-argon` (`Gemini 3.1 Pro`) operating inside the Antigravity agentic harness under the human authors' direct experimental design and rubric (`REVIEW\_TEMPLATE.md` `v1.1`). We also used `gemini-4-argon` inside the Antigravity coding environment to assist with writing Python data-processing, statistical analysis, and figure-plotting scripts, building the interactive web explorer, and drafting and editing portions of the manuscript text and tables. Every analysis script, statistical output, review sample, and manuscript paragraph was inspected, verified, and edited by the human authors, who take full responsibility for the integrity and accuracy of the work.


\begin{thebibliography}{99}
\bibitem{Ioannidis2005} Ioannidis, John P. A. (2005). Why Most Published Research Findings Are False. *PLoS Medicine*, 2(8), e124. doi:10.1371/journal.pmed.0020124
\bibitem{Salter2014} Salter, Susannah J, Cox, Michael J, Turek, Elena M, Calus, Szymon T, Cookson, William O, Moffatt, Miriam F, Turner, Paul, Parkhill, Julian, Loman, Nicholas J, Walker, Alan W (2014). Reagent and laboratory contamination can critically impact sequence-based microbiome analyses. *BMC Biology*, 12(1). doi:10.1186/s12915-014-0087-z
\bibitem{deGoffau2019} de Goffau, Marcus C., Lager, Susanne, Sovio, Ulla, Gaccioli, Francesca, Cook, Emma, Peacock, Sharon J., Parkhill, Julian, Charnock-Jones, D. Stephen, Smith, Gordon C. S. (2019). Human placenta has no microbiome but can contain potential pathogens. *Nature*, 572(7769), 329-334. doi:10.1038/s41586-019-1451-5
\bibitem{Kennedy2023} Kennedy, Katherine M., de Goffau, Marcus C., Perez-Muñoz, Maria Elisa, Arrieta, Marie-Claire, Bäckhed, Fredrik, Bork, Peer, Braun, Thorsten, Bushman, Frederic D., Dore, Joel, de Vos, Willem M., Earl, Ashlee M., Eisen, Jonathan A., Elovitz, Michal A., Ganal-Vonarburg, Stephanie C., Gänzle, Michael G., Garrett, Wendy S., Hall, Lindsay J., Hornef, Mathias W., Huttenhower, Curtis, Konnikova, Liza, Lebeer, Sarah, Macpherson, Andrew J., Massey, Ruth C., McHardy, Alice Carolyn, Koren, Omry, Lawley, Trevor D., Ley, Ruth E., O’Mahony, Liam, O’Toole, Paul W., Pamer, Eric G., Parkhill, Julian, Raes, Jeroen, Rattei, Thomas, Salonen, Anne, Segal, Eran, Segata, Nicola, Shanahan, Fergus, Sloboda, Deborah M., Smith, Gordon C. S., Sokol, Harry, Spector, Tim D., Surette, Michael G., Tannock, Gerald W., Walker, Alan W., Yassour, Moran, Walter, Jens (2023). Questioning the fetal microbiome illustrates pitfalls of low-biomass microbial studies. *Nature*, 613(7945), 639-649. doi:10.1038/s41586-022-05546-8
\bibitem{Sohail2019} Sohail, Mashaal, Maier, Robert M, Ganna, Andrea, Bloemendal, Alex, Martin, Alicia R, Turchin, Michael C, Chiang, Charleston WK, Hirschhorn, Joel, Daly, Mark J, Patterson, Nick, Neale, Benjamin, Mathieson, Iain, Reich, David, Sunyaev, Shamil R (2019). Polygenic adaptation on height is overestimated due to uncorrected stratification in genome-wide association studies. *eLife*, 8. doi:10.7554/elife.39702
\bibitem{Berg2019} Berg, Jeremy J, Harpak, Arbel, Sinnott-Armstrong, Nasa, Joergensen, Anja Moltke, Mostafavi, Hakhamanesh, Field, Yair, Boyle, Evan August, Zhang, Xinjun, Racimo, Fernando, Pritchard, Jonathan K, Coop, Graham (2019). Reduced signal for polygenic adaptation of height in UK Biobank. *eLife*, 8. doi:10.7554/elife.39725
\bibitem{Zaidi2020} Zaidi, Arslan A, Mathieson, Iain (2020). Demographic history mediates the effect of stratification on polygenic scores. *eLife*, 9. doi:10.7554/elife.61548
\bibitem{Squair2021} Squair, Jordan W., Gautier, Matthieu, Kathe, Claudia, Anderson, Mark A., James, Nicholas D., Hutson, Thomas H., Hudelle, Rémi, Qaiser, Taha, Matson, Kaya J. E., Barraud, Quentin, Levine, Ariel J., La Manno, Gioele, Skinnider, Michael A., Courtine, Grégoire (2021). Confronting false discoveries in single-cell differential expression. *Nature Communications*, 12(1). doi:10.1038/s41467-021-25960-2
\bibitem{Zimmerman2021} Zimmerman, Kip D., Espeland, Mark A., Langefeld, Carl D. (2021). A practical solution to pseudoreplication bias in single-cell studies. *Nature Communications*, 12(1). doi:10.1038/s41467-021-21038-1
\bibitem{Li2022} Li, Yumei, Ge, Xinzhou, Peng, Fanglue, Li, Wei, Li, Jingyi Jessica (2022). Exaggerated false positives by popular differential expression methods when analyzing human population samples. *Genome Biology*, 23(1). doi:10.1186/s13059-022-02648-4
\bibitem{Poore2020} Poore, Gregory D., Kopylova, Evguenia, Zhu, Qiyun, Carpenter, Carolina, Fraraccio, Serena, Wandro, Stephen, Kosciolek, Tomasz, Janssen, Stefan, Metcalf, Jessica, Song, Se Jin, Kanbar, Jad, Miller-Montgomery, Sandrine, Heaton, Robert, Mckay, Rana, Patel, Sandip Pravin, Swafford, Austin D., Knight, Rob (2020). RETRACTED ARTICLE: Microbiome analyses of blood and tissues suggest cancer
diagnostic approach. *Nature*, 579(7800), 567-574. doi:10.1038/s41586-020-2095-1
\bibitem{Gihawi2023} Gihawi, Abraham, Ge, Yuchen, Lu, Jennifer, Puiu, Daniela, Xu, Amanda, Cooper, Colin S., Brewer, Daniel S., Pertea, Mihaela, Salzberg, Steven L. (2023). Major data analysis errors invalidate cancer microbiome findings. *mBio*, 14(5). doi:10.1128/mbio.01607-23
\bibitem{Wei2019} Wei, Xinzhu, Nielsen, Rasmus (2019). CCR5-∆32 is deleterious in the homozygous state in humans. *Nature Medicine*, 25(6), 909-910. doi:10.1038/s41591-019-0459-6
\bibitem{Maier2020} Maier, Robert, Akbari, Ali, Wei, Xinzhu, Patterson, Nick, Nielsen, Rasmus, Reich, David (2019). No statistical evidence for an effect of CCR5-∆32 on lifespan in the UK Biobank cohort. *Nature Medicine*, 26(2), 178-180. doi:10.1038/s41591-019-0710-1
\bibitem{Cicchetti1991} Cicchetti, Domenic V. (1991). The reliability of peer review for manuscript and grant submissions: A cross-disciplinary investigation. *Behavioral and Brain Sciences*, 14(1), 119-135. doi:10.1017/s0140525x00065675
\bibitem{Marsh2008} Marsh, Herbert W., Jayasinghe, Upali W., Bond, Nigel W. (2008). Improving the peer-review process for grant applications: Reliability, validity, bias, and generalizability.. *American Psychologist*, 63(3), 160-168. doi:10.1037/0003-066x.63.3.160
\bibitem{Amendola2022} Amendola, Antonella, Canuti, Marta, Bianchi, Silvia, Kumar, Sudhir, Fappani, Clara, Gori, Maria, Colzani, Daniela, [REDACTED_AUTHOR], Miura, Sayaka, Baggieri, Melissa, Marchi, Antonella, Borghi, Elisa, Zuccotti, Gianvincenzo, Raviglione, Mario C., Magurano, Fabio, Tanzi, Elisabetta (2022). Molecular evidence for SARS-CoV-2 in samples collected from patients with morbilliform eruptions since late 2019 in Lombardy, northern Italy. *Environmental Research*, 215, 113979. doi:10.1016/j.envres.2022.113979
\bibitem{Tang2020} Tang, Xiaolu, Wu, Changcheng, Li, Xiang, Song, Yuhe, Yao, Xinmin, Wu, Xinkai, Duan, Yuange, Zhang, Hong, Wang, Yirong, Qian, Zhaohui, Cui, Jie, Lu, Jian (2020). On the origin and continuing evolution of SARS-CoV-2. *National Science Review*, 7(6), 1012-1023. doi:10.1093/nsr/nwaa036
\bibitem{Forster2020} Forster, Peter, Forster, Lucy, Renfrew, Colin, Forster, Michael (2020). Phylogenetic network analysis of SARS-CoV-2 genomes. *Proceedings of the National Academy of Sciences*, 117(17), 9241-9243. doi:10.1073/pnas.2004999117
\bibitem{Aykut2019} Aykut, Berk, Pushalkar, Smruti, Chen, Ruonan, Li, Qianhao, Abengozar, Raquel, Kim, Jacqueline I., Shadaloey, Sorin A., Wu, Dongling, Preiss, Pamela, Verma, Narendra, Guo, Yuqi, Saxena, Anjana, Vardhan, Mridula, Diskin, Brian, Wang, Wei, Leinwand, Joshua, Kurz, Emma, Kochen Rossi, Juan A., Hundeyin, Mautin, Zambrinis, Constantinos, Li, Xin, Saxena, Deepak, Miller, George (2019). The fungal mycobiome promotes pancreatic oncogenesis via activation of MBL. *Nature*, 574(7777), 264-267. doi:10.1038/s41586-019-1608-2
\bibitem{Narayanan2022} Narunsky-Haziza, Lian, Sepich-Poore, Gregory D., Livyatan, Ilana, Asraf, Omer, Martino, Cameron, Nejman, Deborah, Gavert, Nancy, Stajich, Jason E., Amit, Guy, González, Antonio, Wandro, Stephen, Perry, Gili, Ariel, Ruthie, Meltser, Arnon, Shaffer, Justin P., Zhu, Qiyun, Balint-Lahat, Nora, Barshack, Iris, Dadiani, Maya, Gal-Yam, Einav N., Patel, Sandip Pravin, Bashan, Amir, Swafford, Austin D., Pilpel, Yitzhak, Knight, Rob, Straussman, Ravid (2022). Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. *Cell*, 185(20), 3789-3806.e17. doi:10.1016/j.cell.2022.09.005
\bibitem{Sebastiani2012} Sebastiani, Paola, Solovieff, Nadia, DeWan, Andrew T., Walsh, Kyle M., Puca, Annibale, Hartley, Stephen W., Melista, Efthymia, Andersen, Stacy, Dworkis, Daniel A., Wilk, Jemma B., Myers, Richard H., Steinberg, Martin H., Montano, Monty, Baldwin, Clinton T., Hoh, Josephine, Perls, Thomas T. (2012). Genetic Signatures of Exceptional Longevity in Humans. *PLoS ONE*, 7(1), e29848. doi:10.1371/journal.pone.0029848
\bibitem{Turchin2012} Turchin, Michael C, Chiang, Charleston WK, Palmer, Cameron D, Sankararaman, Sriram, Reich, David, Hirschhorn, Joel N (2012). Evidence of widespread selection on standing variation in Europe at height-associated SNPs. *Nature Genetics*, 44(9), 1015-1019. doi:10.1038/ng.2368
\bibitem{Berg2014} Berg, Jeremy J., Coop, Graham (2014). A Population Genetic Signal of Polygenic Adaptation. *PLoS Genetics*, 10(8), e1004412. doi:10.1371/journal.pgen.1004412
\bibitem{Starr2020} Starr, Tyler N., Greaney, Allison J., Hilton, Sarah K., Ellis, Daniel, Crawford, Katharine H.D., Dingens, Adam S., Navarro, Mary Jane, Bowen, John E., Tortorici, M. Alejandra, Walls, Alexandra C., King, Neil P., Veesler, David, Bloom, Jesse D. (2020). Deep Mutational Scanning of SARS-CoV-2 Receptor Binding Domain Reveals Constraints on Folding and ACE2 Binding. *Cell*, 182(5), 1295-1310.e20. doi:10.1016/j.cell.2020.08.012
\bibitem{Worobey2022} Worobey, Michael, Levy, Joshua I., Malpica Serrano, Lorena, Crits-Christoph, Alexander, Pekar, Jonathan E., Goldstein, Stephen A., Rasmussen, Angela L., Kraemer, Moritz U. G., Newman, Chris, Koopmans, Marion P. G., Suchard, Marc A., Wertheim, Joel O., Lemey, Philippe, Robertson, David L., Garry, Robert F., Holmes, Edward C., Rambaut, Andrew, Andersen, Kristian G. (2022). The Huanan Seafood Wholesale Market in Wuhan was the early epicenter of the COVID-19 pandemic. *Science*, 377(6609), 951-959. doi:10.1126/science.abp8715
\bibitem{Murrell2012} Murrell, Ben, Wertheim, Joel O., Moola, Sasha, Weighill, Thomas, Scheffler, Konrad, [REDACTED_AUTHOR] (2012). Detecting Individual Sites Subject to Episodic Diversifying Selection. *PLoS Genetics*, 8(7), e1002764. doi:10.1371/journal.pgen.1002764
\bibitem{Murrell2015} Murrell, Ben, Weaver, Steven, Smith, Martin D., Wertheim, Joel O., Murrell, Sasha, Aylward, Anthony, Eren, Kemal, Pollner, Tristan, Martin, Darren P., Smith, Davey M., Scheffler, Konrad, [REDACTED_AUTHOR] (2015). Gene-Wide Identification of Episodic Selection. *Molecular Biology and Evolution*, 32(5), 1365-1371. doi:10.1093/molbev/msv035
\bibitem{KosakovskyPond2020} [REDACTED_AUTHOR], Poon, Art F Y, Velazquez, Ryan, Weaver, Steven, Hepler, N Lance, Murrell, Ben, Shank, Stephen D, Magalis, Brittany Rife, Bouvier, Dave, [AUTHOR_REDACTED], Anton, Wisotsky, Sadie, [REDACTED_AUTHOR], Frost, Simon D W, Muse, Spencer V (2019). [LAB_SOFTWARE] 2.5—A Customizable Platform for Evolutionary Hypothesis Testing Using Phylogenies. *Molecular Biology and Evolution*, 37(1), 295-299. doi:10.1093/molbev/msz197
\bibitem{Minh2020} Minh, Bui Quang, Schmidt, Heiko A, Chernomor, Olga, Schrempf, Dominik, Woodhams, Michael D, von Haeseler, Arndt, Lanfear, Robert (2020). IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era. *Molecular Biology and Evolution*, 37(5), 1530-1534. doi:10.1093/molbev/msaa015
\bibitem{Love2014} Love, Michael I, Huber, Wolfgang, Anders, Simon (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biology*, 15(12). doi:10.1186/s13059-014-0550-8
\bibitem{Field2016} Field, Yair, Boyle, Evan A, Telis, Natalie, Gao, Ziyue, Gaulton, Kyle J., Golan, David, Yengo, Loic, Rocheleau, Ghislain, Froguel, Philippe, McCarthy, Mark I., Pritchard, Jonathan K. (2016). Detection of human adaptation during the past 2000 years. *Science*, 354(6313), 760-764. doi:10.1126/science.aag0776
\bibitem{Nejman2020} Nejman, Deborah, Livyatan, Ilana, Fuks, Garold, Gavert, Nancy, Zwang, Yaara, Geller, Leore T., Rotter-Maskowitz, Aviva, Weiser, Roi, Mallel, Giuseppe, Gigi, Elinor, Meltser, Arnon, Douglas, Gavin M., Kamer, Iris, Gopalakrishnan, Vancheswaran, Dadosh, Tali, Levin-Zaidman, Smadar, Avnet, Sofia, Atlan, Tehila, Cooper, Zachary A., Arora, Reetakshi, Cogdill, Alexandria P., Khan, Md Abdul Wadud, Ologun, Gabriel, Bussi, Yuval, Weinberger, Adina, Lotan-Pompan, Maya, Golani, Ofra, Perry, Gili, Rokah, Merav, Bahar-Shany, Keren, Rozeman, Elisa A., Blank, Christian U., Ronai, Anat, Shaoul, Ron, Amit, Amnon, Dorfman, Tatiana, Kremer, Ran, Cohen, Zvi R., Harnof, Sagi, Siegal, Tali, Yehuda-Shnaidman, Einav, Gal-Yam, Einav Nili, Shapira, Hagit, Baldini, Nicola, Langille, Morgan G. I., Ben-Nun, Alon, Kaufman, Bella, Nissan, Aviram, Golan, Talia, Dadiani, Maya, Levanon, Keren, Bar, Jair, Yust-Katz, Shlomit, Barshack, Iris, Peeper, Daniel S., Raz, Dan J., Segal, Eran, Wargo, Jennifer A., Sandbank, Judith, Shental, Noam, Straussman, Ravid (2020). The human tumor microbiome is composed of tumor type–specific intracellular bacteria. *Science*, 368(6494), 973-980. doi:10.1126/science.aay9189
\bibitem{Rabosky2014} Rabosky, Daniel L. (2014). Automatic Detection of Key Innovations, Rate Shifts, and Diversity-Dependence on Phylogenetic Trees. *PLoS ONE*, 9(2), e89543. doi:10.1371/journal.pone.0089543
\bibitem{RoganGladen1978} ROGAN, WALTER J., GLADEN, BETH (1978). ESTIMATING PREVALENCE FROM THE RESULTS OF A SCREENING TEST. *American Journal of Epidemiology*, 107(1), 71-76. doi:10.1093/oxfordjournals.aje.a112510
\bibitem{ShroutFleiss1979} Shrout, Patrick E., Fleiss, Joseph L. (1979). Intraclass correlations: Uses in assessing rater reliability.. *Psychological Bulletin*, 86(2), 420-428. doi:10.1037/0033-2909.86.2.420
\bibitem{Tomkins2017} Tomkins, Andrew, Zhang, Min, Heavlin, William D. (2017). Reviewer bias in single- versus double-blind peer review. *Proceedings of the National Academy of Sciences*, 114(48), 12708-12713. doi:10.1073/pnas.1707323114
\bibitem{Huber2022} Huber, Jürgen, Inoua, Sabiou, Kerschbamer, Rudolf, König-Kersting, Christian, Palan, Stefan, Smith, Vernon L. (2022). Nobel and novice: Author prominence affects peer review. *Proceedings of the National Academy of Sciences*, 119(41). doi:10.1073/pnas.2205779119
\bibitem{Nuijten2016} Nuijten, Michèle B., Hartgerink, Chris H. J., van Assen, Marcel A. L. M., Epskamp, Sacha, Wicherts, Jelte M. (2016). The prevalence of statistical reporting errors in psychology (1985–2013). *Behavior Research Methods*, 48(4), 1205-1226. doi:10.3758/s13428-015-0664-2
\bibitem{Brown2017} Brown, Nicholas J. L., Heathers, James A. J. (2017). The GRIM Test. *Social Psychological and Personality Science*, 8(4), 363-369. doi:10.1177/1948550616673876
\bibitem{Weissgerber2021} Weissgerber, Tracey, Riedel, Nico, Kilicoglu, Halil, Labbé, Cyril, Eckmann, Peter, ter Riet, Gerben, Byrne, Jennifer, Cabanac, Guillaume, Capes-Davis, Amanda, Favier, Bertrand, Saladi, Shyam, Grabitz, Peter, Bannach-Brown, Alexandra, Schulz, Robert, McCann, Sarah, Bernard, Rene, Bandrowski, Anita (2021). Automated screening of COVID-19 preprints: can we help authors to improve transparency and reproducibility?. *Nature Medicine*, 27(1), 6-7. doi:10.1038/s41591-020-01203-7
\bibitem{Checco2021} Checco, Alessandro, Bracciale, Lorenzo, Loreti, Pierpaolo, Pinfield, Stephen, Bianchi, Giuseppe (2021). AI-assisted peer review. *Humanities and Social Sciences Communications*, 8(1). doi:10.1057/s41599-020-00703-8
\bibitem{Liang2024} Liang, Weixin, Zhang, Yuhui, Cao, Hancheng, Wang, Binglu, Ding, Daisy Yi, Yang, Xinyu, Vodrahalli, Kailas, He, Siyu, Smith, Daniel Scott, Yin, Yian, McFarland, Daniel A., Zou, James (2024). Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis. *NEJM AI*, 1(8). doi:10.1056/aioa2400196
\bibitem{Schroter2008} Schroter, Sara, Black, Nick, Evans, Stephen, Godlee, Fiona, Osorio, Lyda, Smith, Richard (2008). What errors do peer reviewers detect, and does training improve their ability to detect them?. *Journal of the Royal Society of Medicine*, 101(10), 507-514. doi:10.1258/jrsm.2008.080062
\bibitem{Brian2026} Brian, Dominikus, Pereira Hernández, Xavier Isidro, Yin, Hao, Koury, Jeffrey, Rust, Ruslan (2026). Large language models detect methodological errors that human peer review misses in clinical trials. *medRxiv*. doi:10.64898/2026.10.25.26366455
\bibitem{Aczel2021} Aczel, Balazs, Szaszi, Barnabas, Holcombe, Alex O. (2021). A billion-dollar donation: estimating the cost of researchers' time spent on peer review. *Research Integrity and Peer Review*, 6(1), 14. doi:10.1186/s41073-021-00118-2
\bibitem{Stern2014} Stern, Andrew M., Casadevall, Arturo, Steen, R. Grant, Fang, Ferric C. (2014). Financial costs and personal consequences of research misconduct resulting in retracted publications. *eLife*, 3, e02956. doi:10.7554/eLife.02956
\bibitem{Freedman2015} Freedman, Leonard P., Cockburn, Iain M., Simcoe, Timothy S. (2015). The Economics of Reproducibility in Preclinical Research. *PLOS Biology*, 13(6), e1002165. doi:10.1371/journal.pbio.1002165
\bibitem{Begley2012} Begley, C. Glenn, Ellis, Lee M. (2012). Drug development: Raise standards for preclinical cancer research. *Nature*, 483(7391), 531-533. doi:10.1038/483531a
\end{thebibliography}

---

# Supplementary Information & Tables

## Supplementary Methods and Technical Specifications



### S1. Corpus Construction and Locus Definitions


For Experiment 1 (Calibration, $N = 200$), we constructed three cohorts across five biomedical subfields: Viral Evolution, Cancer and Low-Biomass Microbiome, Statistical Genetics, Transcriptomics and Computational Biology, and Molecular Evolution. Cohort A ($N = 50$, 10 per subfield) comprises open-access manuscripts in PubMed Central that were either formally retracted or refuted by peer-reviewed re-analyses demonstrating fatal analytical, contamination, or statistical defects. Each Cohort A entry in `calibration/cohorts\_200.json` records the retraction notice Digital Object Identifier (DOI) or refutation citation and the defect category. It also records three boolean locus indicators distinguishing internal manuscript flaws from upstream consortium data artifacts.

-  `defect\_locus\_giant\_strict` ($N = 47$): Excludes the three height polygenic adaptation studies (`A11`, `A23`, `A24`). Their false-positive selection signals originated in geographic stratification inside upstream GIANT summary statistics.
-  `defect\_locus\_pilot5` ($N = 45$): Excludes the five papers (`A07`, `A11`, `A19`, `A24`, `A25`). Their invalidation depended on external database or simulation artifacts invisible in the manuscript text.
-  `defect\_locus\_broad6` ($N = 44$): Excludes the union of both sets (`A07`, `A11`, `A19`, `A23`, `A24`, `A25`).

Cohort B ($N = 50$, 10 per subfield) comprises verified benchmark manuscripts selected for validated experimental design, mathematical rigor, or definitive forensic correction of prior field-wide errors. Cohort C ($N = 100$, 20 per subfield) was sampled from Europe PubMed Central open-access full-text research articles published between 2020 and 2025 (`OPEN\_ACCESS:y AND PUB\_YEAR:[2020 TO 2025]`). Phase 1 (`ANON\_01` to `ANON\_75`) served as the 75-paper pilot (25 per cohort), and Phase 2 (`ANON\_76` to `ANON\_200`) served as the strictly held-out 125-paper expansion (25 Cohort A, 25 Cohort B, 75 Cohort C).


### S2. Deterministic XML Ingestion and De-Identification Scrubber


Full-text manuscripts were ingested from NCBI PubMed Central and Europe PubMed Central JATS XML and HTML endpoints via `scripts/fetch\_papers.py` and `scripts/build\_deidentified.py`. To prevent inline mathematical parameters from dropping during XML parsing, our parser extracts both `<tex-math>` and `<mml:math>` nodes inside `<inline-formula>` and `<disp-formula>` elements and preserves `<back>` sections containing Data Availability, Code Availability, and Accession notes alongside `<body>`. The deterministic scrubber strips:

-  Article titles, running headers, journal names, volume and issue strings, and copyright footers.
-  All author names, ORCID identifiers, email addresses, institutional affiliations, funding grants, and Acknowledgements or Author Contributions sections.
-  All Digital Object Identifiers, PubMed IDs, PMCIDs, preprint identifiers, and GitHub, GitLab, Zenodo, or Figshare repository URLs carrying author handles.
-  Explicit retraction prefixes (`RETRACTED:`, `WITHDRAWN:`) and inline publisher retraction notices.
-  In temporal-blinding runs (Experiment 5) and self-audit runs (Experiment 6), all 4-digit publication or copyright years and self-identifying laboratory software names (`[LAB_SOFTWARE]`, `[LAB_SOFTWARE]`, `[LAB_SOFTWARE]`).

SHA-256 digests of all scrubbed input files are archived in `repeatability/scrubbed_inputs_sha256.json` and `ood/scrubbed_inputs_sha256.json`.


### S3. Psychometric Scoring Equations and Statistical Estimators


Each scrubbed manuscript was evaluated by an isolated instance of `gemini-4-argon` invoked via stateless subagent contexts (`1` manuscript per context window, `search\_web` disabled) governed by `REVIEW\_TEMPLATE.md` (`v1.1`). The quantitative scorecard sums four dimensions to 10.0 points:
\begin{equation}
S_{\text{total}} = S_{\text{rigor}} \in [0, 3.5] + S_{\text{claims}} \in [0, 2.5] + S_{\text{biology}} \in [0, 2.0] + S_{\text{repro}} \in [0, 2.0],
\end{equation}
alongside the 8.0-point Reproducibility-free Scientific Core:
\begin{equation}
\text{Core}_8 = S_{\text{rigor}} + S_{\text{claims}} + S_{\text{biology}} \in [0, 8.0].
\end{equation}
Across the 200-paper calibration dataset, unweighted equal-dimension summation correlates with $S_{\text{total}}$ at $r = 0.9986$ and alters ROC-AUC by less than $0.0004$.

True defect prevalence $\hat{\pi}_{\text{RG}}$ in wild literature was estimated from observed failure prevalence $p_{\text{obs}}$ using the Rogan-Gladen estimator:
\begin{equation}
\hat{\pi}_{\text{RG}} = \text{clip}_{[0,1]}\!\left(\frac{p_{\text{obs}} + \widehat{\text{Sp}} - 1}{\widehat{\text{Se}} + \widehat{\text{Sp}} - 1}\right).
\end{equation}
Test-retest repeatability across $N$ manuscripts and $K = 3$ waves was quantified via Shrout-Fleiss two-way random-effects absolute-agreement intraclass correlation:
\begin{equation}
\text{ICC}(2,1) = \frac{\text{MS}_R - \text{MS}_E}{\text{MS}_R + (K - 1)\text{MS}_E + \frac{K}{N}(\text{MS}_C - \text{MS}_E)}, \quad \text{ICC}(2,K) = \frac{K \cdot \text{ICC}(2,1)}{1 + (K - 1)\text{ICC}(2,1)},
\end{equation}
where $\text{MS}_R$, $\text{MS}_C$, and $\text{MS}_E$ denote between-paper, between-wave, and residual mean squares, respectively. All metrics are deterministically reproducible via `scripts/verify_repeatability_and_calibration.py`.


### S4. Replication and Blinded Benchmark on Error-Seeded Clinical Trials (Brian et al.\ 2026)


To cross-validate our blinded review architecture against an independent external benchmark, we replicated the computational pipeline and open dataset of Brian, Pereira Hern\'andez, Yin, Koury, and Rust (2026) (`medRxiv 2026.10.25.26366455v2`). Their study evaluated 15 LLMs on historical British Medical Journal test papers from Schroter et al.\ (2008) ($N = 180$ reviews) and 58 randomized clinical trials published in 2026 ($N = 1,391$ reviews across 14 planted error categories: 9 major [`M1--M9`] and 5 minor [`m1--m5`]). Executing their validation scripts (`reproduce.py`, `validate_submission.py`, and `validate_further_trials.py`) reproduced all saved-data tables and statistics with zero discrepancies. At the same time, our audit revealed four critical properties of uncalibrated open-ended LLM peer review.

-  **Severe sensitivity--specificity tradeoff across models:** Across the 15 models tested by Brian et al., sensitivity to planted errors correlated strongly and negatively with specificity on unmodified control manuscripts (Spearman $\rho = -0.771, p = 0.00076$ on the primary 2026 trials; $\rho = -0.757, p = 0.0011$ across all 58 trials). Flagship models with the highest sensitivity (`Opus 5.5`, `Fable 5`, `GPT-6.1 Sol`) falsely flagged $25.2\%$ to $28.6\%$ of the 14 error categories on unmodified control trials (specificity $71.4\%\text{--}74.8\%$), most frequently accusing clean trials of unjustified conclusions (`M7`, $576$ control flags), missing screen-failure reasons (`m2`, $447$ flags), and missing Hawthorne-effect discussions (`m5`, $189$ flags).
-  **Sample-size asymmetry and workspace context leakage in top-ranked models:** Although plotted at the top of the 58-trial comparison in Brian et al.'s Figure~2, `Opus 5.5`, `Fable 5`, and `Opus 5` were evaluated on only $n = 3$ trials in 2026 (`N`, `I`, `M`) and omitted from all 55 expanded trials (`T01--T60`). Moreover, the repository's forensic audit (`reviewer_tool_and_context_audit.json`) discloses that during those initial 3-trial runs, the agent harness loaded a workspace `MEMORY.md` file describing the ``Schroter-2008 replication,'' resulting in $33.3\%$ ($16/48$) of Experiment~1 and $37.5\%$ ($18/48$) of Experiment~2 reasoning traces explicitly referencing ``schroter'' or ``planted'' errors.
-  **Checklist memorization in training weights:** In isolated memory probes (`SupplFigure3_values.csv`), `Opus 5.5` recalled 11 of the 14 official Schroter error types without seeing a manuscript (`Fable 5` and `Opus 5` recalled $7/14$).
-  **Omission of a frontier Gemini Pro model:** While Anthropic and OpenAI were evaluated with flagship reasoning models spending up to $16.3\text{ min}$ and $110,200$ output tokens ($\$2.24\text{/review}$), Google was represented solely by the lightweight fast model `Gemini 3.8 Flash` ($1.4\text{ min}$, $10,100$ tokens, $\$0.045\text{/review}$).


To fill this gap under strict workspace isolation, we reconstructed the clean control and error-seeded versions of the first three expanded 2026 *Nature Medicine* trials from PubMed Central JATS XML (`T01` = `PMC13668674`, `T02` = `PMC13577891`, `T03` = `PMC13668648`). We then evaluated all six blinded manuscripts with `gemini-4-argon` (`Gemini 3.1 Pro`) using Brian et al.'s reviewer prompt plus our calibrated 10-point score block (Table~\ref{tab:supp_rust_replication}).

\newpage

## Supplementary Tables


\begin{table}[ht!]
\centering
\caption{Complete calibration sensitivity matrix across Phase-1 pilot (`ANON\_01--75`), strictly held-out expansion (`A26--A50, B26--B50`), upstream consortium exclusions, `PMC8135569` relabeling, and Cohort B control-composition subsets.}
\label{tab:supp_calibration}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccc}
\toprule
Analysis Stratum & $N_A, N_B$ & Mean A & Mean B & ROC-AUC & $\widehat{\text{Se}}_{<5.0}$ & $\widehat{\text{Sp}}_{<5.0}$ & $\widehat{\text{Se}}_{<6.0}$ & $\widehat{\text{Sp}}_{<6.0}$ \\
\midrule
Full 200-Paper Study (Published) & 50, 50 & $4.42 \pm 1.97$ & $8.64 \pm 0.84$ & 0.9688 & 66.0\% & 100.0\% & 76.0\% & 98.0\% \\
Phase-1 Pilot Only (`ANON\_01--75`) & 25, 25 & $4.26 \pm 2.17$ & $8.25 \pm 1.30$ & 0.9272 & 68.0\% & 96.0\% & 76.0\% & 92.0\% \\
Held-Out Expansion (`A26--50, B26--50`) & 25, 25 & $4.59 \pm 1.78$ & $8.78 \pm 0.85$ & 0.9824 & 64.0\% & 100.0\% & 76.0\% & 100.0\% \\
Strict GIANT Exclusion (Excl. A11, 23, 24) & 47, 50 & $4.18 \pm 1.77$ & $8.64 \pm 0.84$ & 0.9857 & 70.2\% & 100.0\% & 80.9\% & 98.0\% \\
Internal Flaws Only (Excl. 5 Upstream) & 45, 50 & $3.99 \pm 1.54$ & $8.64 \pm 0.84$ & 0.9926 & 75.6\% & 100.0\% & 88.9\% & 98.0\% \\
Broad Upstream Exclusion (Excl. 6 Upstream) & 44, 50 & $3.91 \pm 1.46$ & $8.64 \pm 0.84$ & 0.9955 & 77.3\% & 100.0\% & 90.9\% & 98.0\% \\
Original Pilot Label (`PMC8135569` in B) & 49, 51 & $4.45 \pm 1.99$ & $8.53 \pm 1.12$ & 0.9562 & 65.3\% & 98.0\% & 75.5\% & 96.1\% \\
Excl. 13 Refutation Controls in B & 50, 37 & $4.42 \pm 1.97$ & $8.64 \pm 0.91$ & 0.9635 & 66.0\% & 100.0\% & 76.0\% & 97.3\% \\
Excl. 7 Senior-Author Controls in B & 50, 43 & $4.42 \pm 1.97$ & $8.58 \pm 0.88$ & 0.9635 & 66.0\% & 100.0\% & 76.0\% & 97.7\% \\
Independent Primary Controls Only in B & 50, 31 & $4.42 \pm 1.97$ & $8.56 \pm 0.99$ & 0.9590 & 66.0\% & 100.0\% & 76.0\% & 96.8\% \\
Specialist Society Controls Only in B & 50, 8 & $4.42 \pm 1.97$ & $8.85 \pm 0.56$ & 0.9850 & 66.0\% & 100.0\% & 76.0\% & 100.0\% \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Per-cohort and pooled test-retest repeatability metrics ($N = 30 \times K = 3 = 90$ blinded evaluations). $\text{SD}_e$ denotes the two-way residual error standard deviation.}
\label{tab:supp_repeatability}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{lccccccc}
\toprule
Cohort Stratum & $n \times K$ & $\text{ICC}(2,1)$ & $\text{ICC}(3,1)$ & $\text{ICC}(2,3)$ & $\text{SD}_e$ (pts) & Unanimous $<5.0$ ($\kappa$) & Unanimous $<6.0$ ($\kappa$) \\
\midrule
Cohort C: Uncurated Wild Literature & $10 \times 3$ & 0.8583 & 0.8502 & 0.9479 & 0.630 & 80.0\% (0.729) & 80.0\% (0.659) \\
Cohort A: Retracted / Refuted & $10 \times 3$ & 0.9200 & 0.9330 & 0.9718 & 0.431 & 90.0\% (0.712) & 100.0\% (1.000) \\
Cohort B: Benchmark Controls & $10 \times 3$ & 0.8636 & 0.8997 & 0.9500 & 0.241 & 100.0\% (1.000) & 100.0\% (1.000) \\
Pooled Calibration + Wild Sample & $30 \times 3$ & 0.9671 & 0.9691 & 0.9888 & 0.460 & 90.0\% (0.864) & 93.3\% (0.910) \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Blinded evaluation scores and defect rates across all eight contemporary 2020--2025 wild subfields ($N = 160$), matched preprint-to-published pairs ($N = 20$ pairs $= 40$ texts), and the balanced open-review concordance cohort ($N = 100$ papers, $261$ human referees, $363$ substantive human critiques).}
\label{tab:supp_subfields}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{llccccc}
\toprule
Cohort & Scientific Subfield / Stratum & $n$ & Mean $\pm$ SD & Median (IQR / Core) & $< 5.0$ (\%) & $< 6.0$ / Recall \\
\midrule
In-Domain (C) & Molecular Evolution & 20 & $6.90 \pm 1.51$ & 6.50 (5.40--8.20) & 5.0\% & 35.0\% \\
In-Domain (C) & Viral Evolution & 20 & $5.97 \pm 1.61$ & 6.35 (4.45--7.43) & 35.0\% & 40.0\% \\
In-Domain (C) & Statistical Genetics & 20 & $5.37 \pm 1.57$ & 5.40 (4.47--6.28) & 40.0\% & 65.0\% \\
In-Domain (C) & Cancer \& Microbiome & 20 & $4.78 \pm 1.59$ & 4.60 (4.15--5.60) & 60.0\% & 80.0\% \\
In-Domain (C) & Transcriptomics \& CompBio & 20 & $4.33 \pm 1.56$ & 4.20 (3.50--4.95) & 75.0\% & 85.0\% \\
\cmidrule{1-7}
In-Domain Total & All Cohort C (Equal Weight) & 100 & $5.47 \pm 1.78$ & 5.45 (4.10--6.80) & 43.0\% & 61.0\% \\
\midrule
OOD (Stage 1 / Cons.) & Ecology \& Macroevolution & 20 & $5.33$ / $5.19$ & 5.35 / 4.80 & 45.0\% / 55.0\% & 70.0\% / 75.0\% \\
OOD (Stage 1 / Cons.) & Neuroscience \& Neuroimaging & 20 & $4.99$ / $4.88$ & 5.20 / 4.80 & 45.0\% / 50.0\% & 75.0\% / 80.0\% \\
OOD (Stage 1 / Cons.) & Structural Bioinfo \& AI Drug & 20 & $4.65$ / $4.56$ & 4.75 / 4.67 & 55.0\% / 60.0\% & 75.0\% / 80.0\% \\
\cmidrule{1-7}
OOD Total (Stage 1) & Single-Pass Evaluation & 60 & $4.99 \pm 1.92$ & 5.05 (3.78--6.02) & 48.3\% & 73.3\% \\
OOD Total (Consensus) & Stage-1+2 Consensus & 60 & $4.88 \pm 1.88$ & 4.80 (3.78--5.81) & 55.0\% & 78.3\% \\
\midrule
Paired Preprint--Pub & Selective Flagship/Society ($\Delta\text{Core}_8$) & 10 pairs & $5.70 \to 6.29$ (/8.0) & $\Delta = +0.59$ ($p=0.013$) & $9/10$ improved & $83.3\%$ ($15/18$) recall \\
Paired Preprint--Pub & Open-Access Megajournals ($\Delta\text{Core}_8$) & 10 pairs & $4.72 \to 4.94$ (/8.0) & $\Delta = +0.22$ ($p=0.12$) & $7/10$ improved & $+0.24$ pts Repro only \\
\midrule
Open-Review ($N=100$) & Selective Flagship / Society (135 Referees) & 50 & $7.49 \pm 1.38$ & 7.75 ($\text{Core}_8 = 5.87$) & 8.0\% & $97.7\%$ ($42/43$) unres.\ recall \\
Open-Review ($N=100$) & Open-Review Megajournals (126 Referees) & 50 & $5.01 \pm 1.69$ & 5.10 ($\text{Core}_8 = 3.79$) & 48.0\% & $98.1\%$ ($53/54$) unres.\ recall \\
Open-Review ($N=100$) & All Open-Review Combined (261 Referees) & 100 & $6.25 \pm 1.98$ & 6.60 ($\text{Core}_8 = 4.83$) & 28.0\% & $97.9\%$ ($95/97$) unres.\ / $78.2\%$ all \\
Open-Review ($N=100$) & Referee Depth \& Anomalies (Sel.\ vs.\ Mega) & 50 vs.\ 50 & $72\%$ vs.\ $12\%$ Thorough & $0\%$ vs.\ $38\%$ Superficial & $2\%$ vs.\ $58\%$ Anomalies & $385$ AI-only catches ($3.85$/paper) \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Thirty-five-year secular quality trajectory ($1991\text{--}2025$, $N = 915$ verified full-text articles across seven 5-year windows and four subfield tracks after excluding 85 archival missing-body-text stubs), within-journal fixed-effect and Oaxaca--Blinder decomposition summaries, and structural biomedical covariate partitions across the pooled wild corpus ($N = 1,076$).}
\label{tab:supp_secular}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{llccccc}
\toprule
Partition Dimension & Stratum / Window & $n$ & Composite (/10) & $\text{Core}_8$ (/8.0) & $< 5.0$ (\%) & $< 6.0$ (\%) \\
\midrule
5-Year Window ($N=915$) & 1991--1995 & 73 & $7.61 \pm 1.43$ & 6.21 (77.6\%) & 6.8\% & 13.7\% \\
5-Year Window ($N=915$) & 1996--2000 & 124 & $7.47 \pm 1.22$ & 6.12 (76.5\%) & 4.0\% & 10.5\% \\
5-Year Window ($N=915$) & 2001--2005 & 142 & $6.48 \pm 1.51$ & 5.23 (65.4\%) & 18.3\% & 31.7\% \\
5-Year Window ($N=915$) & 2006--2010 & 144 & $6.87 \pm 1.48$ & 5.52 (69.0\%) & 11.8\% & 25.7\% \\
5-Year Window ($N=915$) & 2011--2015 & 144 & $6.50 \pm 1.64$ & 5.21 (65.1\%) & 20.1\% & 34.7\% \\
5-Year Window ($N=915$) & 2016--2020 & 144 & $5.93 \pm 2.11$ & 4.69 (58.6\%) & 36.1\% & 47.9\% \\
5-Year Window ($N=915$) & 2021--2025 & 144 & $5.79 \pm 1.83$ & 4.54 (56.7\%) & 31.9\% & 52.1\% \\
\midrule
Subfield Track ($N=915$) & Molecular Evolution \& Phylogenetics & 233 & $6.96 \pm 1.55$ & 5.56 ($r=-0.30, p=3.1\times 10^{-6}$) & 14.2\% & 22.7\% \\
Subfield Track ($N=915$) & Gene Expression \& Genomics & 227 & $6.67 \pm 1.57$ & 5.37 ($r=-0.37, p=1.2\times 10^{-8}$) & 15.4\% & 30.0\% \\
Subfield Track ($N=915$) & Viral Evolution \& Virology & 226 & $6.34 \pm 1.98$ & 5.14 ($r=-0.36, p=2.1\times 10^{-8}$) & 24.8\% & 37.6\% \\
Subfield Track ($N=915$) & Population \& Statistical Genetics & 229 & $6.30 \pm 1.80$ & 5.04 ($r=-0.31, p=2.5\times 10^{-6}$) & 24.5\% & 40.6\% \\
\midrule
Decomposition ($N=915$) & Within-Journal Fixed Effect (30 Journals) & 549 & $-0.23\text{ pts/dec}$ & $-0.24\text{ pts/dec}$ ($p=0.0074$) & $r=-0.094$ & $p=0.027$ \\
Decomposition ($N=915$) & Oaxaca--Blinder (1990s vs.\ 2020s, $-1.82$ pts) & 427 & $54.1\%$ Compositional & $45.9\%$ Within-Stratum & $-0.98$ pts & $-0.84$ pts \\
\midrule
Venue Model ($N=1,076$) & Legacy / Society / Selective Journals & 654 & $6.75 \pm 1.79$ & $5.44 \pm 1.53$ & 17.3\% & 28.7\% \\
Venue Model ($N=1,076$) & Commercial Open-Access Megajournals & 422 & $5.80 \pm 1.73$ & $4.56 \pm 1.48$ & 33.9\% & 51.9\% \\
\midrule
Modality ($N=1,076$) & Wet-Lab Primary Expt. & 408 & $6.81 \pm 1.68$ & $5.51 \pm 1.45$ & 16.4\% & 28.9\% \\
Modality ($N=1,076$) & Hybrid Comp. + Wet-Lab & 351 & $6.56 \pm 1.73$ & $5.21 \pm 1.49$ & 19.9\% & 33.0\% \\
Modality ($N=1,076$) & Dry-Lab Theory / Sim. & 87 & $6.33 \pm 1.96$ & $5.05 \pm 1.68$ & 24.1\% & 34.5\% \\
Modality ($N=1,076$) & Dry-Lab Secondary DB & 230 & $5.33 \pm 1.78$ & $4.21 \pm 1.51$ & 42.6\% & 62.2\% \\
\midrule
Tech. Maturity ($N=1,076$) & Mid-Stage High-Throughput & 348 & $6.65 \pm 1.65$ & $5.29 \pm 1.42$ & 17.0\% & 31.0\% \\
Tech. Maturity ($N=1,076$) & Mature / Classical & 616 & $6.62 \pm 1.71$ & $5.34 \pm 1.47$ & 18.5\% & 32.1\% \\
Tech. Maturity ($N=1,076$) & Commodity Template & 112 & $4.16 \pm 1.42$ & $3.16 \pm 1.16$ & 74.1\% & 90.2\% \\
\midrule
Epistemic Stage ($N=1,076$) & Basic Discovery & 679 & $6.89 \pm 1.68$ & $5.53 \pm 1.46$ & 15.3\% & 26.7\% \\
Epistemic Stage ($N=1,076$) & Translational / Biomarker & 215 & $5.65 \pm 1.80$ & $4.47 \pm 1.54$ & 36.3\% & 54.0\% \\
Epistemic Stage ($N=1,076$) & Clinical / Observational & 182 & $5.33 \pm 1.62$ & $4.23 \pm 1.40$ & 40.7\% & 60.4\% \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Blinded career self-audit ($N = 164$ open-access papers by the senior author, 2004--2026) summary by authorship role and complete listing of all lead-author papers scoring $< 6.0$ ($n = 3$) and all middle co-author papers scoring $< 5.0$ ($n = 8$).}
\label{tab:supp_selfaudit}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{llllcp{7.5cm}}
\toprule
Role / Stratum & ID (PMCID) & Year & Venue & Score (/10) & Primary Blinded Audit Summary / Defect Identified \\
\midrule
First Author ($n=10$) & Summary & 2005--2023 & 8 Journals & $8.33 \pm 1.25$ & Median $8.65$ (IQR $8.43\text{--}9.15$), $0.0\% < 5.0$, $10.0\% < 6.0$ \\
Senior Author ($n=32$) & Summary & 2006--2025 & 18 Journals & $8.19 \pm 1.08$ & Median $8.50$ (IQR $7.80\text{--}8.93$), $0.0\% < 5.0$, $6.2\% < 6.0$ \\
All Lead/Senior ($n=42$) & Summary & 2005--2025 & 22 Journals & $8.22 \pm 1.11$ & Median $8.50$ (IQR $8.12\text{--}9.00$), $0.0\% < 5.0$, $7.1\% < 6.0$ \\
Middle Co-Author ($n=122$) & Summary & 2004--2026 & 49 Journals & $7.29 \pm 1.39$ & Median $7.70$ (IQR $6.50\text{--}8.30$), $6.6\% < 5.0$, $16.4\% < 6.0$ \\
All Career Papers ($N=164$) & Summary & 2004--2026 & 58 Journals & $7.53 \pm 1.38$ & Median $7.85$ (IQR $6.70\text{--}8.53$), $4.9\% < 5.0$, $14.0\% < 6.0$ \\
\midrule
Senior Author ($<6.0$) & `SP\_ANON\_044` (PMC11289888) & 2024 & *Front Bioinform* & 5.0 & Duplicate Table 2 rows (TN vs. Alberta), impossible node count ($1,364$ nodes for $N=295$), unit-scaling errors ($100\times$), and unvalidated heuristic constants (`[LAB_SOFTWARE]`). \\
First Author ($<6.0$) & `SP\_ANON\_028` (PMC1480537) & 2006 & *PLOS Comput Biol* & 5.2 & Base-rate fallacy used to justify unadjusted $p \le 0.05$ across 296 codons ($7$ sites found vs. $\sim 7.4$ expected under null); core `IFEL` method validated. \\
Senior Author ($<6.0$) & `SP\_ANON\_162` (PMC11228553) & 2024 & *Front Bioinform* & 5.4 & Gap-inflated 627-codon alignment for 340-aa Rem2 misclassifying 251 gap columns as invariant sites; disordered-tail confounding in `AlphaFold2` RMSD; mixed `hg19`/`hg38` table coordinates. \\
\midrule
Middle Author ($<5.0$) & `SP\_ANON\_103` (PMC9404229) & 2022 & *Environ Res* & 2.2 & Pre-pandemic 2019 Italian SARS-CoV-2 claim: $0/11$ RT-qPCR positive, $0/9$ $\text{PRNT}_{80}$ positive, single-amplicon nested-PCR carryover of derived 2020 `B.1` control. \\
Middle Author ($<5.0$) & `SP\_ANON\_034` (PMC4592012) & 2015 & *PLOS ONE* & 3.8 & Cross-sectional HIV DNA comparison in CSF vs. blood ($N=28$) with unadjusted multiple comparisons and over-extrapolated compartmental persistence claims. \\
Middle Author ($<5.0$) & `SP\_ANON\_135` (PMC8927931) & 2022 & *BMJ Glob Health* & 3.8 & Commentary/opinion essay defending early-origin SARS-CoV-2 PCR claims without primary experimental validation or contamination controls. \\
Middle Author ($<5.0$) & `SP\_ANON\_109` (PMC4865637) & 2016 & *Nature* & 4.1 & Ongoing HIV-1 replication under ART claimed from months 0--6 decay window ($N=3$), 70-cycle nested PCR without UMIs, and negative/conflicting rates in Extended Data Table 2. \\
Middle Author ($<5.0$) & `SP\_ANON\_003` (PMC8135569) & 2021 & *Mol Biol Evol* & 4.2 & Tumor `SCITE` algorithm applied to skewed pandemic surveillance, $>1\%$ filter erasing Wuhan basal diversity, and circular `COI` outgroup flipping (`proCoV2`). \\
Middle Author ($<5.0$) & `SP\_ANON\_021` (PMC8939770) & 2022 & *Sci Transl Med* & 4.5 & Target-predictor autocorrelation in forecasting 3-month SARS-CoV-2 spread from current spread, passenger hitchhiking inflation, and retrospective collection-date slicing. \\
Middle Author ($<5.0$) & `SP\_ANON\_092` (PMC11598840) & 2024 & *Viruses* & 4.6 & Descriptive VSIV outbreak phylogenomics with unvalidated causal adaptation claims and over-interpreted selection scans on small sample size. \\
Middle Author ($<5.0$) & `SP\_ANON\_026` (PMC5177524) & 2017 & *AIDS* & 4.8 & Observational partner-services cohort with severe missing-data attrition and unadjusted confounding between acute stage and network clustering. \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Research funding brackets (NIH RePORTER annual grant support across $n=222$ NIH-funded wild papers, total acknowledged grants, and estimated study production costs) and journal Open-Access Article Processing Charge tiers across the pooled wild corpus ($N = 1,076$, and $N = 1,176$ with calibration controls). Bottom rows summarize empirical AI review token and API costs ($N = 1,480$ manuscripts, $1,568$ reviews) extrapolated to PubMed Central and PubMed, human peer-review labor benchmarks, and Cohort~A failure grant portfolios.}
\label{tab:supp_economics}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{llccccc}
\toprule
Economic Dimension & Tier / Bracket & $n$ & Cost / Fee Metric & Mean $\pm$ SD (/10) & Median (/10) & $< 5.0$ (\%) \\
\midrule
NIH Grant Support ($N=1,076$) & Unfunded / Non-NIH & 854 & $\$0$ NIH & $6.12 \pm 1.83$ & 6.40 & 27.9\% \\
NIH Grant Support ($n=222$ NIH) & Small / Fellowship / R21 ($<\$250\text{k/yr}$) & 31 & Med $\$158,490\text{/yr}$ & $6.93 \pm 1.51$ & 7.40 & 16.1\% \\
NIH Grant Support ($n=222$ NIH) & 1 Standard R01 ($\$250\text{k--}\$600\text{k/yr}$) & 49 & Med $\$383,323\text{/yr}$ & $7.11 \pm 1.62$ & 7.70 & 10.2\% \\
NIH Grant Support ($n=222$ NIH) & All 1 Grant ($<\$600\text{k/yr}$ Combined) & 80 & Med $\$304,562\text{/yr}$ & $7.04 \pm 1.57$ & 7.60 & 12.5\% \\
NIH Grant Support ($n=222$ NIH) & 2--3 NIH Grants ($\$0.6\text{--}\$1.5\text{M/yr}$) & 76 & Med $\$949,006\text{/yr}$ & $7.63 \pm 1.45$ & 8.00 & 9.2\% \\
NIH Grant Support ($n=222$ NIH) & Mega-Center ($>\$1.5\text{M/yr}$) & 66 & Med $\$3,200,040\text{/yr}$ & $7.46 \pm 1.13$ & 7.80 & 1.5\% \\
\midrule
Total Grants Count ($N=1,076$) & 0 Acknowledged Grants & 615 & 0 Grants & $6.14 \pm 1.85$ & 6.40 & 27.5\% \\
Total Grants Count ($N=1,076$) & 1 Grant (Single PI) & 216 & 1 Grant & $6.49 \pm 1.72$ & 6.80 & 20.8\% \\
Total Grants Count ($N=1,076$) & 2--3 Grants (Collaborative) & 181 & 2--3 Grants & $6.71 \pm 1.82$ & 7.20 & 20.4\% \\
Total Grants Count ($N=1,076$) & 4--6 Grants (Multi-Lab) & 51 & 4--6 Grants & $7.35 \pm 1.47$ & 7.80 & 7.8\% \\
Total Grants Count ($N=1,076$) & 7+ Grants (Consortium) & 13 & $\ge 7$ Grants & $7.35 \pm 1.36$ & 8.00 & 7.7\% \\
\midrule
Est. Study Cost ($N=1,076$) & $<\$25\text{k}$ (Unfunded / No Grant) & 138 & Med $\$14,880$ & $5.24 \pm 1.85$ & 5.12 & 45.7\% \\
Est. Study Cost ($N=1,076$) & $\$25\text{k--}\$100\text{k}$ (Small / Single-Grant) & 162 & Med $\$72,224$ & $5.25 \pm 1.89$ & 5.10 & 46.3\% \\
Est. Study Cost ($N=1,076$) & $\$100\text{k--}\$350\text{k}$ (Standard R01-Scale) & 375 & Med $\$248,000$ & $6.69 \pm 1.64$ & 7.00 & 17.3\% \\
Est. Study Cost ($N=1,076$) & $\$350\text{k--}\$750\text{k}$ (Multi-Grant / HT) & 315 & Med $\$498,669$ & $6.82 \pm 1.60$ & 7.10 & 15.2\% \\
Est. Study Cost ($N=1,076$) & $>\$750\text{k}$ (Mega-Consortium) & 86 & Med $\$1,127,948$ & $7.32 \pm 1.40$ & 7.80 & 5.8\% \\
\midrule
Benchmark Modality ($N=50$) & Cohort B Dry-Lab Math/Software & 14 & Zero Wet-Lab Cost & $8.46 \pm 0.97$ & 8.75 & 0.0\% \\
Benchmark Modality ($N=50$) & Cohort B Wet-Lab Experimental & 36 & Multi-Assay Wet-Lab & $8.71 \pm 0.76$ & 8.90 & 0.0\% \\
\midrule
Journal APC Tier ($N=1,076$) & Diamond / Free OA ($\$0\text{--}\$1.2\text{k}$) & 28 & Mean APC $\$0$ & $4.99 \pm 2.11$ & 5.25 & 50.0\% \\
Journal APC Tier ($N=1,076$) & Commercial Megajournals ($\$1.7\text{k--}\$3.9\text{k}$) & 459 & Mean APC $\$2,879$ & $5.76 \pm 1.74$ & 5.80 & 35.1\% \\
Journal APC Tier ($N=1,076$) & Academic Society / Univ Press ($\$2.0\text{k--}\$4.2\text{k}$) & 361 & Mean APC $\$3,242$ & $6.48 \pm 1.80$ & 6.60 & 20.5\% \\
Journal APC Tier ($N=1,076$) & High-APC Selective ($\$4.5\text{k--}\$7.0\text{k}$) & 216 & Mean APC $\$5,579$ & $7.62 \pm 1.17$ & 8.00 & 3.2\% \\
Journal APC Tier ($N=1,076$) & Luxury Flagships ($\$9.5\text{k--}\$12.3\text{k}$) & 12 & Mean APC $\$11,528$ & $7.80 \pm 1.49$ & 8.30 & 0.0\% \\
Journal APC Tier ($N=1,176$ All) & Luxury Flagships (Wild + Calibration) & 51 & Mean APC $\$11,687$ & $7.82 \pm 1.75$ & 8.50 & 9.8\% \\
\midrule
AI vs.\ Human Review & Single-Pass AI Review ($22,119$ tokens) & 1,580 & $\$0.041$ Batch / $\$0.087$ On-Dem & $15,392$ in / $6,727$ out tok & $< 3\text{ min}$ & $97.9\%$ unres.\ recall \\
AI vs.\ Human Review & 3-Run Consensus AI Ensemble ($\text{ICC}=0.95$) & 1,580 & $\$0.124$ Batch / $\$0.260$ On-Dem & $66,357$ total tokens & $\sim 3\text{ min}$ & $+3.85$ AI-only flaws \\
AI vs.\ Human Review & Human Peer Review ($2.61$ refs $\times 5\text{h} + 2\text{h}$ ed.) & 100 & $\$1,505\text{/paper}$ ($\$100\text{/hr}$) & $15.05\text{ hrs/paper}$ & $3,213$ words & $17.4\text{k--}36.4\text{k}\times$ AI cost \\
\midrule
PubMed Extrapolation & 2025 Annual PMC Open-Access Flow & 921,565 & $\$38,109$ Batch / $\$79,727$ OD & $20.38\text{B}$ tokens/yr & $\$114\text{k}$ 3-Run & $46.9\%$ of PubMed \\
PubMed Extrapolation & 2025 Entire Annual PubMed Flow & 1,965,335 & $\$81,272$ Batch / $\$170,025$ OD & $43.47\text{B}$ tokens/yr & $\$244\text{k}$ 3-Run & vs.\ $\$2.96\text{B}$ human labor \\
PubMed Extrapolation & All-Time PMC Full-Text Stock & 10,900,000 & $\$450,743$ Batch / $\$942,982$ OD & $241.1\text{B}$ tokens & $\$1.35\text{M}$ 3-Run & $100\%$ PMC archive \\
PubMed Extrapolation & All-Time PubMed Stock (1781--2025) & 39,400,000 & $\$1.63\text{M}$ Batch / $\$3.41\text{M}$ OD & $871.5\text{B}$ tokens & $\$4.89\text{M}$ 3-Run & $\approx 1$ NIH R01 grant \\
\midrule
Failure Waste Costs & Cohort A NIH-Funded Failures ($73$ grants) & 18 / 50 & $\$67.68\text{M/yr}$ NIH portfolio & Mean $\$3.76\text{M/yr}$ & Med $\$2.07\text{M/yr}$ & Score $5.3/10$ ($86\% <6.0$) \\
Failure Waste Costs & Tumor/Placental Microbiome (`A16--18, A27`) & 4 & $\$31.85\text{M/yr}$ NIH + $\$17.5\text{M}$ VC & *Micronoma* spinout & $>4,000$ cites & Reagent/human DNA contam. \\
Failure Waste Costs & Wild Failing Papers ($<5.0$) APC \& Grants & 256 & $\$42.4\text{M/yr}$ NIH / $\$830\text{k}$ APC & $\sim\$0.9\text{--}\$1.2\text{B/yr}$ OA APCs & $\$28.2\text{B/yr}$ US & Irreproducible waste \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[ht!]
\centering
\caption{Blinded evaluation of `gemini-4-argon` (`Gemini 3.1 Pro`) against the 12 models evaluated by Brian et al.\ (2026) across the first three expanded 2026 *Nature Medicine* clinical trials (`T01`--`T03`; 3 error-seeded and 3 control reviews per model) and across all 58 trials in Brian et al.\ (2026). Net Youden's $J = \text{Sens}_{\text{Maj}} + \text{Spec}_{\text{Ctrl}} - 1$. Models marked with $^\dagger$ in Brian et al.\ (`Opus 5.5`, `Fable 5`, `Opus 5`) were evaluated on only $n = 3$ initial trials (`N`, `I`, `M`) and omitted from `T01--T60`.}
\label{tab:supp_rust_replication}
\small
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
Model & `T01--T03` Major Sens.\ (\%) & `T01--T03` Control FPR (\%) & `T01--T03` Specificity (\%) & `T01--T03` Youden's $J$ & 58-Trial Total Sens.\ / Spec.\ (\%) & Calibrated Rigor Score (Clean vs.\ Seeded) \\
\midrule
**`gemini-4-argon** (Ours)` & **84.0\%** ($7.56/9$) & **2.4\%** ($0.33/14$) & **97.6\%** & **+0.816** & --- & $\mathbf{6.93 \pm 0.61}$ **(PASS) vs.\ $\mathbf{3.00 \pm 0.50**$ (FAILED)} \\
`GPT-6.1 Sol` & 92.6\% ($8.33/9$) & 13.7\% ($1.92/14$) & 86.3\% & +0.789 & 90.2\% / 74.8\% & --- \\
`Sonnet 5` & 84.3\% ($7.58/9$) & 10.1\% ($1.42/14$) & 89.9\% & +0.742 & 81.2\% / 82.9\% & --- \\
`GPT-5.4` & 81.5\% ($7.33/9$) & 7.7\% ($1.08/14$) & 92.3\% & +0.738 & 70.9\% / 88.2\% & --- \\
`GPT-6 Luna` & 85.2\% ($7.67/9$) & 14.9\% ($2.08/14$) & 85.1\% & +0.703 & 86.3\% / 79.4\% & --- \\
`GPT-5.5` & 81.5\% ($7.33/9$) & 13.1\% ($1.83/14$) & 86.9\% & +0.684 & 73.1\% / 86.2\% & --- \\
`Kimi K3` & 81.5\% ($7.33/9$) & 16.1\% ($2.25/14$) & 83.9\% & +0.654 & 76.2\% / 77.7\% & --- \\
`GPT-5.4 mini` & 70.4\% ($6.33/9$) & 5.4\% ($0.75/14$) & 94.6\% & +0.650 & 59.0\% / 90.8\% & --- \\
`DeepSeek V4 Pro` & 75.9\% ($6.83/9$) & 11.9\% ($1.67/14$) & 88.1\% & +0.640 & 68.1\% / 86.4\% & --- \\
`Gemini 3.8 Flash` & 77.8\% ($7.00/9$) & 16.1\% ($2.25/14$) & 83.9\% & +0.617 & 66.2\% / 84.0\% & --- \\
`Qwen 3.8 27B` & 74.1\% ($6.67/9$) & 15.5\% ($2.17/14$) & 84.5\% & +0.586 & 62.6\% / 81.8\% & --- \\
`gpt-oss-120b` & 59.3\% ($5.33/9$) & 3.6\% ($0.50/14$) & 96.4\% & +0.557 & 56.8\% / 92.8\% & --- \\
`Haiku 4.5` & 55.6\% ($5.00/9$) & 10.1\% ($1.42/14$) & 89.9\% & +0.455 & 45.8\% / 89.1\% & --- \\
\midrule
`Opus 5.5`$^\dagger$ ($n=3$ trials only) & --- & --- & --- & --- & 92.9\% / 71.4\% & --- \\
`Fable 5`$^\dagger$ ($n=3$ trials only) & --- & --- & --- & --- & 92.5\% / 74.6\% & --- \\
`Opus 5`$^\dagger$ ($n=3$ trials only) & --- & --- & --- & --- & 89.7\% / 79.4\% & --- \\
\bottomrule
\end{tabular}%
}
\end{table}
