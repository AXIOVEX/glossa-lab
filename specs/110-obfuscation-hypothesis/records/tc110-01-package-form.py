#!/usr/bin/env python3
"""TC-110-01 — package form check for Spec 110. Payload verdict = exit code."""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # spec dir
fails = []

bundle = json.load(open(os.path.join(ROOT, "aee-claims.json")))
ids = [c["id"] for c in bundle["claims"]]
want = [f"C110-{i}" for i in range(1, 7)]
if ids != want:
    fails.append(f"bundle ids {ids} != {want}")

claims_md = open(os.path.join(ROOT, "claims.md")).read()
md_ids = re.findall(r"\*\*(C110-\d+) —", claims_md)
if md_ids != want:
    fails.append(f"claims.md ids {md_ids} != {want}")

for c in bundle["claims"]:
    if not c.get("falsification_tests"):
        fails.append(f"{c['id']}: no falsifier in bundle")
    if "Does not establish" not in c.get("text", ""):
        fails.append(f"{c['id']}: no does-not-establish in bundle text")
for cid in want:
    seg = claims_md.split(f"**{cid} —")[1].split("**C110-")[0] if f"**{cid} —" in claims_md else ""
    if "*Falsifier:*" not in seg:
        fails.append(f"{cid}: no falsifier in claims.md")
    if "*Does not establish" not in seg:
        fails.append(f"{cid}: no does-not-establish in claims.md")

spec = open(os.path.join(ROOT, "spec.md")).read()
for needle in ["## 1. The hypothesis", "## 2. What deliberate obfuscation",
               "## 3. The battery", "## 4. The gate", "## 5. Corpora",
               "## 6. Verdicts and standing", "## 7. Kill criteria"]:
    if needle not in spec:
        fails.append(f"spec.md missing: {needle}")

reg = open(os.path.join(ROOT, "records", "registration-2026-11-27.md")).read()
for needle in ["## 2. Statistics", "## 3. Bands and thresholds",
               "## 4. The control gate", "## 5. Verdict rules",
               "## 6. Corpora and handling", "NOT TESTABLE AT THIS POWER",
               "B = 999", "11001"]:
    if needle not in reg:
        fails.append(f"registration missing: {needle}")

if fails:
    print("TC-110-01 FAIL")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("TC-110-01 PASS — ids/order equal C110-1..C110-6; falsifiers and "
      "does-not-establish lines present in both files; spec.md sections and "
      "registration elements present in full.")
sys.exit(0)
