# Stage 6 registration — Spec 105 (the ELSEWHERE sandbox), 2026-11-25

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
executed, and Stages 3, 4, and 5 were commissioned and
executed under the directive itself earlier the same
evening. The Stage 6 commission for this study is issued
under that directive.

This record registers Stage 6 of Spec 105 under spec.md
section 8: later stages execute only under their own
registrations amending this spec. It is committed before
any gate runs; the landing's git history is the proof of
that order, and for G-IND it is the proof that the
unseen-mark rule and the margin of section 5 were frozen
before the reserve was unsealed. Stage 6 executes
exactly one ladder rung, L6 (spec.md sections 5 and 7):
the three boundary gates — G-ETE and G-MER (validation)
and G-IND (prediction) — each run by a checker standing
outside its sandbox, returning exactly one word per
registered comparison, GOOD or NOT-GOOD (spec.md section
7). The sandbox receives nothing else: no values, no
corrections, no hints. Not commissioned by this act, and
not executed in this stage: any new derivation rung
(none stands above L6 in the registered ladder); any
unsealing of Spec 096's held-out inscriptions (they are
read by no part of this study, at this stage or any
other); any use of a gate outcome beyond the license of
section 7 of this record. No claim in this study carries
a result by this registration, and nothing in this stage
moves any anchor standing, verdict, or tally in any
program (C105-5). No recommendations-ledger row is
opened (D-105-3, the standing pattern for this study).

## 2. The checkers and their outside material

A gate's checker stands outside the sandbox (spec.md
section 7). The checker may see outside material; the
sandbox never does; and no outside material enters any
sandbox dataset or derivation — the checkers of this
stage read the filed sandbox outputs and the outside
material named here, and return their words. The outside
material is fixed by this section; a comparison that
needed any other outside material would not be a
registered comparison of this stage, and none is run.

**G-ETE outside material.** (i) The signary frame and
transliteration scheme filed in Spec 096's corpus
(`specs/096-eteocypriot-program/corpus/corpus.json`,
SHA-256 of the recorded bytes
`2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597`):
the frame is the Common syllabary, and the token
conventions are: a plain token is a legible sign; `[x]`
is a sign restored by the edition; `?` is a damaged or
illegible sign whose value the edition of record does
not read. (ii) The Common syllabary value table: the
checker's list of the sign values of that frame, as
settled by the Idalion bilingual and carried in the
edition of record's signary (Masson, *Les inscriptions
chypriotes syllabiques*), enumerated here in full so the
table the checker applies is itself on the record — the
five vowels `a e i o u`; the consonant series `ka ke ki
ko ku`, `la le li lo lu`, `ma me mi mo mu`, `na ne ni no
nu`, `pa pe pi po pu`, `ra re ri ro ru`, `sa se si so
su`, `ta te ti to tu`; and `wa we wi wo`, `ya ye`, `za ze
zi zo`, `xa xe xi xo` — 59 values.

**G-MER outside material.** The pinned source build's
own transliteration map (`data/transliteration_map.md`
of the Kovetsky build at pin
`145af0836c071e7c9796d37d4b36add00d347c8a`, the build
whose `inscriptions.jsonl`, SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`,
is this sandbox's source): its section 2 files the 23
Meroitic signs with their values (Rilly & de Voogt 2012,
Table 1.1; Rilly 2016; Rilly 2022) and the ASCII
convention of the corpus files, and its section 1 states
the test-corpus conversion under which the build's texts
stand (Millet's `E` read as `o`; uncertain-reading
capitals lowercased; `S`, `X`, `x`, `N` kept). Read under
that conversion, the build's letter characters name
signs as follows — `a` the a sign, `e` the e sign, `i`
the i sign, `o` the o sign, `y` the y sign, `w` the w
sign, `b` the b sign, `p` the p sign, `m` the m sign,
`n` the n sign, `N` the ne sign, `r` the r sign, `l` the
l sign, `x` the ḫ sign, `X` the ẖ sign, `S` the s sign,
`s` the se sign, `k` the k sign, `q` the q sign, `t` the
t sign, `d` the d sign (21 characters; the te and to
signs are written in this convention as the character
sequences t+e and t+o, per the map's section 4.4, so no
single character names them). The map's section 3 files
the remaining recorded categories: the digits are the
Meroitic numeral signs, and `.` is a lost or illegible
sign (a lacuna), which asserts no sound value. The map's
section 2 also files the two positional facts this gate
checks: the a sign is used only word-initially (its note
to sign 1: "Only word-initially"), and initial /i/ is
written `yi`, with a dummy y (its note to sign 3), so
the i sign does not stand word-initially.

**G-IND outside material.** None beyond the reserve
itself: the gate's checker unseals the reserve under
section 5 and scores the filed derived system against
the filed baseline on it. The reserve dataset stands in
custody at
`~/.syncyard/worktrees/glossa/glossa-custody/spec105/indus-reserve.json`
on tower-compute, sealed since build by its filed
SHA-256
`bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff`.

**Sandbox-side inputs.** The gates read the filed
outputs of the lower rungs, as landed: the Stage 1
derived inventories (`records/stage-1-output-2026-11-25.json`),
the Stage 2 frequency table and the Indus unigram
baseline (`records/stage-2-output-2026-11-25.json`;
`records/stage-2-indus-unigram-baseline-2026-11-25.json`),
the Stage 3 pair and positional tables
(`records/stage-3-output-2026-11-25.json`), the Stage 4
class tables (`records/stage-4-output-2026-11-25.json`),
and the Stage 5 role tables
(`records/stage-5-output-2026-11-25.json`), all as
landed at the Stage 5 merge (`d8ece15f`). The datasets
stand in custody at
`~/.syncyard/worktrees/glossa/glossa-custody/spec105/`
on tower-compute. Dataset SHA-256, as filed at Stage 1
and re-verified before any gate reads them:

- Indus derivation set: indus-derivation.json,
  84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b
- Eteocypriot: eteocypriot.json,
  2799d1034e8af50a110e7df69d6f79ab931cbc13db480ebbc8d4dfcf589421fe
- Meroitic: meroitic.json,
  a8f551e5cc5264decbc2c01d7ee924740245ce8cbeca6b4b7f776e88a3920fb7
- Indus reserve (sealed; hashed at this stage and
  opened only by the G-IND checker, only after this
  registration is committed — section 5): indus-reserve.json,
  bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff

## 3. G-ETE — the comparisons (frozen by this record)

The checker applies the token conventions of section 2
to each derived mark: a plain mark's value is the mark
itself; a bracketed mark `[x]` carries the value x (the
brackets are the edition's restoration marks, outside
knowledge the checker holds; inside the sandbox `[sa]`
and `sa` remain different marks, P-1, and nothing in
this gate changes that); the mark `?` asserts no value
and is **exempt** — it takes part in no comparison of
this gate, and its exemption is itself filed in the
gate's output so the exempt count is on the record.

- **ETE-1 — inventory against the signary (L1).** Every
  non-exempt mark of the derived L1 inventory carries a
  value in the Common syllabary value table of section
  2. **GOOD** iff every non-exempt derived mark's value
  is in the table; otherwise **NOT-GOOD**, with the
  offending marks named in the gate's output. GOOD on
  ETE-1 licenses only this: the assumption-free
  derivation's inventory contains no mark that is not a
  sign of the independently known syllabary — structure
  consistent with what is independently known, at the
  inventory rung. It licenses no reading of any mark
  and no claim about the language.
- **ETE-2 — no merger of distinct known values (L4–L5).**
  No joint substitution class of the filed L4 output
  and no role-identity class of the filed L5 output
  contains two marks whose values (under the same
  conventions, exempt marks taking no part) are
  distinct. **GOOD** iff every filed class of both
  partitions is value-homogeneous; otherwise
  **NOT-GOOD**, with the offending classes named. This
  comparison is exact: it has no tolerance, because a
  class either identifies two differently-valued signs
  or it does not. GOOD on ETE-2 licenses only this: the
  derived class and role structure nowhere collapses
  two independently known distinct signs into one
  structural unit.

## 4. G-MER — the comparisons (frozen by this record)

The checker applies the character table of section 2 to
each derived mark. A mark is **accounted** iff it is a
letter character naming one of the 23 signs, or a digit
(a numeral sign), or `.` (the lacuna, asserting no sound
value). The positional comparisons read the filed L3
positional table; a mark's group is the recorded unit
the build's spaces delimit (the map's section 2: the
word divider stands as a space in the corpus), and an
occurrence's position is its filed L3 class (sole /
initial / final / medial). Both positional comparisons
carry the tolerance of decision D-105-26: conformance
of at least 95 in every 100 occurrences (19 in 20), the
close-or-similar standard spec.md section 7 provides
for first gates, fixed here before the checker runs and
applied identically to both comparisons; the gate's
output files the exact conforming and non-conforming
counts either way, so the margin is on the record.

- **MER-1 — inventory against the known signs (L1).**
  Every mark of the derived L1 inventory is accounted
  under the character table. **GOOD** iff all 32 derived
  marks are accounted; otherwise **NOT-GOOD**, with the
  unaccounted marks named. GOOD on MER-1 licenses only
  this: the assumption-free derivation's inventory
  contains no mark outside the independently known
  signs and recorded categories of the script.
- **MER-2 — the a sign's position (L3).** Outside fact:
  the a sign is used only word-initially (section 2).
  **GOOD** iff at least 95% of the mark `a`'s filed
  occurrences are group-initial or sole; otherwise
  **NOT-GOOD**. GOOD on MER-2 licenses only this: the
  derived order structure's placement of the a sign is
  consistent, at the registered tolerance, with the
  sign's independently known positional restriction.
- **MER-3 — the i sign's position (L3).** Outside fact:
  initial /i/ is written `yi` (section 2), so the i sign
  does not stand word-initially. **GOOD** iff at least
  95% of the mark `i`'s filed occurrences are neither
  group-initial nor sole; otherwise **NOT-GOOD**. GOOD
  on MER-3 licenses only the corresponding statement
  for the i sign.

## 5. G-IND — the prediction gate (frozen by this record)

**The derived system (the predictor).** The system the
gate tests is the derived Indus system at L4–L5, whose
predictive content is the ladder's filed structure over
the derivation set: the L2 frequency table (counts over
5,611 tokens, 372 marks, 1,336 artifacts), the L3
attested ordered-pair table (4,275 adjacencies), and
the L3 positional table (per-mark group-initial counts).
It predicts a reserve token m at a position with
predecessor `prev` — the preceding token of the same
recorded group, or NONE at a group's first token (no
prediction crosses a recorded boundary, the L3 rule
D-105-13) — by these rules, applied in this order:

1. If m is outside the derivation inventory, the
   unseen-mark rule (below) applies, under both models.
2. If `prev` is NONE: if m's filed group-initial count
   is positive, P(m) = initial_count(m) / 1,336;
   otherwise the unigram backoff, P(m) = count(m) /
   5,611.
3. If `prev` is not NONE: if the ordered pair
   (prev, m) is attested in the filed L3 pair table
   with count c > 0, P(m) = c / successors_total(prev),
   where successors_total(prev) is prev's filed L3
   total of attested successors; otherwise the unigram
   backoff, P(m) = count(m) / 5,611. (A `prev` outside
   the derivation inventory attests no pair, by
   construction, and falls to the backoff.)

**The baseline.** The sandbox's own L2 frequency model,
exactly as filed in
`records/stage-2-indus-unigram-baseline-2026-11-25.json`:
at every position, P(m) = count(m) / 5,611 for m in the
derivation inventory, and the unseen-mark rule for m
outside it.

**The unseen-mark rule (frozen before unsealing).** A
reserve token whose mark is outside the derivation
inventory — 18 such marks exist, per the Stage 1 record
(390 recorded marks in the full corpus, 372 in the
derivation inventory) — is scored at the fixed
probability ε = 1 / (5,611 + 372) = 1 / 5,983 under
**both** models. The rule is symmetric by design: an
unseen token contributes the identical log-loss,
ln(5,983), to both models, so unseen tokens cannot
decide the gate; what decides it is the models'
relative scoring of the marks the derivation saw. The
gate's output files the unseen-token count so the size
of the undecidable share is on the record.

**Scoring and the margin (frozen before unsealing).**
The checker unseals the reserve exactly once and scores
every token of every reserve artifact (334 artifacts,
1,391 tokens as filed at Stage 1), artifacts and tokens
in recorded order, by per-token log-loss (natural
logarithm): each model's score is the mean over all
1,391 tokens of −ln P(token). **GOOD** iff
baseline_mean − derived_mean ≥ **0.05 nats per token**;
otherwise **NOT-GOOD**. The margin is small, round, and
non-trivial by design: the derived system must beat the
most elementary predictor the ladder itself produces by
a twentieth of a nat per token on average — equality,
or a win inside that margin, does not pass.

**What the outcomes establish, and what they do not.**
GOOD on G-IND licenses only this: the derived Indus
system, as filed at L4–L5, predicts the withheld
recorded streams better than the sandbox's own L2
unigram baseline by the frozen margin, on this reserve,
under the frozen unseen-mark rule. It is not a
decipherment claim, it assigns no value or meaning to
any mark, and it moves no standing, verdict, or tally
(C105-5). NOT-GOOD means the derived Indus meaning
system stays sandbox-internal, permanently unless a
later gate says otherwise (spec.md section 7), and is
filed as such.

**The unsealing discipline.** The reserve is opened
only by the G-IND checker, only in this stage's
execution, and only after this registration stands
committed in the landing branch's history; the
execution script refuses to open the reserve unless
this registration file is tracked and unmodified in the
clone's git index (a mechanical witness inside the run;
the branch history is the proof of record). The gate's
output files the reserve's SHA-256 as sealed (before
the run) and as scored (the bytes the checker read),
which must be identical: the scored bytes are the
sealed bytes.

## 6. Procedure and test cases

Each gate runs under two independently written checker
implementations, which must agree exactly (the
two-implementation discipline of Stages 1–5, extended
to the checkers): implementation A, a Python checker
over the filed lower-rung outputs; implementation B, an
independent checker built on jq event streams over the
datasets' raw bytes through sort and uniq -c with awk
assemblies, sharing no code with A, which re-derives
the sandbox-side structures it checks (inventories,
positional counts, pair counts, counts) from the
streams themselves and reads the outside tables from
its own copy of the tables of section 2. Agreement is
on the canonical comparison tables: for G-ETE and
G-MER, the per-mark and per-class verdict tables and
the comparison counts; for G-IND, the scoring case
tables — per model, the count of reserve tokens scored
under each rule at each distinct probability, filed as
(rule, numerator, denominator) triples with their token
counts, all integers and rationals exact. Each
implementation then computes the two mean log-losses
from its own case table in double precision; the filed
figures are those means rounded to six decimal places,
and they must be identical between the implementations.
Any disagreement stops that gate and is reported with
its evidence; one gate's stop does not stop the others.

Gate steps, in order: (i) custody hashes verified (a
hash failure stops that gate before any checking);
(ii) G-ETE and G-MER run their comparisons of sections
3 and 4; (iii) G-IND's checker verifies the registration
guard of section 5, unseals the reserve, and scores;
(iv) the outcome record files, per gate: the
comparisons run and the word returned for each, the
counts behind each word, the implementations'
agreement, and for G-IND the case tables, the two mean
log-losses, the margin arithmetic, the unseen-token
count, and the reserve's hashes as sealed and as
scored. No step takes any input beyond sections 2 and
5 of this record and the filed lower-rung outputs.

Test cases registered for this stage:

- **TC-105-20 — G-ETE agreement and execution (C105-1,
  C105-4, C105-5).** The two checker implementations
  produce identical per-mark and per-class verdict
  tables for ETE-1 and ETE-2, and the words returned
  are exactly the words those tables determine under
  section 3. *Pass:* identical tables, and each word
  the table's mechanical consequence.
- **TC-105-21 — G-MER agreement and execution (C105-1,
  C105-4, C105-5).** The same discipline for MER-1,
  MER-2, and MER-3 under section 4, including the
  positional counts implementation B re-derives from
  the Meroitic streams, which must equal the filed L3
  positional rows for the marks `a` and `i`. *Pass:*
  identical tables and counts, and each word the
  table's mechanical consequence under the registered
  tolerance.
- **TC-105-22 — G-IND agreement and execution (C105-4,
  C105-5).** The two implementations' scoring case
  tables are identical, their six-decimal mean
  log-losses are identical, and the word returned is
  the mechanical consequence of the frozen margin
  (section 5). *Pass:* identical case tables and
  figures, and the word determined by them.
- **TC-105-23 — Registration before unsealing, and the
  seal (C105-4).** This registration's commit precedes
  the execution commit in the landing branch's history;
  the reserve's SHA-256 before the run equals the hash
  filed at build; the reserve's SHA-256 as scored
  equals it again; and the execution script's opened
  paths are audited: before this stage no derivation
  opened the reserve (Stages 1–5, TC-105-06/09/12/15/18),
  and in this stage only the G-IND checker opens it,
  after the registration guard passes. *Pass:* the
  order and both hashes as stated, and the audit clean.
- **TC-105-24 — Standing discipline at Stage 6
  (C105-5).** TC-105-07's check over this landing's full
  diff, executed at pull-request time. *Pass:* no record
  states a changed standing, verdict, or tally in any
  program; the gate outcomes appear only in this spec's
  records, stated with the licenses of sections 3–5 and
  no wider; no working sign list, anchors register, or
  corpus file is modified; the recommendations ledger
  is untouched.

## 7. Outcome vocabulary and stop rules

Per gate: **COMPLETED** (the gate ran as registered and
its words are filed) / **STOPPED** (the step that
failed, named, with its evidence). Per comparison, the
word is GOOD or NOT-GOOD, exactly as spec.md section 7
registers, and a NOT-GOOD is a failure of the method at
that rung, filed as such — it is a result of this
study, not an execution failure. A dataset-hash failure
stops that gate before any checking. An implementation
disagreement stops that gate at its test case. The
stage returns no verdict about any language beyond the
gates' own words and their registered licenses.

## 8. Decisions

- **D-105-24 — Stage 6 is registered by this record.**
  The amendment takes the program's record form (as
  adjudication and stage records do elsewhere in this
  repo); spec.md is not edited in place. The landing
  is confined to this spec's records folder.
- **D-105-25 — The checkers' outside tables are the
  filed sources of section 2, and no others.** For
  G-ETE, Spec 096's filed signary frame and token
  conventions with the Common syllabary value table
  enumerated in the registration itself, so the exact
  table applied is on the record. For G-MER, the
  pinned build's own transliteration map: the gate
  checks the derivation against the values of the very
  convention the sandbox's source is written in, as
  that build files them. A checker that ranged wider
  for its tables would make the comparison depend on
  the checker's reading; these tables make it depend
  on the record.
- **D-105-26 — The positional tolerance is 95 in 100,
  fixed before the checker runs.** Spec.md section 7
  provides that a comparison's tolerance is part of
  its gate-stage registration, under the ELSEWHERE rule
  that close-or-similar passes the first gates. The
  positional facts of section 2 are facts about the
  script's orthography; the sandbox's corpus is a
  transcription of damaged ancient texts whose own
  build documents convention-mixing and lacunae, so
  exact conformance is not the registered standard at
  this first gate, and a one-in-twenty tolerance is
  the elementary close-or-similar bar. The tolerance
  applies identically to MER-2 and MER-3, and the
  exact counts are filed either way. The inventory
  comparisons (ETE-1, MER-1) and the non-merger
  comparison (ETE-2) carry no tolerance: a mark is in
  the table or it is not, and a class merges two
  distinct values or it does not.
- **D-105-27 — The G-IND predictor is the filed L3
  structure with unigram backoff, and the initial rule
  is the filed L3 initial distribution.** The derived
  system at L4–L5 has no predictive content beyond the
  ladder's filed tables; the most elementary predictor
  those tables define is the first-order one — the
  attested-pair conditional where a pair is attested,
  the group-initial distribution at a boundary, and
  the L2 unigram everywhere else. Anything smoother
  (interpolation weights, discounting) would be a
  modelling choice imported at gate stage; the
  registered predictor uses only filed counts, in the
  order of section 5.
- **D-105-28 — The unseen-mark rule is a single fixed
  ε = 1/5,983, symmetric across both models.** 5,983 =
  5,611 + 372, the derivation token total plus the
  derivation inventory size: the elementary
  one-count-reserved form, stated as a rule of the
  gate rather than as a change to either model — the
  baseline is scored exactly as filed, and the derived
  predictor exactly as registered, and ε enters only
  where neither model files mass. Symmetry is the
  point: the reserve's 18 unseen marks are a fact
  about the partition, not evidence for either model,
  and the rule keeps them from masquerading as either.
- **D-105-29 — The G-IND margin is 0.05 nats per
  token, frozen before unsealing.** Spec.md section 7
  requires the margin to be frozen in the gate stage's
  registration before the reserve is unsealed; this
  record freezes it. A twentieth of a nat per token on
  average is deliberately small — the derived system
  is a sparse first-order structure over 372 marks and
  most reserve positions will fall to its backoff —
  and deliberately non-zero: the gate exists to
  distinguish a derived system that predicts from one
  that merely redescribes its derivation set, and a
  margin of zero would pass a tie.
- **D-105-30 — Gate outcomes are recorded at their
  registered licenses, and the study's claims are not
  gate claims.** The gates test the derived systems,
  not C105-1..C105-5; no claim's status changes by a
  gate word except as the ELSEWHERE log records the
  contact points discharged. A GOOD licenses the
  comparison checked and nothing else (spec.md section
  7; C105-5); in particular no GOOD at G-ETE or G-MER
  says anything about Indus, no result crosses between
  sandboxes (C105-4), and G-IND's word, either way,
  is a statement about prediction on one sealed
  reserve under one frozen rule — the study's designed
  terminus, reached as registered.
