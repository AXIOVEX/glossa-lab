#!/usr/bin/env python3
"""OD-20 driver — reassessment of soreyi (Spec 097 Stage 4.4's one
PARTIALLY SUPPORTED candidate) against anchor-only and genre/formula
baselines. Commissioned by the owner 2026-11-22 (adjudication item
OD-20 / unit M-17).

Method: the frozen Stage 4 pipeline (pipeline-v2.py, campaign scratch
on tower-compute, SHA-256 reported in the output) is imported as a
module. Step 1 reproduces Stage 4.3 and Stage 4.4 exactly through the
pipeline's own stage43()/stage44() functions (OUT redirected to a
scratch dir) and asserts equality with the filed records before any
baseline is computed. Steps 2-3 compute the two baselines with the
pipeline's own partition()/tokens_of()/build_vocab() so tokenization,
the hash split, and the vocabulary are the frozen ones.

Outputs: aggregate statistics only (F-6 custody posture). The corpus
computed on is the acquired Kovetsky inscription corpus (CC BY 4.0
data) — the same basis freeze v2 registers for Stages 4.2-4.4. No
Otten-derived text is read or written.
"""
import sys, json, hashlib, collections, importlib.util, os

SCRATCH = "/home/tpierson/glossa-work/meroitic-scratch/campaign"
CLONE = "/home/tpierson/glossa-work/od20-2026-11-22"
REC = f"{CLONE}/specs/097-meroitic-reproduction-benchmark/records"
TMPOUT = f"{CLONE}/.od20-tmp"
os.makedirs(TMPOUT, exist_ok=True)

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---- import the frozen pipeline without triggering its mode dispatch ----
sys.argv = ["pipeline-v2.py", "od20-import-only"]
spec = importlib.util.spec_from_file_location("pipeline_v2", f"{SCRATCH}/pipeline-v2.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
P.OUT = TMPOUT  # redirect stage43/stage44 outputs away from the executed scratch

out = {"driver": "od20_soreyi_baselines.py",
       "purpose": "OD-20 soreyi baseline reassessment, Spec 097 Stage 4.4"}
out["input_hashes"] = {
    "pipeline-v2.py (frozen code, campaign scratch)": sha256(f"{SCRATCH}/pipeline-v2.py"),
    "inscriptions.jsonl (Kovetsky acquired corpus)": sha256("/home/tpierson/glossa-work/meroitic-kovetsky-src/data/inscriptions.jsonl"),
    "stage-4-3-candidates.json (filed, repo)": sha256(f"{REC}/stage-4-3-candidates.json"),
    "stage-4-4-results.json (filed, repo)": sha256(f"{REC}/stage-4-4-results.json"),
}

# ================= Step 1: exact reproduction =================
P.stage43()
regen43 = json.load(open(f"{TMPOUT}/stage43-candidates.json"))
filed43 = json.load(open(f"{REC}/stage-4-3-candidates.json"))
out["reproduction_stage43_exact"] = (regen43 == filed43)

P.stage44()
regen44 = json.load(open(f"{TMPOUT}/stage44-results.json"))
filed44 = json.load(open(f"{REC}/stage-4-4-results.json"))
scratch44 = json.load(open(f"{SCRATCH}/stage4-v2/stage44-results.json"))
out["reproduction_stage44_candidates_exact"] = (regen44["candidates"] == filed44["candidates"])
out["reproduction_stage44_controls_exact"] = (regen44["anchor_controls_heldout"] == scratch44["anchor_controls_heldout"])
out["reproduction_stage44_held_by_stratum"] = regen44["heldout_texts_by_stratum"]
soreyi_filed = [c for c in filed44["candidates"] if c["form"] == "soreyi"][0]
out["soreyi_filed_stage44"] = soreyi_filed

# ================= shared basis =================
dev, held = P.partition()
vocab = P.build_vocab()
known = {v["norm"] for v in vocab}
THEO = {"wos", "sorey", "amni", "wosi"}

def profile(form, texts):
    """Per-stratum occurrences / texts-with for one form, frozen tokenization."""
    per = {}
    for d in texts:
        toks = P.tokens_of(d["text"])
        n = toks.count(form)
        e = per.setdefault(d["stratum"], {"occurrences": 0, "texts_with": 0, "texts": 0})
        e["occurrences"] += n; e["texts_with"] += (n > 0); e["texts"] += 1
    tot_occ = sum(v["occurrences"] for v in per.values())
    fun_occ = per.get("funerary", {}).get("occurrences", 0)
    return {"per_stratum": per, "total_occurrences": tot_occ,
            "total_texts_with": sum(v["texts_with"] for v in per.values()),
            "funerary_share_of_occurrences": (fun_occ / tot_occ) if tot_occ else None}

def context_stats(form, texts):
    """Position profile and adjacency rates for one form over a text set."""
    occ = 0; pos = collections.Counter(); adj = collections.Counter(); neigh = collections.Counter()
    texts_with = 0
    for d in texts:
        toks = P.tokens_of(d["text"])
        hit = False
        for i, t in enumerate(toks):
            if t != form: continue
            hit = True; occ += 1
            pos["initial" if i == 0 else "final" if i == len(toks) - 1 else "medial"] += 1
            for j in (i - 1, i + 1):
                if 0 <= j < len(toks):
                    nb = toks[j]; neigh[nb] += 1
                    if nb in ("wos", "wosi"): adj["wos_family"] += 1
                    if nb == "sorey": adj["sorey"] += 1
                    if nb == "soreyi": adj["soreyi"] += 1
                    if nb == "amni": adj["amni"] += 1
                    if nb in THEO: adj["theonym_set"] += 1
                    if nb.startswith("ted") or nb.startswith("terike"): adj["filiation"] += 1
                    if any(ch.isdigit() for ch in nb): adj["numeral"] += 1
        texts_with += hit
    if not occ: return {"occurrences": 0, "texts_with": texts_with}
    slots = 2 * occ  # two neighbour slots per occurrence (edges have one; rate vs slots is an upper-bound convention, stated in the record)
    return {"occurrences": occ, "texts_with": texts_with,
            "position_shares": {k: round(pos[k] / occ, 4) for k in ("initial", "medial", "final")},
            "adjacency_counts": dict(adj),
            "adjacency_rate_per_occurrence": {k: round(v / occ, 4) for k, v in adj.items()},
            "top_neighbours": neigh.most_common(8)}

def passes_frozen_shape(form_profile, dev_funerary_share, min_texts=3):
    lo = max(0.0, dev_funerary_share - 0.25); hi = min(1.0, dev_funerary_share + 0.25)
    fs = form_profile["funerary_share_of_occurrences"]
    return bool(form_profile["total_texts_with"] >= min_texts and fs is not None and lo <= fs <= hi)

# ================= Step 2: anchor-only baseline =================
A = {}
A["vocab_entries_theonym_family"] = [
    {"norm": v["norm"], "form": v["form"], "gloss": v["gloss"],
     "confidence": v["confidence"], "origin": v["origin"]}
    for v in vocab if v["norm"] in ("sorey", "wos", "wosi", "soreyi", "asoreyi")]
for f in ("sorey", "wos", "wosi", "soreyi", "asoreyi"):
    A[f] = {"dev": profile(f, dev), "held": profile(f, held),
            "dev_context": context_stats(f, dev), "held_context": context_stats(f, held)}
# does the anchor itself meet soreyi's frozen prediction shape on held-out?
A["sorey_meets_soreyi_frozen_shape_on_heldout"] = passes_frozen_shape(
    A["sorey"]["held"], A["sorey"]["dev"]["funerary_share_of_occurrences"] or 0.0)
# variant class sorey+soreyi+asoreyi combined
def combined_profile(forms, texts):
    per = {}
    for d in texts:
        toks = P.tokens_of(d["text"])
        n = sum(toks.count(f) for f in forms)
        e = per.setdefault(d["stratum"], {"occurrences": 0, "texts_with": 0, "texts": 0})
        e["occurrences"] += n; e["texts_with"] += (n > 0); e["texts"] += 1
    tot = sum(v["occurrences"] for v in per.values())
    return {"per_stratum": per, "total_occurrences": tot,
            "total_texts_with": sum(v["texts_with"] for v in per.values()),
            "funerary_share_of_occurrences": (per.get("funerary", {}).get("occurrences", 0) / tot) if tot else None}
A["variant_class_sorey_soreyi_asoreyi"] = {"dev": combined_profile(["sorey", "soreyi", "asoreyi"], dev),
                                           "held": combined_profile(["sorey", "soreyi", "asoreyi"], held)}
# same-text co-occurrence of sorey and soreyi
def cooccur(f1, f2, texts):
    both = only1 = only2 = neither = 0
    for d in texts:
        toks = set(P.tokens_of(d["text"]))
        a, b = f1 in toks, f2 in toks
        if a and b: both += 1
        elif a: only1 += 1
        elif b: only2 += 1
        else: neither += 1
    return {"both": both, f"only_{f1}": only1, f"only_{f2}": only2, "neither": neither, "texts": len(texts)}
A["cooccurrence_sorey_soreyi"] = {
    "dev_all": cooccur("sorey", "soreyi", dev),
    "held_all": cooccur("sorey", "soreyi", held),
    "held_funerary": cooccur("sorey", "soreyi", [d for d in held if d["stratum"] == "funerary"]),
    "dev_funerary": cooccur("sorey", "soreyi", [d for d in dev if d["stratum"] == "funerary"])}
out["anchor_only_baseline"] = A

# ================= Step 3: genre/formula baseline =================
G = {}
# full Stage 4.3 pool: dev freq >= 10, len >= 3, not in frozen vocabulary
freq = collections.Counter(); sfreq = collections.defaultdict(collections.Counter)
for d in dev:
    for t in P.tokens_of(d["text"]):
        freq[t] += 1; sfreq[t][d["stratum"]] += 1
pool = [t for t, c in freq.items() if c >= 10 and len(t) >= 3 and P.norm_form(t) not in known]
def pool_pass(form):
    devfun = sfreq[form]["funerary"] / freq[form]
    hp = profile(form, held)
    return devfun, hp, passes_frozen_shape(hp, devfun)
rows = []
for t in pool:
    devfun, hp, ok = pool_pass(t)
    rows.append({"form": t, "dev_occ": freq[t], "dev_funerary_share": round(devfun, 4),
                 "held_texts_with": hp["total_texts_with"],
                 "held_funerary_share": hp["funerary_share_of_occurrences"], "passes": ok})
def summarise(rs):
    return {"n": len(rs), "passes": sum(r["passes"] for r in rs),
            "pass_rate": round(sum(r["passes"] for r in rs) / len(rs), 4) if rs else None}
G["pool_all"] = summarise(rows)
G["pool_dev_funerary_share_ge_0.80"] = summarise([r for r in rows if r["dev_funerary_share"] >= 0.80])
G["pool_dev_funerary_share_eq_1.0"] = summarise([r for r in rows if r["dev_funerary_share"] == 1.0])
G["pool_dev_occ_ge_50"] = summarise([r for r in rows if r["dev_occ"] >= 50])
G["pool_dev_occ_ge_100"] = summarise([r for r in rows if r["dev_occ"] >= 100])
G["pool_rows_sorted_by_dev_occ"] = sorted(rows, key=lambda r: -r["dev_occ"])
G["candidates_within_pool_frame"] = [r for r in rows if r["form"] in
    ("soreyi", "asoreyi", "xolkete", "pxolkete", "xolkte", "wisi")]
# formula carriage: the wos invocation context
held_fun = [d for d in held if d["stratum"] == "funerary"]
dev_fun = [d for d in dev if d["stratum"] == "funerary"]
def presence(form, texts):
    return sum(1 for d in texts if form in P.tokens_of(d["text"]))
G["formula_recurrence"] = {
    "dev_funerary_texts": len(dev_fun), "held_funerary_texts": len(held_fun),
    "dev_funerary_with_wos": presence("wos", dev_fun), "held_funerary_with_wos": presence("wos", held_fun),
    "dev_funerary_with_wosi": presence("wosi", dev_fun), "held_funerary_with_wosi": presence("wosi", held_fun),
    "dev_funerary_with_sorey": presence("sorey", dev_fun), "held_funerary_with_sorey": presence("sorey", held_fun),
    "dev_funerary_with_soreyi": presence("soreyi", dev_fun), "held_funerary_with_soreyi": presence("soreyi", held_fun)}
G["pool_passers"] = sorted([r for r in rows if r["passes"]], key=lambda r: -r["dev_occ"])
def conditional_on(texts, cond_form, target="soreyi"):
    a = b = c = dd = 0
    for d in texts:
        toks = set(P.tokens_of(d["text"]))
        w, s = cond_form in toks, target in toks
        if w and s: a += 1
        elif w: b += 1
        elif s: c += 1
        else: dd += 1
    return {f"{cond_form}_and_{target}": a, f"{cond_form}_only": b, f"{target}_only": c, "neither": dd,
            f"p_{target}_given_{cond_form}": round(a / (a + b), 4) if a + b else None,
            f"p_{target}_given_no_{cond_form}": round(c / (c + dd), 4) if c + dd else None}
G["soreyi_given_wosi_held_funerary"] = conditional_on(held_fun, "wosi")
G["soreyi_given_wosi_dev_funerary"] = conditional_on(dev_fun, "wosi")
def bigram_texts(texts, f1="wosi", f2="soreyi"):
    fwd = rev = 0
    for d in texts:
        toks = P.tokens_of(d["text"])
        pairs = set(zip(toks, toks[1:]))
        if (f1, f2) in pairs: fwd += 1
        if (f2, f1) in pairs: rev += 1
    return {"texts_with_wosi_soreyi_adjacent_in_order": fwd,
            "texts_with_soreyi_wosi_adjacent_in_order": rev, "texts": len(texts)}
G["invocation_bigram_dev_funerary"] = bigram_texts(dev_fun)
G["invocation_bigram_held_funerary"] = bigram_texts(held_fun)
for f in ("wosi",):
    rate = presence(f, dev_fun) / len(dev_fun)
    G[f"expected_held_funerary_texts_{f}"] = {"dev_funerary_text_presence_rate": round(rate, 4),
                                              "expected_in_16_held_funerary": round(rate * 16, 2),
                                              "observed_held_funerary_texts": presence(f, held_fun)}
# conditional: soreyi presence given wos presence, held-out funerary
def conditional(texts):
    a = b = c = dd = 0
    for d in texts:
        toks = set(P.tokens_of(d["text"]))
        w, s = "wos" in toks, "soreyi" in toks
        if w and s: a += 1
        elif w: b += 1
        elif s: c += 1
        else: dd += 1
    return {"wos_and_soreyi": a, "wos_only": b, "soreyi_only": c, "neither": dd,
            "p_soreyi_given_wos": round(a / (a + b), 4) if a + b else None,
            "p_soreyi_given_no_wos": round(c / (c + dd), 4) if c + dd else None}
G["soreyi_given_wos_held_funerary"] = conditional(held_fun)
G["soreyi_given_wos_dev_funerary"] = conditional(dev_fun)
# dev funerary text-presence rate -> expected held-out funerary texts under genre recurrence alone
for f in ("soreyi", "sorey", "wos"):
    rate = presence(f, dev_fun) / len(dev_fun)
    G[f"expected_held_funerary_texts_{f}"] = {"dev_funerary_text_presence_rate": round(rate, 4),
                                              "expected_in_16_held_funerary": round(rate * 16, 2),
                                              "observed_held_funerary_texts": presence(f, held_fun)}
# anchored funerary-formula controls on held-out (same profile shape as the candidates)
G["anchored_controls_heldout_profiles"] = {f: profile(f, held) for f in
    ("ato", "mk", "kdi", "ste", "qore", "tedxe", "terike")}
G["anchored_controls_dev_profiles"] = {f: {"total_occurrences": profile(f, dev)["total_occurrences"],
                                           "funerary_share_of_occurrences": profile(f, dev)["funerary_share_of_occurrences"]}
                                       for f in ("ato", "mk", "kdi", "ste", "qore", "tedxe", "terike")}
out["genre_formula_baseline"] = G

json.dump(out, open(f"{REC}/od20-soreyi-baseline-results-2026-11-22.json", "w"), indent=1, ensure_ascii=False)
print("stage43 repro:", out["reproduction_stage43_exact"])
print("stage44 repro:", out["reproduction_stage44_candidates_exact"], out["reproduction_stage44_controls_exact"])
print("pool:", G["pool_all"], G["pool_dev_funerary_share_eq_1.0"], G["pool_dev_occ_ge_100"])
print("written", f"{REC}/od20-soreyi-baseline-results-2026-11-22.json")
