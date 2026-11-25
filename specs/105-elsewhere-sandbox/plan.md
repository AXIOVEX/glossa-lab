# Spec 105 — Plan

## Inputs

- The owner's order of 2026-11-25 (Glossa-Lab chat):
  "skip it then" (the Spec 104 quantum arm) followed
  by the ELSEWHERE direction — "define the only
  primitives as things we know without a doubt and
  derive our own mathematical and language meaning
  systems. Assume nothing about the real world, we
  do this in our ELSEWHERE sandbox for all 3
  languages" — which is this study's commission
  (spec.md, D-105-4). The decipherment gap analysis
  (program document, 2026-11-25) is its immediate
  background: each program is blocked by information,
  and the sandbox is the instrument that asks what
  the information already held implies when nothing
  is assumed.
- The ELSEWHERE discipline as the owner's framework
  carries it (the 2026-11-05 rule: the inside derives
  from a declared floor; the outside checks at gates
  and returns GOOD / NOT-GOOD; close-or-similar
  passes the first gates). The Riemann program's
  ELSEWHERE line (its Spec 018) is a separate line
  over hardware primitives; this study shares the
  discipline and imports none of its content
  (D-105-9).
- The three source corpora at their pins (spec.md
  §3): the Holdat corpus file (Spec 100's pin,
  verified against the primary data home on the
  mini-server at registration design time: SHA-256
  `62d14d2b…` and the roles file `eb6d3b6a…`, both
  matching their records); Spec 096's corpus and
  Androkles intake files at their current recorded
  bytes (with finding F-104-1's semantic-diff
  evidence for the stale freeze pin); the Kovetsky
  build at pin `145af083…` (the build Specs 097 and
  103 executed against; its `inscriptions.jsonl`
  SHA-256 counted at registration).
- Spec 104's package — the registration mechanics
  this landing follows: bundle intake, taxonomy
  entry, settling chain refresh in the standing
  order, generated layers, census pins.

## Adoption mechanics

1. This package (spec, claims, plan, tasks, test
   cases, the registration record) lands by PR on a
   fresh clone on tower-compute, under
   `~/.syncyard/worktrees/glossa/` (the home-root
   `~/glossa-work` was cleared by the owner's
   2026-11-23 cleanup order; clones never return to
   the home root).
2. Registration, in the standing order (Spec 098's
   D-098-2 pattern, as executed for Specs 099–104):
   the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy
   gains the study entry (spec.md, D-105-2); the
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
   D-105-3).

## Stage plan

- **Stage 0 — registration (this landing).** The
  floor census, the three build procedures with
  their pins and strip rules, the ladder, the gates,
  and the Stage 1 outcome vocabulary are frozen on
  the record; the claims are intaken; no dataset is
  built and no derivation runs.
- **Stage 1 — execution (second landing, under the
  same owner commission).** In order, per sandbox:
  (i) the source pin verified — the Holdat
  operational copy hashed against the Spec 100 pin,
  the Spec 096 files against §3.2's hashes, the
  Kovetsky build against its commit pin and file
  hash; a pin failure stops that sandbox and is
  filed as its outcome; (ii) the dataset built by
  the registered strip rule into custody
  (`~/glossa-custody/spec105/`), its SHA-256 filed
  in the outcome record, with the position-to-source
  mapping filed in the build record (outside the
  dataset); (iii) strip fidelity (TC-105-02,
  TC-105-03) and the stripping verification
  (TC-105-04) run against the built dataset and the
  source, and must pass before any derivation reads
  the dataset; (iv) L0–L1 derivations run under two
  independently written implementations whose
  inventories must agree exactly (TC-105-05), with
  the Indus derivation reading the derivation
  dataset only (TC-105-06); (v) the outcome record
  is filed in `records/` returning, per sandbox,
  COMPLETED or STOPPED exactly as registered
  (spec.md §6), with the recorded censuses as
  reproduced, the derived inventories, and the raw
  outputs saved to a dated file in the same landing,
  and TC-105-07's standing audit read over the
  landing's diff. **Stop rule:** if a step cannot be
  performed as registered — a pin fails, a census
  does not reproduce, a strip test fails, the two
  implementations disagree — that sandbox stops at
  that step, the failure is filed as its outcome,
  and no substitute procedure is improvised. One
  sandbox's stop does not stop the others.
- **Later stages (not commissioned).** L2 and above,
  and each boundary gate, execute only under their
  own registrations amending this spec (spec.md §8).
  The G-IND gate's registration must freeze its
  margin before the reserve is unsealed.

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
