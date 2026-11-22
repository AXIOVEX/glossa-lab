# Spec 099 — Claims

Every claim carries at least one falsifier (a concrete
observation that would show it false) and a "does not
establish" line (the over-reading it forbids), per the
program's claims discipline. The same set, normalized into
`aee-claims.json` without substantive change, is the claims
bundle of record for this package, intaken into the
canonical ledger at adoption (D-099-2).

## The log

**C099-1 — The log carries every one of the 94, exactly
once, as the standings record states them.** Every
strict-core reading in the executed standings (the WS2
relabel execution record: 5 E + 65 I + 4 R + 3 P + 17 U)
appears exactly once in the inference log, with its sign,
its reading as recorded, its executed class, and its
source-diversity flag as that record states them.
*Falsifier:* a sign in the standings record absent from the
log or present twice; a log entry whose reading, class, or
flag differs from the standings record's row for that sign.
*Does not establish:* that the standings are correct — the
log transcribes the record of record, it does not re-derive
it.

**C099-2 — The log is complete against the filed bases, and
contains nothing they do not state.** Every evidence element
stated in a reading's filed basis (the appendix row as filed
from the register, cross-checked against the frozen register
snapshot and the falsifiers annex's evidence line) appears
in that reading's log entry as an item citing the verbatim
basis clause it was extracted from; and no log item cites a
clause its entry's filed basis does not contain.
*Falsifier:* a filed basis element with no corresponding log
item (the completeness check of TC-099-02 enumerates the
checkable families mechanically); or a log item whose
`basis_span` does not occur in the entry's `basis_as_filed`.
*Does not establish:* that the filed bases are complete
derivations — where a basis is truncated or thin, the log
records the truncation or thinness; it does not repair it.

**C099-3 — Every item is typed by the filed basis, and
ambiguity is recorded, never resolved silently.** Each item
is typed (a) primary evidence, (b) another reading or a
candidate-system construct used as evidence, or ambiguous,
under the typing rules of spec section 3.3; every (b) item
names the readings it depends on, or records that the basis
names no target; every (b) and ambiguous item carries a
reason tied to the basis text; and every (b) classification
was verified by reading the filed basis clause it cites.
*Falsifier:* a (b) item whose cited basis clause, read
plainly, states primary evidence and no other reading or
construct; an ambiguous item with no reason; a named target
absent from the cited clause and from the records the spec
names as the item's source.
*Does not establish:* that a (b) typing makes an item worthless
— it makes the item dependent, which is what the audit
measures; several (b) items record real co-occurrence whose
raw counts the log also carries as (a) items.

## The audit

**C099-4 — The audit is a pure function of the log.** The
Q3 graph audit's per-reading outcomes and component list
reproduce exactly from the log file, the executed standings
it carries, and the class rules of spec section 4.2, with no
other input; an independent implementation of those rules
recomputes the filed audit table without difference.
*Falsifier:* the determinism recomputation (TC-099-03's
implementation, run over the real log at Stage 2) differing
from the filed audit table on any reading or component; or
the audit tool's input manifest naming a source beyond the
log and the class-rule records.
*Does not establish:* that the class rules are the uniquely
right ones — they are the adjudication's, applied as
recorded, so the audit measures what the program's own rules
imply.

**C099-5 — The audit applies the adjudication's class rules
and moves nothing.** Each reading's outcome is stated in the
vocabulary of spec section 4.2 (class unchanged / basis
weakened with the losses named / class would change with the
destination named), computed under the relabel execution
record's class definitions and the reclassification form of
its addendum; both the primary treatment (ambiguous retained)
and the sensitivity treatment (ambiguous removed) are
computed and any divergence reported; and no standing,
anchor, or register entry is altered by the audit or by any
record of this package.
*Falsifier:* an outcome inconsistent with the rules applied
to the log's items for that reading; a filed outcome missing
its sensitivity divergence where the two treatments differ;
or a standings record changed citing this audit as its
basis.
*Does not establish:* that a "class would change" outcome
changes the class — it is a report to a further adjudication,
which this package is not.

**C099-6 — Cycles are computed, not asserted.** The
completion record states the strongly connected components
of the log's (b)-graph (named-target edges) as computed, and
lists the (b) items whose targets the filed bases do not
name as open ends; no record of this package describes the
dependency structure among the 94 as acyclic or as cyclic
beyond that computation and that list.
*Falsifier:* a cycle in the log's named-target (b)-graph
absent from the completion record's component list; an open
end omitted from the list; or a cyclicity claim in the
package not backed by the computed components.
*Does not establish:* that an unnamed-target edge conceals no
cycle — the record states the limit on its face, which is
what replaces the dependency record's "not established in
either direction" with a bounded, checkable statement.

## The M267 statement and the bounds

**C099-7 — The M267 dependency statement is exact to the
log, and no retest is run.** The statement names every
(b)-type premise in M267's log entry, with its kind and its
named targets, states which of M267's (a) items survive
removal, and states what a dependency-aware retest must hold
fixed or exclude; this package runs no M267 retest and
designs none in executable detail.
*Falsifier:* a (b) item in M267's log entry missing from the
statement; a slot marker named in the statement that
M267's entry does not carry; or a retest result, in any
form, anywhere in this package's records.
*Does not establish:* that M267's reading is false — it
establishes what its filed basis depends on, which is the
input a future retest commission needs.

**C099-8 — Execution discipline: venue, index, payload
verdicts.** All execution runs on tower-compute in fresh
clones under `~/glossa-work/`; every build, check, and audit
run of this package is indexed in the spec's records with
its raw output or its hash; and every reported verdict is
the run's own payload verdict, never a wrapper or transport
state.
*Falsifier:* a run executed on the coordination VM or the
mini-server; a stage record claiming a check whose raw
output is not filed or hashed in the package's records; or
a reported verdict that is a wrapper state rather than the
payload's own record.
*Does not establish:* that a complete index proves the runs
were correct — it proves they are all on the record, which
is what makes their correctness checkable.
