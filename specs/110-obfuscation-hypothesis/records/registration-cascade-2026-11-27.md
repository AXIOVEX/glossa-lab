# Spec 110 registration cascade — 2026-11-27

The registration commit carries the grown ledger, the refreshed pin,
and the re-executed pair. The prior generation's three run records
depart the store in the same motion; their departure acts are appended
to the run index in the completion commit that follows, naming this
commit, and the gated publications and the gate are re-run over the
final tree there (the Spec 107 M-2 pattern).

## Baseline

- Ledger on main at the cascade's start: 1,133 lines; canonical
  SHA-256 `542c7fa290e7dc24efc6ba4fa2eec0d63fae1c5cae6cfd9f9e2c9b51ac3
  bff04b` (pin: re_derivations[30] of
  `glossa-indus/ledger/settling-canonical.json`).
- The AEE assessment over the six-claim bundle returned **iterate**
  (the standard registration outcome): 6 claims assessed, 23 failure
  modes; all six claims draft-capped below the 0.70 threshold, all
  below 'explained' under the stage cap. Assessment filed at
  `records/aee-assessment-2026-11-27.json`.
- TC-110-01 (package form): **PASS**, payload exit 0 — bundle ids and
  order equal the claims.md set C110-1..C110-6; every falsifier and
  does-not-establish line present in both files; spec.md carries the
  registered sections; the registration record carries the statistics,
  bands, gate, verdict rules, and handling.
- The taxonomy gained the Spec 110 entry under Program infrastructure /
  Governance, lifecycle & generated layers; studies count 111.

## Intake and pin

- `import_bundle.py --spec specs/110-obfuscation-hypothesis
  --date 2026-11-27`: **6 appended, 0 already canonical, 6
  propositions.**
- Ledger: **1,139 lines**; canonical SHA-256
  `a914984740310a301cb3e1c1a8780a58d5edc212bf9998772a4114f37f1d62fa`.
- `validate_ledger.py`: **PASS** — errors none; 1,094 claim entries
  (does_not_establish coverage 755 of 1,094 as the intake counts it).
- `verify-canonicals`: **6/6 PASS** over the grown build.

## The T405 pair re-executed

- Incumbent run `settling-20261128T003231Z-486124`; full-register run
  `settling-20261128T003231Z-5502ae` (candidate field read from each
  record: 486124 is the incumbent, 5502ae the full-register). Both
  result blocks are **byte-equal** to the superseded generation's
  (incumbent `settling-20261127T194911Z-13948f`, full-register
  `settling-20261127T194911Z-c44e3e`) in every block except `run` and
  `pins` — the only difference is the ledger pin itself.
- Comparison re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the previous filing is exactly the ledger pin
  (sha256 + lines).
- Materialization re-run `settling-20261128T003303Z-a36ba8`: assignment
  sets unchanged (incumbent 94 assignments, full-register 286, H003
  out of frame).
- Pin refreshed in the same motion: re_derivations entry **[31]**
  appended and `provenance.ledger` moved to the new pin.

## Departures executed in this commit

- `settling-20261127T194911Z-13948f.json` — sha256
  `bbe1e0a6d02691d94ae2b549078376b50bb59506dbdc51aaf0114ed084aea969`,
  git blob `d624b3bf8f149065f070b38e64dcf0aafd31efd9`.
- `settling-20261127T194911Z-c44e3e.json` — sha256
  `292643086cde497e4062ea2d050aab8c23ff5e63257a750266191f6931046e72`,
  git blob `c1c288d886c88b2b73c476406039a2fedab993ee`.
- `settling-20261127T194943Z-6d174a.json` — sha256
  `28b3ac5e21a44ca192f5758204bab335c52eca16efefe631cf03ad5aec0fc3f4`,
  git blob `05b9b456348ffa2e72f342aa840b661cde0b672a`.

## Generated layers regenerated

- Matrix: written; matrix.json sha256 `4dbc4053…`; **1,617 cells** (one
  per map edge).
- Map: claims 1,094; elements 1,739; edges 1,617; falsifier census
  **1,085 of 1,094** (the same 9 pre-existing extracted-population
  gaps); settling runs carried: 2.
- Program map: claims 1,094 · studies 111 · unjudged studies 28 ·
  judgment calls 0.
- Census pins updated in the five pin-carrying backend test files and
  the two frontend e2e census texts.
- Ledger gate over the registration tree before the completion acts:
  31 PASS / 1 FAIL / 1 NOT-RUN, the single FAIL being V11 run-binding
  naming exactly the three departed records — the expected mid-cascade
  state, cleared by the completion commit's departure acts.
