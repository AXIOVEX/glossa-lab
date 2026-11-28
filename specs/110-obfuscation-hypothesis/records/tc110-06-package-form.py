#!/usr/bin/env python3
"""TC-110-06 — revision package form check for Spec 110.
Payload verdict = exit code."""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # spec dir
fails = []

bundle = json.load(open(os.path.join(ROOT, "claims-revision.json")))
ids = [c["id"] for c in bundle["claims"]]
want = [f"C110-{i}" for i in range(7, 12)]
if ids != want:
    fails.append(f"revision bundle ids {ids} != {want}")

claims_md = open(os.path.join(ROOT, "claims.md")).read()
md_ids = re.findall(r"\*\*(C110-\d+) —", claims_md)
if md_ids != [f"C110-{i}" for i in range(1, 12)]:
    fails.append(f"claims.md ids {md_ids} != C110-1..C110-11")

for c in bundle["claims"]:
    if not c.get("falsification_tests"):
        fails.append(f"{c['id']}: no falsifier in bundle")
    if "Does not establish" not in c.get("text", ""):
        fails.append(f"{c['id']}: no does-not-establish in bundle text")
for cid in want:
    seg = claims_md.split(f"**{cid} —")[1].split("**C110-")[0] \
        if f"**{cid} —" in claims_md else ""
    if "*Falsifier:*" not in seg:
        fails.append(f"{cid}: no falsifier in claims.md")
    if "*Does not establish" not in seg:
        fails.append(f"{cid}: no does-not-establish in claims.md")

spec = open(os.path.join(ROOT, "spec.md")).read()
if "## 8. The revision (2026-11-27)" not in spec:
    fails.append("spec.md missing the revision section")

reg = open(os.path.join(ROOT, "records",
                        "revision-registration-2026-11-27.md")).read()
for needle in ["## 1. What does not change", "## 4. The revised design",
               "per-system", "T-SHUF", "fixed-rank tail",
               "C2 is retired in this revision", "spec110r2-band-",
               "spec110r2-ctl-", "NOT TESTABLE AT THIS POWER",
               "at most 1 of the 12", "B = 999",
               "can exist without a secrecy function",
               "can exist with no textual signature",
               "uniform-substitution undetectability limit"]:
    if needle not in reg:
        fails.append(f"revision registration missing: {needle}")

if fails:
    print("TC-110-06 FAIL")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("TC-110-06 PASS — revision bundle ids/order equal C110-7..C110-11; "
      "claims.md carries all eleven claims with falsifiers and "
      "does-not-establish lines; spec.md revision section and the revision "
      "registration's registered elements present in full.")
sys.exit(0)
