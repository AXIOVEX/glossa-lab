# Spec 101 — Floor Derivation, Candidate Bound, Chance
Treatment, TOO THIN Closure, Instantiation Bound, and
Verbatim Exposure Registration (2026-11-22)

**Status: BINDING AMENDMENT, registered 2026-11-22 —
registration/design correction only.** This record
answers Red Team Round 6 findings RT6-H4, RT6-M5,
RT6-M6, and RT6-L6 against the Spec 101 package as
registered earlier the same day. It executes nothing:
Spec 101 remains NOT EXECUTED, no stage is commissioned
by this record, no candidate is registered by it, no
Perna-side state is built or loaded by it, and no
scoring load of any kind is run. It sets no standing,
returns no verdict, and changes no tally. The original
registered text of `spec.md`, `claims.md`, `tasks.md`,
and `test-cases.md` is preserved; this record binds by
the appended amendment sections and dated pointers in
those files, which name this record as the binding
text.

## 1. RT6-H4 — the floor is computed, never chosen

### 1.1 Registered inputs

The floor of a candidate is a mechanical function of
quantities registered before any scoring load, and of
no other quantities:

- **D = 11** — the number of segments in the ICS 196
  development set, from the Spec 096 corpus of record
  (`specs/096-eteocypriot-program/corpus/corpus.json`,
  version 1.1.1, SHA-256 `2954283d…`).
- **f_i** — candidate *i*'s development-set frequency:
  the number of the D development segments whose
  segment-final suffix is candidate *i*'s registered
  sequence, with the occurrences enumerated in the
  candidate registration (task T201).
- **M** — the Perna-side census size for this test:
  the number of segment-final positions in the intaken
  Perna 2019 census of ICS 194/195, registered in the
  freeze addendum at instantiation (task T202) from
  the intaken corpus state's identity record. M is a
  count of positions, not of signs, because candidates
  are counted at segment-final positions.
- **K** — the number of candidates in the registered
  candidate set, bounded in §2 below.

No other input may enter a floor: not the candidate's
observed Perna-side count (unknown at floor time and
barred in any case), not an editor's judgement of
plausibility, and not any outcome of a prior study.

### 1.2 The null

The stated null, fixed here in advance: under the
null, a Perna-side segment-final position carries
candidate *i*'s ending with probability
**p_i = f_i / D**, independently across the M
positions, so the candidate's Perna-side count is
distributed **X_i ~ Binomial(M, p_i)**. The null is a
chance model over positions derived from the
development frequency alone; it asserts nothing about
the language, and it is the only null this study may
use for the chance treatment in §1.4.

### 1.3 The floor derivation rule

Candidate *i*'s occurrence floor is

> **F_i = the smallest integer k ≥ 2 such that
> P(X_i ≥ k) < 0.05 / K, under X_i ~ Binomial(M, p_i),
> with p_i = f_i / D.**

- **Absolute lower bound (RT6-H4(b)).** The search
  starts at k = 2: no candidate's floor may be below
  **2 occurrences**, whatever f_i, M, and K are.
- The set over which the minimum is taken is never
  empty: P(X_i ≥ M + 1) = 0 < 0.05 / K. If the computed
  F_i exceeds M, the floor stands exactly as computed;
  the candidate is then below its floor at scoring by
  construction, and the floor is not lowered to fit
  the census (see also §4).
- Floors may not move at instantiation, or at any
  later point, except by recomputation of this exact
  formula from the registered inputs (§4). A floor
  that is not the value this formula returns from the
  registered inputs is not a floor of this study.

### 1.4 Chance and multiplicity treatment

At the freeze (task T202), for **each** candidate the
freeze addendum registers, beside its floor:

- its chance expectation **E_i = M · p_i** — the
  expected Perna-side count under the §1.2 null; and
- its tail probability **q_i = P(X_i ≥ F_i)** under
  the same null.

The **family-wise chance probability** — the
probability, under the null, that at least one of the
K registered candidates meets its floor by chance —
is registered at the freeze as the union bound

> **Q = Σ_i q_i** (i = 1..K),

which bounds the family-wise probability without any
independence assumption across candidates (candidates
share positions and are not assumed independent). By
§1.3 each q_i < 0.05 / K, so a correctly computed
freeze has Q < 0.05 by construction; the freeze must
nevertheless compute and state Q from the registered
q_i values, and a freeze whose stated Q is at or
above 0.05 is defective and may not proceed to
scoring.

### 1.5 The amended SUPPORTED condition for C101-1

C101-1 is **SUPPORTED** (at postdictive strength,
spec §3.3) only if **both** conjuncts hold:

1. at least one registered candidate's Perna-side
   count, at its registered positions, is at or above
   its §1.3 floor F_i; **and**
2. the freeze's registered family-wise chance
   probability Q (§1.4) is **below 0.05**.

C101-1 is **NOT SUPPORTED** if every registered
candidate is below its floor or absent at scoring —
the claim's registered falsifier, unchanged and still
able to fire: the floors are set at the null's upper
tail, so a development-frequency ending that does not
in fact recur at that rate in the Perna text returns
counts below its floor. A count at or above a floor
with Q at or above 0.05 likewise does not support:
the two conjuncts are independent gates, and meeting
the count gate alone is not support.

## 2. RT6-H4 — the candidate-count bound

The candidate set is capped by a count derived from
the development corpus itself, computed here from the
Spec 096 corpus of record (§1.1) so the cap is a
registered number, not a future choice.

**Derivation.** Enumerate, over the 11 segments of
ICS 196 in the corpus of record, every segment-final
suffix of every length ≥ 1 sign, and count the
distinct suffixes attested at segment-final position
in **at least two** development segments:

| Ending (segment-final) | Development segments | f |
|---|---|---|
| -se | 3 (segments 6, 7, 8 in reading order) | 3 |
| -na | 2 (segments 1, 5) | 2 |
| -i | 2 (segments 3, 4) | 2 |
| -ti | 2 (segments 9, 11) | 2 |

Segment-final suffixes of length ≥ 2 signs: **none**
recurs in two or more segments (every length-2 final
sequence in the 11 segments is attested exactly
once). The distinct recurring endings attested at
least twice are therefore exactly **4**, all of
length 1.

**The bound.** The registered candidate set satisfies
**K ≤ 4**. A registration (task T201) naming more
than 4 candidates, or naming a candidate that is not
a recurring segment-final ending of the development
set under spec §3.1 P-2's mechanical rule, is not a
registration of this study and may not proceed to a
freeze. This bound is also the K that enters §1.3
and §1.4: multiplicity is charged against at most
the 4 endings the development corpus actually
contains, never against a larger set assembled later.

## 3. RT6-M5 — TOO THIN is a closure outcome

**Registration.** **TOO THIN** is registered for this
study as a **study closure outcome, not a verdict**.
If, at the freeze (task T202), a registered
candidate's predicted positions cannot be
instantiated against the intaken census — that is,
the census carries no positions of the kind the
candidate's registration predicts, so the candidate
could only be scored on a weakened or substituted
position set — then:

- the study **closes TOO THIN at its freeze**, in
  Spec 096's floor discipline (a test that cannot be
  instantiated as registered closes at freeze rather
  than being silently weakened — freeze record
  §6 of Spec 096 is the governing precedent); and
- **C101-1 stands NOT TESTED**: it is neither
  SUPPORTED nor NOT SUPPORTED, no candidate of the
  study is scored, and no outcome record may report
  a verdict for C101-1 from a TOO THIN closure.

**Reconciliation with spec §3.2.** Section 3.2's
sentence "There is no third outcome and no partial
credit" governs **verdicts on C101-1 for a study that
reaches scoring**: a scored study returns SUPPORTED
or NOT SUPPORTED and nothing else. TOO THIN is not a
third verdict; it is a closure state that a study
enters at its freeze, before scoring, in which no
verdict exists to return. The two statements govern
different stages and do not conflict; §3.2's own
final sentence already carries the closure ("a
candidate whose positions cannot be instantiated
against the intaken census closes the study as TOO
THIN at its freeze"), and this section fixes its
effect on C101-1 as NOT TESTED.

**Test.** The closure and its effect on C101-1 are
exercised by **TC-101-06** (appended to
`test-cases.md` by this amendment).

## 4. RT6-M6 — the instantiation bound

The instantiation formula is §1.3's rule, stated
there in full; this section bounds who may do what
with it.

- Task **T202 may only apply §1.3 mechanically** to
  the inputs registered at T201 (each candidate's
  sequence, predicted positions, enumerated
  development occurrences and f_i; K) together with
  the one instantiation input the freeze exists to
  supply, M from the intaken census. T202 computes
  F_i, E_i, q_i, and Q; it registers them; it changes
  nothing else.
- **Any other change is a new candidate
  registration.** Altering a candidate's sequence,
  its predicted positions, its enumerated development
  occurrences or f_i, adding or removing a candidate,
  or stating a floor other than §1.3's value, is not
  an instantiation act: it is a new candidate
  registration that re-runs the precedence discipline
  in full — a new registration commit strictly before
  any scoring load of the Perna-side state, with
  TC-101-02 re-executed against the new commit.
- **Test conformance.** TC-101-02 is extended by this
  amendment to check floor **values** (recompute each
  F_i from §1.3 and the registered inputs), not only
  commit order; TC-101-05 is conformed to the same
  recomputation (appended amendment sections in
  `test-cases.md`).

## 5. RT6-L6 — the verbatim exposure statement

The canonical exposure string for this study is the
sentence of `claims.md` C101-2, quoted here
character-for-character inside quotation marks as
**the** canonical string:

> "that Perna 2019's chapter including its printed reading of ICS 194/195 was read in full on 2026-11-22 (OD-9) before any candidate was registered"

Every outcome record of this study carries this
string verbatim (C101-2), and **TC-101-04 is pointed
at this quoted string**: its search target is the
string as quoted in this section (and in the appended
§3.3 amendment section of `spec.md`), not a paraphrase
of it and not a summary assembled from the claim's
surrounding text. A record that states the exposure
in other words has not carried the statement.

## 6. What this amendment does not do

- It registers no candidate, instantiates no floor
  against a real census (M does not exist until a
  commissioned Stage 1 intake builds the Perna-side
  state), and runs no test case. TC-101-06 and the
  extended TC-101-02 / conformed TC-101-05 are
  registered here and executed only when their stage
  is commissioned, like the rest of the package.
- It changes no claim text, no standing, no verdict,
  and no tally, in this package or any other. The
  pointers appended to `claims.md` (at C101-1 and
  C101-2) and to `tasks.md` (at T201 and T202) are
  dated amendment pointers only.
- Spec 096's package, corpus, freeze, and verdicts
  are untouched; the corpus of record is read here
  only to count what §2 counts.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
