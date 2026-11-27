# Spec 107 — Registration Record (2026-11-26)

**Status: REGISTERED 2026-11-26.** This record files the
registration cascade's executed figures for the Spec 107
landing (branch `spec-107-active-decipherment-loop`).
The study registers the active decipherment loop of the
design document *Active Decipherment Design — Glossa-Lab
(2026-11-26)* and its first cycle (I-1, M-1, E-1), under
the owner's act of 2026-11-26 22:48 ET in the Glossa-Lab
chat ("Adopt the loop and commission cycle 1 as
proposed"). Registration moves no standing, verdict, or
tally in any program (spec.md §7).

## 1. The package

spec.md (the loop at §2; the limits and kill criteria at
§4; cycle 1 at §3), claims.md and aee-claims.json (six
claims, C107-1..C107-6, each with its falsifier and its
does-not-establish line), plan.md, tasks.md, test-cases.md
(TC-107-01..TC-107-06), records/
(cycle-1-registration-2026-11-26.md — the ranking record
with sensitivity statements, the null-yield minimum, and
the full I-1 and M-1 registrations, E-1 by reference to
Spec 101; history-ledger.md, opened live; the AEE
assessment; this record).

**Number (D-107-1).** At the check of 2026-11-26 the
highest landed spec package on origin/main was 106; no
107 directory, branch, or open pull request carried 107.
This package takes 107.

**Test cases at registration.** TC-107-01 PASS (claim
ids and order equal in claims.md and aee-claims.json;
every claim carries a falsifier and a does-not-establish
line; spec.md §2 states the five loop steps and §4 the
five kill criteria). TC-107-02..TC-107-06 execute with
cycle 1 in Stage 1.

## 2. The AEE outcome at registration

`records/aee-assessment-2026-11-26.json` — run_aee.py
assess --phase after_plan (aee 1.5.3) over the bundle's
aee-claims.json: outcome **iterate**; 6 claims assessed,
all 6 draft-capped below the 0.70 confidence threshold —
the expected shape for draft claims at registration, the
same shape Specs 101–106 returned. The assessment's own
ledger entries were written by the tool under
`.specify/extensions/aee/` and are carried in this
landing. (Venue note: the tower's relocated `glossa-ci`
venv's console scripts carry stale shebangs from the
2026-11-23 home cleanup, so the assessment ran through a
PATH shim invoking the venv's interpreter directly, as
for Specs 104–106.)

## 3. Registration cascade (executed figures)

- Taxonomy: Spec 107 added to the program-map taxonomy
  under Program infrastructure / Governance, lifecycle &
  generated layers (decision D-107-2); studies 107 → 108;
  the Program infrastructure domain census 27 → 28.
- Intake: the bundle's 6 claims appended through
  tools/ledger/import_bundle.py, dated 2026-11-26
  (6 appended, 0 already canonical). Ledger 1,091 → 1,097
  lines; claims 1,060 → 1,066; canonical SHA-256
  `a7235a6147112cb32d49a3c3a0ddf00b08343ff0a64321d894667ca983f3bf6b`
  → `51f4fbbd1a96a4cd9c332bc7fa8fc65e568b6c519c008ab3d14ed3bd838ad21a`.
  verify-canonicals over the grown build, before any pin
  moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed over
  the grown build (runs `settling-20261127T040722Z-0bb432`
  incumbent, `settling-20261127T040722Z-04390a`
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
  `settling-20261127T040744Z-a7a115`; incumbent 94,
  full-register 286, H003 out of frame). The canonical
  pin refreshed as re_derivations[23] of
  settling-canonical.json. The superseded generation
  (settling-20261125T181419Z-e4d210,
  settling-20261125T181420Z-28b091,
  settling-20261125T181438Z-0b66a6) departed the run store
  in this landing; their departure acts are appended to
  the run index in the landing's completion commit,
  naming the registration commit as `superseded_by_commit`
  and each record's blob hash from the pre-landing tree
  (e4d210: 874c3c2bc72b5ba296c38635c8df7540fd174e9c;
  28b091: 606deddc6e89d653346f21aae25856df3a1eb348;
  0b66a6: 6157a67dac2c36afa424ced760a4480e332de9f5).
- Generated layers, regenerated in dependency order:
  matrix 1,589 cells (supports 1,582, opposes 7) over
  1,066 rows; map-data 1,710 elements, 1,589 edges,
  settling runs carried 2; program map: 1,066 claims,
  108 studies. Falsifier census 1,057 of 1,066 claims,
  the same 9 gaps.
- Census pins updated from the regenerated actuals in
  test_program_map_conformance.py (including the Program
  infrastructure domain census 27 → 28),
  test_spec086_ledger_gate.py, test_spec086_map.py,
  test_spec095_stage4_instantiation.py,
  test_spec095_t403_dashboard.py (including the T405 run
  of record, re-pinned to settling-20261127T040722Z-0bb432,
  whose quantities are the superseded generation's,
  byte-equal), and the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts): claims
  1,060 → 1,066; bundle population 1,037 → 1,043; open
  class 1,051 → 1,057; falsifier-present 1,051 → 1,057;
  ledger lines 1,091 → 1,097; studies 107 → 108; matrix
  cells and map edges 1,583 → 1,589; map elements
  1,704 → 1,710; supports edges 1,576 → 1,582; claims
  untouched by any run 1,059 → 1,065; draft status
  1,036 → 1,042.
- Recommendations ledger: no row added (D-107-3 — the
  study's provenance is the owner's direct adoption act,
  not a Co-scientist recommendation).

## 4. Standing

Spec 107 is REGISTERED. Cycle 1 (Stage 1) is commissioned
by the same owner act and executes under the
registrations filed at
records/cycle-1-registration-2026-11-26.md (I-1, M-1)
and in Spec 101's package (E-1); its outcomes land as
their own records. No standing, verdict, or tally moved
at registration (C107-5; TC-107-05 will audit the Stage 1
landing diffs the same way).

**Venue.** All work for this package ran on tower-compute
in the fresh clone `~/.syncyard/worktrees/glossa/spec107-reg`
(branch `spec-107-active-decipherment-loop`). Nothing ran
in the coordination VM except the package's drafting and
source reading, which compute nothing against program
data.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

## Completion pass (2026-11-26, same landing)

- **Departure acts appended.** The three superseded settling
  records named in §3 departed the run store in this landing;
  their departure acts were appended to the run index through
  `run_records.append_act` in this completion commit, naming
  the registration commit
  `bbde46b15daca4f7d49a9a729e53332b5b5b6c8d` as
  `superseded_by_commit`. Each act carries both hashes of the
  departed record: the SHA-256 of its bytes (e4d210:
  0a04e2fe8b1ea11f81c8f88d37f922f29427261b3a80234b3f92d05b087b8091;
  28b091: 688c79c5904d3922a520f0e8c55861404405086781f0471dac2440e515ce3735;
  0b66a6: 4d2d5ba2509c35c93e146865be506064054b12a77192e24f736a66be75d56019)
  and its git blob id from the pre-landing tree (e4d210:
  874c3c2bc72b5ba296c38635c8df7540fd174e9c; 28b091:
  606deddc6e89d653346f21aae25856df3a1eb348; 0b66a6:
  6157a67dac2c36afa424ced760a4480e332de9f5) — §3's
  parenthetical named the git blob ids; both kinds stand
  here so the record is exact. The run-index completion
  pass (build_legacy_index.py) appended 1 act and named the
  departed records post-spec skips (folded census 97
  entries).
