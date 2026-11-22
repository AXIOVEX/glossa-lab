"""Spec 099 test cases TC-099-01, TC-099-02, TC-099-03.

Run with the repository's test runner or directly:

    python3 -m pytest specs/099-inference-log/tests/test_inference_log.py

The fixtures are synthetic six-entry logs built to the
schema of spec section 3.2; the same validator, checker, and
audit run over the real 94-entry log at Stages 1 and 2, with
their payload verdicts recorded in the spec's records.
"""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "tools" / "inference_log.py"
_spec = importlib.util.spec_from_file_location("inference_log", _TOOL)
il = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(il)


def _item(sign, n, kind, type_, span, targets=None, reason=None,
          target_note=None, target_source=None, statement="fixture item"):
    item = {
        "id": f"{sign}-{n:02d}",
        "kind": kind,
        "type": type_,
        "statement": statement,
        "basis_span": span,
        "targets": targets or [],
    }
    if reason:
        item["reason"] = reason
    if target_note:
        item["target_note"] = target_note
    if target_source:
        item["target_source"] = target_source
    return item


def _entry(sign, reading, cls, flag, basis, items):
    return {
        "sign": sign,
        "reading": reading,
        "executed_class": cls,
        "q4_flag": flag,
        "basis_as_filed": basis,
        "items": items,
        "entry_notes": [],
    }


BASES = {
    "M901": "DEDR 1234 attests the value; collocates with HIGH anchor M902 (n=7)",
    "M902": "collocates with HIGH anchor M901 (n=3)",
    "M903": "consistent INITIAL (n=15); occupies the MEDIAL slot between anchors",
    "M904": "SA-cons=0.31",
    "M905": "freq=2 in the corpus",
    "M906": "Parpola_1994 proposes the value (4 mentions across sources: "
            "Parpola_1994, Mahadevan_1977)",
}


def fixture_log():
    entries = [
        _entry("M901", "fixture-e", "E", "S", BASES["M901"], [
            _item("M901", 1, "dictionary_entry", "a",
                  "DEDR 1234 attests the value"),
            _item("M901", 2, "interpreted_anchor", "b",
                  "collocates with HIGH anchor M902 (n=7)",
                  targets=["M902"],
                  reason="the premise is M902 under its reading"),
        ]),
        _entry("M902", "fixture-i-cycle", "I", "N", BASES["M902"], [
            _item("M902", 1, "interpreted_anchor", "b",
                  "collocates with HIGH anchor M901 (n=3)",
                  targets=["M901"],
                  reason="the premise is M901 under its reading"),
        ]),
        _entry("M903", "fixture-i-slot", "I", "N", BASES["M903"], [
            _item("M903", 1, "positional_statistic", "a",
                  "consistent INITIAL (n=15)"),
            _item("M903", 2, "slot_label", "b",
                  "occupies the MEDIAL slot between anchors",
                  reason="the slot is a candidate-system construct",
                  target_note="the basis names the slot but no "
                              "anchor signs"),
        ]),
        _entry("M904", "fixture-i-ambiguous-only", "I", "N", BASES["M904"], [
            _item("M904", 1, "consistency_score", "ambiguous",
                  "SA-cons=0.31",
                  reason="the score's filed definition does not "
                         "state its inputs"),
        ]),
        _entry("M905", "fixture-u", "U", "N", BASES["M905"], [
            _item("M905", 1, "corpus_count", "a", "freq=2 in the corpus"),
        ]),
        _entry("M906", "fixture-r", "R", "M", BASES["M906"], [
            _item("M906", 1, "published_proposal", "a", BASES["M906"]),
        ]),
    ]
    return {
        "artifact": "inference-log",
        "spec": "099-inference-log",
        "version": "fixture",
        "entries": entries,
    }


def fixture_rows():
    return [{"sign": s, "basis_as_filed": b} for s, b in BASES.items()]


# ------------------------------------------------------------- TC-099-01


def test_tc01_fixture_validates():
    assert il.validate_log(fixture_log()) == []


def test_tc01_duplicate_sign_rejected():
    log = fixture_log()
    log["entries"].append(copy.deepcopy(log["entries"][0]))
    assert any("duplicate" in e for e in il.validate_log(log))


def test_tc01_bad_class_rejected():
    log = fixture_log()
    log["entries"][0]["executed_class"] = "X"
    assert il.validate_log(log)


def test_tc01_kind_type_mismatch_rejected():
    log = fixture_log()
    log["entries"][0]["items"][0]["type"] = "b"
    assert il.validate_log(log)


def test_tc01_invented_span_rejected():
    log = fixture_log()
    log["entries"][0]["items"][0]["basis_span"] = "a clause the basis lacks"
    assert il.validate_log(log)


def test_tc01_b_item_without_reason_rejected():
    log = fixture_log()
    del log["entries"][0]["items"][1]["reason"]
    assert il.validate_log(log)


def test_tc01_b_item_without_target_or_note_rejected():
    log = fixture_log()
    log["entries"][0]["items"][1]["targets"] = []
    assert il.validate_log(log)


def test_tc01_unstated_target_rejected():
    log = fixture_log()
    log["entries"][0]["items"][1]["targets"] = ["M999"]
    assert il.validate_log(log)


def test_tc01_full_mode_requires_94():
    assert il.validate_log(fixture_log(), expect_full=True)


# ------------------------------------------------------------- TC-099-02


def test_tc02_fixture_complete():
    assert il.check_completeness(fixture_log(), fixture_rows()) == []


def test_tc02_deleted_item_detected():
    log = fixture_log()
    del log["entries"][0]["items"][1]  # the M902 collocate premise
    errs = il.check_completeness(log, fixture_rows())
    assert any("collocate" in e and "M901" in e for e in errs)


def test_tc02_uncovered_element_detected():
    log = fixture_log()
    entry = next(e for e in log["entries"] if e["sign"] == "M905")
    entry["basis_as_filed"] = "freq=2 in the corpus; DEDR 999 also cited"
    rows = fixture_rows()
    for row in rows:
        if row["sign"] == "M905":
            row["basis_as_filed"] = entry["basis_as_filed"]
    errs = il.check_completeness(log, rows)
    assert any("dedr" in e and "M905" in e for e in errs)


def test_tc02_missing_row_detected():
    rows = [r for r in fixture_rows() if r["sign"] != "M906"]
    assert il.check_completeness(fixture_log(), rows)


# ------------------------------------------------------------- TC-099-03


def _independent_audit(log):
    """A second implementation of spec section 4, written from
    the spec text for this test: removal, per-class
    recomputation, and SCCs by pairwise reachability (not
    Tarjan)."""
    entries = {e["sign"]: e for e in log["entries"]}
    edges = {s: set() for s in entries}
    for sign, entry in entries.items():
        for item in entry["items"]:
            if item["type"] == "b":
                edges[sign].update(
                    t for t in item.get("targets", []) if t in entries
                )

    def outcome(cls, items, remove):
        lost = [i["id"] for i in items if i["type"] in remove]
        remaining = [i for i in items if i["type"] not in remove]
        if cls == "I" and not remaining:
            return {"class_outcome": "would_change", "destination": "U",
                    "weakened": bool(lost), "lost_items": lost}
        return {"class_outcome": "unchanged", "destination": None,
                "weakened": bool(lost), "lost_items": lost}

    outcomes = {}
    for sign, entry in entries.items():
        p = outcome(entry["executed_class"], entry["items"], {"b"})
        s = outcome(entry["executed_class"], entry["items"], {"b", "ambiguous"})
        outcomes[sign] = {
            "reading": entry["reading"],
            "executed_class": entry["executed_class"],
            "primary": p,
            "sensitivity": s,
            "divergent": p != s,
        }

    def reaches(src, dst):
        seen, stack = set(), [src]
        while stack:
            cur = stack.pop()
            if cur == dst:
                return True
            if cur not in seen:
                seen.add(cur)
                stack.extend(edges[cur])
        return False

    cycles = []
    assigned = set()
    for sign in entries:
        if sign in assigned:
            continue
        comp = sorted(
            t for t in entries
            if t != sign and reaches(sign, t) and reaches(t, sign)
        )
        if comp:
            group = sorted([sign] + comp)
            cycles.append(group)
            assigned.update(group)
    return outcomes, cycles


def test_tc03_independent_recomputation_matches():
    log = fixture_log()
    result = il.audit_log(log)
    outcomes, cycles = _independent_audit(log)
    assert result["outcomes"] == outcomes
    assert result["scc_cycles"] == cycles


def test_tc03_expected_fixture_outcomes():
    result = il.audit_log(fixture_log())
    o = result["outcomes"]
    # E with a (b) item: unchanged, weakened.
    assert o["M901"]["primary"]["class_outcome"] == "unchanged"
    assert o["M901"]["primary"]["weakened"] is True
    # I resting only on a (b) item: would change to U.
    assert o["M902"]["primary"]["class_outcome"] == "would_change"
    assert o["M902"]["primary"]["destination"] == "U"
    # I with an (a) item and an unnamed (b) slot: unchanged, weakened.
    assert o["M903"]["primary"]["class_outcome"] == "unchanged"
    assert o["M903"]["primary"]["weakened"] is True
    # I resting only on an ambiguous item: the primary treatment
    # retains it (unchanged, not weakened); the sensitivity
    # treatment removes it and the class would change to U.
    assert o["M904"]["primary"]["class_outcome"] == "unchanged"
    assert o["M904"]["primary"]["weakened"] is False
    assert o["M904"]["sensitivity"]["class_outcome"] == "would_change"
    assert o["M904"]["sensitivity"]["destination"] == "U"
    assert o["M904"]["sensitivity"]["weakened"] is True
    assert o["M904"]["divergent"] is True
    # U with only an (a) item: unchanged, not weakened.
    assert o["M905"]["primary"]["weakened"] is False
    # R: unchanged.
    assert o["M906"]["primary"]["class_outcome"] == "unchanged"
    # The planted two-node cycle is found; the unnamed slot is
    # an open end.
    assert result["scc_cycles"] == [["M901", "M902"]]
    assert any(e["sign"] == "M903" for e in result["open_ends"])
    # Census.
    assert result["edge_census"] == {
        "a": 4, "b": 3, "ambiguous": 1, "items": 8,
    }
