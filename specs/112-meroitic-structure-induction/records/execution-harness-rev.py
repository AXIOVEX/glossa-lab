#!/usr/bin/env python3
"""Spec 112 REVISION - Meroitic structure induction: execution harness.

Implements the revised design of
specs/112-meroitic-structure-induction/records/revision-registration-2026-11-28.md
under the revision execution freeze of
records/execution-freeze-rev-2026-11-28.md. The floors, the
ground-truth sets, and the scoring rules are the first execution's,
carried unchanged; the search design is the revision's. Deterministic;
Python standard library only. Every figure the preflight files is
recomputed independently by records/execution-verify-rev.py
(TC-112-11).

Subcommands:
  pins          verify the corpus pins (TC-112-02); print the census
  extract       extract the ground-truth sets (TC-112-03) for the
                byte-identity check against the filed sets
  fixtureproofs TC-112-10 fixture proofs; precondition of the
                preflight (the preflight refuses without them)
  preflight     the revision conformance preflight P-1/P-2/P-3 to
                records/preflight-rev-output.json
  induce        the corpus induction; refuses to run unless
                records/preflight-rev-2026-11-28.md files a full
                PASS verdict (TC-112-04)
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
# parameters. Carried from the first freeze unless marked REVISED;
# the revision registration is the authority for every REVISED line.
SEED = 20261128                # carried: token shuffle; P-3 null shuffle
SEED_SHUFFLE2 = 20261129       # REVISED: P-3 independent shuffle leg
FIXTURE_SEED = 20261130        # REVISED: fixture proofs (development seed)
SEG_MIN_LEN = 5                # carried: segmentation length floor
SEG_MIN_SUPPORT = 2            # REVISED: inventory support (was 3)
SEG_LAMBDA = 2.0               # carried: boundary penalty, nats
SEG_ALPHA = 0.1                # carried: unigram smoothing
K_BEST = 5                     # carried: ranked segmentations per form
PART_MIN_LEN = 2               # carried: partials length range
PART_MAX_LEN = 8
PART_MIN_SUPPORT = 10          # carried: full partial set floor
GT_STEM_FLOOR = 3              # carried: ground-truth stem floor
SLOT_MIN_TEXT_TOKENS = 4       # carried: funerary stream minimum
LABEL_MIN_TOKENS = 8           # carried: P-2 labeled set minimum
# REVISED slot-grammar parameters (revision registration section 2.2)
ANCHOR_MIN_LEN = 3
ANCHOR_MAX_LEN = 4
ANCHOR_MIN_OCC = 50
ANCHOR_MAX_PER_TEXT = 1.25
ANCHOR_LATE_FRAC = 0.75
ANCHOR_LATE_POS = 0.4
PAR_MIN_LEN = 4
PAR_MAX_LEN = 6
PAR_MIN_HOSTS = 10
PAR_MIN_OCC = 50
PAR_ZONE_FRAC = 0.70
PAR_INIT_SHARE = 0.50
YIELD_FRAME_COV = Fraction(1, 3)
YIELD_ZONE_SHARE = Fraction(1, 3)
YIELD_PRECEDENCE = Fraction(2, 3)

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
    stream (carried construction): entries whose form is a suffix
    (leading '-') with a filed corpus form; corpus_form plus
    corpus_variants; the Kovetsky set is the E->o fold."""
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
    gt = {}
    for stream, forms in (("kovetsky", kov_forms), ("otten", ott_forms)):
        suffixes = sorted(gold_suffix_strings(stream),
                          key=lambda s: (-len(s), s))
        for form in sorted(forms):
            if len(form) < SEG_MIN_LEN:
                continue
            bounds = set()
            rules = set()
            for s in suffixes:
                if len(s) <= len(form) - GT_STEM_FLOOR and \
                        form.endswith(s):
                    bounds.add(len(form) - len(s))
                    rules.add("gold-suffix:" + s)
                    break
            for f in FILIATION_STRINGS:
                p = form.find(f)
                if p >= 2:
                    bounds.add(p)
                    rules.add("filiation:" + f)
            for stem in THEONYM_STEMS[stream]:
                if form == stem + "i":
                    bounds.add(len(form) - 1)
                    rules.add("theonym:" + stem)
            if bounds:
                gt[stream + ":" + form] = {
                    "stream": stream, "form": form,
                    "boundaries": sorted(bounds), "rules": sorted(rules)}
    return gt


# ------------------------------------------------- REVISED segmenter
class Segmenter:
    """Positional-class unigram DP segmenter, REVISED design
    (revision registration section 2.1). Class W is abolished:
    whole-span occurrences are not counted under any class, the
    inventory is uniform (substrings with support >= SEG_MIN_SUPPORT
    distinct host forms, plus every single character), and candidate
    segmentations are restricted to two or more segments. Segment
    statistics are occurrence counts over the distinct development
    forms, by positional class I (initial), F (final), M (medial).
    Score: sum of log P(segment | class) minus SEG_LAMBDA per
    boundary. Deterministic (ties by segmentation tuple)."""

    def __init__(self, forms):
        self.forms = sorted(forms)
        self.counts = {c: {} for c in "IFM"}
        self.support = {}
        for form in self.forms:
            n = len(form)
            seen = set()
            for i in range(n):
                for j in range(i + 1, n + 1):
                    if i == 0 and j == n:
                        continue  # no whole-span count (no W class)
                    sub = form[i:j]
                    cls = "I" if i == 0 else ("F" if j == n else "M")
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

    def score(self, pieces):
        tot = 0.0
        for j, p in enumerate(pieces):
            cls = "I" if j == 0 else ("F" if j == len(pieces) - 1 else "M")
            tot += self.logp(p, cls)
        return tot - SEG_LAMBDA * (len(pieces) - 1)

    def segment(self, form, k=K_BEST):
        n = len(form)
        best = [[] for _ in range(n + 1)]
        best[0] = [(0.0, ())]
        for i in range(1, n + 1):
            cand = {}
            for j in range(0, i):
                if j == 0 and i == n:
                    continue  # >= 2 segments: no one-piece candidate
                sub = form[j:i]
                if sub not in self.inventory and len(sub) > 1:
                    continue
                cls = "I" if j == 0 else ("F" if i == n else "M")
                lp = self.logp(sub, cls)
                for score, seg in best[j]:
                    ns = score + lp - (SEG_LAMBDA if seg else 0.0)
                    nseg = seg + (sub,)
                    if nseg not in cand or ns > cand[nseg]:
                        cand[nseg] = ns
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


def median_fraction(vals):
    vals = sorted(vals)
    m = len(vals)
    return vals[m // 2] if m % 2 else (vals[m // 2 - 1] + vals[m // 2]) / 2


# ------------------------------------------------------- P-2 labels
def label_text(toks):
    """Class B label for one funerary text, from the pinned forms
    (carried verbatim from the first execution). Returns the set of
    present slots, or None if the text is not labelable."""
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


# ------------------------------------------- REVISED sequence grammar
def _argmax_type(counter):
    """Deterministic argmax over a Counter: most occurrences, then
    the lexicographically smallest type."""
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


def induce_grammar(texts):
    """The sequence-anchored slot grammar (revision registration
    section 2.2), induced blind from the funerary texts. Returns a
    dict describing the grammar; missing elements are None."""
    from collections import Counter
    g = {}
    # 1. invocation frame
    first = Counter(t[0] for t in texts)
    t0 = _argmax_type(first)
    second = Counter(t[1] for t in texts if t[0] == t0 and len(t) > 1)
    t1 = _argmax_type(second) if second else None
    g["frame"] = {"t0": t0, "t1": t1}
    g["frame_pair_coverage"] = (
        sum(1 for t in texts if len(t) > 1 and t[0] == t0 and t[1] == t1)
        / len(texts)) if texts else 0.0

    def frame_found(toks):
        return len(toks) > 1 and toks[0] == t0 and toks[1] == t1

    g["frame_found_texts"] = sum(1 for t in texts if frame_found(t))
    # 2. offering anchor
    occ = Counter()
    containing = Counter()
    late = Counter()
    for toks in texts:
        n = len(toks)
        seen = set()
        for idx, x in enumerate(toks):
            occ[x] += 1
            if idx >= ANCHOR_LATE_POS * n:
                late[x] += 1
            if x not in seen:
                seen.add(x)
                containing[x] += 1
    anchor = None
    anchor_stats = {}
    cands = []
    for x in occ:
        if not (ANCHOR_MIN_LEN <= len(x) <= ANCHOR_MAX_LEN):
            continue
        if occ[x] < ANCHOR_MIN_OCC:
            continue
        per_text = occ[x] / containing[x]
        late_frac = late[x] / occ[x]
        anchor_stats[x] = {"occ": occ[x], "texts": containing[x],
                           "per_text": per_text, "late_frac": late_frac}
        if per_text <= ANCHOR_MAX_PER_TEXT and late_frac >= ANCHOR_LATE_FRAC:
            cands.append(x)
    if cands:
        anchor = sorted(cands, key=lambda x: (-containing[x], x))[0]
    g["anchor_candidates"] = anchor_stats
    g["anchor"] = anchor
    family = set()
    if anchor is not None:
        family = {anchor} | {x for x in occ
                             if x != anchor and x.startswith(anchor)
                             and len(x) <= 7}
    g["anchor_family"] = sorted(family)

    def first_offering(toks):
        for i, x in enumerate(toks):
            if x in family:
                return i
        return None

    # 3. filiation paradigms
    types = sorted(occ.keys())
    cand_stats = {}
    for ln in range(PAR_MIN_LEN, PAR_MAX_LEN + 1):
        subs = set()
        for x in types:
            for i in range(0, len(x) - ln + 1):
                subs.add(x[i:i + ln])
        for cand in subs:
            hosts = {x for x in types if cand in x}
            if len(hosts) < PAR_MIN_HOSTS:
                continue
            o = 0
            ini = 0
            zone_num = 0
            zone_den = 0
            for toks in texts:
                off = first_offering(toks)
                ff = frame_found(toks)
                for idx, x in enumerate(toks):
                    if cand in x:
                        o += 1
                        if x.startswith(cand):
                            ini += 1
                        if ff:
                            zone_den += 1
                            if idx > 1 and (off is None or idx < off):
                                zone_num += 1
            if o < PAR_MIN_OCC:
                continue
            zone = zone_num / zone_den if zone_den else 0.0
            ishare = ini / o if o else 0.0
            if zone >= PAR_ZONE_FRAC and ishare >= PAR_INIT_SHARE:
                cand_stats[cand] = {"hosts": len(hosts), "occ": o,
                                    "zone_frac": zone,
                                    "initial_share": ishare,
                                    "host_set": hosts}
    ranked = sorted(cand_stats.items(), key=lambda kv: (-kv[1]["occ"], kv[0]))
    marker_a = ranked[0][0] if ranked else None
    marker_b = None
    if marker_a is not None:
        ha = cand_stats[marker_a]["host_set"]
        for cand, st in ranked[1:]:
            if cand in marker_a or marker_a in cand:
                continue
            hb = st["host_set"]
            if len(ha & hb) < 0.5 * min(len(ha), len(hb)):
                marker_b = cand
                break
    g["paradigm_candidates"] = {
        c: {k: v for k, v in st.items() if k != "host_set"}
        for c, st in cand_stats.items()}
    g["marker_a"] = marker_a
    g["marker_b"] = marker_b

    def paradigm_of(x):
        """'A', 'B', or None: the paradigm a token belongs to."""
        pa = x.find(marker_a) if marker_a is not None else -1
        pb = x.find(marker_b) if marker_b is not None else -1
        if pa < 0 and pb < 0:
            return None
        if pb < 0:
            return "A"
        if pa < 0:
            return "B"
        return "A" if pa <= pb else "B"

    g["paradigm_of"] = paradigm_of
    # 4. precedence majorities and the induced slot order
    both = a_first = 0
    for toks in texts:
        ia = next((i for i, x in enumerate(toks)
                   if paradigm_of(x) == "A"), None)
        ib = next((i for i, x in enumerate(toks)
                   if paradigm_of(x) == "B"), None)
        if ia is not None and ib is not None:
            both += 1
            a_first += ia < ib
    g["paradigm_precedence"] = {
        "texts_with_both": both, "a_first": a_first,
        "majority_share": (max(a_first, both - a_first) / both
                           if both else 0.0)}
    filiation1_par = "A" if a_first >= both - a_first else "B"
    g["filiation1_paradigm"] = filiation1_par if both else None

    def offering_precedence(par):
        num = den = 0
        for toks in texts:
            ipar = next((i for i, x in enumerate(toks)
                         if paradigm_of(x) == par), None)
            ioff = first_offering(toks)
            if ipar is not None and ioff is not None:
                den += 1
                num += ioff > ipar
        return num, den

    off_prec = {}
    for par, slot in (("A", None), ("B", None)):
        num, den = offering_precedence(par)
        off_prec[par] = {"after": num, "texts": den,
                         "share": num / den if den else 0.0}
    g["offering_precedence"] = off_prec
    # slot order over the anchor slots by pairwise majority wins
    slot_of_par = {}
    if both:
        slot_of_par[filiation1_par] = "filiation1"
        slot_of_par["B" if filiation1_par == "A" else "A"] = "filiation2"
    g["slot_of_paradigm"] = slot_of_par
    anchor_slots = ["filiation1", "filiation2", "offering"]
    wins = {s: 0 for s in anchor_slots}
    if both:
        wins["filiation1"] += 1  # filiation1 precedes filiation2 by
        # the majority that named it filiation1
    for par, slot in slot_of_par.items():
        if off_prec[par]["texts"] and off_prec[par]["share"] > 0.5:
            wins[slot] += 1
        elif off_prec[par]["texts"]:
            wins["offering"] += 1
    ordered = sorted(anchor_slots,
                     key=lambda s: (-wins[s], TEMPLATE_ORDER.index(s)))
    g["slot_order"] = ["invocation", "presentation"] + ordered + ["closing"]
    return g


def parse_text(toks, g):
    """Assign every token of one text to a slot under the grammar.
    Returns (fillers, sequence): fillers maps slot -> list of types;
    sequence is the induced slot sequence in the grammar's order."""
    from collections import Counter
    frame_types = {g["frame"]["t0"], g["frame"]["t1"]}
    family = set(g["anchor_family"])
    paradigm_of = g["paradigm_of"]
    slot_of_par = g.get("slot_of_paradigm") or {}

    def anchor_slot(x):
        p = paradigm_of(x)
        if p is not None and p in slot_of_par:
            return slot_of_par[p]
        if x in family:
            return "offering"
        return None

    anchors = [i for i, x in enumerate(toks) if anchor_slot(x)]
    first_anchor = min(anchors) if anchors else None
    last_anchor = max(anchors) if anchors else None
    first_frame = next((i for i, x in enumerate(toks) if x in frame_types),
                       None)
    fillers = {}
    last_slot = None
    for idx, x in enumerate(toks):
        if x in frame_types or (first_frame is not None
                                and idx < first_frame):
            s = "invocation"
        else:
            a = anchor_slot(x)
            if a is not None:
                s = a
            elif last_anchor is not None and idx > last_anchor:
                s = "closing"
            elif first_anchor is not None and idx < first_anchor:
                s = "presentation"
            elif last_slot is not None:
                s = last_slot
            else:
                s = "presentation"
        fillers.setdefault(s, []).append(x)
        if anchor_slot(x) is not None:
            last_slot = anchor_slot(x)
    seq = [s for s in g["slot_order"] if s in fillers]
    return fillers, seq


def grammar_parse_all(texts, g):
    """Parse every text; return per-slot filler counters, per-text
    induced sequences, and the yield accounting."""
    from collections import Counter
    per_slot = {s: Counter() for s in TEMPLATE_ORDER}
    sequences = []
    for toks in texts:
        fillers, seq = parse_text(toks, g)
        sequences.append(seq)
        for s, xs in fillers.items():
            per_slot[s].update(xs)
    ent = {}
    for s, c in per_slot.items():
        tot = sum(c.values())
        if tot:
            ent[s] = -sum((v / tot) * math.log2(v / tot)
                          for v in c.values())
    # yield accounting (revision registration section 2.2, item 6)
    y = {}
    cov = g["frame_pair_coverage"]
    y["invocation"] = cov >= YIELD_FRAME_COV
    framed_anchored = 0
    pres_nonempty = 0
    anchored = 0
    closing_nonempty = 0
    for toks in texts:
        fillers, _ = parse_text(toks, g)
        has_anchor = any(s in fillers for s in
                         ("filiation1", "filiation2", "offering"))
        ff = (len(toks) > 1 and toks[0] == g["frame"]["t0"]
              and toks[1] == g["frame"]["t1"])
        if has_anchor:
            anchored += 1
            if fillers.get("closing"):
                closing_nonempty += 1
        if ff and has_anchor:
            framed_anchored += 1
            if fillers.get("presentation"):
                pres_nonempty += 1
    y["presentation"] = bool(framed_anchored) and \
        Fraction(pres_nonempty, framed_anchored) >= YIELD_ZONE_SHARE
    _pp = g["paradigm_precedence"]
    _both = _pp["texts_with_both"]
    maj = Fraction(max(_pp["a_first"], _both - _pp["a_first"]), _both) \
        if _both else Fraction(0)
    pair_ok = g["marker_a"] is not None and g["marker_b"] is not None \
        and maj >= YIELD_PRECEDENCE
    y["filiation1"] = bool(pair_ok)
    y["filiation2"] = bool(pair_ok)
    # offering: anchor found and offering-after-filiation majority
    num = den = 0
    for toks in texts:
        ifil = next((i for i, x in enumerate(toks)
                     if g["paradigm_of"](x) is not None), None)
        ioff = next((i for i, x in enumerate(toks)
                     if x in set(g["anchor_family"])), None)
        if ifil is not None and ioff is not None:
            den += 1
            num += ioff > ifil
    y["offering"] = g["anchor"] is not None and bool(den) and \
        Fraction(num, den) >= YIELD_PRECEDENCE
    y["closing"] = bool(anchored) and \
        Fraction(closing_nonempty, anchored) >= YIELD_ZONE_SHARE
    yield_count = sum(1 for v in y.values() if v)
    return {"per_slot_type_counts": {s: dict(c) for s, c in per_slot.items()},
            "slot_entropy": ent,
            "sequences": sequences,
            "yield_by_slot": y,
            "yield": yield_count,
            "offering_precedence_combined": {"after": num, "texts": den}}


def shuffle_texts(texts, seed=SEED):
    rng = random.Random(seed)
    out = []
    for toks in texts:
        t = list(toks)
        rng.shuffle(t)
        out.append(t)
    return out


# ---------------------------------------------------------- partials
def induce_partials(forms):
    """The full induced partial set (carried construction): every
    substring of length PART_MIN_LEN..PART_MAX_LEN with support >=
    PART_MIN_SUPPORT distinct host forms, with positional profile."""
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
                    continue
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


# ------------------------------------------------------ P-3 helpers
def char_shuffled_forms(forms, seed):
    """Each form's characters permuted (one rng over the sorted
    forms). Returns the distinct shuffled forms, sorted."""
    rng = random.Random(seed)
    out = set()
    for form in sorted(forms):
        chars = list(form)
        rng.shuffle(chars)
        out.add("".join(chars))
    return sorted(out)


def final_segment_supports(seg, forms):
    """Distinct-residual support of every length >= 2 final segment
    of the segmenter's top-1 segmentation, over the given forms of
    length >= SEG_MIN_LEN whose residual has length >= GT_STEM_FLOOR.
    Returns {final_segment: sorted list of distinct residuals}."""
    supports = {}
    for form in sorted(forms):
        if len(form) < SEG_MIN_LEN:
            continue
        ranked = seg.segment(form)
        if not ranked:
            continue
        pieces = ranked[0][1]
        final = pieces[-1]
        residual = form[:len(form) - len(final)]
        if len(final) >= PART_MIN_LEN and len(residual) >= GT_STEM_FLOOR:
            supports.setdefault(final, set()).add(residual)
    return {s: sorted(v) for s, v in supports.items()}


# ------------------------------------------------------------ fixtures
EASY_SUFFIXES = ["wi", "lowi", "te", "kes", "kete", "li", "se", "leb",
                 "yi", "bx", "lo", "l"]
HARD_SUFFIXES = ["E", "b", "bx", "i", "k", "kes", "kete", "kwi", "l",
                 "lE", "lEwi", "leb", "lewi", "li", "lo", "lowi", "o",
                 "s", "se", "te", "wi", "x", "yi", "yte"]


def build_easy_fixture(seed=FIXTURE_SEED, n_stems=700, n_forms=2400):
    """Port of the development easy fixture: planted stems (syllable
    concatenations) plus a suffix inventory; ground truth is the
    onset of the longest planted suffix leaving a stem >= 3."""
    rng = random.Random(seed)
    cons = "bdklmnprstxq"
    vow = "aeiouE"

    def syll():
        return rng.choice(cons) + rng.choice(vow)

    stems = set()
    while len(stems) < n_stems:
        stems.add("".join(syll() for _ in range(rng.randint(2, 4))))
    stems = sorted(stems)
    weights = [1.0 / (i + 1) ** 0.7 for i in range(len(stems))]
    forms = {}
    while len(forms) < n_forms:
        stem = rng.choices(stems, weights=weights)[0]
        r = rng.random()
        if r < 0.72:
            form = stem + rng.choice(EASY_SUFFIXES)
        elif r < 0.90:
            form = stem + rng.choice(EASY_SUFFIXES) \
                + rng.choice(EASY_SUFFIXES)
        else:
            forms.setdefault(stem, None)
            continue
        gt = None
        for s in sorted(EASY_SUFFIXES, key=lambda s: -len(s)):
            if form.endswith(s) and len(form) - len(s) >= 3:
                gt = len(form) - len(s)
                break
        if gt is not None:
            forms[form] = gt
    return forms


def build_hard_fixture(seed=FIXTURE_SEED, n_roots=130, n_stems=900,
                       n_forms=2600):
    """Port of the development hard fixture: stems built from
    recurrent root pieces under Zipf weights (stem-internal
    recurrence competes); the planted suffix inventory is the 24
    gold strings; stacked suffixes, bare stems, defective spellings;
    ground truth mirrors the real construction."""
    rng = random.Random(seed)
    cons = "bdklmnprstxqSNE"
    vow = "aeiouE"
    roots = set()
    while len(roots) < n_roots:
        roots.add(rng.choice(cons) + rng.choice(vow)
                  + (rng.choice(cons) if rng.random() < 0.5 else ""))
    roots = sorted(roots)
    stems = set()
    while len(stems) < n_stems:
        k = rng.choices([1, 2, 3], weights=[0.35, 0.45, 0.20])[0]
        stems.add("".join(rng.choice(roots) for _ in range(k)))
    stems = sorted(stems)
    weights = [1.0 / (i + 1) ** 0.8 for i in range(len(stems))]
    forms = {}
    attempts = 0
    while len(forms) < n_forms and attempts < n_forms * 30:
        attempts += 1
        stem = rng.choices(stems, weights=weights)[0]
        r = rng.random()
        if r < 0.62:
            form = stem + rng.choice(HARD_SUFFIXES)
        elif r < 0.88:
            form = stem + rng.choice(HARD_SUFFIXES) \
                + rng.choice(HARD_SUFFIXES)
        else:
            form = stem
        if rng.random() < 0.06 and len(form) > 5:
            idx = [i for i, c in enumerate(form) if c in vow]
            if idx:
                i = rng.choice(idx)
                form = form[:i] + form[i + 1:]
        if len(form) < 5:
            continue
        gt = None
        for s in sorted(HARD_SUFFIXES, key=lambda s: -len(s)):
            if form.endswith(s) and len(form) - len(s) >= 3:
                gt = len(form) - len(s)
                break
        forms[form] = gt
    return forms


def fixture_median_f1(seg, forms):
    f1s = []
    for form, gt in sorted(forms.items()):
        if gt is None:
            continue
        ranked = seg.segment(form)
        pred = Segmenter.boundaries(ranked[0][1]) if ranked else []
        f1s.append(boundary_f1(pred, [gt]))
    return median_fraction(f1s), len(f1s)


# ------------------------------------------------------------ commands
def cmd_pins():
    kov_texts, kov_dev = load_kovetsky()
    ott_lines, ott_dev = load_otten()
    gm_path = KOVETSKY_DIR + "/data/gold_morphology.json"
    print("kovetsky commit (worktree HEAD recorded at freeze):",
          KOVETSKY_COMMIT)
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


def cmd_fixtureproofs(out_path):
    """TC-112-10: (a) no one-segment candidate in any top-5;
    (b) on the easy fixture the planted segmentation outscores the
    all-single-character fallback on >= 95% of planted forms;
    (c) median boundary F1 >= 0.80 on both fixtures."""
    res = {"fixture_seed": FIXTURE_SEED}
    one_piece = 0
    details = {}
    for name, builder in (("easy", build_easy_fixture),
                          ("hard", build_hard_fixture)):
        forms = builder()
        seg = Segmenter(sorted(forms.keys()))
        for form in sorted(forms.keys()):
            ranked = seg.segment(form)
            if not ranked:
                one_piece += 1
            for _, pieces in ranked:
                if len(pieces) < 2:
                    one_piece += 1
        med, n_gt = fixture_median_f1(seg, forms)
        details[name] = {"n_forms": len(forms), "n_gt_forms": n_gt,
                         "median_f1": str(med),
                         "median_f1_float": float(med),
                         "pass_c": med >= Fraction(4, 5)}
        if name == "easy":
            wins = of = 0
            for form, gt in sorted(forms.items()):
                if gt is None:
                    continue
                of += 1
                planted = (form[:gt], form[gt:])
                if seg.score(planted) > seg.score(tuple(form)):
                    wins += 1
            details[name]["planted_beats_fallback"] = {"wins": wins,
                                                       "of": of}
            details[name]["pass_b"] = Fraction(wins, of) >= Fraction(19, 20)
    res["fixtures"] = details
    res["one_piece_candidates"] = one_piece
    res["proof_a_no_one_piece"] = one_piece == 0
    res["proof_b_planted_beats_fallback"] = details["easy"]["pass_b"]
    res["proof_c_median_f1"] = details["easy"]["pass_c"] \
        and details["hard"]["pass_c"]
    res["pass"] = res["proof_a_no_one_piece"] \
        and res["proof_b_planted_beats_fallback"] \
        and res["proof_c_median_f1"]
    with open(out_path, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(res, indent=1, sort_keys=True))
    print("FIXTURE PROOFS PASS:", res["pass"])


def _grammar_summary(g):
    return {"frame": g["frame"],
            "frame_pair_coverage": g["frame_pair_coverage"],
            "anchor": g["anchor"],
            "anchor_family": g["anchor_family"],
            "marker_a": g["marker_a"],
            "marker_b": g["marker_b"],
            "paradigm_candidates": g["paradigm_candidates"],
            "paradigm_precedence": g["paradigm_precedence"],
            "filiation1_paradigm": g["filiation1_paradigm"],
            "offering_precedence": g["offering_precedence"],
            "slot_order": g["slot_order"]}


def cmd_preflight(gt_path, proofs_path, out_path):
    proofs = json.load(open(proofs_path))
    if not proofs.get("pass"):
        print("REFUSED: fixture proofs (TC-112-10) did not pass in "
              "full; the preflight does not run and the revision "
              "closes as filed")
        sys.exit(2)
    gt = json.load(open(gt_path))["ground_truth"]
    kov_forms, ott_forms = corpus_forms()
    pooled = kov_forms | ott_forms
    seg = Segmenter(pooled)
    # P-1 (scoring carried; segmenter revised)
    f1s = {}
    preds = {}
    for key, rec in sorted(gt.items()):
        form = rec["form"]
        ranked = seg.segment(form)
        pred = Segmenter.boundaries(ranked[0][1]) if ranked else []
        preds[key] = pred
        f1s[key] = boundary_f1(pred, rec["boundaries"])
    median = median_fraction(list(f1s.values()))
    p1 = {"n_forms": len(f1s), "median_f1": str(median),
          "median_f1_float": float(median),
          "per_form_f1": {k: str(v) for k, v in sorted(f1s.items())},
          "per_form_pred_boundaries": preds,
          "pass": median >= Fraction(4, 5)}
    # P-2 (comparison side carried; slot model revised)
    texts = funerary_texts()
    labeled = [(t, label_text(t)) for t in texts]
    labeled = [(t, p) for t, p in labeled if p is not None]
    g = induce_grammar(texts)
    parsed = grammar_parse_all(texts, g)
    matches = 0
    per_text = []
    for toks, present in labeled:
        _, seq = parse_text(toks, g)
        want = [s for s in TEMPLATE_ORDER if s in present]
        if seq == want:
            matches += 1
        per_text.append({
            "text_sha256": sha256_bytes(" ".join(toks).encode()),
            "label_present": sorted(present),
            "induced_sequence": seq})
    rate = Fraction(matches, len(labeled)) if labeled else Fraction(0)
    ent = parsed["slot_entropy"]
    name_max = bool(ent) and max(ent, key=lambda s: ent[s]) == "presentation"
    shuf_texts = shuffle_texts(texts)
    g_shuf = induce_grammar(shuf_texts)
    parsed_shuf = grammar_parse_all(shuf_texts, g_shuf)
    slot_ratio = (Fraction(parsed_shuf["yield"], parsed["yield"])
                  if parsed["yield"] else None)
    p2 = {"labeled_texts": len(labeled),
          "grammar": _grammar_summary(g),
          "sequence_matches": matches,
          "match_rate": str(rate), "match_rate_float": float(rate),
          "slot_entropy": ent,
          "slot_type_counts": parsed["per_slot_type_counts"],
          "per_text": per_text,
          "name_slot_is_max_entropy": name_max,
          "yield": parsed["yield"],
          "yield_by_slot": parsed["yield_by_slot"],
          "shuffle_yield": parsed_shuf["yield"],
          "shuffle_yield_by_slot": parsed_shuf["yield_by_slot"],
          "shuffle_grammar": _grammar_summary(g_shuf),
          "pass": rate >= Fraction(9, 10) and name_max}
    # P-3 (precision carried; proposals revised)
    partials = induce_partials(pooled)
    gold = gold_suffix_strings_union()
    real_supports = final_segment_supports(seg, pooled)
    null_forms = char_shuffled_forms(pooled, SEED)
    null_seg = Segmenter(null_forms)
    null_supports = final_segment_supports(null_seg, null_forms)
    tau = max((len(v) for v in null_supports.values()), default=0)
    proposals = {s: v for s, v in real_supports.items()
                 if len(v) >= tau and tau > 0}
    hits = set(proposals) & gold
    precision = (Fraction(len(hits), len(proposals))
                 if proposals else Fraction(0))
    gold_len2 = {s for s in gold if len(s) >= PART_MIN_LEN}
    recall = (Fraction(len(set(proposals) & gold_len2), len(gold_len2))
              if gold_len2 else Fraction(0))
    shuf_forms = char_shuffled_forms(pooled, SEED_SHUFFLE2)
    shuf_seg = Segmenter(shuf_forms)
    shuf_supports = final_segment_supports(shuf_seg, shuf_forms)
    shuf_proposals = {s for s, v in shuf_supports.items()
                      if len(v) >= tau and tau > 0}
    prop_ratio = (Fraction(len(shuf_proposals), len(proposals))
                  if proposals else None)
    p3 = {"induced_partials": len(partials),
          "tau_st": tau,
          "null_final_segment_supports": {s: len(v) for s, v in
                                          sorted(null_supports.items())},
          "real_final_segment_supports": {s: len(v) for s, v in
                                          sorted(real_supports.items())},
          "proposals": {s: len(v) for s, v in sorted(proposals.items())},
          "proposal_set": sorted(proposals),
          "gold_suffix_strings": len(gold),
          "gold_suffix_string_set": sorted(gold),
          "proposal_hits": len(hits),
          "precision": str(precision),
          "precision_float": float(precision),
          "recall_filed_for_transparency": str(recall),
          "shuffle_proposal_count": len(shuf_proposals),
          "shuffle_proposal_set": sorted(shuf_proposals),
          "shuffle_proposal_ratio": str(prop_ratio)
          if prop_ratio is not None else None,
          "slot_yield_real": parsed["yield"],
          "slot_yield_shuffle": parsed_shuf["yield"],
          "slot_yield_ratio": str(slot_ratio)
          if slot_ratio is not None else None,
          "pass": precision >= Fraction(4, 5)
          and prop_ratio is not None and prop_ratio <= Fraction(1, 5)
          and slot_ratio is not None and slot_ratio <= Fraction(1, 5)}
    out = {"seed": SEED, "seed_shuffle2": SEED_SHUFFLE2,
           "P-1": p1, "P-2": p2, "P-3": p3,
           "pass_in_full": bool(p1["pass"] and p2["pass"] and p3["pass"])}
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("P-1 median F1:", p1["median_f1"], "pass:", p1["pass"])
    print("P-2 match rate:", p2["match_rate"], "name-max:", name_max,
          "pass:", p2["pass"])
    print("P-3 precision:", p3["precision"], "tau:", tau,
          "proposals:", len(proposals), "pass:", p3["pass"])
    print("PASS IN FULL:", out["pass_in_full"])


def cmd_induce(verdict_path, preflight_out, out_dir, freeze_commit):
    verdict = open(verdict_path).read()
    if "PASS IN FULL" not in verdict:
        print("REFUSED: no filed full-pass preflight verdict (TC-112-04)")
        sys.exit(2)
    import os
    pf = json.load(open(preflight_out))
    kov_forms, ott_forms = corpus_forms()
    pooled = kov_forms | ott_forms
    seg = Segmenter(pooled)
    prov = {"harness_sha256": sha256_file(__file__),
            "seed": SEED, "seed_shuffle2": SEED_SHUFFLE2,
            "freeze_commit": freeze_commit,
            "pins": {"kovetsky_commit": KOVETSKY_COMMIT,
                     "inscriptions_sha256": INSCRIPTIONS_SHA256,
                     "gold_morphology_sha256": GOLD_MORPH_SHA256,
                     "otten_commit": OTTEN_COMMIT,
                     "mero_sha256": MERO_SHA256}}
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
        seg_out[form] = {"candidates": cands,
                         "margin_top1_top2": margin}
    with open(os.path.join(out_dir, "induction-segmentations-rev.json"),
              "w") as fh:
        json.dump({"provenance": prov, "forms": seg_out}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    partials = induce_partials(pooled)
    with open(os.path.join(out_dir, "induction-partials-rev.json"),
              "w") as fh:
        json.dump({"provenance": prov, "tau_st": pf["P-3"]["tau_st"],
                   "proposals": pf["P-3"]["proposals"],
                   "proposal_set": pf["P-3"]["proposal_set"],
                   "full_partial_set": partials}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    texts = funerary_texts()
    g = induce_grammar(texts)
    parsed = grammar_parse_all(texts, g)
    assignments = []
    for toks in texts:
        fillers, seq = parse_text(toks, g)
        assignments.append({
            "text_sha256": sha256_bytes(" ".join(toks).encode()),
            "tokens": toks, "sequence": seq,
            "slots": {s: xs for s, xs in fillers.items()}})
    with open(os.path.join(out_dir, "induction-slot-grammar-rev.json"),
              "w") as fh:
        json.dump({"provenance": prov, "grammar": _grammar_summary(g),
                   "yield": parsed["yield"],
                   "yield_by_slot": parsed["yield_by_slot"],
                   "slot_entropy": parsed["slot_entropy"],
                   "text_assignments": assignments}, fh,
                  indent=1, sort_keys=True)
        fh.write("\n")
    print("segmented forms:", len(seg_out))
    print("partials (full set):", len(partials),
          "proposals:", len(pf["P-3"]["proposal_set"]))
    print("funerary texts assigned:", len(assignments),
          "yield:", parsed["yield"])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pins":
        cmd_pins()
    elif cmd == "extract":
        cmd_extract(sys.argv[2])
    elif cmd == "fixtureproofs":
        cmd_fixtureproofs(sys.argv[2])
    elif cmd == "preflight":
        cmd_preflight(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "induce":
        cmd_induce(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("unknown subcommand", cmd)
        sys.exit(2)
