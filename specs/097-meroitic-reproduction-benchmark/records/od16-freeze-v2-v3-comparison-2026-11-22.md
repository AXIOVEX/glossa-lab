# OD-16 — Executable comparison of freeze v2 and freeze v3 (Spec 097, Stage 4.2 affiliation scoring)

**Date: 2026-11-22. Commission: owner decision OD-16 on the
Co-scientist refresh adjudication (adjudication unit M-12,
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
commissioned by the owner in chat 2026-11-22 13:23 ET.
Execution venue: tower-compute. Driver:
`tools/od16_freeze_compare.py` (filed with this spec).
Full machine-readable output: the companion
`records/od16-freeze-v2-v3-comparison-results-2026-11-22.json`.**

## What was asked, and what this record is

The freeze v3 record (`records/campaign-freeze-v3-2026-11-22.md`)
argued from the v2→v3 diff that no Stage 4 number can move,
and stated on its face that this was "not a re-run". Unit
M-12 held that unchanged concept coverage does not by itself
prove an unchanged score or p-value, and OD-16 commissioned
the executable comparison: run both freezes through the same
executable scoring path and compare inputs, scores and nulls
in numbers. This record is that comparison. **No verdict
changes; freeze v2's record and every Stage 4 record stand
untouched, as M-12 requires.**

## Method and validation chain

The scoring path is the program's own frozen pipeline,
`pipeline-v2.py` (campaign scratch on tower-compute,
SHA-256 `74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e`),
imported as a module; its own `gloss_score`, `perm_p`,
`asjp_forms`, `skeleton` and `match` functions were executed
— no reimplementation of any scoring function. The one
replica in the driver is of the `perm_p` loop itself, made
only to expose the full null histogram; on every run the
replica's p is asserted equal to the frozen `perm_p`'s p
before its histogram is reported (assertions held on all
four runs), and the p-values reported below are the frozen
function's.

Inputs and their identity, all verified by hash or equality
in the driver output:

- Vocabulary companions as registered: v2
  `records/freeze-v2-vocabulary-2026-11-20.json` (SHA-256
  `ab1de889b6e8674512fa64c9bb9e7bf5f2efe15f609f681558ba7781f23178fc`),
  v3 `records/freeze-v3-vocabulary-2026-11-22.json`
  (SHA-256 `ee7056a461907f213a92a7aeb268c0e11ffb0c88d736c9799df647101e68bdd1`).
- The v2 companion is the executed input, not a
  reconstruction: the pipeline's own design-mode output in
  the campaign scratch (`stage4-v2/vocab.json`) is
  JSON-equal to it, entry for entry.
- The executed outputs of record: the repo's
  `records/stage-4-2-results.json` and the scratch
  `stage4-v2/stage42-results.json` are byte-identical
  (SHA-256 `9ea5cce7d8cbeea182d49a6253c096e899e8fc94b5a4fd1e2b9a6b376233eb1f`
  both).
- ASJP CLDF inputs match freeze v2 §4's pins exactly
  (forms.csv `4ee30b77…`, languages.csv `647174df…`,
  parameters.csv `2ed306c2…`).

**Validation.** The v2 run through this path reproduces
the executed Stage 4.2 vocabulary legs exactly — S,
per-concept pattern, and p to the last float digit, for
both tests. The executable path is therefore the executed
path. The v3 run is then the comparison of record.

Custody: the vocabulary tests run on the registered
vocabulary companions (CC BY / CC BY-SA apparatus) and the
ASJP lists (CC BY 4.0) only; no Otten-derived text is read
or written, and this record and its companion carry
aggregate statistics and already-committed vocabulary forms
only (F-6 posture: computation permitted, derived artifacts
aggregate-only).

## 1. The inputs compared

**Structural diff of the companions** (keyed by form, gloss,
origin; 179 entries common to both):

| | freeze v2 | freeze v3 |
|---|---|---|
| entries | 182 | 179 |
| entries only in this freeze | qes, qos, qesw | — |
| Wikipedia citations in `sources` | 33 | 0 |
| common entries differing in any field | — | 30, all in `sources` only |
| common entries differing in form, norm, gloss, confidence, category, concept or origin | — | **0** |

The three v2-only entries are exactly anchor A1's forms
(qes, qos, qesw, all glossed "Kush", confidence "probable"),
and all three carry **concept: null** — freeze v2 §3 already
marks A1 PROVISIONAL and excludes it from scoring controls.
The 30 changed entries are the citation removals of the
freeze v3 record §2, verified here field by field: nothing
but the `sources` apparatus changed.

**Scoring-input projection.** Everything `gloss_score` can
see of a vocabulary is the multiset of (norm, consonant
skeleton, concept) over its concept-bearing entries. That
projection is **identical** under the two freezes: 26
concept-bearing forms, with forms per scored concept (ASJP
concept IDs with freeze v2 §4's glosses):

| concept | Meroitic forms | R1 (NES) comparator forms | R2 (AA) comparator forms |
|---|---|---|---|
| 12 two | 2 | 8 | 7 |
| 15 small | 3 | 2 | 3 |
| 16 woman | 2 | 2 | 2 |
| 17 man | 2 | 2 | 3 |
| 21 dog | 1 | 6 | 8 |
| 46 foot | 1 | 2 | 3 |
| 55 eat | 4 | 2 | 2 |
| 62 kill | 2 | 2 | 2 |
| 70 give | 2 | 3 | 3 |
| 72 sun | 4 | 6 | 7 |
| 75 water | 2 | 8 | 8 |
| 97 good | 1 | 2 | 3 |

The comparator side is the same pinned ASJP basis for both
freezes by construction: the R1 pool is 374 forms over the
6 attested NES languages (Old Nubian, Nobiin, Dongolawi,
Kunuz, Meidob, Nara), the R2 pool 496 forms over the 7
Afroasiatic languages (Coptic, Late Egyptian, Middle
Egyptian, Akkadian, Biblical Hebrew, Amharic, Hausa); the
per-concept counts above are the scored concepts' shares of
those pools, and the permutation design shuffles the full
pool across concepts preserving per-concept counts
(freeze v2 §4).

## 2. The scores compared

Both freezes, run through the frozen path, return the
executed Stage 4.2 scores **exactly** — and therefore
identically to each other:

| test | S | matching concepts | p (10,000 permutations, seed 20261120) | bar (p < 0.01 and S ≥ 5) |
|---|---|---|---|---|
| R1 attested, v2 | 4 of 12 | 21, 46, 72, 75 | 0.032596740325967405 | not passed |
| R1 attested, v3 | 4 of 12 | 21, 46, 72, 75 | 0.032596740325967405 | not passed |
| R2 Afroasiatic, v2 | 1 of 12 | 46 | 0.824017598240176 | not passed |
| R2 Afroasiatic, v3 | 1 of 12 | 46 | 0.824017598240176 | not passed |

Per-concept match patterns are identical in all three
columns (v2 run, v3 run, executed record) for both tests.
The matching pairs, identical under both freezes, are:

- **R1, 21 dog:** wle ~ Dongolawi `wEl`, Kunuz `wel`.
- **R1, 46 foot:** st ~ Dongolawi `os`.
- **R1, 72 sun:** ms, mš, mash, mos ~ Dongolawi `masil`,
  Kunuz `masil`, Nobiin `maSa`, Old Nubian `maSal` (16 pairs).
- **R1, 75 water:** ato, ate ~ Meidob `3Ti`, Old Nubian
  `etu` (4 pairs).
- **R2, 46 foot:** st ~ Hausa `sau`.

One detail is the substance of this commission: the cleanup
touched match-bearing forms. The concept-72 forms (ms, mš,
mash, mos) and the concept-75 forms (ato, ate) are among the
30 whose Wikipedia citations were removed, and concept 16's
cleaned forms (kdi, kadi) match under neither freeze. The
matches above reproduce identically with the citations gone,
because the scoring path never reads the apparatus — which
the next sections prove rather than assert.

## 3. The nulls compared

The full permutation-null distributions of S (10,000 draws
each), identical under the two freezes **count for count**,
not merely in their p-values:

| S_perm | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| R1 null count | 1528 | 3797 | 3112 | 1238 | 282 | 40 | 3 |
| R2 null count | 1760 | 4014 | 2903 | 1055 | 234 | 26 | 8 |

R1: null mean 1.5081, sd 1.0131; #{S_perm ≥ S_obs = 4} = 325,
p = (1 + 325) / 10001 = 0.032596740325967405. R2: null mean
1.4099, sd 0.9962; #{S_perm ≥ S_obs = 1} = 8240,
p = (1 + 8240) / 10001 = 0.824017598240176. Both p-values
are the frozen `perm_p`'s own outputs, and the replica's
independent recount of the same seeded stream returned the
same exceedance counts (325 and 8240) on both freezes.

## 4. Why the equivalence holds — the proof

The executable identity above is not a coincidence of this
seed; it is forced by what the scoring path reads, in three
steps, each checked in the driver output:

1. `gloss_score` reads only (skeleton of norm, concept)
   from each concept-bearing vocabulary entry, plus the
   comparator forms. `perm_p` reads the vocabulary only
   through `gloss_score` (its one other vocabulary-derived
   value, a `concepts` list, is computed and never used —
   verified in the frozen source). Neither function reads
   `sources`, `confidence`, `category` or `gloss`.
2. The v2→v3 transformation touched only what step 1 makes
   unreadable: the 3 removed entries carry no concept
   (`gloss_score` skips concept-less entries by
   construction), and the 30 changed entries differ only
   in `sources`.
3. The projection the path actually consumes — the
   (norm, skeleton, concept) multiset of §1 — is identical,
   the comparator pool is one pinned file set, and the seed
   is registered. Every downstream quantity (S, the
   per-concept pattern, the full null distribution, p) is
   a deterministic function of those, so all of them
   coincide; §2 and §3 are the executed confirmation.

## 5. Scope notes

- **The other two Stage 4.2 legs are vocabulary-independent
  by construction.** In the frozen `stage42()`, the
  phonotactic leg is computed from the corpus partition and
  the example phrases, and the formative leg from the gold
  morphology and development tokens; neither reads the
  vocabulary. They are identical under any vocabulary
  freeze, were not re-run, and their executed values stand
  as filed in `stage-4-2-results.json`.
- **One genuine downstream difference, outside the
  affiliation scoring.** Stage 4.3's known-form set is built
  from all vocabulary norms, so a future candidate-generation
  run under freeze v3 would no longer treat qes, qos, qesw
  as known forms. No landed Stage 4.3 result is affected:
  Stage 4.3 ran under freeze v2, and freeze v3 is for future
  work only under its own record. Recorded so that a future
  freeze re-running candidate generation states its
  vocabulary basis explicitly. This touches no verdict and
  is not flagged for adjudication.
- Stage 4.2's verdict — UNDECIDABLE AT THIS POWER, R3 not
  displaced — stands exactly as adjudicated. This record
  adds the executable demonstration M-12 asked for; it is
  not a new result and changes no standing.

**Payload verdict: executable equivalence PROVEN — under
the frozen Stage 4.2 path (itself validated to the last
float digit against the executed outputs), freeze v2 and
freeze v3 return identical scoring inputs (projection
identical; the only diffs are 3 concept-less exclusions and
30 `sources`-only citation removals), identical scores
(R1 S = 4, p = 0.032596740325967405; R2 S = 1,
p = 0.824017598240176) and identical full null distributions
(10,000 draws, count for count); no verdict changed, nothing
flagged for adjudication.**
