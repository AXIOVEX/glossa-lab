# Spec 111 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. TC-111-01 is the
registration acceptance test; the remaining test cases
execute with the evaluation in this landing and their
results are filed here and in the evaluation record.

**TC-111-01 — Package form (C111-1; Stage 0).**
Parse the package's bundle file (aee-claims.json);
compare its claim ids and order against claims.md;
check every claim for a falsifier and a
does-not-establish line; check that spec.md §1 states
the hypothesis, §2 the four predictions, §3 the
grading rule, §4 the two evidence legs, and §6 the
kill criteria; check that the evaluation record
carries a grade for each prediction with its decisive
evidence cited.
*Pass:* the ids and order are equal (C111-1..C111-8);
every claim carries both lines; the hypothesis, the
four predictions, the grading rule, the legs, and the
kill criteria are stated in full; each prediction
carries a grade with citations. **Executed at
registration: PASS.**

**TC-111-02 — Measurement replay (C111-6; Stage 1).**
Re-run records/p1-measurement-harness.py over the
pinned custody inputs (Spec 105 token streams; Spec
107 Latin donor text; seed 11101) and compare the
returned profiles and distances against
records/p1-measurement-raw-output.json.
*Pass:* profiles and distances reproduce within
floating-point tolerance (1e-6 relative) and the
raw-output SHA-256 of the filed copy is unchanged
(6022f09a…). **Executed at registration: PASS** (the
filed raw output is the run's own output; the harness
is deterministic under its filed seed).

**TC-111-03 — Derivation citations carry their claims
(C111-2, C111-3; Stage 1).** For each derivation the
grades rest on (Meroitic from Egyptian hieroglyphic
and demotic; Cypriot syllabary from Cypro-Minoan;
Indus antecedents in the Ravi and Kot Diji phases),
open the cited source and check it states the
derivation or sequence the record attributes to it.
*Pass:* every checked citation carries its claim.
**Executed at registration: PASS** (Rilly & de Voogt
2012 for Meroitic; Steele 2013 and Ferrara 2012 for
the Cypriot line; Kenoyer & Meadow's Harappa record
and Kenoyer 2006 for the Indus sequence).

**TC-111-04 — Claimed-older-writing labels are exact
(C111-4; Stage 1).** Check the evaluation record's
Jiahu, Vinča, and Dispilio entries against their cited
sources: dates as the sources give them (Jiahu c.
6600–6200 BCE and the publishers' "not as writing
itself" assessment, Antiquity 77(295):31–44; Vinča
bulk c. 4500–4000 BCE with the Tărtăria association
dating flagged disputed and the proto-writing standing
stated; Dispilio's direct wood date 5324–5079 cal BC
at 95.4%, Radiocarbon 56(2), with the no-demonstration
standing stated as of 2025).
*Pass:* no entry overstates or understates its source;
each label names its standing as a label.
**Executed at registration: PASS.**

**TC-111-05 — Untestable items name their deciders
(C111-5, C111-7; Stage 1).** Check that every
UNTESTABLE grade in the evaluation record names the
missing evidence and what acquiring or finding it
would take (P1 paleographic leg, §5; P4 Indus content
leg, §5 and §6.1; P3's deciding find class, §5).
*Pass:* no UNTESTABLE grade stands without its
decider stated. **Executed at registration: PASS.**

**TC-111-06 — No-standing-moves and language audit
(C111-1, C111-8; Stage 2).** Read the landed package
for any act moving a standing, verdict, anchor, or
tally in any program, and for any sentence presenting
the hypothesis as assumed, dismissed by posture, or
proven impossible.
*Pass:* no such act and no such sentence exists; the
grades are stated as grades of predictions on current
evidence throughout. **Executed at registration:
PASS.**
