#!/usr/bin/env python3
"""OD-16 driver — executable comparison of Spec 097 freeze v2 vs freeze v3
for the Stage 4.2 affiliation vocabulary tests (R1 NES attested, R2
Afroasiatic). Commissioned by the owner 2026-11-22 (adjudication item
OD-16 / unit M-12).

Method: the frozen Stage 4 pipeline (pipeline-v2.py, campaign scratch on
tower-compute, SHA-256 reported in the output) is imported as a module and
its own gloss_score / perm_p / asjp_forms / skeleton / match functions are
executed on both registered vocabulary companions. The permutation-null
histogram comes from an exact replica of the frozen perm_p loop (same
seed, same RNG consumption order); the replica's p is asserted equal to
the frozen perm_p's p on every run before its histogram is reported.

Outputs: aggregate statistics only (F-6 custody posture). No Otten-derived
text is read or written: the vocabulary tests run on the registered
vocabulary companions (CC BY / CC BY-SA apparatus) and the ASJP CLDF lists
(CC BY 4.0) only.
"""
import sys, json, hashlib, collections, random, importlib.util

SCRATCH = "/home/tpierson/glossa-work/meroitic-scratch/campaign"
CLONE = "/home/tpierson/glossa-work/od16-2026-11-22"
REC = f"{CLONE}/specs/097-meroitic-reproduction-benchmark/records"
DATA = "/home/tpierson/glossa-work/s097-data"

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---- import the frozen pipeline without triggering its mode dispatch ----
sys.argv = ["pipeline-v2.py", "od16-import-only"]
spec = importlib.util.spec_from_file_location("pipeline_v2", f"{SCRATCH}/pipeline-v2.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

out = {"driver": "od16_freeze_compare.py",
       "purpose": "OD-16 executable freeze v2 vs v3 comparison, Spec 097 Stage 4.2 vocabulary tests"}

# ---- input identity / pins ----
out["input_hashes"] = {
    "pipeline-v2.py (frozen code, campaign scratch)": sha256(f"{SCRATCH}/pipeline-v2.py"),
    "freeze-v2-vocabulary-2026-11-20.json": sha256(f"{REC}/freeze-v2-vocabulary-2026-11-20.json"),
    "freeze-v3-vocabulary-2026-11-22.json": sha256(f"{REC}/freeze-v3-vocabulary-2026-11-22.json"),
    "stage-4-2-results.json (executed, repo)": sha256(f"{REC}/stage-4-2-results.json"),
    "stage42-results.json (executed, scratch)": sha256(f"{SCRATCH}/stage4-v2/stage42-results.json"),
    "ASJP forms.csv": sha256(f"{DATA}/forms.csv"),
    "ASJP languages.csv": sha256(f"{DATA}/languages.csv"),
    "ASJP parameters.csv": sha256(f"{DATA}/parameters.csv"),
}
out["asjp_pins_match_freeze_v2_s4"] = (
    out["input_hashes"]["ASJP forms.csv"] == "4ee30b771a2cba59e7e904587f7f60dc3d823824a7b9aae9dd6f73a960139321"
    and out["input_hashes"]["ASJP languages.csv"] == "647174df2eb812eff370355b02b6843d76bfb2b082147bc263e5ccd4cc628be5"
    and out["input_hashes"]["ASJP parameters.csv"] == "2ed306c24552ea61e48ad6dc067859d8b70029abfc1d36668246214a5a1183ec")

v2 = json.load(open(f"{REC}/freeze-v2-vocabulary-2026-11-20.json"))
v3 = json.load(open(f"{REC}/freeze-v3-vocabulary-2026-11-22.json"))
executed = json.load(open(f"{REC}/stage-4-2-results.json"))
scratch_vocab = json.load(open(f"{SCRATCH}/stage4-v2/vocab.json"))
out["executed_scratch_vocab_json_equals_repo_v2_companion"] = (scratch_vocab == v2)
out["repo_results_json_equals_scratch_executed_results"] = (
    executed == json.load(open(f"{SCRATCH}/stage4-v2/stage42-results.json")))

# ---- structural diff of the two companions ----
def key(e):
    return (e["form"], e["gloss"], e["origin"])
k2 = {key(e): e for e in v2}
k3 = {key(e): e for e in v3}
assert len(k2) == len(v2) and len(k3) == len(v3), "duplicate (form,gloss,origin) keys"
only2 = sorted(set(k2) - set(k3))
only3 = sorted(set(k3) - set(k2))
field_diffs = collections.Counter()
non_source_diffs = []
for k in sorted(set(k2) & set(k3)):
    a, b = k2[k], k3[k]
    for f in ("form", "norm", "gloss", "confidence", "category", "concept", "origin", "sources"):
        if a.get(f) != b.get(f):
            field_diffs[f] += 1
            if f != "sources":
                non_source_diffs.append({"key": k, "field": f, "v2": a.get(f), "v3": b.get(f)})
out["structural_diff"] = {
    "entries_v2": len(v2), "entries_v3": len(v3),
    "entries_only_in_v2": [{"form": k[0], "gloss": k[1], "origin": k[2],
                            "concept": k2[k].get("concept"), "confidence": k2[k].get("confidence")} for k in only2],
    "entries_only_in_v3": [{"form": k[0], "gloss": k[1], "origin": k[2],
                            "concept": k3[k].get("concept"), "confidence": k3[k].get("confidence")} for k in only3],
    "common_entries": len(set(k2) & set(k3)),
    "field_diff_counts_among_common": dict(field_diffs),
    "non_sources_field_diffs": non_source_diffs,
    "wikipedia_citations_in_sources_v2": sum(1 for e in v2 for s in e["sources"] if "wikipedia" in json.dumps(s).lower()),
    "wikipedia_citations_in_sources_v3": sum(1 for e in v3 for s in e["sources"] if "wikipedia" in json.dumps(s).lower()),
}

# ---- scoring-input projection (everything gloss_score can see) ----
def projection(vocab):
    rows = [(e["norm"], P.skeleton(e["norm"]), e["concept"]) for e in vocab if e.get("concept")]
    return collections.Counter(rows), sorted(rows)
proj2, rows2 = projection(v2)
proj3, rows3 = projection(v3)
out["scoring_input_projection"] = {
    "concept_bearing_forms_v2": sum(proj2.values()),
    "concept_bearing_forms_v3": sum(proj3.values()),
    "projections_identical_as_multisets": proj2 == proj3,
    "forms_per_concept_v2": dict(sorted(collections.Counter(c for _, _, c in rows2).items())),
    "forms_per_concept_v3": dict(sorted(collections.Counter(c for _, _, c in rows3).items())),
    "rows": [{"norm": n, "skeleton": s, "concept": c} for n, s, c in rows2],
}

# ---- comparator inputs (identical for both freezes by construction) ----
nes = P.asjp_forms(P.NES_LANGS)
aa = P.asjp_forms(P.AA_LANGS)
scored = sorted({c for _, _, c in rows2})
out["comparator_inputs"] = {
    "R1_NES_languages": P.NES_LANGS, "R2_AA_languages": P.AA_LANGS,
    "R1_pool_forms_total": sum(len(x) for x in nes.values()),
    "R2_pool_forms_total": sum(len(x) for x in aa.values()),
    "R1_forms_per_scored_concept": {str(c): len(nes.get(c, [])) for c in scored},
    "R2_forms_per_scored_concept": {str(c): len(aa.get(c, [])) for c in scored},
}

# ---- matching-pair detail (form level) ----
def matching_pairs(vocab, comp_forms):
    by_concept = collections.defaultdict(list)
    for e in vocab:
        if e.get("concept"):
            by_concept[e["concept"]].append(e)
    detail = {}
    for c in scored:
        pairs = []
        for e in by_concept.get(c, []):
            for lang, f in comp_forms.get(c, []):
                if P.match(P.skeleton(e["norm"]), P.asjp_skel(f)):
                    pairs.append({"meroitic_form": e["form"], "meroitic_norm": e["norm"],
                                  "comparator_language": lang, "comparator_form": f})
        detail[str(c)] = sorted(pairs, key=lambda d: (d["meroitic_form"], d["comparator_language"], d["comparator_form"]))
    return detail

# ---- exact replica of frozen perm_p, additionally recording the null ----
def perm_null(vocab, comp_forms, S_obs, nperm=10000, seed=20261120):
    rng = random.Random(seed)
    allforms = [f for fs in comp_forms.values() for f in fs]
    hist = collections.Counter()
    ge = 0
    for _ in range(nperm):
        shuffled = {}
        pool = list(allforms)
        rng.shuffle(pool)
        idx = 0
        for c in sorted(comp_forms):
            k = len(comp_forms[c])
            shuffled[c] = pool[idx:idx + k]
            idx += k
        s, _, _ = P.gloss_score(vocab, shuffled)
        hist[s] += 1
        ge += s >= S_obs
    return (1 + ge) / (1 + nperm), ge, dict(sorted(hist.items()))

def run(vocab, comp_forms):
    S, per, _ = P.gloss_score(vocab, comp_forms)
    p_frozen = P.perm_p(vocab, comp_forms, S)
    p_replica, ge, hist = perm_null(vocab, comp_forms, S)
    assert p_frozen == p_replica, (p_frozen, p_replica)
    mean = sum(s * n for s, n in hist.items()) / sum(hist.values())
    var = sum(n * (s - mean) ** 2 for s, n in hist.items()) / sum(hist.values())
    return {"S": S, "per_concept": {str(k): v for k, v in per.items()},
            "p_frozen_perm_p": p_frozen, "p_replica": p_replica, "ge_count": ge,
            "null_histogram_S_perm": {str(k): v for k, v in hist.items()},
            "null_mean": mean, "null_sd": var ** 0.5,
            "pass_bar_p<0.01_and_S>=5": bool(p_frozen < 0.01 and S >= 5)}

runs = {}
for flabel, vocab in (("v2", v2), ("v3", v3)):
    runs[flabel] = {"R1_attested": run(vocab, nes), "R2_afroasiatic": run(vocab, aa)}
    runs[flabel]["R1_matching_pairs"] = matching_pairs(vocab, nes)
    runs[flabel]["R2_matching_pairs"] = matching_pairs(vocab, aa)
out["runs"] = runs

# ---- validation against the executed Stage 4.2 outputs ----
def check(runres, executed_block):
    return {"S_equal": runres["S"] == executed_block["S"],
            "p_equal_exact_float": runres["p_frozen_perm_p"] == executed_block["p"],
            "per_concept_equal": runres["per_concept"] == executed_block["per_concept"],
            "pass_equal": runres["pass_bar_p<0.01_and_S>=5"] == executed_block["pass"]}
out["validation_vs_executed_stage42"] = {
    "v2_R1": check(runs["v2"]["R1_attested"], executed["vocab_R1_attested"]),
    "v2_R2": check(runs["v2"]["R2_afroasiatic"], executed["vocab_R2_afroasiatic"]),
    "v3_R1": check(runs["v3"]["R1_attested"], executed["vocab_R1_attested"]),
    "v3_R2": check(runs["v3"]["R2_afroasiatic"], executed["vocab_R2_afroasiatic"]),
}
out["v2_v3_runs_identical"] = all(
    runs["v2"][t][f] == runs["v3"][t][f]
    for t in ("R1_attested", "R2_afroasiatic")
    for f in ("S", "per_concept", "p_frozen_perm_p", "ge_count", "null_histogram_S_perm", "null_mean", "null_sd"))
out["v2_v3_matching_pairs_identical"] = (
    runs["v2"]["R1_matching_pairs"] == runs["v3"]["R1_matching_pairs"]
    and runs["v2"]["R2_matching_pairs"] == runs["v3"]["R2_matching_pairs"])

dest = f"{REC}/od16-freeze-v2-v3-comparison-results-2026-11-22.json"
json.dump(out, open(dest, "w"), indent=1, ensure_ascii=False)
print("WROTE", dest)
print("pins ok:", out["asjp_pins_match_freeze_v2_s4"],
      "| scratch vocab == repo v2:", out["executed_scratch_vocab_json_equals_repo_v2_companion"],
      "| repo results == scratch results:", out["repo_results_json_equals_scratch_executed_results"])
print("structural:", out["structural_diff"]["entries_v2"], "->", out["structural_diff"]["entries_v3"],
      "| field diffs:", out["structural_diff"]["field_diff_counts_among_common"],
      "| non-source diffs:", len(out["structural_diff"]["non_sources_field_diffs"]))
print("projections identical:", out["scoring_input_projection"]["projections_identical_as_multisets"])
for fl in ("v2", "v3"):
    for t in ("R1_attested", "R2_afroasiatic"):
        r = runs[fl][t]
        print(fl, t, "S =", r["S"], "p =", r["p_frozen_perm_p"], "ge =", r["ge_count"],
              "null mean/sd =", round(r["null_mean"], 4), round(r["null_sd"], 4))
print("validation:", json.dumps(out["validation_vs_executed_stage42"]))
print("v2/v3 runs identical:", out["v2_v3_runs_identical"],
      "| matching pairs identical:", out["v2_v3_matching_pairs_identical"])
