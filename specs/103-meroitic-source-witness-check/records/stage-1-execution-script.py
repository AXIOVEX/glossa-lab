#!/usr/bin/env python3
"""Spec 103 Stage 1 execution: the Meroitic source-witness check.

Implements specs/103-meroitic-source-witness-check/spec.md section 3
exactly: basis reproduction (Step 1), locus + near-form census
(Step 2), witness comparison (Step 3), boundary adjudication
(Step 4). Runs on tower-compute against the pinned Kovetsky build.
Outputs aggregate/record-form JSON only; no witness text is written
out (witness keys, token verdicts and counts only). Non-open
readings are never read for text (they carry none in the build).
"""
import collections
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

KOV = Path.home() / ".syncyard/worktrees/glossa/kovetsky-src"
REPO = Path.home() / ".syncyard/worktrees/glossa/sw103-exec"
FORMS = ["soreyi", "asoreyi", "xolkete", "pxolkete", "xolkte", "wisi"]
ANCHORS = ["ato", "qore", "kdi", "ste", "mk"]
STRATA = {"funerary": "funerary",
          "royal or temple (stela, wall, cartouche, label)": "royal_temple",
          "document (ostracon, papyrus, wood, vessel)": "document",
          "graffito": "graffito"}


def tokens_of(text):
    return [t for t in re.split(r"[\s.]+", text.lower()) if t and not t.startswith("#")]


def lev(a, b):
    if abs(len(a) - len(b)) > 1:
        return 2
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def expansion_tokens(rec):
    raw = rec.get("text_corpus") or rec.get("text_std") or ""
    t = fold(raw.lower())
    t = re.sub(r"[\[\]?!|:=]", ".", t)
    return [x for x in re.split(r"[\s.]+", t) if x and not x.startswith("#")]


# ---------- basis (frozen pipeline semantics, path adjusted only) ----------
rows = [json.loads(l) for l in open(KOV / "data/inscriptions.jsonl", encoding="utf-8")]
seen = {}
for d in rows:
    t = (d.get("text") or "").strip()
    if t and t not in seen:
        seen[t] = d
dev, held = [], []
for t, d in seen.items():
    stratum = STRATA.get(d.get("kind", "?"), "other")
    h = int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16) % 10
    (held if h == 0 else dev).append({"text": t, "stratum": stratum, "rem": d.get("id"), "row": d})

basis = {
    "index_rows": len(rows),
    "distinct_texts": len(seen),
    "dev_texts": len(dev),
    "held_texts": len(held),
    "held_strata": dict(collections.Counter(x["stratum"] for x in held)),
    "dev_strata": dict(collections.Counter(x["stratum"] for x in dev)),
}

frozen = json.load(open(REPO / "specs/097-meroitic-reproduction-benchmark/records/stage-4-4-results.json"))


def stage44_counts(form, texts):
    per = {}
    for stratum in ["royal_temple", "graffito", "funerary", "document", "other"]:
        st = [x for x in texts if x["stratum"] == stratum]
        if not st:
            continue
        occ = sum(tokens_of(x["text"]).count(form) for x in st)
        twf = sum(1 for x in st if form in tokens_of(x["text"]))
        per[stratum] = {"held_texts": len(st), "occurrences": occ, "texts_with_form": twf}
    tot_twf = sum(v["texts_with_form"] for v in per.values())
    fun_twf = per.get("funerary", {}).get("texts_with_form", 0)
    share = (fun_twf / tot_twf) if tot_twf else 0.0
    return per, share


step1 = {"basis": basis, "forms": {}, "anchors_match": None}
frozen_anchors = frozen["anchor_controls_heldout"]
recomputed_anchors = {}
for stratum in ["royal_temple", "graffito", "funerary", "document"]:
    st = [x for x in held if x["stratum"] == stratum]
    recomputed_anchors[stratum] = {
        a: sum(tokens_of(x["text"]).count(a) for x in st) for a in ANCHORS
        if sum(tokens_of(x["text"]).count(a) for x in st)}
step1["anchors_match"] = (recomputed_anchors == frozen_anchors)
step1["held_strata_match"] = (basis["held_strata"] ==
                              {k: v for k, v in frozen["heldout_texts_by_stratum"].items()})
for cand in frozen["candidates"]:
    form = cand["form"]
    per, share = stage44_counts(form, held)
    fshare = cand["heldout_funerary_share"]
    share_match = (share == fshare) or (fshare is None and share == 0.0)
    match = (per == {k: v for k, v in cand["per_stratum"].items()} and share_match)
    step1["forms"][form] = {"frozen_match": match, "recomputed_share": share,
                            "frozen_share": fshare}

# ---------- expansion witness index (by REM number) ----------
expansion = {}
exp_files = [KOV / "data/expansion" / f for f in
             ["griffith_mi1a.jsonl", "griffith_mi1b.jsonl", "griffith_mi2a.jsonl",
              "griffith_mi2b.jsonl", "griffith_meroe.jsonl"]] + \
            [KOV / "data/expansion/karanog/griffith_karanog.jsonl",
             KOV / "data/expansion/faras/griffith_faras.jsonl"]
for f in exp_files:
    if not f.exists():
        continue
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        rem = str(rec.get("rem") or "").lstrip("0") or "0"
        if rem and rem not in expansion:
            expansion[rem] = {"file": f.name, "tokens": expansion_tokens(rec)}


def witnesses_for(entry):
    """Return (alt_readings, expansion_rec) witness summaries for a basis entry."""
    row = entry["row"]
    alts = []
    for r in row.get("readings") or []:
        if r.get("open") and r.get("text") and r.get("key") != row.get("open_reading"):
            alts.append({"key": r["key"], "tokens": tokens_of(r["text"])})
    rems = [str(x).lstrip("0") or "0" for x in (row.get("rem") or [])]
    exp = None
    for rm in rems:
        if rm in expansion:
            exp = expansion[rm]
            break
    return alts, exp


def witness_verdict(tokens, form):
    """Classify one witness token list against a form."""
    if form in tokens:
        return "attests_form"
    if any(lev(t, form) == 1 for t in tokens):
        return "attests_variant"
    if any(form in t or t in form for t in tokens if len(t) >= 3):
        return "partial_or_containment"
    return "absent"


def classify_counted_locus(entry, form):
    alts, exp = witnesses_for(entry)
    verdicts = {}
    for a in alts:
        verdicts[f"reading:{a['key']}"] = witness_verdict(a["tokens"], form)
    if exp is not None:
        verdicts[f"expansion:{exp['file']}"] = witness_verdict(exp["tokens"], form)
    if not verdicts:
        return "WITNESS UNAVAILABLE", verdicts
    vals = list(verdicts.values())
    if "attests_form" in vals:
        return "FAITHFUL", verdicts
    if "attests_variant" in vals:
        return "FAITHFUL (variant noted)", verdicts
    if "partial_or_containment" in vals:
        return "UNCERTAIN", verdicts
    # all witnesses absent: discrepancy only if the preferred reading's own
    # source transcription (expansion) is among them
    if any(k.startswith("expansion:") for k in verdicts):
        return "DISCREPANCY", verdicts
    return "UNCERTAIN", verdicts


def classify_near_locus(entry, form, near_token):
    """A held text where the extraction did NOT count the form but a
    near-form token occurs. A witness attesting the form itself is a
    missed-count discrepancy; witnesses attesting only the near token
    confirm the extraction's distinction."""
    alts, exp = witnesses_for(entry)
    verdicts = {}
    for a in alts:
        verdicts[f"reading:{a['key']}"] = witness_verdict(a["tokens"], form)
    if exp is not None:
        verdicts[f"expansion:{exp['file']}"] = witness_verdict(exp["tokens"], form)
    if not verdicts:
        return "WITNESS UNAVAILABLE", verdicts
    vals = list(verdicts.values())
    if "attests_form" in vals:
        return "DISCREPANCY (missed count)", verdicts
    if near_token in sum([a["tokens"] for a in alts], []) or \
       (exp is not None and near_token in exp["tokens"]):
        return "FAITHFUL (source carries the distinct near form)", verdicts
    if "attests_variant" in vals or "partial_or_containment" in vals:
        return "UNCERTAIN", verdicts
    return "UNCERTAIN", verdicts


# ---------- witness coverage over the held-out partition ----------
coverage = []
for x in held:
    alts, exp = witnesses_for(x)
    coverage.append({"rem": x["rem"], "stratum": x["stratum"],
                     "alt_readings": len(alts), "expansion": bool(exp),
                     "any_witness": bool(alts) or exp is not None})
step1["witness_coverage"] = coverage
step1["held_texts_without_any_witness"] = [c["rem"] for c in coverage if not c["any_witness"]]

# ---------- Steps 2-4 per form ----------
out = {"step1": step1, "forms": {}}
for cand in frozen["candidates"]:
    form = cand["form"]
    if form not in FORMS:
        continue
    frozen_twf = sum(v["texts_with_form"] for v in cand["per_stratum"].values())
    frozen_fun = cand["per_stratum"].get("funerary", {}).get("texts_with_form", 0)
    frozen_share = cand["heldout_funerary_share"] or 0.0
    frozen_result = cand["heldout_result"]

    loci = []
    counted_entries = [x for x in held if form in tokens_of(x["text"])]
    for x in counted_entries:
        cls, verdicts = classify_counted_locus(x, form)
        loci.append({"rem": x["rem"], "stratum": x["stratum"],
                     "occurrences": tokens_of(x["text"]).count(form),
                     "classification": cls, "witness_verdicts": verdicts})

    near = []
    fragments = []
    for x in held:
        toks = tokens_of(x["text"])
        if form in toks:
            continue
        for t in set(toks):
            kind = None
            if lev(t, form) == 1:
                kind = "edit_distance_1"
            elif form in t or t in form:
                if min(len(t), len(form)) >= 3:
                    kind = "containment"
                else:
                    fragments.append({"rem": x["rem"], "stratum": x["stratum"],
                                      "token": t, "kind": "containment_fragment_lt3"})
                    continue
            if kind:
                cls, verdicts = classify_near_locus(x, form, t)
                near.append({"rem": x["rem"], "stratum": x["stratum"], "token": t,
                             "kind": kind, "classification": cls,
                             "witness_verdicts": verdicts})
        # raw substring occurrences not aligned to a token boundary
        low = x["text"].lower()
        tokset = toks
        if form in low and form not in tokset:
            if not any(n["rem"] == x["rem"] for n in near):
                cls, verdicts = classify_near_locus(x, form, form)
                near.append({"rem": x["rem"], "stratum": x["stratum"], "token": form,
                             "kind": "raw_substring_not_token_aligned",
                             "classification": cls, "witness_verdicts": verdicts})

    # Step 4: adjudication on DISCREPANCY only
    corr_texts = {x["rem"] for x in counted_entries}
    corr_fun = {x["rem"] for x in counted_entries if x["stratum"] == "funerary"}
    for l in loci:
        if l["classification"] == "DISCREPANCY":
            corr_texts.discard(l["rem"])
            corr_fun.discard(l["rem"])
    added = set()
    for n in near:
        if n["classification"].startswith("DISCREPANCY"):
            added.add(n["rem"])
    for rem in added:
        corr_texts.add(rem)
        e = next(x for x in held if x["rem"] == rem)
        if e["stratum"] == "funerary":
            corr_fun.add(rem)
    corr_twf = len(corr_texts)
    corr_share = (len(corr_fun) / corr_twf) if corr_twf else 0.0

    def legs(twf, share):
        return {"texts_leg": twf >= 3, "share_leg": 0.75 <= share <= 1.0}

    frozen_legs = legs(frozen_twf, frozen_share)
    corr_legs = legs(corr_twf, corr_share)
    frozen_result = frozen_legs["texts_leg"] and frozen_legs["share_leg"]
    crossed = (corr_legs["texts_leg"] and corr_legs["share_leg"]) != frozen_result

    # NOT CHECKED mechanical rule: uncertain/unavailable decision-bearing
    # loci whose least-favourable resolution could change either leg.
    def could_cross():
        # removals: counted loci uncertain/unavailable
        rem_unc = [l for l in loci if l["classification"] in
                   ("UNCERTAIN", "WITNESS UNAVAILABLE")]
        # additions: near loci uncertain/unavailable, per stratum
        add_unc_fun = {n["rem"] for n in near if n["classification"] in
                       ("UNCERTAIN", "WITNESS UNAVAILABLE") and n["stratum"] == "funerary"}
        add_unc_nonfun = {n["rem"] for n in near if n["classification"] in
                          ("UNCERTAIN", "WITNESS UNAVAILABLE") and n["stratum"] != "funerary"}
        base_texts = corr_texts - {l["rem"] for l in loci if l["classification"] == "DISCREPANCY"}
        base_fun = corr_fun - {l["rem"] for l in loci if l["classification"] == "DISCREPANCY"}
        scenarios = []
        # least favourable for a PASS: remove all uncertain counted, add all uncertain non-funerary near
        t1 = (base_texts - {l["rem"] for l in rem_unc}) | add_unc_nonfun
        f1 = base_fun - {l["rem"] for l in rem_unc}
        scenarios.append(legs(len(t1), (len(f1) / len(t1)) if t1 else 0.0))
        # least favourable for a FAIL: add all uncertain near (funerary first for share)
        t2 = base_texts | add_unc_fun | add_unc_nonfun
        f2 = base_fun | add_unc_fun
        scenarios.append(legs(len(t2), (len(f2) / len(t2)) if t2 else 0.0))
        # share-only stress for PASS: add non-funerary only
        t3 = base_texts | add_unc_nonfun
        f3 = base_fun
        scenarios.append(legs(len(t3), (len(f3) / len(t3)) if t3 else 0.0))
        return any((s["texts_leg"] and s["share_leg"]) != frozen_result
                   for s in scenarios)

    if crossed:
        outcome = "CLAIM KILLED"
    elif could_cross():
        outcome = "NOT CHECKED - INCOMPLETE COVERAGE"
    else:
        outcome = "CLAIM STANDS"

    out["forms"][form] = {
        "frozen": {"texts_with_form": frozen_twf, "funerary_texts_with_form": frozen_fun,
                   "share": frozen_share, "result": frozen_result, "legs": frozen_legs},
        "counted_loci": loci,
        "near_form_census": near,
        "sub_threshold_fragments": fragments,
        "corrected": {"texts_with_form": corr_twf, "share": corr_share, "legs": corr_legs},
        "boundary_crossed": crossed,
        "outcome": outcome,
    }

print(json.dumps(out, indent=1))
