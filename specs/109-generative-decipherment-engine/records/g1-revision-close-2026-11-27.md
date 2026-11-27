# Spec 109 — G1 Revision Close Record (T102)

**Date:** 2026-11-27. **Scope closed:** the G1 revision
commissioned by the Stage 1 close — a revised
assignment-search generator registered under a new
registration, re-preflighted at the same floors on fresh
corpora (`records/g1-revision-registration-2026-11-27.md`
carries the registration and the diagnosis;
`records/g1-revision-preflight-2026-11-27.md` carries
the results; this record the test cases, the kill
evaluation, and the part state).

## 1. TC-109-02 — Preflight conformance, re-run for this generator (PASS)

Executed as an independent verification script
(`records/g1-revision-tc109-02-verification.py`) over
the custody corpora and the raw output: **PASS, 45/45
checks, payload exit 0** (result JSON in custody,
SHA-256 `a69a51e0…`). What it establishes, in the test
case's own terms:

- The Stage 1 harness pin in the raw output matches the
  filed Stage 1 harness; the seed namespace is the
  registered fresh namespace.
- Each fresh corpus's profile recomputes (1,670
  artifacts / 7,002 tokens / 1,650 distinct), its seed
  of record matches custody, and its two ground-truth
  constructions agree.
- Each filed candidate is a permutation of the 60 values
  respecting the anchors, is the filed best polished
  state, and its recovery recomputes by the script's own
  code to the filed hits and denominator (36/39/46/42/44
  of 57).
- Each candidate's objective rescores from its filed
  assignment to the filed ensemble figure, and each
  penalized margin and null 99th percentile recomputes
  from the filed assignment through the Stage 1 scorers
  (agreement per figure, the null's 999 margins
  included).
- The summary medians recompute from the per-replication
  figures, and the filed verdict (FAILED, clause (i)) is
  the mechanical consequence of registration §2's floors
  over the recomputed figures.
- No undeciphered-system output exists in the run's raw
  output: this stage produced none (see §2).

## 2. TC-109-09 — Program invariants (trace executed at landing)

Executed over this landing's diff: the changes are
confined to Spec 109's own records (the amendment
registration, the revision harness, the verification
script, the preflight record, this close record, the
raw-output copy), `tasks.md`, the history ledger, and
PROGRAM-STATE. No file of Specs 093, 097, 098, 102, 105,
107, or any other study is touched; no gate is altered;
the claims ledger does not move (the amendment's claim
determination, registration §6: no new claim, the claims
as filed already carrying the revised-generator pattern
under C109-7); no standing, verdict, or tally in any
program changed. Nothing was deposited or published.
The trace passes on the landing's read-back.

## 3. TC-109-10 — Kill criteria evaluated (spec.md §9)

1. **Null yield at the frozen bar** — not engaged by
   this stage; it binds at Part 1's own stage over its
   candidates, which do not exist while the generator
   is unlicensed.
2. **Preflight failure — FIRED for G1-R.** The revised
   generator fails clause (i) of its re-preflight
   (median recovery 0.737 at the 0.80 floor). It
   produces no scoreable output. The amendment
   commissions no second revision; a further revision
   is a new commission under a new registration, on the
   evidence this record and the preflight record file
   (the binding constraint is the objective's plateau
   at this profile, not basin-finding, which the
   revision repaired). The floor was not moved.
3. **Control failure** — not fired. The shuffle control
   passed (median 0.175 against the bound 0.368), and
   clause (ii) passed 5/5: the pipeline does not
   measure itself, and what it returns on real structure
   is discriminated by ~990 nats; it is the per-sign
   recovery of edge values that the objective does not
   identify at this scale.
4. **Gate dependence** — not engaged in this stage.
5. **Integrity tripwire** — not fired. No custody
   breach, no gate altered, no undeciphered output
   produced or scored, no floor moved, and the design
   was frozen on the diagnosis before any fresh corpus
   was built (the development findings, including the
   two refinement forms evaluated and set aside, are
   filed at the amendment registration §2).

## 4. Part state after the revision

- **Part 1 (assignment search): OPEN, BLOCKED at its
  generator** — unchanged from the Stage 1 close, now
  with two failed preflights on the record (the filed
  search, clause (i) at median 0.772; the revised
  search G1-R, clause (i) at median 0.737 over its fresh
  draw, with the basin defect repaired and the plateau
  identified as the binding constraint). Stage 3 does
  not run until a generator passes a preflight under a
  new registration, on a new commission.
- Parts 2–5: untouched by this stage; their states
  stand as the Stage 1 close filed them.

## 5. Custody table (full hashes)

Custody root: tower `glossa-custody/spec109/g1-revision/`
(never committed).

| File | Bytes | SHA-256 |
|---|---|---|
| run/raw-output.json | 16,377 | a8209ce0533f82e3df6017711f0c65dffed000a065bbe0708bcbc8c3dd1b3b71 |
| run/tc-109-02-result.json | 4,640 | a69a51e06eaf3dc18ef4b889447c0222d74665b653ec7529321a479d6601ae82 |
| run/synth-rep1.json | — | d8e205d171be5753df4b2730751294f2fe5968cc4da0166b82851703ef3f0abf |
| run/synth-rep2.json | — | 8dd2d2c775f0a43f37bbbf054bcd066266233a2249fbb1c2ec61cf6988f4ad8e |
| run/synth-rep3.json | — | f6500fe57d28e3cd0f7fd4788e98d4218be99055b448a6b480983dd1f4591dc8 |
| run/synth-rep4.json | — | 4ecdc95838eec8f1ee6bfe152122790dcfa7dafd0b580c419b19c9bc8eb2d9c6 |
| run/synth-rep5.json | — | 839a05246ea069f9eda52202bbd879a01fa2e3464cc7fdadbba9c01bfbbf653d |
| diag-output.json | — | 74616f3d68f1ff82e0541c2439ff21309e2ab7225d96fd4d944bf1b7ed8548bd |
| diag2-output.json | — | 5c40a4eeffacd4804f6d61462f09453b4b2dc29e15ae1ab18122800667ed24d8 |

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
