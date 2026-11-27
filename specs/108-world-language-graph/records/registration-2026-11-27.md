# Spec 108 — Registration Record (2026-11-27)

**Status: REGISTERED 2026-11-27.** This record files the
registration cascade's executed figures for the Spec 108
landing (branch `spec-108-wlg-registration-c`). The study
builds and populates the World Language Graph under the
design of 2026-11-26, commissioned by the owner's act of
2026-11-27 03:08 ET in the Glossa-Lab chat ("Commission
the graph build and population as designed", adopting all
eight commissioning decisions of the design as written).
Registration moves no standing, verdict, or tally in any
program (spec.md §6); the graph amends no Spec 106
baseline, template, or pin.

**Landing history, stated plainly.** The registration was
first executed over main at `effb87e9` and landed as
PR #773; while its CI ran, parallel program landings
advanced main (sixteen commits, including a full
registration cascade of their own and the C101-1
adjudication), and the branch's merge became conflicted
in every generated layer — after which GitHub created no
further CI runs for it, nor for its successor PR #778
carrying the identical commits. Both PRs stand closed
unmerged. This landing re-executes the registration over
the advanced main, as the record below states; nothing
from the first execution is carried except the package
itself and the build, whose content does not touch the
ledger layers.

## 1. The package

spec.md (the build at §§2–3; population at §4; the
no-standing-moves clause at §6), claims.md and
aee-claims.json (seven claims, C108-1..C108-7, each with
its falsifier and its does-not-establish line), plan.md,
tasks.md, test-cases.md (TC-108-01..TC-108-09,
implementing audits WLG-01..09), records/
(design-2026-11-26.md — the governing design, copied in
full; history-ledger.md, opened live;
aee-assessment-2026-11-27.json; this record). The build
and population (tools, data, graph streams, batch and
release records) land as the build landing under the
same spec.

**Number (D-108-1).** At the check of 2026-11-27 the
highest landed spec package on origin/main was 107; no
108 directory, branch, or open pull request carried 108.
This package takes 108.

**Test cases at registration.** TC-108-01 PASS (claim
ids and order equal in claims.md and aee-claims.json;
every claim carries a falsifier and a does-not-establish
line; spec.md states both status scales, all seven
predicates, the audit range, NO_GEOMETRY, and
CLOSED_INDETERMINATE — verified mechanically at
registration). TC-108-02..TC-108-09 execute with the
build in Stages 1–3 (the audit suite over the populated
release).

## 2. The AEE outcome at registration

`records/aee-assessment-2026-11-27.json` — run_aee.py
assess --phase after_plan (aee 1.5.3) over the bundle's
aee-claims.json: outcome **iterate**; 7 claims assessed,
all 7 draft-capped below the 0.70 confidence threshold —
the expected shape for draft claims at registration, the
same shape Specs 101–107 returned. The assessment's own
ledger entries were written by the tool under
`.specify/extensions/aee/` and are carried in this
landing. (Venue note: the tower's relocated `glossa-ci`
venv's console scripts carry stale shebangs from the
2026-11-23 home cleanup, so the assessment ran through
a PATH shim invoking the venv's interpreter directly, as
for Specs 104–107.)

## 3. Registration cascade (executed figures)

- Taxonomy: Spec 108 added to the program-map taxonomy
  under Program infrastructure / Governance, lifecycle &
  generated layers (decision D-108-2); studies 108 → 109;
  the Program infrastructure domain census 28 → 29.
- Intake: the bundle's 7 claims appended through
  tools/ledger/import_bundle.py, dated 2026-11-27
  (7 appended, 0 already canonical). Ledger 1,098 → 1,105
  lines; claims 1,066 → 1,073; canonical SHA-256
  `fd4d12e73b0df3ad2d9311772b506b1f0a9e10da4ec156f9456d24fb109d7abc`
  → `416a765de7eecb93c4cf1f83494f29334dffe8adc10080d416def10ee80d80af`.
  verify-canonicals over the grown build, before any pin
  moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed over
  the grown build (runs `settling-20261127T094519Z-ac7b1c`
  incumbent, `settling-20261127T094518Z-78f850`
  full-register, same 286-sign full-frame scope, same
  registered scenario ids); both result blocks byte-equal
  to the superseded generation's, verified by direct
  comparison of the stored records, and the pair's input
  pins identical to the superseded generation's except
  the ledger pin itself. The Stage 4 dual-run comparison
  re-filed from the new pair (its diff against the
  previous filing is the ledger pin only; its result
  block byte-equal, verified). Assignment sets
  re-materialized unchanged (run
  `settling-20261127T094608Z-6e4e6d`; incumbent 94,
  full-register 286, H003 out of frame). The canonical
  pin refreshed as re_derivations[25] of
  settling-canonical.json. The superseded generation
  (settling-20261127T081822Z-b6a378,
  settling-20261127T081822Z-c833b0,
  settling-20261127T081842Z-cbc5d7) departed the run store
  in this landing; their departure acts are appended to
  the run index in the landing's completion commit,
  naming the registration commit as `superseded_by_commit`
  and each record's blob hash from the pre-landing tree.
- Generated layers, regenerated in dependency order:
  matrix 1,596 cells (supports 1,589, opposes 7) over
  1,073 rows; map-data 1,717 elements, 1,596 edges,
  settling runs carried 2; program map: 1,073 claims,
  109 studies. Falsifier census 1,064 of 1,073 claims,
  the same 9 gaps.
- Census pins updated from the regenerated actuals in
  test_program_map_conformance.py (including the Program
  infrastructure domain census 28 → 29, and the open
  class at its post-adjudication figure),
  test_spec086_ledger_gate.py, test_spec086_map.py,
  test_spec095_stage4_instantiation.py,
  test_spec095_t403_dashboard.py (including the T405 run
  of record, re-pinned to settling-20261127T094519Z-ac7b1c,
  whose quantities are the superseded generation's,
  byte-equal), and the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts): claims
  1,066 → 1,073; bundle population 1,043 → 1,050;
  falsifier-present 1,057 → 1,064; ledger lines
  1,098 → 1,105; studies 108 → 109; matrix cells and map
  edges 1,589 → 1,596; map elements 1,710 → 1,717;
  supports edges 1,582 → 1,589; claims untouched by any
  run 1,065 → 1,072; draft status 1,042 → 1,049.
- Recommendations ledger: no row added (D-108-3 — the
  commission is the owner's own act in the Glossa-Lab
  chat, not a Co-scientist recommendation; the ledger
  stays at 139 rows).
