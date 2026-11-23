# Spec 103 — Plan

## Inputs

- The Co-scientist sweep adjudication of 2026-11-23
  (PR #725;
  `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-23.md`),
  unit D-M-3 and owner decision OD-D-2 (§4): the
  proposal, its adjudication as an owner decision,
  and the requirement that the registration carry the
  session's stated claim and kill check, the fixed
  split membership, and the no-pooling rule.
- The Meroitic session's Round D assessment
  (2026-11-23), §3 (D-M-3): the six forms' frozen
  counts (asoreyi in 2 held-out texts, xolkete in 1,
  pxolkete in 0, xolkte in 1 text with 2 occurrences,
  wisi in 0, against the 3-text threshold), the
  aggregate 95.6% accuracy caveat's limits, and the
  advance claim and kill check this spec registers.
- Spec 097's campaign freeze v2
  (`specs/097-meroitic-reproduction-benchmark/records/campaign-freeze-v2-2026-11-20.md`):
  the split rule and counts (§§1–2), the varietas
  discipline (§7), the seal's stated nature (§6).
- The Stage 4.4 outcome record and results
  (`stage-4-4-outcome-record-2026-11-20.md`,
  `stage-4-4-results.json`, same directory): the
  frozen counts and the prediction legs this check
  adjudicates against.
- The corpus completion record (same directory): the
  acquired build's pin, licences, and provenance (§2),
  and gap 5 (§4) — the printed edition is not
  machine-readable here — which fixes the witness
  scope (spec.md D-103-4).
- The frozen pipeline (`pipeline-v2.py`, campaign
  scratch, SHA-256
  `74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e`):
  the extraction of record — ingestion, dedup, split,
  `tokens_of`, and the Stage 4.4 counting — read in
  full at registration.
- Spec 102's package — the registration mechanics this
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
   D-098-2 pattern, as executed for Specs 099–102):
   the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy
   gains the study entry (spec.md, D-103-3); the
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
4. The commission is recorded in the sweep
   adjudication record (append-only addendum §OD-D-2)
   and the recommendations ledger's D-M-3 row moves
   open → accepted in the same landing.

## Stage plan

- **Stage 0 — registration (this landing).** The
  claim, the kill check, the protocol, and the
  outcome vocabulary are frozen on the record; the
  claims are intaken; no step of the check runs.
- **Stage 1 — execution (second landing, under the
  same OD-D-2 commission).** The acquired build is
  re-acquired openly and verified at its pin; Step 1
  reproduction (TC-103-02) runs first; the locus
  census (Step 2), witness comparison (Step 3), and
  boundary adjudication (Step 4) follow exactly as
  registered; the outcome record is filed in
  `records/` in §4's vocabulary, and the
  recommendations ledger's D-M-3 row moves to done
  if the execution completes. If a protocol step
  cannot be performed as registered — a witness class
  not actually held, a material the pin does not
  verify — execution stops, the gate is filed as the
  outcome record, and no substitute protocol is
  improvised.

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
  before the PR opens.

## Risks and limits

- **The witness may be thinner than the census.**
  Some held-out inscriptions may carry no second
  representation (no non-preferred open reading, no
  expansion entry). The design answers this in
  advance: §4's NOT CHECKED — INCOMPLETE COVERAGE is
  a first-class outcome with a mechanical rule, not
  a failure improvised after the fact.
- **The check cannot reach the printed page.** Its
  witnesses are the build's own second
  representations; a discrepancy between the build
  and Griffith's editions is outside its scope by
  registration (D-103-4), and no outcome of this
  check may be cited as edition-level verification.
- **Agreement is expected, and that is the point.**
  The expansion files are the build's transcription
  files of record; the frozen extraction's fidelity
  to them is exactly what a re-derivation could
  silently lose (assembly, dedup first-occurrence
  choice, tokenization), and exactly what this check
  measures. A CLAIM STANDS outcome is a measured
  result, not a formality.
- **The boundary is genuinely near for one form.**
  asoreyi sits 1 text below the bar; the check's
  value concentrates there and at the xolkte family's
  three sparse forms, and its census and adjudication
  are sized accordingly.
