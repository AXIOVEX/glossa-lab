#!/usr/bin/env python3
"""Spec 103 conformance addendum: corrected spec.md section 3.4 checker,
audit of the already-held witnesses, and replay of the Stage 1
classifications.

Commissioned by Round E unit E-M-1 (adjudication
specs/091-anchor-comparison-integrity/records/
coscientist-sweep-adjudication-2026-11-25.md section 3.1) and
registered in records/conformance-addendum-registration-2026-11-25.md,
which states the adjudicated treatment this script implements.
The filed Stage 1 script (records/stage-1-execution-script.py,
SHA-256 661f0afc...) is not edited; its classification functions are
re-implemented here unchanged as the control. The corrected
implementation differs from the filed one in exactly the two
registered places: witness aggregation (no any-witness pass;
disagreement is explicit) and uncertainty retention (markup in a
witness is carried through classification as a flag on the token).

Runs on tower-compute against the pinned Kovetsky build. Outputs
aggregate/record-form JSON only; no witness text is written out
(witness keys, token verdicts, flags and counts only). Non-open
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
REPO = Path.home() / ".syncyard/worktrees/glossa/sw103-addendum"
FORMS = ["soreyi", "asoreyi", "xolkete", "pxolkete", "xolkte", "wisi"]
ANCHORS = ["ato", "qore", "kdi", "ste", "mk"]
STRATA = {"funerary": "funerary",
          "royal or temple (stela, wall, cartouche, label)": "royal_temple",
          "document (ostracon, papyrus, wood, vessel)": "document",
          "graffito": "graffito"}
# The filed expansion preprocessing set (filed expansion_tokens below).
MARKUP_EXPANSION = set("[]?!|:=")
# Markup recognised in open alternative readings (registration section 2).
MARKUP_READING = set("[]?!")


# ---------- tokenization: filed forms (control) ----------

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
    """Filed form, unchanged (control)."""
    raw = rec.get("text_corpus") or rec.get("text_std") or ""
    t = fold(raw.lower())
    t = re.sub(r"[\[\]?!|:=]", ".", t)
    return [x for x in re.split(r"[\s.]+", t) if x and not x.startswith("#")]


# ---------- tokenization: uncertainty-retaining forms (corrected) ----------

def expansion_tokens_flagged(rec):
    """The frozen tokenization's tokens, each with an uncertainty flag.

    Token identity is the filed pipeline's exactly: the folded text
    with the filed markup set replaced by separators, split on
    whitespace and dots. The replacement is character-for-character,
    so a token's span in the transformed string is its span in the
    folded record text; a token is uncertainty-bearing when a markup
    character stood immediately adjacent to its span (registration
    section 2 of the adjudicated treatment)."""
    raw = rec.get("text_corpus") or rec.get("text_std") or ""
    t = fold(raw.lower())
    t2 = "".join("." if c in MARKUP_EXPANSION else c for c in t)
    out = []
    for m in re.finditer(r"[^\s.]+", t2):
        tok = m.group()
        if tok.startswith("#"):
            continue
        s, e = m.span()
        unc = (s > 0 and t[s - 1] in MARKUP_EXPANSION) or \
              (e < len(t) and t[e] in MARKUP_EXPANSION)
        out.append((tok, unc))
    return out


def reading_tokens_flagged(text):
    """Filed tokens_of identity per token; a token containing any of
    [ ] ? ! has those characters removed for comparison and carries
    the uncertainty flag (registration section 2)."""
    out = []
    for tok in tokens_of(text):
        clean = "".join(c for c in tok if c not in MARKUP_READING)
        if clean:
            out.append((clean, clean != tok))
    return out


# ---------- witness collection ----------

def build_expansion_index(kov):
    expansion = {}
    exp_files = [kov / "data/expansion" / f for f in
                 ["griffith_mi1a.jsonl", "griffith_mi1b.jsonl", "griffith_mi2a.jsonl",
                  "griffith_mi2b.jsonl", "griffith_meroe.jsonl"]] + \
                [kov / "data/expansion/karanog/griffith_karanog.jsonl",
                 kov / "data/expansion/faras/griffith_faras.jsonl"]
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
                expansion[rem] = {"file": f.name,
                                  "tokens": expansion_tokens(rec),
                                  "pairs": expansion_tokens_flagged(rec),
                                  "raw": rec.get("text_corpus") or rec.get("text_std") or ""}
    return expansion


def collect_witnesses(entry, expansion):
    """Witness list for a basis entry: open alternative readings and
    the expansion transcription of the preferred reading's source.
    Each witness carries its filed token list, its flagged token
    pairs, and its raw text (for the audit scan only; never output)."""
    ws = []
    row = entry["row"]
    for r in row.get("readings") or []:
        if r.get("open") and r.get("text") and r.get("key") != row.get("open_reading"):
            ws.append({"id": f"reading:{r['key']}", "kind": "reading",
                       "tokens": tokens_of(r["text"]),
                       "pairs": reading_tokens_flagged(r["text"]),
                       "raw": r["text"]})
    for rm in [str(x).lstrip("0") or "0" for x in (row.get("rem") or [])]:
        if rm in expansion:
            e = expansion[rm]
            ws.append({"id": f"expansion:{e['file']}", "kind": "expansion",
                       "tokens": e["tokens"], "pairs": e["pairs"],
                       "raw": e["raw"]})
            break
    return ws


# ---------- witness verdicts ----------

def witness_verdict(tokens, form):
    """Filed form, unchanged (control)."""
    if form in tokens:
        return "attests_form"
    if any(lev(t, form) == 1 for t in tokens):
        return "attests_variant"
    if any(form in t or t in form for t in tokens if len(t) >= 3):
        return "partial_or_containment"
    return "absent"


def witness_verdict_flagged(pairs, form):
    """Corrected: an attestation resting only on uncertainty-bearing
    tokens is an uncertain attestation."""
    form_occs = [u for t, u in pairs if t == form]
    if form_occs:
        return "attests_form" if not all(form_occs) else "attests_form_uncertain"
    var_occs = [u for t, u in pairs if lev(t, form) == 1]
    if var_occs:
        return "attests_variant" if not all(var_occs) else "attests_variant_uncertain"
    toks = [t for t, u in pairs]
    if any(form in t or t in form for t in toks if len(t) >= 3):
        return "partial_or_containment"
    return "absent"


def near_presence(pairs, near_token):
    """Whether a witness carries the near token, and whether that
    carrying is uncertainty-bearing only."""
    occs = [u for t, u in pairs if t == near_token]
    if not occs:
        return "absent"
    return "uncertain" if all(occs) else "present"


# ---------- filed classification (control, unchanged logic) ----------

def classify_counted_filed(ws, form):
    verdicts = {w["id"]: witness_verdict(w["tokens"], form) for w in ws}
    if not verdicts:
        return "WITNESS UNAVAILABLE", verdicts
    vals = list(verdicts.values())
    if "attests_form" in vals:
        return "FAITHFUL", verdicts
    if "attests_variant" in vals:
        return "FAITHFUL (variant noted)", verdicts
    if "partial_or_containment" in vals:
        return "UNCERTAIN", verdicts
    if any(k.startswith("expansion:") for k in verdicts):
        return "DISCREPANCY", verdicts
    return "UNCERTAIN", verdicts


def classify_near_filed(ws, form, near_token):
    verdicts = {w["id"]: witness_verdict(w["tokens"], form) for w in ws}
    if not verdicts:
        return "WITNESS UNAVAILABLE", verdicts
    vals = list(verdicts.values())
    if "attests_form" in vals:
        return "DISCREPANCY (missed count)", verdicts
    if near_token in sum([w["tokens"] for w in ws], []):
        return "FAITHFUL (source carries the distinct near form)", verdicts
    if "attests_variant" in vals or "partial_or_containment" in vals:
        return "UNCERTAIN", verdicts
    return "UNCERTAIN", verdicts


# ---------- corrected classification (adjudicated treatment) ----------

ATTEST = {"attests_form", "attests_variant"}
UNCERT = {"attests_form_uncertain", "attests_variant_uncertain",
          "partial_or_containment"}


def aggregate_counted(verdicts):
    """Registration section 4, in precedence order."""
    if not verdicts:
        return "WITNESS UNAVAILABLE"
    vals = list(verdicts.values())
    attest = any(v in ATTEST for v in vals)
    absent = any(v == "absent" for v in vals)
    uncert = any(v in UNCERT for v in vals)
    if attest and absent:
        return "DISCREPANCY"
    if all(v == "absent" for v in vals):
        if any(k.startswith("expansion:") for k in verdicts):
            return "DISCREPANCY"
        return "UNCERTAIN"
    if uncert or absent:
        return "UNCERTAIN"
    if "attests_variant" in vals:
        return "FAITHFUL (variant noted)"
    return "FAITHFUL"


def classify_counted_corrected(ws, form):
    verdicts = {w["id"]: witness_verdict_flagged(w["pairs"], form) for w in ws}
    return aggregate_counted(verdicts), verdicts


def aggregate_near(verdicts, presences, near_token, form):
    """Registration section 5, in precedence order. When the near
    token is the form itself (raw-substring loci), presence of the
    near token is attestation of the form and is not used."""
    if not verdicts:
        return "WITNESS UNAVAILABLE"
    exp_attests = any(k.startswith("expansion:") and v == "attests_form"
                      for k, v in verdicts.items())
    any_attests = any(v == "attests_form" for v in verdicts.values())
    form_uncertain = any(v == "attests_form_uncertain" for v in verdicts.values())
    if near_token == form:
        near_present = near_uncert = False
    else:
        near_present = any(p == "present" for p in presences.values())
        near_uncert = any(p == "uncertain" for p in presences.values())
    if exp_attests:
        return "DISCREPANCY (missed count)"
    if any_attests and not near_present and not near_uncert:
        return "DISCREPANCY (missed count)"
    if any_attests or form_uncertain:
        return "UNCERTAIN"
    if near_present and not near_uncert:
        return "FAITHFUL (source carries the distinct near form)"
    return "UNCERTAIN"


def classify_near_corrected(ws, form, near_token):
    verdicts = {w["id"]: witness_verdict_flagged(w["pairs"], form) for w in ws}
    presences = {w["id"]: near_presence(w["pairs"], near_token) for w in ws}
    return aggregate_near(verdicts, presences, near_token, form), verdicts


# ---------- basis (frozen pipeline semantics, as filed) ----------

def build_basis(kov):
    rows = [json.loads(l) for l in open(kov / "data/inscriptions.jsonl", encoding="utf-8")]
    seen = {}
    for d in rows:
        t = (d.get("text") or "").strip()
        if t and t not in seen:
            seen[t] = d
    dev, held = [], []
    for t, d in seen.items():
        stratum = STRATA.get(d.get("kind", "?"), "other")
        h = int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16) % 10
        (held if h == 0 else dev).append(
            {"text": t, "stratum": stratum, "rem": d.get("id"), "row": d})
    basis = {
        "index_rows": len(rows),
        "distinct_texts": len(seen),
        "dev_texts": len(dev),
        "held_texts": len(held),
        "held_strata": dict(collections.Counter(x["stratum"] for x in held)),
        "dev_strata": dict(collections.Counter(x["stratum"] for x in dev)),
    }
    return basis, held


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


# ---------- Step 4 machinery (filed, unchanged) ----------

def step4(form, loci, near, counted_entries, held, frozen_cand):
    frozen_twf = sum(v["texts_with_form"] for v in frozen_cand["per_stratum"].values())
    frozen_fun = frozen_cand["per_stratum"].get("funerary", {}).get("texts_with_form", 0)
    frozen_share = frozen_cand["heldout_funerary_share"] or 0.0

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

    def could_cross():
        rem_unc = [l for l in loci if l["classification"] in
                   ("UNCERTAIN", "WITNESS UNAVAILABLE")]
        add_unc_fun = {n["rem"] for n in near if n["classification"] in
                       ("UNCERTAIN", "WITNESS UNAVAILABLE") and n["stratum"] == "funerary"}
        add_unc_nonfun = {n["rem"] for n in near if n["classification"] in
                          ("UNCERTAIN", "WITNESS UNAVAILABLE") and n["stratum"] != "funerary"}
        base_texts = corr_texts - {l["rem"] for l in loci if l["classification"] == "DISCREPANCY"}
        base_fun = corr_fun - {l["rem"] for l in loci if l["classification"] == "DISCREPANCY"}
        scenarios = []
        t1 = (base_texts - {l["rem"] for l in rem_unc}) | add_unc_nonfun
        f1 = base_fun - {l["rem"] for l in rem_unc}
        scenarios.append(legs(len(t1), (len(f1) / len(t1)) if t1 else 0.0))
        t2 = base_texts | add_unc_fun | add_unc_nonfun
        f2 = base_fun | add_unc_fun
        scenarios.append(legs(len(t2), (len(f2) / len(t2)) if t2 else 0.0))
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
    return {"corrected": {"texts_with_form": corr_twf, "share": corr_share,
                          "legs": corr_legs},
            "boundary_crossed": crossed, "outcome": outcome}


# ---------- main replay ----------

def main():
    expansion = build_expansion_index(KOV)
    basis, held = build_basis(KOV)
    frozen = json.load(open(REPO / "specs/097-meroitic-reproduction-benchmark/records/stage-4-4-results.json"))
    filed = json.load(open(REPO / "specs/103-meroitic-source-witness-check/records/stage-1-results-2026-11-23.json"))

    # Step 1 reproduction
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
    coverage = []
    for x in held:
        ws = collect_witnesses(x, expansion)
        nalts = sum(1 for w in ws if w["kind"] == "reading")
        has_exp = any(w["kind"] == "expansion" for w in ws)
        coverage.append({"rem": x["rem"], "stratum": x["stratum"],
                         "alt_readings": nalts, "expansion": has_exp,
                         "any_witness": bool(ws)})
    step1["witness_coverage"] = coverage
    step1["held_texts_without_any_witness"] = [c["rem"] for c in coverage if not c["any_witness"]]
    step1_matches_filed = (
        step1["basis"] == filed["step1"]["basis"] and
        step1["forms"] == filed["step1"]["forms"] and
        step1["anchors_match"] == filed["step1"]["anchors_match"] and
        step1["held_strata_match"] == filed["step1"]["held_strata_match"] and
        step1["witness_coverage"] == filed["step1"]["witness_coverage"] and
        step1["held_texts_without_any_witness"] == filed["step1"]["held_texts_without_any_witness"])

    # Audit: markup incidence over every witness of every held-out text
    audit = {"held_texts_with_markup_in_any_witness": [],
             "witnesses_with_markup": 0, "witnesses_total": 0}
    for x in held:
        ws = collect_witnesses(x, expansion)
        marked = False
        for w in ws:
            audit["witnesses_total"] += 1
            chars = MARKUP_EXPANSION if w["kind"] == "expansion" else MARKUP_READING
            if any(c in chars for c in w["raw"]):
                audit["witnesses_with_markup"] += 1
                marked = True
        if marked:
            audit["held_texts_with_markup_in_any_witness"].append(x["rem"])

    out = {"step1": step1, "step1_matches_filed": step1_matches_filed,
           "audit": audit, "forms": {}, "diff": [], "control_mismatches": []}

    for cand in frozen["candidates"]:
        form = cand["form"]
        if form not in FORMS:
            continue
        filed_form = filed["forms"][form]
        counted_entries = [x for x in held if form in tokens_of(x["text"])]

        loci = []
        for x in counted_entries:
            ws = collect_witnesses(x, expansion)
            fc, fv = classify_counted_filed(ws, form)
            cc, cv = classify_counted_corrected(ws, form)
            loci.append({"rem": x["rem"], "stratum": x["stratum"],
                         "occurrences": tokens_of(x["text"]).count(form),
                         "filed_classification": fc, "corrected_classification": cc,
                         "filed_witness_verdicts": fv, "corrected_witness_verdicts": cv,
                         "mixed_filed_verdicts": len(set(fv.values())) > 1,
                         "uncertainty_bearing": any(v in UNCERT for v in cv.values())})
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
                    ws = collect_witnesses(x, expansion)
                    fc, fv = classify_near_filed(ws, form, t)
                    cc, cv = classify_near_corrected(ws, form, t)
                    near.append({"rem": x["rem"], "stratum": x["stratum"], "token": t,
                                 "kind": kind,
                                 "filed_classification": fc, "corrected_classification": cc,
                                 "filed_witness_verdicts": fv, "corrected_witness_verdicts": cv,
                                 "uncertainty_bearing": any(v in UNCERT for v in cv.values()) or
                                 any(near_presence(w["pairs"], t) == "uncertain" for w in ws)})
            low = x["text"].lower()
            if form in low and form not in toks:
                if not any(n["rem"] == x["rem"] for n in near):
                    ws = collect_witnesses(x, expansion)
                    fc, fv = classify_near_filed(ws, form, form)
                    cc, cv = classify_near_corrected(ws, form, form)
                    near.append({"rem": x["rem"], "stratum": x["stratum"], "token": form,
                                 "kind": "raw_substring_not_token_aligned",
                                 "filed_classification": fc, "corrected_classification": cc,
                                 "filed_witness_verdicts": fv, "corrected_witness_verdicts": cv,
                                 "uncertainty_bearing": any(v in UNCERT for v in cv.values())})

        # Control check: filed rules reproduce the filed results locus for locus
        filed_counted = {(l["rem"]): l for l in filed_form["counted_loci"]}
        for l in loci:
            fl = filed_counted.get(l["rem"])
            if fl is None or fl["classification"] != l["filed_classification"] or \
               fl["witness_verdicts"] != l["filed_witness_verdicts"]:
                out["control_mismatches"].append(
                    {"form": form, "kind": "counted", "rem": l["rem"],
                     "control": l["filed_classification"], "filed": fl["classification"] if fl else None})
            if l["filed_classification"] != l["corrected_classification"]:
                out["diff"].append({"form": form, "kind": "counted", "rem": l["rem"],
                                    "filed": l["filed_classification"],
                                    "corrected": l["corrected_classification"],
                                    "mixed_filed_verdicts": l["mixed_filed_verdicts"],
                                    "uncertainty_bearing": l["uncertainty_bearing"]})
        filed_near = {(n["rem"], n["token"]): n for n in filed_form["near_form_census"]}
        for n in near:
            fn = filed_near.get((n["rem"], n["token"]))
            if fn is None or fn["classification"] != n["filed_classification"] or \
               fn["witness_verdicts"] != n["filed_witness_verdicts"]:
                out["control_mismatches"].append(
                    {"form": form, "kind": "near", "rem": n["rem"], "token": n["token"],
                     "control": n["filed_classification"], "filed": fn["classification"] if fn else None})
            if n["filed_classification"] != n["corrected_classification"]:
                out["diff"].append({"form": form, "kind": "near", "rem": n["rem"],
                                    "token": n["token"],
                                    "filed": n["filed_classification"],
                                    "corrected": n["corrected_classification"],
                                    "uncertainty_bearing": n["uncertainty_bearing"]})

        s4_filed = step4(form, [{"rem": l["rem"], "classification": l["filed_classification"]} for l in loci],
                         [{"rem": n["rem"], "stratum": n["stratum"], "classification": n["filed_classification"]} for n in near],
                         counted_entries, held, cand)
        s4_corr = step4(form, [{"rem": l["rem"], "classification": l["corrected_classification"]} for l in loci],
                        [{"rem": n["rem"], "stratum": n["stratum"], "classification": n["corrected_classification"]} for n in near],
                        counted_entries, held, cand)
        out["forms"][form] = {
            "frozen": filed_form["frozen"],
            "counted_loci": loci,
            "near_form_census": near,
            "sub_threshold_fragments": fragments,
            "control_step4_outcome": s4_filed["outcome"],
            "filed_outcome": filed_form["outcome"],
            "corrected_step4": s4_corr,
            "corrected_outcome": s4_corr["outcome"],
        }

    out["tc103_09"] = {
        "step1_matches_filed": step1_matches_filed,
        "control_mismatches": len(out["control_mismatches"]),
        "diff_count": len(out["diff"]),
        "diff_all_flagged": all(d.get("mixed_filed_verdicts") or d.get("uncertainty_bearing")
                                for d in out["diff"]),
    }
    out["tc103_10"] = {
        "outcomes_preserved": all(
            f["corrected_outcome"] == f["filed_outcome"] for f in out["forms"].values()),
        "table": {form: {"filed": f["filed_outcome"], "corrected": f["corrected_outcome"]}
                  for form, f in out["forms"].items()},
    }
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
