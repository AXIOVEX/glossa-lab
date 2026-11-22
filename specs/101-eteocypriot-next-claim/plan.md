# Spec 101 — Plan

## Inputs

- Adjudication unit E-8 and the owner's OD-10 act of
  2026-11-22 (`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`;
  `specs/096-eteocypriot-program/records/a2-baselines-controls-record-2026-11-22.md`
  is the same commission's analysis half).
- The OD-9 acquisition record
  (`specs/096-eteocypriot-program/records/od9-acquisition-2026-11-22.md`):
  Perna 2019 identified, pinned, and read in full on
  OpenEdition Books.
- The OD-8 audit and rerun record
  (`specs/096-eteocypriot-program/records/a2-audit-rerun-record-2026-11-22.md`),
  findings F-1 and F-4, and Spec 096's amendment 2 §4,
  which together fix precondition P-3.
- Spec 096's package — the form this package follows:
  spec, claims, freeze discipline, floor discipline,
  adjudication route.
- Spec 100's package — the registration mechanics this
  landing follows (D-100-2's pattern): bundle intake,
  taxonomy entry, settling chain refresh in the
  standing order, generated layers, census pins.

## Adoption mechanics

1. This package (spec, claims, plan, tasks, test cases,
   the registration record) lands by PR on a fresh clone
   on tower-compute.
2. Registration, in the standing order (Spec 098's
   D-098-2 pattern, as executed for Specs 099 and 100):
   the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy gains
   the study entry (spec.md, D-101-3); the settling
   chain runs in order — verify-canonicals over the
   grown build before the pin moves, the T405 scenario
   pair re-executed with byte-equal result blocks, the
   comparison re-filed, the assignment sets
   re-materialized, the canonical pin refreshed with
   its `re_derivations` entry, the superseded
   generation's departure accounted; the generated
   layers regenerate in dependency order (matrix, map
   data, program map); every census pin in the
   conformance and dashboard tests is updated from the
   regenerated actuals and the affected tests run
   before the PR opens.
3. The AEE assessment of the bundle is run and filed
   under `records/` (the draft-stage reading is
   expected; an inability to run it is recorded, never
   papered over).

## Stage plan

- **Stage 0 — registration (this landing).** The claim,
  its preconditions, success criteria, and independence
  assessment are frozen on the record; the claims are
  intaken; no stage of the study runs.
- **Stage 1 — intake (gated: fresh owner commission).**
  Precondition P-1: Perna 2019's reading of ICS 194/195
  intaken as a new corpus state with its C095-3
  identity record; the Spec 096 corpus hash checked
  before and after (TC-101-01).
- **Stage 2 — candidate registration (gated).**
  Preconditions P-2 and P-3: candidates derived from
  the ICS 196 development set alone under the stated
  mechanical rule; the candidate set, predicted
  positions, and floors committed before any scoring
  load of the Perna-side state (TC-101-02); the freeze
  addendum carrying every table in full (TC-101-05's
  floor arithmetic instantiated against the intaken
  census).
- **Stage 3 — scoring (gated).** The registered test of
  spec §3.2, run twice for byte-identical reproduction
  (TC-101-03), with an independent recount.
- **Stage 4 — outcome and adjudication package
  (gated).** The outcome record, carrying the exposure
  statement verbatim (TC-101-04) and each candidate's
  count against its floor; the adjudication package
  prepared for the owner's approval act if the outcome
  carries anything to adjudicate.

## Verification

- Every stage's checks run on tower-compute in the
  stage's own fresh clone; each run's raw output is
  filed or hashed in the stage record, and the verdict
  reported is the run's own payload verdict.
- PRs merge only on genuine per-job CI green across
  all ten jobs; a zero-step or cancelled run is NO
  VERDICT, never green.
- Registration's own verification is the ledger gate
  and the program-map conformance checks on the landed
  tree, plus the affected backend suites run before
  the PR opens.

## Risks and limits

- **Postdiction is the ceiling.** The exposure of
  §3.3 cannot be undone by any later discipline; the
  claim's strength is registered as postdictive and
  any stronger reading of a future outcome is a
  misreading this plan already names.
- **Single-text test.** ICS 194/195 is one inscription.
  A met floor shows recurrence in that text; it does
  not sample the language.
- **Edition risk.** The test runs over Perna's
  readings. Where Perna and Masson differ (48 signs),
  the outcome is an outcome over Perna's text; the
  identity record (P-1) is what makes that statement
  checkable rather than assumed.
