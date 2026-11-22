# Eteocypriot Program — ICS 196 Custody Correction

**Date: 2026-11-21. Filed under Red Team Round 1 (findings
RT1-08, RT1-25), adjudicated APPLY on 2026-11-21. The corpus
file (`corpus/corpus.json`) is corrected by the same landing
as this record; the freeze record is NOT edited.**

## What is actually held

ICS 196's status in the corpus was `held_complete`. That
wording claims more than the record holds. Verified from
corpus.json and freeze §1:

- The text is held as reproduced in **secondary sources**:
  Wikipedia ("Eteocypriot language," CC BY-SA), reproducing
  Masson's text, and Woudhuizen 2012, concordant with it —
  two reproductions deriving from the one source, not two
  witnesses.
- Duhoux 2009 (Kadmos 48, pp. 44–48) provides a concordant
  segment-by-segment discussion. It was consulted; it is not
  the edition.
- **Masson's edition (ICS, 2nd ed. 1983, pp. 206–209) was not
  held or read as text.** The Sittig 1914 photograph — the
  witness of record for a stone lost after 1913/14 — was not
  consulted.

## The corrected status

ICS 196's corpus status is restated, and corpus.json is
corrected by the same landing: **held from secondary
reproductions of the edition of record; the edition itself
not held as text.** The corpus pin (the freeze's SHA-256) is
the identity of this file. It is not, and is never cited as,
verification of the edition's fidelity: the pin proves the
program analysed the bytes it filed, not that those bytes are
Masson's text.

Verification against Masson's text, or against the Sittig
photograph, through a lawful route (an interlibrary-loan
request for ICS pp. 206–209 is the route of record) is the
closing act for this item. It is an external act, flagged to
the owner in the Round 1 adjudication (Flag F-3); it is not
executed here, and the corrected status stands until it is
done.

## The licensing corrections (RT1-25)

Filed with this record, in corpus.json's `licensing_basis`
and records:

- Duhoux 2009 is **in-copyright scholarship** (Kadmos 48,
  2009), consulted via an academia.edu posting — not
  "public-domain scholarship," as the basis as filed called
  it.
- The two Androkles `translation_of_record` strings (the SEG
  translation as presented at attalus.org) are replaced by
  the program's own paraphrase, marked as such, with
  attalus.org SEG 32.1318 pointed to and not reproduced. The
  basis's assertion that no copyrighted translation is
  reproduced is true from this correction onward; it was not
  true as filed.
- The ICS 196 `sense` field is the program's rendering and is
  marked as such; its name forms are corrected to the study's
  (Aristona / Aristonaktos).
- A CC BY-SA attribution note is added for the
  Wikipedia-derived transcriptions.

## Corrected file identity

The freeze pin (SHA-256 `5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`) identifies corpus.json as executed at E1 — verified against the file immediately before this correction was applied. The corrected file's SHA-256 is `60125fcf42f5091febd7b74b5fb530b93aba8d07e8ed869efa683eb17a609f19`. The freeze pin is not re-set: it names the executed bytes, and this record names the corrected ones; the two hashes together are the file's history.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
