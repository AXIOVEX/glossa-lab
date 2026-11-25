# Spec 106 — Claims

Six claims, C106-1..C106-6, each with its falsifier and its
does-not-establish line, in the program's claim form. The claims
are intaken at registration through the sanctioned importer
(spec.md, tasks T003); intake sets no standing, and no claim in
this package carries a result beyond what its test cases check
mechanically at registration.

**C106-1 — The framework specification is complete against its
own commission.** `framework.md` defines every moving part the
owner's orders name (baseline template, axiom with kind label,
instance, seed, claim, translation, derivation, evidence set,
checker, verdict, ensemble, iteration, retirement, solution),
states the seeding protocol as an exact seed-record contents
list, states the iteration protocol (what may and may not change
between iterations, how variations are chosen, how verdicts
accumulate), and reserves the word solution for a claim that
survives across all surviving instances of its ensemble and
passes the adopting program's ordinary boundary gates, with an
exact status label for every lesser state.

*Falsifier:* any named moving part without a definition in
framework.md; a seed record field the protocol does not list; a
use of the word "solution" in the package for anything below the
§8 criterion; a lesser state with no label in the §8 vocabulary.

*Does not establish:* that the framework is a good method, or
that any program should adopt it — adoption is each program's
own act, and the specification's completeness is a property of
the text, not of its worth.

**C106-2 — Every axiom line in the three baseline templates
carries exactly one kind label and a source or the UNSOURCED
flag.** Each line of `templates/indus-baseline.md`,
`templates/eteocypriot-baseline.md`, and
`templates/meroitic-baseline.md` matching the axiom form carries
exactly one of (F), (K), (H); carries a named source or the
UNSOURCED flag; and every line whose sourcing is the UNSOURCED
flag is an (H).

*Falsifier:* one line failing any of those checks under the
filed audit (`records/census-audit.py`, TC-106-02).

*Does not establish:* that any axiom is true — the audit checks
labeling and sourcing form, not content; content stands or falls
with the cited sources and the framework's checker.

**C106-3 — The three templates share one schema.** All three
carry the same eight domains in the same order, the same axiom
line grammar, and a Domain 1 that is a pointer to Spec 105
rather than duplicated content, so one ensemble technique built
for one program runs on all three.

*Falsifier:* a domain present in one template and absent or
reordered in another; an axiom line grammar difference between
templates; Spec 105 floor content duplicated into a template's
Domain 1 (TC-106-03).

*Does not establish:* that eight domains are the right domains
for any other program — the framework (§10) leaves domain choice
to the adopting program.

**C106-4 — The censuses were built from sources actually
opened, program records first.** Each census axiom's named
source is a source its builder opened in this study's research
pass (in full, or at search-result depth where the axiom itself
says so), and any content whose source could not be opened is
cited only as summarised in an opened source, dropped, or
carried as (H) UNSOURCED.

*Falsifier:* a census axiom citing a source that does not
support its statement; a source represented as opened in full
that the research record shows only at search-result depth,
without the axiom saying so; an axiom resting on Rilly 2010 or
Rilly & de Voogt 2012 stated as if read directly.

*Does not establish:* that the cited sources are right — the
census records the record as it stands, labeled by kind, and
revisable lines are labeled (K) for exactly that reason.

**C106-5 — Each template carries a seed record in the
framework's provenance format, and the record verifies.** Each
template's seed record states the fields of framework §4
(study identity; template identity and version; the axiom census
as seeded with counts by domain and kind and a SHA-256 over the
axiom lines as filed; the claim queue as opened; the evidence
set and registered contact points; date and authorizing order),
and the stated counts and hash recompute exactly from the filed
template (TC-106-05).

*Falsifier:* a missing §4 field in any seed record; a stated
count or hash that does not recompute from the filed template.

*Does not establish:* that any study has been seeded beyond
these baselines — the seed records open the templates' lineages;
until an instance exists until a Stage 1 commission spawns one.

**C106-6 — This study spawns no instance, tests no claim, and
moves no standing.** The landing's changes are confined to this
spec's package, its own claims' ledger intake artifacts, the
taxonomy entry, the regenerated layers and census pins of the
registration cascade, and no record of any program's standings,
verdicts, or tallies is altered in content.

*Falsifier:* an instance, derivation, or claim verdict anywhere
in this study's records; a landing diff touching a standing,
verdict, or tally record of the Indus, Eteocypriot, or Meroitic
programs (TC-106-06).

*Does not establish:* that the templates' hypotheses are false
or idle — they are declared, seeded, and waiting for a Stage 1
commission, which is the state this claim certifies.
