#!/usr/bin/env python3
"""Spec 109 Stage 4 — independent verification.

TC-109-07 (Part 5 ranking conformance) and TC-109-03
(replay conformance), implemented independently of
records/stage-4-harness.py: the derivation tables
are re-entered from the freeze, the alignment is
computed by substring enumeration (the harness uses
a dynamic program), and every filed figure is
recomputed from the pinned sources and the custody
records, never read from the harness's code.

Usage: stage-4-verify.py <spec109_dir> <custody_dir>
Exit 0 iff every check passes. Prints one line per
check with a running count (timestamped progress).
"""
import hashlib
import json
import os
import random
import sys
import time

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] "
          f"check {len(CHECKS)}: {name} -> "
          f"{'PASS' if ok else 'FAIL'} {detail}", flush=True)
    return ok


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ---------- independent derivation (freeze tables) ----------

VOWEL = {"α": "a", "ε": "e", "η": "e", "ι": "i",
         "ο": "o", "υ": "u", "ω": "o"}
CONS = {"β": "p", "γ": "k", "δ": "t", "ζ": "s",
        "θ": "t", "κ": "k", "λ": "l", "μ": "m",
        "ν": "n", "π": "p", "ρ": "r", "σ": "s",
        "τ": "t", "φ": "p", "χ": "k"}


def derive(word):
    # Normalization per the freeze's derivation tables:
    # NFD decomposition, diacritics stripped, lowercased,
    # final sigma folded; xi expands to the two stems
    # k and s; then R1 (vowel sign), R2 (consonant
    # paired with a following vowel), R3 (dead vowel
    # copies the preceding vowel, default a).
    import unicodedata
    decomposed = unicodedata.normalize("NFD", word)
    base = "".join(c for c in decomposed
                   if not unicodedata.combining(c))
    base = base.lower().replace("ς", "σ")
    units = []
    for c in base:
        if c in VOWEL:
            units.append(("v", VOWEL[c]))
        elif c == "ξ":
            units.append(("c", "k"))
            units.append(("c", "s"))
        elif c in CONS:
            units.append(("c", CONS[c]))
        else:
            raise ValueError(f"unhandled letter {c!r}")
    out = []
    prev_vowel = "a"
    i = 0
    while i < len(units):
        kind, val = units[i]
        if kind == "v":
            out.append(val)
            prev_vowel = val
            i += 1
        elif i + 1 < len(units) and units[i + 1][0] == "v":
            out.append(val + units[i + 1][1])
            prev_vowel = units[i + 1][1]
            i += 2
        else:
            out.append(val + prev_vowel)
            i += 1
    return out


# ---------- independent alignment (substring scan) ----------

def align(a, b):
    """Longest common contiguous subsequence; ties by
    smallest i in a, then smallest j in b."""
    for L in range(min(len(a), len(b)), 0, -1):
        for i in range(len(a) - L + 1):
            for j in range(len(b) - L + 1):
                if a[i:i + L] == b[j:j + L]:
                    return L, i, j
    return 0, 0, 0


def pairings(variant, ds, segs, positions):
    if variant == "A1":
        return {n: positions[n] for n in range(len(ds))}
    if variant == "A2":
        out = {}
        for n, d in enumerate(ds):
            best = max(range(len(segs)),
                       key=lambda s: (align(d, segs[s])[0], -s))
            out[n] = best
        return out
    if variant == "J":
        best_key, best = None, None
        for s1 in range(len(segs)):
            for s2 in range(len(segs)):
                if s1 == s2:
                    continue
                tot = align(ds[0], segs[s1])[0] + align(ds[1], segs[s2])[0]
                key = (tot, -s1, -s2)
                if best_key is None or key > best_key:
                    best_key, best = key, {0: s1, 1: s2}
        return best
    raise ValueError(variant)


def map_endings(prs, ds, segs):
    m, conf, ends = {}, set(), set()
    for n, s in prs.items():
        seg, d = segs[s], ds[n]
        L, i, j = align(d, seg)
        for k in range(L):
            sign, val = seg[j + k], d[i + k]
            if sign in m and m[sign] != val:
                conf.add(sign)
            else:
                m[sign] = val
        ends.add(tuple(seg[j + L:]) if j + L < len(seg)
                 else (seg[-1],))
    for c in conf:
        m.pop(c, None)
    return m, sorted(conf), sorted(ends)


def k1(ends, forms):
    return sum(1 for f in forms
               if any(tuple(f[-len(e):]) == tuple(e) for e in ends))


def k2(m, toks):
    return sum(1 for t in toks if t in m) / len(toks)


def generate(segs, ds, positions, forms, toks):
    vs = {}
    for v in ("A1", "A2", "J"):
        p = pairings(v, ds, segs, positions)
        m, conf, ends = map_endings(p, ds, segs)
        vs[v] = {"pairings": {str(n): s + 1 for n, s in p.items()},
                 "anchored_map": m, "conflicts_excluded": conf,
                 "implied_endings": [list(e) for e in ends],
                 "key1": k1(ends, forms), "key2": k2(m, toks)}
    order = sorted(vs, key=lambda v: (-vs[v]["key1"], -vs[v]["key2"],
                                      ("A1", "A2", "J").index(v)))
    return vs, order


SYNTH_LABELS = [
    "a", "e", "i", "o", "u",
    "ka", "ke", "ki", "ko", "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "na", "ne", "ni", "no", "nu",
    "ra", "re", "ri", "ro", "sa", "se", "si", "so",
    "ta", "te", "ti", "to",
]

SCAN_PHRASES = [
    "all checks passed", "is licensed", "are licensed",
    "licensed for", "licence", "OD-O-2 is resolved",
    "OD-O-2 resolved", "resolves OD-O-2",
    "presumes OD-O-2", "presuming OD-O-2",
    "OD-O-2 is settled",
]


def main():
    spec_dir, custody = sys.argv[1], sys.argv[2]
    corpus_path = os.path.join(
        spec_dir, "..", "096-eteocypriot-program", "corpus",
        "corpus.json")
    intake_path = os.path.join(
        spec_dir, "..", "096-eteocypriot-program", "corpus",
        "corpus-androkles-intake-2026-11-22.json")
    corpus_raw = open(corpus_path, "rb").read()
    check("corpus pin", sha(corpus_raw) ==
          "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597")
    check("intake pin", sha(open(intake_path, "rb").read()) ==
          "8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a")
    records = os.path.join(spec_dir, "records")
    freeze_path = os.path.join(records, "stage-4-freeze-2026-11-27.md")
    check("freeze pin", sha(open(freeze_path, "rb").read()) ==
          "80ec9c9f5cdd0a3f362d1c2679277ec967f899d2fea541e3e5769d0c36d216dd")
    harness_path = os.path.join(records, "stage-4-harness.py")
    check("harness pin", sha(open(harness_path, "rb").read()) ==
          "c9776d3e88bf86a127b8f7b863086b9dbfd386575e6dc513ddb1508210d44a53")

    corpus = json.loads(corpus_raw.decode("utf-8"))
    intake = json.loads(open(intake_path).read())
    ics = [x for x in corpus["inscriptions"] if x["id"] == "ICS196"][0]
    segs = [[t.strip("[]") for t in s]
            for line in ics["eteocypriot_lines"]
            for s in line["segments"]]
    toks = [t for s in segs for t in s]
    words = []
    for line in ics["greek_side"]["lines"]:
        words += line.split()
    ds = [derive(words[4]), derive(words[5])]
    check("derived spellings", ds == [["a", "ri", "si", "to", "na"],
          ["a", "ri", "si", "to", "na", "ka", "to", "so"]])
    forms = [list(f["form"]) for rec in corpus["inscriptions"]
             for f in rec.get("attested_forms_only", [])]
    check("held-out forms census", len(forms) == 8)
    vs, order = generate(segs, ds, [4, 5], forms, toks)

    # TC-109-03 replay: filed candidate records vs recomputation
    filed = [json.loads(x) for x in
             open(os.path.join(custody, "candidate-records.jsonl"))]
    check("candidate record count", len(filed) == 3)
    replay_order = [r["variant"] for r in
                    sorted(filed, key=lambda r: r["rank"])]
    check("replay ranking equals recomputed ranking",
          replay_order == order, f"filed={replay_order} recomputed={order}")
    for r in filed:
        v = vs[r["variant"]]
        check(f"replay {r['variant']} pairings",
              r["pairings"] == v["pairings"])
        check(f"replay {r['variant']} anchored map",
              r["anchored_map"] == v["anchored_map"])
        check(f"replay {r['variant']} endings",
              [list(e) for e in r["implied_endings"]] ==
              v["implied_endings"])
        check(f"replay {r['variant']} margins",
              r["key1"] == v["key1"] and r["key2"] == v["key2"])
        prov = r["provenance"]
        check(f"replay {r['variant']} provenance pins",
              prov["corpus_sha256"] ==
              "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597"
              and prov["freeze_sha256"] ==
              "80ec9c9f5cdd0a3f362d1c2679277ec967f899d2fea541e3e5769d0c36d216dd"
              and prov["generator_sha256"] ==
              "c9776d3e88bf86a127b8f7b863086b9dbfd386575e6dc513ddb1508210d44a53"
              and prov["null_seed"] == 109401)

    # TC-109-07: null recomputation and verdict consequence
    raw_tokens = [t for line in ics["eteocypriot_lines"]
                  for s in line["segments"] for t in s]
    andro = [x for x in intake["inscriptions"]
             if x["id"] == "ANDROKLES-A"][0]
    raw_tokens += [t for line in andro["eteocypriot_side"]["lines"]
                   for s in line["segments"] for t in s]
    inventory = sorted(set(raw_tokens))
    check("filed inventory is 35 marks", len(inventory) == 35)
    rng = random.Random(109401)
    null_max = []
    for _ in range(999):
        perm = inventory[:]
        rng.shuffle(perm)
        mp = dict(zip(inventory, perm))
        best = 0
        for v, data in vs.items():
            ep = [tuple(mp[x] for x in e)
                  for e in data["implied_endings"]]
            best = max(best, k1(ep, forms))
        null_max.append(best)
    null_sorted = sorted(null_max)
    p99 = null_sorted[int(0.99 * 999)]
    raw = json.load(open(os.path.join(
        custody, "stage-4-raw-output-2026-11-27.json")))
    check("null distribution recomputes",
          null_sorted == raw["null"]["null_max_key1_sorted"])
    check("null p99 recomputes", p99 == raw["null"]["p99"] == 2)
    top_key1 = vs[order[0]]["key1"]
    verdict = ("RANKED SET FILED" if top_key1 > p99 else "RANKING NULL")
    check("verdict is the mechanical consequence",
          verdict == raw["verdict"] == "RANKING NULL",
          f"top_key1={top_key1} p99={p99}")

    # clause S recomputation from the custody corpora
    recs, shufs = [], []
    for n in range(1, 6):
        built = json.load(open(os.path.join(
            custody, f"synth-{n}.json")))
        stoks = [t for s in built["segments"] for t in s]
        svs, sorder = generate(built["segments"], built["D"],
                               built["name_positions"],
                               built["heldout_forms"], stoks)
        planted = built["planted_anchored"]
        top_map = svs[sorder[0]]["anchored_map"]
        recs.append(sum(1 for s in planted
                        if top_map.get(s) == s) / len(planted))
        rng_s = random.Random(int(sha(
            (built["seed_string"].rsplit("-try", 1)[0]
             + "-shuffle").encode())[:16], 16))
        perm = SYNTH_LABELS[:]
        rng_s.shuffle(perm)
        mapping = dict(zip(SYNTH_LABELS, perm))
        if any(mapping[s] == s for s in SYNTH_LABELS):
            mapping = dict(zip(SYNTH_LABELS, perm[1:] + perm[:1]))
        d_shuf = [[mapping[x] for x in d] for d in built["D"]]
        svs_s, sorder_s = generate(built["segments"], d_shuf,
                                   built["name_positions"],
                                   built["heldout_forms"], stoks)
        top_map_s = svs_s[sorder_s[0]]["anchored_map"]
        shufs.append(sum(1 for s in planted
                         if top_map_s.get(s) == s) / len(planted))
    med_rec = sorted(recs)[2]
    med_shuf = sorted(shufs)[2]
    filed_s = raw["clause_S"]
    check("clause S recoveries recompute",
          recs == [r["recovery"] for r in filed_s["reps"]],
          f"recomputed={recs}")
    check("clause S shuffle recoveries recompute",
          shufs == [r["shuffle_recovery"] for r in filed_s["reps"]],
          f"recomputed={[round(x, 3) for x in shufs]}")
    check("clause S medians and floors",
          med_rec == filed_s["median_recovery"] == 1.0
          and med_shuf == filed_s["median_shuffle_recovery"]
          and med_rec >= 0.80 and med_shuf < 0.5 * med_rec)

    # TC-109-07 language scan over Part 5's records
    hits = []
    for fn in sorted(os.listdir(records)):
        if fn.startswith("stage-4-") and fn.endswith(".md"):
            text = open(os.path.join(records, fn)).read()
            for phrase in SCAN_PHRASES:
                if phrase in text:
                    hits.append((fn, phrase))
    check("language scan zero hits", hits == [], f"hits={hits}")

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"verification: {n_pass}/{len(CHECKS)} checks PASS")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
