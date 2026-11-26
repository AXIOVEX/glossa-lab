# Stage 4 registration — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

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
executed, and Stage 3 was commissioned and executed
under the directive itself earlier the same evening. The
Stage 4 commission for this study is issued under that
directive.

This record registers Stage 4 of Spec 105 under spec.md
section 8: later stages execute only under their own
registrations amending this spec. It is committed before
any Stage 4 derivation runs; the landing's git history
is the proof of that order. Stage 4 executes exactly one
ladder rung, L4 (spec.md section 5), in all three
sandboxes. Not commissioned by this act, and not
executed in this stage: L5 and above; every boundary
gate (G-ETE, G-MER, G-IND); any unsealing, reading, or
scoring of the Indus reserve. No claim in this study
carries a result by this registration, and nothing in
this stage moves any anchor standing, verdict, or tally
in any program (C105-5). No recommendations-ledger row
is opened (D-105-3, the standing pattern for this
study).

## 2. What L4 derives — procedure, frozen by this record

Spec.md section 5 registers L4 as substitution classes:
"Marks that exchange in parallel contexts (same
neighbours, P-3) form paradigms; groupings may be
re-derived here if the classes earn them." This section
freezes the procedure. Per sandbox, the derivation's
only inputs are the outputs of the lower rungs of the
same sandbox (spec.md section 4) and, for
implementation B, that sandbox's derivation dataset
(the L0 streams, from which B re-derives the contexts by
its own pass, in the two-implementation discipline of
Stages 1–3: the implementations take independent input
paths and must agree exactly, so agreement also
re-checks the filed L3 tables against the streams).
The filed lower-rung outputs are
`records/stage-3-output-2026-11-25.json` (the attested
ordered-pair table and the per-mark positional table,
from which the contexts are read) and
`records/stage-2-output-2026-11-25.json` (the totals
the stage reconciles against), both as landed at the
Stage 3 merge (`80936e9b`). The datasets stand in
custody at
~/.syncyard/worktrees/glossa/glossa-custody/spec105/ on
tower-compute. Dataset SHA-256, as filed at Stage 1 and
re-verified before any Stage 4 derivation reads them:

- Indus derivation set: indus-derivation.json,
  84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b
- Eteocypriot: eteocypriot.json,
  2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe
- Meroitic: meroitic.json,
  a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7
- Indus reserve (sealed; hashed at this stage, never
  opened): indus-reserve.json,
  bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff

**Contexts (D-105-16).** The context of a mark m is
three sets read from its L3 structure:

- **Succ(m)** — the set of distinct marks attested
  immediately after m within a recorded group (the
  distinct second marks of m's attested ordered
  pairs);
- **Pred(m)** — the set of distinct marks attested
  immediately before m within a recorded group (the
  distinct first marks of the pairs ending at m);
- **Pos(m)** — the positional support: the set of
  group-position classes (sole, initial, final,
  medial) in which m occurs at least once, per its
  filed L3 positional row.

A context is a set, not a count vector. How often a
neighbour occurs is a filed fact of L2 and L3; whether
it occurs at all is the parallel-context fact this rung
derives. Two marks stand in parallel contexts exactly
where their context sets are identical.

**The partitions (D-105-17).** Three equivalence
relations over the sandbox's L1 inventory, each filed
as a partition of the whole inventory:

- **Successor classes (σ):** m ~ m′ iff Succ(m) =
  Succ(m′).
- **Predecessor classes (π):** m ~ m′ iff Pred(m) =
  Pred(m′).
- **Joint classes — the substitution classes of this
  rung:** m ~ m′ iff Succ, Pred, and Pos all agree.
  Marks in one joint class exchange in every recorded
  parallel context the ladder has derived: the same
  attested successors, the same attested
  predecessors, the same positions. A joint class is
  a structural role inside the sandbox, nothing more:
  no phonetic value, no meaning, and no grammatical
  category is asserted or implied for any class or
  any mark.

The joint partition refines both one-sided partitions
by construction. The degenerate contexts are named,
not hidden: the marks with Succ(m) = ∅ (no attested
successor) share one σ-class, the empty-successor
class; likewise the marks with Pred(m) = ∅ share one
π-class; and a mark with both sets empty and Pos(m) =
{sole} occurs only as a sole token.

**No grouping re-derivation (D-105-18).** Spec.md
section 5 permits groupings to be re-derived at this
rung "if the classes earn them". This stage does not
exercise that permission: the classes are filed as
structure, and whether they earn a re-derived grouping
is a question for a later stage's registration, on the
filed classes. The recorded groups (P-3) remain the
only groupings in each sandbox.

The rung's steps:

- **S1 — Contexts.** Per mark of the inventory:
  Succ(m), Pred(m), and Pos(m) as defined above.
- **S2 — Partitions.** The three equivalence
  partitions of S1's contexts.
- **S3 — Canonical class tables.** Per kind, one row
  per class: its id, its size, its member marks in
  byte order, and its shared context (for σ, the
  shared successor set in byte order; for π, the
  shared predecessor set in byte order; for the joint
  classes, all three shared sets, the support named
  in byte order of the class names). Classes are
  ordered by size descending, ties by the member list
  compared element-wise in byte order; ids are
  assigned in that order (SC-1, SC-2, …; PC-1, …;
  JC-1, …).
- **S4 — Assignment table.** Per mark, ordered by
  mark in byte order: its σ-class id, its π-class id,
  its joint-class id, |Succ(m)|, |Pred(m)|, and
  |Pos(m)|.
- **S5 — Reconciliation and shape.** The L4 tables
  must reconcile with the filed L2 and L3 outputs
  exactly; every identity below is a check, and a
  failure stops that sandbox at this step:
  (i) partition: the sizes of each kind's classes sum
  to the inventory size;
  (ii) coverage: the assignment table covers exactly
  the L1 inventory, one row per mark;
  (iii) refinement: within every joint class, all
  members carry the same σ-class id and the same
  π-class id;
  (iv) signature consistency across the filed tables:
  for every mark, |Succ(m)| equals the filed L3
  successors_distinct and |Pred(m)| equals the filed
  L3 predecessors_distinct — the sets are derived
  from the filed pair table and the distinct counts
  stand in the filed positional table, two different
  filed tables, so the identity is a real cross-check
  (and implementation B derives both sides from the
  streams independently);
  (v) support consistency: for every mark, Pos(m) is
  exactly the set of group-position classes with
  positive count in its filed L3 positional row, and
  the sum of |Pos(m)| over the inventory equals the
  number of positive (mark, class) cells in the filed
  L3 positional table;
  (vi) bounds: the number of joint classes is at
  least the larger of the σ and π class counts and at
  most the inventory size.
  Shape, from the agreed tables: per kind, the number
  of classes, the largest class size, and the number
  of singleton classes; the marks in non-singleton
  joint classes (the marks with at least one exact
  parallel-context substitute); the size of the
  empty-successor σ-class and of the empty-predecessor
  π-class; and the first five joint classes in
  canonical order, with their members and shared
  context sizes.

No segmentation is imported or derived at this rung,
no group is called a word, and no mark or class is
given a phonetic, semantic, or grammatical reading. A
substitution class inside the sandbox is shared
recorded context, nothing more. The derived meaning
system is L5's business and is not touched here.

**Transport note.** Implementation B (section 4) moves
marks through tab-separated text. A recorded mark
carrying a tab or newline character would break that
transport; implementation A asserts that no mark in
the filed L3 tables carries one, and a violation stops
that sandbox at S1 with the mark named as evidence.
(The recorded marks of all three corpora, as the
Stage 1–3 outputs show, carry none.) The S3 tie-break
compares member lists element-wise in byte order;
implementation B's tab-joined byte comparison
reproduces it because the tab byte lies below every
byte of any recorded mark.

## 3. This stage's derivation log

The derivation log of a rung names each step and its
inputs (spec.md section 4). For L4:

- S1 inputs: the filed L3 tables of the same sandbox
  (implementation A); the same sandbox's L0 token
  streams, its derivation dataset (implementation B);
  P-2 (sequence), P-3 (co-presence), P-5 (boundary).
- S2 inputs: S1's contexts.
- S3 inputs: S2's partitions.
- S4 inputs: S3's tables and S1's context sizes.
- S5 inputs: S1–S4's tables and the filed L2 and L3
  outputs of the same sandbox.

The outcome record restates this log with the run's
verified hashes and outputs. A step that needed any
other input would not be a derivation; none is taken.

## 4. Test cases registered for this stage

- **TC-105-14 — L4 purity and agreement (C105-1,
  C105-3, C105-4).** TC-105-05's discipline extended to
  this rung. The L4 derivation runs under two
  independently written implementations: A, a Python
  derivation over the filed Stage 3 output (the pair
  and positional tables parsed as data); B, a jq event
  stream over the derivation dataset's raw bytes (one
  event per attested pair occurrence and per
  classified occurrence) through LC_ALL=C sort and
  uniq -c with awk assemblies of the per-mark
  contexts, the canonical class tables, and the
  assignment table, sharing no code with A. Each reads
  only its own sandbox's material (A: the filed L2 and
  L3 outputs of the same sandbox; B: the same
  sandbox's derivation dataset). *Pass:* in all three
  sandboxes the two implementations' canonical tables
  are identical — the three class tables and the
  assignment table — their corpus totals are identical
  and reproduce the filed L2/L3 totals, and every
  reconciliation identity of S5 holds exactly against
  the filed L2 and L3 tables. Any disagreement stops
  that sandbox and is reported with its evidence.
- **TC-105-15 — Reserve seal at Stage 4 (C105-4).**
  The reserve dataset's SHA-256 at this stage is
  compared against the hash filed at build
  (bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff);
  the Stage 4 scripts' opened paths are audited: the
  reserve is opened only by the hashing function,
  never parsed, and no Stage 4 input contains a
  reserve artifact. *Pass:* the hash matches and the
  input audit is clean.
- **TC-105-16 — Standing discipline at Stage 4
  (C105-5).** TC-105-07's check over this landing's
  full diff, executed at pull-request time. *Pass:*
  no record states a changed standing, verdict, or
  tally in any program; the stage's outputs appear
  only in this spec's records, labelled
  sandbox-internal; no working sign list, anchors
  register, or corpus file is modified; the
  recommendations ledger is untouched.

## 5. Outcome vocabulary and stop rules

Per sandbox, as in Stages 1–3 (spec.md section 6
applied to this stage): **COMPLETED** (the rung derived
as registered) / **STOPPED** (the step that failed,
named, with its evidence). A dataset-hash failure stops
that sandbox before any derivation. An implementation
disagreement stops that sandbox at TC-105-14. A
reconciliation failure stops that sandbox at S5. One
sandbox's stop does not stop the others. Stage 4
returns no verdict about any language.

## 6. Decisions

- **D-105-15 — Stage 4 is registered by this record.**
  The amendment takes the program's record form (as
  adjudication and stage records do elsewhere in this
  repo); spec.md is not edited in place. The landing
  is confined to this spec's records folder.
- **D-105-16 — A mark's context is its successor set,
  its predecessor set, and its positional support, and
  contexts are sets, not count vectors.** "Same
  neighbours" in spec.md section 5 reads on
  attestation: a neighbour either occurs beside a mark
  in the recordings or it does not. The counts are
  filed facts of L2 and L3; admitting them into the
  class definition would make classes turn on
  frequency, which this rung does not register.
  Position is part of a mark's recorded context by
  P-5, and its support (where the mark can stand, not
  how often it stands there) is the set-valued form of
  L3's positional structure.
- **D-105-17 — The rung files three partitions; the
  joint partition is the substitution classes
  proper.** The one-sided partitions are filed because
  they are the rung's intermediate structure and
  because the refinement identity (S5 iii) is
  checkable only with all three on file.
- **D-105-18 — No grouping re-derivation at this
  stage.** Spec.md section 5's permission is not
  exercised; the recorded groups remain the only
  groupings in each sandbox, and the question whether
  the classes earn a re-derived grouping is left to a
  later stage's registration, on the filed classes.
