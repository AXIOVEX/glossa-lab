# Spec 107 — M-2 Re-registration: the phonotactic battery on its original basis

**Status: REGISTERED 2026-11-27** (on the landing of the
re-registration PR; no scoring run of any kind precedes
that landing). **Scope:** this record re-registers test
M-2 only. It supersedes the basis and calibration-gate
provisions of the cycle-2 registration
(`records/cycle-2-registration-2026-11-27.md` §6) in the
respects stated at §2 below; the battery's design
(§§6.1–6.4 of that registration) is carried over
unchanged. Registration moves no standing, verdict, or
tally in any program.

## 1. Authorization and history

Cycle 2's M-2 stopped at its calibration gate
(`records/m2-outcome-record-2026-11-27.md`, T205): the
registered basis required reconstruction from the pinned
Kovetsky build only, with no Otten byte consumed, while
the filed calibration figures were computed over the
development partition plus the Otten corpus's example
phrases — the gate was unsatisfiable as registered, and
C107-10's falsifier was met in its stop arm. The outcome
record named the two lawful corrections: a Kovetsky-only
basis with freshly computed figures, or a basis that
lawfully includes the example phrases with their custody
restored. A custody search on 2026-11-27 verified the
Otten corpus absent from every custody location.

The owner ruled in the Glossa-Lab chat on 2026-11-27
(11:26 ET): re-acquire the Otten corpus at the pin,
verify against the manifest, restore custody, then
re-register M-2 on its original basis. The restoration
was executed the same day under the owner's further
clearance of 11:33 ET and is filed at
`specs/097-meroitic-reproduction-benchmark/records/custody-restoration-2026-11-27.md`:
the corpus stands in tower custody at
`glossa-custody/spec097/otten-corpus/`, verified 30 of 30
against the step-0 manifest, under the custody terms of
record (owner risk acceptance of 2026-11-20; no licence;
no redistribution; aggregate statistics only). This
re-registration takes the second of the outcome record's
two corrections: the original basis, with its custody
restored.

## 2. What this re-registration changes, and what it does not

Changed, relative to cycle-2 registration §6:

- The basis sentence (§3 below): the example phrases
  enter the basis from the restored Otten custody, not
  from the Kovetsky build, and the "no Otten byte is
  consumed" condition is removed and replaced by the
  custody condition at §3.
- The calibration STOP-gate is replaced by the
  conformance preflight at §4, which administers the
  same four figures as a gate before any battery run,
  in the pattern of the owner's OD-O-1 ruling
  (2026-11-27) for I-2, and adds the custody
  re-verification the restored basis requires.

Not changed: the question; the comparator data and
family sets; the segment and place-class mapping
(§6.1); the five battery items (§6.2); the nulls
(§6.3); the ranges, leans, control, and verdict rule
(§6.4); the contamination statement; the standings
effects. Those provisions govern this re-registration
exactly as filed in the cycle-2 registration, read with
the basis and preflight of §§3–4 below. C107-10 stands
as executed under the cycle-2 registration; this
re-registration intakes a new claim, C107-12 (§6), and
amends no intaken bundle.

## 3. Basis (corrected)

The Meroitic word basis of Spec 097 freeze v2 §4,
reconstructed exactly: the development partition (335
distinct texts) from the pinned Kovetsky build
(inscriptions source at SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`,
source commit
`145af0836c071e7c9796d37d4b36add00d347c8a`), and the
932 distinct example phrases of the per-scholar files
(Millet, Rilly, Kalabsha), which freeze v2 §1 declares
development material, from the Otten & Anastasopoulos
(2025) corpus at pin
`c9158f6865325877112b6b9ceef83b3c80a93c56` as held in
the restored tower custody
(`glossa-custody/spec097/otten-corpus/`), under the
extraction conventions of the filed Stage 4.2 pipeline
(`pipeline-v2.py`, held in campaign custody) including
the freeze's §7 diacritic fold. Per-stratum battery
values are computed over the development texts only,
under M-1's strata (the filed M-1 strata derivation;
Population P partition).

**The 931/932 reconciliation, stated explicitly.** The
step-0 identity record's census counts
`Data/MilletExamples.txt` at 931 data lines. That is a
line count of one file. The freeze's 932 counts the
distinct example phrases across the three per-scholar
files as pipeline-v2's `examples()` constructs the
basis (its filed output records `words_basis: 12863`
over exactly this basis). The two numbers measure
different things and do not conflict; the freeze's
wording governs the basis, and the preflight at §4
tests the basis by its filed figures, not by either
count in isolation.

**Custody condition.** Otten bytes are consumed only
from the restored custody location, only after the
preflight's manifest re-verification (§4, step 1)
passes, and under the custody terms of record: no
Otten byte is committed to this repository, none is
redistributed, and published results carry aggregate
statistics only.

## 4. Conformance preflight (registered gate, OD-O-1 pattern)

Before any battery item is scored:

1. **Custody re-verification.** The Otten custody
   files are re-hashed and checked against the step-0
   manifest (30 files, all must match), and the
   Kovetsky inscriptions source is checked against
   its pin. All hashes are filed in the run record.
2. **Basis reconstruction.** The basis is reconstructed
   exactly as §3 provides, and the reconstruction
   computes: words; word-internal consonant pairs
   separated by exactly one vowel; the same-place
   rate; and the NES reference rate computed on the
   R1 lists as filed.
3. **Figure gate.** All four figures must reproduce
   the filed Stage 4.2 calibration figures — 12,863
   words; 13,406 pairs; same-place rate 0.3152; NES
   reference rate 0.3038, each to 4 decimal places —
   before any battery figure exists. The ASJP
   segment→place-class mapping table is filed in the
   run record before any battery statistic is
   computed, as cycle-2 §6.1 registers.
4. **Failure is the outcome.** If any figure does not
   reproduce, or the custody re-verification fails,
   M-2 STOPS: the preflight failure is filed as the
   leg's outcome, no battery statistic is computed,
   and no basis substitution is made. A preflight
   failure under this re-registration is a new basis
   finding, reported to the owner; it is not corrected
   inside the execution.

## 5. Battery, nulls, verdict, effects

As cycle-2 registration §§6.1–6.4, unchanged: items
SP-CVC (calibration item), LV-CO, ONSET-CC, CODA-C,
LV-TRANS; Null W and Null X (10,000 replicates, seed
20261127); family ranges, leans, the leave-one-out
wrong-family control, split-half description, and the
POSITIVE / NEGATIVE / INDETERMINATE verdict rule. The
contamination statement of cycle-2 §6 stands (Egyptian
loans are not excluded; the basis is the corpus as
filed). Standings effects as registered there:
POSITIVE(F) records phonotactic support for F in the
trace, labelled typological, below Spec 102's gates,
not displacing Spec 097's R3 position; NEGATIVE removes
the phonotactic leg from the program's argument set and
records Rowan's argument as not sustained at battery
standard; INDETERMINATE has no effect. No claim
standing moves under any outcome. M-2 is not the
Spec 102 test: it does not consume Spec 102's gates
G-1 or G-2 and cannot return the affiliation verdict.

## 6. Claim and test case intaken with this re-registration

**C107-12** (M-2 re-registered), carried in the new
bundle file `claims-m2-reregistration.json` (a bundle
once intaken is never amended; `aee-claims.json` and
`claims.json` stand exactly as intaken), with its
falsifier and does-not-establish line in claims.md.
**TC-107-13** (M-2 re-registration execution
conformance) is added to test-cases.md.

**Falsifier (C107-12).** The battery's verdict is not
the mechanical consequence of the re-registered rules
over the filed item values, or the conformance
preflight figures were not reproduced before scoring
and the battery scored anyway, or any Otten byte
consumed came from other than the restored custody at
the pin as verified against the step-0 manifest.

## 7. Execution discipline

Execution on tower-compute only, under
`~/.syncyard/worktrees/glossa/`; every job emits
periodic timestamped progress indicators with countable
work done against total. Raw outputs are saved to dated
files in this package's records; custody bytes are
never committed. Deviations from this re-registration
are recorded as deviations with their reasons in the
outcome record, never silently absorbed.

**AI disclosure:** composed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
