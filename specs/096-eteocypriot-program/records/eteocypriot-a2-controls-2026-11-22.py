#!/usr/bin/env python3
"""Spec 096 / OD-10 — A2 baselines and negative controls.

Runs the frozen A2 method of the E1 driver
(records/eteocypriot-e1-driver.py, imported unmodified: its
derive_cv and lccs are the method) against:

  (a) the executed corpus bytes (freeze commit 173882a2,
      SHA-256 = the freeze pin), with the analysis-bearing
      fields of the current corpus file (version 1.1.1)
      checked byte-identical to them first;
  baselines B-LONG (longest segment), B-FIRST (segment 1),
  B-RAND (analytic chance expectation);
  negative controls, all structure-preserving in the sense
  of adjudication unit E-8:
    NC-1  sign-relabel: a uniform random permutation of the
          attested sign alphabet applied to every segment
          token (segment lengths, repetition structure and
          token order preserved; only sign identity is
          destroyed). D(name) is held fixed.
    NC-2  name-scramble: a uniform random permutation of
          each Greek name's letters (letter multiset
          preserved), re-derived by the frozen R1-R3 path.
          Segments held fixed.
    NC-3  wrong text: the two derived spellings paired
          against the Greek syllabic control excerpt
          (ICS 217, 16 segments) — real syllabic text in the
          same signary, not the bilingual's counterpart.
          No recovery is defined; the LCCS profile is the
          calibration.

999 replicates for NC-1 and NC-2, seeded; deterministic.
No parameter of the frozen method is changed. This script
computes exploratory quantities only (adjudication OD-10);
it scores no claim and changes no verdict.
"""
import hashlib
import importlib.util
import json
import random
import subprocess
import sys

HERE = sys.argv[1]  # specs/096-eteocypriot-program directory
REPO = sys.argv[2]  # repo root of the worker clone
REPLICATES = 999
SEED = 20261122

spec = importlib.util.spec_from_file_location(
    "e1driver", f"{HERE}/records/eteocypriot-e1-driver.py")
drv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drv)

# --- the executed corpus bytes, from git history ---------------
raw = subprocess.run(
    ["git", "-C", REPO, "show", "173882a2:specs/096-eteocypriot-program/corpus/corpus.json"],
    capture_output=True, check=True).stdout
file_sha = hashlib.sha256(raw).hexdigest()
assert file_sha == drv.EXPECTED_CORPUS_SHA256, file_sha
executed = json.loads(raw.decode("utf-8"))

# --- the current corpus file: analysis fields compared ----------
current = json.load(open(f"{HERE}/corpus/corpus.json", encoding="utf-8"))


def analysis_fields(corpus):
    by_id = {r["id"]: r for r in corpus["inscriptions"]}
    ics = by_id["ICS196"]
    return {
        "eteocypriot_lines": ics["eteocypriot_lines"],
        "greek_words": ics["greek_side"]["words"],
        "ground_truth": ics["ground_truth_correspondences"],
        "androkles_sides": [by_id[k].get("eteocypriot_side")
                            for k in ("ANDROKLES-A", "ANDROKLES-B")],
        "ics217_segments": by_id["ICS217"]["greek_syllabic_excerpt"]["segments"],
    }


af_exec, af_cur = analysis_fields(executed), analysis_fields(current)
fields_identical = af_exec == af_cur

by_id = {r["id"]: r for r in executed["inscriptions"]}
ics = by_id["ICS196"]
segments = []
for line in ics["eteocypriot_lines"]:
    segments.extend([[drv.bare(t) for t in seg] for seg in line["segments"]])
gt = [(c["greek_word"], c["eteocypriot_segment_index"])
      for c in ics["ground_truth_correspondences"]]
names = [(w, drv.derive_cv(w), truth) for (w, truth) in gt]
control_segments = af_exec["ics217_segments"]


def a2(d, segs):
    scores = [drv.lccs(d, s) for s in segs]
    best = max(scores)
    return scores.index(best) + 1, best, scores


def recovered_count(pairs):
    return sum(1 for partner, truth in pairs if partner == truth)


out = {
    "run": "eteocypriot-a2-baselines-and-negative-controls",
    "date": "2026-11-22",
    "commission": "OD-10 (adjudication unit E-8), owner act 2026-11-22 12:23 ET",
    "corpus_executed_sha256": file_sha,
    "corpus_current_analysis_fields_identical_to_executed": fields_identical,
    "replicates": REPLICATES,
    "seed": SEED,
}

# --- the real pairing, frozen A2 --------------------------------
real = []
for w, d, truth in names:
    partner, best, scores = a2(d, segments)
    real.append({
        "greek_word": w, "derived": "-".join(d),
        "lccs_by_segment": scores, "A2_partner": partner,
        "A2_lccs": best, "ground_truth_segment": truth,
        "A2_recovered": partner == truth,
    })
# A1 partners are the Greek word indices (freeze section 5).
for entry, (w, d, truth) in zip(real, names):
    idx = [c["greek_word_index"] for c in ics["ground_truth_correspondences"]
           if c["greek_word"] == w][0]
    entry["A1_partner"] = idx
    entry["A1_recovered"] = idx == truth
out["real_pairing"] = {
    "names": real,
    "A2_recovered_count": sum(1 for e in real if e["A2_recovered"]),
    "A1_recovered_count": sum(1 for e in real if e["A1_recovered"]),
    "names_total": len(real),
}

# --- baselines ----------------------------------------------------
longest = max(range(len(segments)), key=lambda i: (len(segments[i]), -i)) + 1
out["baselines"] = {
    "B-LONG_longest_segment": {
        "partner_for_every_name": longest,
        "segment": "-".join(segments[longest - 1]),
        "recovered_count": sum(1 for _, _, t in names if longest == t),
    },
    "B-FIRST_segment_1": {
        "partner_for_every_name": 1,
        "recovered_count": sum(1 for _, _, t in names if 1 == t),
    },
    "B-RAND_uniform_random_partner": {
        "per_name_recovery_probability": 1 / len(segments),
        "expected_recovered_count": len(names) / len(segments),
        "prob_at_least_one_recovered": 1 - (1 - 1 / len(segments)) ** len(names),
        "prob_both_recovered": (1 / len(segments)) ** len(names),
    },
}

# --- NC-1: sign-relabel ------------------------------------------
alphabet = sorted({tok for seg in segments for tok in seg if tok != "?"})
rng = random.Random(SEED)
nc1_rec, nc1_max = [], {w: [] for w, _, _ in names}
for _ in range(REPLICATES):
    perm = alphabet[:]
    rng.shuffle(perm)
    mapping = dict(zip(alphabet, perm))
    relabelled = [[mapping.get(tok, tok) for tok in seg] for seg in segments]
    pairs = []
    for w, d, truth in names:
        partner, best, _ = a2(d, relabelled)
        pairs.append((partner, truth))
        nc1_max[w].append(best)
    nc1_rec.append(recovered_count(pairs))

# --- NC-2: name-scramble ------------------------------------------
rng = random.Random(SEED + 1)
nc2_rec, nc2_max = [], {w: [] for w, _, _ in names}
for _ in range(REPLICATES):
    pairs = []
    for w, d, truth in names:
        letters = list(w)
        rng.shuffle(letters)
        d2 = drv.derive_cv("".join(letters))
        partner, best, _ = a2(d2, segments)
        pairs.append((partner, truth))
        nc2_max[w].append(best)
    nc2_rec.append(recovered_count(pairs))


def summarize(rec, maxmap, real_rec, real_best):
    n = len(rec)
    return {
        "recovered_count_distribution": {
            str(k): rec.count(k) for k in sorted(set(rec))},
        "mean_recovered_count": sum(rec) / n,
        "fraction_recovered_ge_real": sum(1 for r in rec if r >= real_rec) / n,
        "max_lccs": {
            w: {
                "null_mean": sum(v) / len(v),
                "null_max": max(v),
                "fraction_null_ge_real": sum(1 for x in v if x >= real_best[w]) / len(v),
            } for w, v in maxmap.items()},
    }


real_rec = out["real_pairing"]["A2_recovered_count"]
real_best = {e["greek_word"]: e["A2_lccs"] for e in real}
out["NC-1_sign_relabel"] = summarize(nc1_rec, nc1_max, real_rec, real_best)
out["NC-2_name_scramble"] = summarize(nc2_rec, nc2_max, real_rec, real_best)

# --- NC-3: wrong text (ICS 217 control excerpt) -------------------
nc3 = []
for w, d, truth in names:
    partner, best, scores = a2(d, control_segments)
    nc3.append({"greek_word": w, "derived": "-".join(d),
                "lccs_by_segment": scores, "best_partner": partner,
                "best_lccs": best})
out["NC-3_wrong_text_ics217"] = {
    "segments": len(control_segments), "names": nc3,
    "note": "No ground truth exists for this pairing; the LCCS "
            "profile calibrates what the frozen score returns "
            "against real syllabic text that is not the "
            "bilingual's counterpart.",
}

print(json.dumps(out, ensure_ascii=False, indent=1))
