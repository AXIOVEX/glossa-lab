#!/usr/bin/env python3
"""Spec 112 - Meroitic structure induction: execution harness.

Implements the registered design of
specs/112-meroitic-structure-induction/spec.md under the execution
freeze of records/execution-freeze-2026-11-28.md. Deterministic;
Python standard library only. Every figure the preflight files is
recomputed independently by records/execution-verify.py (TC-112-06).

Subcommands:
  pins      verify the corpus pins (TC-112-02); print the corpus census
  extract   extract the ground-truth sets (TC-112-03) to
            records/ground-truth-sets.json
  fixture   TC-112-05 fixture: planted-structure corpus, ordered
            versus shuffled slot induction
  preflight the conformance preflight P-1/P-2/P-3 to
            records/preflight-output.json
  induce    the corpus induction; refuses to run unless
            records/preflight-2026-11-28.md files a full PASS
            verdict (TC-112-04)
"""

import hashlib
import json
import math
import random
import re
import sys
from fractions import Fraction

# ---------------------------------------------------------------- pins
KOVETSKY_DIR = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src"
OTTEN_FILE = ("/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/"
              "spec097/otten-corpus/Data/mero-corpus.txt")
KOVETSKY_COMMIT = "145af0836c071e7c9796d37d4b36add00d347c8a"
INSCRIPTIONS_SHA256 = ("1e91e3a0c52626482bc4015b597df862e7818602dab48a7e8702"
                       "40ab2e567bc4")
GOLD_MORPH_SHA256 = ("c5dc8f3479e81a270a3ee68a9f602c125dcc1211c5fa8b1f8091"
                     "e56b4bf8a5b8")
OTTEN_COMMIT = "c9158f6865325877112b6b9ceef83b3c80a93c56"
MERO_SHA256 = ("b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea2"
               "53ce")

# ------------------------------------------------------- registered
# parameters (execution freeze, records/execution-freeze-2026-11-28.md)
SEED = 20261128                # shuffle control and fixture
SEG_MIN_LEN = 5                # segmentation length floor (spec SS3)
SEG_MIN_SUPPORT = 3            # substring inventory: distinct host forms
SEG_LAMBDA = 2.0               # boundary penalty, nats per boundary
SEG_ALPHA = 0.1                # unigram smoothing
K_BEST = 5                     # ranked segmentations filed per form
PART_MIN_LEN = 2               # recurrent partials: length range
PART_MAX_LEN = 8
PART_MIN_SUPPORT = 10          # recurrent partials: distinct host forms
PART_FINAL_MASS = 0.80         # suffixal proposal: final-mass floor
GT_STEM_FLOOR = 3              # ground truth: minimum stem length
BANDS = 6                      # slot induction: relative-position bands
SLOT_MIN_TEXT_TOKENS = 4       # slot induction: minimum text length
CONC_MIN_OCC = 10              # concentrated type: minimum occurrences
CONC_MASS = 0.60               # concentrated type: modal-band mass floor
SLOT_MIN_TYPES = 5             # slot yield: concentrated types per band
LABEL_MIN_TOKENS = 8           # P-2 labeled set: minimum cleaned tokens

TEMPLATE_ORDER = ["invocation", "presentation", "filiation1",
                  "filiation2", "offering", "closing"]
FILIATION_STRINGS = ["tedxe", "tdxe", "terike", "yerike"]
THEONYM_STEMS = {"otten": ["wES", "SErey", "aSErey"],
                 "kovetsky": ["woS", "Sorey", "aSorey"]}


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def held_out(key):
    return int(sha256_bytes(key.encode()), 16) % 10 == 0


def tokenize(text):
    return [t for t in re.split(r"[\s.]+", text) if t and t.isalpha()]


# ------------------------------------------------------------- corpus
def load_kovetsky():
    insc_path = KOVETSKY_DIR + "/data/inscriptions.jsonl"
    assert sha256_file(insc_path) == INSCRIPTIONS_SHA256, "inscriptions pin"
    rows = [json.loads(l) for l in open(insc_path)]
    texts = {}
    for r in rows:
        t = r.get("text")
        if t and t not in texts:
            texts[t] = r["kind"]
    dev = {t: k for t, k in texts.items() if not held_out(t)}
    return texts, dev


def load_otten():
    assert sha256_file(OTTEN_FILE) == MERO_SHA256, "mero-corpus pin"
    lines = open(OTTEN_FILE).read().splitlines()
    dev_lines = sorted(set(l for l in lines if not held_out(l)))
    return lines, dev_lines


def corpus_forms():
    """Distinct development forms per stream, and the pooled set."""
    _, kov_dev = load_kovetsky()
    _, ott_dev_lines = load_otten()
    kov_forms = set()
    for t in kov_dev:
        kov_forms.update(tokenize(t))
    ott_forms = set()
    for l in ott_dev_lines:
        ott_forms.update(tokenize(l))
    return kov_forms, ott_forms


def funerary_texts():
    """Kovetsky funerary development distinct texts, tokenized."""
    _, kov_dev = load_kovetsky()
    out = []
    for t, kind in sorted(kov_dev.items()):
        if kind == "funerary":
            toks = tokenize(t)
            if len(toks) >= SLOT_MIN_TEXT_TOKENS:
                out.append(toks)
    return out


# ------------------------------------------------------- gold material
def gold_entries():
    path = KOVETSKY_DIR + "/data/gold_morphology.json"
    assert sha256_file(path) == GOLD_MORPH_SHA256, "gold morphology pin"
    return json.load(open(path))


def gold_suffix_strings(stream):
    """Corpus-spelling suffix strings of the gold morphology for one
    stream: entries whose form is a suffix (leading '-') with a filed
    corpus form; corpus_form plus corpus_variants. The Kovetsky stream
    writes the o-sign as 'o' where the Otten spelling writes 'E'
    (transliteration map of record), so its set is the E->o fold."""
    out = set()
    for e in gold_entries():
        if e["form"].startswith("-") and e.get("corpus_form"):
            strs = [e["corpus_form"]] + list(e.get("corpus_variants") or [])
            for s in strs:
                out.add(s if stream == "otten" else s.replace("E", "o"))
    return out


def gold_suffix_strings_union():
    return gold_suffix_strings("otten") | gold_suffix_strings("kovetsky")


# ------------------------------------------------------- ground truth
def extract_ground_truth():
    kov_forms, ott_forms = corpus_forms()
    gt = {}   # "stream:form" -> {"stream","form","boundaries","rules"}
    for stream, forms in (("kovetsky", kov_forms), ("otten", ott_forms)):
        suffixes = sorted(gold_suffix_strings(stream),
                          key=lambda s: (-len(s), s))
        for form in sorted(forms):
            if len(form) < SEG_MIN_LEN:
                continue
            bounds = set()
            rules = set()
            # suffix rule: longest gold suffix leaving a stem >= floor
            for s in suffixes:
                if len(s) <= len(form) - GT_STEM_FLOOR and \
                        form.endswith(s):
                    bounds.add(len(form) - len(s))
                    rules.add("gold-suffix:" + s)
                    break
            # filiation rule: first onset of a filiation form at p >= 2
            for f in FILIATION_STRINGS:
                p = form.find(f)
                if p >= 2:
                    bounds.add(p)
                    rules.add("filiation:" + f)
            # theonym rule: theonym stem + final -i, exact forms
            for stem in THEONYM_STEMS[stream]:
                if form == stem + "i":
                    bounds.add(len(form) - 1)
                    rules.add("theonym:" + stem)
            if bounds:
                gt[stream + ":" + form] = {
                    "stream": stream, "form": form,
                    "boundaries": sorted(bounds), "rules": sorted(rules)}
    return gt


# --------------------------------------------------------- segmenter
class Segmenter:
    """Positional-class unigram DP segmenter over distinct forms.

    Segment statistics are counted over the distinct development
    forms (each form contributes its substrings once), by positional
    class: I (form-initial), F (form-final), M (medial), W (whole
    form). Score of a segmentation: sum of log P(segment | class)
    minus SEG_LAMBDA per boundary. Deterministic."""

    def __init__(self, forms):
        self.counts = {c: {} for c in "IFMW"}
        self.support = {}
        for form in forms:
            n = len(form)
            seen = set()
            for i in range(n):
                for j in range(i + 1, n + 1):
                    sub = form[i:j]
                    cls = ("W" if i == 0 and j == n else
                           "I" if i == 0 else
                           "F" if j == n else "M")
                    c = self.counts[cls]
                    c[sub] = c.get(sub, 0) + 1
                    if sub not in seen:
                        seen.add(sub)
                        self.support[sub] = self.support.get(sub, 0) + 1
        self.totals = {c: sum(d.values()) for c, d in self.counts.items()}
        self.vocab = {c: len(d) for c, d in self.counts.items()}
        self.inventory = {s for s, v in self.support.items()
                          if v >= SEG_MIN_SUPPORT or len(s) == 1}

    def logp(self, sub, cls):
        c = self.counts[cls].get(sub, 0)
        return math.log((c + SEG_ALPHA) /
                        (self.totals[cls] + SEG_ALPHA * self.vocab[cls]))

    def segment(self, form, k=K_BEST):
        n = len(form)
        # best[i]: up to k (score, segmentation tuple) for form[:i]
        best = [[] for _ in range(n + 1)]
        best[0] = [(0.0, ())]
        for i in range(1, n + 1):
            cand = {}
            for j in range(0, i):
                sub = form[j:i]
                whole = (j == 0 and i == n)
                if not whole and sub not in self.inventory \
                        and len(sub) > 1:
                    continue
                cls = ("W" if whole else
                       "I" if j == 0 else
                       "F" if i == n else "M")
                lp = self.logp(sub, cls)
                for score, seg in best[j]:
                    ns = score + lp - (SEG_LAMBDA if seg else 0.0)
                    nseg = seg + (sub,)
                    key = nseg
                    if key not in cand or ns > cand[key]:
                        cand[key] = ns
            ranked = sorted(cand.items(), key=lambda kv: (-kv[1], kv[0]))
            best[i] = [(score, seg) for seg, score in ranked[:k]]
        return best[n]

    @staticmethod
    def boundaries(segmentation):
        out, acc = [], 0
        for seg in segmentation[:-1]:
            acc += len(seg)
            out.append(acc)
        return out


def boundary_f1(pred, gold):
    p, g = set(pred), set(gold)
    tp = len(p & g)
    if not p and not g:
        return Fraction(1)
    if not p or not g:
        return Fraction(0)
    return Fraction(2 * tp, 2 * tp + (len(p - g)) + (len(g - p)))


# ------------------------------------------------------------ slots
def type_profiles(texts):
    """Per-type positional profiles over tokenized texts."""
    prof = {}
    for toks in texts:
        n = len(toks)
        for idx, t in enumerate(toks):
            rel = idx / (n - 1) if n > 1 else 0.0
            band = min(BANDS - 1, int(BANDS * rel))
            d = prof.setdefault(t, {"occ": 0, "bands": [0] * BANDS,
                                    "rel_sum": 0.0})
            d["occ"] += 1
            d["bands"][band] += 1
            d["rel_sum"] += rel
    for d in prof.values():
        d["centroid"] = d["rel_sum"] / d["occ"]
        mb = max(range(BANDS), key=lambda b: (d["bands"][b], -b))
        d["modal_band"] = mb
        d["modal_mass"] = d["bands"][mb] / d["occ"]
    return prof


def slot_yield(prof):
    conc = [t for t, d in prof.items()
            if d["occ"] >= CONC_MIN_OCC and d["modal_mass"] >= CONC_MASS]
    per_band = [0] * BANDS
    for t in conc:
        per_band[prof[t]["modal_band"]] += 1
    return sum(1 for c in per_band if c >= SLOT_MIN_TYPES), per_band


def band_mapping(prof):
    """Map positional bands to template slots by the pinned forms
    (comparison only; the induction itself is blind). Returns
    (mapping band->slot, note) or (None, reason)."""
    def modal_of(pred, what):
        cands = [(d["occ"], t) for t, d in prof.items() if pred(t)]
        if not cands:
            return None, "no type for " + what
        cands.sort(key=lambda x: (-x[0], x[1]))
        return prof[cands[0][1]]["modal_band"], cands[0][1]

    inv, _ = modal_of(lambda t: t == "woSi", "invocation")
    if inv is None:
        return None, "invocation type woSi absent"
    f1, _ = modal_of(lambda t: "tedxe" in t or "tdxe" in t, "filiation1")
    f2, _ = modal_of(lambda t: "terike" in t or "yerike" in t, "filiation2")
    off, _ = modal_of(lambda t: t == "ato", "offering")
    if f1 is None or f2 is None or off is None:
        return None, "a filiation or offering type is absent"
    mapping = {inv: "invocation", f1: "filiation1", f2: "filiation2",
               off: "offering"}
    # band centroids over occurrences assigned by modal band
    band_rel = {}
    for t, d in prof.items():
        band_rel.setdefault(d["modal_band"], []).append(d)
    band_centroid = {}
    for b, ds in band_rel.items():
        occ = sum(d["occ"] for d in ds)
        band_centroid[b] = sum(d["rel_sum"] for d in ds) / occ
    remaining = [b for b in range(BANDS) if b not in mapping]
    remaining.sort(key=lambda b: band_centroid.get(b, 0.0))
    after = [b for b in remaining
             if band_centroid.get(b, 0.0) > band_centroid.get(inv, 0.0)]
    if not after:
        return None, "no unmapped band after the invocation band"
    pres = after[0]
    mapping[pres] = "presentation"
    rest = [b for b in remaining if b != pres]
    if rest:
        mapping[rest[-1]] = "closing"
    return mapping, "ok"


def token_slot(t, idx, n, prof, mapping):
    d = prof.get(t)
    if d is not None and d["occ"] >= 3:
        band = d["modal_band"]
    else:
        rel = idx / (n - 1) if n > 1 else 0.0
        band = min(BANDS - 1, int(BANDS * rel))
    return mapping.get(band)


def induced_sequence(toks, prof, mapping):
    seq = []
    n = len(toks)
    for idx, t in enumerate(toks):
        s = token_slot(t, idx, n, prof, mapping)
        if s is not None and s not in seq:
            seq.append(s)
    return seq


def slot_entropy(texts, prof, mapping):
    """Per-slot filler-type entropy (bits) over the given texts."""
    per_slot = {}
    for toks in texts:
        n = len(toks)
        for idx, t in enumerate(toks):
            s = token_slot(t, idx, n, prof, mapping)
            if s is not None:
                d = per_slot.setdefault(s, {})
                d[t] = d.get(t, 0) + 1
    out = {}
    for s, d in per_slot.items():
        tot = sum(d.values())
        out[s] = -sum((c / tot) * math.log2(c / tot) for c in d.values())
    return out, per_slot


# ------------------------------------------------------- P-2 labels
def label_text(toks):
    """Class B label for one funerary text, from the pinned forms.
    Returns the set of present slots, or None if the text is not
    labelable (invocation pair not in the opening zone, or no
    filiation token)."""
    def find(pred, lo=0):
        for i in range(lo, len(toks)):
            if pred(toks[i]):
                return i
        return None

    wos = find(lambda t: t == "woSi")
    sor = find(lambda t: t in ("Soreyi", "aSoreyi"))
    if wos is None or sor is None or wos > 3 or sor > 4 or wos > sor:
        return None
    fil1 = find(lambda t: "tedxe" in t or "tdxe" in t, sor + 1)
    fil2 = find(lambda t: "terike" in t or "yerike" in t, sor + 1)
    if fil1 is None and fil2 is None:
        return None
    off = find(lambda t: t == "ato" or (t.startswith("ato")
                                        and len(t) <= 7), sor + 1)
    present = {"invocation"}
    anchors = [i for i in (fil1, fil2, off) if i is not None]
    first_anchor = min(anchors)
    if first_anchor > sor + 1:
        present.add("presentation")
    if fil1 is not None:
        present.add("filiation1")
    if fil2 is not None:
        present.add("filiation2")
    if off is not None:
        present.add("offering")
    if max(anchors) < len(toks) - 1:
        present.add("closing")
    return present


# ---------------------------------------------------------- partials
def induce_partials(forms):
    support = {}
    profile = {}
    for form in forms:
        n = len(form)
        seen = set()
        for i in range(n):
            for ln in range(PART_MIN_LEN, PART_MAX_LEN + 1):
                j = i + ln
                if j > n:
                    break
                sub = form[i:j]
                if sub not in seen:
                    seen.add(sub)
                    support.setdefault(sub, set()).add(form)
                if j - i == n:
                    continue  # whole-form occurrence: support only
                d = profile.setdefault(sub, [0, 0, 0])
                if i == 0:
                    d[0] += 1
                elif j == n:
                    d[2] += 1
                else:
                    d[1] += 1
    out = {}
    for sub, hosts in support.items():
        if len(hosts) < PART_MIN_SUPPORT:
            continue
        ini, med, fin = profile.get(sub, [0, 0, 0])
        tot = ini + med + fin
        out[sub] = {
            "support": len(hosts),
            "hosts": sorted(hosts),
            "initial_mass": ini / tot if tot else 0.0,
            "medial_mass": med / tot if tot else 0.0,
            "final_mass": fin / tot if tot else 0.0}
    return out


# ------------------------------------------------------------ fixture
def build_fixture():
    rng = random.Random(SEED)
    alphabet = "abdeiklmnpqrstwxSNE"
    def name():
        return "".join(rng.choice(alphabet)
                       for _ in range(rng.randint(4, 8)))
    names = set()
    while len(names) < 40:
        names.add(name())
    names = sorted(names)
    texts, labels = [], []
    for _ in range(120):
        toks = ["woSi", "Soreyi", rng.choice(names)]
        present = {"invocation", "presentation"}
        if rng.random() < 0.85:
            toks.append(rng.choice(names) + "tedxe")
            present.add("filiation1")
        if rng.random() < 0.85:
            toks.append(rng.choice(names) + "terike")
            present.add("filiation2")
        if rng.random() < 0.8:
            toks.append(rng.choice(["ato", "atomXe"]))
            present.add("offering")
        if rng.random() < 0.8:
            toks.append(rng.choice(["yetmde", "mlolowi", "xitkkete"]))
            present.add("closing")
        texts.append(toks)
        labels.append(present)
    return texts, labels


def shuffle_texts(texts, seed=SEED):
    rng = random.Random(seed)
    out = []
    for toks in texts:
        t = list(toks)
        rng.shuffle(t)
        out.append(t)
    return out


# ------------------------------------------------------------ commands
def cmd_pins():
    kov_texts, kov_dev = load_kovetsky()
    ott_lines, ott_dev = load_otten()
    gm_path = KOVETSKY_DIR + "/data/gold_morphology.json"
    print("kovetsky commit (worktree HEAD recorded at freeze):", KOVETSKY_COMMIT)
    print("inscriptions.jsonl sha256 OK:", INSCRIPTIONS_SHA256)
    print("gold_morphology.json sha256:", sha256_file(gm_path))
    print("otten commit pin:", OTTEN_COMMIT)
    print("mero-corpus.txt sha256 OK:", MERO_SHA256)
    print("kovetsky distinct texts:", len(kov_texts),
          "development:", len(kov_dev))
    fun = funerary_texts()
    print("funerary development texts (>= %d tokens): %d"
          % (SLOT_MIN_TEXT_TOKENS, len(fun)))
    print("otten lines:", len(ott_lines), "development distinct lines:",
          len(ott_dev))
    kov_forms, ott_forms = corpus_forms()
    print("distinct development forms: kovetsky %d, otten %d, pooled %d"
          % (len(kov_forms), len(ott_forms), len(kov_forms | ott_forms)))


def cmd_extract(path):
    gt = extract_ground_truth()
    payload = {"seed": SEED,
               "pins": {"kovetsky_commit": KOVETSKY_COMMIT,
                        "inscriptions_sha256": INSCRIPTIONS_SHA256,
                        "gold_morphology_sha256": GOLD_MORPH_SHA256,
                        "otten_commit": OTTEN_COMMIT,
                        "mero_sha256": MERO_SHA256},
               "ground_truth": gt}
    blob = json.dumps(payload, indent=1, sort_keys=True)
    with open(path, "w") as fh:
        fh.write(blob + "\n")
    print("ground-truth forms:", len(gt))
    print("ground-truth file sha256:", sha256_bytes((blob + "\n").encode()))


def run_slot_preflight(texts, labels):
    prof = type_profiles(texts)
    y, per_band = slot_yield(prof)
    mapping, note = band_mapping(prof)
    res = {"yield": y, "yield_per_band": per_band, "mapping": mapping,
           "mapping_note": note}
    if mapping is not None:
        matches = 0
        for toks, present in zip(texts, labels):
            seq = induced_sequence(toks, prof, mapping)
            want = [s for s in TEMPLATE_ORDER if s in present]
            if seq == want:
                matches += 1
        res["sequence_matches"] = matches
        res["labeled"] = len(labels)
        ent, _ = slot_entropy(texts, prof, mapping)
        res["slot_entropy"] = ent
        if ent:
            res["max_entropy_slot"] = max(ent, key=lambda s: ent[s])
    shuf = shuffle_texts(texts)
    sprof = type_profiles(shuf)
    sy, _ = slot_yield(sprof)
    res["shuffle_yield"] = sy
    res["shuffle_ratio"] = (str(Fraction(sy, y)) if y else None)
    return res


def cmd_fixture():
    texts, labels = build_fixture()
    res = run_slot_preflight(texts, labels)
    print(json.dumps(res, indent=1, sort_keys=True))


def cmd_preflight(gt_path, out_path):
    gt = json.load(open(gt_path))["ground_truth"]
    kov_forms, ott_forms = corpus_forms()
    pooled = kov_forms | ott_forms
    seg = Segmenter(pooled)
    # P-1
    f1s = {}
    preds = {}
    for key, rec in sorted(gt.items()):
        form = rec["form"]
        ranked = seg.segment(form)
        pred = Segmenter.boundaries(ranked[0][1]) if ranked else []
        preds[key] = pred
        f1s[key] = boundary_f1(pred, rec["boundaries"])
    vals = sorted(f1s.values())
    m = len(vals)
    median = vals[m // 2] if m % 2 else (vals[m // 2 - 1] + vals[m // 2]) / 2
    p1 = {"n_forms": m, "median_f1": str(median),
          "median_f1_float": float(median),
          "per_form_f1": {k: str(v) for k, v in sorted(f1s.items())},
          "per_form_pred_boundaries": preds,
          "pass": median >= Fraction(4, 5)}
    # P-2 + shuffle (P-3 second leg shares the slot machinery)
    texts = funerary_texts()
    labeled = [(t, label_text(t)) for t in texts]
    labeled = [(t, p) for t, p in labeled if p is not None]
    prof = type_profiles(texts)
    y, per_band = slot_yield(prof)
    mapping, note = band_mapping(prof)
    p2 = {"labeled_texts": len(labeled), "mapping": mapping,
          "mapping_note": note, "yield": y}
    if mapping is not None:
        matches = 0
        per_text = []
        for toks, present in labeled:
            seq = induced_sequence(toks, prof, mapping)
            want = [s for s in TEMPLATE_ORDER if s in present]
            if seq == want:
                matches += 1
            per_text.append({
                "text_sha256": sha256_bytes(" ".join(toks).encode()),
                "label_present": sorted(present),
                "induced_sequence": seq})
        rate = Fraction(matches, len(labeled)) if labeled else Fraction(0)
        ent, per_slot = slot_entropy(texts, prof, mapping)
        name_max = bool(ent) and \
            max(ent, key=lambda s: ent[s]) == "presentation"
        p2.update({"sequence_matches": matches,
                   "match_rate": str(rate),
                   "match_rate_float": float(rate),
                   "slot_entropy": ent,
                   "slot_type_counts": per_slot,
                   "per_text": per_text,
                   "name_slot_is_max_entropy": name_max,
                   "pass": rate >= Fraction(9, 10) and name_max})
    else:
        p2["pass"] = False
    # P-3
    partials = induce_partials(pooled)
    gold = gold_suffix_strings_union()
    proposals = {s for s, d in partials.items()
                 if d["final_mass"] >= PART_FINAL_MASS}
    hits = proposals & gold
    precision = (Fraction(len(hits), len(proposals))
                 if proposals else Fraction(0))
    gold_len2 = {s for s in gold if len(s) >= PART_MIN_LEN}
    recall = (Fraction(len(proposals & gold_len2), len(gold_len2))
              if gold_len2 else Fraction(0))
    shuf = shuffle_texts(texts)
    sy, _ = slot_yield(type_profiles(shuf))
    ratio = Fraction(sy, y) if y else None
    p3 = {"induced_partials": len(partials),
          "suffixal_proposals": len(proposals),
          "gold_suffix_strings": len(gold),
          "gold_suffix_string_set": sorted(gold),
          "proposal_set": sorted(proposals),
          "proposal_hits": len(hits),
          "precision": str(precision), "precision_float": float(precision),
          "recall_filed_for_transparency": str(recall),
          "real_yield": y, "shuffle_yield": sy,
          "shuffle_ratio": str(ratio) if ratio is not None else None,
          "pass": precision >= Fraction(4, 5) and ratio is not None
                  and ratio <= Fraction(1, 5)}
    out = {"seed": SEED, "P-1": p1, "P-2": p2, "P-3": p3,
           "pass_in_full": bool(p1["pass"] and p2["pass"] and p3["pass"])}
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps({k: out[k] for k in ("P-1", "P-2", "P-3")},
                     indent=1, sort_keys=True)[:2000])
    print("PASS IN FULL:", out["pass_in_full"])


def cmd_induce(gt_path, verdict_path, out_dir, freeze_commit):
    verdict = open(verdict_path).read()
    if "PASS IN FULL" not in verdict:
        print("REFUSED: no filed full-pass preflight verdict (TC-112-04)")
        sys.exit(2)
    import os
    kov_forms, ott_forms = corpus_forms()
    pooled = kov_forms | ott_forms
    seg = Segmenter(pooled)
    harness_sha = sha256_file(__file__)
    prov = {"harness_sha256": harness_sha, "seed": SEED,
            "freeze_commit": freeze_commit,
            "pins": {"kovetsky_commit": KOVETSKY_COMMIT,
                     "inscriptions_sha256": INSCRIPTIONS_SHA256,
                     "gold_morphology_sha256": GOLD_MORPH_SHA256,
                     "otten_commit": OTTEN_COMMIT,
                     "mero_sha256": MERO_SHA256}}
    # segmentations
    seg_out = {}
    for form in sorted(pooled):
        if len(form) < SEG_MIN_LEN:
            continue
        ranked = seg.segment(form)
        cands = [{"segments": list(s), "score": round(sc, 6),
                  "boundaries": Segmenter.boundaries(s)}
                 for sc, s in ranked]
        margin = (round(ranked[0][0] - ranked[1][0], 6)
                  if len(ranked) > 1 else None)
        seg_out[form] = {"candidates": cands, "margin_top1_top2": margin}
    with open(os.path.join(out_dir, "induction-segmentations.json"),
              "w") as fh:
        json.dump({"provenance": prov, "forms": seg_out}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    # partials
    partials = induce_partials(pooled)
    with open(os.path.join(out_dir, "induction-partials.json"), "w") as fh:
        json.dump({"provenance": prov, "partials": partials}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    # slot grammar
    texts = funerary_texts()
    prof = type_profiles(texts)
    mapping, note = band_mapping(prof)
    y, per_band = slot_yield(prof)
    conc = {t: {"occ": d["occ"], "modal_band": d["modal_band"],
                "modal_mass": d["modal_mass"], "centroid": d["centroid"]}
            for t, d in prof.items()
            if d["occ"] >= CONC_MIN_OCC and d["modal_mass"] >= CONC_MASS}
    assignments = []
    for toks in texts:
        seq = induced_sequence(toks, prof, mapping) if mapping else []
        assignments.append({"text_sha256": sha256_bytes(
            " ".join(toks).encode()), "tokens": toks, "sequence": seq})
    with open(os.path.join(out_dir, "induction-slot-grammar.json"),
              "w") as fh:
        json.dump({"provenance": prov, "yield": y,
                   "yield_per_band": per_band,
                   "band_to_slot_mapping": mapping,
                   "mapping_note": note,
                   "concentrated_types": conc,
                   "text_assignments": assignments}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    print("segmented forms:", len(seg_out))
    print("partials:", len(partials))
    print("funerary texts assigned:", len(assignments), "yield:", y)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pins":
        cmd_pins()
    elif cmd == "extract":
        cmd_extract(sys.argv[2])
    elif cmd == "fixture":
        cmd_fixture()
    elif cmd == "preflight":
        cmd_preflight(sys.argv[2], sys.argv[3])
    elif cmd == "induce":
        cmd_induce(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("unknown subcommand", cmd)
        sys.exit(2)
