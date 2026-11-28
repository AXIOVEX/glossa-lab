#!/usr/bin/env python3
"""TC-112-09 — revision package form check for Spec 112. Payload verdict = exit code."""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # spec dir
fails = []

bundle = json.load(open(os.path.join(ROOT, "claims-revision.json")))
ids = [c["id"] for c in bundle["claims"]]
want = [f"C112-{i}" for i in range(8, 12)]
if ids != want:
    fails.append(f"bundle ids {ids} != {want}")

claims_md = open(os.path.join(ROOT, "claims.md")).read()
md_ids = re.findall(r"\*\*(C112-\d+) —", claims_md)
want_all = [f"C112-{i}" for i in range(1, 12)]
if md_ids != want_all:
    fails.append(f"claims.md ids {md_ids} != {want_all}")

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

reg = open(os.path.join(ROOT, "records", "revision-registration-2026-11-28.md")).read()
for needle in ["whole-form", "Class W is abolished", "2 distinct host forms",
               "sequence-anchored", "precedence majorities",
               "character-shuffled null", "TC-112-10", "TC-112-11",
               "Every floor, verbatim", "byte-identical"]:
    if needle not in reg:
        fails.append(f"revision registration missing: {needle}")

tc = open(os.path.join(ROOT, "test-cases.md")).read()
for needle in ["TC-112-09", "TC-112-10", "TC-112-11"]:
    if needle not in tc:
        fails.append(f"test-cases.md missing: {needle}")

if fails:
    print("TC-112-09 FAIL")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("TC-112-09 PASS — revision bundle ids/order equal C112-8..C112-11; "
      "falsifiers and does-not-establish lines present in both files; the "
      "revision registration names the three mechanisms and the design "
      "answers and states that no floor, ground-truth set, or scoring "
      "rule changed; TC-112-09..11 filed.")
sys.exit(0)
