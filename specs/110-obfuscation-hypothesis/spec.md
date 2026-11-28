# Spec 110 — The Deliberate-Obfuscation Hypothesis:
Distributional Tests for Cipher Signatures in the
Program's Three Scripts

**Status: REGISTERED 2026-11-27 — the hypothesis
registered and its battery executed the same day under
the owner's directive of 2026-11-27 ~19:22 ET in the
Glossa-Lab chat ("entertain the idea that perhaps the
language is obfuscated or encrypted on purpose... Do
not assume this to be the case but leave it a
possibility and add tests for it"), under his standing
blanket approval for Glossa work of 2026-11-27 04:05 ET
and his keep-working directive. The hypothesis is
entertained, not assumed: this spec registers the
tests, validates them on controls before any
real-corpus verdict is scoreable, and files whatever
the tests return. Registration and execution move no
standing, verdict, or tally in any program, and no
outcome of this study is a conclusion about any
script's intent or history.**

**Provenance.** The owner's directive above; the
program's standing discipline as filed in Spec 109
(hypothesis registered with falsifiers before any run;
the OD-O-1 conformance pattern — a battery proves
itself on controls before its output on unknown
material is scoreable; kill-criterion discipline;
ranked outcomes, never proclaimed conclusions) and in
Spec 106's ELSEWHERE framework (world-model templates
exercised against controls before they are read
against the world). The attested ancient precedents
for deliberate cryptographic writing (Egyptian
cryptographic and enigmatic texts; Mesopotamian
scholarly cryptography; acrostic and sign-play
traditions) are surveyed in a companion record filed
with the program's goal workspace the same day
(`obfuscation-precedent-survey-2026-11-27.md`); the
survey informs the signature families of §3 and is
evidence about what deliberate obfuscation has
historically looked like, not evidence about these
three scripts.

## 1. The hypothesis

**H.** Some corpus in the program's care, or some
register or stratum of one, was produced under a
deliberate obfuscation transformation — substitution,
sign-value reassignment, inventory manipulation, or
register-restricted encoding — intended to restrict
comprehension to the knowledgeable and privileged.

H is a hypothesis about production, and this study
tests only its distributional signatures. A signature
present is a candidate finding for adjudication
through the program's existing gates; it is not
evidence of intent by itself, and every PRESENT
verdict in this study's records is filed with the
alternative explanations that could produce the same
signature (genre, register, scribal convention, corpus
composition, damage and edition effects). A signature
absent is a finding about the battery's reach at this
power, stated with its floors.

## 2. What deliberate obfuscation can and cannot leave behind

One mathematical fact governs the battery's design and
is registered on its face. A **uniform monoalphabetic
substitution** applied to a whole corpus permutes sign
labels and therefore leaves every label-invariant
statistic — the frequency profile's shape, all
entropies, bigram mutual information, inventory and
hapax structure — exactly unchanged. No internal
statistic can detect it, in this battery or any other.
What deliberate obfuscation *can* leave behind, and
what the battery tests, is:

- **Homophonic or inventory manipulation** (splitting
  signs, adding dummy or variant signs): flattens the
  frequency distribution and inflates the inventory
  and hapax structure — families A and D.
- **Structure-destroying encipherment** (polyalphabetic
  or position-dependent substitution): degrades bigram
  structure toward independence — families A and C1.
- **Differential obfuscation** (one register, stratum,
  site, or period enciphered while another is not, or
  two strata enciphered differently): a consistent
  non-identity permutation between parts of the corpus
  that natural genre difference does not produce —
  families B and C2. This is the historically attested
  shape: cryptographic registers in the ancient record
  are register-bound, not corpus-wide.

The control gate of §4 demonstrates each direction on
synthetic material, including the negative direction:
the battery must **not** fire on a uniformly
substituted corpus, because nothing can. Any future
claim that a whole corpus is uniformly substituted is
outside this battery's reach by construction, and the
registration says so rather than letting a null result
be misread as a disproof of that class.

## 3. The battery (summary; full registration at records/registration-2026-11-27.md)

Four families, each with registered statistics,
thresholds derived from controls only, permutation
nulls (B = 999, seed 11001), power floors, and a
three-outcome verdict rule (SIGNATURE PRESENT /
SIGNATURE ABSENT / NOT TESTABLE AT THIS POWER):

- **Family A — distribution shape.** Normalized
  unigram entropy, top-sign share, conditional-entropy
  ratio, bigram mutual information, against the
  natural-control band. Two registered cipher patterns:
  flattening (entropy above band, top-share below
  band) and structure destruction (conditional-entropy
  ratio above band, mutual information below band).
- **Family B — stratum asymmetry.** Jensen–Shannon
  divergence between stratum sign profiles (Indus: by
  site; other corpora as their metadata supports),
  against a label-permutation null within length
  strata and against the synthetic genre-baseline band.
- **Family C — substitution structure.** C1: bigram
  structure preservation against the natural band. C2:
  cross-part permutation recovery — signs of one part
  matched to another's by label-free distributional
  features; a stable non-identity permutation with
  alignment gain beyond the natural band is the
  differential-substitution signature.
- **Family D — inventory anomalies.** Inventory size
  and hapax structure at the corpus's token count,
  against size-matched synthetic natural bands.

## 4. The gate (OD-O-1 pattern, mandatory)

No real-corpus verdict of this study is scoreable
until the battery has passed its control validation,
registered in full at the registration record §4:

- **Detection side.** On synthetic natural corpora
  transformed by registered obfuscations (homophonic
  expansion; polyalphabetic substitution; differential
  substitution of one stratum or half), each designated
  family must detect its transformation in at least 4
  of 5 replications.
- **Invariance side.** On the same corpora under a
  uniform substitution, no family may fire in at least
  4 of 5 replications — the battery must respect the
  invariance of §2, not hallucinate a signal.
- **False-positive side.** On untransformed natural
  controls (synthetic replications, the Latin control,
  and the deciphered-script Meroitic corpus in its
  control role), each family may fire on at most 1
  control sample under leave-one-out bands.

If any leg of the gate fails, the battery has failed:
Spec 110 files the failure, the real-corpus runs are
not scoreable, and the study stops there. The battery
is redesigned in a later registration, never tuned on
the real corpora.

## 5. Corpora

- **Indus.** The derivation set of the pinned Spec 105
  custody build (1,336 artifacts, 5,611 tokens,
  M-scheme signs; pin SHA-256 `84476daa…`). The 109
  reserve is not used: its seal belongs to Spec 109
  Part 1's adjudication and this study does not open
  it. Site strata joined from the tracked phase100
  population file (pin `c2b14e94…`) by exact sequence
  match; site-ambiguous sequences are excluded from
  the stratum leg and counted on the record.
- **Eteocypriot.** The Spec 096 corpus of record
  (`specs/096-eteocypriot-program/corpus/corpus.json`,
  SHA-256 `2954283d…`): the primary Amathus
  inscriptions' Eteocypriot lines. The corpus is small
  and single-stratum; the registration's floors are
  expected to return NOT TESTABLE for most families,
  and that outcome is filed as measured, not argued
  around.
- **Meroitic.** The pinned Spec 105 custody build
  (376 texts, 28,734 tokens after the registered
  handling of the `.` damage marker, excluded; pin
  SHA-256 `a8f551e5…`). The build carries no stratum
  metadata, so family B is NOT TESTABLE for Meroitic
  as filed. Meroitic's script is deciphered; the
  corpus also serves, in a separate control role, as
  natural-writing control material for the other two
  corpora's bands, never for its own.
- **Latin control.** Caesar, *De Bello Gallico*
  (custody, Spec 107), word-letter sequences, in four
  quarter samples.

## 6. Verdicts and standing

Verdicts are per corpus per family, mechanical
consequences of the registered rules over the filed
figures. A PRESENT verdict files a **candidate
finding** for adjudication through the program's
existing gates and states, on its face, what else
could produce the signature. No verdict of this study
proclaims obfuscation, intent, a reading, or a
decipherment. No standing, verdict, or tally in any
program moves.

## 7. Kill criteria

1. **Gate failure.** The battery fails any leg of §4's
   control validation. The real-corpus runs are not
   scoreable; the study files the failure and stops.
2. **Control failure in execution.** A family succeeds
   on its scramble or natural control at the strength
   it claims on a target — it has measured itself, and
   the family closes until redesigned and re-registered.
3. **Null discipline.** A PRESENT verdict that does not
   survive its registered null and band checks on
   recomputation is withdrawn in the same landing.
4. **Proclamation breach.** Any record of this study
   presenting a signature as proof of deliberate
   intent, or a candidate finding as a conclusion,
   breaches the registration; the study halts until
   the breach is recorded and corrected.
5. **Integrity tripwire.** Any breach of a custody
   term or of the registration discipline halts the
   study immediately, on the program's standing rule.

## 8. Decisions

- **D-110-1 (number).** At the check of 2026-11-27 the
  highest landed spec package on origin/main was 109;
  no 110 directory or open pull request carried 110.
  This package takes 110.
- **D-110-2 (taxonomy).** Spec 110 sits under Program
  infrastructure / Governance, lifecycle & generated
  layers, with Specs 104, 106, 107, and 109: it is
  program method exercised over the three language
  programs, registered as this study's claims.
- **D-110-3 (no recommendations-ledger row).** The
  study's provenance is the owner's direct directive,
  not a Co-scientist recommendation; as with Specs
  104, 106, 107, and 109, no row is added.
- **D-110-4 (custody).** Run intermediates live in
  custody on tower-compute under
  `glossa-custody/spec110/` and are never committed;
  the filed records carry the pins.
- **D-110-5 (the reserve).** The Indus corpus of this
  study is the derivation set only (D-110-5 in §5);
  the 109 reserve's seal is untouched.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
