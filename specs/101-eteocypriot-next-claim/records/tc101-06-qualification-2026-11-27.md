# TC-101-06 — qualification of the closure-exercise claim (2026-11-27)

Filed under Co-scientist Round O, unit O-E-2 (adjudication:
APPLY WITH MODIFICATION), in
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-27-round-o.md`.
The freeze addendum (`records/freeze-addendum-2026-11-27.md`) is
preserved unedited; this record qualifies one of its statements.

## The qualification

The freeze addendum states that the TC-101-06 TOO THIN closure
path "was exercised, not merely read". The filed probe in
`records/freeze-computation.py` does not demonstrate that. The
probe is a constructed dictionary carrying a fixed absent
position-kind label, an instance count looked up with default
zero, a literal `"instantiable": False`, and a literal
`"checker_result"` string describing what the closure branch
returns. No closure routine is invoked on the probe, and none of
the registered effects is observed: no TOO THIN closure, no
NOT TESTED standing, no suppression of scoring, no closure
record. Correctly recognizing that an absent position kind has
zero instances is an instantiability lookup; it is not the
behavioral exercise TC-101-06 (as amended, binding) specifies,
and Spec 107's TC-107-04 incorporates that behavioral
requirement.

**The behavioral coverage gap therefore stands on the record:**
the TOO THIN closure path has not been demonstrated by a filed
execution witness.

## What is not affected

The E-1 study itself. All four registered candidates
instantiated against the intaken census, so the closure path was
never needed for the outcome; nothing is rescored, reopened, or
re-closed by this qualification, and C101-1's NOT SUPPORTED
verdict and the owner's reclassification of its standing are
untouched.

## Closing act (named, not performed here)

An isolated procedure fixture that sends an absent
predicted-position kind through the governing closure procedure
and observes TOO THIN / NOT TESTED with a scoring-call counter
remaining zero. Any such fixture, when performed, is a later
verification and must be filed as one; it will not be evidence
that the historical freeze run performed the exercise.
