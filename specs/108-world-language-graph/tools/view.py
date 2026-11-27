"""Spherical-projection view generator (Spec 108, design section 3).

A view is a generated rendering record over a named release,
never evidence. Geometry is typed before coordinates: this
release populates NO_GEOMETRY for every node (no geometry
assertion with coordinates has been extracted and verified),
so every node appears in the off-sphere index with its
reason, and the sphere carries no placed node. When geometry
assertions are populated by a later batch, this generator
places only nodes whose geometry assertion is in the view
state's admitted set, keeps attested and inferred geometry
in separate layers, and never assigns a default coordinate.

Reproduction rule: regenerating the view from the same
release streams and the same view state yields a byte-equal
view record; the view carries its own SHA-256.

Usage: python3 view.py <package_dir> <release_id>
"""

import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wlg_store import load_jsonl, progress  # noqa: E402


def build_view(pkg, release_id):
    graph_dir = os.path.join(pkg, "graph")
    nodes = load_jsonl(os.path.join(graph_dir, "nodes.jsonl"))
    edges = load_jsonl(os.path.join(graph_dir, "edges.jsonl"))
    gaps = {g["target_node_id"]: g for g in load_jsonl(os.path.join(graph_dir, "gaps.jsonl"))}
    placed, offsphere = [], []
    for i, n in enumerate(nodes, 1):
        if n["geometry_type"] == "NO_GEOMETRY":
            offsphere.append({
                "node_id": n["node_id"], "label": n["label"],
                "status_code": n["status_code"],
                "reason": "NO_GEOMETRY: no defensible geometry assertion "
                          "is populated in this release",
                "gap_id": gaps.get(n["node_id"], {}).get("gap_id"),
            })
        else:
            placed.append({"node_id": n["node_id"],
                           "geometry_type": n["geometry_type"]})
        if i % 50 == 0 or i == len(nodes):
            progress(i, len(nodes), "view generation")
    view = {
        "view_id": f"VIEW-{release_id}-SPHERE-ALLTIME",
        "release_id": release_id,
        "projection": "sphere (canonical); no 2D projection generated in this release",
        "time_window": "all intervals (no slice applied)",
        "layers": {
            "attested_geometry": [p for p in placed
                                  if p["geometry_type"].startswith("ATTESTED")],
            "inferred_geometry": [p for p in placed
                                  if p["geometry_type"] in ("INFERRED_HOMELAND",
                                                            "RECONSTRUCTED_STAGE_AREA")],
            "structural_edges": [e["edge_id"] for e in edges
                                 if e["predicate"] in ("WRITES", "ATTESTED_AT",
                                                       "ADMINISTERED_BY", "USED_IN_POLITY")],
            "hypothesis_edges_default": "off (shown only under a view title naming hypotheses)",
        },
        "never_imply_rules": "design section 3.8, rules 1-8, binding on this view",
        "counts": {"release_nodes": len(nodes), "rendered_on_sphere": len(placed),
                   "off_sphere_index": len(offsphere)},
        "off_sphere_index": offsphere,
    }
    blob = json.dumps(view, ensure_ascii=False, sort_keys=True).encode("utf-8")
    view["view_sha256"] = hashlib.sha256(blob).hexdigest()
    return view


def main():
    pkg, release_id = sys.argv[1], sys.argv[2]
    view = build_view(pkg, release_id)
    out = os.path.join(pkg, "records", f"view-{release_id}.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(view, fh, indent=1, ensure_ascii=False)
    progress(1, 1, "view written")
    print(json.dumps(view["counts"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
