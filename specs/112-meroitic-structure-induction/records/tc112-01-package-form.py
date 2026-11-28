#!/usr/bin/env python3
"""TC-112-01 — package form check for Spec 112. Payload verdict = exit code."""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # spec dir
fails = []

bundle = json.load(open(os.path.join(ROOT, "aee-claims.json")))
ids = [c["id"] for c in bundle["claims"]]
want = [f"C112-{i}" for i in range(1, 8)]
if ids != want:
    fails.append(f"bundle ids {ids} != {want}")

claims_md = open(os.path.join(ROOT, "claims.md")).read()
md_ids = re.findall(r"\*\*(C112-\d+) —", claims_md)
if md_ids != want:
    fails.append(f"claims.md ids {md_ids} != {want}")

for c in bundle["claims"]:
    if not c.get("falsification_tests"):
        fails.append(f"{c['id']}: no falsifier in bundle")
    if "Does not establish" not in c.get("text", ""):
        fails.append(f"{c['id']}: no does-not-establish in bundle text")
for cid in want:
    seg = claims_md.split(f"**{cid} —")[1].split("**C112-")[0] if f"**{cid} —" in claims_md else ""
    if "*Falsifier:*" not in seg:
        fails.append(f"{cid}: no falsifier in claims.md")
    if "*Does not establish" not in seg:
        fails.append(f"{cid}: no does-not-establish in claims.md")

spec = open(os.path.join(ROOT, "spec.md")).read()
for needle in ["145af083", "1e91e3a0", "c9158f6865325877112b6b9ceef83b3c80a93c56",
               "**Segmentation.**", "**Recurrent partials.**", "**Formula-slot structure.**",
               "## 4. The conformance preflight (registered floors)",
               "0.80", "90%", "20%",
               "## 5. Relation to Spec 102 and Spec 109 Stage 5",
               "## 6. Execution sequence (registered, not yet run)",
               "## 7. Kill criteria"]:
    if needle not in spec:
        fails.append(f"spec.md missing: {needle}")

if fails:
    print("TC-112-01 FAIL")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("TC-112-01 PASS — ids/order equal C112-1..C112-7; falsifiers and "
      "does-not-establish lines present in both files; spec.md states the corpus "
      "pins, the three targets, the preflight with its floors, the Stage-5 "
      "relation, the execution sequence, and the kill criteria.")
sys.exit(0)
