# Spec 107 — M-2 Re-registered: Outcome Record (T208)

**Date:** 2026-11-27. **Program:** Spec 107 — Active
Decipherment Loop. **Test:** M-2, the Meroitic phonotactic
battery as re-registered at
`records/m2-re-registration-2026-11-27.md` (PR #799,
merge `24be721e`), battery design carried over unchanged
from the cycle-2 registration
(`records/cycle-2-registration-2026-11-27.md` §§6.1–6.4).

**Outcome: the conformance preflight PASSED in full, the
battery was administered as registered, and the verdict
is INDETERMINATE — 2 of the 5 battery items are scoreable
under the registered denominator floors, below the
registered minimum of 4.** The shortfall is on the
comparator side: the NES (R1) family contributes only 2
qualifying lists on the pair items and on LV-CO, because
four of its six ASJP lists fall below the registered
40-denominator floor on those items. Under the
re-registration's standings effects, INDETERMINATE has
no effect: no claim standing moves, Spec 097's R3
position is untouched, and Spec 102's gates G-1 and G-2
are not consumed. Execution script:
`records/m2-reregistered-execution.py`; raw output:
`records/m2-reregistered-output.json`; mapping table:
`records/m2-reregistered-mapping.json`; run log:
`records/m2-reregistered-run-2026-11-27.log`. All runs
ran on tower-compute; every reported verdict is the
run's own payload verdict (the successful administration
exited 0 after writing its output; §6 records the
attempts that preceded it).

## 1. Conformance preflight (re-registration §4), administered first

Step 1 — custody re-verification, all elements pass:

- **Otten custody:** all 30 files of the restored
  custody (`glossa-custody/spec097/otten-corpus/`)
  re-hashed and checked against the Spec 097 step-0
  manifest: **30 of 30 match** (per-file hashes filed
  in the raw output).
- **Kovetsky pin:** the inscriptions source SHA-256 is
  `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`,
  matching the pin, and the build's HEAD is
  `145af0836c071e7c9796d37d4b36add00d347c8a`, matching
  the registered source commit.
- **ASJP custody:** forms.csv, languages.csv, and
  parameters.csv hashes all match the freeze v2 pins.

Step 2 — basis reconstruction, exactly as §3 provides:
335 development / 33 held-out distinct texts under
freeze v2 §1's rule; **932 distinct example phrases**
from the restored custody's per-scholar files (Millet,
Rilly, Kalabsha) under pipeline-v2's `examples()`
conventions.

Step 3 — figure gate, **PASS** (2026-11-27T19:27:37Z):

| Figure | Filed | Reconstructed | Gate |
|---|---|---|---|
| Words | 12,863 | 12,863 | pass |
| CVC pairs | 13,406 | 13,406 | pass |
| Same-place rate | 0.3152 | 0.3151573922124422 | pass (4 dp) |
| NES reference rate | 0.3038 | 0.3037542662116041 (374 forms, 293 pairs) | pass (4 dp) |

The basis defect that stopped cycle 2's M-2 is closed:
the filed figures reproduce exactly on the original
basis, with the example phrases consumed from the
restored custody at the pin, as the re-registration
provides.

## 2. The battery (cycle-2 §§6.1–6.4, unchanged)

**Mapping table (§6.1).** The ASJP segment→place-class
table was filed at `records/m2-reregistered-mapping.json`
(SHA-256 `06c057352bde8f87…`) at 2026-11-27T19:27:39Z,
before any battery statistic was computed. It covers
every symbol observed in the 13 comparator lists; the
only observed symbol not in the table is `$` (one
occurrence, Amharic), which defaulted to "other" and is
listed as a default in the run record, as §6.1 provides.
The Meroitic-side classes are freeze v2's, verbatim.

**Meroitic pooled values** (basis of 12,863 words):
SP-CVC 0.3152 (13,406 pairs); LV-CO 0.2416 (9,439 words
with ≥ 2 consonants); ONSET-CC 0.3282 (12,863 words);
CODA-C 0.3578 (12,863 words); LV-TRANS 0.0236 (13,406
pairs).

**Family ranges and scoreability** (a list qualifies
for an item iff its own denominator for that item meets
the registered floor of 40; Meroitic's pooled floors
are met on every item):

| Item | R1 (NES) range, lists | R2 (Afroasiatic) range, lists | Scoreable |
|---|---|---|---|
| SP-CVC | [0.2947, 0.2959], 2 | [0.2031, 0.3161], 3 | no — R1 < 3 |
| LV-CO | [0.0988, 0.1184], 2 | [0.0682, 0.1471], 4 | no — R1 < 3 |
| ONSET-CC | [0.0000, 0.0196], 3 | [0.0000, 0.9701], 6 | yes |
| CODA-C | [0.3333, 0.6909], 3 | [0.0336, 1.0000], 6 | yes |
| LV-TRANS | [0.0526, 0.0714], 2 | [0.0593, 0.0781], 3 | no — R1 < 3 |

The R1 shortfall is mechanical: on pair items only
Dongolese Nubian (98 pairs) and Nara (95) reach 40 —
Old Nubian (29), Nobiin (30), Kunuz Nubian (23), and
Meidob Nubian (23) do not; on LV-CO only Dongolese (76)
and Nara (81) reach 40 denominator words. Per-list
values and denominators for all 13 lists are filed in
the raw output.

**Nulls** (10,000 replicates each, seed 20261127;
central 95% of the replicate distribution; the nulls
guard the pooled Meroitic observation, as registered):

- SP-CVC (Null W): central 95% [0.3111, 0.3229];
  observed 0.3152 — **NULL-CONSISTENT**.
- LV-TRANS (Null W): central 95% [0.0362, 0.0415];
  observed 0.0236 — not null-consistent (below).
- LV-CO (Null X): central 95% [0.1830, 0.1949];
  observed 0.2416 — not null-consistent (above).

**Leans and control.** On the two scoreable items,
ONSET-CC leans to R2 (Meroitic 0.3282 lies inside R2's
range and outside R1's) and CODA-C leans to neither
(0.3578 lies inside both ranges): L_R1 = 0, L_R2 = 1.
The leave-one-out wrong-family control over the
scoreable items gives C = 2 (Akkadian and Biblical
Hebrew each lean to R2 on both scoreable items when
scored as targets). Per-stratum values and leans and
the split-half values are filed in the raw output as
description; no stratum value is verdict-bearing here,
because the verdict is reached on scoreability before
leans are counted.

## 3. Verdict

**INDETERMINATE**, on the registered ground: fewer
than 4 items are scoreable (2 of 5). No POSITIVE is
reachable for either family, and NEGATIVE is not
available on this ground — §6.4 reserves NEGATIVE for
administrations with ≥ 4 scoreable items in which
POSITIVE fails for both families. The battery's
discrimination question is therefore not answered at
battery standard by this administration: the
registered floors exclude most of the NES comparator
lists from the pair items and LV-CO, and the design
may not lower its floors inside an execution.

Descriptive findings, filed as description only and
carrying no standings weight: the SP-CVC same-place
rate is null-consistent, agreeing with Spec 097 Stage
4.2's shuffle result (the pooled rate is what
within-word consonant shuffling produces; Rowan's
restriction is not present in the pooled observation);
LV-CO sits above both family ranges and above its
Null X band; LV-TRANS sits below both family ranges
and below its Null W band.

## 4. Falsifier disposition (C107-12)

C107-12's falsifier does not fire, on any of its three
arms: (i) the verdict is the mechanical consequence of
the re-registered rules over the filed item values —
scoreability per §6.4's floors gives 2 scoreable
items, and §6.4's rule returns INDETERMINATE below 4;
(ii) the conformance preflight figures were reproduced
before scoring (gate PASS at 19:27:37Z; the mapping
table was filed at 19:27:39Z; the first battery
statistic follows both in the run log); (iii) every
Otten byte consumed came from the restored custody at
the pin as verified against the step-0 manifest in
this run's own preflight (30 of 30). No ledger act
arises: the re-registration provides that no claim
standing moves under any M-2 outcome, and INDETERMINATE
has no standings effect. C107-10 stands as executed and
was not re-run.

## 5. TC-107-13 (execution conformance) — PASS

(1) The preflight record is filed with the four
figures reproduced and the custody re-verification
(30 of 30) in the same record set, before any battery
figure — §1 above and the raw output. (2) The ASJP
mapping table is filed in the run record and predates
the battery figures (19:27:39Z in the run log). (3)
The verdict recomputes from the filed item values
under the re-registration's rules: §2's scoreability
table and §3. (4) The custody hashes filed in the raw
output match the custody bytes as re-hashed in this
run's preflight, and no Otten byte entered the
repository — the script, the raw output, the mapping
table, and this record carry aggregate statistics only.

## 6. Execution notes and deviations

- **First attempt (19:22Z) crashed** on an internal
  assertion in the execution script: the first
  administration computed the Meroitic pair items over
  segment sequences that compress out non-letter
  characters inside tokens, which diverges from
  pipeline-v2's pair enumeration (13,406 pairs). The
  assertion caught the divergence before any output
  file was written; no statistic from that attempt is
  used anywhere. The script was corrected to
  pipeline-v2's enumeration verbatim (the enumeration
  the preflight and the nulls already used), and the
  leg was re-administered in full, preflight first.
  That re-administration is the run of record.
- **A launch attempt was lost to a connection drop**
  (the transferred script arrived as 0 bytes and was
  detected by hash check before any run; the landed
  script's SHA-256 `c7c8356f3405998e…` was verified
  against the composed source before the run of
  record). The tower route dropped repeatedly during
  this execution; no recovery was improvised.
- **Null implementation:** the nulls are computed with
  a numpy PCG64 generator seeded with the registered
  seed 20261127 (the registration registers the seed
  and the replicate count; the filed central-95%
  bounds make the verdict recomputable from the raw
  output). The central 95% is taken by nearest-rank
  order statistics (the 251st and 9,751st of 10,000
  sorted replicates).
- **Conventions applied, stated for recomputation:**
  comparator list floors are applied to each item's
  own denominator (pairs for pair items; denominator
  words for word items, LV-CO's denominator being
  words with ≥ 2 consonants); control lean counts are
  computed over scoreable items only, with ranges
  recomputed leave-one-out under the same ≥ 3
  qualifying-list rule per item; per-stratum leans use
  ranges only, the nulls guarding the pooled
  observation as registered; Meroitic ONSET-CC and
  CODA-C are computed over the word's letters
  (non-letter characters inside a token are editorial
  marks, not segments), while the pair items use
  pipeline-v2's enumeration over the raw token.
- **Contamination statement (carried over, cycle-2
  §6):** Egyptian loans in Meroitic are not excluded;
  no loan list exists on file to exclude by, and
  constructing one for this test would be an
  unregistered analysis. The basis is the corpus as
  filed, as Stage 4.2 used it.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
