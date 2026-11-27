"""Population builder for the World Language Graph (Spec 108).

Assembles the canonical streams from the filed batch data
under data/ (batches B0-B6), applying the design's type
discipline at assembly: duplicate IDs with differing content
quarantine the later record; cross-batch ID references are
resolved or reported; no record is edited in transit.

Usage: python3 build.py <package_dir>
Emits timestamped progress indicators per batch.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wlg_store import dump_jsonl, load_jsonl, progress  # noqa: E402

BATCHES = ["b0", "b12", "b3", "b4", "b5", "b6"]


def main():
    pkg = sys.argv[1]
    data_dir = os.path.join(pkg, "data")
    graph_dir = os.path.join(pkg, "graph")
    os.makedirs(graph_dir, exist_ok=True)
    merged = {"sources": {}, "nodes": {}, "edges": {}, "assertions": {}}
    quarantine = []
    total_files = sum(
        1 for b in BATCHES for f in
        (os.listdir(os.path.join(data_dir, b)) if os.path.isdir(os.path.join(data_dir, b)) else [])
        if f.endswith(".jsonl"))
    done_files = 0
    for batch in BATCHES:
        bdir = os.path.join(data_dir, batch)
        if not os.path.isdir(bdir):
            continue
        for fname in sorted(os.listdir(bdir)):
            if not fname.endswith(".jsonl"):
                continue
            stream = fname[:-len(".jsonl")]
            if stream not in merged:
                continue
            rows = load_jsonl(os.path.join(bdir, fname))
            id_field = {"sources": "source_id", "nodes": "node_id",
                        "edges": "edge_id", "assertions": "assertion_id"}[stream]
            for i, row in enumerate(rows, 1):
                rid = row[id_field]
                if rid in merged[stream]:
                    if merged[stream][rid] != row:
                        quarantine.append(
                            {"batch": batch, "stream": stream, "id": rid,
                             "reason": "duplicate ID with differing content; "
                                       "first record retained, later quarantined"})
                    continue
                merged[stream][rid] = row
                if i % 50 == 0 or i == len(rows):
                    progress(i, len(rows), f"build batch {batch} {stream}")
            done_files += 1
            progress(done_files, total_files, "build files assembled")
    id_fields = {"sources": "source_id", "nodes": "node_id",
                 "edges": "edge_id", "assertions": "assertion_id"}
    for stream, rows in merged.items():
        dump_jsonl(os.path.join(graph_dir, f"{stream}.jsonl"),
                   list(rows.values()), id_fields[stream])
        progress(len(rows), len(rows), f"stream {stream} written")
    # Cross-reference report: edge endpoints and assertion subjects
    # that resolve to no node or context entity in the release.
    node_ids = set(merged["nodes"])
    dangling = []
    for e in merged["edges"].values():
        for end in (e["subject_id"], e["object_id"]):
            if end not in node_ids:
                dangling.append({"edge_id": e["edge_id"], "endpoint": end})
    for a in merged["assertions"].values():
        if a["subject_id"] not in node_ids and not a["subject_id"].startswith("WLG-"):
            dangling.append({"assertion_id": a["assertion_id"], "endpoint": a["subject_id"]})
    # baseline-links stream: carried from batch B6 as filed.
    bl_src = os.path.join(data_dir, "b6", "baseline-links.jsonl")
    if os.path.exists(bl_src):
        bl = load_jsonl(bl_src)
        dump_jsonl(os.path.join(graph_dir, "baseline-links.jsonl"), bl, "link_id")
        merged["baseline-links"] = {r["link_id"]: r for r in bl}
    report = {
        "counts": {s: len(r) for s, r in merged.items()},
        "quarantine": quarantine,
        "dangling_references": dangling,
    }
    with open(os.path.join(pkg, "records", "build-report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
    progress(1, 1, "build complete")
    print(json.dumps(report["counts"]))
    if dangling:
        print(f"DANGLING REFERENCES: {len(dangling)}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
