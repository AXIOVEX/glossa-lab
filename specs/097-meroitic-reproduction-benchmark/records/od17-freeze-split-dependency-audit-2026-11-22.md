# Spec 097 — OD-17: Dependency-Level Audit of the Freeze Split (Stage 4.2)

**Date: 2026-11-22. Commission:** owner decision OD-17 from
the Co-scientist refresh adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
commissioned by the owner 2026-11-22 13:27 ET. **Venue:**
tower-compute. **Method:** the audit executed the program's
own Stage 4.2 code path (`pipeline-v2.py`, held in the
campaign scratch) — its vocabulary build, its ASJP loading,
its scoring and permutation functions, and its partition
function — against the custody data on tower-compute, and
traced the executed inputs. No Otten-derived text is
published here; every number below is an aggregate over the
CC BY 4.0 inscription corpus, the CC BY / CC BY-SA
vocabulary sources, and the CC BY 4.0 ASJP lists. **Scope:**
the Stage 4.2 affiliation tests as executed under freeze v2
(S = 4 of 12, p = 0.0326, UNDECIDABLE AT THIS POWER), and
the freeze split (335 development / 33 held out over the 368
distinct texts) they rest on. Freeze v3 enters only where
its §3 table bears on the filed denominators (§3.3). **This
audit changes no verdict.** One reporting defect is flagged
for adjudication (§5).

## 0. Reproduction gate

Before any tracing, the executed code path reproduced the
filed Stage 4.2 results exactly: R1 vocabulary test S = 4
with the identical per-concept vector (matches at 21, 46,
72, 75) and permutation p = 0.032596740325967405 (filed:
0.0326); R2 vocabulary test S = 1 (match at 46) and
p = 0.824017598240176 (filed: 0.824). The audit therefore
traces the computation that actually ran, not a
reimplementation.

## 1. Split independence

**The split as executed.** The acquired inscription corpus
collapses to 368 distinct texts (exact-text deduplication
first); each distinct text is then assigned by
SHA-256(text) mod 10 == 0 to held out, else development:
335 development / 33 held out, recomputed identically by
this audit. Because deduplication precedes the hash rule,
one text string cannot fall on both sides: the recomputed
intersection of the two partitions is **0 texts**. The
name-augmented file, whose swapped-name twins caused the
freeze v1 defect, is excluded from the split entirely
(freeze v2 §1), so that leakage channel does not exist in
the executed basis.

**Where the split does and does not enter Stage 4.2.** The
vocabulary tests' inputs never pass through the corpus
split at all: the Meroitic side is the gold-lexicon /
Wiktionary vocabulary and the comparator side is the ASJP
lists. The corpus-derived Stage 4.2 quantities — the
formative leg's attestation counts and the phonotactic
statistic — were computed over the development partition
plus the 932 distinct example phrases. The held-out
partition is computed by the pipeline's partition function
but is read by no Stage 4.2 code path; only Stage 4.4 reads
it. The outcome record's statement that the held-out
partition was not touched is confirmed at code level.

**The example phrases.** The 932 distinct example phrases
(per-scholar files: Millet, Rilly, Kalabsha) are development
material by registration — they are the generation source
and are never sealed. Traced against the held-out side:
**0** of the 932 match a held-out text exactly, and **0**
occur as a token sequence inside any held-out text
(phrases of 3+ tokens). (They also match 0 development texts
exactly; they are a separately normalised source.) The
audit's proof is at the level the freeze's split operates
on — string identity of the executed bases. It is recorded
for completeness that the phrases derive from published
editions of the same inscription population as the corpus;
no string-level channel between them and the 33 held-out
texts exists in the executed computation.

**Conclusion.** No cross-split dependency exists in the
executed Stage 4.2 computation: the partitions are disjoint
by construction and by recomputation, the sealed side is
unread by the stage, and the one development-side source
drawn from outside the corpus (the example phrases) shares
no text with the sealed side.

## 2. Cross-candidate dependencies within Stage 4.2

The 12 scored concepts are usually read as 12 trials. At
dependency level they are not independent, in the following
traced respects. None of these moved an executed outcome
except as noted; each is a property of the design as
frozen, faithfully executed.

**D-1. One skeleton serves two candidates.** The consonant
skeleton **kd** is the entire matching substance of two
different concepts: 16 woman (Meroitic forms kdi, kadi) and
62 kill (ked, kede). A comparator skeleton matching kd
would count toward both candidates at once. As executed,
neither 16 nor 62 matched in either test, so no double
count occurred in S; the dependence is structural. It is
one reason the joint permutation null (§4), not the
freeze's binomial power arithmetic, is the operative null.

**D-2. No form serves two candidates.** Traced
exhaustively: no normalised Meroitic form in the executed
vocabulary is assigned to more than one concept (the shared
-form set is empty). Each gold entry contributes its forms
to exactly one concept.

**D-3. Length-1 skeletons reduce two candidates to a
first-consonant test.** The registered match rule waives
the second-consonant condition when either skeleton has
length 1. Two candidates carry single-consonant Meroitic
skeletons: 70 give (l) and 75 water (t). Concept 75's R1
match — one of the four that make S = 4 — was produced
entirely at length 1 on both sides: ato / ate (skeleton t)
against Meidob 3Ti and Old Nubian etu (both skeleton t).
Concept 46's matches in both tests likewise turned on
length-1 comparator skeletons (R1: Dongolese os, skeleton
s, against st; R2: Hausa sau, skeleton s, against st). The
full match-pair trace for the five observed matches:

| Test | Concept | Meroitic form (skeleton) | Matching comparator forms (skeleton) |
|---|---|---|---|
| R1 | 21 dog | wle (wl) | Dongolese wEl (wl), Kunuz wel (wl) |
| R1 | 46 foot | st (st) | Dongolese os (s) |
| R1 | 72 sun | ms, mš, mos (ms), mash (msx) | Dongolese / Kunuz / Old Nubian masil, maSal (msl), Nobiin maSa (ms) |
| R1 | 75 water | ato, ate (t) | Meidob 3Ti (t), Old Nubian etu (t) |
| R2 | 46 foot | st (st) | Hausa sau (s) |

**D-4. Comparator items filed under more than one
concept.** ASJP files some (language, form) items under
several concepts. Within the scored 12, one such item sits
inside a candidate's denominator: (NARA, Sokna) is filed
under concepts 45 and 46 and is one of only two NES
comparator forms for scored concept 46. It did not produce
the 46 match (its skeleton skn fails the second-consonant
condition against st; the match came from Dongolese os).
Form strings shared across concepts, scored or not, are
few and listed here in full — NES: wel (11, 21), Sokna
(45, 46), ku (17, 18), ni (6, 54, 70); AA: mu (3, 61, 75),
mau (61, 75), ruwa (75, 76), s3w and mutum (17, 18). The
sharing is at string level; as ASJP rows the items are
distinct, and the permutation treats them as distinct.

**D-5. The permutation pool is the whole ASJP concept
list, not the 12 candidates.** As freeze v2 §4 registers,
each permutation shuffles comparator forms across concepts
preserving per-concept counts — over **all 100 concepts**
present for the comparator languages. The NES pool is 374
forms, of which 45 (12%) belong to the scored concepts; the
AA pool is 496 forms, 51 (10%) scored. The null
distribution of S is therefore generated by drawing each
candidate's comparator forms from the pool-wide skeleton
frequencies of those languages (recomputed nulls in §4:
R1 mean S = 1.51). This is the registered design, executed
as frozen; its consequence is that the p-value prices a
match against the languages' whole attested skeleton
inventory, not against the 12 concepts' own forms alone.

**D-6. Sharing across the stage's tests.** The R1 and R2
vocabulary tests share the same Meroitic vocabulary and the
same 12 candidates; concept 46 matched in both through the
same Meroitic form (st). The two comparator language sets
are disjoint; six form strings occur in both pools (Sita,
asa, kare, man, ni, siu) as distinct rows of different
languages. The phonotactic leg's NES reference rate
(0.3038) is computed over the same NES ASJP forms that
serve as R1's comparators, so the R2 phonotactic leg is
benchmarked against the R1 comparator pool. The formative
leg and the vocabulary test share the gold lexicon /
morphology apparatus of one scholarly tradition — the
framework dependence freeze v3 §4 states, which this audit
confirms at input level and does not re-open.

## 3. Candidate-wise denominators

### 3.1 The denominators as executed

Each candidate's score is binary (at least one match), but
the trials behind the 12 binaries are of unequal size on
both sides. As executed (executed vocabulary build; ASJP
forms for the registered language sets):

| Concept (ASJP) | Meroitic forms (n) | NES comparator forms (n) | AA comparator forms (n) | R1 | R2 |
|---|---|---|---|---|---|
| 12 two | tbe, tbo (2) | 8 | 7 | – | – |
| 15 small | shi, sxi, sḫi (3) | 2 | 3 | – | – |
| 16 woman | kadi, kdi (2) | 2 | 2 | – | – |
| 17 man | abr, br (2) | 2 | 3 | – | – |
| 21 dog | wle (1) | 6 | 8 | match | – |
| 46 foot | st (1) | 2 | 3 | match | match |
| 55 eat | hre, xre, ḫr-, ḫre (4) | 2 | 2 | – | – |
| 62 kill | ked, kede (2) | 2 | 2 | – | – |
| 70 give | l, l- (2) | 3 | 3 | – | – |
| 72 sun | mash, mos, ms, mš (4) | 6 | 7 | match | – |
| 75 water | ate, ato (2) | 8 | 8 | match | – |
| 97 good | mlo (1) | 2 | 3 | – | – |
| **Total** | **26 forms** | **45** | **51** | **S = 4** | **S = 1** |

Only 26 of the vocabulary's 182 forms carry a scored
concept; the remaining 156 forms enter no Stage 4.2 score.
NES comparator coverage is uneven by ASJP attestation:
most concepts draw on Dongolese and Nara only, while 12,
21, 72 and 75 draw on up to all six languages.

### 3.2 What the filed reporting used

Freeze v2 §4 and the Stage 4.2 outcome record report only
the shared denominator — "S = 4 of 12 concepts" — and
nowhere state the per-concept form counts of §3.1. "4 of
12" therefore pools trials of unequal opportunity (1–4
Meroitic forms, 2–8 comparator forms per candidate). The
design's own mitigation stands: the permutation null
preserves each concept's comparator count, so the p-value
is computed against nulls with the same unequal
denominators. The audit records the denominators so the
filed ratio can be read against them; it does not
re-adjudicate the ratio.

### 3.3 Freeze v3 §3's table: counts right, labels wrong

Freeze v3 §3 prints a per-concept form-count table. Its
**counts are correct**: audited against both vocabulary
companions and the executed build, the counts per concept
ID are identical in all three (12: 2, 15: 3, 16: 2, 17: 2,
21: 1, 46: 1, 55: 4, 62: 2, 70: 2, 72: 4, 75: 2, 97: 1),
and the v2 and v3 companions carry identical forms for
every scored concept, confirming v3 §3's coverage claim
numerically. Its **gloss labels are wrong for 9 of the 12
IDs** under the ASJP parameter numbering the test was
executed and filed under (ASJP parameters.csv, pinned in
freeze v2 §4): the table calls 12 "night" (ASJP: two),
15 "dog" (small), 17 "fire" (man), 21 "head" (dog),
46 "bone" (foot), 55 "louse" (eat), 62 "belly" (kill),
70 "heart" (give), 97 "egg" (good); only 16 woman, 72 sun
and 75 water agree. Its sentence naming R1's matching
concepts as "(2, 15, 16, 75)" likewise does not correspond
to the executed record: the matches are 21, 46, 72, 75,
and concept 2 was not a scored concept. Flagged for
adjudication in §5.

### 3.4 The formative leg's denominator

Freeze v2 §4 states the formative leg's bar as at least 20
tokens "in the development texts". As executed, the
attestation counter ran over the development texts **plus
the 932 example phrases** (the outcome record's basis
sentence discloses the phrases in the stage's computation
basis). Recounted on the freeze's stated basis
(development texts only), the same five formatives pass
the bar — -l 249, -leb 33, -o 622, -kwi 29, -w 60 — so the
leg's outcome (5 against a bar of 3, pass) is unchanged.
The executed basis did move one non-passing formative
close to the bar: -se counts 19 as executed but 2 on
development texts alone. Recorded as a freeze-conformance
discrepancy with no outcome effect; the leg is supporting
only and the verdict does not rest on it under either
denominator.

## 4. Multiplicity

**As filed.** No family-wise or false-discovery treatment
appears anywhere in freeze v2, its amendment, or the
outcome record. The Stage 4.2 family as executed comprises
the two vocabulary tests, the phonotactic leg (shuffle
p = 0.4737, plus its reference-rate condition) and the
formative leg (a count against a bar; it carries no
p-value and cannot enter a p-value correction). The
SUPPORTED verdict is disjunctive over the two rivals: R1
supported iff its vocabulary test passes; R2 supported iff
its vocabulary test and the phonotactic leg both pass.

**Within each vocabulary test, the 12-concept multiplicity
is handled by construction.** S is a single joint statistic
and its p-value comes from the joint permutation null, not
from 12 separate tests. Recomputed null distributions
(10,000 permutations, registered seed and design): R1 —
mean S = 1.5081, P(S ≥ 4) = 0.0325, P(S ≥ 5) = 0.0043;
R2 — mean S = 1.4099, P(S ≥ 5) = 0.0034. The freeze's
analytic α ≈ 0.0043 for the S ≥ 5 bar (a binomial
calculation assuming independent concepts at a 0.10 chance
rate) coincides with the R1 permutation tail P(S ≥ 5) =
0.0043; the permutation figure is the operative one, and
the binomial power statement (0.81 at a 0.50 per-concept
rate, 0.42 at 0.35) inherits the independence assumption
that D-1 shows the design does not strictly meet.

**Across tests, computed corrections.** No correction was
registered in advance, so the following are audit
computations, reported as such — not a retro-fitted bar.
Family of the two vocabulary tests (the family the
disjunctive verdict draws on):

| Test | p as filed | Bonferroni | Holm | Šidák | Benjamini–Hochberg q |
|---|---|---|---|---|---|
| R1 vocabulary | 0.0326 | 0.0652 | 0.0652 | 0.0641 | 0.0652 |
| R2 vocabulary | 0.8240 | 1.0000 | 0.8240 | 0.9690 | 0.8240 |

Widening the family to all three p-bearing Stage 4.2 tests
(R1 vocabulary 0.0326, phonotactic 0.4737, R2 vocabulary
0.8240): R1 adjusts to 0.0978 under Bonferroni, Holm and
Benjamini–Hochberg alike; the phonotactic leg adjusts to
1.0000 (Bonferroni), 0.9473 (Holm), 0.7105 (BH); R2
adjusts to 1.0000 (Bonferroni), 0.9473 (Holm), 0.8240
(BH).

**Consequence: none.** R1 failed its registered joint bar
uncorrected, on both components (p = 0.0326 against
p < 0.01; S = 4 against S ≥ 5). Every standard correction
widens that margin, and R2 and the phonotactic leg fail by
wide margins under any treatment. The Stage 4.2 verdict —
UNDECIDABLE AT THIS POWER, R3 not displaced — is unchanged
under every correction computed. What the corrections add
is the size of the margin: at family level the R1 signal
sits at roughly p ≈ 0.065–0.098, not at the filed 0.0326.

## 5. Flagged for adjudication

**F-A (reporting defect, freeze v3 §3).** The per-concept
table in freeze v3 §3 attaches glosses from a numbering
other than the ASJP parameter numbering of record to 9 of
its 12 concept IDs, and its matching-concepts sentence
"(2, 15, 16, 75)" does not correspond to the executed
Stage 4.2 record (21, 46, 72, 75). The table's counts are
verified correct (§3.3), and the defect touches no Stage 4
number — Stage 4.2 ran under freeze v2 and freeze v3 is
for future work only — but any future test frozen against
v3 would inherit the mislabelled table. Recommended
disposition: a dated correction to freeze v3 §3's labels
and sentence, counts unchanged. This audit takes no
position beyond the recommendation; the correction itself
is an adjudication act.

Nothing else found by this audit touches a verdict. The
formative-leg denominator discrepancy (§3.4) is
outcome-invariant and is recorded as a conformance note,
not a flag.

**Payload verdict: OD-17 audit executed — split
independence proven by trace and recomputation (partitions
disjoint, held-out unread by Stage 4.2, example phrases
share no text with the sealed side); candidate-wise
denominators stated as executed (26 Meroitic forms, 45 NES
and 51 AA comparator forms over the 12 concepts) against
the filed shared denominator of 12; multiplicity as filed
was none across tests and joint-by-construction within
each vocabulary test, and the Stage 4.2 p-value under the
standard corrections is 0.0652 (two-test family) to 0.0978
(three-test family) for R1 — the UNDECIDABLE verdict is
unchanged under all of them; one reporting defect in
freeze v3 §3 flagged for adjudication as F-A.**

