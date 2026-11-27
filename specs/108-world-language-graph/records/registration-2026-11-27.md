# Spec 108 — Registration Record (2026-11-27)

**Status: REGISTERED 2026-11-27.** This record files the
registration cascade's executed figures for the Spec 108
landing (branch `spec-108-world-language-graph-registration`).
The study builds and populates the World Language Graph
under the design of 2026-11-26, commissioned by the
owner's act of 2026-11-27 03:08 ET in the Glossa-Lab chat
("Commission the graph build and population as designed",
adopting all eight commissioning decisions of the design
as written). Registration moves no standing, verdict, or
tally in any program (spec.md §6); the graph amends no
Spec 106 baseline, template, or pin.

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
  (7 appended, 0 already canonical). Ledger 1,097 → 1,104
  lines; claims 1,066 → 1,073; canonical SHA-256
  `51f4fbbd1a96a4cd9c332bc7fa8fc65e568b6c519c008ab3d14ed3bd838ad21a`
  → `e8b4f72caa7a2f2ece7b3c7e0f9b64f3c7fe548ce09220ac8a13da881bfd2ded`.
  verify-canonicals over the grown build, before any pin
  moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed over
  the grown build (runs `settling-20261127T082425Z-2084b0`
  incumbent, `settling-20261127T082426Z-faea4d`
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
  `settling-20261127T082441Z-2c4fe3`; incumbent 94,
  full-register 286, H003 out of frame). The canonical
  pin refreshed as re_derivations[24] of
  settling-canonical.json. The superseded generation
  (settling-20261127T040722Z-0bb432,
  settling-20261127T040722Z-04390a,
  settling-20261127T040744Z-a7a115) departed the run store
  in this landing; their departure acts are appended to
  the run index in the landing's completion commit,
  naming the registration commit as `superseded_by_commit`
  and each record's blob hash from the pre-landing tree.
  Two absence records written during this cascade by a
  malformed-scope invocation
  (settling-20261127T082417Z-9b84c2,
  settling-20261127T082417Z-e77294 — the scope was passed
  without its frame qualification and the engine refused,
  as designed) stand in the store as the refusal records
  they are; the corrected executions are the pair named
  above. (During the landing the two files were briefly
  removed in error with the departing generation; both
  were restored byte-exact before the landing completed —
  SHA-256 26e49be0… and 48bb08e8…, verified against the
  hashes taken before the removal — and no departure act
  is filed for them: they never entered standing.)
- Generated layers, regenerated in dependency order:
  matrix 1,596 cells (supports 1,589, opposes 7) over
  1,073 rows; map-data 1,717 elements, 1,596 edges,
  settling runs carried 2; program map: 1,073 claims,
  109 studies. Falsifier census 1,064 of 1,073 claims,
  the same 9 gaps.
- Census pins updated from the regenerated actuals in
  test_program_map_conformance.py (including the Program
  infrastructure domain census 28 → 29),
  test_spec086_ledger_gate.py, test_spec086_map.py,
  test_spec095_stage4_instantiation.py,
  test_spec095_t403_dashboard.py (including the T405 run
  of record, re-pinned to settling-20261127T082425Z-2084b0,
  whose quantities are the superseded generation's,
  byte-equal), and the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts): claims
  1,066 → 1,073; bundle population 1,043 → 1,050; open
  class 1,057 → 1,064; falsifier-present 1,057 → 1,064;
  ledger lines 1,097 → 1,104; studies 108 → 109; matrix
  cells and map edges 1,589 → 1,596; map elements
  1,710 → 1,717; supports edges 1,582 → 1,589; claims
  untouched by any run 1,065 → 1,072; draft status
  1,042 → 1,049.
- Recommendations ledger: no row added (D-108-3 — the
  commission is the owner's own act in the Glossa-Lab
  chat, not a Co-scientist recommendation; the ledger
  stays at 139 rows).
