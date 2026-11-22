# Meroitic Program — Citation Discipline Record (Spec 097)

> **Correction pointer (2026-11-21, Red Team Round 3 —
> RT3-04):** this record's §1 basis statement for A8 (the
> dim-100/120 vocabulary header counts) and its §6
> attribution of the B1 gloss pair to freeze v1 are
> superseded by
> `records/citation-discipline-erratum-2026-11-21.md`, whose
> own §2 freeze citation is corrected by that erratum's
> Round 3 note (RT3-07). Citations of Leg A bases and of the
> B1 glosses follow the erratum as corrected.

**Date: 2026-11-21. Filed under Red Team Round 1 (findings
RT1-29, RT1-33, RT1-34, RT1-44, RT1-45, RT1-46, RT1-47,
RT1-48, RT1-49, RT1-56), each adjudicated APPLY on 2026-11-21.
This record fixes the form in which the benchmark's legs, the
Stage 4.2 verdict, and the Stage 4.4 scores are cited from
this record onward. It changes no number, no verdict, and no
standing; it governs how the existing record is quoted.**

## 1. Leg A — the exact tally carries its bases (RT1-44)

The tally is cited as **"4 of 10 counts exact, on the bases
stated here"** (tallies as corrected by
`records/verdict-tally-correction-2026-11-21.md`):

- **A1 (193)** is exact on the distinct-headword basis. The
  outcome record's own cell records 195 data rows, of which
  175 carry translations; the paper's count is of translated
  words. The reproduction is exact for headwords and off by
  18 for the thing labelled.
- **A6 (1,729)** and **A8 (1,868)** are the vocabulary header
  counts of the dim-100/120 embedding files. The dim-20/50
  files carry 1,746 and 1,902 respectively, as named variants.
  The paper counted types in a corpus that was never
  deposited; the program counted a deposited proxy artifact
  and, between two deposited variants, the one that matches.

## 2. Leg B — citation label sharpened (RT1-45)

The restatement retitled Leg B "internal fixture calibration."
That is no longer sufficient. The outcome record states, in
its own parenthesis, that the fixture's own 551-token
constructed corpus does not follow its stated rank order. A
comparator whose stated order is not reproduced by its own
tokens cannot serve as a calibration standard at a ρ ≥ 0.90
bar: the leg measures distance from an order nothing attains,
including its author. From this record onward Leg B is cited
only as: **"fixture internally inconsistent; the leg is not
interpretable as calibration."** Any downstream use of Leg B
as evidence about the fixture's quality inherits this label.

## 3. Leg C — arm structure and fixed points first (RT1-46)

Leg C is cited with its arm structure stated: **Arm 1, the
primary arm, ran on the authors' published embeddings on both
sides** (held under the same no-license custody as the
corpus); **Arm 2 is the only fully independent arm.** The
frozen fixed points failed and are stated before any
"pattern" sentence: unseen precision@10 was not exactly 0 in
the seeded cells (observed {0.0, 1.19, 1.45, 1.72, 3.45}),
and maximum training accuracy reached 33.33%, above the
registered ≤25% band. The first run's 18 superseded cells
were invalidated by a defect the program found in its own
first driver (dims 100/120 indexed with the dim-20 word
list). "Headline pattern reproduced" is a weaker criterion
than the frozen one and is never quoted without the two
sentences above.

## 4. Stage 4.2 — the directional clause and the power statement travel together (RT1-34)

The Stage 4.2 outcome record states: "The signal is in the
direction R1 predicts and below the registered bar." S = 4/12
at p = 0.0326 under a registered bar of p < 0.01 AND S ≥ 5 is
a failure of the test. From this record onward, citations of
Stage 4.2 either drop the directional clause or carry the
power statement with it: **power 0.42 at a 0.35 true
correspondence rate (0.50 at 0.50) — a miss of this size is
uninformative, not suggestive.** The verdict lines themselves
(UNDECIDABLE AT THIS POWER; R3 not displaced) were and remain
disciplined; this clause governs the sentence around them.

It is also stated once, here, for the whole Spec 097
sequence: **the program's preregistrations in this spec are
timestamped only by its own repository history.** The entire
sequence executed on a single calendar day, 2026-11-20; every
"frozen before computation" claim rests on intra-day PR
ordering in a self-hosted record. That is disclosed, not
cured, by this sentence.

## 5. Stage 4.2 — framework-dependence stated at the point of citation (RT1-47)

The affiliation test's evidence base is substantially one
scholarly tradition testing itself, and citations of the
Stage 4.2 verdict carry that statement:

- The 182-form vocabulary is drawn from the acquired gold
  lexicon — whose per-entry apparatus is dominated by Rilly's
  own publications — plus Wiktionary. The R1 hypothesis under
  test is Rilly's. The vocabulary leg therefore tests whether
  Rilly-glossed forms skeleton-match attested Nubian/Nara
  forms: a consistency check inside one framework, mitigated
  but not cured by the attested-only comparator rule.
- The formative leg passes by counting formatives whose
  **published NES comparandum in their source apparatus** —
  the gold lexicon's apparatus asserts the comparandum, and
  the leg counts the assertion. (The arithmetic is verified:
  exactly 5 formatives meet both registered criteria.)
- Freeze v2 §3 announced Wikipedia "removed as freeze-grade
  sources." Its scope, on its face, was the Class A and Class
  E anchors. Verified in the Round 1 adjudication by
  recomputation: **33 of the 182 vocabulary entries still
  list "Wikipedia contributors (2026)" among their sources**,
  including forms for concepts 16 (woman: kdi/kadi) and 75
  (water: at/ato/ate) — and 75 water is one of R1's four
  matching concepts. The removal claim is cited only with
  this scope attached. Cleaning the vocabulary's source
  apparatus is a freeze-v3 act, not a citation fix.

## 6. The soreyi score — citation form (RT1-29, RT1-49)

Every citation of soreyi's PARTIALLY SUPPORTED score carries,
in the same sentence, both of the following:

1. **The form was already present in anchor freeze v1**
   (Class B, B1) as the Osiris invocation form — wos "Isis,"
   sorey "Osiris" — glossed by the tradition before Stage 4.3
   existed. The blind test rediscovered a spelling variant of
   the commonest funerary theonym in funerary texts. **The
   result validates a retrieval route, not a reading.** Half
   the candidate register (3 of 6: soreyi, asoreyi, wisi)
   consists of such variants of anchored theonyms; the
   genuinely unanchored family (xolkte) failed outright.
2. **The cap at PARTIALLY SUPPORTED has two recorded
   reasons**, and both are named: (i) the held-out seal is
   procedural and unverifiable by construction (freeze v2
   §6, registered before Stage 4.4 ran); and (ii) the
   candidate reading as generated ("theonym-adjacent cult or
   offering term") is weaker than the fact the blind test
   actually supports — a rationale that appears first in the
   Stage 4.4 record and amounts to capping for a defect of
   Stage 4.3's generation. Summaries quoting only reason (i)
   are incomplete in the program's favour and are not used.

## 7. Corpus counts — reconciliation note (RT1-48)

Three numbers circulate for the acquired corpus. Their bases:

- **652** — rows of the acquired build's inscription index
  (`data/inscriptions.jsonl`), keyed by REM number, with site,
  genre, and source-page provenance (corpus completion record
  §2).
- **368** — distinct texts after the campaign's own
  deduplication of that build on the exact `text` field
  (freeze v2 §1): the basis of the 335 development / 33
  held-out split.
- **396** — the source's own census: "396 inscriptions
  machine-readable under the open license, 327 of them absent
  from the public (Otten) corpus" (completion record §2, §5).
  The "327 absent" figure is denominated on the 396.

**Open item, stated plainly:** no record reconciles the
652-row index against the source's 396-inscription census
(rows vs inscriptions vs cross-source duplicates is nowhere
stated), and that relation is not derivable from the held
records. It stands as an open reconciliation item against the
source's documentation. Every filed number above is cited
with its basis attached.

Related (RT1-33): the campaign's held-out discipline covers
only the 368-text acquired corpus. Freeze v1's split (1,825
of 18,090 mero-corpus lines; 77 of 652 inscriptions) is
superseded by freeze v2 and is never quoted as "the" seal.
The claim that the deposited mero-corpus.txt collapses to
~662 distinct texts rests on an unnamed "independent 2026
account"; the program has not reproduced that measurement,
and freeze v2 does not rely on it (it excludes the file from
the split entirely).

## 8. Stage 4.4 table — the xolkte row confirmed (RT1-56)

The Stage 4.4 outcome table records xolkte with 2 funerary
occurrences in 1 held-out text, against soreyi's 10/10 and
asoreyi's 2/2 pattern. Confirmed from
`records/stage-4-4-results.json` in the Round 1 adjudication:
funerary stratum — occurrences 2, texts_with_form 1. The
figure is correct as computed; two occurrences in one text is
what the run produced. The FAIL verdict is unaffected (below
the 3-text bar either way).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
