# Spec 112 — Test Cases

**TC-112-01 (package form).** The claims bundle's
ids and order equal claims.md C112-1..C112-7; every
claim carries a falsifier and a does-not-establish
line in both files; spec.md states the corpus pins,
the three targets, the preflight with its floors,
the Stage-5 relation, the execution sequence, and
the kill criteria.

**TC-112-02 (corpus pin verification).** The
Kovetsky build's commit and source hash and the
Otten corpus pin recompute to the values spec.md §2
registers, from the custody objects themselves,
before any other test case runs.

**TC-112-03 (ground-truth set integrity).** The
preflight's ground-truth sets (anchor inventory
Class B forms and slot template; gold morphology)
are extracted from their records of origin and
hash-pinned at the preflight freeze; the filed sets
recompute byte-identically from those records.

**TC-112-04 (no output before preflight).** The
study's record tree contains no corpus-output file
before a filed full-pass preflight verdict; the
check runs over the tree at the preflight freeze and
again at any corpus run.

**TC-112-05 (shuffle construction).** The shuffle
control's construction (token order destroyed within
texts, inventory and text lengths preserved,
registered seed) verifies on a fixture corpus with
known structure: the fixture's structure is present
in the ordered run and absent, at the registered
cap, in the shuffled run.

**TC-112-06 (two-implementation agreement).** The
preflight figures (P-1 boundary F1, P-2 slot match
rate and name-slot variance rank, P-3 precision and
shuffle yield ratio) are recomputed by an
independent implementation from the filed outputs
and agree exactly.

**TC-112-07 (provenance completeness).** Every
filed candidate (segmentation, partial, slot
grammar element) carries search state, seed, and
data pins; a candidate missing any element fails
this case and is not filed.

**TC-112-08 (non-interference).** The registration
and any execution under it write nothing into Spec
102's or Spec 109's trees, change no gate, source
rule, or pin of either, and assign no gloss to any
Meroitic form; verified by tree diff over both specs
at the close of any stage.
