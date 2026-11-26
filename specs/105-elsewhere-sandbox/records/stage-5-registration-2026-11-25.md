# Stage 5 registration — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

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
executed, and Stages 3 and 4 were commissioned and
executed under the directive itself earlier the same
evening. The Stage 5 commission for this study is issued
under that directive.

This record registers Stage 5 of Spec 105 under spec.md
section 8: later stages execute only under their own
registrations amending this spec. It is committed before
any Stage 5 derivation runs; the landing's git history
is the proof of that order. Stage 5 executes exactly one
ladder rung, L5 (spec.md section 5), in all three
sandboxes. Not commissioned by this act, and not
executed in this stage: L6 — every boundary gate (G-ETE,
G-MER, G-IND); any unsealing, reading, or scoring of the
Indus reserve. No claim in this study carries a result
by this registration, and nothing in this stage moves
any anchor standing, verdict, or tally in any program
(C105-5). No recommendations-ledger row is opened
(D-105-3, the standing pattern for this study).

## 2. What L5 derives — procedure, frozen by this record

Spec.md section 5 registers L5 as the derived meaning
system: "A mark's meaning inside the sandbox **is** its
derived structural role: its substitution class, its
positions, its companions. Nothing more is claimed, and
the claim is about the sandbox's system, not about any
language in the world." This section freezes the
procedure.

**No semantic content (D-105-23).** The word "meaning"
in this rung's name is the spec's own term for a mark's
derived structural role inside the sandbox, and it
carries nothing else. Nothing in this stage assigns or
implies a phonetic value, a gloss, a translation, or a
grammatical or semantic category for any mark, class, or
role; no role record is evidence about any language in
the world; and no output of this stage is a decipherment
claim (C105-5). A role is a profile of recorded
structure, stated in the sandbox's own derived terms
only.

Per sandbox, the derivation's only inputs are the
outputs of the lower rungs of the same sandbox (spec.md
section 4) and, for implementation B, that sandbox's
derivation dataset (the L0 streams, from which B
re-derives the frequency, context, and class structures
by its own passes, in the two-implementation discipline
of Stages 1–4: the implementations take independent
input paths and must agree exactly, so agreement also
re-checks the filed L2, L3, and L4 tables against the
streams). The filed lower-rung outputs are
`records/stage-2-output-2026-11-25.json` (the frequency
table), `records/stage-3-output-2026-11-25.json` (the
attested ordered-pair table and the per-mark positional
table), and `records/stage-4-output-2026-11-25.json`
(the three class tables and the assignment table), all
as landed at the Stage 4 merge (`8a54d0ec`). The
datasets stand in custody at
~/.syncyard/worktrees/glossa/glossa-custody/spec105/ on
tower-compute. Dataset SHA-256, as filed at Stage 1 and
re-verified before any Stage 5 derivation reads them:

- Indus derivation set: indus-derivation.json,
  84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b
- Eteocypriot: eteocypriot.json,
  2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe
- Meroitic: meroitic.json,
  a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7
- Indus reserve (sealed; hashed at this stage, never
  opened): indus-reserve.json,
  bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff

**The role record (D-105-20).** The role of a mark m,
R(m), is one record assembling the mark's complete filed
profile across the ladder, every component read from the
filed lower-rung outputs of the same sandbox:

- **Frequency position (L2):** count(m); the frequency
  of m as the filed reduced fraction; and rank(m), the
  mark's position (1-based) in the filed L2 derived
  ordering (count descending, ties by mark in byte
  order).
- **Attested relations (L3):** Succ(m) and Pred(m), the
  attested successor and predecessor sets of L4's
  context definition (D-105-16).
- **Positional support (L3):** Pos(m), the set of
  group-position classes (sole, initial, final, medial)
  in which m occurs at least once.
- **Substitution-class assignment (L4):** m's
  successor-class id, predecessor-class id, and
  joint-class id from the filed assignment table, and
  the size of m's joint class. The joint class is the
  substitution class proper (D-105-17); its shared
  context is the Succ / Pred / Pos triple itself.

**Role identity (D-105-21).** The identity key of a
role is its content: the tuple (count(m), Succ(m),
Pred(m), Pos(m)). Two marks share a role — are
role-identical — exactly where their keys are equal.
The identity classes, the partition of the inventory by
the key, are filed as a canonical table: one row per
class with its id (RC-1, RC-2, …), its size, its member
marks in byte order, and the shared key (the count, the
frequency fraction it determines against the sandbox
total, and the three shared sets). Classes are ordered
by size descending, ties by the member list compared
element-wise in byte order; ids are assigned in that
order. The class ids of the lower rungs and the rank
are filed in the role record but are **not** key
components: an id is a label of a class, not content;
and a mark's rank among marks of equal count is fixed
by the byte order of the marks' recorded identities
(the L2 ordering's tie-break), a property of the
recorded names, not of the structural profile. A role
is what the ladder derives about a mark with the mark's
recorded identity set aside, so nothing that depends on
that identity's byte order can enter the key. Marks
sharing a key necessarily share all three of their L4
class ids as well, since equal Succ fixes the successor
class, equal Pred the predecessor class, and the triple
the joint class; the key is stated in content terms so
that identity is a fact about profiles, not about the
numbering a stage happened to assign.

**Role overlap (D-105-22).** Overlap is graded by
component agreement over the four key components
(frequency, successors, predecessors, positions). For
two distinct marks, their overlap degree is the number
of the four components on which they agree, from 0 to
4; degree 4 is role identity. Per mark, ordered by mark
in byte order, the stage files: the counts of other
marks at each degree 0–4, and the member lists at
degrees 3 and 4 (the degree-4 list is the mark's
identity class minus itself). For the sandbox as a
whole, the stage files the number of unordered pairs at
each degree 0–4. Overlap below degree 4 is a relation,
not a partition: it is not transitive, and no class is
formed from it.

The rung's steps:

- **S1 — Role records.** Per mark of the inventory:
  R(m) as defined above, filed ordered by mark in byte
  order.
- **S2 — Identity partition.** The partition of the
  inventory by the identity key, filed as the canonical
  identity class table.
- **S3 — Overlap table.** Per mark, the degree counts
  and the degree-3 and degree-4 member lists; and the
  sandbox's unordered pair counts at each degree.
- **S4 — Reconciliation and shape.** The L5 tables must
  reconcile with the filed L2, L3, and L4 outputs
  exactly; every identity below is a check, and a
  failure stops that sandbox at this step:
  (i) coverage and partition: the role table covers
  exactly the L1 inventory, one row per mark; the
  identity class sizes sum to the inventory size;
  (ii) frequency consistency: for every mark, the
  count and the frequency fraction equal the filed L2
  row, the rank equals the mark's position in the
  filed L2 ordering, and the counts sum to the filed
  token total;
  (iii) context consistency: for every mark, Succ and
  Pred equal the sets read from the filed L3 pair
  table, their sizes equal the filed L3 distinct
  counts, and Pos equals the set of position classes
  with positive count in the filed L3 positional row;
  (iv) assignment consistency: for every mark, the
  three class ids and the joint class size equal the
  filed L4 assignment and class tables; the filed
  joint class's shared context equals the mark's key
  context; and every identity class's members share
  one joint-class id (identity refines the joint
  partition);
  (v) overlap consistency: for every mark, the degree
  counts sum to the inventory size minus one; the
  degree-4 member list equals the mark's identity
  class minus itself; for each degree, the sum over
  marks of the degree counts is even and equals twice
  the filed pair count at that degree; and the
  degree-4 count sum equals the sum over identity
  classes of size × (size − 1);
  (vi) bounds: the number of identity classes is at
  least the number of joint classes and at most the
  inventory size.
  Shape, from the agreed tables: the inventory size;
  the number of identity classes (distinct roles); the
  largest identity class size; the number of marks
  sharing a role (in non-singleton identity classes)
  and the number whose role is unique; the unordered
  pair counts at degrees 0–4; the number of marks with
  at least one degree-3 partner; and the first five
  identity classes in canonical order, with their
  members and shared counts.

No segmentation is imported or derived at this rung, no
group is called a word, and no mark, class, or role is
given a phonetic, semantic, or grammatical reading. The
derived meaning system this rung files is the role
system itself — each mark's structural role, the roles
that coincide, and the graded overlap between roles —
and it is the last derivation rung of the ladder: above
it stand only the boundary gates of L6, which are not
this stage's business and are not touched here.

**Transport note.** Implementation B (section 4) moves
marks through tab-separated text. A recorded mark
carrying a tab or newline character would break that
transport; implementation A asserts that no mark in the
filed L2, L3, or L4 tables carries one, and a violation
stops that sandbox at S1 with the mark named as
evidence. (The recorded marks of all three corpora, as
the Stage 1–4 outputs show, carry none.) The S2
tie-break compares member lists element-wise in byte
order; implementation B's tab-joined byte comparison
reproduces it because the tab byte lies below every
byte of any recorded mark.

## 3. This stage's derivation log

The derivation log of a rung names each step and its
inputs (spec.md section 4). For L5:

- S1 inputs: the filed L2, L3, and L4 outputs of the
  same sandbox (implementation A); the same sandbox's
  L0 token streams, its derivation dataset
  (implementation B); the floor (P-1 – P-5) as the
  lower rungs applied it.
- S2 inputs: S1's role records (their identity keys).
- S3 inputs: S1's role records (their key components).
- S4 inputs: S1–S3's tables and the filed L2, L3, and
  L4 outputs of the same sandbox.

The outcome record restates this log with the run's
verified hashes and outputs. A step that needed any
other input would not be a derivation; none is taken.

## 4. Test cases registered for this stage

- **TC-105-17 — L5 purity and agreement (C105-1,
  C105-3, C105-4).** TC-105-05's discipline extended to
  this rung. The L5 derivation runs under two
  independently written implementations: A, a Python
  derivation over the filed Stage 2, Stage 3, and Stage
  4 outputs (the frequency, pair, positional, class,
  and assignment tables parsed as data); B, a set of jq
  event streams over the derivation dataset's raw bytes
  (occurrence, pair, and classified-occurrence events)
  through LC_ALL=C sort and uniq -c with awk assemblies
  of the per-mark counts and ranks, the per-mark
  contexts, the three L4 partitions and assignment, the
  role records, the identity classes, and the overlap
  table, sharing no code with A. Each reads only its
  own sandbox's material (A: the filed L2, L3, and L4
  outputs of the same sandbox; B: the same sandbox's
  derivation dataset). *Pass:* in all three sandboxes
  the two implementations' canonical tables are
  identical — the role table, the identity class table,
  and the overlap table — their corpus totals are
  identical and reproduce the filed L2/L3/L4 totals,
  and every reconciliation identity of S4 holds exactly
  against the filed L2, L3, and L4 tables. Any
  disagreement stops that sandbox and is reported with
  its evidence.
- **TC-105-18 — Reserve seal at Stage 5 (C105-4).**
  The reserve dataset's SHA-256 at this stage is
  compared against the hash filed at build
  (bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff);
  the Stage 5 scripts' opened paths are audited: the
  reserve is opened only by the hashing function,
  never parsed, and no Stage 5 input contains a
  reserve artifact. *Pass:* the hash matches and the
  input audit is clean.
- **TC-105-19 — Standing discipline at Stage 5
  (C105-5).** TC-105-07's check over this landing's
  full diff, executed at pull-request time. *Pass:*
  no record states a changed standing, verdict, or
  tally in any program; the stage's outputs appear
  only in this spec's records, labelled
  sandbox-internal; no working sign list, anchors
  register, or corpus file is modified; the
  recommendations ledger is untouched.

## 5. Outcome vocabulary and stop rules

Per sandbox, as in Stages 1–4 (spec.md section 6
applied to this stage): **COMPLETED** (the rung derived
as registered) / **STOPPED** (the step that failed,
named, with its evidence). A dataset-hash failure stops
that sandbox before any derivation. An implementation
disagreement stops that sandbox at TC-105-17. A
reconciliation failure stops that sandbox at S4. One
sandbox's stop does not stop the others. Stage 5
returns no verdict about any language.

## 6. Decisions

- **D-105-19 — Stage 5 is registered by this record.**
  The amendment takes the program's record form (as
  adjudication and stage records do elsewhere in this
  repo); spec.md is not edited in place. The landing
  is confined to this spec's records folder.
- **D-105-20 — The role record is the complete filed
  profile.** Spec.md section 5 names the role as the
  mark's substitution class, positions, and companions;
  this stage files those together with the mark's
  frequency position, which is the remaining filed
  component of the mark's profile across the ladder, so
  that the role record is the whole of what the ladder
  has derived about the mark and nothing else has to be
  consulted to state it. The frequency component enters
  the identity key as the count (with its fraction,
  which the count and the sandbox total determine), not
  as a class or a band.
- **D-105-21 — Role identity is keyed on content, not
  on labels or on byte order.** The key is (count,
  Succ, Pred, Pos). Class ids are labels assigned by a
  stage's canonical ordering and carry no content
  beyond the classes they name, whose content the key
  already contains; rank among equal counts is an
  artifact of the tie-break on recorded identities.
  Keying identity on either would make the identity
  relation a fact about this stage's bookkeeping rather
  than about the derived profiles.
- **D-105-22 — Overlap is component-agreement degree,
  and only degree 4 forms classes.** A graded relation
  is filed because the identity relation alone would
  report only coincidence or its absence; the degree
  records how much of two roles is shared, component by
  component, at the same set-valued standard the ladder
  has used since L4. Degrees below 4 define no
  equivalence and no grouping is formed from them.
- **D-105-23 — No semantic content.** "Meaning" at L5
  is the spec's term for derived structural role
  (spec.md section 5) and nothing more: this stage
  assigns no phonetic value, gloss, translation, or
  grammatical or semantic category to any mark, class,
  or role, and its outputs are sandbox-internal in the
  standing sense (C105-5) until a boundary gate — not
  commissioned here — says otherwise about a specific
  comparison.
