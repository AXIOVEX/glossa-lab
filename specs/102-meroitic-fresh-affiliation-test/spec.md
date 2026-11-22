# Spec 102 — Meroitic Fresh Affiliation Test: An Expanded-Wordlist Discriminating Test on New and Independent Material

**Status: REGISTERED 2026-11-22 — NOT EXECUTED.** This
package registers a genuinely fresh discriminating test
of Meroitic affiliation under adjudication item OD-21
(unit M-18). Registration freezes the design, its
material gates, its power profile, and its adjudication
vocabulary. No stage of the study has run: no wordlist
has been acquired or digitised, no vocabulary has been
built, and nothing has been scored. Execution requires
a fresh owner commission; it is not authorized by this
registration.

**Provenance.** The Co-scientist refresh adjudication
of 2026-11-22 (PR #673;
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
unit M-18, asked for a genuinely fresh discriminating
test only after the preceding checks, preferring
securely contextualised new inscriptions, independent
textual groups, or external evidence with distinct
predictions, and instructed that if fresh material is
unavailable the limitation be stated instead of
recycling the consumed holdout. The owner's OD-21 act
of 2026-11-22 13:51 ET commissioned the design and
registration. The preceding checks M-18 names are of
record: the OD-15 power and simulation audit (PR #690),
the OD-16 freeze v2/v3 executable comparison (PR #691),
the OD-17 dependency audit (PR #692), the OD-14 custody
clarification programme and refusal protocol
(PR #689), the OD-19 inspectable packet (PR #694), and
the OD-18 expert-verification preparation (PR #693;
the Rilly letter stands approved for sending by the
owner's separate act and is not part of this spec).

## 1. What this spec is

Stage 4.2 of Spec 097 tested affiliation on a
12-concept slice of the published vocabulary and
returned UNDECIDABLE AT THIS POWER: the R2
(Afroasiatic) failure is informative, the R1
(Nubian/Nara) failure is not — it remains fully
consistent with a moderate affiliation (OD-15 §5).
This spec registers the test that can settle the R1
question at moderate strength, and it is built so
that it cannot produce another uninterpretable
UNDECIDABLE: it is administered only when its
material and power gates are both met, and otherwise
it closes NOT ADMINISTERED with the limitation stated,
exactly as M-18 instructs.

The research question is unchanged from Stage 4.2 —
is Meroitic affiliated with the Nubian/Nara family
(R1), with the Afroasiatic comparator set (R2), or
with neither at detectable strength (R3, recordable
only as not displaced)? What is new is everything the
answer rests on: a Meroitic wordlist source this
program has never held or scored, a concept set at
least three times the size of the executed slice, an
attestation channel Stage 4.2 never used for its
vocabulary tests, and a primary statistic that
extracts graded evidence per concept instead of a
binary match.

## 2. The grounding, as counted at design time

All counts below were executed on tower-compute on
2026-11-22 against the custody holdings, by the
program's own frozen pipeline code
(`pipeline-v2.py`, imported unchanged); the counting
script and its outputs are filed at
`records/design-stage-counts-2026-11-22.md` and
`tools/design_power_sim.py`.

- **The held-material ceiling is 12 concepts.** The
  frozen vocabulary (gold lexicon, CC BY 4.0, plus
  Meroitic Wiktionary, CC BY-SA 4.0) carries 182
  forms, of which 26 carry an ASJP concept, over
  exactly the 12 concepts Stage 4.2 scored (12, 15,
  16, 17, 21, 46, 55, 62, 70, 72, 75, 97). No
  fuller mapping of the held sources yields more:
  the gold lexicon's remaining entries are titles,
  theonyms, toponyms, and kin terms with no ASJP
  concept. Concept-count expansion from held material
  is therefore impossible, and this spec does not
  pretend otherwise.
- **Comparators are not the constraint.** The ASJP
  lists (CC BY 4.0, pins as freeze v2 §4) cover all
  100 concepts for both the R1 set (Old Nubian,
  Nobiin, Dongolawi, Kunuz, Meidob, Nara) and the R2
  set (Coptic, Late Egyptian, Middle Egyptian,
  Akkadian, Biblical Hebrew, Amharic, Hausa).
- **The reconstruction pool is narrow.**
  PROTO_NILE_NUBIAN in ASJP covers 16 concepts (11,
  22, 39, 41, 43, 44, 47, 51, 54, 57, 61, 66, 72,
  75, 82, 100), of which only 72 and 75 intersect
  the scored 12. A reconstruction arm is possible
  only on an expanded Meroitic wordlist (§3.4).
- **The consumed holdout is not reused.** Spec 097's
  33 held-out texts were read by Stage 4.4 and are
  consumed as evidence. Nothing in this spec scores
  them, seals them, or cites them as fresh material.
- **Material no stage has ever scored.** The Otten
  corpus's mero-corpus.txt (662 distinct texts under
  name-masking, per the corpus completion record)
  was excluded from every stage's computation. Its
  authority is unclarified (OD-14 Element 1), so it
  enters this design only as a gated, non-decisive
  leg (§3.5).

## 3. The registered design

### 3.1 Material sources and their authority states

| # | Source | Role in this design | Authority state (OD-14 chain) |
|---|---|---|---|
| S-1 | The fuller published Meroitic wordlist of the scholarly tradition — Rilly 2010, *Le méroïtique et sa famille linguistique*, and the lexicon apparatus of Rilly & de Voogt 2012 — digitised by the program into a new vocabulary | The decisive leg's Meroitic side (§3.2) | Published scholarship, not yet held. Acquisition (purchase or library access) is an owner-gated step, not authorized by this registration. Once digitised, the compilation is the program's own work over published sources, in the gold lexicon's position (Element 2's class), not Otten-derived |
| S-2 | The acquired inscription corpus (Kovetsky build, pin `145af083…`, 396 inscriptions / 368 distinct texts) | Attestation filter for S-1 forms (§3.2) and the split construction of §3.6 | **Clarified**: data CC BY 4.0 over Griffith's public-domain editions (OD-14 Element 2) |
| S-3 | ASJP CLDF lists (pins as freeze v2 §4), attested forms; PROTO_NILE_NUBIAN and PROTO_NUBIAN lists for the §3.4 arm only | Comparators | **Clarified**: CC BY 4.0 |
| S-4 | The gold lexicon (CC BY 4.0) and Meroitic Wiktionary (CC BY-SA 4.0) | The Stage 4.2 twelve, carried as the comparability subset (§3.3) | **Clarified** (OD-14 Element 2's class) |
| S-5 | The Otten corpus, mero-corpus.txt distinct texts only | Gated non-decisive leg (§3.5) | **Unclarified**: no licence; owner risk-acceptance only; permission request of 2026-11-20 unanswered (OD-14 Element 1). The decisive leg does not depend on it in any part |

The decisive leg (Leg A, §3.2) computes only on
S-1 + S-2 + S-3 + S-4, every element clarified or
the program's own compilation of published work.
If S-1's acquisition is refused, unaffordable, or
yields too little, Leg A is not administered (§3.7)
and no substitute source may be quietly introduced
(the OD-14 §4.7 rebuild rule, applied here by
analogy and stated as this spec's own rule).

### 3.2 Leg A — the decisive test

- **Vocabulary.** Every Meroitic form in the
  digitised S-1 wordlist whose gloss maps to an ASJP
  concept under the freeze's complete mapping table
  (§3.8), with spelling variants kept as distinct
  forms (freeze v2 §7's varietas discipline carries
  over unchanged: no spelling normalization; only
  case-folding and the registered diacritic fold).
- **Attestation filter.** A form enters the scored
  vocabulary only if it is attested as a token in
  the S-2 inscription corpus. Forms failing
  attestation are excluded, counted, and listed in
  the freeze. Attestation is a filter, not evidence:
  no held-out or independence claim is made for it,
  and the study's independence rests on the new
  source (S-1), the frozen mapping and rule, and
  the permutation null.
- **Concept sets are per-test.** A concept is scored
  in the R1 test iff the filtered vocabulary carries
  at least one form for it and the R1 comparator set
  carries at least one form for it; likewise for R2.
  The two tests may therefore score different concept
  sets, each with its own denominator, tabled in the
  freeze (§3.8). This replaces Stage 4.2's
  both-sets intersection, which discarded concepts
  for no evidential reason.
- **Primary statistic T.** Per concept, the best
  skeleton score over all Meroitic × comparator form
  pairs: 2 if the pair matches under the frozen
  correspondence rule (first skeleton consonants
  equal, and second consonants equal or either
  skeleton of length 1), 1 if the first consonants
  alone are equal, 0 otherwise. T is the sum over
  the test's concepts. The null is the joint
  permutation null of freeze v2 §4 (comparator forms
  shuffled across concepts, per-concept counts
  preserved, over the test's full comparator pool),
  at 100,000 permutations with the freeze's
  registered seed.
- **Pass bar.** A family test passes iff its
  Holm-adjusted permutation p across the two-test
  family (Leg A's R1 and R2) is below 0.01. The
  Holm treatment is registered here, in advance
  (the OD-17 lesson: Stage 4.2 filed no across-test
  correction, and the audit had to compute it after
  the fact).

### 3.3 Comparability subset

The Stage 4.2 twelve are scored and reported as a
named subset of each test, under both T and the
frozen binary S, so the fresh result can be read
against the executed one without conflating them.
Subset results carry no verdict of their own.

### 3.4 Arm R — the reconstruction arm (non-decisive)

Against PROTO_NILE_NUBIAN and PROTO_NUBIAN, the same
T statistic over the concepts the expanded vocabulary
covers in the proto lists. Registered as
**exploratory, never decisive**, for the dependence
OD-17 D-6 and freeze v2 both state: reconstructions
are built in part from the attested daughters, so
agreement is not independent confirmation. Arm R is
reported separately, is never pooled with Leg A, and
no verdict cites it.

### 3.5 Leg B — the gated Otten leg (non-decisive)

On a filed OD-14 clarification (a grant covering the
use, or an institutional determination), and only
then: the phonotactic rate and formative attestation
statistics of freeze v2 §4, computed over the 662
distinct mero-corpus.txt texts — material no stage
has ever scored. Leg B is supporting evidence only,
is reported with the custody caveat or the
clarification's terms as they stand at execution,
and publishes no Otten-derived text (aggregate
statistics only, per F-6). If no clarification has
landed when Leg A is administered, Leg B is recorded
as NOT ADMINISTERED (custody gate) and Leg A's
verdict stands alone. A refusal triggers OD-14 §4
for the whole program and suspends this spec.

### 3.6 Split independence

Where any stage of this study derives material from
the S-2 corpus (attestation derivation, form
selection checks), the construction is: exact-text
deduplication first, then assignment by
SHA-256(text) mod 10 == 0 under a study-specific
salt registered in the freeze, so no text can fall
on both sides and this study's partition is not
Spec 097's. Derivation work uses the development
side only. Genre stratification follows freeze v2
§2, and the funerary stratum is reported separately
in every corpus-derived table. The seal's nature is
stated as freeze v2 §6 stated it: procedural and
unverifiable by construction, on a public corpus.

### 3.7 Administration gates — the discriminating property

Leg A is administered only if **both** gates pass at
its freeze, computed and filed before any scoring:

- **G-1, material.** The filtered vocabulary scores
  at least **40 concepts** in each family test, of
  which at least **20 concepts lie outside the
  Stage 4.2 twelve** in each test.
- **G-2, power.** The freeze's design-time simulation,
  by the method of §4 (injection over the frozen
  lists, the OD-15 §4 method, with the prospective
  binomial bound of §4 stated alongside), shows at
  least **80% power at θ = 0.30, d = 0.75** for the
  primary statistic T in each family test.

If either gate fails, the study closes **NOT
ADMINISTERED** with the failing gate and the counted
shortfall on the record. A NOT ADMINISTERED closure
is not a verdict on affiliation and may not be cited
as one. No gate may be lowered by amendment after
the freeze; a design that needs lower gates is a new
registration.

### 3.8 Complete tables (the OD-17 / F-A discipline)

The freeze files, in full, before any scoring: the
complete gloss→ASJP-concept mapping table for the
digitised wordlist; the per-concept denominators for
each test (Meroitic forms, comparator forms, and
attesting S-2 texts per concept); and every gloss
label verified against ASJP `parameters.csv` under
its pinned hash (freeze v2 §4) — the check whose
absence produced OD-17's flag F-A against freeze v3
§3. A scoring run that uses any table not in the
freeze, or any label the check rejects, voids the
run (claim C102-4).

## 4. The power profile, on the face of the design

Computed at design time on tower-compute
(2026-11-22; script and outputs in
`records/design-stage-counts-2026-11-22.md`).
Parameterisation as OD-15: θ is the share of scored
concepts carrying a true correspondence, d the
probability the correspondence rule detects it.

**Where the executed design stood (OD-15, of
record).** Binary S at N = 12: minimum detectable
effect at 80% power θ ≈ 0.43 (d = 1.0), 0.57
(d = 0.75), 0.85 (d = 0.5). R1's observed failure
excludes only θ above ≈ 0.55 at perfect detection.

**The primary statistic at the executed size
(design-stage injection, conditional frame).** On
the real Stage 4.2 lists, T for R1 is 9 against a
permutation null mean of 4.50 and a 99th percentile
of 10 (permutation p = 0.0421); for R2, T is 4
against a null mean of 5.08 (p = 0.7623) — the same
asymmetry OD-15 measured, in the new statistic.
Injection power for T at N = 12 (4,000 replicates
per cell): 0.88 at (θ = 0.35, d = 0.75); 0.72 at
(0.35, 0.50); 0.67 at (0.20, 0.75). Minimum
detectable effect at 80% power: **θ ≈ 0.29
(d = 0.75), 0.42 (d = 0.50), 0.22 (d = 1.0)** —
roughly half the binary design's, at the same
N. This frame is conditional on the executed lists
and flatters the design, as OD-15 §4 states of its
own; it is registered as the method G-2 re-runs on
the frozen expanded lists, not as a promise.

**The binary statistic at expanded N (prospective
binomial bound).** With the measured chance rate
q0 = 0.1255 (OD-15 §2) and per-test α ≤ 0.005:
N = 30 → bar S ≥ 10, power 0.52 at (0.30, 0.75);
N = 40 → bar S ≥ 12, power 0.68; N = 50 → bar
S ≥ 14, power 0.78. The independence assumption
makes this the conservative bound; the permutation
tail OD-15 measured is thinner. The expanded test's
decisive statistic is T, whose G-2 simulation on
the actual frozen lists is the operative power
statement; the binomial table is carried so the
binary comparability subset's limits are also on
the face of the design.

**What an outcome will mean, registered in
advance.** If Leg A is administered and R1 passes,
R1 is SUPPORTED at the registered bar. If R1 fails
with G-2 met, the failure excludes θ above the
freeze's computed consistency boundary (the OD-15
§5 construction, recomputed on the frozen lists),
which at the gated power is at or below θ ≈ 0.30
at d = 0.75 — a moderate Nubian/Nara affiliation
would then be excluded, not merely undetected, and
the verdict is R1 NOT SUPPORTED at its registered
bar, with R3 still recordable only as not displaced.
An UNDECIDABLE AT THIS POWER outcome is available
only if the freeze's own power statement, met at
G-2, is falsified by the executed null (a registered
contingency, claim C102-1's falsifier side); the
design's purpose is that this outcome should not
occur, and if it does the record must say why in
numbers.

## 5. Adjudication vocabulary

Per family test: **SUPPORTED** (bar passed) /
**NOT SUPPORTED at its registered bar** (administered,
bar failed, consistency boundary as §4) /
**NOT ADMINISTERED** (a gate failed, or the custody
gate closed Leg B). Program verdict: R1 SUPPORTED /
R2 SUPPORTED / both NOT SUPPORTED with R3 not
displaced / NOT ADMINISTERED. R3 is never recorded
as supported (freeze v2 §5 carries over).

## 6. Hard limits

- No execution under this landing. Every stage in
  `tasks.md` beyond Stage 0 is gated on a fresh
  owner commission; S-1's acquisition is separately
  owner-gated as a purchase/access act.
- No external contact is authorized by this spec.
  The OD-18 expert-verification channel is a
  separate instrument and no question for it is
  registered here.
- Spec 097's freezes, executed bytes, corpus files,
  and adjudicated verdicts are not modified by this
  spec or by any stage of this study.
- No Otten-derived text is published by any stage;
  derived artifacts from Element 1 material remain
  aggregate-only under F-6, and OD-14's refusal
  protocol binds this spec from its adoption.
- No standing is set by registration. Any ledger
  standing change for C102-1..C102-5 remains a
  recorded adjudication by a named human approver.
  Automated actors never approve, verify, or promote.

## 7. Decisions

- **D-102-1 — number.** At the check of 2026-11-22
  the highest landed spec package on origin/main
  was 101 (`specs/101-eteocypriot-next-claim/`); no
  102 directory, branch, or open pull request
  carried 102. This package takes 102.
- **D-102-2 — claims.** C102-1..C102-5 (claims.md)
  are intaken at registration through
  `tools/ledger/import_bundle.py`, the only
  sanctioned path, inside this landing's PR, in the
  Spec 096/098/099/100/101 pattern. Intake sets no
  standing.
- **D-102-3 — program-map placement.** The program
  is entered in
  `glossa-indus/map/program-map-taxonomy.json` under
  Sign inventory & corpus / Signary & corpus models
  — Spec 097's own placement, whose reasoning
  carries over: this study is the Meroitic program's
  next test, not program infrastructure.
- **D-102-4 — the decisive leg rests on new
  material or not at all.** The expanded wordlist
  (S-1) is the design's decisive source because the
  design-time count (§2) proves held material
  cannot expand the concept set. Registering a
  same-material rerun with a stronger statistic as
  the decisive test was considered and rejected:
  it would be a re-analysis of consumed evidence,
  which M-18's instruction against recycling
  forbids in spirit. The stronger statistic is
  registered, but it decides only over the fresh
  vocabulary.
- **D-102-5 — the Otten leg is gated, never
  decisive.** mero-corpus.txt's distinct texts are
  the one large body of Meroitic no stage has
  scored, and their authority is the one
  unclarified element in the OD-14 chain. The
  design therefore names them, gates them on
  clarification, and rests nothing decisive on
  them (§3.5).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
