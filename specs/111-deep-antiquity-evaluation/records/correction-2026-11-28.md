# Spec 111 — Correction cross-reference (2026-11-28): conditional-entropy feature of the P1 descriptive leg

Filed under Round Q of the Co-scientist loop, ledger row
Q-I-1 (adjudication
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-28-round-q.md`
§1). The full correction and adjudication record for Spec 111
in this round is
`records/correction-and-adjudication-2026-11-28.md`; this note
carries the entropy qualification for the P1 descriptive leg
in the form the Spec 110 correction prescribes.

Spec 111's profile function files `H_XY - H_all` as its
conditional entropy, instead of subtracting `H_X` (the first
marginal entropy of the same normalized within-sequence
bigram table). The filed quantity is therefore not the
conditional entropy claimed. From the filed aggregate tables
(Indus, bits): H_all 6.265061399, H_X 6.499966322,
H_Y 5.491198311, H_XY 10.240560673, proper I(X;Y)
1.750603959, Spec 111's filed value 3.975499274. The
two-sequence witness `[a,b]`, `[a,c]` returns filed
conditional entropy -0.5 against a true conditional entropy
of 1 bit.

Qualification, of record: the P1 distance matrix reproduces
its filed feature values, but one feature is not the
conditional entropy claimed, and the conditional-entropy
interpretation of the P1 descriptive leg is withheld
accordingly. The descriptive profile result is not an
ancestry-detection test. All frozen outputs and the original
evaluation bytes are preserved; no grade is changed by this
note.
