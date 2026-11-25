# Spec 104 — Plan

## Inputs

- The owner's decipherment gap analysis (program
  document, 2026-11-25): the survey of what each
  Glossa-Lab program is missing, which identifies the
  Eteocypriot bilingual alignment as the one well-posed
  quantum-testable subproblem in the program — a
  discrete optimization with a crisp score, certifiable
  against an exact optimum — and the owner's order of
  2026-11-25 in the Glossa-Lab chat ("do the quantum
  alignment benchmark after the program doc"), which is
  this study's commission (spec.md, D-104-5).
- Spec 096's frozen pilot materials: the corpus
  (`specs/096-eteocypriot-program/corpus/corpus.json`,
  freeze pin SHA-256
  `5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`),
  the E1 driver
  (`records/eteocypriot-e1-driver.py`: the R1–R3
  derivation D and the LCCS scoring, read in full at
  registration), and the filed E1 run record
  (`records/eteocypriot-e1-run-2026-11-20.json`: the
  score matrix, the A2 rule's joint infeasibility on
  segment 6, and the development-only loading
  discipline this study inherits).
- The IBM Quantum connector doc
  (`~/workspace/custom-connectors/custom.ibm-quantum/CONNECTOR.md`):
  the registered route, its instance CRN, and its
  documented authentication reality (verified
  2026-10-27), re-verified by the registration-day
  probe of 2026-11-25 (HTTP 401, error code 1219, on
  the backends and account reads) — the basis of
  spec.md §4's route disclosure and D-104-2.
- Spec 103's package — the registration mechanics this
  landing follows: bundle intake, taxonomy entry,
  settling chain refresh in the standing order,
  generated layers, census pins.

## Adoption mechanics

1. This package (spec, claims, plan, tasks, test
   cases, the registration record) lands by PR on a
   fresh clone on tower-compute, under
   `~/.syncyard/worktrees/glossa/` (the home-root
   `~/glossa-work` was cleared by the owner's
   2026-11-23 cleanup order; clones never return to
   the home root).
2. Registration, in the standing order (Spec 098's
   D-098-2 pattern, as executed for Specs 099–103):
   the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy
   gains the study entry (spec.md, D-104-3); the
   settling chain runs in order — verify-canonicals
   over the grown build before the pin moves, the
   T405 scenario pair re-executed with byte-equal
   result blocks, the comparison re-filed, the
   assignment sets re-materialized, the canonical pin
   refreshed with its `re_derivations` entry, the
   superseded generation's departure accounted; the
   generated layers regenerate in dependency order
   (matrix, map data, program map); every census pin
   in the conformance and dashboard tests is updated
   from the regenerated actuals and the affected tests
   run before the PR opens.
3. The AEE assessment of the bundle is run and filed
   under `records/` (the draft-stage reading is
   expected; an inability to run it is recorded,
   never papered over).
4. No recommendations-ledger row is added (spec.md,
   D-104-4).

## Stage plan

- **Stage 0 — registration (this landing).** The
  instance, the formulation and its lemma, the arms
  and their parameters, the scaling generation, and
  the verdict vocabulary are frozen on the record;
  the claims are intaken; no solver runs.
- **Stage 1 — execution (second landing, under the
  same owner commission).** In order: (i) the
  instance is built from the pinned corpus and
  TC-104-02 passes before any solving; (ii) the
  EXACT arm certifies the real instance (exhaustive
  + ILP, TC-104-03) and every synthetic size (ILP,
  TC-104-04); (iii) the SA arm runs on every instance
  under the registered parameters, with TC-104-05's
  determinism check on the real instance; (iv) the
  quantum route is re-probed once and the response
  filed (TC-104-06) — if it authenticates, the QAOA
  arm runs as registered in spec.md §4; if it
  refuses, the arm closes as NOT EXECUTED — ROUTE
  DEAD on the filed evidence; (v) the outcome record
  is filed in `records/` returning V-104-A and
  V-104-B exactly as registered, with the raw solver
  outputs saved to a dated file in the same landing,
  and TC-104-07's standing audit read over the
  landing's diff. **Stop rule:** if a step cannot be
  performed as registered — the corpus pin fails,
  the recomputed matrix differs from the filed run
  record, the two exact methods disagree — execution
  stops at that step, the failure is filed as the
  outcome record, and no substitute procedure is
  improvised. The quantum route's refusal is not a
  stop-rule event: it is a registered outcome (§4).

## Verification

- Every stage's checks run on tower-compute in the
  stage's own fresh clone under
  `~/.syncyard/worktrees/glossa/`; each run's raw
  output is filed or hashed in the stage record, and
  the verdict reported is the run's own payload
  verdict.
- PRs merge only on genuine per-job CI green across
  all ten jobs; a zero-step or cancelled run is NO
  VERDICT, never green.
- Registration's own verification is the ledger gate
  and the program-map conformance checks on the
  landed tree, plus the affected backend suites run
  on tower-compute before the PR opens.
