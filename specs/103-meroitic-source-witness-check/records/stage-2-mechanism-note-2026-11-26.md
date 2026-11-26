# Spec 103 — Stage 2 Mechanism Note: Transferable Learnings (2026-11-26)

Filed under the owner's direction in the commissioning
order (Glossa-Lab chat, 2026-11-26 10:27 ET): while
executing the asoreyi witness check, learn all that can
be learned about mechanisms transferable to the Indus
and Eteocypriot programs, and file those learnings
explicitly. These are observations only. No work is
started on the other programs by this note, and no
standing or verdict moves anywhere.

## 1. The mechanism as designed, and what it actually was

The designed mechanism was *witness completion*: a
frozen classification (Spec 103 Stage 1) had returned
NOT CHECKED — INCOMPLETE COVERAGE for one form because
8 of 33 held-out texts carried no witness in the
acquired build. The plan was to close the gap with an
edition-of-record witness: hold the REM, transcribe its
transliterations for the eight texts, and let the
corrected checker classify the six open loci.

What execution found is that the mechanism has a hidden
precondition nobody had stated: **the edition must
carry the witness in the form the checker consumes.**
The REM is a repertory, not a re-edition. For
already-published texts it catalogues the monument and
reproduces plates; for all eight texts in scope it
prints no transliteration at all. Custody was complete,
identification was exact, the checker was ready — and
there was no witness, because the witness form (a
transliteration token stream) does not exist in the
source for these texts. "We hold the edition of record"
and "we hold a witness for text X" are different facts,
and only the second one closes a coverage gap.

## 2. Coverage accounting: one label hid three states

Stage 1's WITNESS UNAVAILABLE label merged states that
Stage 2 had to separate to describe its own result:

- **(a) No witness source held.** asoreyi's state from
  2026-11-23 to the REM acquisition.
- **(b) Witness source held, but it carries no witness
  in the consumed form for this text.** asoreyi's state
  after Stage 2: the edition is in custody, its entries
  are identified and inspected, and the transliteration
  the checker consumes is not in them.
- **(c) Witness held and consumed.** The 25 held-out
  texts Stage 1 classified.

Moving from (a) to (b) is real progress — it closes a
route definitively and names the instrument that would
be needed instead — but a single WITNESS UNAVAILABLE
label makes the movement invisible. Any future coverage
accounting in this program family should carry the
substate: held-and-consumed, held-but-not-in-consumed-
form, not held. The same three-state distinction
applies wherever a program counts its evidence coverage
in sources rather than in consumed streams.

## 3. Independence is a property of the consumed form, not of the volume

For Sh. 9 and Sh. 16, the REM plates reproduce Griffith
1911a's hand copies — the same publication whose
transliteration the build's extraction carries. Even if
a token stream had been extracted from those plates, it
would not have been an independent witness against
Griffith's reading in the way the check requires; it
would have been Griffith checked against Griffith. The
volume is modern, authoritative, and exactly the right
acquisition for identification, bibliography, and
plates — and none of that makes its reproduced copies
an independent token stream. The transferable rule:
**when a witness is proposed, ask who produced this
token stream, from what, before asking how authoritative
the container is.** Independence lives at the level of
the consumed form.

## 4. The existence check belongs in the acquisition, not the execution

One page inspection per in-scope text, done at
acquisition time, would have established that the REM
prints no transliteration for Sh. 9 and Sh. 16 — before
a registration was written around transcribing it. The
acquisition itself was still worth making (the REM is
the field's settling record and is now held for all
future Meroitic work), but its expected value for this
specific check was misjudged because the witness form
was assumed from the edition's reputation rather than
verified in the entries. Rule for future acquisitions
in all three programs: **an acquisition record should
state, for the exact texts or items in scope, that the
consumed form has been seen in the source** — one
rendered page per item — or should record that it has
not been checked, so a later registration does not
build on the assumption.

## 5. Checker design observations

- **The outcome vocabulary absorbed the failure
  truthfully.** WITNESS UNAVAILABLE plus NOT CHECKED —
  INCOMPLETE COVERAGE gave the execution an honest
  value for "the witness does not exist in the needed
  form", and the registration discipline (spec.md §6:
  a protocol change is a new registration) blocked the
  three substitutions that were physically available
  and would each have been a quiet protocol change:
  treating the PDFs' OCR text layer as the witness,
  reading Griffith's hand copies as if they were the
  REM's transliteration, or treating the notices'
  descriptive name readings as text witnesses. A
  checker whose vocabulary has no truthful value for a
  missing witness invites exactly those substitutions.
- **Filed executors should not hardcode their venue.**
  The conformance addendum's script hardcodes the repo
  path of the clone it was executed in
  (`sw103-addendum`, deleted in the same motion as its
  landing, per program discipline). Replaying it
  byte-untouched required staging its two inputs at
  that exact path. The replay succeeded and the
  control is exact, but the friction is a design
  lesson: an executor that resolves its inputs relative
  to its own location (or the repo root derived from
  it) replays anywhere; one that embeds a clone path
  replays only by resurrecting the path. Future
  executors in this family should derive paths, and a
  replay test belongs in their test cases.
- **Registration before execution is what made the
  negative result clean.** Because the witness
  definition, the loci, and the kill condition were
  committed before any page was rendered, the finding
  "the witness does not exist in the registered form"
  is itself a registered outcome rather than a
  mid-flight renegotiation. The negative result is
  worth as much to the program as a classification
  would have been: the REM route is now closed on
  evidence, not on assumption.

## 6. Where the analogous gaps sit in the other two programs

**Indus — independent sourcing of anchors (the M047
pattern).** The Indus register stands at 1 of 94 strict
core anchors independently sourced (M047, via the T501
recomputation, PR #730). The Stage 2 lesson applies
directly: an anchor's "independent source" should be
counted only when the source carries an independent
reading in the consumed form — a reading of the sign
produced independently of the catalogue tradition the
candidate was built from — not when a second volume
that reproduces the same catalogue reading is held.
Coverage counted in volumes held will overstate
coverage counted in independent token streams consumed,
by exactly the mechanism that made the REM look like a
witness for Sh. 9 and Sh. 16. The three-state accounting
of §2 (held-and-consumed / held-but-not-independent-in-
form / not held) is the shape an honest anchor-sourcing
census would take.

**Eteocypriot — the ICS 196 edition-of-record check
(ETE-ENV-04).** The outstanding item is a portion copy
of the standard edition's text of ICS 196 (the request
to Natalie Smith is unanswered). Stage 2's lesson for
the day it arrives: verify, on the copy itself, that it
carries the consumed form for the exact segments in
scope — the edition's printed text of the relevant
lines — and record the substate if it does not, before
any check is registered around it. An edition-of-record
check whose edition arrives as plates, excerpts, or a
different portion than the one in scope is Stage 2's
outcome in another program's clothes. The Eteocypriot
program has already met the friendly version of this
distinction once: the Spec 104 freeze pin named the
right bytes under a stale label, and Round E's ruling
was that the record must say exactly which. Form and
label both matter; Stage 2 adds *existence of the form
in the source* to the list of things to verify rather
than assume.

## 7. What would settle asoreyi (named, not started)

A separately registered sign-level re-reading of the
Shablul monuments (Philadelphia 5108 and 5116) or of
the published plates, or a modern re-edition printing
a transliteration of REM 0376 / REM 0383, acquired
under a new registration. Nothing in this note
commissions either.

**AI disclosure:** written by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
