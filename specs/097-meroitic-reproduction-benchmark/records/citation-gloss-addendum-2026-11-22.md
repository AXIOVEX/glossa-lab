# Citation-Gloss Addendum and Reconciliation Table — Co-scientist Refresh Adjudication Landings (Spec 097)

**Date:** 2026-11-22. **Program:** Spec 097 — Meroitic
Reproduction Benchmark. **Authority:** the Co-scientist
refresh adjudication of 2026-11-22
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
§5, landing L-4, units M-1, M-3, M-4, M-6, M-8, M-10,
M-11 and M-14 as there adjudicated. This addendum fixes
the glosses and scope clauses that travel with Spec 097
citations and assembles the claim-by-claim
reconciliation table from the filed records only.
**It changes no verdict, no tally and no custody
posture.** The adjudicated citation forms stand,
including Leg A's "positively contradicted: 1 (A9)"
(M-2 is an owner-decision item and is not landed here).

## 1. Leg A scope clause (M-1)

Every citation of the Leg A verdict — **REPRODUCED IN
PART / DEPOSIT INCOMPLETE** — carries the scope clause:
"incomplete" means incomplete **for reproducing the
specified published quantities**. It does not imply a
breached deposition commitment, none having been
established. Missing material makes a count untestable
from the deposit, not wrong: absence of the counted
intermediates and source materials is evidence about
the deposit, not a failed reproduction of the count
(the verdict restatement's own basis).

## 2. Table 2 name-list discrepancy — rule and provenance (M-3)

Stated with every citation surface, outside the
ten-item Leg A tally: **names, 22 reproduced versus 18
published.** Counting rule: the standalone-file basis —
each Table 2 dictionary size counted on its standalone
file (the other six sizes reproduce exactly on that
basis: nouns 26, numbers 15, verbs 14, titularies 9,
adjectives/adverbs 6, prepositions 3). Provenance: the
discrepancy traces to repository state after
publication — the combined dictionary file's names
section holds exactly 18 pairs; the standalone names
file, added at the pinned (post-publication) commit,
differs by +6 pairs and −2 orthographic variants
(outcome record; tally correction of 2026-11-21).

## 3. Claim-by-claim reconciliation table (M-4)

Assembled from the filed outcome record of 2026-11-20,
its companion results files (`leg-a-results.json`,
`leg-b-results.json`, `leg-c-summary.json`), the
verdict restatement of 2026-11-20 and the tally
correction of 2026-11-21. Reproduction basis throughout
Leg A: the program's census scripts over the pinned
corpus, re-run on tower-compute; every reproduced value
in the outcome record was reproduced exactly by that
re-run.

### Leg A — the ten counts (published: Otten & Anastasopoulos)

| # | Published location and target | Counting rule | Reproduced | Scoped verdict |
|---|---|---|---|---|
| A1 | Table 1, translated Meroitic entries: 193 | Distinct headwords, LobbanVocabList.txt (195 data rows, 175 carrying translations; the count matches on the distinct-headword basis) | 193 | Exact |
| A2 | Table 1, Meroitic phrases: 897 | No frozen basis reproduces it (envelope 861–1,149 across the frozen cleanings; Table 1's 897 vs §5.2's 871 differ by 26) | — | Basis-unstated divergence — the counted processed corpus was never published |
| A3 | Table 1, Egyptian texts: 302 | Not countable | — | Untestable for absence — the Ramses scrape material is not in the repository in any form |
| A4 | Table 1, Nubian pages: 708 | Not countable | — | Untestable for absence — scanning-programme material not in the repository |
| A5 | §5.3, phrases pre-augmentation: 871 | Closest frozen basis 872 (Δ1); envelope 838–885 | — | Basis-unstated divergence — same cause as A2 |
| A6 | §5.3, Egyptian types: 1,729 | Vocabulary headers of the published dim-100/120 Egyptian embeddings (dim 20/50 carry 1,746, a named variant) | 1,729 | Exact |
| A7 | §5.3, Egyptian tokens: 99,338 | Not countable | — | Untestable for absence — no Egyptian corpus text is published |
| A8 | §5.3, distinct Meroitic forms post-augmentation: 1,868 | Distinct whitespace types in mero-corpus.txt (cross-confirmed by the dim-100/120 Meroitic vocabularies; \w+ types 1,808) | 1,868 | Exact |
| A9 | §5.3, phrases post-augmentation: 17,257 | Non-blank lines of the deposited mero-corpus.txt | 18,090 (17,995 distinct), Δ +833 | Positively contradicted — the deposited file is the name-augmented training file, not the counted augmented file |
| A10 | §5.3, words post-augmentation: 782,761 | \w+ token count (whitespace basis 756,028; dot-split 782,750, Δ11) | 782,761 | Exact |

Tallies of record (tally correction, 2026-11-21):
Exact 4 (A1, A6, A8, A10); positively contradicted 1
(A9); untestable for absence 3 (A3, A4, A7);
basis-unstated divergences 2 (A2, A5). 4 + 1 + 3 + 2 =
10. On the testable counts only: 4 exact of 7.

### Beside the ten counts

| Item | Statement |
|---|---|
| Table 2 names | 18 published; 22 reproduced on the standalone-file basis — stated separately, not as one of the ten counts (§2 above). |
| The 662 result | **Additional** to the ten Leg A items (adjudication §4, C-3): the MikeKovetsky/meroitic account's count of distinct texts in the deposited corpus file, reproduced exactly — 662 distinct texts, 18,075 tokens — under RT1-13 in the F-4 package (`records/662-distinct-texts-reproduction-2026-11-22.md`). No Leg A tally changes. |
| Leg B fixture — impact | The Leg B fixture (a sign inventory with a stated frequency-rank convention) was found internally inconsistent and is not interpretable as calibration (restated verdict); its criteria fail on both filed bases (attested-set extras under either reading; Spearman ρ = 0.314 E-only / 0.258 full fold against the ρ ≥ 0.90 bar). **Fixture dependency, as far as the filed records show: no downstream conclusion in the filed records depends on the fixture** — Leg B's verdict measures the fixture against the corpus and draws no finding about Meroitic sign values, and Legs A and C do not use it. Any deeper dependency analysis is new work (adjudication unit M-16's commission family, an owner decision). |
| Leg C — cell-level disagreements, quantified | Pattern reproduced; fixed points not held. Unseen-dictionary P@10 across all valid runs: {0.0, 1.19, 1.45, 1.72, 3.45} percent against the paper's fixed point of exactly 0 — the non-zero values are the seeded cells, at chance level (1–3 pairs of 58–84). Training-dictionary accuracy at 100d, Arm 1, sits inside the paper's at-most-20 percent headline (numerals [13.33, 6.67, 20.0]; nouns [11.54, 7.69, 7.69]), but the at-most-25 percent training band is exceeded in some non-100d cells; the maximum training accuracy anywhere is 33.33 percent. Substantive inference: the disagreements are confined to cells the paper does not headline; the headline pattern at 100d (low training accuracy, no meaningful unseen transfer, numerals strongest in the primary arm) reproduces, and the record reports the cells as they stand. |

## 4. F-6 restated (M-6)

The circulated F-6 sentence ("no further steps on this
corpus absent an objection from its authors") does not
state the posture of record and is replaced, in every
surface that carries it, by the following restatement,
which itemises the five action classes at their current
states under the custody record of 2026-11-20
(`records/custody-record-2026-11-20.md`). **The posture
itself is unchanged by this restatement**; any change
to what is permitted or paused is an owner decision
(adjudication unit M-7).

> **F-6 (restated).** The Otten corpus repository
> (pin `c9158f68…`) carries no licence. The corpus is
> held under an **owner risk-acceptance** (the owner,
> Tristen Pierson, by the delegation of 2026-11-20) —
> not a licensing finding and not the rights holders'
> consent; the permission request of 2026-11-20 stands
> unanswered, and silence is not permission. Under that
> posture: **retention — permitted** (the pinned copy
> lives in scratch custody on tower-compute; it is
> never committed to this repository); **computation —
> permitted** (held-custody computation, as executed in
> freeze v3 and the 662 reproduction, proceeds without
> waiting for an objection); **derived artifacts —
> permitted in aggregate form only** (the program
> publishes its own code and derived aggregate
> statistics only; no output may require redistributing
> Otten-derived text); **sharing — paused** (no
> redistribution of the corpus or of Otten-derived text
> to any party); **publication — permitted for
> aggregate statistics only, barred for corpus material**
> (every citation of the benchmark verdict carries the
> custody caveat in the same sentence until permission
> lands).

## 5. Affiliation gloss rules (M-8)

Citations of the Stage 4.2 result observe the
following. The result is **UNDECIDABLE AT THIS POWER**:
S = 4 of 12 concepts, permutation p = 0.0326, against
the registered bars p < 0.01 AND S ≥ 5 — failing both.
UNDECIDABLE AT THIS POWER is a registered outcome, not
proof that low power is the sole explanation. "R3 not
displaced" is honest as non-rejection only: it is not
evidence that an isolate hypothesis is true, a
chance-matching statistical null is not synonymous with
linguistic isolation, and R1, R2 and R3 are not implied
to exhaust possible affiliations. The result is not
rescued at p < 0.05 after the fact. The filed power
statement travels with the result (power 0.81 only if
the true per-concept correspondence rate is 0.50; 0.42
at 0.35 — a miss of this size is uninformative, not
suggestive).

## 6. The partial candidate — narrowing sentences (M-10)

Every citation of soreyi's Stage 4.4 result carries the
record's own narrowing sentences: the result **validates
a retrieval route, not a reading**. Soreyi's presence in
10 of 16 held-out funerary texts establishes frequency
in that subset; it does not distinguish "offering term"
from a divine-name variant or another recurrent funerary
component. Soreyi already stood in anchor freeze v1
Class B as the Osiris invocation form, and the blind
test supports exactly the behaviour of a spelling
variant of the anchored theonym sorey — present across
the held-out funerary corpus, absent elsewhere. The
campaign's one positive blind-test result is a variant
of an already-anchored form, rediscovered by the
distributional route; it is a bounded result about the
method, not a new reading.

## 7. Seal rule, cap reasons, candidate pointers (M-11)

Campaign summary surfaces carry: the seal-rule sentence
— **"The seal is procedural and unverifiable by
construction (freeze v2 §6); that sentence travels with
every score"** (Stage 4.4 record); the cap's two
recorded reasons (the procedural,
unverifiable-by-construction held-out seal; and the
candidate reading as generated, "theonym-adjacent cult
or offering term," being weaker than the fact the blind
test supports); and pointers to the six candidate
definitions and their falsifiers (Stage 4.3 records:
`records/stage-4-3-outcome-record-2026-11-20.md` and
companion `records/stage-4-3-candidates.json`; scoring
at Stage 4.4 against frozen pass/fail predictions —
presence in at least 3 held-out texts; funerary share
in the registered range). There is no numeric score
behind the cap and no uncapped score exists to disclose
(adjudication §4, C-1).

## 8. Expert-verification attribution discipline (M-14)

Summaries keep "only Rilly could answer" **attributed
to the correspondent** (de Voogt, 2026-11-20): it is not
a methodological restriction. De Voogt's confidence in
the wordlist's standing is contextual testimony, not
item-by-item confirmation; the redirect is neither
confirmation nor a negative judgment. The Stage 4.5
verdict stands cited as **ANSWERED-BY-REDIRECT / NOT
CONFIRMED**.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.

## 9. Amendment — OD-13: the A9 citation form (2026-11-22)

**Date of amendment: 2026-11-22. Authority: owner
decision OD-13 (unit M-2), recorded at §10 of the
governing adjudication record.** The owner changed
the adjudicated citation of Leg A claim A9. From this
amendment forward, A9 is cited as **discrepant under
the documented reproduction procedure**: the published
count (17,257 phrases post-augmentation) was never
tested against the counted file, because the deposited
file is the name-augmented training file (18,090
non-blank lines), not the counted augmented file.

**Original form, preserved (amendment trail).** The
text above is not rewritten. It carries the superseded
form in three places: the headnote ("The adjudicated
citation forms stand, including Leg A's 'positively
contradicted: 1 (A9)'"), the A9 row of the §3 table
("Positively contradicted - the deposited file is the
name-augmented training file, not the counted augmented file"), and the tallies paragraph
("positively contradicted 1 (A9)"). Each is superseded
as a citation form by this amendment; the numbers and
the counting basis stated in the table are unchanged.

**What does not change.** The Leg A tallies stand:
Exact 4 (A1, A6, A8, A10) / Contradicted 1 (A9) /
Untestable 3 (A3, A4, A7) / Basis-unstated 2 (A2, A5).
The tally's one-count category is unchanged as a
count; only A9's citation form changes. No verdict
changes, and the Leg A verdict (REPRODUCED IN PART /
DEPOSIT INCOMPLETE) is untouched. The Table 2 names
statement (§2) is outside OD-13, which names A9
only, and stands as written.

**AI disclosure:** this amendment was executed by an
AI agent (Muse, via Muse) at the direction of
Tristen Pierson, per constitution sec. VI.

**Gloss — 2026-11-22, Red Team Round 6 correction (RT6-L3), on the §9 OD-13 amendment above:** the tally heading "Contradicted 1 (A9)" is a count label of record, and A9's citation form within it is the OD-13 form, "discrepant under the documented reproduction procedure". Tallies unchanged.
