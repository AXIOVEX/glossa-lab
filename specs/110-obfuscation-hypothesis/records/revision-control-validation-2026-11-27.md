# Spec 110 — Revision control validation (the revised gate)

Filed 2026-11-27. The revised battery's control gate ran **once**,
on the registered seeds, before any real corpus was scored, exactly
as `records/revision-registration-2026-11-27.md` §5 registers it.
Harness: `records/obfuscation-harness-rev2.py`, SHA-256
`c5e319137111ca5fc166e8078352dac97251dcbf6b9c268b69a47ef4c85f911f`;
payload exit 0; elapsed 56.2 s. Raw output in custody:
`glossa-custody/spec110-rev/gate-output-rev2.json`, SHA-256
`53c2af448245003e70f644abbaa949144c5feaa396f4845cc24dfc354d76540c`.
Input pins verified at run time and filed in the output (Indus
derivation `84476daa…`, phase100 `c2b14e94…`, Eteocypriot corpus
`2954283d…`, Meroitic `a8f551e5…`, Latin DBG `84ac8411…` — all five
equal to the first battery's pins).

**Outcome in one line: the gate passed for family A (structure
pattern), family B, and family C (C1) at the Indus profile, and
failed for family A (flattening) and family D at the Indus profile
and for every family at the Meroitic profile (the invariance leg).
Execution proceeded for the scoreable set only
(`records/revision-execution-2026-11-27.md`).**

## Bands (per system; min/max over the band corpora)

| profile | A1 | A2 | A3 | A4 | V | fixed-rank tail |
|---|---|---|---|---|---|---|
| Indus (20) | [0.8837, 0.9002] | [0.0250, 0.0542] | [0.4295, 0.4541] | [4.0246, 4.2679] | [316, 325] | [0.0738, 0.0838] |
| Meroitic (20) | [0.7025, 0.7377] | [0.1206, 0.1729] | [0.8549, 0.9023] | [0.3463, 0.5238] | [28, 31] | [0.0064, 0.0154] |
| Eteocypriot (12) | [0.9051, 0.9571] | [0.1111, 0.2037] | [0.2455, 0.3767] | [2.3451, 2.9995] | [17, 21] | [0.0185, 0.0926] |
| Latin q1–q4 (12 each) | per-quarter bands filed in the raw output | | | | [24–26] | [0.0959, 0.1326] |

Family B genre baseline (Indus profile, observed omnibus JSD of the
20 band corpora under their planted site splits): rows 0.1277–0.1494,
**maximum 0.1494**.

## Legs at the Indus profile

- **G-A-FLAT — FAIL.** Flattening on T-HOM 5/5; on T-POLY **3/5**
  (ctl2, ctl3 did not fire). The pattern is not scoreable at this
  profile; family A renders no flattening verdict on Indus.
- **G-A-STRUCT — PASS.** Structure on T-SHUF **5/5**.
- **G-C1 — PASS.** C1 on T-SHUF **5/5**.
- **G-D — FAIL.** The joint rule on T-HOM **3/5** (ctl2, ctl4 did
  not fire; in both, the inventory leg fell short — the split's V
  gain over a band whose own V spread is [316, 325] is not reliable
  at 4/5). Family D renders no verdict on Indus.
- **G-INV — PASS, 5/5** (no fire on T-SUB-U in any gate corpus).
- **G-B — PASS.** T-SUB-D fired **5/5** (observed omnibus
  0.3305–0.3857 against null p99 0.1593–0.1665 and the baseline
  maximum 0.1494; target stratum Harappa in all five).
- **G-FP-B — PASS, 0/5** (natural omnibus 0.1323–0.1433, each below
  its null p99 0.1466–0.1539 and the baseline maximum).

## Legs at the Meroitic profile — the invariance failure

Detection passed across the board (flattening T-HOM 5/5 and T-POLY
5/5; structure T-SHUF 5/5; C1 5/5; D on T-HOM 5/5). **G-INV FAILED,
3/5 clean**, and under the registered scoreability rule nothing at
this profile is scoreable.

The mechanism is measured, not conjectured. On all five gate
corpora the T-SUB-U statistics are **numerically identical** to the
untransformed statistics (label invariance holds exactly, as it
must). The leg failed because two *untransformed* gate corpora fell
outside the 20-corpus band in the structure direction, and their
identical relabelings therefore "fired" too: ctl1 natural A3 0.9105
against a band maximum of 0.9023 and A4 0.3075 against a band
minimum of 0.3463; ctl2 natural A3 0.9025 against the same maximum
(a miss by 0.0002) and A4 0.3416 against the same minimum. The
Meroitic-profile band, built as registered (min/max over 20
synthetic corpora), is too tight for the generator's own A3/A4
sampling spread at V0 = 31. That is a band-coverage failure priced
into the invariance leg's registered form; the leg is not redefined
after the fact, and the Meroitic corpus renders no A, C, or D
verdict in this revision. A future revision that wants Meroitic
scoreable must register a band estimator with honest coverage at
small inventories in advance.

## Legs at the Eteocypriot profile (filed; verdicts floor-blocked)

Flattening T-HOM 3/5, T-POLY 1/5; structure T-SHUF 1/5; C1 1/5; D on
T-HOM 4/5; invariance 3/5 clean. No leg set passes; no verdicts were
available at this profile in any case (every family's floor fails
at N = 54).

## The false-positive panel (12 samples, each under its own band)

| sample | flat | struct | C1 | D |
|---|---|---|---|---|
| Indus ctl 1–5, untransformed | 0 | 0 | 0 | 0 |
| Latin q1 | – | – | – | – |
| Latin q2 | – | – | **fire** | – |
| Latin q3 | – | – | – | – |
| Latin q4 | – | – | – | – |
| Meroitic whole / half 1 / half 2 | 0 | 0 | 0 | 0 |
| **totals** | **0** | **0** | **1** | **0** |

Every count is within the registered at-most-1 rule. C1's count is
exactly 1 (Latin q2, under its own quarter's band): **C1's
re-registration condition is met, at the rule, not inside it** —
filed so a future reader prices C1's PRESENT accordingly.

## Scoreability (the execution's licence)

| profile | A flat | A struct | B | C1 | D |
|---|---|---|---|---|---|
| Indus | no (G-A-FLAT) | **yes** | **yes** | **yes** | no (G-D) |
| Meroitic | no (G-INV) | no (G-INV) | NOT TESTABLE (no strata) | no (G-INV) | no (G-INV) |
| Eteocypriot | NOT TESTABLE (floors) | | | | |

Independent recomputation: **TC-110-07 PASS** — every band, leg
count, panel count, and outcome in this record reproduces from the
registered seeds by an independent statistics implementation
(`records/tc110-07-08-revision-verification.py`, 43 checks with its
execution section, all passing).
