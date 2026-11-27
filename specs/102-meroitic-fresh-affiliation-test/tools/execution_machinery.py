#!/usr/bin/env python3
"""Spec 102 — execution machinery for the Meroitic fresh affiliation test.

MACHINERY PREPARATION ONLY (execution registration, 2026-11-27).
This module implements, from the registered text of Spec 102
(spec.md SS3.2, SS3.6 as amended, SS3.7, SS4 as amended RT6-M11) and
Spec 097 freeze v2 (SS4, SS7), the computations the study's freeze
and scoring stages will call:

  * the per-concept graded score and the primary statistic T
    (spec SS3.2), and the frozen binary statistic S for the
    comparability subset (spec SS3.3, freeze v2 SS4);
  * the joint permutation null of T (comparator forms shuffled
    across concepts, per-concept counts preserved) and the
    permutation p-value in freeze v2's form;
  * the Holm adjustment across the two-test family (spec SS3.2);
  * gate G-1's arithmetic (spec SS3.7, TC-102-01);
  * gate G-2's operative simulation (spec SS4 amendment RT6-M11):
    the registered injection construction, 4,000 replicates per
    (theta, d) cell, the bar at the permutation null's 99th
    percentile, one freeze-registered integer seed from which all
    streams derive deterministically;
  * the prospective binomial bound carried alongside G-2
    (spec SS4: q0 = 0.1255, per-test alpha <= 0.005);
  * the SS3.6 split construction as amended (RT6-H6), exercised by
    TC-102-07.

Data model: the machinery works at SKELETON level. A "form" in
this module is a consonant skeleton (a string). The skeleton
computation itself (ASJPcode mapping for comparator forms;
case-folding and the registered diacritic fold for Meroitic
forms, freeze v2 SS7, both registered as pipeline code of
Spec 097) is NOT fixed by Spec 102's registered text and is a
freeze-time input: the freeze pins the skeleton implementation
(imported unchanged from the Spec 097 pipeline, as the design
stage did) and every function here takes skeletons as given.
`fixture_skeleton` below exists ONLY for the synthetic fixtures
in the companion test file; it is not the study skeleton and no
study computation may call it.

No real concept list, vocabulary, or comparator list is read by
this module; it is exercised only on the synthetic fixtures in
test_execution_machinery.py. Nothing here freezes a concept
list, computes a real power figure, or scores a Meroitic form.
"""

import hashlib
import math
import random

# ------------------------------------------------------------------
# Registered constants (spec SS3.7, SS4 as amended)
# ------------------------------------------------------------------

G1_MIN_CONCEPTS = 40          # per family test
G1_MIN_OUTSIDE_TWELVE = 20    # per family test
G2_THETA = 0.30
G2_D = 0.75
G2_MIN_POWER = 0.80
G2_REPLICATES = 4000          # per (theta, d) cell (RT6-M11 (b))
G2_BAR_NULL_PERMUTATIONS = 4000  # design-stage inner null (RT6-M11,
                              # mirroring tools/design_power_sim.py)
SCORING_PERMUTATIONS = 100000  # spec SS3.2 permutation null size
PASS_P = 0.01                  # Holm-adjusted, spec SS3.2
BINOMIAL_Q0 = 0.1255           # spec SS4 (OD-15 SS2 measurement)
BINOMIAL_ALPHA = 0.005         # per-test, spec SS4

STAGE_42_TWELVE = (12, 15, 16, 17, 21, 46, 55, 62, 70, 72, 75, 97)


def derive_rng(freeze_seed, stream):
    """Deterministic stream derivation from the freeze's single
    registered integer seed (RT6-M11 (d)). Every simulation stream
    in a freeze (permutation null, injection, per test) names its
    stream; the same (seed, stream) pair always yields the same
    stream, on any machine, because random.Random seeded with a
    str uses the full string deterministically."""
    if not isinstance(freeze_seed, int):
        raise TypeError("freeze seed must be a single integer")
    return random.Random("spec102:{}:{}".format(freeze_seed, stream))


# ------------------------------------------------------------------
# SS3.6 split construction (as amended, RT6-H6)
# ------------------------------------------------------------------

def split_assignment(text, salt_bytes):
    """digest = SHA-256(salt || 0x00 || UTF-8(text)); value = the
    digest as a big-endian integer; assignment = value mod 10.
    Residue 0 is the development (derivation) side; residues 1-9
    the held-out side."""
    digest = hashlib.sha256(salt_bytes + b"\x00" + text.encode("utf-8")).digest()
    residue = int.from_bytes(digest, "big") % 10
    return {
        "digest": digest.hex(),
        "residue": residue,
        "side": "development" if residue == 0 else "held-out",
    }


# ------------------------------------------------------------------
# SS3.2 statistic: per-concept score, T, and the binary S
# ------------------------------------------------------------------

def pair_score(mer_skel, comp_skel):
    """The frozen correspondence rule at skeleton level (spec
    SS3.2): 2 if the first skeleton consonants are equal AND
    (the second consonants are equal OR either skeleton has
    length 1); 1 if the first consonants alone are equal;
    0 otherwise. An empty skeleton scores 0 against everything."""
    if not mer_skel or not comp_skel:
        return 0
    if mer_skel[0] != comp_skel[0]:
        return 0
    if len(mer_skel) == 1 or len(comp_skel) == 1 or mer_skel[1] == comp_skel[1]:
        return 2
    return 1


def concept_score(mer_skels, comp_skels):
    """Per concept: the best pair score over all Meroitic x
    comparator skeleton pairs (spec SS3.2)."""
    best = 0
    for ms in mer_skels:
        for cs in comp_skels:
            s = pair_score(ms, cs)
            if s > best:
                best = s
                if best == 2:
                    return 2
    return best


def statistic_T(mer_by_concept, comp_by_concept, concepts):
    """T: the sum of per-concept scores over the test's concepts
    (spec SS3.2). Concepts are the test's own concept set (SS3.2:
    concept sets are per-test)."""
    return sum(
        concept_score(mer_by_concept.get(c, []), comp_by_concept.get(c, []))
        for c in concepts
    )


def statistic_S_binary(mer_by_concept, comp_by_concept, concepts):
    """The frozen binary S (freeze v2 SS4) for the comparability
    subset (spec SS3.3): the number of concepts for which at least
    one pair matches (pair score 2)."""
    return sum(
        1
        for c in concepts
        if concept_score(mer_by_concept.get(c, []), comp_by_concept.get(c, [])) == 2
    )


# ------------------------------------------------------------------
# Permutation null and p-value (spec SS3.2; freeze v2 SS4 form)
# ------------------------------------------------------------------

def _shuffled_comparator(comp_by_concept, concepts, rng):
    """One draw of the joint permutation null: comparator forms
    shuffled across concepts over the test's full comparator pool,
    per-concept counts preserved (spec SS3.2)."""
    pool = []
    for c in concepts:
        pool.extend(comp_by_concept.get(c, []))
    rng.shuffle(pool)
    out = {}
    idx = 0
    for c in concepts:
        n = len(comp_by_concept.get(c, []))
        out[c] = pool[idx:idx + n]
        idx += n
    return out


def permutation_null(mer_by_concept, comp_by_concept, concepts,
                     nperm, rng):
    """The permutation null distribution of T, as a list of
    nperm values, in draw order."""
    return [
        statistic_T(mer_by_concept,
                    _shuffled_comparator(comp_by_concept, concepts, rng),
                    concepts)
        for _ in range(nperm)
    ]


def permutation_p_value(observed, null_values):
    """p = (1 + #{perm >= obs}) / (1 + nperm) (freeze v2 SS4)."""
    ge = sum(1 for x in null_values if x >= observed)
    return (1 + ge) / (1 + len(null_values))


def percentile_99(values):
    """The bar construction of RT6-M11 (c), in the design-stage
    form: sorted(values)[int(0.99 * len(values))]."""
    ordered = sorted(values)
    return ordered[int(0.99 * len(ordered))]


def holm_adjust(p_by_test):
    """Holm adjustment across the family of tests (spec SS3.2).
    Returns adjusted p per test; a test passes iff its adjusted
    p is below PASS_P."""
    items = sorted(p_by_test.items(), key=lambda kv: kv[1])
    m = len(items)
    adjusted = {}
    running = 0.0
    for i, (name, p) in enumerate(items):
        adj = (m - i) * p
        running = max(running, adj)
        adjusted[name] = min(1.0, running)
    return adjusted


# ------------------------------------------------------------------
# Gate G-1 (spec SS3.7; TC-102-01 recomputation form)
# ------------------------------------------------------------------

def gate_g1(filtered_mer_by_concept, comp_by_concept_by_test):
    """G-1 arithmetic over the frozen filtered vocabulary.
    filtered_mer_by_concept: concept -> Meroitic skeletons (the
    attestation-filtered vocabulary of SS3.2).
    comp_by_concept_by_test: test name -> concept -> comparator
    skeletons. A concept is scored in a test iff the filtered
    vocabulary and that test's comparator set each carry at
    least one form for it (SS3.2). Returns per-test counts and
    the gate verdict; this function computes the gate, it does
    not administer anything."""
    out = {}
    for test, comp in comp_by_concept_by_test.items():
        scored = [
            c for c in filtered_mer_by_concept
            if filtered_mer_by_concept[c] and comp.get(c)
        ]
        outside = [c for c in scored if c not in STAGE_42_TWELVE]
        out[test] = {
            "scored_concepts": len(scored),
            "outside_twelve": len(outside),
            "concepts": sorted(scored),
            "pass": (
                len(scored) >= G1_MIN_CONCEPTS
                and len(outside) >= G1_MIN_OUTSIDE_TWELVE
            ),
        }
    out["gate_pass"] = all(v["pass"] for v in out.values())
    return out


# ------------------------------------------------------------------
# Gate G-2: the operative injection simulation (RT6-M11)
# ------------------------------------------------------------------

def inject_once(mer_by_concept, comp_by_concept, concepts,
                theta, d, rng):
    """One injected comparator set, by the registered
    construction (RT6-M11 (a)): for each scored concept,
    independently, with probability theta the concept is
    designated corresponding, and with probability d the
    correspondence is made detectable, in which case one
    comparator form is appended for that concept, built from
    a Meroitic skeleton of that concept with a trailing "a"
    appended at FORM level. At skeleton level the appended
    form's skeleton is that Meroitic skeleton itself (the
    trailing vowel carries no consonant), so the frozen rule
    scores the pair 2 whenever the skeleton is non-empty.
    Concepts with no non-empty Meroitic skeleton cannot be
    made detectable and are skipped, as the design-stage code
    (which appended skeleton + "a" and re-skeletonised) also
    scored them 0."""
    comp2 = {c: list(comp_by_concept.get(c, [])) for c in concepts}
    for c in concepts:
        if rng.random() < theta and rng.random() < d:
            skels = [s for s in mer_by_concept.get(c, []) if s]
            if skels:
                comp2[c].append(rng.choice(skels))
    return comp2


def injection_power(mer_by_concept, comp_by_concept, concepts,
                    theta, d, freeze_seed, stream,
                    reps=G2_REPLICATES,
                    bar_null_permutations=G2_BAR_NULL_PERMUTATIONS,
                    bar_override=None):
    """Power of T at (theta, d) by the registered method: the
    bar is the 99th percentile of the permutation null of T
    over the frozen lists; a replicate counts as a pass iff
    its injected T strictly exceeds the bar (RT6-M11 (c), and
    tools/design_power_sim.py). Streams derive from the single
    freeze seed: '<stream>:null' for the bar, '<stream>:inj'
    for the replicates."""
    if bar_override is None:
        rng_null = derive_rng(freeze_seed, stream + ":null")
        null = permutation_null(mer_by_concept, comp_by_concept,
                                concepts, bar_null_permutations, rng_null)
        bar = percentile_99(null)
    else:
        bar = bar_override
    rng = derive_rng(freeze_seed, stream + ":inj")
    hits = 0
    for _ in range(reps):
        injected = inject_once(mer_by_concept, comp_by_concept,
                               concepts, theta, d, rng)
        if statistic_T(mer_by_concept, injected, concepts) > bar:
            hits += 1
    return {"power": hits / reps, "bar": bar, "replicates": reps,
            "theta": theta, "d": d}


def gate_g2(mer_by_concept, comp_by_concept_by_test, concepts_by_test,
            freeze_seed):
    """G-2 as registered: at least 80% power at theta = 0.30,
    d = 0.75 for T in EACH family test (spec SS3.7), by the
    RT6-M11 simulation over the frozen lists. Freeze-time only:
    this function is called with frozen lists under a freeze;
    the machinery preparation that filed it called it on no
    real lists."""
    out = {}
    for test, comp in comp_by_concept_by_test.items():
        res = injection_power(mer_by_concept, comp,
                              concepts_by_test[test],
                              G2_THETA, G2_D, freeze_seed,
                              stream="g2:" + test)
        res["pass"] = res["power"] >= G2_MIN_POWER
        out[test] = res
    out["gate_pass"] = all(
        v["pass"] for k, v in out.items() if isinstance(v, dict)
    )
    return out


# ------------------------------------------------------------------
# The prospective binomial bound (spec SS4), carried alongside G-2
# ------------------------------------------------------------------

def _binom_sf(k, n, q):
    """P(X >= k) for X ~ Bin(n, q), exact via math.comb."""
    return sum(
        math.comb(n, i) * q ** i * (1 - q) ** (n - i)
        for i in range(k, n + 1)
    )


def binomial_bound(n, theta=G2_THETA, d=G2_D):
    """Bar and power for the binary statistic at concept count
    n: the smallest bar s with P(S >= s | q0) <= alpha, and the
    power at q = q0 + (1 - q0) * theta * d (spec SS4)."""
    bar = None
    for s in range(0, n + 2):
        if _binom_sf(s, n, BINOMIAL_Q0) <= BINOMIAL_ALPHA:
            bar = s
            break
    q = BINOMIAL_Q0 + (1 - BINOMIAL_Q0) * theta * d
    return {"n": n, "bar": bar, "alpha": _binom_sf(bar, n, BINOMIAL_Q0),
            "power": _binom_sf(bar, n, q)}


# ------------------------------------------------------------------
# Fixture skeleton — TEST FIXTURES ONLY, never a study input
# ------------------------------------------------------------------

_FIXTURE_FOLD = {"ḥ": "h", "ḫ": "x", "ṭ": "t", "ṯ": "t", "š": "s"}


def fixture_skeleton(form):
    """A deliberately simple skeleton for synthetic fixtures:
    case-fold, fold the five diacritic letters of freeze v2 SS7
    by the table above, drop vowels a e i o u. NOT the study
    skeleton (see the module docstring)."""
    out = []
    for ch in form.lower():
        ch = _FIXTURE_FOLD.get(ch, ch)
        if ch not in "aeiou":
            out.append(ch)
    return "".join(out)
