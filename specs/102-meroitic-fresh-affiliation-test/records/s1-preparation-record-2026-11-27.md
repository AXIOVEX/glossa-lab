# Spec 102 — S-1 Preparation Record: Appendix Lexicon Extraction and G-1 Coverage Measurement (2026-11-27)

## 1. What this record is, and what it is not

This is a preparation and measurement record. It measures
whether the S-1 wordlist material now in custody can meet
the affiliation test's registered source gates (spec §3.7),
as far as the material in hand takes that question. It is
not a registration, not a freeze, and not an execution
stage of Spec 102. No test was registered by this work, no
part of the affiliation test was run, and nothing was
scored against any family hypothesis: no Meroitic form was
compared with any comparator form, and no correspondence
was counted anywhere in this preparation. The affiliation
test itself remains **NOT commissioned** and owner-gated,
exactly as the registration leaves it.

## 2. Source and custody

The source measured is the Appendix lexicon of Rilly &
de Voogt 2012, held in the Spec 102 custody home on
tower-compute at
`~/.syncyard/worktrees/glossa/glossa-custody/spec102/rilly-devoogt-2012-appendix-lexicon.pdf`
(286,195 bytes, 42 pages, printed pp. 189–230). Its
SHA-256 was verified before any use in this preparation:
`0a0068de8b7afe787acf33bfa67d67f496b8358b58bee8f47f9280f5f7771199`,
identical to the custody entry of record (acquisition
record §11). The custody terms govern throughout (OD-14
chain, Element 7): the compilation made from the source
is the program's own work over published sources, there
is no redistribution of the lexicon text, and use is
scoring/aggregate only. Every product of this extraction
stays in custody (section 4); this filed record carries
aggregate counts only.

## 3. What the Appendix is, as measured

The Appendix is 200 numbered concept entries, the
numbered sequence verified complete (1–200, no gaps, no
duplicates). Each entry is a concept heading over a
five-column comparison table whose columns are the
North Eastern Sudanic side of the comparison: proto-NES,
Nara, proto-Nubian, proto-Taman, proto-Nyima. **The
Appendix prints no Meroitic form for any of its 200
concepts.** There is no Meroitic column, and a whole-text
search of the 42 pages finds the word "Meroitic" exactly
once, inside a loan note in another language's column,
naming a Meroitic form incidentally; that mention is not
a wordlist entry for Meroitic, and its concept is not an
ASJP concept. The Appendix's own introduction states
what it is: two hundred terms used for the comparison of
the languages within the NES group, with the full
discussion referenced to Rilly (2010: 420–529).

So, in S-1's own terms: the Appendix in custody is the
concept frame and the NES-side apparatus of S-1. The
Meroitic side of S-1 — the forms a scored concept is
defined over (spec §3.2) — is book 1, Rilly 2010, which
is not yet in custody (section 8).

## 4. Extraction and its quality, stated honestly

The extraction ran on tower-compute over the custody
PDF (pdftotext, layout mode), producing a structured
per-entry working file (entry number, printed page,
heading, senses, and the entry's raw text block), a
mapping table, and a coverage summary. All of these,
with the raw text extractions and the extraction script,
are held in the custody prep folder `prep-2026-11-27/`
inside the Spec 102 custody home. No byte of them is
committed in this landing or anywhere else.

Quality accounting:

- **Concept headings: reliable.** All 200 headings were
  recovered and the numbering verified sequential. 29
  headings carry the printed parentheses as
  private-use-area glyph substitutions in the extraction;
  all were normalized mechanically, and after
  normalization no heading is parenthesis-unbalanced.
  The coverage arithmetic of section 6 rests on these
  headings.
- **Entry bodies: not character-reliable.** 199 of the
  200 entry blocks contain extraction-corrupted glyphs:
  diacritic substitution characters throughout, some
  letters and the printed page numbers rendered as
  private-use-area glyphs, and column interleaving where
  multi-line table cells wrap. Cell-level forms in this
  extraction must therefore not be cited at character
  level. Any future digitisation of the NES-side
  apparatus needs a checked transcription pass against
  the page images. This defect does not touch section
  6's arithmetic, which rests on the headings and on
  the absence of Meroitic forms; the absence was
  established by whole-text search, not by parsing
  cells, so cell fidelity cannot manufacture or hide a
  Meroitic form.

## 5. The usability rule, stated before its results

A concept is **usable in principle as a scored concept**
from a source if and only if (a) the source supplies at
least one Meroitic form for it, and (b) the concept maps
to an ASJP concept under the mapping rule below. This is
the preparation form of the registered definition: a
scored concept in Leg A is a concept for which the
digitised S-1 wordlist carries at least one form whose
gloss maps to the ASJP concept (spec §3.2).

Mapping rule, applied mechanically. An entry's senses
are its heading's comma-separated gloss phrases, with
parenthetical qualifiers and cross-references removed
and verb markers stripped. A sense maps to an ASJP
concept if and only if it equals that concept's label
in the program's pinned ASJP `parameters.csv` (the Name
field, or the Concepticon gloss with its own
parenthetical stripped) — **tier 1** — or is one of
three enumerated loose synonyms (many, claw, stone,
reached from the headings' numerous, nail, rock) —
**tier 2**, counted separately and never merged into
tier 1. Six further sense candidates were examined and
excluded under the conservative rule; their would-be
concepts are 8, 49, 67, 79, and 93 (five concepts, six
sense hits). The freeze's own complete mapping table
(spec §3.8) does not exist yet and will supersede this
preparation mapping when a freeze is registered;
nothing here binds it.

## 6. Coverage arithmetic: the Appendix alone

Concept side:

- Entries: **200**. Entries mapping to at least one
  ASJP concept under the rule: **84**.
- Distinct ASJP concepts covered: **82 of 100** —
  **79 at tier 1** (label match) and **3 more at
  tier 2 only** (concepts 10, 45, 77). **2** of the
  covered concepts (24, 63) rest on a non-primary
  sense of their entry only.
- Sensitivity: admitting the six excluded borderline
  senses would raise coverage by at most 5 concepts,
  to 87. They were not admitted.
- The Stage 4.2 twelve, on the concept side: **all 12
  appear** — 12 two, 15 small, 16 woman, 17 man,
  21 dog, 46 foot, 55 eat, 62 kill, 70 give, 72 sun,
  75 water, 97 good (ASJP numbers with the glosses as
  recorded in the Stage 4.2 freeze vocabulary).

Meroitic side:

- Concepts for which the Appendix supplies a Meroitic
  form: **0**.
- Usable in principle from the Appendix alone:
  **0 concepts**. Usable outside the Stage 4.2 twelve
  from the Appendix alone: **0 concepts**.

## 7. G-1 against the Appendix alone

G-1 (spec §3.7) requires the filtered vocabulary to
score at least **40 concepts in each family test**, of
which at least **20 lie outside the Stage 4.2 twelve**
in each test.

**Verdict for the Appendix alone: NOT MET — short by
40 scored concepts in each family test, and short by
20 outside-the-twelve concepts in each test.**

The shortfall is identical for the two tests because
the comparator side binds nothing: both ASJP sets
cover 100 of 100 concepts (spec §2), so per-test
concept sets can differ only through the Meroitic side
and the attestation filter. The shortfall is
structural, not an extraction shortfall: the Appendix
prints no Meroitic forms, and a scored concept is
defined over Meroitic forms. No amount of further work
on this PDF changes the count.

Two parts are **not computable** from the Appendix
alone, with their reasons:

- **The attestation-filtered count.** G-1 is stated
  over the filtered vocabulary (spec §3.2): a form
  enters only if attested as a token in the S-2
  inscription corpus. That computation needs book 1's
  Meroitic forms, which are not in custody; the filter
  can only shrink whatever set book 1 supplies, so no
  filtered count exists yet.
- **G-1 as a gate.** By registration the gate is
  computed at the freeze over the frozen filtered
  vocabulary (TC-102-01 recomputes it there). This
  record's figures are the pre-freeze measurement the
  freeze will recompute from, not the gate itself.

What the Appendix does establish for G-1: it does not
cap the gate below its floor. Its concept frame covers
82 of the 100 ASJP concepts, including all twelve of
the comparability subset. If book 1's digitisation
yields Meroitic forms for at least 40 of those
concepts — at least 20 of them outside the twelve —
that also pass the attestation filter, G-1's
arithmetic is satisfiable from S-1 as acquired.

## 8. What book 1 adds, when it arrives

Book 1 is Rilly 2010, *Le méroïtique et sa famille
linguistique* (Peeters, ISBN 978-90-429-2237-2), print
copy in transit (order reference 6b0851920a66f,
€55.00 total, ordered 2026-11-26; Peeters gave no
delivery date or estimate). Per the acquisition record
(§§3, 11), its load-bearing contents are Chapter III's
comparison of 43 Meroitic words (pp. 59–156), the
Meroitic lexique (pp. 114–147), and the 200-term NES
comparison apparatus (pp. 420–529) — the full
discussion the 2012 Appendix expressly defers to. On
arrival it goes to the same custody home for
digitisation of the lexique and the apparatus under
the registered terms.

That digitisation supplies the missing half of this
measurement: for each of the Appendix's 82 covered
concepts, whether S-1 carries a Meroitic form becomes
determinable, and the pre-filter usable count becomes
computable for the first time. How many of the 82
gain a Meroitic form is not knowable before the
digitisation and is not estimated here. Book 1's
lexique may also carry ASJP-mappable Meroitic glosses
for concepts the Appendix does not head; any such
addition is bounded by the ASJP 100 and is likewise
not countable from the Appendix.

## 9. What G-2 will require, once the concept set is fixed

G-2 (spec §3.7; method at spec §4 as amended
2026-11-22, RT6-M11) was not run in this preparation,
and none of its inputs exists yet. Once the concept
set is fixed at a freeze, the gate requires:

- the frozen filtered vocabulary and the frozen
  comparator lists for each family test — the
  simulation injects over the actual frozen lists;
- the frozen correspondence rule and the primary
  statistic T as registered (spec §3.2);
- the permutation null of T over the frozen lists
  (100,000 permutations), whose 99th percentile is
  the bar a replicate must exceed;
- the registered injection construction: for each
  scored concept independently, designation as
  corresponding with probability θ, and with
  probability d the appending of one comparator form
  built from a Meroitic skeleton of that concept with
  a trailing "a";
- 4,000 replicates per (θ, d) cell;
- a single integer seed registered in the freeze
  before any scoring, from which all simulation
  streams derive deterministically;
- the prospective binomial bound (q0 = 0.1255,
  per-test α ≤ 0.005) stated alongside the simulation.

The gate itself: at least 80% power at θ = 0.30,
d = 0.75 for T in each family test.

## 10. State after this record

S-1 state: book 2's Appendix material is extracted in
custody and measured (concept frame 82 of 100 ASJP
concepts, all twelve of the comparability subset;
Meroitic forms supplied by book 2's Appendix: none,
by the source's own design); book 1's print copy is in
transit, awaiting delivery. G-1 is not met by the
Appendix alone, short by 40 scored concepts and by 20
outside-the-twelve concepts per family test, for the
structural reason stated; the gate itself remains a
freeze-time computation over book 1's digitised
material. The affiliation test remains **NOT
commissioned**; no stage has been executed and nothing
has been scored. No standing, verdict, or tally moved.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
