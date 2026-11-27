#!/usr/bin/env python3
"""Spec 107, test M-2 as re-registered (2026-11-27) — execution.

Administers, in the registered order:
  (1) the conformance preflight of records/m2-re-registration-
      2026-11-27.md section 4: Otten custody re-verification
      against the Spec 097 step-0 manifest (30 files), the
      Kovetsky inscriptions pin check, basis reconstruction
      under pipeline-v2 conventions (tokens_of, same_place_rate,
      PLACE, examples() verbatim in substance), and the
      four-figure gate (12,863 words; 13,406 pairs; same-place
      rate 0.3152; NES reference rate 0.3038, each to 4 dp);
  (2) only on a full preflight pass, the phonotactic battery
      of the cycle-2 registration sections 6.1-6.4, carried
      over unchanged: items SP-CVC, LV-CO, ONSET-CC, CODA-C,
      LV-TRANS; Null W and Null X (10,000 replicates, seed
      20261127); family ranges, leans, the leave-one-out
      wrong-family control, split-half description, and the
      POSITIVE / NEGATIVE / INDETERMINATE verdict rule.

The ASJP segment-to-place-class mapping table (cycle-2
section 6.1) is written to the mapping file, with its hash
logged, BEFORE any battery statistic is computed. Raw output
(aggregate statistics only; no Otten byte) is written as
JSON to argv[1]; the mapping table to argv[2]. Exit codes:
0 = preflight passed and battery administered; 3 = preflight
failure (M-2 stops; the failure is the leg's outcome).
"""
import csv
import hashlib
import json
import random
import re
import subprocess
import sys
from datetime import datetime, timezone

WT = "/home/tpierson/.syncyard/worktrees/glossa/spec107-m2-exec-20261127"
KOV = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src"
CUST = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec097"
OTTEN = f"{CUST}/otten-corpus"
MANIFEST = (f"{WT}/specs/097-meroitic-reproduction-benchmark/records/"
            "meroitic-benchmark-step0-manifest-2026-11-20.txt")
KOV_SHA256 = "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
KOV_COMMIT = "145af0836c071e7c9796d37d4b36add00d347c8a"
OTTEN_PIN = "c9158f6865325877112b6b9ceef83b3c80a93c56"
ASJP_PINS = {
    "forms.csv": "4ee30b771a2cba59e7e904587f7f60dc3d823824a7b9aae9dd6f73a960139321",
    "languages.csv": "647174df2eb812eff370355b02b6843d76bfb2b082147bc263e5ccd4cc628be5",
    "parameters.csv": "2ed306c24552ea61e48ad6dc067859d8b70029abfc1d36668246214a5a1183ec",
}
FILED = {"words": 12863, "cvc_pairs": 13406,
         "same_place_rate": 0.3152, "nes_reference_rate": 0.3038}
NES_LANGS = ["OLD_NUBIAN", "NOBIIN", "DONGOLESE_NUBIAN",
             "KUNUZ_NUBIAN", "MEIDOB_NUBIAN", "NARA"]
AA_LANGS = ["COPTIC", "LATE_EGYPTIAN", "MIDDLE_EGYPTIAN", "AKKADIAN",
            "BIBLICAL_HEBREW", "AMHARIC", "HAUSA"]
FAMILIES = {"R1_NES": NES_LANGS, "R2_AFROASIATIC": AA_LANGS}
SEED = 20261127
NREP = 10000


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] M-2-rereg {msg}", flush=True)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------- pipeline-v2 conventions (verbatim in substance) ----------
def tokens_of(text):
    return [t for t in re.split(r"[\s.]+", text.lower())
            if t and not t.startswith("#")]


PLACE = {"p": "labial", "b": "labial", "m": "labial",
         "k": "velar", "q": "velar", "g": "velar", "x": "velar",
         "t": "coronal", "d": "coronal", "s": "coronal",
         "z": "coronal", "n": "coronal", "l": "coronal",
         "r": "coronal"}
VOWELS = set("aeiou")


def cons_of(word):
    """Consonant (index, char) list, pipeline-v2's predicate."""
    return [(i, c) for i, c in enumerate(word)
            if c not in VOWELS and c.isalpha()]


def cvc_pairs(word):
    """Adjacent consonants at char distance exactly 2 (one vowel
    between), pipeline-v2's pair enumeration."""
    cons = cons_of(word)
    return [(c1, c2) for (i1, c1), (i2, c2) in zip(cons, cons[1:])
            if i2 - i1 == 2]


def same_place_rate(words):
    tot = 0
    same = 0
    for w in words:
        for c1, c2 in cvc_pairs(w):
            tot += 1
            if PLACE.get(c1) and PLACE.get(c1) == PLACE.get(c2):
                same += 1
    return (same / tot if tot else None), tot


STRATA = {"funerary": "funerary",
          "royal or temple (stela, wall, cartouche, label)":
          "royal_temple",
          "document (ostracon, papyrus, wood, vessel)": "document",
          "graffito": "graffito"}


def main():
    out_path, mapping_path = sys.argv[1], sys.argv[2]
    out = {"test": "M-2 re-registered (Spec 107, T208)",
           "registration": "records/m2-re-registration-2026-11-27.md",
           "started_utc": datetime.now(timezone.utc).isoformat()}

    # ================= PREFLIGHT (re-registration section 4) =====
    log("preflight step 1: custody re-verification begins")
    manifest = {}
    for line in open(MANIFEST, encoding="utf-8"):
        parts = line.split()
        if len(parts) == 2 and len(parts[0]) == 64:
            manifest[parts[1]] = parts[0]
    assert len(manifest) == 30, f"manifest entries: {len(manifest)}"
    custody_check = {}
    n_ok = 0
    for rel, want in sorted(manifest.items()):
        got = sha256_file(f"{OTTEN}/{rel}")
        custody_check[rel] = {"filed": want, "actual": got,
                              "match": got == want}
        n_ok += got == want
    log(f"preflight step 1: Otten custody {n_ok}/30 files match "
        f"the step-0 manifest")
    kov_raw = open(f"{KOV}/data/inscriptions.jsonl", "rb").read()
    kov_hash = hashlib.sha256(kov_raw).hexdigest()
    kov_head = subprocess.run(["git", "-C", KOV, "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    log(f"preflight step 1: Kovetsky inscriptions sha256 "
        f"{kov_hash[:16]}... (pin {KOV_SHA256[:16]}...), HEAD "
        f"{kov_head[:12]} (pin {KOV_COMMIT[:12]})")
    asjp_check = {}
    for fn, want in ASJP_PINS.items():
        got = sha256_file(f"{CUST}/{fn}")
        asjp_check[fn] = {"filed": got == want, "sha256": got}
    log("preflight step 1: ASJP custody hashes checked against "
        "freeze v2 pins: "
        + ", ".join(f"{fn}={'OK' if v['filed'] else 'FAIL'}"
                    for fn, v in asjp_check.items()))
    custody_ok = (n_ok == 30 and kov_hash == KOV_SHA256
                  and kov_head == KOV_COMMIT
                  and all(v["filed"] for v in asjp_check.values()))
    out["preflight"] = {
        "custody_reverification": {
            "otten_manifest_files": len(manifest),
            "otten_files_matching": n_ok,
            "otten_pin": OTTEN_PIN,
            "per_file": custody_check,
            "kovetsky_inscriptions_sha256": kov_hash,
            "kovetsky_inscriptions_pin_match": kov_hash == KOV_SHA256,
            "kovetsky_head": kov_head,
            "kovetsky_head_pin_match": kov_head == KOV_COMMIT,
            "asjp_custody": asjp_check,
            "pass": custody_ok}}

    log("preflight step 2: basis reconstruction begins")
    ins = [json.loads(l) for l in kov_raw.decode("utf-8").splitlines()
           if l.strip()]
    seen = {}
    for d in ins:
        t = (d.get("text") or "").strip()
        if t and t not in seen:
            seen[t] = d
    dev, held = [], []
    for t, d in seen.items():
        entry = {"text": t,
                 "stratum": STRATA.get(d.get("kind", "?"), "other")}
        h = int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16) % 10
        (held if h == 0 else dev).append(entry)
    log(f"preflight step 2: partition {len(dev)} development / "
        f"{len(held)} held out (filed 335 / 33)")
    distinct = set()
    for fn in ["MilletExamples.txt", "RillyExamples.txt",
               "Kalabsha_Millet.txt"]:
        for line in open(f"{OTTEN}/Data/{fn}", encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                distinct.add(line)
    examples = sorted(distinct)
    log(f"preflight step 2: {len(examples)} distinct example "
        f"phrases (filed 932)")
    words = []
    for d in dev:
        words += tokens_of(d["text"])
    for line in examples:
        words += tokens_of(line)
    rate, tot = same_place_rate(words)
    nes_words = []
    with open(f"{CUST}/forms.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["Language_ID"] in NES_LANGS:
                nes_words.append(r["Form"].lower())
    nes_rate, nes_tot = same_place_rate(nes_words)
    figures = {"words": len(words), "cvc_pairs": tot,
               "same_place_rate": rate,
               "nes_reference_rate": nes_rate,
               "nes_forms": len(nes_words), "nes_pairs": nes_tot,
               "development_texts": len(dev), "held_out_texts": len(held),
               "distinct_example_phrases": len(examples)}
    gate = (len(words) == FILED["words"] and tot == FILED["cvc_pairs"]
            and round(rate, 4) == FILED["same_place_rate"]
            and round(nes_rate, 4) == FILED["nes_reference_rate"])
    out["preflight"]["basis_reconstruction"] = figures
    out["preflight"]["filed_figures"] = FILED
    out["preflight"]["figure_gate_pass"] = gate
    out["preflight"]["pass"] = bool(custody_ok and gate)
    log(f"preflight step 3: figures words {len(words)} (filed "
        f"12863); pairs {tot} (filed 13406); same-place "
        f"{rate:.4f} (filed 0.3152); NES {nes_rate:.4f} (filed "
        f"0.3038); gate {'PASS' if gate else 'FAIL'}")
    if not out["preflight"]["pass"]:
        out["outcome"] = "PREFLIGHT FAILURE - M-2 STOPS (no battery statistic computed)"
        out["battery"] = None
        json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
        log("preflight FAILED - M-2 stops; outcome written")
        return 3
    log("preflight PASS - battery administration begins")
    return battery(out, out_path, mapping_path, dev, words)


# ---------- battery (cycle-2 registration sections 6.1-6.4) ----------
# ASJP symbol -> class, derived from the ASJP codebook's articulatory
# definitions. Non-segments (diacritic modifiers and separators) are
# dropped before classification. Any observed symbol not in this
# table defaults to "other" and is listed in the run record.
ASJP_TABLE = {
    # vowels: a e i o u; E = mid central vowel; 3 = high central
    # vowel (in these lists the Amharic central vowel)
    "a": "vowel", "e": "vowel", "i": "vowel", "o": "vowel",
    "u": "vowel", "E": "vowel", "3": "vowel",
    # labial: stops, labiodental fricatives, bilabial nasal, and
    # the labial-velar glide w
    "p": "labial", "b": "labial", "m": "labial", "f": "labial",
    "v": "labial", "w": "labial",
    # velar: stops, fricatives x/X, uvular q, velar nasal N
    "k": "velar", "g": "velar", "q": "velar", "x": "velar",
    "X": "velar", "N": "velar",
    # coronal: dental/alveolar stops and fricatives, postalveolar
    # fricatives and affricates, nasal, liquids; 5 per the
    # pipeline's registered ASJP_MAP (5 -> s)
    "t": "coronal", "d": "coronal", "T": "coronal", "s": "coronal",
    "z": "coronal", "S": "coronal", "C": "coronal", "n": "coronal",
    "l": "coronal", "r": "coronal", "5": "coronal",
    # other: glottal stop 7 and h, pharyngeal 8, palatal glides y j
    "7": "other", "h": "other", "8": "other", "y": "other",
    "j": "other",
}
ASJP_NONSEGMENTS = {" ", "~", '"'}


def asjp_segments(form, defaults):
    segs = []
    for ch in form:
        if ch in ASJP_NONSEGMENTS:
            continue
        cls = ASJP_TABLE.get(ch)
        if cls is None:
            cls = "other"
            defaults.add(ch)
        segs.append(cls)
    return segs


def meroitic_segments(word):
    segs = []
    for c in word:
        if c in VOWELS:
            segs.append("vowel")
        elif c.isalpha():
            segs.append(PLACE.get(c, "other"))
    return segs


ITEMS = ["SP-CVC", "LV-CO", "ONSET-CC", "CODA-C", "LV-TRANS"]
PAIR_ITEMS = {"SP-CVC", "LV-TRANS"}
NULL_ITEMS = {"SP-CVC": "W", "LV-TRANS": "W", "LV-CO": "X"}


def meroitic_item_values(word_list):
    """Battery items over raw Meroitic tokens. Pair items use
    pipeline-v2's pair enumeration verbatim (the SP-CVC pair
    population of freeze v2 section 4); LV-CO uses pipeline-v2's
    consonant predicate; ONSET-CC and CODA-C are computed over
    the word's letters (non-letter characters inside a token
    are editorial marks, not segments)."""
    pairs = []
    for w in word_list:
        pairs += cvc_pairs(w)
    npairs = len(pairs)
    out = {}
    out["SP-CVC"] = ((sum(1 for a, b in pairs
                          if PLACE.get(a)
                          and PLACE.get(a) == PLACE.get(b)) / npairs
                      if npairs else None), npairs)
    out["LV-TRANS"] = ((sum(1 for a, b in pairs
                            if {PLACE.get(a), PLACE.get(b)}
                            == {"labial", "velar"}) / npairs
                        if npairs else None), npairs)
    multi = 0
    lvco = 0
    onset = 0
    coda = 0
    for w in word_list:
        classes = [PLACE.get(c) for _, c in cons_of(w)]
        if len(classes) >= 2:
            multi += 1
            if "labial" in classes and "velar" in classes:
                lvco += 1
        letters = [c for c in w if c.isalpha()]
        if (len(letters) >= 2 and letters[0] not in VOWELS
                and letters[1] not in VOWELS):
            onset += 1
        if letters and letters[-1] not in VOWELS:
            coda += 1
    nw = len(word_list)
    out["LV-CO"] = ((lvco / multi if multi else None), multi)
    out["ONSET-CC"] = ((onset / nw if nw else None), nw)
    out["CODA-C"] = ((coda / nw if nw else None), nw)
    return out


def item_values(seqs):
    """Item values over a list of segment-class sequences.
    Returns {item: (value, denominator)}."""
    out = {}
    pairs = []
    for s in seqs:
        cons = [(i, c) for i, c in enumerate(s) if c != "vowel"]
        for (i1, c1), (i2, c2) in zip(cons, cons[1:]):
            if i2 - i1 == 2:
                pairs.append((c1, c2))
    npairs = len(pairs)
    out["SP-CVC"] = ((sum(1 for a, b in pairs if a == b) / npairs
                      if npairs else None), npairs)
    out["LV-TRANS"] = ((sum(1 for a, b in pairs
                            if {a, b} == {"labial", "velar"}) / npairs
                        if npairs else None), npairs)
    multi = [s for s in seqs if sum(1 for c in s if c != "vowel") >= 2]
    out["LV-CO"] = ((sum(1 for s in multi
                         if "labial" in s and "velar" in s) / len(multi)
                     if multi else None), len(multi))
    nw = len(seqs)
    out["ONSET-CC"] = ((sum(1 for s in seqs
                            if len(s) >= 2 and s[0] != "vowel"
                            and s[1] != "vowel") / nw
                        if nw else None), nw)
    out["CODA-C"] = ((sum(1 for s in seqs
                          if s and s[-1] != "vowel") / nw
                      if nw else None), nw)
    return out


def battery(out, out_path, mapping_path, dev, words):
    # --- comparator lists, one per language, as filed ---
    forms = {}
    with open(f"{CUST}/forms.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["Language_ID"] in NES_LANGS + AA_LANGS:
                forms.setdefault(r["Language_ID"], []).append(r["Form"])
    defaults = set()
    comp_seqs = {lang: [asjp_segments(f, defaults) for f in fs]
                 for lang, fs in forms.items()}
    # --- section 6.1: mapping table filed BEFORE any statistic ---
    mapping = {
        "filed_before_battery_statistics": True,
        "asjp_symbol_to_class": ASJP_TABLE,
        "asjp_non_segments_dropped": sorted(ASJP_NONSEGMENTS),
        "asjp_defaulted_symbols": sorted(defaults),
        "meroitic_place_classes": {
            "labial": ["p", "b", "m"], "velar": ["k", "q", "g", "x"],
            "coronal": ["t", "d", "s", "z", "n", "l", "r"],
            "other": "every other consonant, including h "
                     "(freeze v2, cycle-2 section 6.1)"},
        "derivation_notes": [
            "ASJP classes from the codebook's articulatory "
            "definitions; E and 3 are vowel symbols (central "
            "vowels); N is the velar nasal (velar); 5 follows the "
            "pipeline's registered ASJP_MAP (5 -> s, coronal); "
            "7 is the glottal stop and 8 the pharyngeal (other); "
            "y and j are palatal glides (other); w is the "
            "labial-velar glide (labial).",
            "The tilde and double-quote are segment modifiers "
            "(nasalization; glottalization) in these lists, not "
            "segments, and spaces are separators; all three are "
            "dropped before classification.",
            "Symbols observed in the 13 lists but absent from "
            "the table default to 'other' and are listed in "
            "asjp_defaulted_symbols."]}
    json.dump(mapping, open(mapping_path, "w"), indent=1,
              ensure_ascii=False)
    mh = sha256_file(mapping_path)
    log(f"section 6.1 mapping table filed at {mapping_path} "
        f"(sha256 {mh[:16]}...); defaulted symbols: "
        f"{sorted(defaults)}; battery statistics begin now")

    # --- Meroitic values: pooled, per stratum, split-half ---
    mer = {"pooled": meroitic_item_values(words)}
    strata_words = {}
    for d in dev:
        strata_words.setdefault(d["stratum"], []).extend(
            tokens_of(d["text"]))
    mer["per_stratum"] = {s: meroitic_item_values(ws)
                          for s, ws in sorted(strata_words.items())}
    halves = [[], []]
    for idx, d in enumerate(dev):
        halves[idx % 2] += tokens_of(d["text"])
    mer["split_half_dev_texts_only"] = {
        f"half_{i + 1}": meroitic_item_values(ws)
        for i, ws in enumerate(halves)}
    log(f"Meroitic pooled items computed over {len(words)} words; "
        f"strata: {sorted(strata_words)}")

    comp = {lang: item_values(seqs) for lang, seqs in comp_seqs.items()}
    log("comparator item values computed for 13 lists")

    # --- floors, ranges, scoreability ---
    def floor_of(item):
        return 100 if item in PAIR_ITEMS else 100

    def list_floor(item):
        return 40

    ranges, scoreable = {}, {}
    for item in ITEMS:
        ranges[item] = {}
        for fam, langs in FAMILIES.items():
            vals = [comp[l][item][0] for l in langs
                    if comp[l][item][0] is not None
                    and comp[l][item][1] >= list_floor(item)]
            ranges[item][fam] = ([min(vals), max(vals)]
                                 if vals else None)
            ranges[item][fam + "_n_lists"] = len(vals)
        mer_val, mer_den = mer["pooled"][item]
        scoreable[item] = bool(
            mer_val is not None and mer_den >= floor_of(item)
            and all(ranges[item][f + "_n_lists"] >= 3
                    for f in FAMILIES))
    log("family ranges and scoreability computed: "
        + ", ".join(f"{i}={'yes' if scoreable[i] else 'no'}"
                    for i in ITEMS))

    # --- nulls (Meroitic pooled observation only) ---
    # Vectorized with numpy; the generator is PCG64 seeded with
    # the registered seed 20261127 (the registration registers
    # the seed and the replicate count; the filed central-95%
    # bounds make the verdict recomputable from the output).
    import numpy as np
    nulls = {}
    CODE = {"labial": 0, "velar": 1, "coronal": 2}
    cons_class = []          # class code per consonant, corpus order
    word_ids = []            # word index per consonant
    word_offsets = [0]
    pair_a, pair_b = [], []
    for wi, w in enumerate(words):
        cons = cons_of(w)
        base = len(cons_class)
        for _, c in cons:
            cons_class.append(CODE.get(PLACE.get(c), 3))
            word_ids.append(wi)
        for a in range(len(cons) - 1):
            if cons[a + 1][0] - cons[a][0] == 2:
                pair_a.append(base + a)
                pair_b.append(base + a + 1)
        word_offsets.append(len(cons_class))
    C0 = np.array(cons_class, dtype=np.int8)
    WID = np.array(word_ids, dtype=np.int64)
    PA = np.array(pair_a, dtype=np.int64)
    PB = np.array(pair_b, dtype=np.int64)
    npairs = len(PA)
    assert npairs == mer["pooled"]["SP-CVC"][1], npairs
    # Null W: within-word consonant shuffle; items SP-CVC, LV-TRANS
    rng = np.random.default_rng(SEED)
    w_dist = {"SP-CVC": [], "LV-TRANS": []}
    for rep in range(NREP):
        keys = rng.random(len(C0))
        order = np.lexsort((keys, WID))
        S = C0[order]
        sa, sb = S[PA], S[PB]
        w_dist["SP-CVC"].append(float(np.mean((sa == sb) & (sa != 3))))
        w_dist["LV-TRANS"].append(float(np.mean(
            ((sa == 0) & (sb == 1)) | ((sa == 1) & (sb == 0)))))
        if (rep + 1) % 500 == 0:
            log(f"Null W progress: {rep + 1}/{NREP} replicates")
    # Null X: cross-word consonant permutation; item LV-CO
    rng_x = np.random.default_rng(SEED)
    x_dist = []
    offsets = np.array(word_offsets, dtype=np.int64)
    counts = np.diff(offsets)
    multi_mask = counts >= 2
    n_multi = int(multi_mask.sum())
    assert n_multi == mer["pooled"]["LV-CO"][1], n_multi
    for rep in range(NREP):
        S = C0[rng_x.permutation(len(C0))]
        lab = np.add.reduceat((S == 0).astype(np.int8), offsets[:-1])
        vel = np.add.reduceat((S == 1).astype(np.int8), offsets[:-1])
        hits = int(np.sum((lab > 0) & (vel > 0) & multi_mask))
        x_dist.append(hits / n_multi)
        if (rep + 1) % 500 == 0:
            log(f"Null X progress: {rep + 1}/{NREP} replicates")
    out["null_implementation"] = ("numpy Generator (PCG64), seed "
                                  "20261127, 10000 replicates per "
                                  "null; Null W shuffles consonants "
                                  "within words, Null X permutes "
                                  "consonants across words")

    def central95(dist):
        s = sorted(dist)
        return s[int(0.025 * len(s))], s[int(0.975 * len(s))]

    for item, dist in [("SP-CVC", w_dist["SP-CVC"]),
                       ("LV-TRANS", w_dist["LV-TRANS"]),
                       ("LV-CO", x_dist)]:
        lo, hi = central95(dist)
        obs = mer["pooled"][item][0]
        nulls[item] = {"null": NULL_ITEMS[item], "replicates": NREP,
                       "seed": SEED, "central95": [lo, hi],
                       "observed": obs,
                       "null_consistent": bool(lo <= obs <= hi)}
        log(f"Null {NULL_ITEMS[item]} for {item}: central 95% "
            f"[{lo:.4f}, {hi:.4f}], observed {obs:.4f}, "
            f"NULL-CONSISTENT={nulls[item]['null_consistent']}")

    # --- leans ---
    def in_range(v, r):
        return r is not None and r[0] <= v <= r[1]

    def lean(item, value, use_null, rngs):
        leans = []
        for fam in FAMILIES:
            other = [f for f in FAMILIES if f != fam][0]
            if (in_range(value, rngs[item][fam])
                    and not in_range(value, rngs[item][other])
                    and not (use_null and item in nulls
                             and nulls[item]["null_consistent"])):
                leans.append(fam)
        return leans

    mer_leans = {item: lean(item, mer["pooled"][item][0], True, ranges)
                 for item in ITEMS}
    L = {fam: sum(1 for item in ITEMS
                  if scoreable[item] and fam in mer_leans[item])
         for fam in FAMILIES}
    log(f"pooled leans: {mer_leans}; L_R1={L['R1_NES']}, "
        f"L_R2={L['R2_AFROASIATIC']}")

    # --- control: leave-one-out wrong-family ---
    control = {}
    C = 0
    for target in NES_LANGS + AA_LANGS:
        counts = {fam: 0 for fam in FAMILIES}
        for item in ITEMS:
            if not scoreable[item]:
                continue
            t_ranges = {}
            item_ok = True
            for fam, langs in FAMILIES.items():
                vals = [comp[l][item][0] for l in langs if l != target
                        and comp[l][item][0] is not None
                        and comp[l][item][1] >= list_floor(item)]
                t_ranges[fam] = ([min(vals), max(vals)]
                                 if vals else None)
                if len(vals) < 3:
                    item_ok = False
            if not item_ok:
                continue
            for fam in FAMILIES:
                other = [f for f in FAMILIES if f != fam][0]
                v = comp[target][item][0]
                if (in_range(v, t_ranges[fam])
                        and not in_range(v, t_ranges[other])):
                    counts[fam] += 1
        control[target] = counts
        C = max(C, max(counts.values()))
    log(f"control: C={C} (max lean count over 13 leave-one-out "
        f"targets)")

    # --- per-stratum leans (ranges only; nulls guard the pooled
    # observation only, as registered) ---
    stratum_leans = {}
    for s, vals in mer["per_stratum"].items():
        stratum_leans[s] = {}
        for item in ITEMS:
            v, den = vals[item]
            if v is None or den < floor_of(item):
                stratum_leans[s][item] = None
            else:
                stratum_leans[s][item] = lean(item, v, False, ranges)

    # --- verdict (cycle-2 section 6.4) ---
    n_scoreable = sum(1 for i in ITEMS if scoreable[i])
    verdict, pos_fam, arms = None, None, []
    if n_scoreable < 4:
        verdict = "INDETERMINATE"
        arms.append("fewer than 4 scoreable items")
    else:
        for fam in FAMILIES:
            other = [f for f in FAMILIES if f != fam][0]
            if L[fam] >= 3 and L[fam] - L[other] >= 2 and L[fam] > C:
                pos_fam = fam
        if pos_fam:
            adequate = [s for s, sl in stratum_leans.items()
                        if any(v is not None for v in sl.values())]
            supported = [s for s in adequate
                         if any(pos_fam in (stratum_leans[s][i] or [])
                                for i in ITEMS if scoreable[i])]
            if adequate and not supported:
                verdict = "INDETERMINATE"
                arms.append("pooled POSITIVE contradicted in every "
                            "adequate-floor stratum")
            else:
                verdict = f"POSITIVE({pos_fam})"
        else:
            verdict = "NEGATIVE"
            if C >= max(L.values()):
                arms.append("control arm: C >= max(L_R1, L_R2)")
            nb = [i for i in ITEMS if scoreable[i] and i in nulls]
            if nb and sum(1 for i in nb
                          if nulls[i]["null_consistent"]) > len(nb) / 2:
                arms.append("null arm: a majority of the null-bearing "
                            "scoreable items are NULL-CONSISTENT")
            nonsep = sum(1 for i in ITEMS if scoreable[i]
                         and in_range(mer["pooled"][i][0],
                                      ranges[i]["R1_NES"])
                         == in_range(mer["pooled"][i][0],
                                     ranges[i]["R2_AFROASIATIC"]))
            if nonsep > n_scoreable / 2:
                arms.append("non-separation: Meroitic inside both or "
                            "neither range on a majority of scoreable "
                            "items")
    log(f"verdict: {verdict}; arms: {arms}")

    def ser(vals):
        return {i: {"value": vals[i][0], "denominator": vals[i][1]}
                for i in ITEMS}

    out["battery"] = {
        "mapping_file_sha256": mh,
        "meroitic": {"pooled": ser(mer["pooled"]),
                     "per_stratum": {s: ser(v) for s, v in
                                     mer["per_stratum"].items()},
                     "split_half_dev_texts_only":
                         {k: ser(v) for k, v in
                          mer["split_half_dev_texts_only"].items()}},
        "comparators": {l: ser(comp[l]) for l in comp},
        "family_ranges": ranges,
        "scoreable": scoreable,
        "n_scoreable": n_scoreable,
        "nulls": nulls,
        "meroitic_pooled_leans": mer_leans,
        "lean_counts": L,
        "control_lean_counts": control,
        "control_C": C,
        "per_stratum_leans": stratum_leans,
        "verdict": verdict,
        "positive_family": pos_fam,
        "negative_arms": arms if verdict == "NEGATIVE" else [],
        "indeterminate_grounds": arms if verdict == "INDETERMINATE"
        else []}
    out["outcome"] = verdict
    out["finished_utc"] = datetime.now(timezone.utc).isoformat()
    json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
    log(f"battery complete; verdict {verdict}; output written to "
        f"{out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
