#!/usr/bin/env python3
"""Spec 102 — fixture tests for tools/execution_machinery.py.

SYNTHETIC FIXTURES ONLY. Every expected value in this file was
computed independently of the machinery: by hand from the
registered rule text (spec SS3.2), from the filed TC-102-07
table (test-cases.md), by exact enumeration with itertools, or
from the prospective binomial table printed in spec SS4 itself.
No real concept list, vocabulary, or comparator list appears
here; no Meroitic form is scored; no power figure for any real
list is computed.
"""

import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import execution_machinery as em


# --- TC-102-07: the split construction, against its filed table ---

TC10207 = [
    ("ato", "1f3924e248a2b980d52b2377dcb6a526e7d2953b04513ccfc2edf0ff15c74e2d", 7, "held-out"),
    ("mk lb", "dc3d011961afa4289598b90d308e39a8a5f34813f5f7d4af475d12c4321e3147", 3, "held-out"),
    ("qore kdi ste", "39832e505bdfc025077c1f7aafe47d76e40de22471f148b242beb69088e90bb8", 0, "development"),
    ("REM 1003 Akinidad stela text", "39716c8af11f898ffb36de94eb501ffe5953b03d2ed0970898f018d2bf034e83", 9, "held-out"),
    ("bedewi ato mk", "6aa442f449ca7fd04e478e36feef2ff2ae3020977107ccf9278276247b0adc54", 0, "development"),
]
EXAMPLE_SALT = b"spec102-split-example-salt-2026-11-22"


def test_split_construction_tc10207():
    for text, digest, residue, side in TC10207:
        got = em.split_assignment(text, EXAMPLE_SALT)
        assert got["digest"] == digest, text
        assert got["residue"] == residue, text
        assert got["side"] == side, text


# --- SS3.2 pair rule, hand-computed cases ---

def test_pair_score_hand_cases():
    assert em.pair_score("ktb", "kt") == 2   # first and second equal
    assert em.pair_score("ktb", "k") == 2    # either skeleton length 1
    assert em.pair_score("s", "sr") == 2     # either skeleton length 1
    assert em.pair_score("ktb", "kb") == 1   # first only
    assert em.pair_score("ktb", "sb") == 0   # first differs
    assert em.pair_score("", "kt") == 0      # empty skeleton
    assert em.pair_score("kt", "") == 0


def test_statistic_T_and_S_hand_computed():
    mer = {1: ["ktb"], 2: ["s"], 3: ["mn"]}
    comp = {1: ["kb"], 2: ["sr"], 3: ["tn"]}
    # concept 1: 1 (first only); concept 2: 2 (length-1); concept 3: 0
    assert em.statistic_T(mer, comp, [1, 2, 3]) == 3
    assert em.statistic_S_binary(mer, comp, [1, 2, 3]) == 1


# --- Permutation null: exact enumeration, computed independently ---

def test_permutation_null_exact_enumeration():
    mer = {1: ["k"], 2: ["t"]}
    comp = {1: ["k"], 2: ["t"]}
    concepts = [1, 2]
    # Independent enumeration: the two assignments of the pool
    # [k, t] to concepts (1, 2) give T = 4 and T = 0.
    expected = []
    for perm in set(itertools.permutations(["k", "t"])):
        sh = {1: [perm[0]], 2: [perm[1]]}
        expected.append(em.statistic_T(mer, sh, concepts))
    assert sorted(expected) == [0, 4]
    rng = em.derive_rng(12345, "fixture-null")
    null = em.permutation_null(mer, comp, concepts, 400, rng)
    assert set(null) == {0, 4}
    frac4 = null.count(4) / len(null)
    assert 0.35 < frac4 < 0.65  # both assignments recur ~equally


def test_permutation_p_value_form():
    # (1 + #{perm >= obs}) / (1 + nperm), freeze v2 SS4 form
    assert em.permutation_p_value(4, [0, 4, 0, 4]) == 0.6
    assert em.permutation_p_value(5, [0, 4, 0, 4]) == 0.2


def test_percentile_99_design_form():
    assert em.percentile_99(list(range(100))) == 99


# --- Holm adjustment, hand-computed ---

def test_holm_hand_cases():
    adj = em.holm_adjust({"R1": 0.004, "R2": 0.03})
    assert abs(adj["R1"] - 0.008) < 1e-12
    assert abs(adj["R2"] - 0.03) < 1e-12
    adj2 = em.holm_adjust({"R1": 0.006, "R2": 0.006})
    assert abs(adj2["R1"] - 0.012) < 1e-12
    assert abs(adj2["R2"] - 0.012) < 1e-12


# --- G-1 arithmetic on a synthetic vocabulary ---

def test_gate_g1_synthetic():
    mer = {1000 + i: ["k"] for i in range(45)}       # 45 concepts
    comp_r1 = {1000 + i: ["k"] for i in range(45)}   # R1 covers all
    comp_r2 = {1000 + i: ["k"] for i in range(39)}   # R2 covers 39
    out = em.gate_g1(mer, {"R1": comp_r1, "R2": comp_r2})
    assert out["R1"]["scored_concepts"] == 45
    assert out["R1"]["outside_twelve"] == 45
    assert out["R1"]["pass"] is True
    assert out["R2"]["scored_concepts"] == 39
    assert out["R2"]["pass"] is False
    assert out["gate_pass"] is False


def test_gate_g1_twelve_counted_correctly():
    mer = {c: ["k"] for c in em.STAGE_42_TWELVE}     # only the twelve
    comp = {c: ["k"] for c in em.STAGE_42_TWELVE}
    out = em.gate_g1(mer, {"R1": comp})
    assert out["R1"]["scored_concepts"] == 12
    assert out["R1"]["outside_twelve"] == 0
    assert out["R1"]["pass"] is False


# --- Injection construction: deterministic extremes ---

def test_injection_extremes():
    mer = {1: ["kt"], 2: ["mn"]}
    comp = {1: [], 2: []}
    # theta = d = 1: every concept is made detectable, T = 4 always
    res = em.injection_power(mer, comp, [1, 2], 1.0, 1.0,
                             freeze_seed=7, stream="fixture",
                             reps=50, bar_override=3)
    assert res["power"] == 1.0
    # theta = 0: nothing is injected, T = 0, and 0 does not
    # strictly exceed a bar of 0
    res0 = em.injection_power(mer, comp, [1, 2], 0.0, 0.75,
                              freeze_seed=7, stream="fixture",
                              reps=50, bar_override=0)
    assert res0["power"] == 0.0


def test_seed_determinism():
    mer = {1: ["kt"], 2: ["mn"], 3: ["sb"]}
    comp = {1: ["kb"], 2: ["tn"], 3: ["s"]}
    kw = dict(reps=40, bar_null_permutations=40)
    a = em.injection_power(mer, comp, [1, 2, 3], 0.3, 0.75,
                           freeze_seed=99, stream="fixture", **kw)
    b = em.injection_power(mer, comp, [1, 2, 3], 0.3, 0.75,
                           freeze_seed=99, stream="fixture", **kw)
    assert a == b


# --- The binomial bound against spec SS4's own printed table ---

def test_binomial_bound_matches_spec_table():
    # spec SS4: N=30 -> bar 10, power 0.52; N=40 -> 12, 0.68;
    # N=50 -> 14, 0.78 (powers as printed, two decimals)
    for n, bar, power in ((30, 10, 0.52), (40, 12, 0.68), (50, 14, 0.78)):
        out = em.binomial_bound(n)
        assert out["bar"] == bar, n
        assert abs(out["power"] - power) < 0.011, n
        assert out["alpha"] <= 0.005, n


# --- Fixture skeleton sanity (fixture only) ---

def test_fixture_skeleton():
    assert em.fixture_skeleton("Ktb") == "ktb"
    assert em.fixture_skeleton("ato") == "t"
    assert em.fixture_skeleton("šḥ") == "sh"


if __name__ == "__main__":
    tests = [(k, v) for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    for i, (name, fn) in enumerate(tests, 1):
        fn()
        print("[{}/{}] PASS {}".format(i, len(tests), name))
    print("ALL {} FIXTURE TESTS PASS".format(len(tests)))
