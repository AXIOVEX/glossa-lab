# Eteocypriot Program — Independent Audit and Rerun of the Frozen A2 Implementation (OD-8)

**Date:** 2026-11-22. **Program:** Spec 096 — Eteocypriot
Program. **Commission:** the owner's act of 2026-11-22
11:41 ET, adopting adjudication item OD-8 (E-6) from
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`:
an independent audit and rerun of the frozen Spec 096 A2
implementation, without retuning. **Standing glossa-lab
clone-processing approval:** owner, 2026-11-22 11:26 ET.

**Scope discipline.** No parameter, threshold, or input was
changed. No verdict is changed by this record. Every
discrepancy found is recorded as a finding and flagged for
adjudication in §5. The audit was executed on tower-compute
in a fresh clone at origin/main `8c2724798aa8e2429c86c63525b3174f633e9274`;
the tip was re-read immediately before this landing.

**Objects audited.** The frozen driver
`records/eteocypriot-e1-driver.py` (SHA-256
`9ec475fd419150e7d07a6a36f3e306eadc62b0427cdb2a4924825870116c9c95`;
one commit in its history, `fee0905e`, the Stages 2–3
landing — the driver is byte-identical to the version that
produced the adjudicated run), its specification (the freeze
record of 2026-11-20 §5, with the preregistration draft of
2026-11-17 §5 as the upstream specification), the frozen
corpus, and the filed run record
`records/eteocypriot-e1-run-2026-11-20.json` (SHA-256
`4a3b4be437baab7d93a148712002ff480d748078cfd859797b3e39ca2b3df63c`).

## 1. The rerun

**1.1 Against the corpus as it stands in the repo, the
frozen driver refuses to run.** The driver's fail-closed
check (driver lines 111–114) compares the corpus file's
SHA-256 against the freeze pin
`5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`.
The corpus file at origin/main hashes to
`2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597`
(15,706 bytes, against the frozen 13,440), and the driver
exits 3 with the refusal. The cause is on the record: the
corpus file was deliberately corrected in three post-run
red-team landings (Round 1, commit `1498ac0a`; Round 2,
`6453d211`; Round 3, `d0047041`) — status, licensing, sense,
and translation fields — under records that state the freeze
pin is not re-set, because it names the executed bytes. The
hash chain verifies end to end: the freeze-commit corpus
(`173882a2`) hashes to the freeze pin exactly, and the
Round 1 corrected file hashes to
`60125fcf42f5091febd7b74b5fb530b93aba8d07e8ed869efa683eb17a609f19`,
exactly the value the ICS 196 custody correction record of
2026-11-21 names for it.

**1.2 The corrections touch no analysis-bearing field.** A
field-level diff of the corpus between the freeze commit and
origin/main shows every difference is metadata: top-level
`corrected`, `version`, `delimitation_of_record`,
`licensing_basis`; ICS 196 `status`, `status_note`, and
`greek_side.sense`; the Androkles records'
`translation_of_record` replaced by `translation_paraphrase`;
ICS 217 and held-out `status_note` / `sealed` fields. The
fields the driver reads are byte-identical in both versions:
ICS 196 `eteocypriot_lines`, the Greek `words`, the
`ground_truth_correspondences`, and the Androkles
`eteocypriot_side` (empty in both).

**1.3 Against the executed bytes, the rerun reproduces the
filed run record byte for byte.** The frozen corpus was
recovered from git history (commit `173882a2`; SHA-256
verified equal to the freeze pin before the run) and the
frozen driver, unmodified, was executed on it on
tower-compute (Python 3.12.3, exit 0). Its output is
byte-identical to `records/eteocypriot-e1-run-2026-11-20.json`
(`diff` empty; both SHA-256
`4a3b4be437baab7d93a148712002ff480d748078cfd859797b3e39ca2b3df63c`).
Every output quantity of the adjudicated run therefore
reproduces exactly, conditional on the executed bytes — see
finding F-2 in §5 for what that condition means for the
reproducibility claim as scoped in C096-4.

## 2. The independent reimplementation

The verdict-bearing quantities were recomputed by a second
implementation written from the freeze record's text alone
(§§2, 3, 5), without consulting the driver source; it is
filed with this record as
`records/eteocypriot-e1-independent-reimplementation-2026-11-22.py`.
Its LCCS is a dynamic-programming computation, a different
algorithm from the driver's brute-force scan. It agrees with
the filed run record on every quantity:

| Quantity | Filed run record | Independent recomputation |
|---|---|---|
| Corpus file SHA-256 | `5077285e…f2dd` (pin) | `5077285e…f2dd` |
| Per-inscription pins (all six, incl. held-out) | freeze §2 table | all six match the freeze §2 table |
| ICS 196 census | 11 segments, 54 signs, 51 legible, 1 restored, 2 damaged | identical |
| Segments (11, reading order) | as filed | identical |
| D(Ἀρίστωνα) | a-ri-si-to-na | a-ri-si-to-na |
| D(Ἀριστώνακτος) | a-ri-si-to-na-ka-to-so | a-ri-si-to-na-ka-to-so |
| LCCS table, Ἀρίστωνα | [1,1,0,0,1,4,1,0,1,1,0] | identical |
| LCCS table, Ἀριστώνακτος | [1,1,0,0,1,4,2,0,1,1,1] | identical |
| A1 recovered | 0 of 2 | 0 of 2 |
| A2 partners | segment 6 (LCCS 4); segment 6 (LCCS 4) | identical |
| A2 recovered | 1 of 2 | 1 of 2 |
| ICS 196 leg passes | false | false |
| Androkles Eteocypriot segments held | 0 and 0 | 0 and 0 |
| P1 passes as registered | false | false |

One qualification, stated plainly: the freeze's rules R1–R3
do not by themselves fix the consonant-stem table (finding
F-4). For the two ground-truth names the derivation is
nevertheless fully determined by R1–R3 plus letter identity:
the only consonants occurring are ρ, σ, τ, ν, κ, whose
Common-syllabary stems are the letter identities r, s, t, n,
k, and every cluster and final in the two names is forced by
R2/R3 as written. The independent derivation therefore does
not borrow the driver's table for any quantity a verdict
rests on. Quantities NOT independently reimplemented: none
that a verdict rests on. The Androkles leg and P1 outputs
are not computations in either implementation (finding F-6).

## 3. What counted as recovery, and what competed (E-6's questions)

Read from the driver (lines 156–183) against freeze §5:

- **Recovery** is exact segment-index identity: the paired
  segment must be the ground-truth correspondent segment. No
  accepted variants, no boundary tolerance, no LCCS threshold
  — LCCS is only the A2 pairing device; both names scored
  A2 LCCS 4 and differ in outcome purely on partner identity.
- **The A2 search space** was all 11 ICS 196 segments for
  each name, exhaustively scored; 11 alternatives competed
  per name. No tie occurred at the maximum for either name
  (each maximum is unique), so the earliest-segment
  tie-break was never exercised.
- **What "unanchored" excluded**, positively stated from the
  code: no name is supplied to the search beyond its derived
  spelling D(name); no window is selected; no segment is
  excluded or weighted; the scoring is raw LCCS length with
  no tuned parameter. Ground truth is read only after the
  segments are loaded, and only into scoring fields.
- **Prior inspection:** nothing in the implementation
  encodes the answers — no hardcoded partner, window, or
  per-name adjustment exists in the driver. Whether the
  run's author had inspected the target locations before the
  run is a historical question code inspection cannot
  settle, and this audit does not settle it; the assessment's
  caution ("not supplied with the answers" does not by
  itself establish a blind test) stands.

## 4. Code against specification — the audit read

The driver implements freeze §5's A1 and A2 as the freeze
writes them. The findings below are the places where code,
freeze, and preregistration diverge from one another, or
where the code's form differs from what a reader of the
specification would expect. Line numbers are the driver's.

- **A1 (lines 165–167)** is a pure index comparison
  (`greek_word_index == segment_index`); no segment content
  is consulted. Already relabelled by amendment 2 §1;
  confirmed here at source.
- **A2 (lines 168–172)** is argmax LCCS over all segments,
  ties to earliest (`scores.index(best)`), exactly as freeze
  §5 states it.
- **Derivation (lines 35–90).** `letters_of` strips
  diacritics to letter identity, maps final sigma to sigma,
  and expands ξ to k+s; `STEMS` (lines 36–40) maps the
  voiced and aspirated consonants onto the voiceless series;
  `derive_cv` (line 71) defaults the R3 dead vowel to "a"
  and tracks the preceding vowel through vowels consumed by
  R2 pairings (lines 77, 83). None of these tables or rules
  appears in freeze §5's R1–R3 (see F-4).
- **Pins (lines 124–128).** The driver computes the
  development records' pins and reports them; it does not
  compare them against the freeze's table. The only
  fail-closed verification is the whole-file hash
  (lines 111–114), which is what freeze §2 specifies; the
  driver's docstring ("verifies each development record's
  per-inscription pin") overstates the code (see F-3).
- **Scope of scoring (lines 156–183).** A1 and A2 are
  computed only for the two ground-truth correspondences.
  The other five Greek words are never derived or scored
  (see F-5).
- **Hardcoded outcomes (lines 191–215).** The Androkles
  leg's `administrable` flags and the P1 block's
  `P1_passes_as_registered: False` are literals, not computed
  results; the segment counts they rest on (0 held) are
  computed from the corpus. This implements freeze §6's
  registered consequence (F-E1b NOT MET, so P1 cannot pass)
  in assertoric form (see F-6).
- **Run-record date (line 147)** is the literal string
  "2026-11-20". The output contains no run-varying field,
  which is part of why byte-identical reproduction is
  achievable at any later date (see F-7).

## 5. Findings, flagged for adjudication

No verdict is changed by this record. The findings are
flagged to the approver with the verdict each touches.

- **F-1 (known deviation, independently confirmed; touches
  C096-1).** A2 as frozen and executed is not the
  preregistration's A2. The preregistration (draft §5)
  defines A2 as name-anchored free alignment — anchored on
  the known name correspondences, otherwise free, unmatched
  material carried as unmatched. Freeze §5 redefines A2 as
  an unanchored argmax-LCCS pairing, and the driver
  implements the freeze. The substitution was recorded only
  after the run (amendment 2 §1). This audit confirms the
  deviation at source in all three documents and adds the
  positive account in §3 of what the executed search was.
- **F-2 (new; touches C096-4's scope, and C096-1's rerun
  mechanics only).** The reproducibility that C096-4's
  adjudicated scope claims for the ICS 196 leg ("run
  byte-identically reproducible") holds against the executed
  bytes, which today exist in the repo only as git history
  (freeze commit `173882a2`); against the corpus file as it
  stands at origin/main, the frozen driver refuses to run
  (§1.1). No output quantity is affected (§1.2, §2), and the
  corrections that caused this were themselves recorded acts
  with the pin deliberately not re-set. But no record before
  this one states that a fresh checkout cannot rerun E1 as
  filed, and the C096-4 scope sentence does not carry the
  condition. Flagged for adjudication: whether the scope
  sentence should be amended to state the condition.
- **F-3 (new, minor; touches no verdict).** The driver's
  docstring claims per-inscription pin verification the code
  does not perform (§4). Freeze §2 specifies only the
  whole-file check, so the code conforms to its
  specification and the docstring alone overstates.
- **F-4 (known, confirmed; touches C096-1's basis).** Freeze
  §5's R1–R3 underdetermine the derivation the driver
  implements: the consonant-stem table, the ξ expansion, the
  diacritic and final-sigma handling, and the dead-vowel
  default appear nowhere in the freeze (amendment 2 §4,
  RT1-22, already binds any future E1 re-run on a freeze
  containing the full table). This audit adds that the
  underdetermination does not reach the two verdict-bearing
  derivations (§2), so it does not disturb the filed numbers.
- **F-5 (new, minor; touches no verdict).** Freeze §5's A2
  sentence reads "each Greek name is paired with the segment
  maximizing LCCS"; the driver scores only the two
  ground-truth names. Recovery is defined only against
  ground truth, and P1's terms concern the correspondences,
  so no quantity changes; the freeze text and the code
  differ in stated scope.
- **F-6 (form finding; touches C096-1's basis as already
  recorded).** P1's failure is asserted by the driver as a
  literal, implementing freeze §6's registered consequence,
  rather than computed. This is the implementation form of
  the fact amendment 2 §2 already states: P1 was unpassable
  before E1 ran. The ICS 196 leg's quantities, by contrast,
  are genuinely computed, and reproduce (§§1–2).
- **F-7 (observation; touches C096-4's scope).** Byte-identical
  reproduction is partly by construction: the run record
  contains no run-varying field (its date is a literal).
  The reproduction in §1.3 is nonetheless a real check of
  every computed quantity, and §2's independent
  recomputation does not depend on it.

## 6. Bottom line

The frozen A2 implementation does what freeze §5 says, the
freeze is not the preregistration's A2 (F-1, already on the
record), and every quantity the adjudicated verdicts rest on
reproduces exactly — by byte-identical rerun on the executed
bytes and by independent recomputation from the freeze text.
The one new material fact is F-2: the executed bytes now
live only in git history, so the run is reproducible
conditionally, not from a fresh checkout as filed. That
finding, and the minor F-3 and F-5, are flagged for
adjudication; this record changes no verdict and no standing.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

---

> **Addendum (2026-11-23, append-only):** finding F-2 of §5
> has been adjudicated by the owner (OD-C-2): the narrowed
> scope sentence of C096-4 IS amended to state the
> executed-bytes condition. The disposition, with the
> original sentence preserved and the amended sentence of
> record, is filed at
> `records/f2-adjudication-record-2026-11-23.md`. F-2
> stands closed. This addendum edits no filed text above.
