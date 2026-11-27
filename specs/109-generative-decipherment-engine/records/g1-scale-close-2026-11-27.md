# Spec 109 — G1 Identifiability-Scale Study Close Record (T103)

**Date:** 2026-11-27. **Scope closed:** the
identifiability-scale study commissioned after the G1
revision's re-preflight failure — the G1-R preflight run
at 2× and 4× corpus scale under a registered amendment,
to decide between information and objective design as
the explanation of the 1× clause (i) failure
(`records/g1-scale-registration-2026-11-27.md` carries
the registration, the scale definition, and the
decision rule; `records/g1-scale-study-2026-11-27.md`
carries the results; this record the test cases, the
kill evaluation, and the part state).

**Outcome: MIXED**, as filed in the study record §5 —
the 2× median crosses the floor (0.807) and the 4×
median falls back below it (0.772); the anatomy changed
character at scale (basin failures in 3 of 10
replications carrying all of the study's stem misses),
while in basin-found replications the 1× plateau
persists. Neither (A) nor (B) is supported in its clean
form; no licensing verdict was issued or could be; the
floor was not moved.

## 1. TC-109-02 — Preflight conformance, re-run in verification form for this study (PASS)

Executed as an independent verification script
(`records/g1-scale-tc109-02-verification.py`) over the
custody corpora and both raw outputs: **PASS, 119/119
checks, payload exit 0** (result JSON in custody,
SHA-256 `16584d85…`). What it establishes, in the test
case's own terms:

- The Stage 1, G1 revision, scale harness, and
  amendment pins in each raw output match the filed
  files; each seed namespace is the registered fresh
  namespace for its scale.
- Each corpus's profile recomputes at its scale
  (artifacts / tokens / counted slots / family 4,000),
  its seed of record matches custody, its two
  ground-truth constructions agree, its distinct count
  and effective scale recompute, and its fallback count
  stands at or above the registered combinatorial floor
  (269k − 529) with length-2 distinct within the 529
  cap.
- Each filed candidate is a permutation of the 60
  values respecting the anchors; its recovery and its
  miss anatomy recompute by the script's own code to
  the filed hits, denominator (57 at every
  replication), and role splits.
- Each candidate's objective and the planted truth's
  objective rescore from the filed assignments under
  the Stage 1 objective construction, and each
  objective gap recomputes.
- Each penalized margin and null 99th percentile
  recomputes from the filed assignment through the
  Stage 1 scorers (agreement per figure, the null's
  999 margins included).
- The summary medians and clause flags recompute from
  the per-replication figures, and the amendment §5
  decision rule, evaluated mechanically over the
  verified summaries, returns MIXED (crossing at 2×
  but not 4×).
- No undeciphered-system output exists in either raw
  output: this study produced none (see §2).

## 2. TC-109-09 — Program invariants (trace executed at landing)

Executed over this landing's diff: the changes are
confined to Spec 109's own records (the amendment
registration, the scale harness, the verification
script, the study record, this close record, the two
raw-output copies), `tasks.md`, the history ledger, and
PROGRAM-STATE. No file of Specs 093, 097, 098, 102, 105,
107, or any other study is touched; no gate is altered;
the claims ledger does not move (the amendment's claim
determination, registration §6: no new claim — the
study asserts no new proposition and is registered
under C109-7's preflight discipline as filed); no
standing, verdict, or tally in any program changed.
Nothing was deposited or published. The trace passes on
the landing's read-back.

## 3. TC-109-10 — Kill criteria evaluated (spec.md §9, under the amendment §7 posture)

1. **Null yield at the frozen bar** — not engaged; it
   binds at Part 1's own stage over its candidates,
   which do not exist while the generator is
   unlicensed.
2. **Preflight failure** — not engaged by this study,
   which issued no licensing verdict. G1-R's fired
   state under this criterion (the G1 revision close)
   stands unchanged: G1 produces no scoreable output
   and Stage 3 remains blocked.
3. **Control failure** — not fired. The shuffle
   control passed at both scales (median 0.175 against
   the bounds 0.404 and 0.386), so the amendment's
   shuffle-void rule was not triggered and no scale's
   figure is void.
4. **Gate dependence** — not engaged.
5. **Integrity tripwire** — no breach. The study's two
   disclosures are on the record: the amendment's
   scale definition carries its two combinatorial
   accommodations in its §2 as registered before any
   verdict run (a development smoke build exposed the
   length-2 cap — a 300k pool target against 529
   possible pairs — before the registration was
   finalized, and the correction was registered, not
   patched silently); and the first launch was stopped
   before any replication completed to add the
   harness's self-pin to the raw outputs, then
   relaunched clean, with no figure from the stopped
   launch used.

**Part 1 state after this study:** OPEN, BLOCKED at
its generator, unchanged. The study closes the
scale question as commissioned — with a MIXED outcome
and its mechanism split quantified (3 of 10 scale
replications basin failures, a search-calibration
phenomenon at scale; 7 of 10 plateau replications, the
1× phenomenon persisting) — and poses the
energy-scale-calibration question for a future
registration. It commissions nothing further.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
