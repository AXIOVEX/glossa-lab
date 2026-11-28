#!/usr/bin/env python3
"""Spec 110 REVISED deliberate-obfuscation battery — filed harness.

Registered in specs/110-obfuscation-hypothesis/records/
revision-registration-2026-11-27.md. Contents:

  - ProfileLang / build_profile_corpus: the parameterized natural-
    writing generator (the Spec 109 Stage 1 recipe generalized to
    arbitrary profiles, with the two-tier stemval periphery), used to
    build per-system control bands and gate corpora.
  - Statistics: family A (A1-A4, first registration's forms), family B
    omnibus JSD with the within-length-bin stratum null, family D's
    joint rule (inventory V and the fixed-rank tail mass at rank
    floor(V0/2)).
  - Transformations: T-HOM, T-POLY, T-SUB-D, T-SUB-U (carried over
    from the first battery) and T-SHUF (within-sequence permutation,
    the revision's structure-destruction control).
  - The driver: per-system bands, the control gate (detection,
    invariance, and the 12-sample false-positive panel, each sample
    scored under its own system's band), then execution over the
    three target corpora for gate-passing families only.

The gate runs before any real corpus is scored, on the registered
seeds. Outputs land in custody glossa-custody/spec110-rev/
(gate-output-rev2.json, raw-output-rev2.json). The development
measurements that shaped this design (rounds dev1-dev3, development
seeds only) are disclosed in the revision registration.
"""
import datetime
import hashlib
import json
import math
import os
import random
import time
from collections import Counter, defaultdict


# --------------------------------------------------------------------------
# Profile generator (machinery constants are generic, not fitted to targets)

STEM_W_EXP = 0.7        # Stage 1 stem-weight Zipf exponent
STEMVAL_POP_EXP = 0.9   # stemval popularity Zipf exponent (generic Zipf)
PREF_LIST = 15          # Stage 1 collocation preference list size
PREF_WEIGHT = 6.0       # Stage 1 closer preference weight
OPENER_STEM_PROB = 0.7  # Stage 1 opener->stem preference probability
SITE_SIGMA = 0.12       # per-site stem-weight lognormal perturbation


class ProfileLang:
    def __init__(self, rng, V0, periphery_share=0.25, periphery_sub=0.10):
        vals = list(range(V0))
        rng.shuffle(vals)
        n_open = max(1, round(0.13 * V0))
        n_close = max(1, round(0.13 * V0))
        n_ctx = max(1, round(0.20 * V0))
        n_aff = max(1, round(0.15 * V0))
        self.openers = vals[:n_open]
        self.closers = vals[n_open:n_open + n_close]
        self.ctx = vals[n_open + n_close:n_open + n_close + n_ctx]
        aff = vals[n_open + n_close + n_ctx:
                   n_open + n_close + n_ctx + n_aff]
        self.stemvals = vals[n_open + n_close + n_ctx + n_aff:]
        S = len(self.stemvals)
        # affix units drawn from the affix pool (reuse across units)
        def draw(k):
            return tuple(rng.choice(aff) for _ in range(k))
        self.p1, self.p2 = draw(2), draw(2)
        self.s1, self.s2 = draw(2), draw(3)
        # Two-tier stemvals: a core used uniformly for stem building,
        # and a periphery substituted into a stem position with low
        # probability. The periphery is the generic rare-tail
        # mechanism: in a large inventory at a moderate token count,
        # peripheral signs are barely attested. Core within-stem
        # transitions stay near-uniform (the Stage 1 recipe), so
        # bigram structure comes from stem reuse and the edge classes,
        # not from a popularity gradient inside stems.
        n_per = max(1, round(periphery_share * S))
        self.core_vals = self.stemvals[:S - n_per]
        self.per_vals = self.stemvals[S - n_per:]
        self.periphery_sub = periphery_sub
        C = len(self.core_vals)
        t2 = min(C * C, max(60, round(4.6 * V0)))
        t3 = min(C ** 3, max(40, round(1.55 * V0)))
        self.stems_by_len = {}
        for L, target in ((2, t2), (3, t3)):
            seen = set()
            guard = 0
            while len(seen) < target and guard < target * 60:
                guard += 1
                st = tuple(rng.choice(self.core_vals) for _ in range(L))
                if self.per_vals and rng.random() < periphery_sub:
                    j = rng.randrange(L)
                    st = st[:j] + (rng.choice(self.per_vals),) + st[j + 1:]
                seen.add(st)
            self.stems_by_len[L] = sorted(seen)
        all_stems = self.stems_by_len[2] + self.stems_by_len[3]
        rng.shuffle(all_stems)
        self.stem_index = {s: i for i, s in enumerate(all_stems)}
        self.stems = all_stems
        self.stem_w = [1.0 / (i + 1) ** STEM_W_EXP for i in range(len(all_stems))]
        # collocation preferences: openers/ctx prefer stems; closers/ctx too
        self.open_pref = {}
        self.close_pref = {}
        for v in self.openers + self.ctx:
            self.open_pref[v] = rng.sample(
                range(len(all_stems)), min(PREF_LIST, len(all_stems)))
        for v in self.closers + self.ctx:
            self.close_pref[v] = rng.sample(
                range(len(all_stems)), min(PREF_LIST, len(all_stems)))
        # marginal stemval usage weights (for lone signs)
        marg = Counter()
        for st, w in zip(all_stems, self.stem_w):
            for v in st:
                marg[v] += w
        self.lone_vals = list(marg)
        self.lone_w = [marg[v] for v in self.lone_vals]

    def _pick_stem(self, rng, want, weights):
        pool = self.stems_by_len[want]
        idxs = [self.stem_index[s] for s in pool]
        ws = [weights[i] for i in idxs]
        return rng.choices(pool, weights=ws)[0]

    def _pick_stem_for_opener(self, rng, value, want, weights):
        pref = self.open_pref.get(value)
        if pref and rng.random() < OPENER_STEM_PROB:
            cands = [self.stems[i] for i in pref
                     if len(self.stems[i]) == want]
            if cands:
                return rng.choice(cands)
        return self._pick_stem(rng, want, weights)

    def sequence(self, rng, L, site, weights, ctx_open):
        if L == 1:
            return [rng.choices(self.lone_vals, weights=self.lone_w)[0]]
        opts = [(o, c) for o in (0, 1, 2) for c in (0, 1, 2, 3)
                if L - o - c >= 2]
        o, c = rng.choice(opts)
        seq = []
        opener_value = None
        if o == 2:
            seq += list(rng.choice((self.p1, self.p2)))
        elif o == 1:
            pool = self.openers + [v for v in self.ctx if ctx_open.get(v)]
            opener_value = rng.choice(pool)
            seq.append(opener_value)
        m = L - o - c
        last_stem = None
        rem = m
        first = True
        while rem > 0:
            if rem == 1:
                seq.append(rng.choices(self.lone_vals,
                                       weights=self.lone_w)[0])
                rem = 0
                continue
            want = rem if rem <= 3 else (2 if rem == 4 else rng.choice((2, 3)))
            if first and opener_value is not None:
                last_stem = self._pick_stem_for_opener(
                    rng, opener_value, want, weights)
            else:
                last_stem = self._pick_stem(rng, want, weights)
            seq += list(last_stem)
            rem -= want
            first = False
        if c == 1:
            pool = self.closers + [v for v in self.ctx if not ctx_open.get(v)]
            ws = []
            li = self.stem_index.get(last_stem)
            for v in pool:
                pref = self.close_pref.get(v)
                ws.append(PREF_WEIGHT if pref and li in pref else 1.0)
            seq.append(rng.choices(pool, weights=ws)[0])
        elif c == 2:
            seq += list(self.s1)
        elif c == 3:
            seq += list(self.s2)
        assert len(seq) == L, (len(seq), L, o, c)
        return seq


def build_profile_corpus(seed, V0, lengths, site_labels=None):
    """One synthetic natural corpus at a profile.

    site_labels: optional list (aligned with lengths) of site labels or
    None; when given, per-site variation is planted (context-role flips
    and stem-weight perturbation per site). Returns (seqs, sites).
    """
    rng = random.Random(seed)
    lang = ProfileLang(rng, V0)
    sites = site_labels if site_labels is not None else [None] * len(lengths)
    # per-site stem weights and ctx roles
    site_weights = {}
    site_ctx_open = {}
    for s in sorted(set(x for x in sites if x is not None), key=str):
        site_weights[s] = [w * math.exp(rng.gauss(0.0, SITE_SIGMA))
                           for w in lang.stem_w]
        site_ctx_open[s] = {v: rng.random() < 0.5 for v in lang.ctx}
    base_ctx_open = {v: True for v in lang.ctx}
    seqs = []
    seen = set()
    fallback = 0
    for i, L in enumerate(lengths):
        site = sites[i]
        w = site_weights.get(site, lang.stem_w)
        co = site_ctx_open.get(site, base_ctx_open)
        placed = None
        for _ in range(200):
            q = lang.sequence(rng, L, site, w, co)
            key = tuple(q)
            if key not in seen:
                seen.add(key)
                placed = q
                break
        if placed is None:
            placed = q
            fallback += 1
        seqs.append(placed)
    return seqs, sites, {"distinct_fallback": fallback, "lang": lang}


# --------------------------------------------------------------------------
# Statistics (registration section 2 forms carried over)

def counts_of(seqs):
    c = Counter()
    for q in seqs:
        c.update(q)
    return c


def entropy_bits(counter, total):
    h = 0.0
    for v in counter.values():
        p = v / total
        h -= p * math.log2(p)
    return h


def family_a_stats(seqs):
    c = counts_of(seqs)
    N = sum(c.values())
    V = len(c)
    H = entropy_bits(c, N)
    bc = Counter()
    for q in seqs:
        for a, b in zip(q, q[1:]):
            bc[(a, b)] += 1
    nb = sum(bc.values())
    by_first = defaultdict(Counter)
    for (a, b), v in bc.items():
        by_first[a][b] = v
    h2 = 0.0
    for a, ctr in by_first.items():
        na = sum(ctr.values())
        h2 += (na / nb) * entropy_bits(ctr, na)
    return {"N": N, "V": V,
            "A1": H / math.log2(V) if V > 1 else 0.0,
            "A2": max(c.values()) / N,
            "A3": h2 / H if H > 0 else 0.0,
            "A4": H - h2, "H": H, "H2": h2}


def d_stats(seqs):
    """Family D candidates: V, hapax share, rare shares, Lorenz tail mass,
    tail-type count beyond 90% coverage, effective inventory."""
    c = counts_of(seqs)
    N = sum(c.values())
    V = len(c)
    hap = sum(1 for v in c.values() if v == 1)
    rare2 = sum(1 for v in c.values() if v <= 2)
    rare2_tok = sum(v for v in c.values() if v <= 2)
    ascending = sorted(c.values())
    half = V // 2
    tail_mass = sum(ascending[:half]) / N if half else 0.0
    # types needed to exceed 90% coverage (descending), tail = the rest
    desc = sorted(c.values(), reverse=True)
    acc, need = 0, 0
    for v in desc:
        acc += v
        need += 1
        if acc >= 0.90 * N:
            break
    H = entropy_bits(c, N)
    return {"V": V, "N": N,
            "hapax_type_share": hap / V if V else 0.0,
            "rare2_type_share": rare2 / V if V else 0.0,
            "rare2_token_share": rare2_tok / N if N else 0.0,
            "lorenz_tail_mass": tail_mass,
            "tail_types_beyond_90": V - need,
            "eff_inventory": 2.0 ** H,
            "eff_ratio": (2.0 ** H) / V if V else 0.0}


def profile_of(seqs, inventory=None):
    c = counts_of(seqs)
    N = sum(c.values())
    inv = inventory if inventory is not None else sorted(c, key=str)
    return {s: c.get(s, 0) / N for s in inv}, c, N


def jsd(p, q):
    keys = set(p) | set(q)
    tot = 0.0
    for k in keys:
        a, b = p.get(k, 0.0), q.get(k, 0.0)
        m = 0.5 * (a + b)
        if a > 0:
            tot += 0.5 * a * math.log2(a / m)
        if b > 0:
            tot += 0.5 * b * math.log2(b / m)
    return tot


def omnibus_jsd(strata_seqs):
    profs, toks = {}, {}
    for lab, sq in strata_seqs.items():
        pr, _, n = profile_of(sq)
        profs[lab] = pr
        toks[lab] = n
    labs = list(profs)
    num, den = 0.0, 0.0
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            w = toks[labs[i]] * toks[labs[j]]
            num += w * jsd(profs[labs[i]], profs[labs[j]])
            den += w
    return num / den if den else 0.0


def length_bin(q):
    n = len(q)
    if n <= 2:
        return 0
    if n <= 4:
        return 1
    if n <= 6:
        return 2
    return 3


def stratum_null(seqs, labels, seed, draws=999, log=None):
    rng = random.Random(seed)
    bins = defaultdict(list)
    for i, q in enumerate(seqs):
        bins[length_bin(q)].append(i)
    obs_groups = defaultdict(list)
    for i, lab in enumerate(labels):
        obs_groups[lab].append(seqs[i])
    obs = omnibus_jsd(dict(obs_groups))
    labs_by_bin = {b: [labels[i] for i in idxs] for b, idxs in bins.items()}
    null = []
    for d in range(draws):
        groups = defaultdict(list)
        for b, idxs in bins.items():
            labs = labs_by_bin[b][:]
            rng.shuffle(labs)
            for i, lab in zip(idxs, labs):
                groups[lab].append(seqs[i])
        null.append(omnibus_jsd(dict(groups)))
        if log and (d + 1) % 333 == 0:
            log(f"  stratum null: {d + 1}/{draws} draws")
    null.sort()
    p99 = null[int(0.99 * (len(null) - 1))]
    pct = sum(1 for v in null if v <= obs) / len(null)
    return obs, p99, pct, null


# --------------------------------------------------------------------------
# Transformations (carried over from the first battery)

def permute_labels(seqs, perm):
    return [[perm.get(s, s) for s in q] for q in seqs]


def make_perm(inventory, seed):
    rng = random.Random(seed)
    vals = list(inventory)
    sh = vals[:]
    rng.shuffle(sh)
    return dict(zip(vals, sh))


def t_hom(seqs, seed):
    c = counts_of(seqs)
    top = [s for s, _ in c.most_common(10)]
    rng = random.Random(seed)
    out = []
    for q in seqs:
        nq = []
        for s in q:
            if s in top:
                nq.append(f"{s}#h{rng.randint(0, 1)}")
            else:
                nq.append(s)
        out.append(nq)
    return out


def t_poly(seqs, seed):
    inv = sorted(counts_of(seqs), key=str)
    perms = [make_perm(inv, seed + k) for k in range(3)]
    return [[perms[i % 3].get(s, s) for i, s in enumerate(q)] for q in seqs]


# --------------------------------------------------------------------------
# C2-R: bigram-signature matching

SIG_K = 40  # top-K components of each sorted distribution in a signature
CTX_K = 24  # ranked-context signature width (top-K frequent context signs)


def _sorted_topk(counter, total, k=SIG_K):
    probs = sorted((v / total for v in counter.values()), reverse=True)
    top = probs[:k]
    tail = 1.0 - sum(top)
    return top + [0.0] * (k - len(top)) + [tail]


def sign_signatures(seqs):
    c = counts_of(seqs)
    N = sum(c.values())
    succ = defaultdict(Counter)
    pred = defaultdict(Counter)
    for q in seqs:
        for a, b in zip(q, q[1:]):
            succ[a][b] += 1
            pred[b][a] += 1
    sigs = {}
    for s in c:
        ns = sum(succ[s].values())
        np_ = sum(pred[s].values())
        sv = _sorted_topk(succ[s], ns) if ns else [0.0] * (SIG_K + 1)
        pv = _sorted_topk(pred[s], np_) if np_ else [0.0] * (SIG_K + 1)
        sigs[s] = (sv, pv, math.log(c[s] / N), c[s])
    return sigs


def _sig_dist(a, b):
    d = 0.0
    for x, y in zip(a[0], b[0]):
        d += abs(x - y)
    for x, y in zip(a[1], b[1]):
        d += abs(x - y)
    d += abs(a[2] - b[2])
    return d


def match_bigram(seqs_p, seqs_q, min_count=5):
    """Match Q signs to P signs by bigram signatures.

    Returns dict with mapping (Q sign -> P sign) over the scored
    population (signs with count >= min_count in both parts), plus
    gain, self_agreement, scored/shared counts, and the recovery-ready
    mapping over all shared signs.
    """
    sp = sign_signatures(seqs_p)
    sq = sign_signatures(seqs_q)
    shared = sorted(set(sp) & set(sq), key=str)
    scored = [s for s in shared if sp[s][3] >= min_count
              and sq[s][3] >= min_count]
    # distance matrix over scored signs
    dist = {}
    for qs in scored:
        for ps in scored:
            dist[(qs, ps)] = _sig_dist(sq[qs], sp[ps])
    # greedy mutual-best
    cand = sorted(((d, str(qs), str(ps), qs, ps)
                   for (qs, ps), d in dist.items()))
    mapping = {}
    used = set()
    for _, _, _, qs, ps in cand:
        if qs not in mapping and ps not in used:
            mapping[qs] = ps
            used.add(ps)
    # swap polish on total distance (O(1) deltas)
    def total(m):
        return sum(dist[(s, m[s])] for s in m)
    cur = total(mapping)
    keys = list(mapping)
    for _ in range(200):
        improved = False
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                delta = (dist[(a, mapping[b])] + dist[(b, mapping[a])]
                         - dist[(a, mapping[a])] - dist[(b, mapping[b])])
                if delta < -1e-12:
                    mapping[a], mapping[b] = mapping[b], mapping[a]
                    cur += delta
                    improved = True
        if not improved:
            break
    # gain on unigram profiles (mapped vs identity), over scored signs'
    # mass only: profiles restricted to the union inventory, mapping
    # applied to Q's scored signs, others keep labels.
    prof_p, _, _ = profile_of(seqs_p)
    prof_q, _, _ = profile_of(seqs_q)

    def mapped_jsd(m):
        mq = {}
        for s, v in prof_q.items():
            t = m.get(s, s)
            mq[t] = mq.get(t, 0.0) + v
        return jsd(prof_p, mq)
    ident = {s: s for s in shared}
    gain = mapped_jsd(ident) - mapped_jsd(mapping)
    self_agree = (sum(1 for s in scored if mapping.get(s) == s) / len(scored)
                  if scored else 0.0)
    return {"mapping": mapping, "gain": gain, "self_agreement": self_agree,
            "scored_signs": len(scored), "shared_signs": len(shared),
            "total_distance": cur}


def _assign_from_dist(dist, scored):
    cand = sorted(((d, str(qs), str(ps), qs, ps)
                   for (qs, ps), d in dist.items()))
    mapping = {}
    used = set()
    for _, _, _, qs, ps in cand:
        if qs not in mapping and ps not in used:
            mapping[qs] = ps
            used.add(ps)
    cur = sum(dist[(s, mapping[s])] for s in mapping)
    keys = list(mapping)
    for _ in range(200):
        improved = False
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                delta = (dist[(a, mapping[b])] + dist[(b, mapping[a])]
                         - dist[(a, mapping[a])] - dist[(b, mapping[b])])
                if delta < -1e-12:
                    mapping[a], mapping[b] = mapping[b], mapping[a]
                    cur += delta
                    improved = True
        if not improved:
            break
    return mapping, cur


def _gain_and_agree(seqs_p, seqs_q, mapping, scored, shared):
    prof_p, _, _ = profile_of(seqs_p)
    prof_q, _, _ = profile_of(seqs_q)

    def mapped_jsd(m):
        mq = {}
        for s, v in prof_q.items():
            t = m.get(s, s)
            mq[t] = mq.get(t, 0.0) + v
        return jsd(prof_p, mq)
    ident = {s: s for s in shared}
    gain = mapped_jsd(ident) - mapped_jsd(mapping)
    self_agree = (sum(1 for s in scored if mapping.get(s) == s) / len(scored)
                  if scored else 0.0)
    return gain, self_agree


def ranked_context_signatures(seqs, k=CTX_K):
    """Signature per sign: its successor distribution over the part's
    own top-k most frequent signs (by rank), its predecessor
    distribution over the same ranked contexts, and its log frequency
    share. Ranked contexts aggregate counts over frequent signs, so
    the vectors are estimable at stratum sizes where per-sign bigram
    distributions are not."""
    c = counts_of(seqs)
    N = sum(c.values())
    top = [s for s, _ in c.most_common(k)]
    rank = {s: i for i, s in enumerate(top)}
    succ = defaultdict(Counter)
    pred = defaultdict(Counter)
    for q in seqs:
        for a, b in zip(q, q[1:]):
            succ[a][b] += 1
            pred[b][a] += 1
    sigs = {}
    for s in c:
        sv = [0.0] * (k + 1)
        ns = sum(succ[s].values())
        if ns:
            for t, v in succ[s].items():
                sv[rank.get(t, k)] += v / ns
        pv = [0.0] * (k + 1)
        np_ = sum(pred[s].values())
        if np_:
            for t, v in pred[s].items():
                pv[rank.get(t, k)] += v / np_
        sigs[s] = (sv, pv, math.log(c[s] / N), c[s])
    return sigs


def match_ranked(seqs_p, seqs_q, min_count=5):
    """C2-R on ranked-context signatures (same assignment, gain, and
    self-agreement machinery as match_bigram)."""
    sp = ranked_context_signatures(seqs_p)
    sq = ranked_context_signatures(seqs_q)
    shared = sorted(set(sp) & set(sq), key=str)
    scored = [s for s in shared if sp[s][3] >= min_count
              and sq[s][3] >= min_count]
    dist = {}
    for qs in scored:
        for ps in scored:
            dist[(qs, ps)] = _sig_dist(sq[qs], sp[ps])
    mapping, cur = _assign_from_dist(dist, scored)
    gain, self_agree = _gain_and_agree(seqs_p, seqs_q, mapping, scored,
                                       shared)
    return {"mapping": mapping, "gain": gain, "self_agreement": self_agree,
            "scored_signs": len(scored), "shared_signs": len(shared),
            "total_distance": cur}


# ---------------------------------------------------------------------------
# Spec 110 REVISION driver: loaders, bands, gate, execution. Appended to
# the library above (generator + statistics + transformations, from the
# development build revlib.py) to form the filed harness
# records/obfuscation-harness-rev2.py. Every constant below is the frozen
# revision registration's; the gate runs once, on the registered seeds,
# before any real corpus is scored.
# ---------------------------------------------------------------------------

WT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
CUSTODY = os.environ.get(
    "GLOSSA_CUSTODY",
    "/home/tpierson/.syncyard/worktrees/glossa/glossa-custody")
CUST105 = os.path.join(CUSTODY, "spec105")
CUST107 = os.path.join(CUSTODY, "spec107")
OUT_DIR = os.path.join(CUSTODY, "spec110-rev")
OUT_GATE = os.path.join(OUT_DIR, "gate-output-rev2.json")
OUT_RAW = os.path.join(OUT_DIR, "raw-output-rev2.json")
NULL_DRAWS = 999
BAND_N = {"ind": 20, "mer": 20, "ete": 12}
LAT_BAND_N = 12
CTL_N = 5


def ts():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%SZ")


def log(msg):
    print(f"[{ts()}] {msg}", flush=True)


def sha256_file(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---- corpus loaders (the first battery's registered handling, sec. 6) -----

def load_indus():
    raw = json.load(open(os.path.join(CUST105, "indus-derivation.json")))
    seqs = []
    for art in raw:
        for line in art["lines"]:
            flat = [s for g in line for s in g]
            if flat:
                seqs.append(flat)
    p100 = json.load(open(os.path.join(WT, "outputs/phase100_full_corpus.json")))
    seq2site = {}
    conflicts = set()
    for t in p100["translations"]:
        k = tuple(t["signs"])
        if k in seq2site and seq2site[k] != t["site"]:
            conflicts.add(k)
        seq2site.setdefault(k, t["site"])
    sites = []
    for q in seqs:
        k = tuple(q)
        sites.append(None if k in conflicts else seq2site.get(k))
    return seqs, sites


def load_eteocypriot():
    raw = json.load(open(os.path.join(
        WT, "specs/096-eteocypriot-program/corpus/corpus.json")))
    seqs = []
    for ins in raw["inscriptions"]:
        if ins.get("stratum") != "primary-amathus":
            continue
        for ln in ins.get("eteocypriot_lines") or []:
            for seg in ln["segments"]:
                if seg:
                    seqs.append(list(seg))
        for ln in ins.get("eteocypriot_side") or []:
            segs = ln.get("segments") if isinstance(ln, dict) else None
            if segs:
                for seg in segs:
                    if seg:
                        seqs.append(list(seg))
    return seqs


def load_meroitic():
    raw = json.load(open(os.path.join(CUST105, "meroitic.json")))
    seqs = []
    for t in raw:
        for line in t["lines"]:
            flat = [s for g in line for s in g if s != "."]
            if flat:
                seqs.append(flat)
    return seqs


def load_latin():
    text = open(os.path.join(CUST107, "de-bello-gallico-gutenberg-218.txt"),
                encoding="utf-8", errors="replace").read().lower()
    words, cur = [], []
    for ch in text:
        if "a" <= ch <= "z":
            cur.append(ch)
        else:
            if len(cur) >= 2:
                words.append(cur)
            cur = []
    if len(cur) >= 2:
        words.append(cur)
    return words


def load_profiles():
    ind_seqs, ind_sites = load_indus()
    mer_seqs = load_meroitic()
    ete_seqs = load_eteocypriot()
    lat = load_latin()
    q = len(lat) // 4
    prof = {
        "ind": {"V0": 372, "seqs": ind_seqs, "sites": ind_sites,
                "lengths": [len(s) for s in ind_seqs]},
        "mer": {"V0": 31, "seqs": mer_seqs, "sites": None,
                "lengths": [len(s) for s in mer_seqs]},
        "ete": {"V0": 32, "seqs": ete_seqs, "sites": None,
                "lengths": [len(s) for s in ete_seqs]},
    }
    for i in range(4):
        qs = lat[i * q:(i + 1) * q]
        prof[f"latq{i + 1}"] = {"V0": 26, "seqs": qs, "sites": None,
                                "lengths": [len(s) for s in qs]}
    return prof


def census_of(seqs):
    c = counts_of(seqs)
    return {"sequences": len(seqs), "N": sum(c.values()), "V": len(c),
            "hapax_types": sum(1 for v in c.values() if v == 1)}


# ---- statistics bundle ------------------------------------------------------

def tail_stats(seqs, V0):
    c = counts_of(seqs)
    N = sum(c.values())
    desc = sorted(c.values(), reverse=True)
    cut = V0 // 2
    return {"V": len(c), "frtail": sum(desc[cut:]) / N if N else 0.0}


def astats(seqs, V0):
    st = family_a_stats(seqs)
    st.update(tail_stats(seqs, V0))
    return st


def band_of(rows, keys):
    return {k: [min(r[k] for r in rows), max(r[k] for r in rows)] for k in keys}


def a_fires(st, band):
    return {
        "flat": st["A1"] > band["A1"][1] and st["A2"] < band["A2"][0],
        "struct": st["A3"] > band["A3"][1] and st["A4"] < band["A4"][0],
        "c1": st["A3"] > band["A3"][1] or st["A4"] < band["A4"][0],
    }


def d_fire(st, dband):
    return st["V"] > dband["V"][1] and st["frtail"] > dband["frtail"][1]


# ---- transformations added by the revision ---------------------------------

def t_shuf(seqs, seed):
    rng = random.Random(seed)
    out = []
    for q in seqs:
        nq = list(q)
        rng.shuffle(nq)
        out.append(nq)
    return out


def t_sub_u(seqs, seed):
    return permute_labels(seqs, make_perm(sorted(counts_of(seqs), key=str), seed))


def t_sub_d(seqs, sites, target, seed):
    perm = make_perm(sorted(counts_of(seqs), key=str), seed)
    return [[perm.get(s, s) for s in q] if sites[i] == target else list(q)
            for i, q in enumerate(seqs)]


# ---- synthetic corpora at a profile -----------------------------------------

def synth(P, seed, with_sites):
    sites = None
    if with_sites:
        rng = random.Random(f"spec110r2-sites-{seed}")
        sites = P["sites"][:]
        rng.shuffle(sites)
    seqs, planted, _info = build_profile_corpus(seed, P["V0"], P["lengths"], sites)
    return seqs, planted


# ---- family B ----------------------------------------------------------------

def b_strata(seqs, sites):
    """Floor-meeting strata: >=300 tokens and >=30 texts, non-null labels."""
    groups = defaultdict(list)
    for q, s in zip(seqs, sites):
        if s is not None:
            groups[s].append(q)
    return {lab: sq for lab, sq in groups.items()
            if sum(len(q) for q in sq) >= 300 and len(sq) >= 30}


def b_eval(seqs, sites, seed, baseline_max):
    strata = b_strata(seqs, sites)
    if len(strata) < 2:
        return None
    keep = [(q, s) for q, s in zip(seqs, sites) if s in strata]
    obs, p99, _pct, _null = stratum_null([q for q, _s in keep],
                                         [s for _q, s in keep],
                                         seed, draws=NULL_DRAWS)
    return {"obs": obs, "null_p99": p99, "baseline_max": baseline_max,
            "strata": sorted(strata),
            "fire": obs > p99 and obs > baseline_max}


def b_obs(seqs, sites):
    strata = b_strata(seqs, sites)
    if len(strata) < 2:
        return None
    return omnibus_jsd(strata)


# ---- main ---------------------------------------------------------------------

def main():
    t0 = time.time()
    os.makedirs(OUT_DIR, exist_ok=True)
    pins = {
        "indus_derivation": sha256_file(os.path.join(CUST105, "indus-derivation.json")),
        "phase100": sha256_file(os.path.join(WT, "outputs/phase100_full_corpus.json")),
        "eteocypriot": sha256_file(os.path.join(
            WT, "specs/096-eteocypriot-program/corpus/corpus.json")),
        "meroitic": sha256_file(os.path.join(CUST105, "meroitic.json")),
        "latin_dbg": sha256_file(os.path.join(
            CUST107, "de-bello-gallico-gutenberg-218.txt")),
        "harness_sha256": sha256_file(os.path.abspath(__file__)),
    }
    log(f"input pins: {json.dumps({k: v[:12] for k, v in pins.items()})}")
    profiles = load_profiles()
    cens = {n: census_of(P["seqs"]) for n, P in profiles.items()}
    log("profiles: " + ", ".join(f"{n} N={cens[n]['N']} V={cens[n]['V']}"
                                  for n in cens))

    # ---- bands ---------------------------------------------------------------
    bands, dbands, band_rows = {}, {}, {}
    for name in ("ind", "mer", "ete"):
        P = profiles[name]
        rows = []
        for i in range(1, BAND_N[name] + 1):
            seqs, _sites = synth(P, f"spec110r2-band-{name}-{i}", name == "ind")
            rows.append(astats(seqs, P["V0"]))
        band_rows[name] = rows
        bands[name] = band_of(rows, ("A1", "A2", "A3", "A4"))
        dbands[name] = band_of(rows, ("V", "frtail"))
        log(f"band {name}: A={json.dumps(bands[name])} D={json.dumps(dbands[name])}")
    lat_bands, lat_dbands = {}, {}
    for q in (1, 2, 3, 4):
        P = profiles[f"latq{q}"]
        rows = []
        for i in range(1, LAT_BAND_N + 1):
            seqs, _ = synth(P, f"spec110r2-band-latq{q}-{i}", False)
            rows.append(astats(seqs, P["V0"]))
        lat_bands[q] = band_of(rows, ("A1", "A2", "A3", "A4"))
        lat_dbands[q] = band_of(rows, ("V", "frtail"))
        log(f"band latq{q}: A={json.dumps(lat_bands[q])} D={json.dumps(lat_dbands[q])}")

    # ---- family B genre baseline (Indus profile band corpora) -----------------
    b_baseline_rows = []
    for i in range(1, BAND_N["ind"] + 1):
        seqs, sites = synth(profiles["ind"], f"spec110r2-band-ind-{i}", True)
        b_baseline_rows.append(b_obs(seqs, sites))
    b_baseline_max = max(b_baseline_rows)
    log(f"B genre baseline: max {b_baseline_max:.4f} over {len(b_baseline_rows)} band corpora")

    # ---- gate corpora ------------------------------------------------------------
    gate = {}
    for name in ("ind", "mer", "ete"):
        P = profiles[name]
        band, dband = bands[name], dbands[name]
        legs = []
        for i in range(CTL_N):
            seed = f"spec110r2-ctl-{name}-{i + 1}"
            seqs, sites = synth(P, seed, name == "ind")
            row = {"seed": seed}
            nat = astats(seqs, P["V0"])
            row["nat"] = nat
            row["nat_fires"] = a_fires(nat, band)
            row["nat_dfire"] = d_fire(nat, dband)
            hst = astats(t_hom(seqs, 11001 + i), P["V0"])
            row["hom"] = hst
            row["hom_flat"] = a_fires(hst, band)["flat"]
            row["hom_dfire"] = d_fire(hst, dband)
            pst = astats(t_poly(seqs, 11101 + i), P["V0"])
            row["poly"] = pst
            row["poly_flat"] = a_fires(pst, band)["flat"]
            sst = astats(t_shuf(seqs, 11501 + i), P["V0"])
            row["shuf"] = sst
            sf = a_fires(sst, band)
            row["shuf_struct"] = sf["struct"]
            row["shuf_c1"] = sf["c1"]
            ust = astats(t_sub_u(seqs, 11401 + i), P["V0"])
            row["subu"] = ust
            uf = a_fires(ust, band)
            row["subu_any_fire"] = (uf["flat"] or uf["struct"] or uf["c1"]
                                    or d_fire(ust, dband))
            if name == "ind":
                row["b_nat"] = b_eval(seqs, sites, 11001 + i, b_baseline_max)
                strata = b_strata(seqs, sites)
                order = sorted(strata, key=lambda s: -sum(len(q) for q in strata[s]))
                target = order[1]
                dseqs = t_sub_d(seqs, sites, target, 11301 + i)
                row["b_subd"] = b_eval(dseqs, sites, 11001 + i, b_baseline_max)
                row["b_subd"]["stratum"] = target
            legs.append(row)
            log(f"gate {name} ctl{i}: HOM flat={row['hom_flat']} D={row['hom_dfire']}; "
                f"POLY flat={row['poly_flat']}; SHUF struct={row['shuf_struct']} "
                f"c1={row['shuf_c1']}; INV clean={not row['subu_any_fire']}"
                + (f"; B SUBD={row['b_subd']['fire']} NAT={row['b_nat']['fire']}"
                   if name == "ind" else ""))
        gate[name] = legs

    # ---- false-positive panel: 12 samples, each under its own system's band -----
    panel = []
    for i, leg in enumerate(gate["ind"]):
        f = leg["nat_fires"]
        panel.append({"sample": f"ind-ctl-{i + 1}-untransformed", "band": "ind",
                      "flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": leg["nat_dfire"], "stats": leg["nat"]})
    for q in (1, 2, 3, 4):
        st = astats(profiles[f"latq{q}"]["seqs"], 26)
        f = a_fires(st, lat_bands[q])
        panel.append({"sample": f"latin-q{q}", "band": f"latq{q}",
                      "flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": d_fire(st, lat_dbands[q]), "stats": st})
    mer_all = profiles["mer"]["seqs"]
    half = len(mer_all) // 2
    for label, sq in (("meroitic-whole", mer_all), ("meroitic-half1", mer_all[:half]),
                      ("meroitic-half2", mer_all[half:])):
        st = astats(sq, 31)
        f = a_fires(st, bands["mer"])
        panel.append({"sample": label, "band": "mer",
                      "flat": f["flat"], "struct": f["struct"], "c1": f["c1"],
                      "d": d_fire(st, dbands["mer"]), "stats": st})
    fp = {k: sum(1 for p in panel if p[k]) for k in ("flat", "struct", "c1", "d")}
    fp_b = sum(1 for leg in gate["ind"] if leg["b_nat"] and leg["b_nat"]["fire"])
    log(f"FP panel fires over {len(panel)} samples: {json.dumps(fp)}; FP-B: {fp_b}/5")

    # ---- gate outcomes -------------------------------------------------------------
    def cnt(name, key):
        return sum(1 for leg in gate[name] if leg[key])

    outcomes = {}
    for name in ("ind", "mer", "ete"):
        o = {
            "flat_hom": cnt(name, "hom_flat"), "flat_poly": cnt(name, "poly_flat"),
            "flat_detection": cnt(name, "hom_flat") >= 4 and cnt(name, "poly_flat") >= 4,
            "struct_shuf": cnt(name, "shuf_struct"),
            "struct_detection": cnt(name, "shuf_struct") >= 4,
            "c1_shuf": cnt(name, "shuf_c1"), "c1_detection": cnt(name, "shuf_c1") >= 4,
            "d_hom": cnt(name, "hom_dfire"), "d_detection": cnt(name, "hom_dfire") >= 4,
            "inv_clean": sum(1 for leg in gate[name] if not leg["subu_any_fire"]),
        }
        o["invariance"] = o["inv_clean"] >= 4
        o["a_flat_scoreable"] = o["flat_detection"] and o["invariance"] and fp["flat"] <= 1
        o["a_struct_scoreable"] = (o["struct_detection"] and o["invariance"]
                                  and fp["struct"] <= 1)
        o["c1_scoreable"] = o["c1_detection"] and o["invariance"] and fp["c1"] <= 1
        o["d_scoreable"] = o["d_detection"] and o["invariance"] and fp["d"] <= 1
        outcomes[name] = o
        log(f"gate outcome {name}: {json.dumps(o)}")
    b_gate = {"subd_fires": sum(1 for leg in gate["ind"]
                                if leg["b_subd"] and leg["b_subd"]["fire"]),
              "fp_fires": fp_b}
    b_gate["detection"] = b_gate["subd_fires"] >= 4
    b_gate["fp_ok"] = fp_b <= 1
    b_gate["b_scoreable"] = b_gate["detection"] and b_gate["fp_ok"]
    log(f"gate outcome B (indus): {json.dumps(b_gate)}")

    gate_doc = {
        "spec": "110-revision", "pins": pins, "null_draws": NULL_DRAWS,
        "censuses": cens, "bands": bands, "dbands": dbands,
        "lat_bands": {str(q): lat_bands[q] for q in lat_bands},
        "lat_dbands": {str(q): lat_dbands[q] for q in lat_dbands},
        "b_baseline_rows": b_baseline_rows, "b_baseline_max": b_baseline_max,
        "gate": gate, "panel": panel, "fp": fp, "fp_b": fp_b,
        "outcomes": outcomes, "b_gate": b_gate,
        "elapsed_s": round(time.time() - t0, 1),
    }
    with open(OUT_GATE, "w") as fh:
        json.dump(gate_doc, fh, indent=1, sort_keys=True)
    log(f"gate output filed: {OUT_GATE} ({gate_doc['elapsed_s']}s)")

    # ---- execution: only scoreable families/patterns render verdicts ----------------
    raw = {"spec": "110-revision", "pins": pins, "corpora": {}}

    def a_verdict(entry, o, fires):
        pats = []
        if o["a_flat_scoreable"]:
            pats.append(("flattening", fires["flat"]))
        if o["a_struct_scoreable"]:
            pats.append(("structure", fires["struct"]))
        if not pats:
            return
        entry["a_patterns_scored"] = [n for n, _f in pats]
        hit = [n for n, f in pats if f]
        entry["verdicts"]["A"] = ("SIGNATURE PRESENT (" + ", ".join(hit) + ")"
                                  if hit else "SIGNATURE ABSENT")

    ind = profiles["ind"]
    ist = astats(ind["seqs"], 372)
    ifires = a_fires(ist, bands["ind"])
    entry = {"census": cens["ind"], "stats": ist, "a_fires": ifires,
             "d_fire": d_fire(ist, dbands["ind"]), "verdicts": {}}
    a_verdict(entry, outcomes["ind"], ifires)
    if b_gate["b_scoreable"]:
        entry["b"] = b_eval(ind["seqs"], ind["sites"], 11999, b_baseline_max)
        entry["verdicts"]["B"] = ("SIGNATURE PRESENT" if entry["b"]["fire"]
                                  else "SIGNATURE ABSENT")
    if outcomes["ind"]["c1_scoreable"]:
        entry["verdicts"]["C"] = ("SIGNATURE PRESENT" if ifires["c1"]
                                  else "SIGNATURE ABSENT")
    if outcomes["ind"]["d_scoreable"]:
        entry["verdicts"]["D"] = ("SIGNATURE PRESENT" if entry["d_fire"]
                                  else "SIGNATURE ABSENT")
    raw["corpora"]["indus"] = entry
    log(f"indus verdicts: {json.dumps(entry['verdicts'])}")

    mer = profiles["mer"]
    mst = astats(mer["seqs"], 31)
    mfires = a_fires(mst, bands["mer"])
    entry = {"census": cens["mer"], "stats": mst, "a_fires": mfires,
             "d_fire": d_fire(mst, dbands["mer"]), "verdicts": {}}
    a_verdict(entry, outcomes["mer"], mfires)
    entry["verdicts"]["B"] = ("NOT TESTABLE AT THIS POWER "
                              "(no stratum metadata in the corpus build)")
    if outcomes["mer"]["c1_scoreable"]:
        entry["verdicts"]["C"] = ("SIGNATURE PRESENT" if mfires["c1"]
                                  else "SIGNATURE ABSENT")
    if outcomes["mer"]["d_scoreable"]:
        entry["verdicts"]["D"] = ("SIGNATURE PRESENT" if entry["d_fire"]
                                  else "SIGNATURE ABSENT")
    raw["corpora"]["meroitic"] = entry
    log(f"meroitic verdicts: {json.dumps(entry['verdicts'])}")

    raw["corpora"]["eteocypriot"] = {
        "census": cens["ete"],
        "verdicts": {f: "NOT TESTABLE AT THIS POWER" for f in ("A", "B", "C", "D")},
        "floor_note": "N=54 tokens against the registered N>=1000 floor "
                      "(families A, C, D); single stratum against the family B floor.",
    }
    log("eteocypriot: all families NOT TESTABLE AT THIS POWER (floors)")
    raw["elapsed_s"] = round(time.time() - t0, 1)
    with open(OUT_RAW, "w") as fh:
        json.dump(raw, fh, indent=1, sort_keys=True)
    log(f"raw output filed: {OUT_RAW}")
    log("REVISION RUN COMPLETE")


if __name__ == "__main__":
    main()
