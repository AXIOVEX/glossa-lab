# Spec 110 — Revision registration (the revised deliberate-obfuscation battery)

Filed 2026-11-27, after the first battery's control gate FAILED
(`records/control-validation-2026-11-27.md`, PR #810, merge
`4d57d8c9`) and before any revised run. The hypothesis H of the first
registration stands **UNTESTED**; this revision changes the detection
basis where the gate record diagnosed design defects, under the
program's kill-criterion discipline: revise the search design, never
the bar.

Worker worktree `~/.syncyard/worktrees/glossa/spec110-rev-wt-20261127`,
branch `spec-110-revised-battery`, off main `4d57d8c9` (the landing
base is re-checked at landing time; the intake cascade is re-executed
over the merged build if main has moved, and the cascade record says
so on its face).

## 1. What does not change

- The hypothesis H, the four verdict forms (SIGNATURE PRESENT /
  SIGNATURE ABSENT / NOT TESTABLE AT THIS POWER, per corpus per
  family), and the gate-first rule are unchanged. A PRESENT files a
  candidate for adjudication and proclaims nothing about intent.
- No threshold from the first battery is loosened. Carried over
  verbatim: detection at ≥4 of 5 gate corpora; the false-positive
  rule at most 1 fire in the 12-sample panel; invariance at ≥4 of 5;
  stratum nulls at B = 999 draws; the corpus floors (families A, C, D:
  N ≥ 1,000 tokens; family B: at least 2 strata of ≥300 tokens and
  ≥30 texts each); family A's statistics A1–A4 and their registered
  forms; family B in full (statistic, null, genre-baseline rule,
  stratum handling); the transformations T-HOM, T-POLY, T-SUB-D,
  T-SUB-U with their registered constructions; the corpus handling of
  §6 of the first registration (same loaders, same pins).
- Every changed statistic or rule below is re-registered here, with
  its own falsifier (§8), before any run.

## 2. The diagnosis this revision answers

From the first battery's gate record:

- **G-A failed on band construction.** The pooled band mixed Latin
  letter samples (A4 up to 1.8670) with synthetic sign samples and was
  too wide to see anything: T-POLY fired the flattening pattern 5/5
  but the structure pattern 0/5 (replication 1: A3 0.7196 against a
  pooled band maximum of 0.7861; A4 1.6165 against a band minimum of
  0.8578).
- **G-D failed on the statistic.** Splitting the 10 most frequent
  signs does not move hapax-type share; the filed D rule (inventory
  size AND hapax share) fired 0/5 on its own positive control.
- **G-C failed on both legs.** C1 detected T-POLY 0/5 (same band
  defect), and C2 recovered planted permutations at 0.092–0.200
  against the 0.80 bar.
- **G-FP failed for C1.** C1 fired on 2 of 12 natural controls (two
  Latin quarters) against the at-most-1 rule. Family B false-fired
  exactly 1 of 5, within its rule; family B passed its gate outright
  (omnibus JSD 0.2014–0.2788 against null p99 0.0103–0.0113 and a
  genre-baseline maximum of 0.0245).

The precedent survey (filed 2026-11-27, after the first battery) adds
the positive direction for family D: the strongest attested
obfuscation signature in the ancient record is **inventory inflation
with a long rare tail** — the Egyptian cryptographic repertoire grew
from roughly 760 signs to several thousand, most of them rare.

## 3. Development evidence (disclosed; development seeds only)

The revision's design choices were made on development corpora
generated under development seeds (`spec110r-dev*`, disjoint from
every band and gate seed registered in §5), following the program's
G1-E precedent: design on development corpora, disclose, freeze, then
run the gate once on fresh seeds. The development record, in brief:

- **Generator.** A parameterized natural-writing generator at a
  target profile (inventory V0, exact length multiset, optional
  planted site labels), generalizing the Spec 109 Stage 1 recipe:
  opener/closer/context sign classes at 13/13/20% of the inventory, an
  affix pool of 15%, prefix pairs and suffix units, a stem lexicon of
  distinct length-2/3 tuples over the remaining stemvals (targets
  min(C², max(60, 4.6·V0)) and min(C³, max(40, 1.55·V0)) for a core of
  C stemvals), stem weights 1/(i+1)^0.7, collocation preference lists
  of 15 at weight 6.0, opener→stem probability 0.7 — all Stage 1
  constants — with per-site context-role flips and per-site
  stem-weight lognormal perturbation (σ = 0.12). One revision to the
  recipe, made and measured in development round 2: the stemvals are
  two-tier — a core used uniformly for stem building, and a periphery
  (25% of stemvals) substituted into a stem position with probability
  0.10. Round 1's single-tier build produced synthetic corpora whose
  rare tail was far thinner than any real corpus at the same profile
  (Indus-profile hapax-type share 0.025–0.037 against the real
  corpus's 0.2231); the periphery is the generic mechanism that
  produces a rare tail at all. It is a machinery constant, not fitted
  to any target statistic.
- **T-POLY fires the flattening pattern, not the structure pattern,
  at both scoreable profiles** (development rounds 2–3). At the Indus
  profile its A3 fell *below* the band (0.398–0.409 against
  [0.4334, 0.4465]) and its A4 rose above it (4.59–4.73): at period 3
  on positional text, a polyalphabetic mixture leaks position-class
  structure into the corpus bigram statistics instead of destroying
  it. The first battery's structure leg for T-POLY was therefore
  testing a mechanism that does not occur at these profiles; the
  filed gate failure is a design defect, and §4 corrects it.
- **T-SHUF (within-sequence sign permutation) fires the structure
  pattern and C1 cleanly at both profiles** (Indus profile: A3
  0.5536–0.5554 against a band maximum of 0.4483, A4 3.3024–3.3244
  against a band minimum of 4.1068, 3/3; Meroitic profile: A3 0.9942,
  A4 0.0208, 1/1 measured). T-SHUF is the honest structure-destruction
  control: it removes sequential order and keeps composition.
- **Family B's baseline is honest.** With realistic site sizes
  (332–2,070 tokens over 372 signs), the natural omnibus JSD of
  synthetic corpora under planted site splits is 0.133–0.147 —
  profile-estimation noise in small strata, which the
  label-permutation null prices in. T-SUB-D separated decisively in
  every development round (0.369–0.413). Family B needs no change.
- **C2 is at chance under every basis tried.** Summary features
  (first battery): 0.092–0.200. Sorted-bigram signatures: 0.000–0.122.
  Ranked-context signatures (top-24 ranked contexts): 0.000–0.122 at
  minimum count 5, 0.053–0.062 at 10, ≈0 at 20. Ranked-context in the
  split-half geometry: 0.000, 0.000, 0.054. The binding constraint is
  intrinsic: at roughly 1,700–2,100 tokens per stratum over a
  372-sign inventory, per-sign context fingerprints are too sparse to
  identify a permutation. No fourth basis is registered; §4 retires
  C2.
- **Family D candidates under T-HOM.** Inventory V fired at both
  profiles (Indus profile 331–332 against a band maximum of 323;
  Meroitic profile 40–41 against 31). Of the tail candidates, the
  fixed-rank tail mass (the token mass of all types ranked below the
  top floor(V0/2)) fired at both profiles with the healthiest Indus
  margins (0.0872–0.0945 against a band maximum of 0.0832); the
  Lorenz 0.5 fraction fired 3/3 but with a margin of 0.0005 on one
  corpus; hapax-type share and the ≤2-count shares do not move under
  T-HOM (the first battery's defect); types beyond 90% coverage did
  not fire at the Indus profile. §4 registers V and the fixed-rank
  tail, jointly.
- **A filed fragility in family D's tail leg.** On the deciphered
  samples, the real fixed-rank tail mass sits far above the synthetic
  band at every profile measured (Meroitic whole 0.1050 against a
  band maximum of 0.0147; Latin quarters 0.1036–0.1479), while their
  inventories do not exceed their bands (Meroitic V = 31 against a
  band maximum of 31; Latin V = 21–26) — the joint rule's V clause is
  what holds those samples ABSENT. The synthetic model's tail is
  thinner than real writing's at the same profile even with the
  periphery mechanism; the registration files this now so that a
  future D PRESENT is read with it on the record (§7).

## 4. The revised design

### 4.1 Profiles and per-system bands (answers G-A)

For each target system, a **profile**: the corpus's inventory size
V0, its exact sequence-length multiset, and its token count. Bands
are built **per system, from synthetic natural corpora generated at
that system's profile only** — 20 band corpora for the Indus profile
(V0 = 372) and the Meroitic profile (V0 = 31), 12 for the
Eteocypriot profile (V0 = 32), and 12 per Latin quarter (V0 = 26,
each quarter at its own length multiset; Latin is a control, never a
target). For the Indus profile, each synthetic corpus carries the
real corpus's site-label multiset, reshuffled under a registered
seed, so family B's baseline is measured under planted site splits of
the same shape. A band is the min/max interval of a statistic over
the band corpora, as in the first battery; what changes is the
estimator's input — one system's profile, never a pool. No pooled
cross-system band decides any verdict. (The deciphered corpora
themselves are never inside any band; they appear only as
false-positive panel samples, each scored under its own system's
synthetic band — the first registration's leave-target-out falsifier
carries over.)

### 4.2 Family A — statistics unchanged, patterns gated separately

A1–A4 as registered in the first battery. Two patterns, each gated
separately (detection, invariance, false positives):

- **Flattening pattern**: A1 above band AND A2 below band. Its
  registered positive controls are T-HOM and T-POLY (development
  evidence: both produce it at both scoreable profiles).
- **Structure pattern**: A3 above band AND A4 below band. Its
  registered positive control is **T-SHUF** (within-sequence sign
  permutation under a registered seed). T-POLY is filed as *not*
  producing the structure pattern at these profiles, with the
  position-class leakage mechanism of §3 as the reason; the first
  battery's T-POLY structure leg is withdrawn as a design defect,
  not re-barred.

A flattening PRESENT no longer distinguishes homophonic expansion
from polyalphabetic mixing; both are filed among its alternative
explanations (§7).

### 4.3 Family B — unchanged

Carried over in full from the first registration, with its pass on
the record: omnibus token-weighted pairwise JSD over floor-meeting
site strata, the within-length-bin label-permutation null at
B = 999, the genre baseline as the maximum observed omnibus over the
profile's band corpora under their planted splits, PRESENT = observed
above null p99 AND above the baseline maximum. Sequences with no site
label are excluded from family B only, in synthetic and real corpora
alike. Family B is scoreable for the Indus corpus only (Meroitic has
no stratum metadata in its build; Eteocypriot has a single stratum).

### 4.4 Family C — C2 retired, C1 re-registered conditionally

**C2 is retired in this revision**, on the development record of §3:
three matching bases and two geometries all recover planted
permutations at chance at the Indus profile, and the constraint is
intrinsic to the profile's token-per-stratum counts. The claim set
narrows accordingly (claims C110-7..C110-11 carry no substitution-
recovery claim). Retirement is a narrowing, not a loosening: no
verdict family C renders in this revision rests on recovery.

**Family C is C1 alone**: A3 above band OR A4 below band, statistics
and form unchanged. Two registered changes, both corrections of filed
defects: its detection control is T-SHUF (T-POLY does not destroy
corpus bigram structure at these profiles, §3; the first battery's
C1 detection leg measured the pooled band's width, not C1), and its
re-registration is **conditional on its false-positive leg**: C1
renders verdicts only if it fires on at most 1 of the 12 panel
samples (§5). If the leg fails, C1 is not re-registered, family C
closes in this revision, and the gate record says so.

### 4.5 Family D — the inventory-inflation rule (answers G-D)

Family D is re-registered as the joint Egyptian-pattern rule:

- **D1**: observed inventory V above the per-system band maximum.
- **D2**: fixed-rank tail mass — the share of tokens carried by all
  types ranked below the top floor(V0/2) types — above the
  per-system band maximum.
- **Verdict PRESENT requires D1 AND D2.** Either leg alone is filed
  as an excursion, not a verdict: inventory inflation alone is not
  diagnostic (an undeciphered corpus's graphic inventory is partly a
  sign-list editorial fact), and tail mass alone is the filed
  fragility of §3.
- Registered positive control: T-HOM (the homophonic split is the
  mechanism that inflates an inventory with rare variants, as in the
  Egyptian attestation).

The first battery's D statistics (hapax-type share and the ≤2-count
shares) are withdrawn: they do not respond to the family's own
positive control, which the gate record proved.

### 4.6 Transformations

T-HOM, T-POLY, T-SUB-D, T-SUB-U carried over verbatim from the first
registration (same constructions, same seed bases: T-HOM 11001 + i,
T-POLY 11101 + i, T-SUB-D 11301 + i, T-SUB-U 11401 + i, stratum nulls
11001 + i). T-SUB-D's target stratum is the second-largest
floor-meeting stratum of the corpus under test. **T-SHUF** is added:
within each sequence, a seeded permutation of its signs (seed
11501 + i); composition and lengths are preserved exactly, sequential
order is destroyed. The real-corpus family B null uses seed 11999.

### 4.7 Floors and verdict composition

Floors as §1. Per corpus, per family:

- **Family A**: PRESENT if any *scoreable* pattern fires (the pattern
  is named in the verdict); ABSENT if at least one pattern is
  scoreable and none fires; no verdict if neither pattern is
  scoreable at that profile (the gate record carries the failure).
- **Family B**: PRESENT / ABSENT by its unchanged rule when
  scoreable; NOT TESTABLE where the stratum floor fails.
- **Family C**: PRESENT if re-registered C1 fires; ABSENT if
  re-registered C1 does not fire; no verdict if C1 is not
  re-registered.
- **Family D**: PRESENT if scoreable and D1 AND D2 fire; ABSENT if
  scoreable and the joint rule does not fire; no verdict if not
  scoreable.
- Any family whose floor fails files NOT TESTABLE AT THIS POWER.

## 5. The gate (runs first, once, on these seeds)

Band seeds: `spec110r2-band-{ind,mer,ete}-{1..20}` (Eteocypriot
`{1..12}`); `spec110r2-band-latq{q}-{1..12}` per quarter. Indus site
reshuffles: `spec110r2-sites-<corpus-seed>`. Gate corpora:
`spec110r2-ctl-{ind,mer,ete}-{1..5}`. Development seeds are disjoint
from all of these.

Legs, per profile P ∈ {Indus, Meroitic} for the verdict-bearing
families (Eteocypriot legs are run and filed; its verdicts are
floor-blocked regardless):

- **G-A-FLAT(P)**: the flattening pattern fires on T-HOM in ≥4/5 gate
  corpora at P AND on T-POLY in ≥4/5.
- **G-A-STRUCT(P)**: the structure pattern fires on T-SHUF in ≥4/5.
- **G-B**: family B fires on T-SUB-D in ≥4/5 Indus gate corpora (full
  rule: above null p99 AND above the genre-baseline maximum).
- **G-C1(P)**: C1 fires on T-SHUF in ≥4/5.
- **G-D(P)**: the joint D rule fires on T-HOM in ≥4/5.
- **G-INV(P)**: on T-SUB-U, no family A pattern, no C1 clause, and no
  D rule fires, in ≥4/5 (label invariance; family B's statistic is
  invariant under a global permutation by construction).
- **G-FP**: the 12-sample panel — the 5 Indus gate corpora
  untransformed under the Indus band; the 4 real Latin quarters, each
  under its own quarter's band; the real Meroitic corpus whole and in
  two halves (split by sequence order) under the Meroitic band. Each
  pattern/family (flattening, structure, C1, D) must fire on at most
  1 of the 12. **G-FP-B**: family B fires on at most 1 of the 5 Indus
  gate corpora under their planted site splits.

Scoreability at a profile: a pattern/family renders verdicts there
iff its detection leg passed at that profile AND G-INV passed there
AND its G-FP count is ≤1 (family B: G-B AND G-FP-B). A family or
pattern that fails renders no verdict at that profile, and the gate
record says so — per-family, per-pattern gating is this revision's
explicit form of the first battery's gate rule.

## 6. Corpus handling and censuses

Loaders identical to the first registration §6; the five input pins
are re-verified by the harness at run time and filed in its output.
Measured censuses under that handling:

- **Indus** (derivation set): 1,336 sequences, 5,611 tokens, 372
  types, 83 hapax types (share 0.2231); A1 0.7337, A2 0.0841,
  A3 0.5971, A4 2.5245. Floor-meeting site strata (≥300 tokens,
  ≥30 texts): Mohenjo-daro (491 texts / 2,070 tokens), Harappa
  (393 / 1,664), Dholavira (79 / 332), Kalibangan (87 / 376),
  Lothal (91 / 376).
- **Eteocypriot** (primary Amathus): 11 sequences, 54 tokens, 32
  types. Every family's floor fails; NOT TESTABLE AT THIS POWER is
  the expected filing, as the first registration anticipated.
- **Meroitic** (`.` damage marker excluded): 376 sequences, 28,734
  tokens, 31 types, no hapax types; A1 0.8190, A2 0.1561, A3 0.7581,
  A4 0.9817. No stratum metadata: family B NOT TESTABLE.
- **Latin** (Caesar, *De Bello Gallico*; words of ≥2 letters as
  sequences): 23,266 words, 138,328 letters, 26 types; four quarters
  of ≈5,816 words / ≈34.5k tokens. Control only.

## 7. What a PRESENT would and would not establish

The survey's two cautions are part of this registration. **A cipher
device can exist without a secrecy function** (atbash is attested as
a device; a secrecy purpose for it is not supported), and **a secrecy
regime can exist with no textual signature at all** (the Mesopotamian
secrecy colophons restricted knowledge paratextually, with zero
script transformation). An ABSENT therefore never establishes that
no secrecy regime existed, and a PRESENT never establishes intent.
The **uniform-substitution undetectability limit** is restated: a
whole corpus under one fixed substitution is label-equivalent to its
plaintext, and no statistic in this battery can see it; G-INV is the
battery's honesty about its own blind spot.

Per family, the leading alternative explanations are registered in
advance. Flattening PRESENT: homophonic expansion, polyalphabetic
mixing, or a genuinely flat natural distribution the generator's
class structure does not produce. Structure PRESENT: destroyed or
absent sequential constraint — or the corpus's sign sequences not
being fixed-word-like in the generator's stem sense (real words in a
deciphered control, Latin, sit at the top of their band; a corpus
whose texts are not word-repetitions will sit above it), genre and
text-length effects, or editorial sequence construction. Family B
PRESENT: register or scribal-school stratification, diachronic
mixture, or excavation/publication bias, before any per-stratum
substitution reading. Family D PRESENT: the joint inflation pattern
— or sign-list editorial practice (the inventory counts graphic
types, and Indus sign lists are contested across editions), allograph
splitting, or the model-thin tail of §3 combined with a genuinely
rich inventory.

## 8. Claims and falsifiers

The revision's claims are filed as the bundle
`claims-revision.json` (C110-7..C110-11), intaken through the
standard cascade; the first battery's bundle is never amended.

- **C110-7** (design): the revised battery is the test this
  registration specifies. Falsified if any statistic, band, gate leg,
  or verdict is computed otherwise than as registered here, or if any
  threshold carried over in §1 is found loosened.
- **C110-8** (gate-first): the gate of §5 ran before any real corpus
  was scored, on the registered seeds; C1 counts as re-registered
  only under its §4.4 condition. Falsified by a verdict filed from
  any family/pattern/profile whose gate leg failed, or by a gate
  record that postdates an execution record.
- **C110-9 / C110-11** (Indus / Meroitic verdicts): the outcome for
  the corpus is exactly the outcome filed in the revision execution
  record — per-family verdicts where the gate licensed them, the
  gate failure where it did not. Falsified if the independent
  recomputation (TC-110-08) does not reproduce every filed verdict
  from the filed bands and statistics.
- **C110-10** (Eteocypriot): every family files NOT TESTABLE AT THIS
  POWER. Falsified by any other verdict filed for that corpus.

## 9. Machinery

Harness: `records/obfuscation-harness-rev2.py` (single file;
generator, statistics, transformations, gate, execution; raw output
to custody `glossa-custody/spec110-rev/gate-output-rev2.json` and
`raw-output-rev2.json`, with the input pins and the harness's own
SHA-256 filed in the output). Verification: TC-110-06 (package
form), TC-110-07 (gate recomputation from the filed gate output by an
independent statistics implementation), TC-110-08 (execution
recomputation), TC-110-04 and TC-110-05 at the revision close (trace
and kill-criteria evaluation), as filed in `test-cases.md`.
