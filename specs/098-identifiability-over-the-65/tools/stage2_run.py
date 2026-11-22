"""Spec 098 Stage 2 runner: rival construction (T201), the
TC-098-01 guard over the actual development export, prediction
sheet rendering (T202), and the Stage 2 outcome record.

Run on tower-compute from a fresh clone, under the Stage 2
freeze (records/stage-2-freeze-2026-11-22.md). Modes:

  rivals   — verify the corpus pin, reproduce the Stage 1
             power grid for the executed population of 69,
             recompute the frozen split and verify the seal
             hash against the committed seal record WITHOUT
             reading the custody file, build the development
             export, run the TC-098-01 guard over it, construct
             R-A..R-E and the Arm E additions for all 69 signs,
             and write records/stage-2-rivals-2026-11-22.json
             plus the rendered rival-construction record.
  sheets   — read the authored sheet determinations
             (records/stage-2-sheet-determinations-2026-11-22.json)
             and the rivals data; render
             records/stage-2-prediction-sheets-2026-11-22.md.
  outcome  — combine rivals + determinations; apply the frozen
             precedence as far as Stage 2 can state it; write
             records/stage-2-outcome-2026-11-22.json and render
             records/stage-2-outcome-2026-11-22.md.

No mode reads the custody file, states an actual held-out
count, or scores anything. Margins and null percentiles are
Stage 3 quantities and are recorded as not computed.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC_DIR = HERE.parent
REPO = SPEC_DIR.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "backend"))

from seal_and_score import (  # noqa: E402
    SealViolation,
    development_export,
    seal_hash,
    split_clusters,
)
from stage1_run import clusters, load_records, sign_tokens  # noqa: E402

ANNEX = SPEC_DIR / "records/population-annex-2026-11-21.md"
GRID = SPEC_DIR / "records/stage1-grid-2026-11-21.json"
RIVALS_OUT = SPEC_DIR / "records/stage-2-rivals-2026-11-22.json"
RIVALS_MD = SPEC_DIR / "records/stage-2-rival-construction-2026-11-22.md"
DET_IN = SPEC_DIR / "records/stage-2-sheet-determinations-2026-11-22.json"
SHEETS_MD = SPEC_DIR / "records/stage-2-prediction-sheets-2026-11-22.md"
OUTCOME_OUT = SPEC_DIR / "records/stage-2-outcome-2026-11-22.json"
OUTCOME_MD = SPEC_DIR / "records/stage-2-outcome-2026-11-22.md"

SEAL_SHA256 = "1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9"
SEAL_HELD_COUNT = 517
SEAL_CLUSTERS = 2413

# Arm E of the annex as amended: M202 left the population at
# Stage 1 (WS2 strike), M044 by the Round 2 adjudication.
ARM_E_EXECUTED = ["M047", "M124", "M329", "M330"]
ARM_E_DROPPED = {"M202": "WS2 relabel execution 2026-11-21 (class E to U)",
                 "M044": "M044 addendum adjudication 2026-11-21 (class E to U)"}

# Gloss alternations on the candidate's own record (Stage 2
# freeze section 4), with their sources.
GLOSS_ALTERNATION = {
    "M047": "DEDR 4897 fish/star (T303 application record)",
    "M329": "gloss 'gold, precious; personal name' (T303 application record)",
}

# Referent glosses for the logogram rival where the record
# carries one outside the VOCABULARY (Arm E, T303 record).
RECORD_GLOSSES = {
    "M047": "fish",
    "M124": "pot / jar",
    "M329": "gold",
}

# Arm E additions (Stage 2 freeze section 5), from the T303
# application record: comparandum-as-value and cross-sign
# rivals. Each entry: (label, value, source).
ARM_E_ADDITIONS = {
    "M047": [
        ("R-X1 comparandum-as-value (Elamite)", "in", "MC-01, T303 record"),
        ("R-X2 comparandum-as-value (Sanskrit)", "mina", "SL-06, T303 record"),
    ],
    "M124": [
        ("R-X1 comparandum-as-value (Elamite; M044's comparanda package, "
         "the cross-sign arm named for this sign; Sanskrit comparandum "
         "'kona', SL-04, recorded with it)", "kun", "MC-18, T303 record"),
    ],
    "M329": [
        ("R-X1 comparandum-as-value (Elamite; Sanskrit comparandum "
         "'pura', SL-14, recorded with it)", "pur", "MC-21, T303 record"),
    ],
    "M330": [
        ("R-X1 cross-sign rival: M202's evidence package (Elamite 'an', "
         "MC-07; Sanskrit 'annam/anna', SL-03)", "can", "T303 record"),
        ("R-X2 comparandum-as-value (Elamite)", "an", "MC-07, T303 record"),
        ("R-X3 comparandum-as-value (Sanskrit)", "anna", "SL-03, T303 record"),
    ],
}


# ---------------------------------------------------------------- annex

def parse_annex():
    """Population annex rows: (sign, value as recorded, dedr as
    recorded), in annex order, per arm."""
    text = ANNEX.read_text(encoding="utf-8")
    arms = {"I": [], "E": []}
    arm = None
    for line in text.splitlines():
        if line.startswith("## Arm I"):
            arm = "I"
            continue
        if line.startswith("## Arm E"):
            arm = "E"
            continue
        if line.startswith("Count check"):
            arm = None
        if arm:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) > 3 and re.fullmatch(r"M\d{3}", parts[1]):
                arms[arm].append({"sign": parts[1], "value": parts[2],
                                  "dedr": parts[3], "arm": arm})
    assert len(arms["I"]) == 65, len(arms["I"])
    assert len(arms["E"]) == 6, len(arms["E"])
    return arms


def executed_population():
    arms = parse_annex()
    pop = list(arms["I"])
    by_sign = {r["sign"]: r for r in arms["E"]}
    for s in ARM_E_EXECUTED:
        pop.append(by_sign[s])
    assert len(pop) == 69, len(pop)
    return pop


# ---------------------------------------------------------------- shape

_FOLD = {"L": "ḷ", "T": "ṭ", "D": "ḍ", "N": "ṇ", "R": "ṟ", "3": "ṉ"}
_VOWELS = "aeiou"
_NASALS = set("nm")
_STOPS = set("kgcjtdpb")
_LIQUIDS = set("lr")


def normalize(value: str) -> str:
    """Normalization for shape computation only (Stage 2 freeze
    section 5). Values of record are never respelled."""
    v = value.strip()
    for k, x in _FOLD.items():
        v = v.replace(k, x)
    v = unicodedata.normalize("NFD", v.lower())
    v = "".join(c for c in v if unicodedata.category(c) != "Mn")
    v = re.sub(r"[^a-z]", "", v)
    v = re.sub(r"([aeiou])\1", r"\1", v)  # collapse long-vowel doubling
    return v


def alternants(value: str):
    return [a.strip() for a in value.split("/")]


def _nuclei(v: str):
    """Vowel nuclei spans; 'ai' and 'au' count as one nucleus."""
    spans = []
    i = 0
    while i < len(v):
        if v[i] in _VOWELS:
            if v[i] == "a" and i + 1 < len(v) and v[i + 1] in "iu":
                spans.append((i, i + 2))
                i += 2
            else:
                spans.append((i, i + 1))
                i += 1
        else:
            i += 1
    return spans


def _coda_class(coda: str) -> str:
    if not coda:
        return "open"
    last = coda[-1]
    if last in _NASALS:
        return "nasal"
    if last in _STOPS:
        return "stop"
    if last in _LIQUIDS:
        return "liquid"
    return "other"


def shape(value: str):
    """(syllable count, per-syllable coda classes) of the
    normalized value, syllabified by vowel nuclei with a
    maximal single-consonant onset (Stage 2 freeze section 5)."""
    v = normalize(value)
    spans = _nuclei(v)
    classes = []
    for idx, (a, b) in enumerate(spans):
        if idx + 1 < len(spans):
            between = v[b:spans[idx + 1][0]]
            coda = between[:-1] if between else ""
        else:
            coda = v[b:]
        classes.append(_coda_class(coda))
    return (len(spans), tuple(classes))


# ---------------------------------------------------------------- choices

def free_choices(pop):
    """Free-choice accounting of Stage 2 freeze section 4."""
    by_value = Counter(r["value"] for r in pop)
    out = {}
    for r in pop:
        variant = 1 if "/" in r["value"] else 0
        homophony = 1 if by_value[r["value"]] >= 2 else 0
        gloss = 1 if r["sign"] in GLOSS_ALTERNATION else 0
        out[r["sign"]] = {
            "variant_alternation": variant,
            "homophony_allowance": homophony,
            "gloss_alternation": gloss,
            "total": variant + homophony + gloss,
        }
    return out


# ---------------------------------------------------------------- rivals

def build_pools(pop):
    from glossa_lab.data.dravidian import VOCABULARY as DRAV
    from glossa_lab.data.sanskrit import VOCABULARY as SANS
    annex_pool = []
    for r in pop:
        for alt in alternants(r["value"]):
            annex_pool.append({"value": alt, "source": f"annex value of {r['sign']}"})
    return annex_pool, list(DRAV.keys()), list(SANS.keys())


def draw_rival(candidate_row, pool, pool_name):
    """First pool value (in pool order) with the candidate's
    shape, not equal to any candidate alternant."""
    target = shape(alternants(candidate_row["value"])[0])
    cand_norms = {normalize(a) for a in alternants(candidate_row["value"])}
    tried = 0
    for entry in pool:
        val = entry["value"] if isinstance(entry, dict) else entry[0]
        tried += 1
        if normalize(val) in cand_norms:
            continue
        if shape(val) == target:
            src = entry["source"] if isinstance(entry, dict) else f"{pool_name} VOCABULARY"
            return {"value": val, "source": src, "pool_size": len(pool),
                    "pool_position": tried}
    return None


def construct_rivals(pop):
    annex_pool, drav_pool, sans_pool = build_pools(pop)
    from glossa_lab.data.dravidian import VOCABULARY as DRAV
    rivals = {}
    for r in pop:
        s = r["sign"]
        ra = draw_rival(r, annex_pool + [{"value": k, "source": "dravidian.py VOCABULARY"}
                                         for k in drav_pool], "annex+dravidian")
        rb = draw_rival(r, [{"value": k, "source": "sanskrit.py VOCABULARY"}
                            for k in sans_pool], "sanskrit")
        gloss = DRAV.get(normalize(alternants(r["value"])[0])) or RECORD_GLOSSES.get(s)
        rc = {"construction": "logogram: the sign carries the candidate "
                              "value's referent as a logogram, no phonetic value",
              "referent_gloss": gloss,
              "referent_gloss_source": ("dravidian.py VOCABULARY" if
                                        DRAV.get(normalize(alternants(r["value"])[0]))
                                        else ("T303 application record" if gloss else None))}
        rivals[s] = {
            "R-A": ({"family": "R-A matched wrong Dravidian value (C2/C5)",
                     "value": ra["value"], "source": ra["source"],
                     "free_choices": 0} if ra else
                    {"family": "R-A matched wrong Dravidian value (C2/C5)",
                     "value": None, "not_constructible": True,
                     "reason": "no same-shape Dravidian value in the frozen "
                               "search space (annex values + dravidian.py "
                               "VOCABULARY)", "free_choices": 0}),
            "R-B": ({"family": "R-B unrelated-family value (C5), Sanskrit",
                     "value": rb["value"], "source": rb["source"],
                     "free_choices": 0} if rb else
                    {"family": "R-B unrelated-family value (C5), Sanskrit",
                     "value": None, "not_constructible": True,
                     "reason": "no same-shape Sanskrit value in the frozen "
                               "search space (sanskrit.py VOCABULARY)",
                     "free_choices": 0}),
            "R-C": {"family": "R-C logogram rival (C1/C3)", **rc, "free_choices": 0},
            "R-D": {"family": "R-D structural-only model (C6-adjacent baseline)",
                    "construction": "no value assignment; the language-neutral "
                                    "order-1 neighbour-pair model over the "
                                    "sign's development contexts, unconditioned "
                                    "(the annex estimator with the unconditioned "
                                    "assignment)", "free_choices": 0},
            "R-E": "model-level: see the global permutation in this record",
        }
        for label, val, src in ARM_E_ADDITIONS.get(s, []):
            rivals[s][label.split(" ")[0] + " " + label.split(" ")[1]] = {
                "family": label, "value": val, "source": src, "free_choices": 0}
    # R-E: rotate recorded values within each shape class (annex order).
    classes = {}
    for r in pop:
        classes.setdefault(shape(alternants(r["value"])[0]), []).append(r)
    permutation = {}
    for shp, rows in classes.items():
        if len(rows) < 2:
            for r in rows:
                permutation[r["sign"]] = {"receives_value": r["value"],
                                          "from_sign": r["sign"], "fixed_point": True}
        else:
            for i, r in enumerate(rows):
                src = rows[i - 1]
                permutation[r["sign"]] = {"receives_value": src["value"],
                                          "from_sign": src["sign"], "fixed_point": False}
    return rivals, permutation


# ---------------------------------------------------------------- corpus

def corpus_checks(records):
    seq = [r for r in records
           if any(t is not None for t in (r.get("canonical_grapheme_ids") or []))]
    fields = Counter()
    all_keys = set()
    for r in seq:
        all_keys.update(r.keys())
        for k, v in r.items():
            if v not in (None, "", [], {}):
                fields[k] += 1
    motif_like = [k for k in all_keys if "motif" in k or "iconograph" in k]
    return {"sequence_bearing": len(seq), "fields": dict(sorted(fields.items())),
            "motif_or_iconography_fields": motif_like}


def grid_and_guard(records, pop):
    cl = clusters(records)
    ids = sorted(cl)
    dev_ids, held_ids = split_clusters(ids)
    seal_ok = seal_hash(held_ids) == SEAL_SHA256 and len(held_ids) == SEAL_HELD_COUNT \
        and len(ids) == SEAL_CLUSTERS
    devset = set(dev_ids)
    rows = [{"cluster_id": cid, "glossa_id": cl[cid]["glossa_id"]} for cid in dev_ids]
    guard_rows = development_export(rows, held_ids)  # raises SealViolation on leak
    dev_tokens = Counter()
    for cid, r in cl.items():
        if cid in devset:
            dev_tokens.update(sign_tokens(r))
    grid = {g["sign"]: g for g in json.loads(GRID.read_text(encoding="utf-8"))["grid"]}
    per_sign = {}
    grid_match = True
    for r in pop:
        s = r["sign"]
        d = dev_tokens.get(s, 0)
        g = grid.get(s)
        if g is None or g["dev_tokens"] != d:
            grid_match = False
        exp = d / 4.0
        per_sign[s] = {
            "dev_tokens": d,
            "expected_heldout_tokens": round(exp, 2),
            "meets_floor_in_expectation": exp >= 5,
            "grid_row_reproduced": bool(g and g["dev_tokens"] == d),
        }
    return {"clusters": len(ids), "dev_clusters": len(dev_ids),
            "held_clusters_recomputed": len(held_ids), "seal_recomputed_ok": seal_ok,
            "guard_rows_passed": len(guard_rows), "grid_reproduced": grid_match,
            "per_sign": per_sign}


# ---------------------------------------------------------------- modes

def mode_rivals():
    records = load_records()
    pop = executed_population()
    checks = corpus_checks(records)
    assert checks["motif_or_iconography_fields"] == [], checks
    gg = grid_and_guard(records, pop)
    assert gg["seal_recomputed_ok"], gg
    assert gg["grid_reproduced"], gg
    choices = free_choices(pop)
    rivals, permutation = construct_rivals(pop)
    data = {
        "stage": "Spec 098 Stage 2, T201 (rival construction)",
        "population": {"count": len(pop),
                       "arm_I": [r["sign"] for r in pop if r["arm"] == "I"],
                       "arm_E": [r["sign"] for r in pop if r["arm"] == "E"],
                       "dropped_from_annex_arm_E": ARM_E_DROPPED},
        "corpus_field_census": checks,
        "split_and_guard": {k: v for k, v in gg.items() if k != "per_sign"},
        "per_sign_counts": gg["per_sign"],
        "free_choices": choices,
        "shapes": {r["sign"]: {"value_as_recorded": r["value"],
                               "normalized_first_alternant": normalize(alternants(r["value"])[0]),
                               "shape": shape(alternants(r["value"])[0])}
                   for r in pop},
        "rivals": rivals,
        "global_permutation_R-E": permutation,
    }
    RIVALS_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                          encoding="utf-8")
    lines = RIVALS_PROSE.splitlines()
    lines.append("| Sign | Candidate | R-A (Dravidian) | R-B (Sanskrit) | R-C referent | Extra Arm E rivals |")
    lines.append("|---|---|---|---|---|---|")
    for r in pop:
        s = r["sign"]
        rv = rivals[s]
        ra = rv["R-A"].get("value") or "NOT CONSTRUCTIBLE"
        rb = rv["R-B"].get("value") or "NOT CONSTRUCTIBLE"
        rc = rv["R-C"].get("referent_gloss") or "(function only)"
        extra = "; ".join(f"{k}: {v.get('value')}" for k, v in rv.items()
                          if k.startswith("R-X")) or "—"
        lines.append(f"| {s} | {r['value']} | {ra} | {rb} | {rc} | {extra} |")
    lines.append("")
    lines.append("R-D for every sign: the structural-only model (no value "
                 "assignment; unconditioned order-1 neighbour-pair model). "
                 "R-E: the global permutation filed in the data "
                 "(`global_permutation_R-E` in "
                 "`records/stage-2-rivals-2026-11-22.json`); signs in "
                 "singleton shape classes are fixed points.")
    RIVALS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_ra = sum(1 for s in rivals if rivals[s]["R-A"].get("value"))
    n_rb = sum(1 for s in rivals if rivals[s]["R-B"].get("value"))
    print(f"clusters={gg['clusters']} dev={gg['dev_clusters']} "
          f"held_recomputed={gg['held_clusters_recomputed']} seal_ok={gg['seal_recomputed_ok']}")
    print(f"guard: development export rows passed={gg['guard_rows_passed']} "
          f"(no SealViolation); grid reproduced for 69 signs={gg['grid_reproduced']}")
    print(f"R-A constructed {n_ra}/69; R-B constructed {n_rb}/69; "
          f"R-C, R-D constructed 69/69; R-E permutation over "
          f"{sum(1 for v in permutation.values() if not v['fixed_point'])} moved signs")
    print(f"PAYLOAD VERDICT T201: rivals_written={RIVALS_OUT.name} "
          f"population=69 seal_verify=True guard_pass=True grid_reproduced=True")
    return 0


def load_stage2():
    rivals = json.loads(RIVALS_OUT.read_text(encoding="utf-8"))
    det = json.loads(DET_IN.read_text(encoding="utf-8"))
    return rivals, det


def mode_sheets():
    rivals, det = load_stage2()
    pop = executed_population()
    lines = SHEETS_PROSE.splitlines()
    for r in pop:
        s = r["sign"]
        d = det[s]
        lines.append(f"## {s} — candidate value as recorded: {r['value']}")
        lines.append("")
        lines.append(f"Sheet determination: **{d['sheet']}**"
                     + (f" (reason class {d['reason_class']})" if d.get("reason_class") else ""))
        lines.append("")
        lines.append(d["text"])
        lines.append("")
    SHEETS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_acc = sum(1 for s in det if det[s]["sheet"] == "ACCEPTED")
    print(f"sheets: ACCEPTED {n_acc}; not constructible "
          f"{sum(1 for s in det if det[s]['sheet'] == 'NOT_CONSTRUCTIBLE')}; "
          f"not constructed {sum(1 for s in det if det[s]['sheet'] == 'NOT_CONSTRUCTED')}")
    print(f"PAYLOAD VERDICT T202: sheets_written={SHEETS_MD.name} accepted={n_acc}")
    return 0


def mode_outcome():
    rivals, det = load_stage2()
    pop = executed_population()
    counts = rivals["per_sign_counts"]
    choices = rivals["free_choices"]
    outcomes = {}
    for r in pop:
        s = r["sign"]
        c = counts[s]
        ch = choices[s]
        threshold = 10.0 + 2.0 * ch["total"]
        exp = c["expected_heldout_tokens"]
        if s == "M374":
            outcome, basis = "UNDECIDABLE AT THIS POWER", \
                "frozen default (T102): unattested, unscored"
        elif not c["meets_floor_in_expectation"]:
            outcome, basis = "UNDECIDABLE AT THIS POWER", \
                "decision rule 1, grid arm, in expectation (Stage 1 grid); " \
                "the binding count test on actual held-out counts runs at Stage 3"
        elif det[s]["sheet"] != "ACCEPTED":
            outcome, basis = "NOT IDENTIFIABLE", \
                "by construction: no accepted prediction sheet (spec 3.5, " \
                "claim C098-4); final unless the Stage 3 count test fires rule 1"
        else:
            outcome, basis = "PROCEEDS TO STAGE 3", \
                "accepted prediction sheet and eligible in expectation; the " \
                "frozen-vocabulary outcome is determined at Stage 3 scoring"
        outcomes[s] = {
            "sign": s, "arm": r["arm"], "candidate_value": r["value"],
            "dedr_as_recorded": r["dedr"],
            "free_choices": ch,
            "threshold_nats_vs_zero_choice_rival": threshold,
            "dev_tokens": c["dev_tokens"],
            "expected_heldout_tokens": exp,
            "min_detectable_margin_nats_per_token_at_expected_count":
                (round(threshold / exp, 3) if exp > 0 else None),
            "eligibility": ("FROZEN DEFAULT" if s == "M374" else
                            ("ELIGIBLE IN EXPECTATION" if c["meets_floor_in_expectation"]
                             else "BELOW FLOOR IN EXPECTATION")),
            "rivals": {k: (v.get("value") if isinstance(v, dict) else v)
                       for k, v in rivals["rivals"][s].items()},
            "sheet": det[s]["sheet"],
            "stage2_outcome": outcome,
            "outcome_basis": basis,
            "margin_nats": None,
            "margin_note": "not computed — Stage 3 quantity (seal unreleased)",
            "null_p99": None,
            "null_note": "not computed — Stage 3 quantity (seal unreleased)",
        }
    dist = Counter(o["stage2_outcome"] for o in outcomes.values())
    data = {"stage": "Spec 098 Stage 2 outcome (T201 + T202)",
            "population_count": len(pop),
            "distribution": dict(dist), "outcomes": outcomes}
    OUTCOME_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    lines = OUTCOME_PROSE.splitlines()
    lines.append("| Sign | Arm | Value | Free choices | Threshold (nats) | Dev tokens | Expected held-out | MDM (nats/token) | Eligibility | Sheet | Stage 2 outcome |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in pop:
        o = outcomes[r["sign"]]
        lines.append("| {sign} | {arm} | {v} | {fc} | {th} | {dt} | {exp} | {mdm} | {el} | {sh} | {oc} |".format(
            sign=o["sign"], arm=o["arm"], v=o["candidate_value"], fc=o["free_choices"]["total"],
            th=o["threshold_nats_vs_zero_choice_rival"], dt=o["dev_tokens"],
            exp=o["expected_heldout_tokens"],
            mdm=o["min_detectable_margin_nats_per_token_at_expected_count"],
            el=o["eligibility"], sh=o["sheet"], oc=o["stage2_outcome"]))
    lines.append("")
    lines.append("Family counts (multiplicity family = the 69 signs): "
                 + "; ".join(f"{k}: {v}" for k, v in sorted(dist.items())) + ".")
    OUTCOME_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"distribution: {dict(dist)}")
    print(f"PAYLOAD VERDICT STAGE2-OUTCOME: outcomes_written={OUTCOME_OUT.name} "
          f"population=69 undecidable={dist.get('UNDECIDABLE AT THIS POWER', 0)} "
          f"not_identifiable={dist.get('NOT IDENTIFIABLE', 0)} "
          f"proceeds={dist.get('PROCEEDS TO STAGE 3', 0)}")
    return 0


RIVALS_PROSE = """# Spec 098 — Stage 2, T201: rival construction record

**Date:** 2026-11-22 · **Task:** T201 (acceptance: record +
test) · **Claim:** C098-3 · **Venue:** tower-compute, fresh
clone · **Freeze:** `records/stage-2-freeze-2026-11-22.md`
§5 · **Runner:** `tools/stage2_run.py` (rivals mode) ·
**Data:** `records/stage-2-rivals-2026-11-22.json`.

Construction followed the Stage 2 freeze exactly: one
deterministic construction per competitor, over development
data only, from the frozen search space; frequency and
position matching by construction (WP8 family C2's terms —
a wrong mapping for the same sign inherits that sign's
frequency and positional profile exactly). Munda is not
carried by any lexicon of record in the repository, so R-B
is drawn from Sanskrit for every sign (freeze §5).

The task's test leg (the TC-098-01 guard over the actual
development export) ran in the same payload: the frozen
split was recomputed over the corpus of record (2,413
clusters; 517 held out), the recomputed held-out set's seal
hash verified against the committed seal
(1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9,
verify True) without reading the custody file, and
`development_export` passed all 1,896 development rows with
no SealViolation. The Stage 1 power grid was reproduced
exactly for the 69 signs (development token counts equal on
every row). No held-out sequence, token, or per-sign
held-out count was examined or stated; the seal was not
opened or released.

Payload verdict (the runner's own record): PAYLOAD VERDICT
T201: rivals_written=stage-2-rivals-2026-11-22.json
population=69 seal_verify=True guard_pass=True
grid_reproduced=True (runner exit 0).

Per-sign rivals (R-A and R-B values as drawn; full sources,
shapes, and pool data in the JSON):
"""

SHEETS_PROSE = """# Spec 098 — Stage 2, T202: prediction sheets

**Date:** 2026-11-22 · **Task:** T202 (acceptance: record) ·
**Claim:** C098-4 · **Venue:** tower-compute, fresh clone ·
**Freeze:** `records/stage-2-freeze-2026-11-22.md` §6 ·
**Runner:** `tools/stage2_run.py` (sheets mode), rendering the
authored determinations of
`records/stage-2-sheet-determinations-2026-11-22.json`.

One section per sign of the executed population of 69, in
annex order. A sheet is ACCEPTED only where the frozen record
states, for the candidate, a neighbour-identity or
neighbour-class prediction (a filed collocation with a named
sign, a filed slot pattern with named flanking signs, or a
filed sign sequence) that the rivals as constructed do not
state. A sheet resting on a motif association alone is not
accepted: the corpus of record carries no motif field on any
sequence-bearing record (field census in the T201 record) and
the frozen estimator scores neighbour-pair contexts only.
A sheet whose only differing observable is position or
frequency is rejected under spec §3.5. Where no sheet can be
constructed, the gap is named per sign; the sign is recorded
NOT IDENTIFIABLE by construction (subject to the precedence
of decision rule 1, applied in the outcome record).

On an accepted sheet, the candidate's signature is the
neighbour set its record states; every rival takes the
unconditioned assignment (all of the sign's development
occurrences), no rival's record stating a signature. The
assignment rule and its fairness basis are the Stage 2
freeze's §6.
"""

OUTCOME_PROSE = """# Spec 098 — Stage 2 Outcome Record (T201 + T202)

**Date:** 2026-11-22 · **Tasks:** T201, T202 · **Claims:**
C098-3, C098-4 · **Venue:** tower-compute, fresh clone ·
**Freeze:** `records/stage-2-freeze-2026-11-22.md` ·
**Runner:** `tools/stage2_run.py` · **Data:**
`records/stage-2-rivals-2026-11-22.json`,
`records/stage-2-outcome-2026-11-22.json`.

## Population, as executed

69 signs — Arm I, the 65 of the population annex; Arm E,
four (M047, M124, M329, M330) — confirmed from the current
standings record (4 E + 65 I + 4 R + 3 P + 18 U = 94) at
execution commit 6bcd95eb. The F-9 act had not landed at
that commit and no F-9 pull request was open; M047 is a
member as class E on its entry as filed (Stage 2 freeze §0).

## What Stage 2 determined

Under the frozen precedence (spec §4) as far as Stage 2 can
state it: 48 signs stand at UNDECIDABLE AT THIS POWER (one
by the T102 frozen default, M374; 47 on decision rule 1's
grid arm, in expectation — their binding count test on
actual held-out counts runs at Stage 3); 17 signs are NOT
IDENTIFIABLE by construction (eligible in expectation, no
accepted prediction sheet — spec §3.5); 4 signs proceed to
Stage 3 with accepted prediction sheets (M089, M267, M347,
M375). No sign is DISCRIMINATED ON PSEUDO-HELD-OUT: that
outcome, and every per-sign margin and permutation-null
percentile, is a Stage 3 quantity computed from held-out
log-likelihoods under the single recorded release of the
seal, and is recorded here as not computed — Stage 3 (the
Stage 2 freeze's §7 states this in advance). The seal was
not opened, read, or released in Stage 2; the custody file
was not read by any Stage 2 process.

## Per-sign record

Margins and null percentiles are "not computed — Stage 3"
for every sign and are carried in the data file
(`records/stage-2-outcome-2026-11-22.json`) on every row.
Threshold is the penalized-margin threshold in nats against
a zero-free-choice rival (10 + 2 × free choices); MDM is
that threshold divided by the expected held-out count, in
nats per token (the Stage 1 grid's measure, at the
candidate's own threshold).
"""


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "rivals"
    if mode == "rivals":
        raise SystemExit(mode_rivals())
    if mode == "sheets":
        raise SystemExit(mode_sheets())
    if mode == "outcome":
        raise SystemExit(mode_outcome())
    print(f"unknown mode {mode}", file=sys.stderr)
    raise SystemExit(2)
