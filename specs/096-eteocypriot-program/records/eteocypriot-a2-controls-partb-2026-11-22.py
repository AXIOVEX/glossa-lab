#!/usr/bin/env python3
"""Spec 096 / OD-10 — A2 baselines and negative controls, part (b).

The part (a) comparisons (records/eteocypriot-a2-controls-
2026-11-22.py) rerun against the intake-enlarged corpus state
produced by the OD-10 Androkles intake
(corpus/corpus-androkles-intake-2026-11-22.json): the frozen
A2 method of the E1 driver (derive_cv and lccs, imported
unmodified) over a segment pool of ICS 196's eleven segments
(indices 1-11, unchanged, so the ground-truth indices 6 and 7
keep their meaning) followed by ANDROKLES-A's three segments
in the edition's order (indices 12-14).

Guards, all fail-closed:
- the executed corpus bytes are recovered from git history
  and verified against the freeze pin, as in part (a);
- corpus.json (version 1.1.1) must still hash to its intake
  pin — the intake created a new state and touched nothing;
- the intake state's ICS 196 analysis-bearing fields must be
  identical to the executed bytes', and its ANDROKLES-A side
  must carry the 15-sign, 3-segment reading of the intake
  record.

Baselines and controls are constructed exactly as in part
(a): B-LONG, B-FIRST, B-RAND (analytic, at the enlarged pool
size); NC-1 sign-relabel (alphabet of the enlarged pool),
NC-2 name-scramble, NC-3 wrong text (ICS 217). 999 replicates
per control, same seeds as part (a) (20261122 / 20261123).
Exploratory only: no claim is scored, no verdict is changed.
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

# --- corpus.json must be untouched -------------------------------
cur_raw = open(f"{HERE}/corpus/corpus.json", "rb").read()
cur_sha = hashlib.sha256(cur_raw).hexdigest()
assert cur_sha == "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597", cur_sha
current = json.loads(cur_raw.decode("utf-8"))

# --- the intake-enlarged state ------------------------------------
state_path = f"{HERE}/corpus/corpus-androkles-intake-2026-11-22.json"
state_raw = open(state_path, "rb").read()
state_sha = hashlib.sha256(state_raw).hexdigest()
state = json.loads(state_raw.decode("utf-8"))
assert state["version"] == "1.2.0", state["version"]


def analysis_fields(corpus):
    by_id = {r["id"]: r for r in corpus["inscriptions"]}
    ics = by_id["ICS196"]
    return {
        "eteocypriot_lines": ics["eteocypriot_lines"],
        "greek_words": ics["greek_side"]["words"],
        "ground_truth": ics["ground_truth_correspondences"],
        "ics217_segments": by_id["ICS217"]["greek_syllabic_excerpt"]["segments"],
    }


af_exec = analysis_fields(executed)
af_state = analysis_fields(state)
fields_identical = af_exec == af_state
assert fields_identical, "intake state altered ICS 196 analysis fields"

by_id = {r["id"]: r for r in state["inscriptions"]}
ics = by_id["ICS196"]
segments = []
for line in ics["eteocypriot_lines"]:
    segments.extend([[drv.bare(t) for t in seg] for seg in line["segments"]])
n_ics = len(segments)

a_side = by_id["ANDROKLES-A"]["eteocypriot_side"]
assert a_side is not None and a_side["sign_count"] == 15
a_segments = []
for line in a_side["lines"]:
    a_segments.extend([[drv.bare(t) for t in seg] for seg in line["segments"]])
assert len(a_segments) == 3 and sum(len(s) for s in a_segments) == 15
segments = segments + a_segments

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
    "run": "eteocypriot-a2-baselines-and-negative-controls-part-b",
    "date": "2026-11-22",
    "commission": "OD-10 (adjudication unit E-8), owner act 2026-11-22 12:23 ET",
    "corpus_executed_sha256": file_sha,
    "corpus_current_sha256": cur_sha,
    "corpus_state": "corpus/corpus-androkles-intake-2026-11-22.json",
    "corpus_state_sha256": state_sha,
    "corpus_state_ics196_analysis_fields_identical_to_executed": fields_identical,
    "pool": {
        "segments_total": len(segments),
        "ics196_segments": n_ics,
        "androkles_a_segments": ["-".join(s) for s in a_segments],
        "androkles_a_segment_indices": [n_ics + 1, n_ics + 2, n_ics + 3],
    },
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
