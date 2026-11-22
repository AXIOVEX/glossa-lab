# M267 dependency-aware retest — 2026-11-22

**Spec:** 091 (anchor comparison integrity), filed beside the
governing record. **Commission:** the F-4 study package,
commissioned by the owner in chat 2026-11-22. **Governing
record:** the M267 dependency statement in
`q3-graph-audit-completion-2026-11-21.md` (Spec 099's Q3 graph
audit), which set the conditions this retest runs under and
reserved the retest to a separate commission. This record is
that commission's result. **Execution venue:** tower-compute
(fresh clone `~/glossa-work/f4-package` at origin/main
`6bcd95eb`). All computations run over filed records in the
repository; no new corpus was staged and no substitute corpus
was used.

## 1. The conditions, as the dependency statement set them

M267's basis carries exactly one (b)-type premise: the slot
label [AGENT]-M267-[TITLE] (M267-05), whose AGENT markers are
M176 and M328 and whose TITLE markers are M099 and M073, and
one ambiguous premise (M267-04, the Phase-64 score, whose
inputs are unstated and which is unusable until they are). The
statement's condition: the slot-pattern statistic may not be
used as confirmation of the genitive reading unless the
markers' readings are independently justified first, or the
pattern is recomputed over uninterpreted sign positions only.
The withdrawn figures (Phase-74's 4.3x enrichment and
z = 8.038) stay withdrawn and were not used as inputs anywhere
in this retest. The surviving (a) inputs are the raw corpus
counts (freq = 400, with the Holdat custody caveat: the corpus
is unheld, and no written Miller permission is on file), DEDR
494, and the standing raw pattern counts (26 observed against
a permutation null mean of 6).

## 2. Route (a): the markers' readings are not independently justified

The current standings of the Phase-74 battery's marker sets
(standings of record after the Spec 098/099 executions):

- AGENT set {M059, M176, M305, M328, M336}: all five stand at
  class **U** — no basis outside raw patterning.
- TITLE set {M030, M041, M073, M099, M211}: M030, M041, M073
  and M099 stand at class **I** — internally motivated
  candidates whose support is not demonstrated; M211 is
  outside the 94-reading population and carries no class.

No marker's reading is independently justified: the AGENT
markers stand at the lowest class, and the TITLE markers'
class I is by definition not independent justification.
Route (a) is therefore closed on the record, and the
slot-pattern statistic (26 / 67 / 79 / 228) is **excluded as
confirmation** in this retest, exactly as the dependency
statement directs. It is examined below only for internal
consistency, as a filed count.

## 3. Route (b): what the surviving evidence supports

### 3.1 The raw counts stand as filed

freq = 400 is filed identically in four independent records:
the Phase-74 output, the Phase-64 output (n = 400), the
Phase-142 collocate record (freq 400), and the anchors file.
The filed 2x2 (both 26, agent-before-only 67, title-after-only
79, neither 228) sums to exactly 400. Its marginals
cross-check against the filed neighbour lists, which agree
exactly between the Phase-74 and Phase-142 records on every
shared entry: tokens with a left neighbour in the AGENT set
total 93, of which the top-neighbour lists account for
M328 40 + M059 30 + M176 17 = 87, leaving 6 for M305 + M336
combined (both below the filed top lists' cutoffs, as
expected); tokens with a right neighbour in the TITLE set
total 105, which is exactly M099 84 + M211 21 — from which it
follows, on the filed counts, that the other three TITLE
markers (M073, M030, M041) never follow M267 at all. The
"title-after" cell of the filed statistic is carried entirely
by two of its five markers. The raw counts stand as filed;
the statistic built on them remains excluded as confirmation
under section 2.

### 3.2 The uninterpreted recompute

Recomputing the pattern over uninterpreted sign positions
only (whether an M267 token has any left neighbour, any right
neighbour, both, or neither) from the two filed slot
computations over the same population:

| | Phase-64 partition | Phase-142 partition |
|---|---|---|
| both neighbours (flanked) | 314 | 324 |
| left only (terminal position) | 63 | 59 |
| right only (initial position) | 23 | 17 |
| neither (single-sign text) | 0 | 0 |
| total | 400 | 400 |

(Phase-64 files rates 0.058 / 0.158 / 0.785 at n = 400, whose
unique integer solution is 23 / 63 / 314; Phase-142 files the
counts 17 / 59 / 324 directly. The two filed computations
differ in their position conventions — a definitional
divergence between two filed records, which this retest
reports rather than silently resolving.)

What this establishes, under either computation: M267 is
flanked on both sides in roughly four-fifths of its tokens
(78.5% or 81.0%) and never occurs as a single-sign text. That
is a positional fact about the sign, consistent with a medial
grammatical particle. It does not discriminate the genitive
from the many other functions a medial particle can carry,
and it is the strongest statement the uninterpreted evidence
supports.

### 3.3 The null is not recomputed — the gap, named

The within-inscription permutation null behind the filed
"null mean 6" cannot be recomputed on this venue: it requires
the pinned raw corpus (`corpora/downloads/external_repos/
holdatllc_indus/indus_corpus 2.csv`, pinned SHA-256
`62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`),
which is not held on tower-compute — the only files of that
name on the venue are 8-line synthetic test fixtures in
archive test directories, and no staged copy survives in any
clone. Tranche 1 recorded the same limitation and worked from
corpus-derived records; this retest does the same and issues
**no new significance figure**. The filed null mean of 6
stands as filed (a truncated permutation mean; its spread was
never filed — tranche 2's finding), and the withdrawn
z = 8.038 is not revived in any form.

### 3.4 The DEDR 494 leg does not verify as filed

The anchors file's M267 basis cites "DEDR 494 (in locative)".
The F-4 DEDR digital-edition pass (filed beside this record,
`dedr-digital-edition-pass-2026-11-22.md`) establishes from
the dictionary's own digital edition (DSAL) and the restored
tree alike that entry 494 (print p. 48) is Ta. il "house,
home, place, wife", and that *in* is not a DEDR headword at
all. The DEDR leg as filed therefore does not match its named
source in either edition. This retest reports the finding as
evidence; it draws no standing consequence from it — that is
a separate adjudication, as the commission directs.

### 3.5 Excluded inputs

The Phase-64 score (M267-04, ambiguous) is excluded: its
inputs are unstated. The Phase-74 enrichment (4.3x) and
z = 8.038 are excluded: withdrawn, and their computation
depended on the same positional machinery the dependency
statement impugns.

## 4. Verdict, in the frozen vocabulary of the original battery

The Phase-74 battery's frozen verdict vocabulary is:
GENITIVE_CONFIRMED if p < 0.05 and the observed rate exceeds
0.10; GENITIVE_MARGINAL if p < 0.10; otherwise
UNCERTAIN_CONFIRMED; with promotion requiring the CONFIRMED
conditions.

**Verdict: GENITIVE_MARGINAL — not promoted** (the original
run's own filed verdict and promotion state, reached again
under the dependency conditions, on weaker and cleaner
grounds).

The reasoning, in order. (i) The confirmation arm is disabled:
the slot-pattern statistic is excluded (section 2), so no
p-value from it can carry a CONFIRMED verdict, and the
recomputed uninterpreted pattern (section 3.2) yields no
p-value at all on the evidence held. (ii) The battery's own
promotion rule could never have been met by the filed run in
any case: the observed rate is 26 / 400 = 6.5%, below the
battery's 10% bar, so even had the slot statistic been
admissible, the outcome is MARGINAL, not CONFIRMED — the
original run's "not promoted" was correct under its own
rules. (iii) What survives — a sign of frequency 400, flanked
in roughly four-fifths of its tokens, never standing alone —
is suggestive of a medial grammatical function and consistent
with the genitive among others. Suggestive and not conclusive
is exactly what the battery's MARGINAL tier names.

## 5. What this record does not do

It changes no standing: M267's class is untouched, and the
consequences, if any, of the DEDR 494 finding (section 3.4)
and of this verdict for the anchors file's M267 basis (which
still cites the withdrawn z and the unverified DEDR leg) are
for separate adjudication. It does not restore the withdrawn
figures, does not recompute the permutation null, and does
not substitute another corpus for the unheld Holdat file
(the in-repo research export is a different population and
was not used).

**Payload verdict: the retest was executed under the
dependency statement's conditions on the evidence held;
verdict GENITIVE_MARGINAL, not promoted; the from-raw
permutation arm was not executable and its gap is named in
section 3.3.**
