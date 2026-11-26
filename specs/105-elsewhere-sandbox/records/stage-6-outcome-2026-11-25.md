# Stage 6 outcome — Spec 105: L6, the boundary gates (2026-11-25)

Stage 6 of Spec 105 was registered by record under
spec.md section 8 on 2026-11-25
(`records/stage-6-registration-2026-11-25.md`, committed
before any gate ran — registration commit `199069df`
precedes the execution commit in the landing branch's
history) and executed the same day under the owner's
keep-working directive (RCPH chat, 2026-11-25 19:07 ET,
naming glossa-lab expressly; see the registration's
section 1). Execution ran on tower-compute from custody
datasets whose SHA-256 hashes were re-verified before
use and matched the filed pins exactly (derivation
`84476daa…`, reserve `bfbe79cb…`, Eteocypriot
`2799d103…`, Meroitic `a8f551e5…`), and Spec 096's
corpus bytes, the G-ETE checker's provenance, re-hashed
to the registered value (`2954283d…`). The filed run is
`records/stage-6-execution.py` over the filed Stage 1–5
outputs, written to `records/stage-6-output-2026-11-25.json`.
Each gate ran under two independent checker
implementations (registration section 6): A, a Python
checker over the filed lower-rung outputs; B, a jq event
stream over the datasets' raw bytes through sort and
uniq -c with awk assemblies, sharing no code with A,
re-deriving the sandbox-side structures it checks and
applying its own copy of the outside tables. One defect
in implementation B was caught by the agreement check
during the run and fixed before the filed run: B's
Meroitic stream read the dataset's groups as raw
strings where the build stores them as mark lists, so
its first G-MER table carried the JSON text's own
characters and no positional classes; the disagreement
stopped G-MER in that run exactly as registered, B was
corrected to join each group before classification, and
the stage was re-executed in full. The filed run is the
corrected script's run; its G-IND figures are identical
to the stopped run's (the G-IND checker was untouched by
the defect), and the reserve was opened in both runs
only by the G-IND checker, only after the registration
guard passed (below). A and the filed tables were never
in question.

## 1. G-ETE — GOOD, GOOD

The checker stood outside the sandbox on Spec 096's
filed signary frame and token conventions and the Common
syllabary value table enumerated in the registration
(section 2). The mark `?` is exempt (it asserts no
value); `[sa]` is checked at the value sa; the sandbox
itself received nothing.

- **ETE-1 (L1, inventory against the signary): GOOD.**
  All 35 derived marks were checked: 1 exempt (`?`), 34
  carrying values, and every one of the 34 values is in
  the 59-value Common syllabary table; none out of
  table. GOOD licenses only this: the assumption-free
  derivation's inventory contains no mark that is not a
  sign of the independently known syllabary.
- **ETE-2 (L4–L5, no merger of distinct known values):
  GOOD.** All 70 filed classes were checked — the 35 L4
  joint substitution classes and the 35 L5 role-identity
  classes — and every class is value-homogeneous; no
  class merges two distinct known values. GOOD licenses
  only this: the derived class and role structure
  nowhere collapses two independently known distinct
  signs into one structural unit.

TC-105-20 PASS: the two implementations' per-mark and
per-class verdict tables are identical, and each word is
the table's mechanical consequence.

## 2. G-MER — GOOD, GOOD, GOOD

The checker stood outside the sandbox on the pinned
build's own transliteration map (the values of the very
convention the sandbox's source is written in, as that
build files them; registration section 2).

- **MER-1 (L1, inventory against the known signs):
  GOOD.** All 32 derived marks are accounted: the 21
  letter characters each name one of the 23 signs of
  the map's table (the te and to signs are written in
  this convention as t+e and t+o sequences, so no
  single character names them), the 10 digits are the
  numeral signs, and `.` is the lacuna. None
  unaccounted. GOOD licenses only this: the derivation's
  inventory contains no mark outside the independently
  known signs and recorded categories of the script.
- **MER-2 (L3, the a sign's position): GOOD.** Outside
  fact: the a sign is used only word-initially. Of its
  737 filed occurrences, 725 are group-initial or sole
  — 98.4% conformance against the registered 95%
  close-or-similar tolerance (D-105-26); 12 occurrences
  (11 medial, 1 final) do not conform, and they are on
  the record here and in the raw output.
- **MER-3 (L3, the i sign's position): GOOD.** Outside
  fact: initial /i/ is written `yi`, so the i sign does
  not stand word-initially. Of its 2,880 filed
  occurrences, 2,857 are neither group-initial nor sole
  — 99.2% conformance against the same registered
  tolerance; 23 occurrences (20 initial, 3 sole) do not
  conform, on the record as above.

TC-105-21 PASS: the two implementations' tables are
identical, including the positional counts B re-derived
from the Meroitic streams, which equal the filed L3
positional rows for `a` and `i` exactly.

## 3. G-IND — GOOD

The registration guard passed before any unsealing:
this stage's registration file stood tracked and
unmodified in the clone's git index when the checker
ran, and the branch history shows the registration
commit preceding the execution commit. The checker then
unsealed the reserve and scored every token of every
reserve artifact: 334 artifacts, 1,391 tokens, in
recorded order. The reserve's SHA-256 as sealed and as
scored are identical (`bfbe79cb…`): the scored bytes are
the sealed bytes.

The derived predictor (registration section 5, frozen
before unsealing) scored the reserve by its filed rules:
595 tokens by the attested-pair rule, 334 by the
group-initial rule (exactly one per artifact), 436 by
unigram backoff, and 26 by the unseen-mark rule. The
baseline scored 1,365 tokens by the filed unigram and
the same 26 unseen tokens at the same frozen ε =
1/5,983, so the unseen tokens — 26 of 1,391, carrying
marks among the 18 reserve-only marks — contributed the
identical log-loss to both models and could not decide
the gate. The agreed scoring case table (265 distinct
cases) is filed in the raw output.

- Baseline mean per-token log-loss: **4.557943** nats.
- Derived mean per-token log-loss: **4.178289** nats.
- Difference: **0.379654** nats per token, against the
  frozen margin of **0.05**.
- **IND-1: GOOD** — the derived system beats its own L2
  unigram baseline by more than the frozen margin.

GOOD on G-IND licenses only this (registration section
5): the derived Indus system, as filed at L4–L5,
predicts the withheld recorded streams better than the
sandbox's own L2 unigram baseline by the frozen margin,
on this reserve, under the frozen unseen-mark rule. It
is not a decipherment claim, it assigns no value or
meaning to any mark, and it moves no standing, verdict,
or tally (C105-5). TC-105-22 PASS (identical case tables
and six-decimal figures from both implementations; the
word is their mechanical consequence). TC-105-23 PASS
(registration order as above; both reserve hashes as
stated; the run's opened-paths audit is filed in the
raw output — the derivation, Eteocypriot, and Meroitic
datasets read by the checkers, the reserve's content
read by the G-IND checker alone, after the guard).

## 4. Test cases

- TC-105-20 (G-ETE agreement and execution): **PASS** —
  section 1.
- TC-105-21 (G-MER agreement and execution): **PASS** —
  section 2 (after the disclosed implementation-B
  correction; the stopped first run is part of this
  record, not smoothed over).
- TC-105-22 (G-IND agreement and execution): **PASS** —
  section 3.
- TC-105-23 (registration before unsealing, and the
  seal): **PASS** — section 3.
- TC-105-24 (standing discipline at Stage 6): executed
  at pull-request time over the landing diff; its result
  is recorded in the landing's pull request and in
  PROGRAM-STATE, as in Stages 1–5.

## 5. What Stage 6 establishes, and what it does not

The ladder's three registered contact points are
discharged, each at exactly its registered license. The
Eteocypriot derivation's inventory and class structure
are consistent with the independently known Cypriot
syllabary at the comparisons checked (ETE-1, ETE-2). The
Meroitic derivation's inventory is fully accounted by
the known signs and recorded categories, and its order
structure places the a and i signs consistently, at the
registered tolerance, with those signs' independently
known positional restrictions (MER-1, MER-2, MER-3). The
Indus derived system predicts its sealed reserve better
than the sandbox's own unigram baseline by 0.379654
nats per token against a frozen 0.05 margin (IND-1).
Nothing further follows. No gate outcome assigns a
phonetic value, a gloss, a translation, or a semantic
category to any mark in any sandbox; no outcome is a
decipherment claim; no outcome crosses between
sandboxes (C105-4); and no anchor standing, program
verdict, or tally moves (C105-5). The Indus reserve's
seal (C105-4) is spent as registered: it was kept
through every derivation rung and opened once, by the
registered checker, under the frozen rule and margin —
the claim stands, its seal clause discharged by the act
it was written to govern.

With Stage 6 the study's registered design is complete:
the ladder L0–L5 derived in all three sandboxes, and the
L6 boundary gates run as registered. The study stands
open only to a later registration amending the spec
under section 8; nothing above L6 was ever registered,
and no gate outcome licenses one.

## Round J addendum (2026-11-25) — G-ETE source conformance and the ETE-2 certificate

Appended at the landing of the Round J Co-scientist
adjudication (PR for
`records/coscientist-sweep-adjudication-2026-11-25-round-j.md`
in the Spec 091 package, §2). Nothing above is altered: the
registered table, the filed script, and the historical gate
output stand as executed. This addendum records two
findings of the Eteocypriot session (units J-E-1 and J-E-2),
both sustained at adjudication on the filed record.

**J-E-1 — the G-ETE reference table's provenance is
unresolved.** The Stage 6 registration (§2) describes the
Common syllabary value table applied by the G-ETE checker
as the sign values of the frame "as settled by the Idalion
bilingual and carried in the edition of record's signary
(Masson, *Les inscriptions chypriotes syllabiques*)", and
enumerates 59 values including `ye`, `ze`, `zi`, `xi`, `xo`
and nowhere `yo`. Two checked Common-syllabary references
differ from that enumeration in exactly six values: the
CREWS project Common-syllabary worksheet (Y row ya/yo, Z
row za/zo, X row xa/xe, the five registered-only cells
blank) and the Unicode Cypriot Syllabary chart (55 encoded
syllables; JA/JO, ZA/ZO, XA/XE) — registered-only `ye`,
`ze`, `zi`, `xi`, `xo`; reference-only `yo`. No passage
supporting the exact 59-value enumeration, with a checkable
location and transliteration mapping, is on file in this
package or was produced at adjudication; the attribution
therefore stands UNRESOLVED as filed, and is not filled in
by assertion. Input impact, verified at adjudication from
the filed Stage 6 output: the ETE-1 table carries 33
distinct observed values, none of them in the set
difference, so the observed inventory returns GOOD under
the checked reference repertoire as well, and ETE-1's word
is unaffected under either table. Any corrected checker
execution follows its own registration under spec.md §8;
the registered table is not silently replaced.

**J-E-2 — ETE-2's zero-opportunity certificate.** ETE-2
returned GOOD under its registered non-merger rule. All 70
checked classes are singletons (the 35 L4 joint classes and
the 35 L5 identity classes, recomputed from the filed
Stage 4 and Stage 5 outputs at adjudication; exactly one
class in each partition contains the exempt mark `?`),
leaving zero within-class pairs of value-carrying marks;
homogeneity is therefore guaranteed by the partitions and
supplies no nontrivial external corroboration of a class
merger or class-discovery ability. The registered word,
counts, and historical tables are retained unchanged. The
same qualification is noted at the Spec 105
seed-and-iteration log's Iteration 6 entry.

---

## Round N addendum (2026-11-26) — G-IND conformance annotation (unit N-I-1) and execution chronology (unit N-I-2)

Appended at the landing of the Round N adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-26-round-n.md`
§§2.1–2.2). Nothing above is altered: the registration,
the filed script, the raw output, the figures, and the
historical gate words stand exactly as filed.

### N-I-1 — Conformance annotation: the G-IND scoring weights are not normalized probabilities

Round N's Indus session demonstrated from the filed
Stage 2 and Stage 3 tables and the filed execution script
that the G-IND next-token weights do not sum to one. For a
predecessor x with attested successor set S(x), the
registered pair weights c(x,m)/c(x,*) already sum to 1
over S(x); the rule then adds positive unigram weights
c(m)/5611 for every known mark outside S(x), without
discounting the attested successors and without any row
normalizer before the logarithms. Exact witnesses from the
filed tables (mass over the 372 derivation marks): group
start 1 + 853/5611 = 1.152023; after M342,
1 + 1567/5611 = 1.279273; after M176,
1 + 1612/5611 = 1.287293. Both checker implementations
implement the same registered construction; their agreement
verifies agreement on these weights, not their validity as
probabilities.

What stands: recomputation from the filed case table
reproduces baseline 4.557943, derived 4.178289, difference
0.379654 against the frozen 0.05 margin. The historical
GOOD on G-IND is the correct mechanical consequence of the
frozen scoring rule and is retained. What is withdrawn:
the interpretation of that difference as an advantage of
0.379654 nats per token in normalized predictive log-loss.
The result is to be cited as a comparison of the frozen
unnormalized scoring rules as registered. A normalized
predictive log-loss advantage is NOT established, and no
corrected verdict is asserted here: the aggregate case
table discards the predecessor identities a row-normalized
replay would need, and any normalized correction is a
separate act requiring its own registration, with no
tuning to recover GOOD.

Citation surfaces: this annotation is the qualification of
record for IND-1 wherever it is cited forward. The Round J
assessment's acceptance of IND-1 GOOD (§1 of
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25-round-j.md`)
was a brief-level assessment, not an independent
normalization check, and carries this qualification by the
dated note appended to that record at this landing. The
ELSEWHERE methods paper (Zenodo record 24571025, DOI
10.5281/zenodo.24571025, deposited 2026-11-26) states the
gate figures at their registered license; this annotation
is the qualification of record for future citation of
those figures.

Advance kill check, run at adjudication and not met: the
finding falls if the filed scoring path contains a
normalizer actually applied before every logarithm, or a
disjoint sample-space construction under which the
next-token rows sum to one. Neither is present in the
inspected registration or code, and the explicit mass sums
above contradict normalization directly.

### N-I-2 — Execution chronology: "opened once" and the two full scoring executions

This record's opening account states that the stage was
re-executed in full after implementation B's G-MER defect
was caught, that the filed run is the corrected script's
run, and that "the reserve was opened in both runs only by
the G-IND checker, only after the registration guard
passed". Section 5 states that the reserve "was kept
through every derivation rung and opened once, by the
registered checker, under the frozen rule and margin". The
two passages use "opened" at different units; this
chronology fixes the distinction on the record:

(a) First release/disclosure: one. The reserve's contents
were first disclosed to a checker in the stopped run,
after the registration guard passed. Nothing about the
reserve was available to any derivation rung (Stages 1–5)
before that moment, and the seal clause's purpose — no
exposure before the frozen rule and margin were fixed —
was met at that single first disclosure.

(b) Checker invocations / content reads: two full scoring
executions read the reserve — the stopped run and the
corrected filed run — each only through the G-IND checker
(implementations A and B), each after the guard passed.
The second execution changed no input, no rule, and no
margin: the only correction was to implementation B's
Meroitic stream read (the G-MER defect), and the G-IND
figures of the two runs are identical, as recorded above.

(c) The replay after the G-MER repair is therefore an
unchanged re-scoring after a first disclosure, not a
second holdout and not adaptive re-testing: no quantity
was tuned against the reserve between the runs.

What remains unresolved, recorded rather than settled by
assertion: no provision of the Stage 6 registration
expressly governs an unchanged replay after first
disclosure; the registration's single-unsealing language
and TC-105-23 are written at the unit of first disclosure.
Whether a future registration should expressly permit or
forbid such replays is a prospective registration question,
not decided here. No first-run log is recreated by this
addendum; the stopped run's outputs were not separately
filed, and this chronology rests on the execution account
already in this record. Nothing in this chronology alleges
changed data, adaptive tuning, or a second fresh reserve,
and the historical GOOD is unaffected by it.

