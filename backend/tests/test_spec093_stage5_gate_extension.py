"""Spec 093 Stage 5 — the V12 culture-layer gate class
(T502) and the taxonomy amendment it verifies (T501).

The battery exercises `_v12_checks` over synthetic mini
trees, one seeded violation per leg, each required to
turn its leg red and name the violation — the T502 test
acceptance (a seeded violation fails) at unit scale —
plus the clean-layer pass, the absent-layer NOT-RUN
posture (the V10/V11 posture toward a layer that has
not landed), and a real-tree run: the committed tree at
the extended profile passes V12 in full scope (the
second half of T502's acceptance), with the layer
holding exactly the family's fourteen claims.
"""

from __future__ import annotations

import json
from pathlib import Path

from glossa_lab import ledger_gate as lg

ROOT = Path(__file__).resolve().parents[2]
STUDY = "093-material-context-channel"
DOMAIN = "Material context"

FAMILY = [
    {"id": f"{STUDY}/C093-{i}", "kind": "claim"} for i in (1, 2, 3)
]
OTHER = [{"id": "001-glossa-lab-baseline/C001-1", "kind": "claim"}]


def _claim_node(cid: str, domain: str = DOMAIN) -> dict:
    return {"id": cid, "domain": domain}


def _clean_claim_nodes() -> list[dict]:
    return [_claim_node(e["id"]) for e in FAMILY] + [
        _claim_node(OTHER[0]["id"], "Program infrastructure")
    ]


def _clean_study_nodes() -> list[dict]:
    return [
        {"id": STUDY, "domain": DOMAIN},
        {"id": "001-glossa-lab-baseline",
         "domain": "Program infrastructure"},
    ]


def _tree(
    tmp_path: Path,
    *,
    domains: list[str] | None = None,
    claim_nodes: list[dict] | None = None,
    study_nodes: list[dict] | None = None,
    register: str | None = None,
) -> Path:
    map_dir = tmp_path / "glossa-indus" / "map"
    map_dir.mkdir(parents=True)
    (map_dir / "program-map-taxonomy.json").write_text(
        json.dumps(
            {
                "version": lg.PROGRAM_MAP_TAXONOMY_VERSION,
                "domains": (
                    domains
                    if domains is not None
                    else [DOMAIN, "Program infrastructure"]
                ),
                "subdomains": {},
                "studies": [],
            }
        ),
        encoding="utf-8",
    )
    (map_dir / "program-map.json").write_text(
        json.dumps(
            {
                "nodes": {
                    "claims": (
                        claim_nodes
                        if claim_nodes is not None
                        else _clean_claim_nodes()
                    ),
                    "studies": (
                        study_nodes
                        if study_nodes is not None
                        else _clean_study_nodes()
                    ),
                }
            }
        ),
        encoding="utf-8",
    )
    (map_dir / "gap-register.md").write_text(
        register
        if register is not None
        else "# Gap register\n\n## Existing entries\n\n"
        "GR-088-01. A gap (Sign inventory & corpus). UNSTATED.\n",
        encoding="utf-8",
    )
    return tmp_path


def _legs(checks: list[lg.Check]) -> dict[str, lg.Check]:
    return {c.name: c for c in checks}


CITATION = "V12 culture layer — citation existence"
FLOW = "V12 culture layer — one-way flow (layer = ledger family)"
COUNTING = "V12 culture layer — gap-register section counting"


def test_v12_not_run_where_the_layer_has_not_landed(tmp_path):
    root = _tree(
        tmp_path,
        domains=["Program infrastructure"],
        claim_nodes=[_claim_node(OTHER[0]["id"],
                                 "Program infrastructure")],
        study_nodes=[{"id": "001-glossa-lab-baseline",
                      "domain": "Program infrastructure"}],
    )
    checks = lg._v12_checks(root, FAMILY + OTHER)
    assert len(checks) == 1
    assert checks[0].name == "V12 culture layer"
    assert checks[0].status == "NOT-RUN"


def test_v12_clean_layer_passes_all_legs(tmp_path):
    root = _tree(tmp_path)
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert set(legs) == {CITATION, FLOW, COUNTING}
    assert all(c.status == "PASS" for c in legs.values()), legs
    # No culture-side section yet: the counting leg passes
    # with the zero count on its face (Stage 6 lands the
    # section under this support).
    assert "0 GR-093 entries counted" in legs[COUNTING].evidence[0]


def test_v12_bad_citation_fails(tmp_path):
    nodes = _clean_claim_nodes() + [
        _claim_node(f"{STUDY}/C093-99")
    ]
    root = _tree(tmp_path, claim_nodes=nodes)
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[CITATION].status == "FAIL"
    assert any("C093-99" in e for e in legs[CITATION].evidence)


def test_v12_missing_family_claim_fails_the_flow_leg(tmp_path):
    nodes = [n for n in _clean_claim_nodes()
             if n["id"] != f"{STUDY}/C093-2"]
    root = _tree(tmp_path, claim_nodes=nodes)
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[FLOW].status == "FAIL"
    assert any("C093-2" in e for e in legs[FLOW].evidence)
    assert legs[CITATION].status == "PASS"


def test_v12_family_claim_grouped_elsewhere_fails(tmp_path):
    nodes = _clean_claim_nodes()
    for n in nodes:
        if n["id"] == f"{STUDY}/C093-1":
            n["domain"] = "Claim families by study line"
    root = _tree(tmp_path, claim_nodes=nodes)
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[FLOW].status == "FAIL"
    assert any("C093-1" in e for e in legs[FLOW].evidence)


def test_v12_missing_study_node_fails_citation(tmp_path):
    root = _tree(
        tmp_path,
        study_nodes=[{"id": "001-glossa-lab-baseline",
                      "domain": "Program infrastructure"}],
    )
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[CITATION].status == "FAIL"


_COMPLETE_ENTRY = """GR-093-01. A MISSING THING (Material context). DATA-BLOCKED.

Kind: missing node. Source: Spec 093 Stage 6 (T601).

**Missing piece:** the thing that is not known.

**Candidate (acceptance test):** the administration whose
outcome would discharge this entry.

**Falsifier:** the observation that would show the piece
is not missing.

**Type:** in-house re-derivation.

**Owner gates:** none.
"""


def _register_with_section(body: str) -> str:
    return (
        "# Gap register\n\n## Existing entries\n\n"
        "GR-088-01. A gap (Sign inventory & corpus). UNSTATED.\n\n"
        "## Culture-side entries — Spec 093 (GR-093)\n\n"
        + body
    )


def test_v12_register_section_is_counted(tmp_path):
    root = _tree(
        tmp_path, register=_register_with_section(_COMPLETE_ENTRY)
    )
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[COUNTING].status == "PASS", legs[COUNTING]
    assert "1 GR-093 entries counted" in legs[COUNTING].evidence[0]


def test_v12_register_entry_missing_an_element_fails(tmp_path):
    broken = _COMPLETE_ENTRY.replace("**Falsifier:**", "Falsifier:")
    root = _tree(
        tmp_path, register=_register_with_section(broken)
    )
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[COUNTING].status == "FAIL"
    assert any(
        "GR-093-01" in e and "Falsifier" in e
        for e in legs[COUNTING].evidence
    )


def test_v12_wrapped_cross_reference_is_not_an_entry(tmp_path):
    # Regression (Stage 6): a wrapped line inside an
    # entry's own text that begins with a cross-reference
    # ("GR-093-05." at a line wrap) is not an entry
    # heading; entry headings count only at paragraph
    # starts. The landed GR-093 section itself exposed
    # the case.
    entry = _COMPLETE_ENTRY.replace(
        "**Candidate (acceptance test):** the administration whose\n"
        "outcome would discharge this entry.",
        "**Why its absence blocks convergence:** the bound in\n"
        "GR-093-05.\n"
        "stands behind this one.\n\n"
        "**Candidate (acceptance test):** the administration whose\n"
        "outcome would discharge this entry.",
    )
    root = _tree(tmp_path, register=_register_with_section(entry))
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[COUNTING].status == "PASS", legs[COUNTING]
    assert "1 GR-093 entries counted" in legs[COUNTING].evidence[0]


def test_v12_empty_culture_section_fails(tmp_path):
    root = _tree(tmp_path, register=_register_with_section(""))
    legs = _legs(lg._v12_checks(root, FAMILY + OTHER))
    assert legs[COUNTING].status == "FAIL"


def test_v12_real_tree_passes_at_the_extended_profile():
    report = lg.run_gate(ROOT, scope={"V12"})
    assert report.ok, report.render()
    legs = _legs([c for c in report.checks
                  if c.name.startswith("V12")])
    assert set(legs) == {CITATION, FLOW, COUNTING}
    assert all(c.status == "PASS" for c in legs.values())
    assert "14 claim nodes" in legs[CITATION].evidence[0]
    assert "exactly the ledger's 14 claims" in legs[FLOW].evidence[0]
