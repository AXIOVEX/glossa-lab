# Spec 109 — Stage 1 Close Record (T101)

**Date:** 2026-11-27. **Stage closed:** Stage 1 —
the generator conformance preflight (Indus generators;
`records/stage-1-preflight-2026-11-27.md` carries the
results, this record the stage's test cases, kill
evaluation, and part states).

## 1. TC-109-02 — Preflight conformance (run; PASS)

The test case was executed as an independent
verification script
(`records/stage-1-tc109-02-verification.py`) over the
custody corpora and both raw outputs, recomputing
every filed figure rather than reading the harness's
own summary: **PASS, 38/38 checks, payload exit 0**
(result JSON in custody, SHA-256 `d66250fe…`). What
it establishes, in the test case's own terms:

- The synthetic profile matches the filed censuses
  (1,670 artifacts / 7,002 tokens / duplication
  exactly 20/1670 per replication, distinct 1,650).
- Every recovery figure in the preflight record
  recomputes from the custody corpora (positional,
  segmentation, partials, numerical, context, and
  the filed per-replication margins' pass structure),
  and the summary medians recompute from the
  per-replication figures.
- Each generator's filed verdict is the mechanical
  consequence of registration §2's floors over the
  recomputed figures (checked clause by clause,
  including the shuffle-control bounds).
- Clause (iii): the I-2 re-run's medians satisfy
  RIGHT above WRONG and SHUFFLE for both donors, and
  the re-run completed with its verdict block
  (INDETERMINATE, the registered configuration).
- The two-implementation agreement statement covers
  every ground-truth set and every recovery figure
  (harness asserts at computation; this verification
  is the second reading of the filed result).
- The positional limitation is carried on the
  preflight record's face (§4 there), with the
  re-run's own ground-truth sets (1 mark Meroitic,
  0 Latin) as its evidence.
- No undeciphered-system scoring output predates or
  accompanies the preflight record: this stage
  produced none (see §2).

## 2. TC-109-09 — Program invariants (trace executed at landing)

Executed over this stage's landing diff: the changes
are confined to Spec 109's own records (preflight
record, this close record, harness, verification
script, raw-output copy), `tasks.md`, the history
ledger, and PROGRAM-STATE. No file of Specs 093, 097,
098, 102, 105, 107, or any other study is touched; no
gate is altered; no standing, verdict, tally, or
ledger row in any program changed; no claim moved
(the preflight outcome changes no registered claim's
position — C109-2's preflight requirement is what
this stage executed, and its outcome is recorded by
this filing, not by a claims-ledger motion). Nothing
was deposited or published. The trace passes on the
landing's read-back.

## 3. TC-109-10 — Kill criteria evaluated (spec.md §9)

1. **Null yield at the frozen bar** — not fired as a
   part-closing event in this stage; it binds at the
   parts' own stages over their candidate outcomes.
2. **Preflight failure — FIRED, three times.** The
   assignment-search generator (clause i), the
   segmentation family (recovery and control), and
   the recurrent-partial family (control) fail the
   conformance preflight as registered. Each produces
   no scoreable output and no undeciphered run until
   a revised generator passes a preflight under a
   new registration. The floors were not moved.
3. **Control failure — FIRED for the segmentation
   family** (shuffle F1 median 0.443, 78% of its true
   rate — the statistic substantially measures
   itself) **and at the boundary for the partials
   family** (control 0.500 against the required
   < 0.500). The positional and numerical families'
   controls and the context channel's control all
   read 0.000.
4. **Gate dependence** — not engaged in this stage.
   Part 4 remains GATED on Spec 102's G-1, and its
   iconography sub-channel remains gated and unused,
   as registered.
5. **Integrity tripwire** — not fired. No custody
   breach, no gate altered, no undeciphered output
   produced or scored anywhere in the stage.

## 4. Part states after Stage 1

- **Part 1 (assignment search): OPEN, BLOCKED at its
  generator.** Stage 3 does not run until a revised
  search design is registered and passes its own
  preflight. The margin anatomy (preflight record
  §5) is the revision's starting evidence: the
  objective discriminates; the search does not
  reliably find what the objective discriminates.
- **Part 2 (structure induction): OPEN IN PART.**
  Positional classes and the numerical/metrological
  family are licensed for Stage 2. The segmentation
  and recurrent-partial families are closed as filed
  under this preflight; each reopens only through a
  revised design under a new registration.
- **Part 3 (context channel): OPEN, licensed.** Its
  Stage 2 execution proceeds as registered (term
  capped at its own null's 99th percentile,
  no-iconography label, out-of-site validation).
- **Part 4 (gloss induction): GATED** (unchanged;
  Spec 102's G-1).
- **Part 5 (candidate ranking): OPEN** (unchanged;
  its preflight clauses run at Stage 4).

## 5. Custody table (full hashes)

Custody root: tower `glossa-custody/spec109/`
(never committed).

| File | Bytes | SHA-256 |
|---|---|---|
| stage-1-preflight-raw-output.json | 10,876 | dd5fc76dba3e096e336ba24c63d7f1f416ef5c2babdac8189ef9f4f478c8315b |
| i2-rerun-raw-output.json | 86,092 | 526fe7f96f65973766f26e623a1a046ae5ad1fdc8bb87f699dcbf3182f17dfa9 |
| synth-rep1.json | 126,033 | 0752da6236379dd0ad5f1dd7f5e0ec2a8b72d2f19bbe98a04e3b903bd5bdb5c9 |
| synth-rep2.json | 126,520 | f4a78a7063315cfd026f0366c09591b8dc652157d12d9b1728bc893658d3155d |
| synth-rep3.json | 125,876 | c61bb9ec19931a71fcfb4fdda50e3a10c475299ad863257ecfaf7a84a90a51d6 |
| synth-rep4.json | 127,364 | ae78c5ac9a31ba9302c36485ed69355bc14842dac818fa8303c2006c30799d0f |
| synth-rep5.json | 126,451 | 6dc2fc7d292b1aadc992280f7c3b12aad5e7513ea81a53507d01631760c1e46d |
| tc-109-02-result.json | 3,282 | d66250feb26d9c10dbc8af344107c18cf32d00b7e960995a5c56dd5de37c6508 |

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
