#!/usr/bin/env python3
"""Spec 103 conformance addendum — regression tests (TC-103-07, TC-103-08).

Both Round E counterexamples are exercised against the filed
(control) classification and the corrected classification: the
filed code's deviation is asserted as the control result, and the
section 3.4-conforming result is asserted for the corrected code.
The preserved behaviours (unanimous attestation, variant
attestation, the all-absent rule, unavailable witnesses, the
near-locus rules) are asserted for both implementations.

Runnable directly (`python3 conformance-addendum-tests.py`) or
under pytest. No build data is read: all witnesses are synthetic.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "conformance_addendum_script",
    Path(__file__).with_name("conformance-addendum-script.py"))
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def W(wid, kind, tokens, pairs=None, raw=""):
    if pairs is None:
        pairs = [(t, False) for t in tokens]
    return {"id": wid, "kind": kind, "tokens": tokens, "pairs": pairs, "raw": raw}


# ----- TC-103-07: counterexample 1 — witness disagreement -----

def test_counterexample_1_disagreement_is_discrepancy():
    ws = [W("reading:a", "reading", ["soreyi"]),
          W("reading:b", "reading", ["ato"])]
    filed, fv = m.classify_counted_filed(ws, "soreyi")
    corrected, cv = m.classify_counted_corrected(ws, "soreyi")
    assert fv == {"reading:a": "attests_form", "reading:b": "absent"}, fv
    assert filed == "FAITHFUL", filed            # the deviation, as filed
    assert corrected == "DISCREPANCY", corrected  # spec 3.4 as written


def test_preserved_counted_behaviours():
    # unanimous attestation
    ws = [W("expansion:x.jsonl", "expansion", ["ato", "soreyi"])]
    assert m.classify_counted_filed(ws, "soreyi")[0] == "FAITHFUL"
    assert m.classify_counted_corrected(ws, "soreyi")[0] == "FAITHFUL"
    # variant attestation is faithful source spelling (varietas)
    ws = [W("expansion:x.jsonl", "expansion", ["soreya"])]
    assert m.classify_counted_filed(ws, "soreyi")[0] == "FAITHFUL (variant noted)"
    assert m.classify_counted_corrected(ws, "soreyi")[0] == "FAITHFUL (variant noted)"
    # all witnesses absent, expansion among them: discrepancy
    ws = [W("expansion:x.jsonl", "expansion", ["ato", "qore"])]
    assert m.classify_counted_filed(ws, "soreyi")[0] == "DISCREPANCY"
    assert m.classify_counted_corrected(ws, "soreyi")[0] == "DISCREPANCY"
    # all witnesses absent, alternative readings only: uncertain
    ws = [W("reading:a", "reading", ["ato"])]
    assert m.classify_counted_filed(ws, "soreyi")[0] == "UNCERTAIN"
    assert m.classify_counted_corrected(ws, "soreyi")[0] == "UNCERTAIN"
    # no witnesses
    assert m.classify_counted_filed([], "soreyi")[0] == "WITNESS UNAVAILABLE"
    assert m.classify_counted_corrected([], "soreyi")[0] == "WITNESS UNAVAILABLE"


# ----- TC-103-08: counterexample 2 — uncertainty retention -----

def test_counterexample_2_bracketed_witness_is_uncertain():
    pairs = m.expansion_tokens_flagged({"text_corpus": "[soreyi?]"})
    assert pairs == [("soreyi", True)], pairs
    assert m.expansion_tokens({"text_corpus": "[soreyi?]"}) == ["soreyi"]
    ws = [W("expansion:x.jsonl", "expansion", ["soreyi"], pairs=pairs)]
    filed, _ = m.classify_counted_filed(ws, "soreyi")
    corrected, cv = m.classify_counted_corrected(ws, "soreyi")
    assert filed == "FAITHFUL", filed             # the deviation, as filed
    assert cv == {"expansion:x.jsonl": "attests_form_uncertain"}, cv
    assert corrected == "UNCERTAIN", corrected    # spec 3.4 as written


def test_unqualified_witness_stays_unqualified():
    pairs = m.expansion_tokens_flagged({"text_corpus": "soreyi"})
    assert pairs == [("soreyi", False)], pairs
    ws = [W("expansion:x.jsonl", "expansion", ["soreyi"], pairs=pairs)]
    assert m.classify_counted_corrected(ws, "soreyi")[0] == "FAITHFUL"


def test_intra_token_brackets_flag_both_fragments():
    # the filed preprocessing turns the brackets into separators, so
    # so[re]yi fragments to so / re / yi; every fragment is flagged
    pairs = m.expansion_tokens_flagged({"text_corpus": "so[re]yi"})
    assert pairs == [("so", True), ("re", True), ("yi", True)], pairs


def test_reading_markup_flagged():
    pairs = m.reading_tokens_flagged("soreyi? ato")
    assert pairs == [("soreyi", True), ("ato", False)], pairs


# ----- near-locus behaviours -----

def test_near_missed_count_preserved():
    ws = [W("expansion:x.jsonl", "expansion", ["soreyi"])]
    assert m.classify_near_filed(ws, "soreyi", "sorey")[0] == "DISCREPANCY (missed count)"
    assert m.classify_near_corrected(ws, "soreyi", "sorey")[0] == "DISCREPANCY (missed count)"


def test_near_distinct_form_preserved():
    ws = [W("expansion:x.jsonl", "expansion", ["wosi"])]
    want = "FAITHFUL (source carries the distinct near form)"
    assert m.classify_near_filed(ws, "wisi", "wosi")[0] == want
    assert m.classify_near_corrected(ws, "wisi", "wosi")[0] == want


def test_near_uncertain_witness_corrected():
    pairs = m.expansion_tokens_flagged({"text_corpus": "[wosi?]"})
    ws = [W("expansion:x.jsonl", "expansion", ["wosi"], pairs=pairs)]
    want = "FAITHFUL (source carries the distinct near form)"
    assert m.classify_near_filed(ws, "wisi", "wosi")[0] == want  # deviation, as filed
    assert m.classify_near_corrected(ws, "wisi", "wosi")[0] == "UNCERTAIN"


def test_near_disagreement_is_uncertain_when_corrected():
    ws = [W("reading:a", "reading", ["wisi"]),
          W("expansion:x.jsonl", "expansion", ["wosi"])]
    assert m.classify_near_corrected(ws, "wisi", "wosi")[0] == "UNCERTAIN"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"{len(fns)} tests passed")
