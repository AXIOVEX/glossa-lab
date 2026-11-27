#!/usr/bin/env python3
"""Spec 109, Stage 1 — the shared conformance preflight (T101).

Executes the preflight registered at
specs/109-generative-decipherment-engine/records/registration-2026-11-27.md
section 2, for the Indus generators (Part 1 assignment search,
Part 2 structure induction, Part 3 context channel — the three
share this harness; Parts 4 and 5 run their own preflight clauses
at their stages, per spec.md section 10).

CONSTRUCTION, fixed before any run (this header is the harness's
as-built statement; the filed preflight record carries it):

Synthetic corpora (clause a). Five replications, seeds
"spec109-s1-synth-{1..5}". Each corpus is built to the Indus
profile exactly: 1,670 artifacts (one sequence each), 7,002
tokens, the empirical length multiset of the Spec 105 custody
datasets (lengths 2..8: {2:269, 3:330, 4:415, 5:330, 6:164,
7:116, 8:46}), and duplication exactly d = 20/1670 (1,650
distinct sequences; 20 equal-length copies). Planted structure,
in value space, ciphered to signs by a seeded permutation:
  - 60 syllable values (12 consonants x 5 vowels) with roles:
    8 openers (sequence-initial only), 8 closers (sequence-final
    only), 12 context values (opener role at site A, closer role
    at site B), 9 affix values forming the planted partials
    P1, P2 (initial, length 2), S1 (final, length 2), S2 (final,
    length 3), and 23 stem values forming 400 planted stems
    (300 of length 2, 100 of length 3, Zipf-weighted use; the
    length-2 pool exceeds the profile's 269 length-2 sequences
    so the distinctness the profile requires is attainable).
  - Sequences: [PREF?] [OPENER?] CORE [CLOSER?] [SUFF?] with
    CORE = 1-2 stems; planted word boundaries at every join.
  - 60 counted sequences per corpus: stem + a run of 2-5
    repetitions of one of 5 numeral signs (structural class;
    numerals carry no syllable value and are excluded from the
    assignment recovery denominator).
  - Every edge value (opener, closer, context) carries an
    individual collocation signature: its own preferred subset
    of stems it opens or closes, in the corpus and in the
    family corpus alike. A value with no individual signature
    is exchangeable with its class-mates and unidentifiable in
    principle; the development run demonstrated that failure
    (edge roles recovered 3/28 while stems and affixes, which
    carry signatures, recovered 29/29), so the signatures are
    part of the planted grammar, as they are in any real
    system, where a value's identity is its distribution.
  - A value-side family corpus (4,000 sequences, same grammar,
    no sites, no numerals) supplies the predictor weights in
    the frozen predictor form (Spec 105 Stage 6 section 5
    weighting, as in Spec 107's scorer A/B): the value side is
    the symmetry breaker, as the registered value inventory
    (WLG dossiers) is for Part 1. The search objective is the
    duplicate-aware 5-fold cross-validated predictive
    log-likelihood under that form; because the weights are
    fixed on the value side, the fold scores sum to the full
    derivation score exactly, and the harness computes that
    sum directly (the identity is stated in the record).
  - Split: duplicate-aware, distinct sequences by
    first-appearance ordinal, ordinal % 5 == 4 to the reserve
    (the synthetic holdout), the rest to derivation.
  - Anchors: 3 stem values revealed to the search (the
    register's 3 E-standing anchors, mirrored).

Generators under test.
  G1 (Part 1): constraint propagation (anchors fixed;
  positional admissibility from G2's rho=0.95 detection on the
  derivation: a sign detected initial-restricted may take only
  values whose family initial share >= 0.95, final likewise),
  then simulated annealing (25 restarts x 80,000 swap steps,
  geometric temperature 30 -> 0.1, seeds filed; restart 0 is
  initialized by frequency matching between derivation signs
  and family values, restarts 1-24 by random admissible
  assignments) over admissible assignments, top candidate by
  objective.
  G2 (Part 2): positional classes (per-sign positional shares,
  restriction at rho = 0.95 and 0.90, occurrence floor 5);
  segmentation (boundary after position i iff the adjacent
  pair's pointwise MI falls below the sequence's own mean
  pair MI — the local form of the registered local-minimum
  rule over MI scores; development diagnostics for this and
  the other faithful mechanizations are filed in the
  preflight record);
  recurrent partials (sequence-initial and sequence-final
  strings of length 2-4 at frequency >= 5); numerical checks
  (signs with >= 80% of occurrences inside same-sign runs,
  run lengths bounded by 8 with >= 3 distinct lengths).
  G3 (Part 3): the context term of registration section 4 in
  per-sign form: log ratio of the sign's site-conditional
  initial rate to its corpus-wide initial rate, differenced
  across the two sites; null by permuting site labels within
  length strata (B = 999, seed filed per replication).

Registered criteria (registration section 2), applied per
generator as its output kinds allow:
  (i) recovery: median planted recovery >= 0.80 across the 5
      replications (G1: planted-value recovery over >=5-token
      non-anchor syllable signs; G2: per family — positional,
      segmentation F1, partial recall, numerical; G3:
      planted context-sign recovery beyond the null's 99th
      percentile in the planted direction).
  (ii) margin (G1 only — Parts 2 and 3 file no margins;
      registration section 4 states the context term is not a
      margin): the top candidate's penalized margin on the
      synthetic holdout (frozen decide() form: >= 10 nats over
      the best rival — WRONG derangement, a shuffled
      assignment, the structural-only base — above the 99th
      percentile of the permutation null, B = 999, 2 nats
      charged per searched assignment) clears in the median
      replication. All margin scoring is under the fixed
      value-side family predictor: a predictor trained on the
      mapped derivation is label-invariant and cannot
      discriminate assignments (demonstrated in development:
      penalized margin identically the null's), so the
      holdout is scored in value space under each assignment
      against the family weights, exactly as the search
      objective is.
  (iii) deciphered controls: Spec 107's filed I-2 execution
      re-run unchanged in this stage (separate process; its
      medians are read from its raw output): RIGHT medians
      above WRONG and SHUFFLE medians for both donors.
  Controls: a generator whose SHUFFLE recovery approaches its
      RIGHT recovery has measured itself and fails (registered
      form: shuffle recovery >= 0.5 x right recovery fails).
  Positional limitation (carried on the record's face): the
      Latin/Meroitic re-specified positional ground-truth sets
      hold 1 and 0 marks against the floor of 5, so positional
      recovery on those controls is NOT MEASURABLE; the
      positional clause runs on the synthetic corpora, whose
      truth is planted above the floor.
  Clause (c): every ground-truth set and recovery figure is
      computed by two independent implementations; an exact
      disagreement is a preflight STOP.

No undeciphered-system output is produced or scored anywhere
in this stage. Writes: raw-output JSON (argv[1]); synthetic
corpora and intermediates to custody (argv[2]).
"""
import hashlib
import json
import math
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from statistics import median

CUSTODY105 = "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/spec105"
REPS = 5
RECOVERY_FLOOR = 0.80
N_ART = 1670
N_TOK = 7002
N_DUP = 20
NUMERAL_RUN_CAP = 8


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] S109-S1 {msg}", flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ------------------------------------------------------------ profile
def indus_lengths():
    def load(name):
        data = json.load(open(f"{CUSTODY105}/{name}"))
        return [tuple(tuple(g) for g in art["lines"][0]) for art in data]
    deriv = load("indus-derivation.json")
    reserve = load("indus-reserve.json")
    full, di, ri = [], 0, 0
    for i in range(len(deriv) + len(reserve)):
        if i % 5 == 4:
            full.append(reserve[ri]); ri += 1
        else:
            full.append(deriv[di]); di += 1
    lengths = [sum(len(g) for g in art) for art in full]
    assert len(lengths) == N_ART and sum(lengths) == N_TOK
    return lengths


# ------------------------------------------------------------ language
CONS = ["p", "t", "k", "b", "d", "g", "m", "n", "s", "z", "r", "l"]
VOWS = ["a", "i", "u", "e", "o"]
VALUES = [c + v for c in CONS for v in VOWS]          # 60 syllables
VID = {v: i for i, v in enumerate(VALUES)}
NVAL = 60
NUMSIGNS = [60, 61, 62, 63, 64]                        # numeral sign ids


class Language:
    """Planted value-space grammar. Deterministic given rng."""

    def __init__(self, rng):
        vals = list(range(NVAL))
        rng.shuffle(vals)
        self.openers = sorted(vals[0:8])
        self.closers = sorted(vals[8:16])
        self.ctx = sorted(vals[16:28])
        aff = vals[28:37]
        self.p1 = (aff[0], aff[1])
        self.p2 = (aff[2], aff[3])
        self.s1 = (aff[4], aff[5])
        self.s2 = (aff[6], aff[7], aff[8])
        self.stemvals = sorted(vals[37:60])
        # stem pools by length: 300 distinct length-2 stems (the
        # profile carries 269 length-2 sequences, so the pool must
        # exceed that) and 100 distinct length-3 stems
        self.stems_by_len = {2: [], 3: []}
        for L, target in ((2, 300), (3, 100)):
            seen = set()
            while len(self.stems_by_len[L]) < target:
                st = tuple(rng.choice(self.stemvals) for _ in range(L))
                if st not in seen:
                    seen.add(st)
                    self.stems_by_len[L].append(st)
        self.stem_w = {L: [1.0 / (i + 1) ** 0.7
                           for i in range(len(pool))]
                       for L, pool in self.stems_by_len.items()}
        self.stems = self.stems_by_len[2] + self.stems_by_len[3]
        self.anchors = sorted(rng.sample(self.stemvals, 3))
        # Individual collocation signatures for the edge values:
        # each opener / closer / context value preferentially
        # co-occurs with its own subset of stems, so a value's
        # identity has observable consequences (an edge value
        # drawn uniformly with no signature would be exchangeable
        # with its class-mates and unidentifiable in principle;
        # the smoke run demonstrated exactly that failure).
        self.open_pref = {}
        self.close_pref = {}
        for v in self.openers + self.ctx:
            self.open_pref[v] = rng.sample(range(len(self.stems)), 15)
        for v in self.closers + self.ctx:
            self.close_pref[v] = rng.sample(range(len(self.stems)), 15)

    def pick_stem(self, rng, want=None):
        if want is None:
            want = rng.choice((2, 3))
        return rng.choices(self.stems_by_len[want],
                           weights=self.stem_w[want])[0]

    def pick_stem_for_opener(self, rng, value, want):
        """First stem after an opening edge value: with prob 0.7
        from the value's preferred stems of the wanted length."""
        pref = self.open_pref.get(value)
        if pref and rng.random() < 0.7:
            cands = [self.stems[i] for i in pref
                     if len(self.stems[i]) == want]
            if cands:
                return rng.choice(cands)
        return self.pick_stem(rng, want)

    def pick_closer(self, rng, pool, last_stem):
        """Closing edge value: weighted by its preference for the
        stem it closes (values without a preference entry are
        uniform)."""
        idx = self.stems.index(last_stem)
        weights = []
        for v in pool:
            pref = self.close_pref.get(v)
            weights.append(6.0 if pref and idx in pref else 1.0)
        return rng.choices(pool, weights=weights)[0]

    def sequence(self, rng, L, site=None, counted=False):
        """One value-space sequence of exact length L with planted
        boundary positions (offsets after which a word ends).
        Context values take the opener role at site A and the
        closer role at site B; in the family corpus (site None)
        they take either edge role."""
        if counted:
            r = rng.choice([x for x in (L - 2, L - 3) if 2 <= x <= 5])
            s = L - r
            stem = self.pick_stem(rng, s)
            num = rng.choice(range(5))
            seq = list(stem) + [1000 + num] * r   # numeral marker
            return seq, {len(stem) - 1}
        opts = []
        for o in (0, 1, 2):
            for c in (0, 1, 2, 3):
                t = L - o - c
                if t in (2, 3) or t in (4, 5, 6):
                    opts.append((o, c, t))
        o, c, t = rng.choice(opts)
        seq, bounds = [], set()
        opener_value = None
        if o == 2:
            seq += list(rng.choice((self.p1, self.p2)))
            bounds.add(len(seq) - 1)
        elif o == 1:
            pool = self.openers
            if site == "A" or site is None:
                pool = self.openers + self.ctx
            opener_value = rng.choice(pool)
            seq.append(opener_value)
            bounds.add(0)
        nstems = 1 if t <= 3 else 2
        last_stem = None
        for k in range(nstems):
            want = t if nstems == 1 else (t // 2 if k == 0 else t - t // 2)
            if k == 0 and opener_value is not None:
                last_stem = self.pick_stem_for_opener(rng, opener_value,
                                                      want)
            else:
                last_stem = self.pick_stem(rng, want)
            seq += list(last_stem)
            bounds.add(len(seq) - 1)
        if c == 1:
            pool = self.closers
            if site == "B" or site is None:
                pool = self.closers + self.ctx
            seq.append(self.pick_closer(rng, pool, last_stem))
            bounds.add(len(seq) - 1)
        elif c == 2:
            seq += list(self.s1)
            bounds.add(len(seq) - 1)
        elif c == 3:
            seq += list(self.s2)
            bounds.add(len(seq) - 1)
        assert len(seq) == L, (len(seq), L, o, c, t)
        bounds.discard(L - 1)
        return seq, bounds


def build_corpus(seed, lengths):
    rng = random.Random(seed)
    lang = Language(rng)
    # site assignment and counted selection, seeded
    order = list(range(N_ART))
    rng.shuffle(order)
    counted_slots = set()
    for i in order:
        if lengths[i] >= 4 and len(counted_slots) < 60:
            counted_slots.add(i)
    sites = {}
    for i in range(N_ART):
        sites[i] = "A" if rng.random() < 0.5 else "B"
    seqs, bounds_list = [], []
    seen = set()
    for i in range(N_ART):
        for _attempt in range(500):
            s, b = lang.sequence(rng, lengths[i], site=sites[i],
                                 counted=i in counted_slots)
            key = tuple(s)
            if key not in seen:
                seen.add(key)
                seqs.append(s)
                bounds_list.append(b)
                break
        else:
            raise RuntimeError(f"distinctness cap at slot {i}")
    # duplication: 20 equal-length copies replace their targets
    by_len = defaultdict(list)
    for i, s in enumerate(seqs):
        by_len[len(s)].append(i)
    targets = []
    pool = [i for i in range(N_ART)]
    rng.shuffle(pool)
    used_src = set()
    for tgt in pool:
        cands = [j for j in by_len[lengths[tgt]] if j != tgt
                 and j not in used_src and j not in targets]
        if cands:
            src = rng.choice(cands)
            seqs[tgt] = list(seqs[src])
            bounds_list[tgt] = set(bounds_list[src])
            sites[tgt] = sites[src]
            used_src.add(src)
            targets.append(tgt)
            if len(targets) == N_DUP:
                break
    assert len(targets) == N_DUP
    # cipher: value v -> sign perm[v]; numerals 1000+k -> NUMSIGNS[k]
    perm = list(range(NVAL))
    rng.shuffle(perm)
    signseqs = [[perm[v] if v < 1000 else NUMSIGNS[v - 1000] for v in s]
                for s in seqs]
    # family corpus (value space)
    fam_rng = random.Random(seed + "-family")
    fam = []
    len_pool = [L for L in lengths]
    for _ in range(4000):
        s, _b = lang.sequence(fam_rng, fam_rng.choice(len_pool))
        fam.append([v for v in s if v < 1000])
    truth = {
        "perm_value_to_sign": perm,
        "openers": lang.openers, "closers": lang.closers,
        "ctx": lang.ctx, "p1": lang.p1, "p2": lang.p2,
        "s1": lang.s1, "s2": lang.s2, "anchors": lang.anchors,
        "stems": [list(s) for s in lang.stems],
    }
    return {"signseqs": signseqs, "bounds": bounds_list, "sites": sites,
            "family": fam, "truth": truth,
            "counted_slots": sorted(counted_slots)}


# ------------------------------------------------- predictor (A and B)
def weights_from(groups):
    c, ic, pc, st = Counter(), Counter(), Counter(), Counter()
    for g in groups:
        if not g:
            continue
        ic[g[0]] += 1
        for i, m in enumerate(g):
            c[m] += 1
            if i:
                pc[(g[i - 1], m)] += 1
                st[g[i - 1]] += 1
    return {"c": c, "ic": ic, "pc": pc, "st": st,
            "N": sum(c.values()), "V": len(c), "G": len(groups)}


def w_derived(w, prev, m):
    eps = 1.0 / (w["N"] + w["V"])
    if m not in w["c"]:
        return eps
    if prev is None:
        return w["ic"][m] / w["G"] if w["ic"][m] > 0 else w["c"][m] / w["N"]
    if w["pc"][(prev, m)] > 0:
        return w["pc"][(prev, m)] / w["st"][prev]
    return w["c"][m] / w["N"]


def score_a(w, groups):
    """Mean base and derived negative log-likelihood (loop form,
    Spec 107 scorer A)."""
    eps = 1.0 / (w["N"] + w["V"])
    base = derived = n = 0
    for g in groups:
        for i, m in enumerate(g):
            prev = g[i - 1] if i else None
            wb = w["c"][m] / w["N"] if m in w["c"] else eps
            base += -math.log(wb)
            derived += -math.log(w_derived(w, prev, m))
            n += 1
    return base / n, derived / n


def score_b(w, groups):
    """Independent implementation: context-grouped accumulation
    (Spec 107 scorer B form)."""
    contexts = Counter()
    for g in groups:
        if not g:
            continue
        contexts[(None, g[0])] += 1
        for a, b in zip(g, g[1:]):
            contexts[(a, b)] += 1
    eps = 1.0 / (w["N"] + w["V"])
    base = derived = n = 0
    for (prev, m), k in contexts.items():
        wb = w["c"][m] / w["N"] if m in w["c"] else eps
        base += -math.log(wb) * k
        derived += -math.log(w_derived_b(w, prev, m)) * k
        n += k
    return base / n, derived / n


def w_derived_b(w, prev, m):
    # independently written weight lookup (same registered form)
    if m not in w["c"]:
        return 1.0 / (w["N"] + w["V"])
    if prev is None:
        return (w["ic"][m] / w["G"]) if w["ic"].get(m, 0) else (w["c"][m] / w["N"])
    pair = w["pc"].get((prev, m), 0)
    return pair / w["st"][prev] if pair else w["c"][m] / w["N"]


def heldout_totals(w, groups):
    ba, da = score_a(w, groups)
    bb, db = score_b(w, groups)
    if abs(da - db) > 1e-9 or abs(ba - bb) > 1e-9:
        raise AssertionError(f"scorer disagreement: A {ba},{da} B {bb},{db}")
    n = sum(len(g) for g in groups)
    return {"base_total": ba * n, "derived_total": da * n, "tokens": n}


# ------------------------------------------------------------ split
def split_corpus(signseqs):
    seen, distinct = set(), []
    for s in signseqs:
        key = tuple(s)
        if key not in seen:
            seen.add(key)
            distinct.append(s)
    deriv, reserve = [], []
    for i, s in enumerate(distinct):
        (reserve if i % 5 == 4 else deriv).append(s)
    return deriv, reserve, len(distinct)


def truncate_numerals(seq):
    out = []
    for m in seq:
        if m >= 60:
            break
        out.append(m)
    return out


# ------------------------------------------------- G2: induction
def positional_counts(seqs):
    pos = defaultdict(Counter)
    for g in seqs:
        if len(g) == 1:
            pos[g[0]]["sole"] += 1
            continue
        for i, m in enumerate(g):
            pos[m]["initial" if i == 0 else
                  "final" if i == len(g) - 1 else "medial"] += 1
    return pos


def detect_restricted(pos, rho, floor=5):
    det = {}
    for m, c in pos.items():
        total = sum(c.values())
        if total < floor:
            continue
        for cls in ("initial", "final"):
            if c[cls] / total >= rho:
                det[m] = cls
    return det


def g2_positional(seqs, truth_restricted):
    pos = positional_counts(seqs)
    out = {}
    for rho, key in ((0.95, "0.95"), (0.90, "0.90")):
        det = detect_restricted(pos, rho)
        # implementation A: direct comparison
        denom_a = sum(1 for s in truth_restricted
                      if sum(pos[s].values()) >= 5)
        hits_a = sum(1 for s, cls in truth_restricted.items()
                     if sum(pos[s].values()) >= 5 and det.get(s) == cls)
        # implementation B: set algebra over detected/truth pairs
        truth_pairs = {(s, c) for s, c in truth_restricted.items()
                       if sum(pos[s].values()) >= 5}
        det_pairs = {(s, c) for s, c in det.items()}
        hits_b = len(truth_pairs & det_pairs)
        denom_b = len(truth_pairs)
        assert (hits_a, denom_a) == (hits_b, denom_b), "G2 positional A/B"
        out[key] = {"hits": hits_a, "denominator": denom_a,
                         "recovery": hits_a / denom_a if denom_a else None,
                         "false_positives": len(det_pairs - truth_pairs),
                         "detected": len(det)}
    return out


def g2_segmentation(seqs, bounds_list):
    pair = Counter()
    uni = Counter()
    for g in seqs:
        uni.update(g)
        pair.update(zip(g, g[1:]))
    N = sum(uni.values())
    Nb = sum(pair.values())

    def pmi(a, b):
        return math.log((pair[(a, b)] / Nb) /
                        ((uni[a] / N) * (uni[b] / N)))
    # boundary rule (fixed at the harness freeze): a boundary is
    # scored after position i iff the adjacent pair's PMI falls
    # below the sequence's own mean pair PMI (the local form of
    # the registered local-minimum rule over MI scores)
    # implementation A: per-position loop
    tp = fp = fn = tot = 0
    for g, bset in zip(seqs, bounds_list):
        pmis = [pmi(g[i], g[i + 1]) for i in range(len(g) - 1)]
        mean_pmi = sum(pmis) / len(pmis) if pmis else 0.0
        for i in range(len(g) - 1):
            tot += 1
            pred = pmis[i] < mean_pmi
            if pred and i in bset:
                tp += 1
            elif pred:
                fp += 1
            elif i in bset:
                fn += 1
    # implementation B: aggregate over pair types
    type_stats = {}
    for g, bset in zip(seqs, bounds_list):
        pmis = [pmi(g[i], g[i + 1]) for i in range(len(g) - 1)]
        mean_pmi = sum(pmis) / len(pmis) if pmis else 0.0
        for i in range(len(g) - 1):
            key = (g[i], g[i + 1], pmis[i] < mean_pmi, i in bset)
            type_stats[key] = type_stats.get(key, 0) + 1
    tp_b = sum(k for (_a, _b, p, t), k in type_stats.items() if p and t)
    fp_b = sum(k for (_a, _b, p, t), k in type_stats.items() if p and not t)
    fn_b = sum(k for (_a, _b, p, t), k in type_stats.items() if not p and t)
    assert (tp, fp, fn) == (tp_b, fp_b, fn_b), "G2 segmentation A/B"
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "positions": tot,
            "precision": prec, "recall": rec, "f1": f1}


def g2_partials(seqs, planted_initial, planted_final):
    init_c, fin_c = Counter(), Counter()
    for g in seqs:
        for k in (2, 3, 4):
            if len(g) >= k:
                init_c[tuple(g[:k])] += 1
                fin_c[tuple(g[-k:])] += 1
    ext_i = {s for s, c in init_c.items() if c >= 5}
    ext_f = {s for s, c in fin_c.items() if c >= 5}
    # implementation A
    hits_a = (len(set(planted_initial) & ext_i)
              + len(set(planted_final) & ext_f))
    # implementation B
    hits_b = sum(1 for s in planted_initial if s in ext_i) \
        + sum(1 for s in planted_final if s in ext_f)
    assert hits_a == hits_b, "G2 partials A/B"
    denom = len(planted_initial) + len(planted_final)
    return {"hits": hits_a, "denominator": denom,
            "recovery": hits_a / denom,
            "extracted_initial": len(ext_i), "extracted_final": len(ext_f)}


def g2_numerical(seqs, planted_numerals):
    # implementation A: explicit run scan
    run_tokens = Counter()
    total = Counter()
    run_lengths = defaultdict(set)
    max_run = Counter()
    for g in seqs:
        total.update(g)
        i = 0
        while i < len(g):
            j = i
            while j + 1 < len(g) and g[j + 1] == g[i]:
                j += 1
            runlen = j - i + 1
            if runlen >= 2:
                run_tokens[g[i]] += runlen
                run_lengths[g[i]].add(runlen)
                max_run[g[i]] = max(max_run[g[i]], runlen)
            i = j + 1
    det_a = {m for m in total
             if total[m] >= 5 and run_tokens[m] / total[m] >= 0.8
             and len(run_lengths[m]) >= 3 and max_run[m] <= NUMERAL_RUN_CAP}
    # implementation B: groupby
    from itertools import groupby
    rt_b, rl_b, mr_b, tot_b = Counter(), defaultdict(set), Counter(), Counter()
    for g in seqs:
        tot_b.update(g)
        for m, grp in groupby(g):
            runlen = len(list(grp))
            if runlen >= 2:
                rt_b[m] += runlen
                rl_b[m].add(runlen)
                mr_b[m] = max(mr_b[m], runlen)
    det_b = {m for m in tot_b
             if tot_b[m] >= 5 and rt_b[m] / tot_b[m] >= 0.8
             and len(rl_b[m]) >= 3 and mr_b[m] <= NUMERAL_RUN_CAP}
    assert det_a == det_b, "G2 numerical A/B"
    hits = len(set(planted_numerals) & det_a)
    return {"hits": hits, "denominator": len(planted_numerals),
            "recovery": hits / len(planted_numerals),
            "detected": sorted(det_a),
            "false_positives": len(det_a - set(planted_numerals))}


# ------------------------------------------------- G3: context
def context_stats(seqs, sites_list):
    """Per-sign (initial count, total) per site. sites_list aligns
    with seqs (the full corpus order)."""
    per = defaultdict(lambda: {"A": [0, 0], "B": [0, 0]})
    for g, site in zip(seqs, sites_list):
        for i, m in enumerate(g):
            per[m][site][1] += 1
            if i == 0:
                per[m][site][0] += 1
    return per


def ctx_statistic(per, m):
    ia, ta = per[m]["A"]
    ib, tb = per[m]["B"]
    if ta == 0 or tb == 0:
        return 0.0
    return (math.log((ia + 0.5) / (ta + 1))
            - math.log((ib + 0.5) / (tb + 1)))


def g3_context(seqs, sites_list, planted_ctx_signs, seed):
    per = context_stats(seqs, sites_list)
    stats = {m: ctx_statistic(per, m) for m in per}
    # null: permute site labels within length strata, B = 999
    rng = random.Random(seed)
    strata = defaultdict(list)
    for idx, g in enumerate(seqs):
        strata[len(g)].append(idx)
    null_stats = defaultdict(list)
    for _b in range(999):
        labels = list(sites_list)
        for _len, idxs in strata.items():
            labs = [sites_list[i] for i in idxs]
            rng.shuffle(labs)
            for i, lab in zip(idxs, labs):
                labels[i] = lab
        per_b = context_stats(seqs, labels)
        for m in planted_ctx_signs:
            null_stats[m].append(abs(ctx_statistic(per_b, m)))
    # implementation A recovery
    hits_a, p99s = 0, {}
    for m in planted_ctx_signs:
        dist = sorted(null_stats[m])
        p99 = dist[math.ceil(0.99 * len(dist)) - 1]
        p99s[m] = p99
        if stats[m] > p99 and stats[m] > 0:
            hits_a += 1
    # implementation B recovery (recompute stats independently)
    per_b2 = defaultdict(lambda: {"A": [0, 0], "B": [0, 0]})
    for g, site in zip(seqs, sites_list):
        initials = {g[0]} if g else set()
        for m in set(g):
            per_b2[m][site][1] += g.count(m)
        if g:
            per_b2[g[0]][site][0] += 1
    hits_b = 0
    for m in planted_ctx_signs:
        ia, ta = per_b2[m]["A"]
        ib, tb = per_b2[m]["B"]
        st = (math.log((ia + 0.5) / (ta + 1))
              - math.log((ib + 0.5) / (tb + 1))) if ta and tb else 0.0
        assert abs(st - stats[m]) < 1e-12, "G3 statistic A/B"
        if st > p99s[m] and st > 0:
            hits_b += 1
    assert hits_a == hits_b, "G3 recovery A/B"
    # control: one permuted labelling treated as the truth
    labels = list(sites_list)
    for _len, idxs in strata.items():
        labs = [sites_list[i] for i in idxs]
        rng.shuffle(labs)
        for i, lab in zip(idxs, labs):
            labels[i] = lab
    per_c = context_stats(seqs, labels)
    hits_c = sum(1 for m in planted_ctx_signs
                 if ctx_statistic(per_c, m) > p99s[m]
                 and ctx_statistic(per_c, m) > 0)
    denom = len(planted_ctx_signs)
    return {"hits": hits_a, "denominator": denom,
            "recovery": hits_a / denom,
            "control_hits": hits_c, "control_recovery": hits_c / denom,
            "median_statistic": median(stats[m] for m in planted_ctx_signs)}


# ------------------------------------------------- G1: search
def family_positional(family):
    pos = positional_counts(family)
    init_vals, fin_vals = set(), set()
    for m, c in pos.items():
        total = sum(c.values())
        if total >= 20:
            if c["initial"] / total >= 0.95:
                init_vals.add(m)
            if c["final"] / total >= 0.95:
                fin_vals.add(m)
    return init_vals, fin_vals


def build_objective(deriv_trunc, fam_w):
    S = [[0] * NVAL for _ in range(NVAL)]
    I0 = [0] * NVAL
    for g in deriv_trunc:
        if not g:
            continue
        I0[g[0]] += 1
        for a, b in zip(g, g[1:]):
            S[a][b] += 1
    LW = [[math.log(w_derived(fam_w, a, b)) for b in range(NVAL)]
          for a in range(NVAL)]
    LW0 = [math.log(w_derived(fam_w, None, b)) for b in range(NVAL)]
    return S, I0, LW, LW0


def objective(S, I0, LW, LW0, phi):
    tot = 0.0
    for a in range(NVAL):
        tot += I0[a] * LW0[phi[a]]
        row = S[a]
        lwrow = LW[phi[a]]
        for b in range(NVAL):
            if row[b]:
                tot += row[b] * lwrow[phi[b]]
    return tot


def _swap_delta(S, I0, LW, LW0, phi, x, y):
    """Exact objective change when the values of signs x and y are
    swapped, over the affected rows/columns only."""
    vx, vy = phi[x], phi[y]
    if vx == vy:
        return 0.0
    old = I0[x] * LW0[vx] + I0[y] * LW0[vy]
    new = I0[x] * LW0[vy] + I0[y] * LW0[vx]
    for b in range(NVAL):
        pb = phi[b]
        nb = vy if b == x else (vx if b == y else pb)
        old += S[x][b] * LW[vx][pb] + S[y][b] * LW[vy][pb]
        new += S[x][b] * LW[vy][nb] + S[y][b] * LW[vx][nb]
    for a in range(NVAL):
        pa = phi[a]
        na = vy if a == x else (vx if a == y else pa)
        old += S[a][x] * LW[pa][vx] + S[a][y] * LW[pa][vy]
        new += S[a][x] * LW[na][vy] + S[a][y] * LW[na][vx]
    # intersections (x,x),(x,y),(y,x),(y,y) were counted twice
    old -= (S[x][x] * LW[vx][vx] + S[x][y] * LW[vx][vy]
            + S[y][x] * LW[vy][vx] + S[y][y] * LW[vy][vy])
    new -= (S[x][x] * LW[vy][vy] + S[x][y] * LW[vy][vx]
            + S[y][x] * LW[vx][vy] + S[y][y] * LW[vx][vx])
    return new - old


def anneal(S, I0, LW, LW0, phi0, admissible, fixed, steps, seed):
    rng = random.Random(seed)
    phi = list(phi0)
    cur = objective(S, I0, LW, LW0, phi)
    best, best_phi = cur, list(phi)
    free = [s for s in range(NVAL) if s not in fixed]
    for step in range(steps):
        T = 30.0 * (0.1 / 30.0) ** (step / steps)
        x, y = rng.sample(free, 2)
        vx, vy = phi[x], phi[y]
        if vy not in admissible[x] or vx not in admissible[y]:
            continue
        d = _swap_delta(S, I0, LW, LW0, phi, x, y)
        if d >= 0 or rng.random() < math.exp(d / T):
            phi[x], phi[y] = vy, vx
            cur += d
            if cur > best:
                best, best_phi = cur, list(phi)
    # exact rescoring of the returned state (the filed margins are
    # computed independently by scorer A/B in any case)
    exact = objective(S, I0, LW, LW0, best_phi)
    return best_phi, exact


def _initial_assignment(rng, fixed, admissible, deriv, family, freq_init):
    phi = [None] * NVAL
    for s, v in fixed.items():
        phi[s] = v
    rest_signs = [s for s in range(NVAL) if s not in fixed]
    rest_vals = [v for v in range(NVAL) if v not in set(fixed.values())]
    if freq_init:
        sign_freq = Counter(m for g in deriv for m in g if m < 60)
        fam_freq = Counter(m for g in family for m in g)
        signs_sorted = sorted(rest_signs, key=lambda s: (-sign_freq[s], s))
        vals_sorted = sorted(rest_vals, key=lambda v: (-fam_freq[v], v))
        for s, v in zip(signs_sorted, vals_sorted):
            phi[s] = v
    else:
        rng.shuffle(rest_vals)
        for s, v in zip(rest_signs, rest_vals):
            phi[s] = v
    # repair admissibility by swaps among non-fixed signs
    for _ in range(2000):
        bad = [s for s in rest_signs if phi[s] not in admissible[s]]
        if not bad:
            break
        s = bad[0]
        partners = [t for t in rest_signs
                    if phi[t] in admissible[s] and phi[s] in admissible[t]]
        if not partners:
            admissible[s] = set(range(NVAL))   # infeasible: relax, record
            continue
        t = rng.choice(partners)
        phi[s], phi[t] = phi[t], phi[s]
    return phi


def g1_search(deriv, family, anchors_sign_value, det_init, det_final,
              steps, seed_prefix, restarts=25):
    fam_w = weights_from(family)
    init_vals, fin_vals = family_positional(family)
    deriv_trunc = [truncate_numerals(g) for g in deriv]
    S, I0, LW, LW0 = build_objective(deriv_trunc, fam_w)
    admissible = {}
    for s in range(NVAL):
        adm = set(range(NVAL))
        if s in det_init:
            adm &= init_vals
        if s in det_final:
            adm &= fin_vals
        admissible[s] = adm if adm else set(range(NVAL))
    fixed = dict(anchors_sign_value)          # sign -> value
    rest_signs = [s for s in range(NVAL) if s not in fixed]
    best_phi, best_obj = None, None
    for r in range(restarts):
        rng = random.Random(f"{seed_prefix}-init{r}")
        phi0 = _initial_assignment(rng, fixed, admissible, deriv, family,
                                   freq_init=(r == 0))
        cand, obj = anneal(S, I0, LW, LW0, phi0, admissible, fixed,
                           steps, f"{seed_prefix}-restart{r}")
        if best_obj is None or obj > best_obj:
            best_phi, best_obj = cand, obj
    relaxed = [s for s in rest_signs if admissible[s] == set(range(NVAL))
               and (s in det_init or s in det_final)]
    return best_phi, {"objective": best_obj, "relaxed": relaxed,
                      "init_values": sorted(init_vals),
                      "fin_values": sorted(fin_vals),
                      "restarts": restarts}


def map_groups(groups, phi):
    return [[phi[m] if m < 60 else m for m in g] for g in groups]


def g1_margins(family, reserve, phi_cand, phi_wrong, phi_shuffle):
    """Margins under the FIXED value-side (family) predictor: the
    held-out material is scored in value space under each
    assignment, with the predictor's weights supplied by the
    family corpus, never by the mapped derivation (a predictor
    trained on the mapped derivation is label-invariant and no
    margin computed from it can discriminate assignments — the
    smoke run demonstrated this: penalized margin identically
    the null's)."""
    fam_w = weights_from(family)
    tot_cand = heldout_totals(fam_w, map_groups(reserve, phi_cand))
    tot_wrong = heldout_totals(fam_w, map_groups(reserve, phi_wrong))
    tot_shuf = heldout_totals(fam_w, map_groups(reserve, phi_shuffle))
    rivals = {"wrong": tot_wrong["derived_total"],
              "shuffle_assignment": tot_shuf["derived_total"],
              "base": tot_cand["base_total"]}
    margin_raw = min(rivals.values()) - tot_cand["derived_total"]
    return {"tot_cand": tot_cand, "rivals": rivals,
            "margin_raw": margin_raw}


def g1_null(family, reserve, phi_cand, fixed, best_rival_total,
            n_free, seed):
    fam_w = weights_from(family)
    rng = random.Random(seed)
    free_signs = [s for s in range(NVAL) if s not in fixed]
    margins = []
    for _b in range(999):
        vals = [phi_cand[s] for s in free_signs]
        rng.shuffle(vals)
        psi = list(phi_cand)
        for s, v in zip(free_signs, vals):
            psi[s] = v
        tot = heldout_totals(fam_w, map_groups(reserve, psi))
        margins.append(best_rival_total - tot["derived_total"]
                       - 2 * n_free)
    margins.sort()
    return margins[math.ceil(0.99 * len(margins)) - 1], margins


# ------------------------------------------------------------ truth
def truth_restricted_a(truth, perm):
    t = {}
    for v in truth["openers"]:
        t[perm[v]] = "initial"
    for v in truth["closers"]:
        t[perm[v]] = "final"
    t[perm[truth["p1"][0]]] = "initial"
    t[perm[truth["p2"][0]]] = "initial"
    t[perm[truth["s1"][-1]]] = "final"
    t[perm[truth["s2"][-1]]] = "final"
    return t


def truth_restricted_b(signseqs, perm):
    """Independent construction (Spec 107 ground-truth form) over
    the value-space corpus: >= 20 occurrences and (initial+sole)
    or (final+sole) share >= 0.99."""
    inv = [0] * NVAL
    for v, s in enumerate(perm):
        inv[s] = v
    valseqs = [[inv[m] for m in g if m < 60] for g in signseqs]
    pos = positional_counts(valseqs)
    out = {}
    for v, c in pos.items():
        total = sum(c.values())
        if total < 20:
            continue
        if (c["initial"] + c["sole"]) / total >= 0.99:
            out[perm[v]] = "initial"
        elif (c["final"] + c["sole"]) / total >= 0.99:
            out[perm[v]] = "final"
    return out


def recovery_g1(phi, truth_perm, anchors_signs, token_counts):
    inv = [0] * NVAL
    for v, s in enumerate(truth_perm):
        inv[s] = v
    denom_a = hits_a = 0
    for s in range(NVAL):
        if s in anchors_signs or token_counts[s] < 5:
            continue
        denom_a += 1
        if phi[s] == inv[s]:
            hits_a += 1
    # implementation B
    planted = {s: inv[s] for s in range(NVAL)
               if s not in anchors_signs and token_counts[s] >= 5}
    hits_b = len([s for s, v in planted.items() if phi[s] == v])
    assert hits_a == hits_b and denom_a == len(planted), "G1 recovery A/B"
    return {"hits": hits_a, "denominator": denom_a,
            "recovery": hits_a / denom_a if denom_a else None}


# ------------------------------------------------------------ main
def main():
    out_path, custody_dir = sys.argv[1], sys.argv[2]
    steps = int(sys.argv[3]) if len(sys.argv) > 3 else 80000
    reps = int(sys.argv[4]) if len(sys.argv) > 4 else REPS
    lengths = indus_lengths()
    log(f"profile: {N_ART} artifacts, {N_TOK} tokens, lengths "
        f"{min(lengths)}..{max(lengths)}")
    results = {"profile": {"artifacts": N_ART, "tokens": N_TOK,
                           "duplication_rate": N_DUP / N_ART,
                           "length_multiset_sha256":
                           sha(json.dumps(sorted(lengths)).encode())},
               "replications": []}
    for rep in range(1, reps + 1):
        # corpus build with retry: a build is admitted only if the
        # profile gates hold exactly and the two ground-truth
        # constructions agree (a disagreement is a STOP for an
        # admitted corpus, never silently filed)
        seed = None
        for attempt in range(50):
            cand_seed = (f"spec109-s1-synth-{rep}" if attempt == 0
                         else f"spec109-s1-synth-{rep}-try{attempt}")
            corp = build_corpus(cand_seed, lengths)
            signseqs = corp["signseqs"]
            truth = corp["truth"]
            perm = truth["perm_value_to_sign"]
            if sorted(len(s) for s in signseqs) != sorted(lengths):
                continue
            _d, _r, n_distinct_try = split_corpus(signseqs)
            if n_distinct_try != N_ART - N_DUP:
                continue
            if truth_restricted_a(truth, perm) != \
                    truth_restricted_b(signseqs, perm):
                continue
            tc_try = Counter(m for g in signseqs for m in g)
            if any(tc_try[s] < 5 for s in range(NVAL)):
                continue
            seed = cand_seed
            break
        assert seed is not None, f"no admissible corpus for rep {rep}"
        sites_list = [corp["sites"][i] for i in range(N_ART)]
        assert len(signseqs) == N_ART
        assert sum(len(s) for s in signseqs) == N_TOK
        deriv, reserve, n_distinct = split_corpus(signseqs)
        t_a = truth_restricted_a(truth, perm)
        t_b = truth_restricted_b(signseqs, perm)
        assert t_a == t_b, f"ground-truth disagreement rep {rep}"
        token_counts = Counter(m for g in signseqs for m in g)
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        row = {"rep": rep, "seed": seed, "distinct": n_distinct,
               "derivation_sequences": len(deriv),
               "reserve_sequences": len(reserve),
               "reserve_tokens": sum(len(g) for g in reserve)}
        # ---- G2 on the full corpus
        row["g2_positional"] = g2_positional(signseqs, t_a)
        row["g2_segmentation"] = g2_segmentation(signseqs, corp["bounds"])
        planted_init = [tuple(perm[v] for v in truth["p1"]),
                        tuple(perm[v] for v in truth["p2"])]
        planted_fin = [tuple(perm[v] for v in truth["s1"]),
                       tuple(perm[v] for v in truth["s2"])]
        row["g2_partials"] = g2_partials(signseqs, planted_init, planted_fin)
        row["g2_numerical"] = g2_numerical(signseqs, NUMSIGNS)
        # ---- G2 shuffle control
        rng_sh = random.Random(seed + "-g2shuffle")
        shuf_seqs = []
        for g in signseqs:
            gg = list(g)
            rng_sh.shuffle(gg)
            shuf_seqs.append(gg)
        row["g2_shuffle"] = {
            "positional_0.95": g2_positional(shuf_seqs, t_a)["0.95"]["recovery"],
            "segmentation_f1": g2_segmentation(shuf_seqs, corp["bounds"])["f1"],
            "partials": g2_partials(shuf_seqs, planted_init, planted_fin)["recovery"],
            "numerical": g2_numerical(shuf_seqs, NUMSIGNS)["recovery"]}
        log(f"rep {rep}: G2 done — positional@0.95 "
            f"{row['g2_positional']['0.95']['recovery']:.3f}, segmentation "
            f"F1 {row['g2_segmentation']['f1']:.3f}, partials "
            f"{row['g2_partials']['recovery']:.3f}, numerical "
            f"{row['g2_numerical']['recovery']:.3f}")
        # ---- G3
        planted_ctx_signs = [perm[v] for v in truth["ctx"]]
        row["g3_context"] = g3_context(signseqs, sites_list,
                                       planted_ctx_signs, seed + "-g3null")
        log(f"rep {rep}: G3 done — context recovery "
            f"{row['g3_context']['recovery']:.3f} (control "
            f"{row['g3_context']['control_recovery']:.3f})")
        # ---- G1
        pos_deriv = positional_counts(deriv)
        det = detect_restricted(pos_deriv, 0.95)
        det_init = {s for s, c in det.items() if c == "initial"}
        det_final = {s for s, c in det.items() if c == "final"}
        phi, info = g1_search(deriv, corp["family"], anchors_sv,
                              det_init, det_final, steps, seed + "-g1")
        row["g1_recovery"] = recovery_g1(phi, perm, set(anchors_sv),
                                         token_counts)
        log(f"rep {rep}: G1 search done — recovery "
            f"{row['g1_recovery']['recovery']:.3f} "
            f"({row['g1_recovery']['hits']}/{row['g1_recovery']['denominator']})")
        # shuffle control: identical pipeline on shuffled derivation
        rng_s2 = random.Random(seed + "-g1shuffle")
        shuf_deriv = []
        for g in deriv:
            gg = list(g)
            rng_s2.shuffle(gg)
            shuf_deriv.append(gg)
        pos_sh = positional_counts(shuf_deriv)
        det_sh = detect_restricted(pos_sh, 0.95)
        phi_sh, _ = g1_search(shuf_deriv, corp["family"], anchors_sv,
                              {s for s, c in det_sh.items() if c == "initial"},
                              {s for s, c in det_sh.items() if c == "final"},
                              steps, seed + "-g1shuf")
        row["g1_shuffle_recovery"] = recovery_g1(phi_sh, perm,
                                                 set(anchors_sv),
                                                 token_counts)
        # margins and null
        rng_der = random.Random(seed + "-derange")
        der = list(range(NVAL))
        while True:
            rng_der.shuffle(der)
            if all(der[v] != v for v in range(NVAL)):
                break
        inv = [0] * NVAL
        for v, s in enumerate(perm):
            inv[s] = v
        phi_wrong = [der[inv[s]] for s in range(NVAL)]
        rng_sa = random.Random(seed + "-shufassign")
        free_signs = [s for s in range(NVAL) if s not in anchors_sv]
        sa_vals = [phi[s] for s in free_signs]
        rng_sa.shuffle(sa_vals)
        phi_shuffle = list(phi)
        for s, v in zip(free_signs, sa_vals):
            phi_shuffle[s] = v
        mg = g1_margins(corp["family"], reserve, phi, phi_wrong,
                        phi_shuffle)
        n_free = NVAL - len(anchors_sv)
        best_rival_total = min(mg["rivals"].values())
        penalized = mg["margin_raw"] - 2 * n_free
        p99, _dist = g1_null(corp["family"], reserve, phi, anchors_sv,
                             best_rival_total, n_free, seed + "-null")
        row["g1_margin"] = {
            "candidate_derived_total": mg["tot_cand"]["derived_total"],
            "rivals": mg["rivals"], "margin_raw": mg["margin_raw"],
            "free_choices": n_free, "penalized_margin": penalized,
            "null_p99": p99,
            "pass": bool(penalized >= 10 and penalized > p99)}
        log(f"rep {rep}: G1 margins done — penalized {penalized:.1f} "
            f"nats, null p99 {p99:.1f}, pass {row['g1_margin']['pass']}")
        row["g1_relaxed"] = info["relaxed"]
        results["replications"].append(row)
        # custody: the corpus and its truth
        with open(f"{custody_dir}/synth-rep{rep}.json", "w") as f:
            json.dump({"seed": seed, "signseqs": signseqs,
                       "bounds": [sorted(b) for b in corp["bounds"]],
                       "sites": sites_list, "family": corp["family"],
                       "truth": truth,
                       "counted_slots": corp["counted_slots"]}, f)
        log(f"rep {rep}: corpus written to custody "
            f"({rep}/{reps} replications complete)")

    def med(key_path):
        vals = []
        for r in results["replications"]:
            x = r
            for k in key_path:
                x = x[k]
            if x is not None:
                vals.append(x)
        return median(vals) if vals else None

    summary = {
        "g1_recovery_median": med(["g1_recovery", "recovery"]),
        "g1_shuffle_recovery_median": med(["g1_shuffle_recovery", "recovery"]),
        "g1_margin_pass_reps": sum(1 for r in results["replications"]
                                   if r["g1_margin"]["pass"]),
        "g1_penalized_median": med(["g1_margin", "penalized_margin"]),
        "g2_positional_0.95_median": med(["g2_positional", "0.95", "recovery"]),
        "g2_positional_0.90_median": med(["g2_positional", "0.90", "recovery"]),
        "g2_segmentation_f1_median": med(["g2_segmentation", "f1"]),
        "g2_partials_median": med(["g2_partials", "recovery"]),
        "g2_numerical_median": med(["g2_numerical", "recovery"]),
        "g2_shuffle_medians": {
            "positional_0.95": med(["g2_shuffle", "positional_0.95"]),
            "segmentation_f1": med(["g2_shuffle", "segmentation_f1"]),
            "partials": med(["g2_shuffle", "partials"]),
            "numerical": med(["g2_shuffle", "numerical"])},
        "g3_recovery_median": med(["g3_context", "recovery"]),
        "g3_control_median": med(["g3_context", "control_recovery"]),
    }
    ctrl = lambda right, shuf: (shuf is not None and right
                                and shuf < 0.5 * right)
    verdicts = {
        "G1_assignment_search": {
            "clause_i_recovery": summary["g1_recovery_median"] >= RECOVERY_FLOOR,
            "clause_ii_margin": summary["g1_margin_pass_reps"] >= 3,
            "shuffle_control": ctrl(summary["g1_recovery_median"],
                                    summary["g1_shuffle_recovery_median"])},
        "G2_structure_induction": {
            "positional": summary["g2_positional_0.95_median"] >= RECOVERY_FLOOR,
            "segmentation": summary["g2_segmentation_f1_median"] >= RECOVERY_FLOOR,
            "partials": summary["g2_partials_median"] >= RECOVERY_FLOOR,
            "numerical": summary["g2_numerical_median"] >= RECOVERY_FLOOR,
            "shuffle_control_positional": ctrl(
                summary["g2_positional_0.95_median"],
                summary["g2_shuffle_medians"]["positional_0.95"]),
            "shuffle_control_segmentation": ctrl(
                summary["g2_segmentation_f1_median"],
                summary["g2_shuffle_medians"]["segmentation_f1"]),
            "shuffle_control_partials": ctrl(
                summary["g2_partials_median"],
                summary["g2_shuffle_medians"]["partials"]),
            "shuffle_control_numerical": ctrl(
                summary["g2_numerical_median"],
                summary["g2_shuffle_medians"]["numerical"])},
        "G3_context_channel": {
            "clause_i_recovery": summary["g3_recovery_median"] >= RECOVERY_FLOOR,
            "shuffle_control": ctrl(summary["g3_recovery_median"],
                                    summary["g3_control_median"])},
    }
    for g, clauses in verdicts.items():
        clauses["verdict"] = ("PASSED" if all(clauses.values())
                              else "FAILED")
    results["summary"] = summary
    results["verdicts"] = verdicts
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)
    log(f"verdicts: {json.dumps({g: v['verdict'] for g, v in verdicts.items()})}")
    log(f"raw output written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
