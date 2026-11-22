# Spec 101 — registration record (2026-11-22)

Commission: OD-10 (owner, 2026-11-22), part 3 — a specification of a
realistic next Eteocypriot claim, registered but not executed. This
record states what was registered and the registration cascade's
executed figures. No execution stage of Spec 101 is commissioned by
this record; every stage in the plan is gated on a fresh owner
commission.

## What was registered

`specs/101-eteocypriot-next-claim/` — spec.md, claims.md,
aee-claims.json, plan.md, tasks.md, test-cases.md (TC-101-01..05),
this record, and the AEE assessment below. The claim: a postdictive
occurrence test — recurring-ending candidates registered from the
ICS 196 development set alone, then counted in ICS 194/195 under
Perna 2019's re-edition. Claims C101-1..C101-4 (occurrence at
registered positions/floor; exposure honesty; no scoring on unstated
tables; Perna-side state carries its own identity and the Spec 096
corpus is untouched). The blind form of the test was deliberately
not registered (decision D-101-4 in spec.md): its precondition is
false on the record, because Perna's chapter, including its printed
reading, was read in full on 2026-11-22 under OD-9 before any
candidate existed. Exposure is stated in the spec as the governing
limit on what any outcome may be taken to mean.

## AEE assessment

`records/aee-assessment-2026-11-22.json` — run_aee.py assess
--phase after_plan (aee 1.5.3) over the bundle's aee-claims.json:
outcome **iterate**; 4 claims assessed, 16 failure modes, all 4
below the 0.70 confidence threshold, draft-capped at
gather_evidence/iterate — the expected shape for draft claims at
registration, the same shape Spec 096's adoption assessment
returned. The assessment's own ledger entries were written by the
tool under `.specify/extensions/aee/` and are carried in the same
landing.

## Registration cascade (executed figures)

- Taxonomy: Spec 101 added to the program map taxonomy under
  Program infrastructure / Governance, lifecycle & generated layers
  (decision D-101-3); studies 101 → 102.
- Intake: the bundle's 4 claims appended to the ledger (0 already
  canonical). Ledger 1,063 → 1,067 lines; claims 1,032 → 1,036;
  canonical SHA-256 `94174d7c…` → `a047eb146baece9a1d007663339e29d929bc8ebd39d2fb4a2155fb0fb44a640d`.
  verify-canonicals over the regenerated build: 6/6 PASS.
- Settling layer: the T405 pair re-executed over the grown build;
  result blocks byte-equal to the superseded generation (runs
  `settling-20261122T173321Z-57cfda` incumbent,
  `settling-20261122T173321Z-05bab2` full-register). The Stage 4
  dual-run comparison re-filed (its diff against the previous
  filing is the ledger pin only). Assignment sets re-materialized
  unchanged (incumbent 94, full-register 286, H003 out of frame).
  The canonical pin refreshed as re_derivations[17] of
  settling-canonical.json. The superseded generation's run records
  (settling-20261122T165435Z-5611f9, -c7bc9d,
  settling-20261122T165448Z-548d35) departed the run store in this
  landing; their departure acts are appended to the legacy run
  index by the completion pass in the same pull request.
- Generated layers: matrix regenerated (1,559 cells over 1,036
  rows); program map regenerated (1,680 elements, 1,559 edges;
  falsifier census 1,027 of 1,036 claims, the same 9 gaps).
- Census pins updated from the regenerated actuals in
  test_spec095_stage4_instantiation.py, test_spec086_ledger_gate.py,
  test_spec095_t403_dashboard.py (including the T405 run of record),
  test_spec086_map.py, and test_program_map_conformance.py (claims
  1,036; bundle 1,013; open/falsifier-present 1,027; ledger lines
  1,067; studies 102; matrix cells and map edges 1,559; map
  elements 1,680; claims untouched by any run 1,035).

## Standing

Spec 101 is REGISTERED. Nothing in it is executed. Its execution
stages (Perna-side intake, candidate registration, freeze addendum,
scoring) each require a fresh owner commission, and precondition
P-1 requires the Spec 096 corpus to hash to
`2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597`
before and after any Perna-side work.

## Completion pass (2026-11-22, same landing)

The registration cascade above was executed by the first
OD-10 worker, whose session ended before the landing
completed; this completion pass (the OD-10 redo) verified
its figures against the tree, finished the cascade, and
landed it. Three completions are recorded so the record
above reads true end to end:

1. **Program-map artifacts regenerated.** The cascade's
   matrix and map-data regeneration verified exactly
   (ledger gate legs V1–V5 pass on the tree as salvaged),
   but the V10 program-map artifacts
   (`program-map.json`, `program-map-finds.json`,
   `program-map.html`) still carried the pre-101 ledger
   stamp. They were regenerated with
   `tools/map/generate_program_map.py` from the current
   ledger and taxonomy (claims 1,036, studies 102), and
   the gate's V10 legs pass on the result.
2. **Census pins completed from the regenerated
   actuals.** The pin updates listed in §2 covered the
   headline censuses; the completion pass updated the
   remaining pins the new census reaches, each from the
   regenerated artifact it pins: draft-status claims
   1,008 → 1,012 and supports edges/cells 1,548 → 1,552
   and the AEE state census total 1,032 → 1,036
   (`test_spec086_map.py`); matrix rows 1,032 → 1,036
   (`test_spec095_stage4_instantiation.py`); dashboard
   studies 101 → 102 (`test_spec095_t403_dashboard.py`);
   the taxonomy domain census, Program infrastructure
   24 → 25 (`test_program_map_conformance.py`); and the
   gate's own evidence pins, map edge census supports
   1,548 → 1,552 and program-map study nodes 101 → 102
   (`test_spec086_ledger_gate.py`); and the two frontend e2e census texts, 1,032 -> 1,036 claims (`frontend/e2e/system-graph.spec.ts`, `frontend/e2e/researcher-dashboard.spec.ts`), caught by the landing pull request's first CI run and fixed in the same landing.
3. **Departure acts appended.** The three superseded
   settling records named in §2 departed the run store
   in this landing; their departure acts were appended
   to the legacy run index through
   `run_records.append_act` in the landing's completion
   commit, naming the registration commit as
   `superseded_by_commit` and each record's blob hash
   from the pre-landing tree, as §2 anticipated.
