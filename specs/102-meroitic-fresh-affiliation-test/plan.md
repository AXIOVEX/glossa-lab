# Spec 102 — Plan

## Inputs

- Adjudication unit M-18 and the owner's OD-21 act
  of 2026-11-22 (`specs/091-anchor-comparison-
  integrity/records/coscientist-refresh-
  adjudication-2026-11-22.md`).
- The OD-15 power and simulation audit
  (`specs/097-meroitic-reproduction-benchmark/
  records/power-simulation-audit-2026-11-22.md`):
  the executed design's minimum detectable effects
  and the asymmetry of the Stage 4.2 failures; its
  §4 injection method is this design's G-2 method.
- The OD-17 dependency audit (same directory):
  candidate-wise denominators, the joint permutation
  null as the operative null, the absent across-test
  correction, and flag F-A (freeze v3 §3's
  mislabelled table), which spec §3.8 closes by
  construction.
- The OD-14 custody clarification programme and
  refusal protocol (same directory): the authority
  chain spec §3.1's table is taken from, element by
  element, and the refusal protocol that binds this
  spec.
- The OD-16 freeze v2/v3 comparison (same
  directory): the two freezes are executably
  equivalent on every verdict-bearing quantity, so
  no part of this design needs to re-litigate them.
- Spec 097's package — the form this package
  follows: spec, claims, freeze discipline,
  adjudication vocabulary (freeze v2 §5), the
  varietas discipline (freeze v2 §7).
- Spec 101's package — the registration mechanics
  this landing follows: bundle intake, taxonomy
  entry, settling chain refresh in the standing
  order, generated layers, census pins.

## Adoption mechanics

1. This package (spec, claims, plan, tasks, test
   cases, the design-stage counts record, the
   registration record) lands by PR on a fresh
   clone on tower-compute.
2. Registration, in the standing order (Spec 098's
   D-098-2 pattern, as executed for Specs 099, 100
   and 101): the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy
   gains the study entry (spec.md, D-102-3); the
   settling chain runs in order — verify-canonicals
   over the grown build before the pin moves, the
   T405 scenario pair re-executed with byte-equal
   result blocks, the comparison re-filed, the
   assignment sets re-materialized, the canonical
   pin refreshed with its `re_derivations` entry,
   the superseded generation's departure accounted;
   the generated layers regenerate in dependency
   order (matrix, map data, program map); every
   census pin in the conformance and dashboard
   tests is updated from the regenerated actuals
   and the affected tests run before the PR opens.
3. The AEE assessment of the bundle is run and
   filed under `records/` (the draft-stage reading
   is expected; an inability to run it is recorded,
   never papered over).

## Stage plan

- **Stage 0 — registration (this landing).** The
  design, its gates, its power profile, and its
  adjudication vocabulary are frozen on the record;
  the claims are intaken; no stage of the study runs.
- **Stage 1 — acquisition (gated: fresh owner
  commission; the acquisition act itself separately
  owner-gated).** S-1 acquired and digitised with
  per-entry apparatus (T101).
- **Stage 2 — vocabulary build (gated).** The
  complete mapping table written; the attestation
  filter run under the §3.6 split construction;
  exclusions counted and listed (T201).
- **Stage 3 — freeze and gates (gated).** The
  freeze filed in full (§3.8); G-1 and G-2 computed;
  a gate failure closes the study NOT ADMINISTERED
  at this stage (T301).
- **Stage 4 — scoring (gated on both gates).** Leg
  A scored twice for byte-identical reproduction,
  with independent recomputation; Arm R filed
  separately as exploratory (T401).
- **Stage 5 — outcome (gated).** The outcome record
  in §5's vocabulary, Leg B's state recorded, the
  adjudication package prepared for the owner's
  approval act (T501).

## Verification

- Every stage's checks run on tower-compute in the
  stage's own fresh clone; each run's raw output is
  filed or hashed in the stage record, and the
  verdict reported is the run's own payload verdict.
- PRs merge only on genuine per-job CI green across
  all ten jobs; a zero-step or cancelled run is NO
  VERDICT, never green.
- Registration's own verification is the ledger
  gate and the program-map conformance checks on
  the landed tree, plus the affected backend suites
  run before the PR opens.

## Risks and limits

- **The acquisition may not reach the gate.** The
  fuller published wordlist's ASJP-mappable yield
  is not known until it is digitised; if G-1 fails,
  the honest outcome is NOT ADMINISTERED, and the
  R1 question stays open at exactly the strength
  OD-15 measured. The design registers that
  possibility rather than diluting the gate.
- **The wordlist is one scholarly tradition.**
  S-1, the gold lexicon, and the formative apparatus
  descend substantially from Rilly's work (the
  framework dependence OD-17 D-6 confirms). The
  attestation filter and the OD-18 expert channel
  are mitigations, not cures; the freeze must state
  the dependence, and no outcome may be cited as
  independent of the tradition that produced the
  wordlist.
- **Transcription quality.** The S-2 corpus is a
  measured-accuracy transcription of century-old
  editions (OD-14 Element 2's caveat); attestation
  failures may be transcription failures, and the
  freeze reports the exclusion count so the size of
  that channel is on the record.
- **The conditional frame flatters.** G-2's method
  is OD-15 §4's injection frame, which conditions
  on the frozen lists; the prospective binomial
  bound is carried in spec §4 so the gate is not
  read as stronger than it is.
