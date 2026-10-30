from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parent.parent
import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from expand_peer_review_to_50 import parse_xml_manuscript, scrub_doc

root = Path(str(REPO_ROOT))
exp_dir = root / "field_expansion_160"
(exp_dir / "raw_papers").mkdir(parents=True, exist_ok=True)
(exp_dir / "scrubbed_papers").mkdir(parents=True, exist_ok=True)
(exp_dir / "reviews").mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    used_pmids = set()
    used_pmcids = set()

    for jpath in [
        root / "cohorts_200.json",
        root / "ood_exp/manifest.json",
        root / "open_review_exp/manifest_open_review_100.json",
        root / "peer_review_exp/manifest.json",
        root / "secular_trend_exp/manifest_1000.json",
        root / "spond_self_audit/manifest.json",
    ]:
        if not jpath.exists():
            continue
        data = json.loads(jpath.read_text())
        items = data if isinstance(data, list) else [x for v in data.values() if isinstance(v, list) for x in v]
        for it in items:
            if isinstance(it, dict):
                if it.get("pmid"):
                    used_pmids.add(str(it["pmid"]))
                if it.get("pmcid"):
                    used_pmcids.add(str(it["pmcid"]))

    print(f"Loaded exclusion sets: {len(used_pmids)} PMIDs, {len(used_pmcids)} PMCIDs")

    FIELD_SPECS = [
        (
            "Viral Evolution",
            20,
            '(TITLE:"phylodynamic" OR TITLE:"molecular clock" OR TITLE:"viral evolution" OR TITLE:"spillover" OR TITLE:"genomic epidemiology" OR TITLE:"phylogeograph") AND (TITLE:"virus" OR TITLE:"SARS-CoV-2" OR TITLE:"influenza" OR TITLE:"dengue" OR TITLE:"rabies" OR TITLE:"mpox" OR TITLE:"HIV")',
            "Core",
        ),
        (
            "Molecular Evolution",
            20,
            '(TITLE:"positive selection" OR TITLE:"dN/dS" OR TITLE:"codon" OR TITLE:"purifying selection" OR TITLE:"adaptive evolution" OR TITLE:"molecular evolution") AND (TITLE:"evolution" OR TITLE:"phylogen" OR TITLE:"genome" OR TITLE:"mammalian" OR TITLE:"gene family")',
            "Core",
        ),
        (
            "Cancer & Microbiome",
            16,
            '(TITLE:"microbiome" OR TITLE:"metagenom" OR TITLE:"16S" OR TITLE:"microbiota" OR TITLE:"mycobiome") AND (TITLE:"cancer" OR TITLE:"tumor" OR TITLE:"colorectal" OR TITLE:"carcinoma" OR TITLE:"oncolog" OR TITLE:"melanoma" OR TITLE:"gastric" OR TITLE:"pancreatic")',
            "Core (Cancer Microbiome)",
        ),
        (
            "Cancer & Microbiome",
            4,
            '(TITLE:"microbiome" OR TITLE:"metagenom" OR TITLE:"16S" OR TITLE:"microbiota") AND (TITLE:"gut" OR TITLE:"intestinal" OR TITLE:"fecal" OR TITLE:"dysbiosis") NOT (TITLE:"cancer" OR TITLE:"tumor" OR TITLE:"carcinoma")',
            "Core (Host Microbiome)",
        ),
        (
            "Statistical Genetics",
            20,
            '(TITLE:"genome-wide association" OR TITLE:"polygenic" OR TITLE:"GWAS" OR TITLE:"heritability" OR TITLE:"Mendelian randomization") AND (TITLE:"stratification" OR TITLE:"selection" OR TITLE:"risk score" OR TITLE:"trait" OR TITLE:"architecture" OR TITLE:"causal" OR TITLE:"biobank")',
            "Core",
        ),
        (
            "Transcriptomics & CompBio",
            20,
            '(TITLE:"single-cell" OR TITLE:"scRNA-seq" OR TITLE:"RNA-seq" OR TITLE:"transcriptom") AND (TITLE:"signature" OR TITLE:"prognostic" OR TITLE:"microenvironment" OR TITLE:"atlas" OR TITLE:"clustering" OR TITLE:"machine learning" OR TITLE:"deconvolution")',
            "Core",
        ),
        (
            "Ecology & Macroevolution",
            20,
            '(TITLE:"species distribution" OR TITLE:"MaxEnt" OR TITLE:"habitat suitability" OR TITLE:"macroevolution" OR TITLE:"diversification rate" OR TITLE:"niche modeling" OR TITLE:"biodiversity") AND (TITLE:"climate change" OR TITLE:"phylogen" OR TITLE:"conservation" OR TITLE:"ecological" OR TITLE:"ensemble")',
            "OOD",
        ),
        (
            "Neuroscience & Neuroimaging",
            20,
            '(TITLE:"fMRI" OR TITLE:"resting-state" OR TITLE:"functional connectivity" OR TITLE:"EEG" OR TITLE:"DTI" OR TITLE:"neuroimaging" OR TITLE:"brain network") AND (TITLE:"cognitive" OR TITLE:"cortex" OR TITLE:"dynamics" OR TITLE:"patients" OR TITLE:"disorder" OR TITLE:"connectivity")',
            "OOD",
        ),
        (
            "Structural Bioinfo & AI Drug Discovery",
            20,
            '(TITLE:"molecular docking" OR TITLE:"virtual screening" OR TITLE:"molecular dynamics" OR TITLE:"drug-target interaction" OR TITLE:"pharmacophore" OR TITLE:"deep learning") AND (TITLE:"inhibitor" OR TITLE:"discovery" OR TITLE:"kinase" OR TITLE:"binding" OR TITLE:"QSAR" OR TITLE:"ADMET")',
            "OOD",
        ),
    ]

    rng = random.Random(20261029)

    def try_fetch_hybrid(r):
        pmcid = r.get("pmcid")
        if not pmcid:
            return None
        meta = {
            "cohort_id": "TEMP",
            "pmcid": pmcid,
            "pmid": str(r.get("pmid", "")),
            "doi": r.get("doi", ""),
            "title": r.get("title", ""),
            "authors": r.get("authorString", ""),
            "journal": r.get("journalTitle", ""),
            "year": int(r.get("pubYear", 0)),
            "citedByCount": int(r.get("citedByCount", 0)),
        }
        try:
            u = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            xml_bytes = urllib.request.urlopen(u, timeout=12).read()
            md = parse_xml_manuscript(xml_bytes, meta, pmcid)
            if len(md) < 13000:
                return None
            return (meta, md)
        except Exception:
            return None

    selected_records = []
    idx_counter = 1

    for domain, target_k, q_base, sub_note in FIELD_SPECS:
        q = f'{q_base} AND IN_EPMC:Y AND OPEN_ACCESS:Y AND PUB_YEAR:[2020 TO 2025] AND PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review" NOT PUB_TYPE:"Retracted Publication" NOT PUB_TYPE:"Preprint"'
        pool = []
        cursor = "*"
        for _ in range(3):
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&pageSize=150&cursorMark={urllib.parse.quote(cursor)}"
            try:
                data = json.loads(urllib.request.urlopen(url, timeout=15).read().decode())
                res = data.get("resultList", {}).get("result", [])
                next_cursor = data.get("nextCursorMark")
                if not res:
                    break
                for r in res:
                    pmcid = r.get("pmcid")
                    pmid = str(r.get("pmid", ""))
                    if (
                        pmcid
                        and pmid
                        and pmcid not in used_pmcids
                        and pmid not in used_pmids
                        and not any(w in r.get("title", "") for w in ["Correction", "Erratum", "Retraction", "Withdrawn"])
                    ):
                        pool.append(r)
                        used_pmcids.add(pmcid)
                        used_pmids.add(pmid)
                if not next_cursor or next_cursor == cursor:
                    break
                cursor = next_cursor
            except Exception:
                break

        rng.shuffle(pool)
        valid_for_spec = []
        for cand in pool:
            if len(valid_for_spec) >= target_k:
                break
            fetched = try_fetch_hybrid(cand)
            if fetched is None:
                continue
            meta, md = fetched
            anon_id = f"FEXP_ANON_{idx_counter:03d}"
            cid = f"FEXP_{idx_counter:03d}"
            meta["cohort_id"] = cid
            meta["anon_id"] = anon_id
            meta["domain"] = domain
            meta["sub_note"] = sub_note
            meta["cohort"] = "C_EXP" if "Core" in sub_note else "OOD_EXP"
            cites = meta["citedByCount"]
            meta["citation_tier"] = "High (>=25)" if cites >= 25 else ("Mid (5-24)" if cites >= 5 else "Low (0-4)")
            scrubbed = scrub_doc(md, meta, anon_id)
            if len(scrubbed) < 11000:
                continue
            meta["raw_bytes"] = len(md)
            meta["scrubbed_bytes"] = len(scrubbed)
            (exp_dir / "raw_papers" / f"{cid}_{meta['pmcid']}.md").write_text(md, encoding="utf-8")
            (exp_dir / "scrubbed_papers" / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
            valid_for_spec.append(meta)
            selected_records.append(meta)
            idx_counter += 1

        print(f"  {domain} ({sub_note}): fetched {len(valid_for_spec)}/{target_k}", flush=True)
        assert len(valid_for_spec) == target_k, f"Expected {target_k} for {domain} ({sub_note}), got {len(valid_for_spec)}"

    with open(exp_dir / "manifest_160.json", "w") as f:
        json.dump(selected_records, f, indent=2)

    print(f"Successfully harvested and scrubbed {len(selected_records)} new 2020-2025 Everyday Papers across all 8 fields!")
