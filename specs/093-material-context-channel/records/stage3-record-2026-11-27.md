# Spec 093 Stage 3 — stage record (2026-11-27)

Stage 3 (Comparanda register: T301) executed 2026-11-27
under the owner's commission of 2026-11-27 in the
Glossa-Lab chat ("Yes do all these things now or take my
approval now to do at the best time"), which commissioned
Stages 3–6 of this spec. One task, one artifact, one
mechanical check. No computation of any kind was run
under any register entry by this stage; no claim's
status, stage, or score was changed (C093-13).

## 1. Reconciliation — the commission and the filed record

The filed record carried this spec as closed with
Stages 3–6 uncommissioned: the history ledger's
backfilled state entry (2026-11-25) states "Stages 3-6
of the study were not commissioned on the filed record,"
and the package holds no commission-and-grounding record
for the study (the backfill's GAP entry). Two things
follow, and this record states both rather than papering
over either:

- **The filed spec text is the only authority for what
  the stages are.** Stage 3 below is executed exactly as
  spec.md §2 item 4, plan.md Stage 3, and tasks.md T301
  define it — register v1 seeded per D-093-7, each entry
  carrying the four elements of C093-4, acceptance by the
  four-element gate. Nothing was imported from another
  spec's definitions.
- **The owner's 2026-11-27 commission reopens execution
  of the registered stages; it amends no definition.**
  The earlier "closed" description in the program's
  summaries is superseded as a statement about
  commissioning only: the stages were unexecuted, not
  undefined, and they are now executed in their
  registered order (3, 4, 5, 6) under this commission.

One stale sentence is noted for the reader, not edited:
spec.md's Status line still reads "the study this spec
designs has not been administered in any part," which
Stages 1–2 (executed 2026-11-06 and 2026-11-19/20)
already falsified as a present-tense statement. The
stage records are the operative history; the closeout
record (Stage 6) will state the study's final state.

## 2. T301 — Register v1: DONE

Artifact: `records/comparanda-register-v1.md`. Four
entries, each carrying comparanda set, transmission
mechanism with its source, fixed window, and compared
practice (C093-4):

| entry | set | window (fixed) |
|---|---|---|
| CR-093-01 | the 14 Indus-type seals in Mesopotamian find contexts (`seals_at_mesopotamia.json`) | 2334–1600 BCE |
| CR-093-02 | the Meluhha documentary record (1,462 CDLI hits, `meluhha_tablets.json`) | 2500–1600 BCE |
| CR-093-03 | the Gulf/Dilmun seal population (Laursen Table 1 rebuild, 121 rows) | 2100–1750 BCE |
| CR-093-04 | the receiving culture's written corpora (the catalogue's Sumerian Ur III and Akkadian entries) | 2112–2004 BCE |

Seeding per D-093-7 is total over its named sources:
the check below accounts for all 39 catalogue corpora
exactly once — 2 entered (CR-093-04), 5 the subject
corpus itself (a corpus is not its own comparandum),
32 named in the register's annex as considered and not
entered because no transmission mechanism of record
exists in-repo for them (H2 admits no comparison
without one; each remains admissible by a later
amendment arguing its mechanism from named sources
before any computation under it).

**Acceptance (gate).** `tools/spec093/check_comparanda_register.py`,
run on tower-compute against this landing's tree:

```
comparanda register check: 4 entries (CR-093-01, CR-093-02, CR-093-03, CR-093-04); catalogue census 39 corpora
  CR-093-01: four elements present; mechanism source named
  CR-093-02: four elements present; mechanism source named
  CR-093-03: four elements present; mechanism source named
  CR-093-04: four elements present; mechanism source named
  catalogue accounted: 39/39; double-accounted: 0
RESULT: PASS
```

The check's first run FAILED on 19 unaccounted corpora;
the failures were name-string mismatches (line-wrapped
and shortened forms of the catalogue's exact names), and
the register was corrected to carry the catalogue's
names verbatim, one per line. The check as landed is the
check that passed; the failure and its repair are
recorded here, not hidden.

## 3. What this stage binds downstream

Stage 4's contact-context administration (T403) cites
CR-093-01 and CR-093-02; its freeze states its
expectations under those entries' frozen terms. No
Stage 4 pass is a cross-cultural comparison beyond
T403, and the site and material passes cite no register
entry — stated on their own records' faces, as C093-4's
falsifier requires a reader to be able to check.

*This does not establish:* that the seeded comparisons
are the right ones — only that each was fixed, with its
mechanism, before anything was computed under it.
(T301's line, carried verbatim.)

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
