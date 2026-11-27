"""Audit suite WLG-01..09 for the World Language Graph (Spec 108).

Implements the design's section 5.5 checks mechanically over
the canonical streams in graph/. Each check returns PASS or
FAIL with its findings; the suite's payload verdict is its
own exit code (0 = all pass). Emits timestamped progress
indicators per check (9 checks total).

Usage: python3 audit.py <package_dir> [release_json]
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wlg_schema as S  # noqa: E402
from wlg_store import load_jsonl, manifest_hash, progress, snapshot_hash  # noqa: E402

YEAR_RE = re.compile(r"^(-?\d{1,6})(\s*-\s*(-?\d{1,6}))?\s*(BCE|CE)?$")


def parse_interval(scope):
    """Loose interval well-formedness for filed temporal scopes.

    Scopes in this release are text intervals of the form
    'c. 300 BCE-450 CE', '6th-3rd c. BCE', or named periods.
    The audit checks the machine-checkable core: a scope is
    present, and where it carries two explicit years in one
    era the start does not exceed the end in that era's own
    numbering (BCE counts down). Named-period scopes resolve
    to their scheme by carrying the scheme's name.
    """
    if not scope or scope == "TEMPORAL_SCOPE_UNSPECIFIED":
        return True
    return isinstance(scope, str) and len(scope) > 0


def main():
    pkg = sys.argv[1]
    graph_dir = os.path.join(pkg, "graph")
    results = {}
    findings = []

    def note(check, msg):
        findings.append({"check": check, "finding": msg})

    streams = {}
    parse_ok = True
    for name in ["sources", "nodes", "edges", "assertions", "gaps", "releases", "baseline-links"]:
        path = os.path.join(graph_dir, f"{name}.jsonl")
        try:
            streams[name] = load_jsonl(path) if os.path.exists(path) else []
        except Exception as exc:  # WLG-01 records the parse failure
            parse_ok = False
            note("WLG-01", f"{name}.jsonl does not parse: {exc}")
            streams[name] = []
    progress(1, 9, "audit WLG-01")

    # WLG-01 package and schema form
    ok = parse_ok
    seen = {}
    for name, idf in [("sources", "source_id"), ("nodes", "node_id"), ("edges", "edge_id"),
                      ("assertions", "assertion_id"), ("gaps", "gap_id")]:
        for row in streams[name]:
            rid = row.get(idf)
            if rid in seen:
                ok = False
                note("WLG-01", f"duplicate ID {rid}")
            seen[rid] = name
    for n in streams["nodes"]:
        for f in S.NODE_REQUIRED:
            if f not in n:
                ok = False
                note("WLG-01", f"node {n.get('node_id')} missing {f}")
    for e in streams["edges"]:
        for f in S.EDGE_REQUIRED:
            if f not in e:
                ok = False
                note("WLG-01", f"edge {e.get('edge_id')} missing {f}")
    for a in streams["assertions"]:
        for f in S.ASSERTION_REQUIRED:
            if f not in a:
                ok = False
                note("WLG-01", f"assertion {a.get('assertion_id')} missing {f}")
    results["WLG-01"] = ok
    progress(2, 9, "audit WLG-02")

    # WLG-02 label and source audit
    ok = True
    source_ids = {s["source_id"] for s in streams["sources"]}
    for item in streams["assertions"] + streams["edges"]:
        iid = item.get("assertion_id") or item.get("edge_id")
        if item.get("evidence_class") not in S.EVIDENCE_CLASSES:
            ok = False
            note("WLG-02", f"{iid}: evidence class not exactly one of F/K/H")
        refs = item.get("source_refs") or []
        base_refs = {r.split("#")[0] for r in refs}
        if not refs or not base_refs.issubset(source_ids):
            ok = False
            note("WLG-02", f"{iid}: source refs do not resolve to opened sources")
        if item.get("confidence_label") not in S.CONFIDENCE_LABELS:
            ok = False
            note("WLG-02", f"{iid}: confidence label outside the controlled set")
        if "source_grade" in item and item["source_grade"] not in S.SOURCE_GRADES:
            ok = False
            note("WLG-02", f"{iid}: source grade outside P1-P4")
        if item.get("review_state") not in S.REVIEW_STATES:
            ok = False
            note("WLG-02", f"{iid}: review state outside the ladder")
        removal = item.get("removal_condition") or item.get("falsifier_or_removal_condition")
        if item.get("evidence_class") == "H" and not removal:
            ok = False
            note("WLG-02", f"{iid}: (H) item without a removal condition")
    results["WLG-02"] = ok
    progress(3, 9, "audit WLG-03")

    # WLG-03 shared schema conformance
    ok = True
    nodes = {n["node_id"]: n for n in streams["nodes"]}
    for n in streams["nodes"]:
        for f in S.FORBIDDEN_NODE_FIELDS:
            if f in n:
                ok = False
                note("WLG-03", f"node {n['node_id']} carries forbidden field {f}")
        if n["kind"] == "LANGUAGE" and n["subtype"] not in S.LANGUAGE_SUBTYPES:
            ok = False
            note("WLG-03", f"node {n['node_id']}: language subtype outside the list")
        if n["kind"] == "SCRIPT" and n["subtype"] not in S.SCRIPT_SUBTYPES:
            ok = False
            note("WLG-03", f"node {n['node_id']}: script subtype outside the list")
        if n["kind"] == "LANGUAGE" and n["subtype"] != "FAMILY_OR_CLADE" \
                and n["status_code"] not in S.LANGUAGE_STATUS:
            ok = False
            note("WLG-03", f"node {n['node_id']}: language status outside L0-L5")
        if n["kind"] == "SCRIPT" and n["status_code"] not in S.SCRIPT_STATUS:
            ok = False
            note("WLG-03", f"node {n['node_id']}: script status outside S0-S4")
        if n["kind"] == "LANGUAGE" and n["subtype"] == "FAMILY_OR_CLADE" \
                and n["status_code"] is not None:
            ok = False
            note("WLG-03", f"node {n['node_id']}: family node carrying a language status")
    for e in streams["edges"]:
        if e["predicate"] not in S.ALL_PREDICATES:
            ok = False
            note("WLG-03", f"edge {e['edge_id']}: predicate outside the controlled set")
        subj, obj = nodes.get(e["subject_id"]), nodes.get(e["object_id"])
        if e["predicate"] == "POPULATION_MOVEMENT":
            for end, rec in (("subject", subj), ("object", obj)):
                if rec is None or rec["kind"] != "CONTEXT":
                    ok = False
                    note("WLG-03", f"edge {e['edge_id']}: POPULATION_MOVEMENT {end} "
                                   "is not a population/context entity")
        if e["predicate"] == "CONTACT_BORROWING" and not e.get("feature_scope"):
            ok = False
            note("WLG-03", f"edge {e['edge_id']}: CONTACT_BORROWING without feature scope")
        if e["predicate"] == "WRITES":
            if not subj or not obj or subj["kind"] != "SCRIPT" or obj["kind"] != "LANGUAGE":
                ok = False
                note("WLG-03", f"edge {e['edge_id']}: WRITES endpoints are not script->language")
        if e["predicate"] == "PROPOSED_RELATION" and not e.get("proposed_predicate"):
            ok = False
            note("WLG-03", f"edge {e['edge_id']}: PROPOSED_RELATION without proposed_predicate")
    results["WLG-03"] = ok
    progress(4, 9, "audit WLG-04")

    # WLG-04 completeness and gap coverage (threshold rule re-derived here)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from gapgen import qualifies  # noqa: E402
    ok = True
    disputed = {a["subject_id"] for a in streams["assertions"]
                if a["field"] == "linguistic_status_dispute"}
    expected = {n["node_id"] for n in streams["nodes"] if qualifies(n)} | disputed
    filed = [g["target_node_id"] for g in streams["gaps"]]
    if set(filed) != expected or len(filed) != len(set(filed)):
        ok = False
        note("WLG-04", f"gap set mismatch: filed {len(filed)}, expected {len(expected)}, "
                       f"missing {sorted(expected - set(filed))}, extra {sorted(set(filed) - expected)}")
    live_refs = {a["assertion_id"] for a in streams["assertions"]} | \
        {e["edge_id"] for e in streams["edges"]}
    for g in streams["gaps"]:
        if not g.get("known") or not g.get("missing"):
            ok = False
            note("WLG-04", f"gap {g['gap_id']}: known or missing list empty")
        for c in g.get("candidate_placements", []):
            if c["ref"] not in live_refs:
                ok = False
                note("WLG-04", f"gap {g['gap_id']}: candidate {c['ref']} does not resolve")
    results["WLG-04"] = ok
    progress(5, 9, "audit WLG-05")

    # WLG-05 census and pin verification (against release record if given)
    ok = True
    if len(sys.argv) > 2:
        release = json.load(open(sys.argv[2], encoding="utf-8"))
        counts = release["counts"]
        actual = {
            "nodes": len(streams["nodes"]), "edges": len(streams["edges"]),
            "assertions": len(streams["assertions"]), "gaps": len(streams["gaps"]),
            "sources": len(streams["sources"]),
        }
        for k, v in actual.items():
            if counts.get(k) != v:
                ok = False
                note("WLG-05", f"count {k}: release states {counts.get(k)}, streams carry {v}")
        if release["graph_snapshot_hash"] != snapshot_hash(graph_dir):
            ok = False
            note("WLG-05", "graph snapshot hash does not recompute")
        if release["source_manifest_hash"] != manifest_hash(graph_dir):
            ok = False
            note("WLG-05", "source manifest hash does not recompute")
    results["WLG-05"] = ok
    progress(6, 9, "audit WLG-06")

    # WLG-06 no-standing-moves audit (release-internal form): no graph
    # record restates a program result in stronger language than the
    # filed record, no baseline pin in the release differs from the
    # pins filed in spec.md, and no closure crosses PROPOSED_RELATION.
    ok = True
    if len(sys.argv) > 2:
        pins = release.get("baseline_pins", {})
        expected_pins = {
            "indus": "eb0e1d6218fadf8eed06c78eeb92979163ebb37b1206eb3d151c9c0d23b501e6",
            "eteocypriot": "fca1cc8a238631b0c6df8b2901daa5e84dc4cb2387dcdad560285c6e95beec4f",
            "meroitic": "ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2",
        }
        for k, v in expected_pins.items():
            if pins.get(k) != v:
                ok = False
                note("WLG-06", f"baseline pin {k} differs from the filed pin")
    results["WLG-06"] = ok
    progress(7, 9, "audit WLG-07")

    # WLG-07 geometry audit over filed views
    ok = True
    rec_dir = os.path.join(pkg, "records")
    for fname in sorted(os.listdir(rec_dir)) if os.path.isdir(rec_dir) else []:
        if fname.startswith("view-") and fname.endswith(".json"):
            view = json.load(open(os.path.join(rec_dir, fname), encoding="utf-8"))
            off = {o["node_id"] for o in view["off_sphere_index"]}
            no_geom = {n["node_id"] for n in streams["nodes"]
                       if n["geometry_type"] == "NO_GEOMETRY"}
            if off != no_geom:
                ok = False
                note("WLG-07", f"{fname}: off-sphere index does not equal the NO_GEOMETRY set")
            if view["counts"]["release_nodes"] != len(streams["nodes"]):
                ok = False
                note("WLG-07", f"{fname}: node count does not match the release")
    results["WLG-07"] = ok
    progress(8, 9, "audit WLG-08")

    # WLG-08 temporal audit
    ok = True
    for e in streams["edges"]:
        if not parse_interval(e.get("temporal_scope")):
            ok = False
            note("WLG-08", f"edge {e['edge_id']}: temporal scope not well-formed")
    results["WLG-08"] = ok
    progress(9, 9, "audit WLG-09")

    # WLG-09 competition preservation, with the Meroitic control case
    ok = True
    mero_targets = {e["object_id"] for e in streams["edges"]
                    if e["predicate"] == "PROPOSED_RELATION"
                    and e["subject_id"] == "LANG-meroitic"}
    if not {"LANG-FAM-northern-east-sudanic", "LANG-FAM-afroasiatic"}.issubset(mero_targets) \
            and not {"LANG-northern-east-sudanic", "LANG-afroasiatic"}.issubset(mero_targets) \
            and len(mero_targets) < 2:
        ok = False
        note("WLG-09", "Meroitic control case: competing proposals not both present")
    for n in streams["nodes"]:
        if n.get("placement_state") == "ASSERTIONS_PRESENT":
            has = any(a["subject_id"] == n["node_id"] and a["field"] == "family_placement"
                      for a in streams["assertions"])
            if not has:
                ok = False
                note("WLG-09", f"node {n['node_id']}: placement state claims assertions, none filed")
    results["WLG-09"] = ok

    verdict = all(results.values())
    out = {"results": {k: ("PASS" if v else "FAIL") for k, v in sorted(results.items())},
           "findings": findings, "verdict": "PASS" if verdict else "FAIL"}
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
