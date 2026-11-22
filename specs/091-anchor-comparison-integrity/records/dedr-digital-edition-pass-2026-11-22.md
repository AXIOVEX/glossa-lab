# DEDR digital-edition pass — 2026-11-22

**Spec:** 091 (anchor comparison integrity). **Commission:**
the F-4 study package, commissioned by the owner in chat
2026-11-22. **Execution venue:** tower-compute. This pass
settles the two numbering questions the record left open: the
M329 entry-4524 tree-vs-print question (register
reconciliation, 2026-11-20) and M044's symmetry clause
(re-verification record, 2026-11-21), which named this exact
instrument: "a pass with the dictionary's own digital
edition, queried by entry number, can close this."

## 1. Instruments

**The tree.** The restored DEDR tree, obtained as the records
make it available: the restore pin's repository
(`github.com/moli-mandala/data` at
`d5050e5a9671012df416e9c474c75aba41c07f8c`) cloned on
tower-compute, and all 15 files of the restored subset
re-verified byte-identical against the restore verification
record (`dedr-restore-verification-2026-11-19.json`) before
any lookup — 15 of 15 SHA-256 matches, including
`dedr_new.csv` at
`fbcc2b2d47c9be24338d846319de2b2c5a2ad4f45451274e3223bc63bc60cae0`
(85,374 rows, 5,623 entries). The mini-server origin tree was
not touched; it remains read-only reference custody.

**The print side, consulted lawfully.** DSAL (Digital
Dictionaries of South Asia, University of Chicago) is the
dictionary's own digital edition of Burrow & Emeneau's *A
Dravidian Etymological Dictionary*, 2nd edition. It is
queried by headword and returns, for each result, the print
entry number and the print page — the two facts every open
question turns on. No print copy was reproduced; entry
numbers, pages and headword glosses are cited as facts.

## 2. Controls — the numbering agrees where it was already verified

Four entries the register reconciliation had verified against
print (its DSAL spot-check set) were re-run through both
instruments:

| entry | headword | tree | DSAL (print no., page) |
|---|---|---|---|
| 7 | akam "inside, house, place…" | 7 | 7, p. 6 |
| 399 | āḷ "man, husband, servant…" | 399 | 399, p. 40 |
| 1651 | kuṭam "waterpot, hub of a wheel" | 1651 | 1651, p. 151 |
| 2814 | cēr "to join, attach, admix…" | 2814 | 2814, p. 248 |

Tree number = print number in all four. A fifth control from
the verified set, 2017 kēḷ "to hear", was **not** re-verified
in this pass: DSAL's headword search returns the homonymous
entry 2018 kēḷ "kindred, friendship" for this form and the
"to hear" entry was not reached by the search forms used. It
is carried from the reconciliation's verified set and stated
as carried, not as re-verified here.

## 3. Question 1 — M329 and entry 4524: settled, no divergence

The reconciliation flagged a numbering-integrity risk: the
program's records cited "DEDR 4524" for M329's basis
(Ta. poṉ "gold") on the strength of a print page (p. 404)
verified under PR #633, while the restored tree's entry 4524
is a different, two-row entry (Ka. bobbaḍe "rind, bark") —
raising the possibility that the tree's numbering diverges
from print in this range.

The pass establishes:

- **Print entry 4524 (DSAL, p. 400)** is Ka. bobbaḍe "rind,
  bark" (with Te. bobbara; cross-reference DED 3697) —
  **identical to the tree's entry 4524**.
- **Print poṉ "gold, metal, iron, wealth, ornament, beauty"
  is entry 4570 (DSAL, p. 404)** — the page PR #633 verified —
  and the tree's entry 4570 is the same entry with the same
  gloss (poṉ; poṉṉaṉ; poṉṉavaṉ; poṉmai…).

**There is no tree-vs-print divergence.** The tree and the
print agree at both numbers. What was wrong was the program's
own filed citation: the entry M329's basis meant is DEDR
**4570**, not 4524. The reconciliation's numbering-integrity
flag is resolved on evidence: the tree's numbering is print's
numbering at every point this pass tested (the four controls,
4524, and 4570). The consequence for M329's basis is stated
as evidence only: its DEDR leg's substance — the poṉ entry,
verified at print p. 404 — stands at the corrected entry
number 4570 in both editions. Any amendment of the filed
citation in the anchors record is a separate act, not this
pass's.

## 4. Question 2 — M044's symmetry clause at entry 1638: settled, not triggered

The re-verification record's clause: the M044 symmetry
objection (its DEDR-1638 leg was struck as unverifiable
because its source chain could not be verified end to end)
would reopen if a *print-verified contradiction of the tree
at 1638* were produced — the test being whether print 1638 is
something other than the tree's kucukucu.

The pass establishes: **print entry 1638 (DSAL, p. 150) is
Ta. kucukucu (-pp-, -tt-) "to whisper" — identical to the
tree's entry 1638.** No print-verified contradiction of the
tree at 1638 exists on this evidence. The clause's condition
is **not met**; the symmetry objection is not reopened by
this pass, and the re-verification record's disposition of
M044 stands undisturbed by it. (As the re-verification
record itself states, the clause concerned the symmetry
objection only; M044's class does not turn on it.)

## 5. Side finding — entry 494 (input to the M267 retest)

Entry 494 was looked up because the M267 retest (filed beside
this record) carries DEDR 494 among its surviving inputs. In
both editions, **entry 494 (DSAL, p. 48) is Ta. il "house,
home, place, wife"** (with illam "house, home"). The anchors
file's citation "DEDR 494 (iṉ locative)" does not match its
named source in either edition, and *iṉ* is not a DEDR
headword (DSAL headword search: no results — it is a suffix,
not a dictionary entry). The finding and its use are the
retest record's; this pass contributes the per-entry
evidence.

## 6. What this pass does not do

It changes no standing and amends no filed citation. It
closes the two questions it was commissioned to settle, on
the evidence tabled above, and it leaves the tree's custody
exactly as it found it: the tower-compute clone is a working
copy of the restore pin, verified against the restore record,
and the mini-server origin tree was never written to.

**Payload verdict: both questions settled — Q1: no
tree-vs-print divergence (print 4524 = tree 4524, bobbaḍe
"rind, bark"; poṉ is entry 4570 in print and tree alike; the
filed citation number was the program's error). Q2: the
symmetry clause is not triggered (print 1638 = tree 1638,
kucukucu "to whisper"). Controls 4 of 4 re-verified identical;
one control (2017) carried, not re-verified, and stated as
such.**
