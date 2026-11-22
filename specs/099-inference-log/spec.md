# Spec 099 — The Inference Log: Derivation Record and Dependency Graph Audit of the 94 Strict-Core Readings

**Status: ADOPTED 2026-11-21** (owner's commission in the
Glossa-Lab chat, 2026-11-21 22:14 ET: "Commission the
inference-log build" — flag F-4, first item, of the Red Team
Round 1 adjudication). This package builds the artefact whose
absence has blocked two named pieces of program work since
2026-11-21, and executes the first of them as its own first
execution. It fabricates nothing the record does not hold: the
log is extracted from the filed bases, and every classification
the filed basis does not settle is recorded as ambiguous, with
its reason, never resolved silently.

**Provenance.** Three records converge on this build.

1. The adjudication of the independent Co-scientist audit of
   the 94 strict-core readings
   (`specs/091-anchor-comparison-integrity/records/coscientist-audit-94-adjudication-2026-11-21.md`),
   section 3 (Q3), required a graph audit of the 94: "obtain
   the inference log for every reading (assignment date,
   evidence dates, source observations, all assumed neighbour
   values); label edges as raw observation, semantic assumption
   or score inheritance; compute strongly connected components;
   rerun with target, descendants and shared training material
   excluded where appropriate." Its execution was
   **adjudicated-but-blocked** in that record, for one stated
   reason: "the appendix does not contain the inference log or
   a complete derivation graph, and this adjudication must not
   fabricate it." Q3's twelve items were executed as basis
   notes on the named links only; the full-scope audit was
   left registered as a future study. This spec is that study.
2. The dependency record filed under Red Team Round 1 finding
   RT1-13
   (`specs/091-anchor-comparison-integrity/records/dependency-record-2026-11-21.md`):
   "No inference log exists. The program has no artefact that
   records, derivation by derivation, which readings were
   inferred from which others. It follows that neither the
   presence nor the absence of a closed cycle among the 94 is
   established." Its closure list is, verbatim in substance:
   (1) a commissioned inference-log build over the 94;
   (2) strongly-connected-component computation over that log;
   (3) dependency-aware reruns of every reading downstream of
   any cycle found. Items (1) and (2) are this package. Item
   (3) is not: a rerun is a separate commission, and this
   package's audit reports what removal of the dependent
   premises does to each basis under the class rules — it does
   not rescore any reading.
3. The M267 rerun record (Tranche 2 of the Q5 reruns,
   `specs/091-anchor-comparison-integrity/records/q5-reruns-tranche2-2026-11-21.md`)
   returned M267's slot-pattern claim NOT EXECUTABLE AS
   SPECIFIED, because its AGENT/TITLE slot labels derive from
   the same candidate system the claim is scored under; the
   standings supplement
   (`specs/091-anchor-comparison-integrity/records/standings-supplement-2026-11-21.md`,
   section 2) withdrew M267's enrichment figures as evidence
   and named what a retest requires (independently fixed slot
   labels, a pre-stated null, a selection correction). The
   retest is a separate commission; this package supplies its
   dependency statement (section 5).

## 1. What this spec is

Three deliverables, in dependency order:

- **The log** (Stage 1). For each of the 94 strict-core
  readings, its derivation as filed: the evidence items its
  filed basis cites, each item typed **(a)** primary evidence,
  **(b)** another reading or a construct of the candidate
  system used as evidence, or **ambiguous** where the filed
  basis does not settle the type. A tracked record in a
  documented machine-readable form (JSON) plus a
  human-readable rendering.
- **The Q3 graph audit** (Stage 2, this spec's first
  execution). From the log alone: remove all (b)-type items
  (other-readings-as-evidence), recompute what each reading's
  remaining basis supports under the adjudication's class
  rules, compute the strongly connected components of the
  (b)-graph, and file the result back into the Spec 091
  records as the Q3 audit's completion record — closing the
  adjudication's blocked unit. Any class change the audit
  implies is **reported, not executed**: standings move only
  through a further adjudication, which is not this package.
- **The M267 dependency statement** (Stage 2, in the same
  completion record). From the log: exactly which of M267's
  premises are (b)-type, and what a dependency-aware retest
  must hold fixed or exclude. The retest itself is not run.

## 2. The grounding, as measured at adoption

- The standings of record are the executed classes of the
  WS2 relabel execution
  (`specs/091-anchor-comparison-integrity/records/standings-relabel-execution-2026-11-21.md`):
  **5 E + 65 I + 4 R + 3 P + 17 U = 94**, with the M202
  addendum rule stated there in section 4. The log carries
  those classes; it does not re-derive them.
- The filed bases of record are the audit package appendix
  (`APPENDIX-94.md`, filed 2026-11-20 from the program's
  anchor-support audit and canonical anchor register, updated
  by the two corrected revalidation rounds), cross-checked
  against the frozen register snapshot
  (`glossa-corpus/indus/ANCHOR_STATUS_AUDIT.csv`) and the
  per-reading falsifiers annex
  (`specs/091-anchor-comparison-integrity/records/per-reading-falsifiers-2026-11-21.md`),
  whose rows name the evidence line each reading stands on.
- The dependency chains already named on the record (the
  dependency record, above) are the log's expected (b)-edge
  population, not its boundary: M005, M030, M068 → M342;
  M089 → M342, M176, M267; M037, M075 → M267; M347 → M342,
  M328, M367, M099; M374 → M328, M073; M375 → M342, M176;
  M398 → M267, M342; M267 → the AGENT/TITLE slot system,
  whose named markers include M176 and M328 (AGENT) and M099
  and M073 (TITLE) per the standings supplement section 2.
  The build verifies each of these against the filed basis
  text and logs what else the bases state.
- The audit's spot-check result, against which the full-scope
  audit is compared in the completion record: Q3's twelve
  items removed the interpreted-anchor premises on the named
  links and **no class changed**; the bases of the seventeen
  readings those items name were weakened (M347 and M375 with
  major arguments removed).

## 3. The log: sources, schema, typing rules

### 3.1 Sources of record

The build reads exactly three sources, pinned by SHA-256 in
the log's own provenance block at build time:

1. The appendix rows (the filed basis text per reading,
   verbatim, carried into the log as `basis_as_filed`).
2. The frozen register snapshot (sign, reading, evidence
   type, DEDR, source — cross-check only).
3. The falsifiers annex rows (the evidence line each reading
   stands on — cross-check only).

Where the three disagree on a checkable field, the build
records the disagreement on the entry; it does not pick a
winner silently. (One such disagreement is already on the
record: M007's basis cites DEDR 7 for its commodity claim
while its dictionary reference is DEDR 0340; both are logged.)

### 3.2 Schema

One entry per reading: `sign`, `reading` (as recorded),
`executed_class` (E / I / R / P / U, from the standings of
record), `q4_flag` (the source-diversity flag of record),
`basis_as_filed` (verbatim), `items`, `entry_notes`. One item
per distinct evidence element the filed basis states:
`id` (sign + ordinal), `kind`, `type` (`a`, `b`, or
`ambiguous`), `statement` (the item in the log's words),
`basis_span` (the verbatim clause of `basis_as_filed` the
item is extracted from — every item must cite one, and the
span must occur in the basis), `targets` (for (b) items: the
readings depended on, by sign id; empty where the basis names
none, with `target_note` then required), `reason` (required
for (b) and ambiguous items: why the basis text makes it so),
`status_note` (where a landed record annotates the item —
withdrawn as evidence, recorded FAILED, claim struck — the
annotation and its source).

Restatements of one observation inside a single basis (a
Round assignment and its UPGRADED-V18 restatement; a DEDR
entry cited in the basis and again as the row's dictionary
reference) are one item citing both spans' clauses in its
statement. Roll-up phrases that point at the row's other
items ("existing evidence", "plus existing evidence → HIGH")
are derivation steps, not items; where a basis carries one,
the entry notes it.

### 3.3 Item kinds and their types

| Kind | Type | What it is |
|---|---|---|
| `corpus_count` | a | A raw frequency or co-occurrence count, as a count |
| `positional_statistic` | a | A positional assignment or positional/bigram result (position, rate, pass/fail as filed) |
| `dictionary_entry` | a | A DEDR entry or a Proto-Dravidian lexical form cited from the dictionary tradition |
| `published_proposal` | a | A named published attribution or literature attestation (Parpola, Mahadevan, a named source) |
| `comparative_lexical` | a | A comparandum from another language family as a published lexical item (Munda, Elamite, Sanskrit forms as filed) |
| `motif_association` | a | A seal-motif association as filed (exclusivity, lift), as an observation |
| `iconographic_interpretation` | a | A sign-form interpretation (what the drawing depicts) |
| `crosswalk_identity` | a | A catalogue crosswalk identity — sign identity at most, never a value (adjudication Q2 point 3) |
| `corrected_validation` | a | A corrected battery or site-statistics outcome, as a later act of record |
| `literary_parallel` | a | A literary parallel as filed (Sangam name prefixes and the like) |
| `interpreted_anchor` | b | A collocate or neighbour premise whose force depends on the neighbour's interpreted value (HIGH-anchor collocates; interpreted neighbours inside a pattern) |
| `slot_label` | b | A slot-system construct: a grammar-slot model inference, a pattern scored against slot labels (AGENT/TITLE, NAME_AY_AN and kin), /su/-slot coverage, compound slot coherence, name-slot patterns |
| `self_assertion` | b | The candidate value itself counted as an input ("has specific PDR reading" — the adjudication's words: an input, not corroboration) |
| `internal_label` | b | A program-internal status label counted in the basis (a `verified` status, a staging promotion) |
| `consistency_score` | ambiguous | A computed score whose filed description does not state whether other readings' values enter it (SA-cons; grid-fit and expansion scores of the same family) |

Typing is by the basis text as read, not by kind alone where
the text says otherwise: a collocate clause filed as a bare
count is a `corpus_count`; the same collocation filed as a
HIGH-anchor premise is an `interpreted_anchor` — and where a
basis files both the count and the premise (the UPGRADED
rows), the log carries both items, exactly as the
adjudication's Q3 execution did (premise struck, count
retained as an unverified corpus observation).

### 3.4 Ambiguity rule

An item is `ambiguous` when the filed basis, read plainly,
does not settle whether it is primary evidence or a
candidate-system construct. The entry records the reason.
Ambiguity is a property of the filing, not a defect to be
repaired by inference: no ambiguous item is re-typed by the
build, by the audit, or by any later act that does not cite
new filed evidence. Two standing cases, named in advance so
the build cannot be accused of inventing them: the SA-cons
consistency scores (no filed definition states their inputs),
and any basis element truncated in the filing (a collocate
whose target the filed text cuts off is an `interpreted_anchor`
only where a target is named; the truncated remainder is
recorded as an ambiguous item stating the truncation).

## 4. The audit: removal, recomputation, components

The audit is a pure function of the log, the executed
standings it carries, and the class rules below (claim
C099-4). It reads no other source.

### 4.1 Removal

Primary treatment: remove every (b)-type item. Ambiguous
items are retained. Sensitivity treatment: remove (b) and
ambiguous items. Both treatments are computed for every
reading; the filed outcome is the primary treatment's, and
any reading whose outcome differs under the sensitivity
treatment is reported with both.

### 4.2 Class recomputation

Under the class definitions of the relabel execution record
and the reclassification form of its addendum (a reading is
reclassed on its remaining filed basis):

- **E** rests on external-support claims on file. Those claims
  are (a) items; their striking rule is the addendum's
  re-verification rule, already executed (M202). (b)-removal
  therefore cannot move an E reading's class. Outcome:
  unchanged; weakened if any item was removed under the
  treatment in question.
- **I** rests on internal candidate motivation. If, after
  the treatment's removal, at least one item remains, an
  internal motivation remains on the filed basis: unchanged,
  weakened if any item was removed (the losses named). Under
  the primary treatment an ambiguous item counts as remaining
  basis; under the sensitivity treatment it does not — which
  is what makes an ambiguous-only I reading diverge between
  the treatments. If no item remains after the treatment's
  removal, no internal motivation remains on the filed basis:
  **class would change to U** — reported, not executed.
- **R** and **P** are workflow states (a revalidation hold; a
  provisional pending state), not evidence classes; the
  adjudication's own Q3 items 10–12 removed credit under both
  without moving either. Outcome: unchanged; weakened if any
  item was removed under the treatment in question.
- **U** cannot fall further and cannot be promoted by a
  removal. Outcome: unchanged; weakened if any item was
  removed under the treatment in question.

Outcome vocabulary, exactly: **class unchanged** /
**basis weakened** (the removed items named) / **class would
change** (the destination class named). "Basis weakened" is
reported together with the class outcome (a reading is class
unchanged *and* basis weakened where both hold).

### 4.3 Components

Strongly connected components of the directed graph whose
edges are the (b) items with named in-register targets,
computed over all 94 nodes. The completion record states the
components of size greater than one and any self-loop, or
states that none exist. Edges whose targets the basis does
not name (section 3.4) are listed in the completion record as
open ends: the component result is a result over named-target
edges, and the record says so.

### 4.4 What the audit is not

The audit does not rescore any reading, rerun any battery, or
recompute any statistic. The dependency record's closure item
(3) — dependency-aware reruns downstream of any cycle — is
engaged only if the component computation finds a cycle, and
is in any case a separate commission. The audit's comparison
against the Q3 spot-check (section 2) is stated in the
completion record in the spot-check's own terms: class
changes (none, or the named exceptions) and the weakened set,
with the full-scope weakened count stated alongside the
Q3-comparable count (readings weakened by removal of
`interpreted_anchor` or `slot_label` items — the Q3 family).

## 5. The M267 dependency statement

M267's log entry is the statement's whole source. The
statement names: every (b) item in M267's entry, with its
kind and its named targets (the AGENT/TITLE slot markers of
record — M176 and M328 as AGENT markers, M099 and M073 as
TITLE markers, per the standings supplement section 2, which
names them as included markers, not as an exhaustive list);
which of M267's (a) items survive removal (the filed counts
and distribution, the dictionary entry); and what a
dependency-aware retest must therefore hold fixed or exclude
(independently fixed slot labels in place of the register's
own readings for every slot the pattern scores against; the
withdrawn enrichment figures not re-entered as inputs; a
pre-stated null and a selection correction, as the supplement
already requires). No retest is run, designed in executable
detail, or scheduled by this package.

## 6. Decisions

- **D-099-1 (number).** At the check of 2026-11-21 the
  highest landed package on origin/main was 098 and no 099
  directory, branch, or open pull request existed; this
  package takes 099. If a parallel package lands 099 first,
  this package renumbers under the Spec 097 precedent rather
  than colliding.
- **D-099-2 (registration performed in full, Spec 098
  pattern).** The claims are intaken into the canonical
  ledger in this package's own landing pull request through
  the bundle-import route (C099-1..C099-8 appended,
  2026-11-21), with the taxonomy entry added, the settling
  chain refreshed in the standing order, the generated layers
  regenerated, and every census pin the intake moves updated
  in the same pull request. The full account is in
  `records/adoption-and-registration-2026-11-21.md`.
- **D-099-3 (the audit reports; it does not move).** Any
  class change the Stage 2 audit implies is reported for a
  further adjudication. No record of this package alters a
  standing, an anchor, or the register.
- **D-099-4 (venue).** All execution runs on tower-compute,
  in fresh clones under `~/glossa-work/`, never in the
  coordination VM and never on the mini-server (which serves
  only). Every run's verdict is its payload verdict, never a
  wrapper state.

## 7. Test cases

Three test cases exercise this package's requirements; all
are implemented in `tests/` against the reference
implementation in `tools/inference_log.py`, executed on
tower-compute, with payload verdicts recorded in
`records/tc-execution-2026-11-21.md`. At adoption they run on
fixtures; the same implementations run over the real log and
the real filed bases at Stage 1, and over the real log at
Stage 2, with those verdicts recorded in the stage records.

- **TC-099-01 — Schema validation.** The validator accepts a
  conforming fixture log covering all five classes, an
  ambiguous item, and an unnamed-target (b) item; it rejects
  a log with a (b) item carrying no reason, an item whose
  `basis_span` does not occur in its entry's basis, a
  duplicate sign, and a class outside the vocabulary. At
  Stage 1 the same validator runs over all 94 rows of the
  real log.
- **TC-099-02 — Completeness of extraction.** On fixture
  basis rows planting one element of each checkable family
  (a DEDR citation, a collocate premise with its count, a
  slot pattern, a consistency score, a motif clause, a
  truncated clause), the checker confirms a correct fixture
  log covers every planted element exactly and cites only
  spans the basis contains; it fails a log with one element
  deleted and a log with one invented span. At Stage 1 the
  same checker runs over the real filed bases against the
  real log.
- **TC-099-03 — Audit determinism.** On a fixture log
  planting a weakened E, a would-change I (no (a) item under
  removal), a weakened I, an ambiguous-only I (primary and
  sensitivity outcomes differ), and a two-node cycle, an
  independent implementation of section 4 written inside the
  test reproduces the reference implementation's per-reading
  outcomes and component list exactly.
