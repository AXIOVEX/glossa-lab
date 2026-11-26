# Stage 3 registration — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

## 1. The act

The owner's keep-working directive, RCPH chat, 2026-11-25
19:07 ET: "Do not stop. Keep working on this until we take
it as far as we can. All the studies we're working on
including glossa-lab." The directive names this program
expressly, was forwarded to the Glossa-Lab chat under the
routing rule the same evening, and is recorded in
MEMORY.md. It continues the owner's resume order of the
same day (Glossa-Lab chat, 2026-11-25 17:27 ET) under
which Stage 2 of this study was commissioned and
executed. The Stage 3 commission for this study is
issued under that directive.

This record registers Stage 3 of Spec 105 under spec.md
section 8: later stages execute only under their own
registrations amending this spec. It is committed before
any Stage 3 derivation runs; the landing's git history
is the proof of that order. Stage 3 executes exactly one
ladder rung, L3 (spec.md section 5), in all three
sandboxes. Not commissioned by this act, and not
executed in this stage: L4 and above; every boundary
gate (G-ETE, G-MER, G-IND); any unsealing, reading, or
scoring of the Indus reserve. No claim in this study
carries a result by this registration, and nothing in
this stage moves any anchor standing, verdict, or tally
in any program (C105-5). No recommendations-ledger row
is opened (D-105-3, the standing pattern for this
study).

## 2. What L3 derives — procedure, frozen by this record

Spec.md section 5 registers L3 as order structure:
"Positional patterns from P-2 and P-5: which marks and
classes begin, end, and neighbour; a derived
combinatorics of the streams." This section freezes the
procedure. Per sandbox, the derivation's only inputs
are that sandbox's derivation dataset and the outputs
of the lower rungs of the same sandbox (spec.md
section 4): the L0 token streams (the dataset itself)
and the filed L2 outputs (`records/stage-2-output-2026-11-25.json`:
per-mark counts and corpus totals), with which the L3
tables must reconcile exactly (step T5). The datasets
stand in custody at
~/.syncyard/worktrees/glossa/glossa-custody/spec105/ on
tower-compute. Dataset SHA-256, as filed at Stage 1 and
re-verified before any Stage 3 derivation reads them:

- Indus derivation set: indus-derivation.json,
  84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b
- Eteocypriot: eteocypriot.json,
  2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe
- Meroitic: meroitic.json,
  a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7
- Indus reserve (sealed; hashed at this stage, never
  opened): indus-reserve.json,
  bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff

**The sequence unit and adjacency (D-105-13).** The
unit of order is the group as recorded (P-3, P-5).
Adjacency holds only between consecutive tokens of the
same group, in recorded order (P-2). No adjacency is
asserted across a group boundary, a line boundary, or
an artifact boundary: a recorded boundary is a break in
the order structure, not a join. For the Indus sandbox
(one group per artifact) the group sequence is the
artifact's whole stream; for Meroitic the groups are
the recorded space-separated runs within the artifact's
one line; for Eteocypriot the groups are the recorded
segments within their recorded lines.

The rung's steps:

- **T1 — Attested ordered pairs.** For each group of
  length n ≥ 2, its n−1 ordered pairs of consecutive
  marks (first, second) are tallied, counting as
  derived at L2. Output: the attested ordered-pair
  table — one row per distinct ordered pair, with its
  count — ordered by count descending, ties by the
  first mark ascending in byte order, then the second
  mark ascending in byte order (the S4 ordering rule of
  Stage 2, extended to pairs).
- **T2 — Neighbour structure.** From T1's table, per
  mark of the L1 inventory: its attested successors
  (the distinct second marks of its pairs) with their
  counts and their total; its attested predecessors
  (the distinct first marks) with their counts and
  their total. A mark with successor total 0 occurs
  only group-finally or as a sole token; a mark with
  predecessor total 0 occurs only group-initially or
  as a sole token. The neighbour structure is filed as
  part of the per-mark table of T3, not as a separate
  table.
- **T3 — Positional structure.** Each token occurrence
  is classified by its position in its group, in
  exactly one of four disjoint classes: **sole** (the
  only token of a group of length 1), **initial** (the
  first token of a group of length ≥ 2), **final**
  (the last token of a group of length ≥ 2), **medial**
  (any other token). Per mark: the four class counts.
  At the other recorded levels (P-5), per mark:
  **line-initial** and **line-final** occurrence counts
  (the first and last token of each recorded line; a
  line of one token counts its mark as both), and
  **artifact-initial** and **artifact-final** counts
  (the same rule at the artifact level). Output: the
  per-mark positional table — mark, its L2 count, the
  four group-position class counts, the four
  line/artifact boundary counts, successor and
  predecessor distinct counts and totals (T2) —
  ordered by mark ascending in byte order.
- **T4 — Sequence-length structure.** The group-length
  distribution (the number of groups of each recorded
  length) and the line-length distribution (the number
  of lines of each recorded token length), each ordered
  by length ascending, counted as derived at L2.
- **T5 — Reconciliation and shape.** The L3 tables must
  reconcile with the filed L2 outputs exactly; every
  identity below is a check, and a failure stops that
  sandbox at this step:
  (i) per mark, sole + initial + final + medial equals
  the mark's filed L2 count;
  (ii) per mark, successor total equals the L2 count
  minus final minus sole, and predecessor total equals
  the L2 count minus initial minus sole;
  (iii) the sum of all pair counts equals tokens minus
  groups (each group of length n contributes n−1
  pairs);
  (iv) the line-initial counts sum to the number of
  lines, and the line-final counts likewise; the
  artifact-initial and artifact-final counts sum to
  the number of artifacts;
  (v) the group-length distribution sums to the number
  of groups and its length-weighted sum equals the
  token total; the line-length distribution sums to
  the number of lines and its length-weighted sum
  equals the token total.
  Shape, from the agreed tables: the number of distinct
  attested ordered pairs; the inventory-squared count
  of possible ordered pairs, for scale; the pairs
  attested once and the pairs recurring; the total
  count of self-pairs (a, a); the marks with no
  attested successor, no attested predecessor, neither,
  and both; and the top 10 attested pairs under the T1
  ordering, with their counts.

No segmentation is imported or derived at this rung:
the groups are the recorded groups (P-3), no group is
called a word, and no mark is given a phonetic,
semantic, or grammatical reading. Order structure
inside the sandbox is adjacency and position as
recorded, nothing more. Substitution classes are L4's
business and are not touched here.

**Transport note.** Implementation B (section 4) moves
marks through tab-separated text. A recorded mark
carrying a tab or newline character would break that
transport; implementation A asserts that no mark in
its dataset carries one, and a violation stops that
sandbox at T1 with the mark named as evidence. (The
recorded marks of all three corpora, as the Stage 1
and Stage 2 outputs show, carry none.)

## 3. This stage's derivation log

The derivation log of a rung names each step and its
inputs (spec.md section 4). For L3:

- T1 inputs: the sandbox's L0 token streams (its
  derivation dataset, hash as above), P-2 (sequence),
  P-5 (boundary), and counting as derived at L2.
- T2 inputs: T1's table.
- T3 inputs: the same dataset's recorded group, line,
  and artifact structure (P-3, P-5) and counting as
  derived at L2.
- T4 inputs: the same dataset's recorded group and
  line structure (P-5).
- T5 inputs: T1–T4's tables and the filed L2 table
  (a lower-rung output of the same sandbox).

The outcome record restates this log with the run's
verified hashes and outputs. A step that needed any
other input would not be a derivation; none is taken.

## 4. Test cases registered for this stage

- **TC-105-11 — L3 purity and agreement (C105-1,
  C105-3, C105-4).** TC-105-05's discipline extended to
  this rung. The L3 derivation runs under two
  independently written implementations: A, a Python
  derivation over the parsed dataset; B, a jq event
  stream over the dataset's raw bytes (one event per
  pair, per classified occurrence, per boundary
  occurrence, per group and line length) through
  LC_ALL=C sort and uniq -c with an awk assembly of the
  canonical tables, sharing no code with A. Each reads
  only its own sandbox's derivation dataset (and, for
  T5, the filed L2 output of the same sandbox).
  *Pass:* in all three sandboxes the two
  implementations' canonical tables are identical —
  the ordered pair table, the per-mark positional
  table, and the two length distributions — their
  corpus totals are identical and reproduce the filed
  L2 totals, and every reconciliation identity of T5
  holds exactly against the filed L2 table. Any
  disagreement stops that sandbox and is reported with
  its evidence.
- **TC-105-12 — Reserve seal at Stage 3 (C105-4).**
  The reserve dataset's SHA-256 at this stage is
  compared against the hash filed at build
  (bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff);
  the Stage 3 scripts' opened paths are audited: the
  reserve is opened only by the hashing function,
  never parsed, and no Stage 3 input contains a
  reserve artifact. *Pass:* the hash matches and the
  input audit is clean.
- **TC-105-13 — Standing discipline at Stage 3
  (C105-5).** TC-105-07's check over this landing's
  full diff, executed at pull-request time. *Pass:*
  no record states a changed standing, verdict, or
  tally in any program; the stage's outputs appear
  only in this spec's records, labelled
  sandbox-internal; no working sign list, anchors
  register, or corpus file is modified; the
  recommendations ledger is untouched.

## 5. Outcome vocabulary and stop rules

Per sandbox, as in Stages 1 and 2 (spec.md section 6
applied to this stage): **COMPLETED** (the rung derived
as registered) / **STOPPED** (the step that failed,
named, with its evidence). A dataset-hash failure stops
that sandbox before any derivation. An implementation
disagreement stops that sandbox at TC-105-11. A
reconciliation failure stops that sandbox at T5. One
sandbox's stop does not stop the others. Stage 3
returns no verdict about any language.

## 6. Decisions

- **D-105-12 — Stage 3 is registered by this record.**
  The amendment takes the program's record form (as
  adjudication and stage records do elsewhere in this
  repo); spec.md is not edited in place. The landing
  is confined to this spec's records folder.
- **D-105-13 — Adjacency is group-internal only.** A
  recorded boundary (group, line, artifact) breaks the
  order structure; no pair is formed across one. The
  alternative — joining streams across boundaries —
  would assert an order the recording does not record
  (P-2 admits only the recording's order, and P-5
  admits the boundaries as recorded).
- **D-105-14 — The positional classification is the
  four-way disjoint classification of T3.** Sole,
  initial, final, and medial partition every
  occurrence, which is what makes reconciliation
  identity (i) an exact check against L2 rather than
  an approximation. At the line and artifact levels a
  one-token unit counts its mark as both initial and
  final, so identities (iv) hold exactly as well.
