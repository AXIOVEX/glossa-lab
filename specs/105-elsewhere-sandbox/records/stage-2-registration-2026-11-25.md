# Stage 2 registration — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

## 1. The act

Owner's resume order, Glossa-Lab chat, 2026-11-25 17:27 ET:
"those files should move too. And get back to the work here
for all 3 languages and the ELSEWHERE studies and all the
typical academia co-scientist work." The Stage 2 commission
for this study was issued under that order in the same chat.

This record registers Stage 2 of Spec 105 under spec.md
section 8: later stages execute only under their own
registrations amending this spec. It is committed before
any Stage 2 derivation runs; the landing's git history is
the proof of that order. Stage 2 executes exactly one
ladder rung, L2 (spec.md section 5), in all three
sandboxes. Not commissioned by this act, and not executed
in this stage: L3 and above; every boundary gate (G-ETE,
G-MER, G-IND); any unsealing, reading, or scoring of the
Indus reserve. No claim in this study carries a result by
this registration, and nothing in this stage moves any
anchor standing, verdict, or tally in any program
(C105-5). No recommendations-ledger row is opened
(D-105-3, the standing pattern for this study).

## 2. What L2 derives — procedure, frozen by this record

Per sandbox, the derivation's only inputs are that
sandbox's derivation dataset and the outputs of the lower
rungs of the same sandbox (spec.md section 4). The
datasets stand in custody at their current home,
~/.syncyard/worktrees/glossa/glossa-custody/spec105/ on
tower-compute (relocated 2026-11-25 under the owner's
home-root governance; the relocation is recorded in
PROGRAM-STATE, and the dataset hashes were re-verified
unchanged after the move). Dataset SHA-256, as filed at
Stage 1 and re-verified before any Stage 2 derivation
reads them:

- Indus derivation set: indus-derivation.json,
  84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b
- Eteocypriot: eteocypriot.json,
  2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe
- Meroitic: meroitic.json,
  a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7
- Indus reserve (sealed; hashed at this stage, never
  opened): indus-reserve.json,
  bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff

The rung's steps:

- **S1 — Tally.** Each token occurrence, in recorded
  order, increments its mark's tally: recurrence (P-4)
  made countable. Output: one count per mark of the L1
  inventory. This step is where number enters the
  sandbox: as a tally of recurrences, derived, never
  assumed (spec.md section 2, the demotion of counting).
- **S2 — Totals.** The corpus totals (artifacts, lines,
  groups, tokens) re-derived by counting the dataset's
  recorded structure (P-3, P-5). The derived totals must
  reproduce Stage 1's filed censuses exactly; a mismatch
  stops that sandbox at this step.
- **S3 — Frequency.** A mark's frequency is its count
  against the whole (spec.md section 5): frequency =
  count / tokens, filed as the exact reduced fraction.
  No decimal approximation is filed anywhere.
- **S4 — Derived ordering.** The frequency table is
  ordered by count descending; ties are ordered by the
  mark ascending in byte order. The ordering is part of
  the filed structure, so the two implementations of
  section 4 must produce it identically.
- **S5 — Shape.** From the agreed table: the inventory
  size; the singleton marks (count 1) and recurring
  marks (count 2 or more) counted, quantifying L1's
  recurrence mark; and the cumulative token share of
  the top 1, top 5, and top 10 marks, each as an exact
  fraction.

## 3. This stage's derivation log

The derivation log of a rung names each step and its
inputs (spec.md section 4). For L2:

- S1 inputs: the sandbox's L0 token streams (its
  derivation dataset, hash as above) and P-4
  (recurrence). Nothing else.
- S2 inputs: the same dataset's recorded artifact,
  line, and group structure (P-3, P-5).
- S3 inputs: S1's counts and S2's token total.
- S4 inputs: S3's table.
- S5 inputs: S3's table.

The outcome record restates this log with the run's
verified hashes and outputs. A step that needed any
other input would not be a derivation; none is taken.

## 4. The Indus unigram baseline (built here, consumed by G-IND later)

Spec.md section 7 names the registered baseline for
G-IND: the sandbox's own L2 frequency model. This stage
builds and files its parameters, from the Indus
derivation set alone:

- model: unigram; probability rule P(m) = count(m) /
  tokens over the derivation inventory (372 marks;
  tokens 5,611 as derived at S2);
- parameters: the agreed per-mark counts of S1 with
  their S3 frequencies, in the S4 order;
- filed at records/stage-2-indus-unigram-baseline-2026-11-25.json
  and as a section of the stage's raw output.

Marks outside the derivation inventory carry no filed
mass: the baseline as filed assigns probability only
over the 372 derivation marks. The G-IND gate stage
registers its unseen-mark rule and freezes its margin
before the reserve is unsealed (spec.md section 7);
this stage freezes neither, and does not score the
reserve. Building the baseline is a derivation-set act
only (TC-105-09).

## 5. Test cases registered for this stage

- **TC-105-08 — L2 purity and agreement (C105-1,
  C105-3, C105-4).** TC-105-05's discipline extended to
  this rung. The L2 derivation runs under two
  independently written implementations: A, a Python
  tally over the parsed dataset; B, a jq stream of the
  dataset's raw bytes through sort and uniq -c with an
  awk tally and fraction reduction, sharing no code
  with A. Each reads only its own sandbox's derivation
  dataset. *Pass:* in all three sandboxes the two
  implementations' ordered (mark, count, reduced
  frequency) tables are identical, their corpus totals
  are identical, the totals reproduce Stage 1's filed
  censuses, and the table sizes reproduce Stage 1's
  derived inventories (Indus 372, Eteocypriot 35,
  Meroitic 32). Any disagreement stops that sandbox
  and is reported with its evidence.
- **TC-105-09 — Reserve seal at Stage 2 (C105-4).**
  The reserve dataset's SHA-256 at this stage is
  compared against the hash filed at build
  (bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff);
  the Stage 2 scripts' opened paths are audited: the
  reserve is opened only by the hashing function,
  never parsed, and no Stage 2 input contains a
  reserve artifact. *Pass:* the hash matches and the
  input audit is clean.
- **TC-105-10 — Standing discipline at Stage 2
  (C105-5).** TC-105-07's check over this landing's
  full diff, executed at pull-request time. *Pass:*
  no record states a changed standing, verdict, or
  tally in any program; the stage's outputs appear
  only in this spec's records, labelled
  sandbox-internal; no working sign list, anchors
  register, or corpus file is modified; the
  recommendations ledger is untouched.

## 6. Outcome vocabulary and stop rules

Per sandbox, as in Stage 1 (spec.md section 6 applied
to this stage): **COMPLETED** (the rung derived as
registered) / **STOPPED** (the step that failed, named,
with its evidence). A dataset-hash failure stops that
sandbox before any derivation. An implementation
disagreement stops that sandbox at TC-105-08. One
sandbox's stop does not stop the others. Stage 2
returns no verdict about any language.

## 7. Decisions

- **D-105-10 — Stage 2 is registered by this record.**
  The amendment takes the program's record form (as
  adjudication and stage records do elsewhere in this
  repo); spec.md is not edited in place. The landing
  is confined to this spec's records folder.
- **D-105-11 — The study's two logs open in this
  landing.** Spec 105 registered on 2026-11-25, hours
  before the history-ledger convention and the
  ELSEWHERE framework's provenance standard were
  formalized the same day, and its package carried
  neither a history ledger nor a seed-and-iteration
  log. Both open in this landing
  (records/history-ledger.md;
  records/elsewhere-seed-and-iteration-log.md), their
  content before Stage 2 backfilled from the filed
  records and marked as backfilled, per the convention
  and framework sections 9-10. From Stage 2 on, both
  are written as the work happens.
