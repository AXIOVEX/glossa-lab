# M048 — the missing corrected battery result — 2026-11-22

**Spec:** 091 (anchor comparison integrity). **Referral:**
RT2-08 (Red Team Round 2), whose threshold arm was executed
in the Round 2 execution and whose first arm — produce the
corrected battery result M048 never had — was referred to
this commission. **Commission:** the F-4 study package,
commissioned by the owner in chat 2026-11-22. **Execution
venue:** tower-compute (fresh clone `~/glossa-work/f4-package`
at origin/main `6bcd95eb`).

## 1. The gap this record fills

The corrected battery (battery v2, the T301 design executed
by T302 over the 28 `requires_revalidation` Phase-48
promotions) never ran on M048. T302's population was defined
by the revalidation flags, and M048's Phase-48 promotion
stands instead at `insufficient_evidence` under disposition
rule R4 — it is one of the GR-088-27 pair (with M367),
outside Spec 091 — so it was excluded from T302 with the
reason recorded, and no corrected result existed for it. Its
sibling in the comparison, M089, holds a filed corrected
result (score 2). The asymmetry was flagged in the register
reconciliation section (h) and at RT2-08. This record
produces M048's result by the same corrected method. (The
pair's other member, M367, was not in this commission; its
corrected result remains unproduced and this record does not
imply otherwise.)

## 2. Method — the battery's own code, its inputs validated

The result was produced by driving battery v2's own check
functions (`backend/scripts/phase48_medium_validation_v2.py`,
SHA-256
`68c0bcd6dc00c573545338dc70c23bbee05612b8e7a16ade9faa0372c98bdda6`)
for the single sign M048, reading "mu/muṉ" from the anchors
file of record, under the battery's own scoring rule: three
tri-state checks, a `not_run` never counts, score = number of
passes, promotion at score ≥ 2. Inputs, and how each was
validated:

- **Role row** (positional check): the in-repo roles file
  `data/raw/other_sites/holdatllc_all_symbol_semantic_roles_csv`
  (SHA-256 `ae144d4128d5f78275dca11ac75d9a6f525b591151c005c784c9d3c25e54a17b`
  — different bytes from the copy T302 staged, a fact stated
  here as T302's record stated its own pin). Before use, the
  file was validated against the WP5 support audit's
  reconstruction: it agrees with the audit on semantic_role
  and avg_position for **30 of 30** promoted signs. M048's
  row: count 157, avg_position 0.627, is_starter False,
  is_ending True, semantic_role CASE_MARKER_SUFFIX — identical
  to the audit's reconstruction on every field the check uses.
- **DEDR dataset** (DEDR check): the restored tree's
  `dedr_new.csv`, byte-identical to the restore record's
  verification (SHA-256
  `fbcc2b2d47c9be24338d846319de2b2c5a2ad4f45451274e3223bc63bc60cae0`;
  tree re-verified 15 of 15 in the F-4 digital-edition pass),
  staged at the battery's expected path for the run and
  removed after. T302 ran with this dataset not held; its
  record anticipated this configuration exactly: "If the
  dataset is restored to the program's holdings, a future run
  under a new commission could execute the leg." This is that
  run.
- **Corpus** (bigram check): the pinned Holdat corpus CSV
  (SHA-256 `62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`)
  is **not held on this venue** — the only files of that name
  present are 8-line synthetic test fixtures in archive test
  directories. The bigram check was therefore not executed,
  and no substitute corpus was used (the in-repo research
  export is a different population).

No act was filed into T302's acts file, which the battery's
own rule keeps closed; this result is a standalone run record
(`study-20261122T075700Z-f40448.json`, beside this record).

## 3. The result

| check | outcome | detail |
|---|---|---|
| positional | **PASS** | role CASE_MARKER_SUFFIX; avg_position 0.627 ≥ 0.5, is_ending True, is_starter False — every expectation met on inputs present in full |
| DEDR | **PASS** | `exact_match_3` — the battery's normalized reading ("mumu") has exactly 3 exact matches in the restored DEDR |
| bigram | **NOT_RUN** | corpus not held on the venue (section 2); not executed |

**Score: 2 of 3 (1 not_run). Promotion under the battery's
rule: TRUE — M048 meets the corrected battery's 2-point
promotion threshold.**

Two comparisons the record owes the reader:

- **Against the historical recorded battery** (WP5 audit
  reconstruction): the historical run recorded all three
  checks as passes — positional PASS, DEDR PASS with detail
  `exact_match_3`, bigram PASS at neighbour_match 3/4 = 75%.
  Battery v2 reproduces the positional and DEDR outcomes
  **exactly**, down to the DEDR detail string, under its
  corrected rules. The bigram leg's historical pass was
  genuine as recorded but backend-dependent — the P8 defect
  v2 exists to remove — and v2 cannot re-execute it without
  the corpus; it is carried here as a recorded observation,
  not as a v2 outcome, and the score above does not count it.
- **Against T302's input configuration**: had this run used
  T302's configuration (DEDR dataset not held), the DEDR leg
  would be `not_run` and the executed legs would score 1 —
  below threshold. The difference between the two
  configurations is solely the DEDR dataset's restoration on
  2026-11-19. The filed result is the current-holdings one,
  because the restoration is a fact of the program's holdings
  and T302's record named this commission as the leg's route.

## 4. Consequence handling — reported, not taken

RT2-08's adjudication states the consequence in advance: "if
M048's corrected battery is run under F-4 and scores at the
threshold, its class must be re-adjudicated." It has scored
at the threshold (2, with the third leg not_run for a named
custody reason). **That re-adjudication is a separate act and
is not performed by this record.** M048's class stands at U,
its anchor promotion entry stands as filed (including the
duplicated collocation counts the reconciliation noted —
M342 at n=13 and n=17, M176 at n=5 and n=8, M267 at n=7 —
which are the anchors record's to correct, not this run's),
and no act, standing or basis changes follow from this record
alone.

**Payload verdict: corrected battery result produced for
M048 under battery v2 by the battery's own code — positional
PASS, DEDR PASS (`exact_match_3`, reproducing the historical
detail exactly), bigram NOT_RUN (pinned corpus not held on
the venue; gap named), score 2, promotion threshold met. The
class re-adjudication RT2-08 attaches to this outcome is
referred, not executed.**
