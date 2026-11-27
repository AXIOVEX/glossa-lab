# Spec 093 Stage 4 — T403 contact-context freeze v1

**Frozen 2026-11-27, before the administration under
it.** This freeze states the expectations the
contact-context administration is adjudged against,
the counts that decide them, and the bounds of what
the administration may conclude. Expectations set after
the administration's counts are seen would be a fit,
not a test (C093-4); these are set here, first.

## 1. Entries cited (Stage 3, comparanda register v1)

- **CR-093-01** — Indus-type seals in Mesopotamian find
  contexts; fixed window 2334–1600 BCE.
- **CR-093-02** — the Meluhha documentary record; fixed
  window 2500–1600 BCE.

No other register entry is cited by this administration.

## 2. Inputs (pins)

- `glossa-corpus/indus/sources/contact-zone-rebuilt-2026-10-25/seals_at_mesopotamia.json`
  (14 seal rows).
- `glossa-corpus/indus/sources/contact-zone-rebuilt-2026-10-25/meluhha_tablets.json`
  (1,462 hit rows).
  The files' identities are verified by the
  administration script against the tree at run time and
  stated in the outcome record; the rebuild's provenance
  record (`contact_zone_rebuild_provenance.md`) is the
  mechanism's source, as the register entries state.

## 3. The frozen expectations

Adjudged mechanically by
`tools/spec093/run_stage4_contact.py` from the rows of
the two files (field and period counting over the named
evidence class — no statistic over any population is
computed, and none may be read into the results):

- **E1 (the class is context-bearing).** All 14 seal
  rows carry a non-empty `find_period` as recorded, and
  at least 12 of 14 carry an excavation find spot — a
  `find_spot` value that is a named place, not an
  unprovenanced marker.
- **E2 (deposition outside the Indus region).** At
  least 10 of 14 rows name a find spot outside the
  Indus region: Mesopotamia (Ur, Tell Asmar, Kish), Susa
  / Elam, the Gulf / Dilmun (Failaka, Bahrain sites),
  or the Iranian plateau (Konar Sandal, Jalalabad).
  Lothal is an Indus-region spot and does not count
  toward E2; unprovenanced rows do not count.
- **E3 (the class is inscription-bearing).** At least
  10 of 14 rows carry a recorded `inscription_length`
  of 2 or more with `signs_confidence` other than
  "none".
- **E4 (the documentary record's shape, under
  CR-093-02's window).** Among the 1,462 Meluhha hits:
  the modal recorded period is Ur III, and at least
  1,000 hits carry a recorded period that is exactly
  one of the in-window labels — ED IIIb, ED IIIb
  (with the file's uncertainty mark), Old Akkadian,
  Lagash II, Ur III, Early Old Babylonian, Old
  Babylonian. Compound period labels count as
  out-of-window (a fixed window excludes, or it is not
  a window). E4's expectations are set against the
  rebuild's filed aggregates (`hits_by_period` in the
  same file — the register's grounding, read as
  inventory); the administration recomputes from the
  rows, and a disagreement between the recomputation
  and the filed aggregates is itself a recorded
  outcome, not a number to be averaged.

Each expectation is adjudged MET or NOT MET at its
stated count. The administration's outcome is the four
verdicts and the bounded statement of §4 — there is no
aggregate pass/fail beyond them, and no expectation may
be revised under this freeze after the counts run.

## 4. What the administration licenses, and what it does not

If E1–E3 are met, the licensed statement is: *the 14
excavated seals form an evidence class whose find
contexts are recorded, predominantly outside the Indus
region, over the window CR-093-01 froze; Indus-type
seals were deposited in Mesopotamian, Elamite, Gulf,
and Iranian-plateau contexts in that window.* If E4 is
met, the licensed statement is: *the documentary record
of the contact, inside CR-093-02's frozen window, is
concentrated in the Ur III period.*

Neither statement is a population claim: n=14 is an
evidence class (T403's own bound), the Meluhha counts
describe the surviving textual record as rebuilt, not
trade volume, and the identification of Meluhha with
the Indus world is the mechanism's premise — named in
the register, not proven by this administration. No
reading, sign value, or direction-of-influence claim
beyond deposition is licensed (C093-13).

*This does not establish:* a population claim of any
kind — n=14 is an evidence class, and this task's
record says so on its face. (T403's line, carried
verbatim.)
