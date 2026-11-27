import json
import sys

pkg = sys.argv[1]
gaps = [json.loads(l) for l in open(f"{pkg}/graph/gaps.jsonl")]
nodes = {}
for l in open(f"{pkg}/graph/nodes.jsonl"):
    n = json.loads(l)
    nodes[n["node_id"]] = n
lines = [
    "# World Language Graph - Gap Register (Release WLG-R1, 2026-11-27)",
    "",
    "Generated mechanically by tools/gapgen.py from the release streams "
    "under the design section 4.2 rule; the machine form is graph/gaps.jsonl "
    "and governs. Within a band, order is a work order, not a likelihood.",
    "",
]
for g in sorted(gaps, key=lambda g: (g["priority"]["owner_priority"], g["target_node_id"])):
    n = nodes[g["target_node_id"]]
    parts = []
    for c in g["candidate_placements"]:
        parts.append(f"{c.get('target', c['ref'])} (band {c['band']})")
    cands = ", ".join(parts) or "none"
    lines.append(f"## {n['label']} - {g['current_status']} - {g['gap_kind']}")
    lines.append(
        f"- Target: {g['target_node_id']}; blockers: {', '.join(g['blockers'])}; "
        f"priority: owner {g['priority']['owner_priority']}, "
        f"readiness {g['priority']['readiness']}; state: {g['lifecycle_state']}")
    lines.append(f"- Missing: {', '.join(g['missing'])}")
    lines.append(f"- Candidates: {cands}")
    lines.append("")
open(f"{pkg}/records/gap-register-release-1-2026-11-27.md", "w").write("\n".join(lines))
print(f"gap register md: {len(gaps)} entries")
