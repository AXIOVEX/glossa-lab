#!/usr/bin/env python3
"""Spec 109 — Stage 4 harness (T401, Part 5: Eteocypriot
reading candidates).

Implements exactly the freeze at
records/stage-4-freeze-2026-11-27.md: the comparanda
variants A1 / A2 / J derived from the ICS 196 name
anchors (comparanda (a) alone; (b) not filed complete
under Spec 101 P-3, per the freeze's determination);
the E1 derivation D(name) from the freeze's complete
tables; anchored maps and implied endings; the
lexicographic ranking (component (1) the E-4 count
mechanized, component (2) coverage; component (3)
dropped at registration); the permutation null
(B = 999, seed 109401); and the Stage 4 preflight —
clause (S) synthetic syllabary-profile corpora and
clause (N) the name-anchor control.

Discipline: fail-closed on the corpus pin; stdlib
only; deterministic; timestamped countable progress
lines on stdout; every verdict is data in the raw
output, the payload exit code is 0 on completion and
nonzero only on an integrity/assertion failure.
Custody outputs (synthetic corpora, candidate
records) are written under glossa-custody/spec109/
stage-4/ and never committed; the raw output JSON is
written to the path given as argv[2] (the filed copy
is byte-identical to the custody original).
"""
import hashlib
import json
import random
import sys
import time
import unicodedata

CORPUS_SHA256 = "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597"
DRIVER_SHA256 = "9ec475fd419150e7d07a6a36f3e306eadc62b0427cdb2a4924825870116c9c95"
FREEZE_SHA256 = "80ec9c9f5cdd0a3f362d1c2679277ec967f899d2fea541e3e5769d0c36d216dd"
NULL_SEED = 109401
NULL_B = 999
RECOVERY_FLOOR = 0.80
SYNTH_SEED_STRINGS = [f"spec109-s4-synth-{i}" for i in range(1, 6)]

# The derivation tables, as frozen (freeze section 3;
# Spec 096 freeze section 5; the E1 driver's tables).
VOWELS = {"α": "a", "ε": "e", "η": "e", "ι": "i", "ο": "o", "υ": "u", "ω": "o"}
STEMS = {
    "β": "p", "γ": "k", "δ": "t", "ζ": "s", "θ": "t", "κ": "k",
    "λ": "l", "μ": "m", "ν": "n", "π": "p", "ρ": "r", "σ": "s",
    "τ": "t", "φ": "p", "χ": "k",
}

# The 35-label synthetic syllabary inventory (harness
# constant; filed in the preflight record).
SYNTH_LABELS = [
    "a", "e", "i", "o", "u",
    "ka", "ke", "ki", "ko", "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "na", "ne", "ni", "no", "nu",
    "ra", "re", "ri", "ro", "sa", "se", "si", "so",
    "ta", "te", "ti", "to",
]
assert len(SYNTH_LABELS) == 35

SEGMENT_SKELETON = [2, 3, 5, 4, 3, 6, 9, 7, 7, 2, 5]


def log(msg):
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}",
          flush=True)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# ---------- the derivation (freeze section 3) ----------

def letters_of(word):
    decomposed = unicodedata.normalize("NFD", word)
    base = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    base = base.lower().replace("ς", "σ")
    units = []
    for ch in base:
        if ch in VOWELS:
            units.append(("v", VOWELS[ch]))
        elif ch == "ξ":
            units.append(("c", "k"))
            units.append(("c", "s"))
        elif ch in STEMS:
            units.append(("c", STEMS[ch]))
        else:
            raise ValueError(f"unhandled Greek letter {ch!r} in {word!r}")
    return units


def derive_cv(word):
    units = letters_of(word)
    out = []
    prev_vowel = "a"
    i = 0
    while i < len(units):
        kind, val = units[i]
        if kind == "v":
            out.append(val)  # R1
            prev_vowel = val
            i += 1
        else:
            nxt = units[i + 1] if i + 1 < len(units) else None
            if nxt is not None and nxt[0] == "v":
                out.append(val + nxt[1])  # R2
                prev_vowel = nxt[1]
                i += 2
            else:
                out.append(val + prev_vowel)  # R3
                i += 1
    return out


# ---------- alignment machinery (freeze sections 2-3) ----------

def lccs_align(a, b):
    """(length, i, j) of the longest common contiguous
    subsequence; smallest i, then smallest j, on ties."""
    best = 0
    bi = bj = -1
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            if k > best:
                best, bi, bj = k, i, j
    return best, bi, bj


def pairings_for(variant, d_list, segments, name_positions):
    """name index -> segment index (0-based)."""
    if variant == "A1":
        return {n: name_positions[n] for n in range(len(d_list))}
    if variant == "A2":
        out = {}
        for n, d in enumerate(d_list):
            best_seg, best_len = None, -1
            for s_idx, seg in enumerate(segments):
                L, _, _ = lccs_align(d, seg)
                if L > best_len:
                    best_len, best_seg = L, s_idx
            out[n] = best_seg
        return out
    if variant == "J":
        best = None
        n_seg = len(segments)
        for s1 in range(n_seg):
            for s2 in range(n_seg):
                if s1 == s2:
                    continue
                total = (lccs_align(d_list[0], segments[s1])[0]
                         + lccs_align(d_list[1], segments[s2])[0])
                key = (total, -s1, -s2)
                if best is None or key > best[0]:
                    best = (key, {0: s1, 1: s2})
        return best[1]
    raise ValueError(variant)


def anchored_map_and_endings(pairings, d_list, segments):
    """M_V and E_V per freeze section 3. Returns
    (M, conflicts, endings) with endings a sorted list
    of sign-sequence tuples."""
    anchored = {}
    conflicts = set()
    endings = set()
    for n, s_idx in pairings.items():
        seg = segments[s_idx]
        d = d_list[n]
        L, i, j = lccs_align(d, seg)
        for k in range(L):
            sign, val = seg[j + k], d[i + k]
            if sign in anchored and anchored[sign] != val:
                conflicts.add(sign)
            else:
                anchored[sign] = val
        if j + L < len(seg):
            endings.add(tuple(seg[j + L:]))
        else:
            endings.add((seg[-1],))
    for c in conflicts:
        anchored.pop(c, None)
    return anchored, sorted(conflicts), sorted(endings)


def key1_of(endings, heldout_forms):
    n = 0
    for form in heldout_forms:
        f = tuple(form)
        if any(len(e) <= len(f) and f[len(f) - len(e):] == tuple(e)
               for e in endings):
            n += 1
    return n


def key2_of(anchored, text_tokens):
    if not text_tokens:
        return 0.0
    return sum(1 for t in text_tokens if t in anchored) / len(text_tokens)


def run_generator(segments, d_list, name_positions, heldout_forms,
                  text_tokens):
    """The Part 5 generator: per variant, pairings, map,
    endings, keys; and the per-text ranking."""
    variants = {}
    for v in ("A1", "A2", "J"):
        p = pairings_for(v, d_list, segments, name_positions)
        m, conflicts, endings = anchored_map_and_endings(p, d_list, segments)
        variants[v] = {
            "pairings": {str(n): s + 1 for n, s in p.items()},
            "anchored_map": m,
            "conflicts_excluded": conflicts,
            "implied_endings": [list(e) for e in endings],
            "key1": key1_of(endings, heldout_forms),
            "key2": key2_of(m, text_tokens),
        }
    order = sorted(variants, key=lambda v: (-variants[v]["key1"],
                                            -variants[v]["key2"],
                                            ("A1", "A2", "J").index(v)))
    return variants, order


# ---------- clause (N): the name-anchor control ----------

def clause_n(corpus):
    ics = [x for x in corpus["inscriptions"] if x["id"] == "ICS196"][0]
    segments = []
    for line in ics["eteocypriot_lines"]:
        for s in line["segments"]:
            segments.append([t.strip("[]") for t in s])
    greek_words = []
    for line in ics["greek_side"]["lines"]:
        greek_words += line.split()
    names = [greek_words[4], greek_words[5]]
    d_list = [derive_cv(n) for n in names]
    checks = {}
    checks["D_name1"] = d_list[0] == ["a", "ri", "si", "to", "na"]
    checks["D_name2"] = d_list[1] == ["a", "ri", "si", "to", "na", "ka", "to", "so"]
    checks["LCCS_name1_seg6"] = lccs_align(d_list[0], segments[5])[0] == 4
    checks["LCCS_name2_seg6"] = lccs_align(d_list[1], segments[5])[0] == 4
    checks["LCCS_name2_seg7"] = lccs_align(d_list[1], segments[6])[0] == 2
    p_a1 = pairings_for("A1", d_list, segments, [4, 5])
    checks["A1_pairings"] = (p_a1[0] + 1, p_a1[1] + 1) == (5, 6)
    p_a2 = pairings_for("A2", d_list, segments, [4, 5])
    checks["A2_pairings"] = (p_a2[0] + 1, p_a2[1] + 1) == (6, 6)
    p_j = pairings_for("J", d_list, segments, [4, 5])
    joint = (lccs_align(d_list[0], segments[p_j[0]])[0]
             + lccs_align(d_list[1], segments[p_j[1]])[0])
    checks["J_pairings"] = (p_j[0] + 1, p_j[1] + 1) == (6, 7)
    checks["joint_optimum_6"] = joint == 6
    return {
        "checks": checks,
        "passed": all(checks.values()),
        "D": [d_list[0], d_list[1]],
        "joint_optimum": joint,
        "segments_count": len(segments),
        "token_count": sum(len(s) for s in segments),
    }


# ---------- clause (S): synthetic corpora ----------

def build_synthetic(seed_string):
    """Returns (corpus_dict, attempts). Raises on
    exhaustion of the -try suffixes."""
    attempt = 0
    while True:
        suffix = "" if attempt == 0 else f"-try{attempt}"
        seed_int = int(sha256_bytes((seed_string + suffix).encode())[:16], 16)
        rng = random.Random(seed_int)
        built = try_build(rng)
        if built is not None:
            built["seed_string"] = seed_string + suffix
            built["attempts"] = attempt + 1
            return built
        attempt += 1
        if attempt > 40:
            raise RuntimeError(f"synthetic admission exhausted for {seed_string}")


def try_build(rng):
    """Deterministic slot plan over rng-drawn labels. All
    draws are distinct labels, so cross-contamination
    between the planted structures is impossible by
    construction; the assertions verify the LCCS shape,
    the token floors, and the generator's own J pairing.
    Counts (verified in the plan): each stem_alpha sign
    carries exactly 5 tokens; d1x and d2a carry 5 each."""
    labels = SYNTH_LABELS[:]
    rng.shuffle(labels)
    it = iter(labels)
    take = lambda n: [next(it) for _ in range(n)]
    A = take(4)                       # stem_alpha A0..A3
    d1x = take(1)[0]
    d2a, d2b, d2c = take(3)
    tail_a = take(2)                  # S6 tail (planted ending)
    tail_b = take(3)                  # S7 tail (planted ending)
    tail_c = take(2)                  # third planted ending
    prefix7 = take(4)                 # S7 prefix signs
    F = take(8)                       # filler (pool) signs
    d1 = A + [d1x]
    d2 = d1 + [d2a, d2b, d2c]
    s6 = A + tail_a
    s7 = prefix7 + [d1x, d2a] + tail_b
    segs = [None] * 11
    segs[0] = [F[0], A[1]]
    segs[1] = [A[2], F[1], A[3]]
    segs[2] = [A[0], F[2], A[1], F[3], A[2]]
    segs[3] = [tail_c[0], tail_c[1], A[0], A[3]]
    segs[4] = [A[2], F[4], A[0]]
    segs[5] = s6
    segs[6] = s7
    segs[7] = [A[1], F[5], A[2], F[6], A[3], F[7], A[0]]
    segs[8] = [d1x, d2a, F[0], F[1], d1x, d2a, F[2]]
    segs[9] = [A[1], A[3]]
    segs[10] = [d1x, d2a, F[3], d1x, d2a]
    if [len(s) for s in segs] != SEGMENT_SKELETON:
        return None
    if lccs_align(d1, s6)[0] != 4 or lccs_align(d2, s6)[0] != 4:
        return None
    if lccs_align(d2, s7)[0] != 2 or lccs_align(d1, s7)[0] > 2:
        return None
    tokens = [t for s in segs for t in s]
    planted_anchored = set(A) | {d1x, d2a}
    for s in planted_anchored:
        if tokens.count(s) < 5:
            return None
    for idx, seg in enumerate(segs):
        if idx in (5, 6):
            continue
        if lccs_align(d1, seg)[0] > 2 or lccs_align(d2, seg)[0] > 2:
            return None
    p_j = pairings_for("J", [d1, d2], segs, [4, 5])
    if (p_j[0], p_j[1]) != (5, 6):
        return None
    distinct = set(tokens)
    singletons = sum(1 for s in distinct if tokens.count(s) == 1)
    # held-out forms: stream subsequences as stems + planted finals
    form_stems = [segs[0], segs[1][:2], segs[4], segs[9],
                  segs[2][:3], segs[3][:2], segs[7][:3], segs[10][:2]]
    form_finals = [tail_a, tail_a, tail_a, tail_b, tail_b,
                   tail_c, tail_c, []]
    forms = [list(st) + list(fin)
             for st, fin in zip(form_stems, form_finals)]
    return {
        "segments": segs,
        "D": [d1, d2],
        "name_positions": [4, 5],
        "heldout_forms": forms,
        "planted_anchored": sorted(planted_anchored),
        "planted_pairings": {"0": 6, "1": 7},
        "census": {
            "tokens": len(tokens),
            "distinct_marks": len(distinct),
            "singletons": singletons,
        },
    }


def recovery_of(candidate_map, planted_anchored):
    if not planted_anchored:
        return 0.0
    hit = sum(1 for s in planted_anchored if candidate_map.get(s) == s)
    return hit / len(planted_anchored)


def clause_s():
    reps = []
    for seed_string in SYNTH_SEED_STRINGS:
        built = build_synthetic(seed_string)
        segs = built["segments"]
        tokens = [t for s in segs for t in s]
        variants, order = run_generator(segs, built["D"],
                                        built["name_positions"],
                                        built["heldout_forms"], tokens)
        top = order[0]
        rec = recovery_of(variants[top]["anchored_map"],
                          built["planted_anchored"])
        # shuffle control: derange the D sequences' labels
        rng = random.Random(int(sha256_bytes(
            (seed_string + "-shuffle").encode())[:16], 16))
        perm = SYNTH_LABELS[:]
        rng.shuffle(perm)
        mapping = dict(zip(SYNTH_LABELS, perm))
        if any(mapping[s] == s for s in SYNTH_LABELS):
            mapping = dict(zip(SYNTH_LABELS, perm[1:] + perm[:1]))
        d_shuf = [[mapping[x] for x in d] for d in built["D"]]
        variants_s, order_s = run_generator(segs, d_shuf,
                                            built["name_positions"],
                                            built["heldout_forms"], tokens)
        top_s = order_s[0]
        rec_s = recovery_of(variants_s[top_s]["anchored_map"],
                            built["planted_anchored"])
        reps.append({
            "seed_string": built["seed_string"],
            "attempts": built["attempts"],
            "census": built["census"],
            "planted_anchored": built["planted_anchored"],
            "ranking": order,
            "top_variant": top,
            "recovery": rec,
            "shuffle_top_variant": top_s,
            "shuffle_recovery": rec_s,
            "variants": variants,
            "corpus": built,
        })
        log(f"clause S rep {built['seed_string']}: top={top} "
            f"recovery={rec:.3f} shuffle_recovery={rec_s:.3f} "
            f"({len(reps)}/5)")
    recs = sorted(r["recovery"] for r in reps)
    shufs = sorted(r["shuffle_recovery"] for r in reps)
    median_rec = recs[len(recs) // 2]
    median_shuf = shufs[len(shufs) // 2]
    return {
        "reps": reps,
        "median_recovery": median_rec,
        "median_shuffle_recovery": median_shuf,
        "floor": RECOVERY_FLOOR,
        "recovery_pass": median_rec >= RECOVERY_FLOOR,
        "shuffle_pass": median_shuf < 0.5 * median_rec,
    }


# ---------- the real ranking and its null ----------

def real_run(corpus, intake):
    ics = [x for x in corpus["inscriptions"] if x["id"] == "ICS196"][0]
    segments = []
    for line in ics["eteocypriot_lines"]:
        for s in line["segments"]:
            segments.append([t.strip("[]") for t in s])
    tokens = [t for s in segments for t in s]
    greek_words = []
    for line in ics["greek_side"]["lines"]:
        greek_words += line.split()
    names = [greek_words[4], greek_words[5]]
    d_list = [derive_cv(n) for n in names]
    heldout = []
    for rec in corpus["inscriptions"]:
        for f in rec.get("attested_forms_only", []):
            heldout.append(list(f["form"]))
    variants, order = run_generator(segments, d_list, [4, 5], heldout, tokens)
    # development inventory for the null (freeze section 6): the
    # filed 35-mark inventory of Spec 105's L1 derivation over
    # the same two pinned files. Spec 105's strip keeps the
    # restored sign '[sa]' as a mark in its own right (its
    # stage-1 output files the 35-mark list with '[sa]' and
    # 'sa' as separate entries, over 69 tokens); the inventory
    # is therefore built from the tokens AS RECORDED, without
    # bracket stripping. '[sa]' occurs in no anchored map and
    # no implied ending, so it only enlarges the permutation
    # domain, as filed.
    raw_tokens = []
    for line in ics["eteocypriot_lines"]:
        for s in line["segments"]:
            raw_tokens += list(s)
    andro = [x for x in intake["inscriptions"]
             if x["id"] == "ANDROKLES-A"][0]
    andro_tokens = []
    for line in andro["eteocypriot_side"]["lines"]:
        for s in line["segments"]:
            andro_tokens += list(s)
    inventory = sorted(set(raw_tokens) | set(andro_tokens))
    if len(inventory) != 35:
        raise RuntimeError(
            f"development inventory has {len(inventory)} marks, "
            "freeze fixes 35")
    return segments, tokens, d_list, heldout, variants, order, inventory


def permutation_null(variants_obs, segments, d_list, heldout, tokens,
                     inventory35):
    rng = random.Random(NULL_SEED)
    null_max = []
    top_stable = 0
    obs_top = max(v["key1"] for v in variants_obs.values())
    for b in range(NULL_B):
        perm = inventory35[:]
        rng.shuffle(perm)
        mapping = dict(zip(inventory35, perm))
        variants_p = {}
        for v, data in variants_obs.items():
            m_p = {mapping[s]: val for s, val in data["anchored_map"].items()}
            e_p = [tuple(mapping[x] for x in e)
                   for e in data["implied_endings"]]
            variants_p[v] = {"key1": key1_of(e_p, heldout),
                             "key2": key2_of(m_p, tokens)}
        null_max.append(max(x["key1"] for x in variants_p.values()))
        if b % 200 == 0:
            log(f"permutation null: {b}/{NULL_B} permutations")
    null_max_sorted = sorted(null_max)
    p99 = null_max_sorted[int(0.99 * NULL_B)]
    log(f"permutation null: {NULL_B}/{NULL_B} permutations; "
        f"p99={p99} observed_top_key1={obs_top}")
    return {
        "B": NULL_B,
        "seed": NULL_SEED,
        "null_max_key1_sorted": null_max_sorted,
        "p99": p99,
        "null_mean": sum(null_max) / len(null_max),
        "observed_top_key1": obs_top,
        "separates": obs_top > p99,
    }


INTAKE_SHA256 = "8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a"


def main():
    corpus_path, raw_out_path, custody_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    intake_path = sys.argv[4]
    raw = open(corpus_path, "rb").read()
    file_sha = sha256_bytes(raw)
    if file_sha != CORPUS_SHA256:
        print(f"REFUSED: corpus sha256 {file_sha} != freeze pin",
              file=sys.stderr)
        return 3
    intake_raw = open(intake_path, "rb").read()
    if sha256_bytes(intake_raw) != INTAKE_SHA256:
        print("REFUSED: intake sha256 != freeze pin", file=sys.stderr)
        return 3
    intake = json.loads(intake_raw.decode("utf-8"))
    corpus = json.loads(raw.decode("utf-8"))
    log("stage 4 harness: corpus and intake pins verified; "
        "starting preflight")
    out = {"corpus_sha256": file_sha, "null_seed": NULL_SEED, "null_B": NULL_B}
    # clause N
    out["clause_N"] = clause_n(corpus)
    log(f"clause N: passed={out['clause_N']['passed']} "
        f"checks={sum(out['clause_N']['checks'].values())}/"
        f"{len(out['clause_N']['checks'])}")
    # clause S
    out["clause_S"] = clause_s()
    cs = out["clause_S"]
    log(f"clause S: median_recovery={cs['median_recovery']:.3f} "
        f"recovery_pass={cs['recovery_pass']} "
        f"shuffle_pass={cs['shuffle_pass']}")
    out["preflight_passed"] = bool(out["clause_N"]["passed"]
                                  and cs["recovery_pass"]
                                  and cs["shuffle_pass"])
    log(f"preflight passed={out['preflight_passed']}")
    # custody: synthetic corpora
    import os
    os.makedirs(custody_dir, exist_ok=True)
    for rep in cs["reps"]:
        with open(os.path.join(
                custody_dir,
                f"synth-{rep['seed_string'].split('-')[-1]}.json"),
                "w") as fh:
            json.dump(rep["corpus"], fh, indent=1, sort_keys=True)
    if out["preflight_passed"]:
        segments, tokens, d_list, heldout, variants, order, inventory = \
            real_run(corpus, intake)
        out["real"] = {
            "segments": segments,
            "inventory": inventory,
            "token_count": len(tokens),
            "D": d_list,
            "heldout_forms": heldout,
            "variants": variants,
            "ranking": order,
        }
        log(f"real ranking: order={order} "
            f"key1={{ {', '.join(f'{v}: {variants[v]['key1']}' for v in order)} }}")
        null = permutation_null(variants, segments, d_list, heldout,
                                tokens, inventory)
        out["null"] = null
        top = order[0]
        tied_top = sum(1 for v in variants
                       if variants[v]["key1"] == variants[top]["key1"]
                       and variants[v]["key2"] == variants[top]["key2"]) > 1
        out["verdict"] = ("RANKED SET FILED"
                          if null["separates"] and not tied_top
                          else "RANKING NULL")
        log(f"verdict: {out['verdict']} (tied_top={tied_top})")
        # custody: candidate records with full provenance
        self_sha = sha256_bytes(open(__file__, "rb").read())
        out["harness_sha256"] = self_sha
        with open(os.path.join(custody_dir, "candidate-records.jsonl"),
                  "w") as fh:
            for rank, v in enumerate(order, 1):
                fh.write(json.dumps({
                    "text": "ICS196",
                    "rank": rank,
                    "variant": v,
                    "pairings": variants[v]["pairings"],
                    "anchored_map": variants[v]["anchored_map"],
                    "conflicts_excluded": variants[v]["conflicts_excluded"],
                    "implied_endings": variants[v]["implied_endings"],
                    "key1": variants[v]["key1"],
                    "key2": variants[v]["key2"],
                    "provenance": {
                        "generator": "stage-4-harness.py",
                        "generator_sha256": self_sha,
                        "corpus_sha256": CORPUS_SHA256,
                        "driver_sha256": DRIVER_SHA256,
                        "freeze_sha256": FREEZE_SHA256,
                        "null_seed": NULL_SEED,
                        "constraint_set_version":
                            "stage-4-freeze-2026-11-27 (comparanda (a) "
                            "alone; variants A1/A2/J)",
                    },
                }, sort_keys=True) + "\n")
    with open(raw_out_path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    log(f"raw output written: {raw_out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
