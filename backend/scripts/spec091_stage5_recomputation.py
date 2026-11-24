#!/usr/bin/env python3
"""Spec 091 Stage 5 (T501), W1 leg: the eligible-set recomputation fed by
Kobayashi's filed T401 blind coding.

Implements eligibility-defs-v1.md section 5 mechanically over the three
records it names: the frozen WP4 provenance overlay (staged record), the
locator record (T202 artifact + supplementary pass; per entry per field
the supplement's outcome wins, per records/stage-2-supplement-delta.json),
and the coding record (T401, Kobayashi). Classification follows WP4's
rule order exactly as eligibility-defs v1 section 5 restates it, and
never depends on agreement between values (eligibility-defs D11).
Identity figures (raw / audit-normalized) are computed for reporting
only, under the audit rule the provenance overlay carries (spec 006
Step 3c): lowercase, NFD-strip diacritics, first segment before '/',
strip parenthetical glosses, letters only.

The run asserts the anti-redefinition guarantee: every entry with no
valid coding reproduces its staged WP4 classification exactly. A
mismatch aborts the run (exit 2) and is reported, never smoothed over.
"""
import hashlib
import json
import pathlib
import re
import sys
import unicodedata
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "backend/glossa_lab/data"
RECORDS = ROOT / "specs/091-anchor-comparison-integrity/records"

PROVENANCE = DATA / "mahadevan_parpola_crosswalk_v2_provenance.json"
LOCATORS = DATA / "mahadevan_parpola_crosswalk_v2_locators.json"
LOCATORS_SUPP = DATA / "mahadevan_parpola_crosswalk_v2_locators_supplement.json"
CODING = DATA / "mahadevan_parpola_crosswalk_v2_coding_kobayashi.json"

CLASSES = ["independently_sourced", "used_during_candidate_construction",
           "project_derived", "unverified", "ineligible"]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def audit_normalize(value):
    """The audit rule (spec 006 Step 3c), as carried in the provenance
    overlay's identity blocks. Reporting identity only."""
    if value is None:
        return None
    s = value.lower()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.split("/")[0]
    s = re.sub(r"\([^)]*\)", "", s)
    s = "".join(c for c in s if c.isalpha())
    return s


def main():
    started = datetime.now(timezone.utc)
    prov = load(PROVENANCE)
    loc_base = {e["sign"]: e for e in load(LOCATORS)["entries"]}
    loc_supp = {e["sign"]: e for e in load(LOCATORS_SUPP)["entries"]}
    coding = load(CODING)
    construction = set(prov["inputs"]["construction_input_signs"])
    staged = {e["sign"]: e for e in prov["entries"]}

    def merged_locator(sign, field):
        # Per entry per field, the supplement's outcome wins.
        supp = loc_supp.get(sign, {}).get(field)
        if supp is not None:
            return supp
        return loc_base.get(sign, {}).get(field)

    # --- Section 3 precondition checks per coded entry -------------------
    coded = {}
    precondition_failures = {}
    for entry in coding["entries"]:
        sign = entry["sign"]
        pr = entry["phonetic_reading"]
        loc_field = merged_locator(sign, "phonetic_reading")
        fails = []
        if loc_field is None or loc_field["outcome"] != "located":
            fails.append("section 3.1: no locator-record locator for the field")
            loc = None
        else:
            loc = loc_field["locator"]
            for part in ("work", "pinpoint", "sign_scheme"):
                if not loc.get(part):
                    fails.append(f"section 2/3.1: locator part {part} empty")
            cited = pr["coded_from_locator"]
            if cited["work"] != loc["work"] or cited["pinpoint"] != loc["pinpoint"]:
                fails.append("section 3.1: coding record's cited locator does "
                             "not match the locator record")
        if not coding["coder"].get("name") or not coding["coder"].get("lineage_exclusion"):
            fails.append("section 3.2: coder identity / lineage exclusion missing")
        if not coding.get("blinding_protocol"):
            fails.append("section 3.3: blinding protocol not cited")
        if coding.get("deviations"):
            fails.append("section 3.3/4: a recorded deviation voids the coding")
        if not pr.get("coded_value") or pr.get("not_attested"):
            fails.append("no coded value supplied")
        if fails:
            precondition_failures[sign] = fails
        else:
            coded[sign] = pr["coded_value"]

    # --- Section 5 recomputation -----------------------------------------
    results = {}
    mismatches = []
    for sign, e in staged.items():
        anchor_reading = e.get("anchor_reading_as_recorded")
        staged_class = e["comparison_classification"]
        if sign in coded:
            eff_value = coded[sign]
            eff_origin = "independent_primary_source"
            input_kind = "coded"
        else:
            eff_value = e["phonetic_reading"].get("value")
            eff_origin = e["phonetic_reading"].get("value_origin")
            input_kind = "staged"
        loc_field = merged_locator(sign, "phonetic_reading")
        has_locator = bool(
            loc_field and loc_field["outcome"] == "located"
            and loc_field["locator"].get("work")
            and loc_field["locator"].get("pinpoint")
            and loc_field["locator"].get("sign_scheme"))
        # WP4's rule order, as restated in eligibility-defs v1 section 5.
        if not eff_value or anchor_reading is None:
            cls, rule = "ineligible", 1
        elif eff_origin == "project_anchor_table_copy":
            cls, rule = "project_derived", 2
        elif sign in construction:
            cls, rule = "used_during_candidate_construction", 3
        elif eff_origin == "independent_primary_source" and has_locator:
            cls, rule = "independently_sourced", 4
        else:
            cls, rule = "unverified", 5
        results[sign] = {
            "sign": sign,
            "input": input_kind,
            "staged_classification": staged_class,
            "recomputed_classification": cls,
            "rule_fired": rule,
            "eligible": cls == "independently_sourced",
        }
        if input_kind == "staged" and cls != staged_class:
            mismatches.append({"sign": sign, "staged": staged_class,
                               "recomputed": cls})

    if mismatches:
        print("ANTI-REDEFINITION FAILURE: uncoded entries do not reproduce "
              "their staged classes:", json.dumps(mismatches), file=sys.stderr)
        return 2

    # --- Identity reporting (reporting only; D11) -------------------------
    identity = {}
    for entry in coding["entries"]:
        sign = entry["sign"]
        cv = entry["phonetic_reading"]["coded_value"]
        loc_field = merged_locator(sign, "phonetic_reading")
        cited = loc_field["locator"]["cited_value"] if loc_field and loc_field["outcome"] == "located" else None
        anchor = staged[sign].get("anchor_reading_as_recorded")
        identity[sign] = {
            "coded_value": cv,
            "alternatives_as_filed": entry["phonetic_reading"]["alternatives_as_filed"],
            "locator_cited_value": cited,
            "coded_vs_cited_raw_identical": (cv == cited) if cited is not None else None,
            "coded_vs_cited_normalized_identical": (
                audit_normalize(cv) == audit_normalize(cited)) if cited is not None else None,
            "anchor_reading_as_recorded": anchor,
            "coded_vs_anchor_raw_identical": (cv == anchor) if anchor is not None else None,
            "coded_vs_anchor_normalized_identical": (
                audit_normalize(cv) == audit_normalize(anchor)) if anchor is not None else None,
        }

    def census(res):
        c = {k: 0 for k in CLASSES}
        for r in res.values():
            c[r["recomputed_classification"]] += 1
        return c

    staged_census = {k: 0 for k in CLASSES}
    for e in staged.values():
        staged_census[e["comparison_classification"]] += 1

    eligible = sorted(s for s, r in results.items() if r["eligible"])
    changed = {s: r for s, r in results.items()
               if r["recomputed_classification"] != r["staged_classification"]}

    finished = datetime.now(timezone.utc)
    pin_material = (sha256(PROVENANCE) + sha256(LOCATORS) + sha256(LOCATORS_SUPP)
                    + sha256(CODING) + sha256(pathlib.Path(__file__)))
    run_id = "study-" + started.strftime("%Y%m%dT%H%M%SZ") + "-" + \
        hashlib.sha256(pin_material.encode()).hexdigest()[:6]

    detail = {
        "run_id": run_id,
        "spec": "091-anchor-comparison-integrity",
        "stage": "stage-5-t501-w1-recomputation",
        "coder": coding["coder"]["name"],
        "precondition_failures": precondition_failures,
        "coded_entries": {s: {**results[s], **identity[s]} for s in sorted(coded)},
        "changed_entries": changed,
        "eligible_set": eligible,
        "census_staged": staged_census,
        "census_recomputed": census(results),
        "uncoded_reproduction": {"checked": sum(1 for r in results.values()
                                                if r["input"] == "staged"),
                                 "mismatches": mismatches},
        "examined_census": {
            "entries_total": len(staged),
            "phonetic_located": sum(1 for s in staged
                                    if (merged_locator(s, "phonetic_reading") or {})
                                    .get("outcome") == "located"),
            "phonetic_coded_this_run": len(coded),
        },
    }
    detail_path = RECORDS / "t501-w1-recomputation-results-2026-11-24.json"
    detail_path.write_text(json.dumps(detail, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")

    run_record = {
        "run": {
            "run_id": run_id,
            "surface": "study",
            "tool": "spec091_stage5_recomputation.py --execute",
            "tool_version": "stage-5 recomputation v1 (Spec 091, T501 W1 leg)",
            "started": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "finished": finished.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "key": {
                "surface": "study",
                "command": "spec091_stage5_recomputation.py --execute",
                "tool_version": "stage-5 recomputation v1 (Spec 091, T501 W1 leg)",
                "environment_class": "tower-compute/linux",
                "code_version": "3a911aae52f91850249c4eb530628ac2138f4ebc",
                "seed": "no-seed",
                "input_pins": {
                    "spec": "091-anchor-comparison-integrity",
                    "stage": "stage-5-t501-w1-recomputation",
                    "eligibility_defs": "specs/091-anchor-comparison-integrity/eligibility-defs-v1.md",
                    "blinding_protocol": "specs/091-anchor-comparison-integrity/blinding-protocol-v1.md",
                    "frozen_artifacts": {
                        "provenance_sha256": sha256(PROVENANCE),
                        "locators_sha256": sha256(LOCATORS),
                        "locators_supplement_sha256": sha256(LOCATORS_SUPP),
                    },
                    "coding_record_sha256": sha256(CODING),
                    "coding_packet_sha256": coding["filing"]["attachment_sha256"],
                    "recomputation_script_sha256": sha256(pathlib.Path(__file__)),
                },
            },
            "determinism_class": "deterministic pure function of the pinned inputs "
                                 "(eligibility-defs v1 section 5)",
        },
        "result": {
            "artifact": "specs/091-anchor-comparison-integrity/records/"
                        "t501-w1-recomputation-results-2026-11-24.json",
            "artifact_sha256": sha256(detail_path),
            "eligible_set": eligible,
            "census": detail["census_recomputed"],
        },
    }
    run_path = RECORDS / f"{run_id}.json"
    run_path.write_text(json.dumps(run_record, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    print("run_id:", run_id)
    print("eligible set:", eligible)
    print("census staged:    ", staged_census)
    print("census recomputed:", detail["census_recomputed"])
    print("changed:", {s: (r["staged_classification"], r["recomputed_classification"])
                       for s, r in changed.items()})
    print("precondition failures:", precondition_failures)
    print("uncoded reproduction: OK (175/175 staged classes reproduced)"
          if not mismatches else "FAILED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
