# Spec 100 — Round 7 correction execution record (RT7-L1)

**Date: 2026-11-23. Authority: Red Team Round 7,
finding RT7-L1.** Round 7 confirmed at the payload
(its case E) that `gate_record_check`'s `Permission
basis:` check was keyword matching: the sentence
"Permission basis: Miller grants nothing in this
reply." contains a granting term and no refusal term,
and the gate opened.

## The change

`tools/motif_rerun.py`, check (d) only: a basis line
bearing any negation (NEGATION_RE: nothing / not /
no / never / none / nobody / n't) is refused, even
when it also contains a granting term. The gate fails
closed; an unqualified grant line carries no
negation. Checks (a)–(c), the refusal-term check, the
granting-term check, and every other behaviour are
unchanged. New test case TC-100-10 in `test-cases.md`,
implemented as `test_tc100_10_negated_grant_refused`.

## Payload verdicts (run 2026-11-23, worker clone at
base `78e32fcf` plus this correction)

| Run | Result |
|---|---|
| Full TC-100 suite (`pytest specs/100-motif-claims-rerun/tests/ -q`) | **11 passed, exit 0** (the 10 prior tests plus TC-100-10; the grant legs of TC-100-07 / TC-100-09 still open the gate on an unqualified grant line, exit 0) |
| Case A — record mode, real tree, no deposit | **GATE CLOSED, exit 3** — the gate still refuses today's real state |
| Case E — fixture deposit at the registered path, true SHA-256, basis "Miller grants nothing in this reply." | **GATE CLOSED, exit 3** — "'Permission basis:' line bears a negation, not an unqualified grant" (before this correction this case opened the gate) |

No standing, verdict, or tally changes. Execution of
the study remains gated on Miller's reply, which has
not come.
