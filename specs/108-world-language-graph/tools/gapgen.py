"""Gap-register generator (Spec 108, design section 4).

Generates exactly one gap entry for every node meeting a
section 4.2 threshold, from the release's own status
assessments. Candidate references resolve to placement
assertions on the node and PROPOSED_RELATION edges that
target it; bands come from the filed band records in
data/b6/gap-bands.json where present, else from the
mechanical default: a proposal carrying a basis and a
falsifier stands in band C; one without stands in band D.
No probability is computed anywhere in this generator.

Usage: python3 gapgen.py <package_dir>
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wlg_store import dump_jsonl, load_jsonl, progress  # noqa: E402

KNOWN_FIELDS = {"corpus_description", "known_summary", "decipherment_history",
                "corpus_count_text"}
SCRIPT_MISSING = {
    "S0": ["SIGN_VALUES", "SEGMENTATION", "BILINGUAL_OR_PARALLEL"],
    "S1": ["SIGN_VALUES", "BILINGUAL_OR_PARALLEL"],
    "S2": ["SIGN_VALUES", "GENRE_BREADTH"],
}
LANG_MISSING = {
    "L0": ["LEXICON", "GRAMMAR", "RELATED_LANGUAGE_IDENTIFICATION", "CORPUS_SIZE"],
    "L1": ["LEXICON", "GRAMMAR", "RELATED_LANGUAGE_IDENTIFICATION", "CORPUS_SIZE"],
    "L2": ["LEXICON", "GRAMMAR", "RELATED_LANGUAGE_IDENTIFICATION"],
    "L3": ["RELATED_LANGUAGE_IDENTIFICATION"],
}


def qualifies(node):
    if node["kind"] == "SCRIPT" and node["status_code"] in ("S0", "S1", "S2"):
        return True
    if node["kind"] == "LANGUAGE" and node["status_code"] in ("L0", "L1", "L2"):
        return True
    if (node["kind"] == "LANGUAGE" and node["status_code"] == "L3"
            and node["placement_state"] == "PLACEMENT_UNRESOLVED"):
        return True
    if node["subtype"] == "INFERRED_UNKNOWN":
        return True
    return False


def main():
    pkg = sys.argv[1]
    graph_dir = os.path.join(pkg, "graph")
    nodes = load_jsonl(os.path.join(graph_dir, "nodes.jsonl"))
    assertions = load_jsonl(os.path.join(graph_dir, "assertions.jsonl"))
    edges = load_jsonl(os.path.join(graph_dir, "edges.jsonl"))
    bands = {}
    bpath = os.path.join(pkg, "data", "b6", "gap-bands.json")
    if os.path.exists(bpath):
        bands = json.load(open(bpath, encoding="utf-8"))
    disputed = {a["subject_id"] for a in assertions
                if a["field"] == "linguistic_status_dispute"}
    targets = [n for n in nodes if qualifies(n) or n["node_id"] in disputed]
    gaps = []
    for i, node in enumerate(targets, 1):
        nid = node["node_id"]
        known = [a["assertion_id"] for a in assertions
                 if a["subject_id"] == nid and a["field"] in KNOWN_FIELDS]
        cands = []
        for a in assertions:
            if a["subject_id"] == nid and a["field"] == "family_placement":
                cands.append({"ref": a["assertion_id"], "kind": "placement_assertion",
                              "band": bands.get(a["assertion_id"], "B")})
        for e in edges:
            if e["predicate"] == "PROPOSED_RELATION" and e["subject_id"] == nid:
                band = bands.get(e["edge_id"])
                if band is None:
                    band = "C" if (e.get("basis") and e.get("falsifier_or_removal_condition")) else "D"
                cands.append({"ref": e["edge_id"], "kind": "proposed_relation",
                              "band": band, "target": e["object_id"]})
        band_order = {"A": 0, "B": 1, "C": 2, "D": 3}
        cands.sort(key=lambda c: band_order[c["band"]])
        if node["kind"] == "SCRIPT" and nid in disputed:
            kind = "LINGUISTIC_STATUS_DISPUTED"
        elif node["kind"] == "SCRIPT":
            kind = "SCRIPT_UNDECIPHERED"
        elif node["status_code"] == "L3":
            kind = "CLASSIFICATION_UNRESOLVED"
        else:
            kind = "LANGUAGE_NOT_UNDERSTOOD"
        missing = (SCRIPT_MISSING.get(node["status_code"]) if node["kind"] == "SCRIPT"
                   else LANG_MISSING.get(node["status_code"])) or []
        override = bands.get(f"gap:{nid}", {})
        gaps.append({
            "gap_id": f"GAP-{nid}",
            "target_node_id": nid,
            "gap_kind": kind,
            "current_status": node["status_code"],
            "known": known,
            "missing": override.get("missing", missing),
            "blockers": override.get("blockers", ["INFORMATION"]),
            "candidate_placements": cands,
            "movement_conditions": override.get("movement_conditions", []),
            "priority": override.get("priority", {
                "owner_priority": 3, "readiness": "PARTIAL",
                "blocker_class": override.get("blockers", ["INFORMATION"])[0]}),
            "linked_tests": override.get("linked_tests", []),
            "custody_and_access": override.get("custody_and_access", "none recorded"),
            "lifecycle_state": override.get("lifecycle_state", "OPEN"),
            "last_reviewed": "release 1 (2026-11-27)",
        })
        if i % 20 == 0 or i == len(targets):
            progress(i, len(targets), "gap register generated")
    dump_jsonl(os.path.join(graph_dir, "gaps.jsonl"), gaps, "gap_id")
    progress(len(gaps), len(gaps), "gap register written")
    print(f"gaps: {len(gaps)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
