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

**TC-112-09 (revision package form).** The revision
package verifies in form: claims-revision.json ids
and order equal claims.md C112-8..C112-11; every
revision claim carries a falsifier and a
does-not-establish line in both files; the revision
registration names the three filed failure
mechanisms and the design answers, and states that
no floor, ground-truth set, or scoring rule changed.

**TC-112-10 (fixture proofs).** The revision's
fixture proofs run at the freeze, before the
preflight, over the registered fixtures: (a) no
one-segment candidate appears in any top-5
segmentation; (b) on the easy fixture the planted
segmentation outscores the all-single-character
fallback on the planted forms; (c) the median
boundary F1 on the easy fixture and on the hard
fixture (recurrent root pieces, the 24 gold strings
as the planted inventory, stacked suffixes, bare
stems, defective spellings) is at least 0.80. Any
failure closes the revision as filed without a
preflight run.

**TC-112-11 (revision two-implementation
agreement).** The revision's preflight figures (P-1
median boundary F1, P-2 slot match rate, name-slot
variance rank, and slot yield; P-3 precision, the
null-derived threshold, and the shuffle yield ratio)
are recomputed by an independent implementation from
the filed outputs and agree exactly (rational
figures) or to the carried tolerance (entropies).
