#!/usr/bin/env python3
"""Spec 099 Stage 1 — build the inference log.

Assembles the 94-entry inference log (spec section 3) from:

- the audit package appendix (the basis text as filed, one
  row per reading),
- the WS2 relabel execution record (the executed standings:
  reading, class, Q4 flag per sign),
- the curation in this file: the template rules below propose
  items from the basis text's own segments, and the per-sign
  curation (CURATION) settles the entries whose bases the
  templates do not cover. Every (b) item in the output was
  verified against the filed basis clause it cites by reading
  it (spec section 3.3); ambiguous items carry their reason.

Usage:

    python3 build_inference_log.py APPENDIX.md RELABEL.md \
        --out inference-log.json --render inference-log.md

The builder is deterministic: same inputs, same log.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

MOTIF_SUPPLEMENT_SIGNS = {
    "M006", "M013", "M016", "M045", "M057", "M062",
    "M060", "M067", "M063", "M068", "M080",
}

MOTIF_NOTE = (
    "motif evidence not reproducible from held records "
    "(standings supplement 2026-11-21, section 3)"
)

CORRECTED_BATTERY_RE = re.compile(
    r"Later corrected validation battery: score (\d+) against a "
    r"promotion threshold of 2 \(([^)]*)\); moved from requires "
    r"revalidation to this class\."
)
SITE_CHECK_RE = re.compile(
    r"Later corrected site-statistics check: outcome ([^;]+); "
    r"moved from requires revalidation to this class\."
)


def parse_appendix(text: str) -> dict:
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| M"):
            continue
        cells = [c.strip() for c in line.split("|")]
        # ['', sign, reading, class, basis, falsifier, '']
        if len(cells) < 6:
            continue
        sign = cells[1]
        if not re.fullmatch(r"M\d{3}", sign):
            continue
        rows[sign] = {"reading": cells[2], "basis": cells[4]}
    return rows


def parse_standings(text: str) -> dict:
    rows = {}
    for line in text.splitlines():
        m = re.match(
            r"\| \d+ \| (M\d{3}) \| (.+?) \| .+? \| (E|I|R|P|U) ?\*? \| ([SNMA]) \|",
            line,
        )
        if m:
            rows[m.group(1)] = {
                "reading": m.group(2).strip(),
                "executed_class": m.group(3),
                "q4_flag": m.group(4),
            }
    return rows


class EntryBuilder:
    def __init__(self, sign: str, basis: str):
        self.sign = sign
        self.basis = basis
        self.items: list[dict] = []
        self.notes: list[str] = []

    def add(self, kind, type_, statement, span, targets=None,
            reason=None, target_note=None, target_source=None,
            status_note=None):
        assert span in self.basis, (self.sign, span)
        item = {
            "id": f"{self.sign}-{len(self.items) + 1:02d}",
            "kind": kind,
            "type": type_,
            "statement": statement,
            "basis_span": span,
            "targets": targets or [],
        }
        if reason:
            item["reason"] = reason
        if target_note:
            item["target_note"] = target_note
        if target_source:
            item["target_source"] = target_source
        if status_note:
            item["status_note"] = status_note
        self.items.append(item)
        return item

    def note(self, text):
        self.notes.append(text)


# ------------------------------------------------------------ templates


def seg_items(b: EntryBuilder):
    """Template items from the common basis segments."""
    basis = b.basis
    # Positional: Round segment, optionally merged with the
    # UPGRADED-V18 restatement that follows it.
    m = re.search(
        r"Round \d+: (INITIAL|MEDIAL|FINAL) position \(freq=(\d+)\), "
        r"distributional assignment(; UPGRADED-V18: consistent "
        r"(?:INITIAL|MEDIAL|TERMINAL) \(n=\d+\))?",
        basis,
    )
    if m:
        b.add("positional_statistic", "a",
              f"positional distribution: {m.group(1)} position, "
              f"frequency {m.group(2)}, distributional assignment"
              + ("; restated as consistent in the V18 upgrade"
                 if m.group(3) else ""),
              m.group(0))
    else:
        m = re.search(
            r"UPGRADED: (?:high|moderate) frequency \(\d+\); consistent "
            r"(?:INITIAL|MEDIAL|TERMINAL) position \(n=\d+\)",
            basis,
        )
        if m:
            b.add("positional_statistic", "a",
                  "positional distribution as upgraded: " + m.group(0),
                  m.group(0))
        m = re.search(r"Round \d+: [^;]*?distributional assignment "
                      r"\[Phase[^\]]*\]", basis)
        if m and not any(i["kind"] == "positional_statistic"
                         for i in b.items):
            b.add("positional_statistic", "a",
                  "positional distribution: " + m.group(0), m.group(0))
    # Self-assertion.
    if "has specific PDR reading" in basis:
        b.add("self_assertion", "b",
              "the basis asserts the sign 'has specific PDR reading'",
              "has specific PDR reading",
              reason="the adjudication's words: an input, not "
                     "corroboration — the candidate system's own "
                     "assertion about its reading, filed as part of "
                     "the basis",
              target_note="the assertion names no other reading; "
                          "it is the system's own claim about "
                          "this reading")
    # Collocates: raw count (a) + interpreted-anchor premise (b).
    for m in re.finditer(
            r"(?:collocates with HIGH anchor|HIGH-anchor collocate) "
            r"(M\d{3}) \(n=(\d+)\)", basis):
        b.add("corpus_count", "a",
              f"raw co-occurrence count with {m.group(1)}: "
              f"n={m.group(2)}", m.group(0))
        b.add("interpreted_anchor", "b",
              f"collocation premise: this sign collocates with "
              f"{m.group(1)} as a HIGH anchor",
              m.group(0), targets=[m.group(1)],
              reason=f"the premise is {m.group(1)} under its "
                     f"interpreted reading and HIGH standing; the "
                     f"raw count is carried separately as an (a) item")
    # Truncated collocate (M336): premise filed, target cut off.
    if re.search(r"collocates with HIGH anchor ;", basis):
        b.add("interpreted_anchor", "b",
              "a third collocation premise is filed but its target "
              "is cut off in the basis as filed",
              "collocates with HIGH anchor",
              reason="the basis truncates mid-clause at this "
                     "premise; the premise is (b)-type but its "
                     "target cannot be recovered from the filed text",
              target_note="the basis as filed names no target; "
                          "the clause is truncated")
    # Truncated collocate count (M367): target named, count cut off.
    m = re.search(r"collocates with HIGH anchor (M\d{3}) \(n=;", basis)
    if m:
        b.add("interpreted_anchor", "b",
              f"collocation premise: this sign collocates with "
              f"{m.group(1)} as a HIGH anchor; the count is cut "
              f"off in the basis as filed",
              m.group(0), targets=[m.group(1)],
              reason=f"the premise is {m.group(1)} under its "
                     f"interpreted reading and HIGH standing",
              status_note="the filed count is truncated in the "
                          "basis as filed")
    # SA-cons consistency scores (ambiguous).
    for m in re.finditer(r"\[(Phase-\d+[^\]]*SA-cons=[\d.]+[^\]]*)\]",
                         basis):
        b.add("consistency_score", "ambiguous",
              "candidate-system consistency score: " +
              re.search(r"SA-cons=[\d.]+", m.group(0)).group(0),
              m.group(0),
              reason="the filed basis states the score but no "
                     "definition of its inputs; whether it is "
                     "computed over primary data or over "
                     "interpreted material is not stated, so it "
                     "is recorded ambiguous under spec section 3.4")
    # Phase-272 DEDR injection.
    m = re.search(r"Phase-272: DEDR (\d+) injected \+ existing "
                  r"evidence → HIG?H?", basis)
    if m:
        b.add("dictionary_entry", "a",
              f"DEDR {m.group(1)} cited for this reading "
              f"(Phase-272 injection)", m.group(0))
        b.note("the Phase-272 segment's roll-up ('existing "
               "evidence → HIGH') is a derivation step of the "
               "candidate system, recorded here, not an item "
               "(spec section 3.3)")
    # Phase-255 commodity corroboration.
    m = re.search(
        r"Phase-255: commodity phoneme corroboration — matches "
        r"PDr '([^']+)'=([a-z]+) \(DEDR (\d+)\)"
        r"(, appears on (\d+) trade/zebu seals)?", basis)
    if m:
        b.add("dictionary_entry", "a",
              f"commodity phoneme corroboration: PDr "
              f"'{m.group(1)}' = {m.group(2)} (DEDR {m.group(3)})",
              m.group(0))
        if m.group(4):
            b.add("motif_association", "a",
                  f"the sign appears on {m.group(5)} trade/zebu seals",
                  m.group(4).lstrip(", "))
    # Motif exclusivity + PDR gloss.
    m = re.search(r"Exclusive to ([a-z ]+?) seals \(lift > 5\.0\)",
                  basis)
    if m:
        note = MOTIF_NOTE if b.sign in MOTIF_SUPPLEMENT_SIGNS else None
        b.add("motif_association", "a",
              f"the sign is exclusive to {m.group(1)} seals "
              f"(filed lift > 5.0)", m.group(0), status_note=note)
    m = re.search(r"PDR ([^\s=]+(?: [^\s=]+)?) = ([^;.]+)", basis)
    if m and "Exclusive to" in basis:
        b.add("comparative_lexical", "a",
              f"PDr {m.group(1)} = {m.group(2)} (the motif's "
              f"lexical counterpart)", m.group(0))
    # Corrected validation battery / site-statistics check.
    m = CORRECTED_BATTERY_RE.search(basis)
    if m:
        b.add("corrected_validation", "a",
              f"corrected validation battery: score {m.group(1)} "
              f"against a promotion threshold of 2 ({m.group(2)}); "
              f"the sign was moved from requires revalidation to "
              f"its filed class on this result", m.group(0))
    m = SITE_CHECK_RE.search(basis)
    if m:
        b.add("corrected_validation", "a",
              f"corrected site-statistics check: outcome "
              f"{m.group(1)}; the sign was moved from requires "
              f"revalidation to its filed class on this result",
              m.group(0))
    # Dictionary reference segment (when no DEDR item yet covers
    # the same number).
    m = re.search(r"Dictionary reference as recorded: (?:DEDR )?(\d+)",
                  basis)
    if m:
        num = m.group(1).lstrip("0") or "0"
        covered = any(
            i["kind"] == "dictionary_entry"
            and re.search(rf"DEDR 0*{num}\b", i["statement"])
            for i in b.items
        )
        if not covered:
            b.add("dictionary_entry", "a",
                  f"DEDR {num} recorded as this reading's "
                  f"dictionary reference", m.group(0))


# ------------------------------------------------------------- curation


def _phase276(b: EntryBuilder, elamite, sanskrit, dedr, status=None):
    b.add("comparative_lexical", "a",
          f"external corroboration leg: {elamite}", elamite)
    b.add("comparative_lexical", "a",
          f"external corroboration leg: {sanskrit}", sanskrit,
          status_note=status)
    # Spec section 3.2: a DEDR entry cited in the basis and
    # again as the row's dictionary reference is ONE item
    # citing both clauses. The template's dictionary-reference
    # arm runs before this curation, so merge into that item
    # when it already cites the same entry (Round 4, RT4-08).
    num = dedr.split()[-1].lstrip("0") or "0"
    for item in b.items:
        if item["kind"] == "dictionary_entry" and re.search(
                rf"DEDR 0*{num}\b", item["statement"]):
            item["statement"] = (
                f"DEDR {num} — one observation cited twice in "
                f"the basis: as an external corroboration leg "
                f"('{dedr}') and as this reading's dictionary "
                f"reference; entered as one item (spec "
                f"section 3.2)")
            return
    b.add("dictionary_entry", "a",
          f"external corroboration leg: {dedr}", dedr)


def _su_slot(b: EntryBuilder):
    b.add("slot_label", "b",
          "the reading is filed as providing partial coverage "
          "for the Shu-ilishu /su/ phonological slot",
          "Provides partial coverage for Shu-ilishu /su/ "
          "phonological slot.",
          reason="the /su/ slot is a construct of the candidate "
                 "system's phonological coverage argument; the "
                 "coverage claim is evidence only inside that "
                 "system",
          target_note="the basis names the slot but no reading "
                      "as its premise")


def _mentions(b: EntryBuilder, source, status=None):
    m = re.search(r"reading '[^']+' found in literature "
                  r"\(4 mentions across sources: ([^)]+)\)", b.basis)
    b.add("published_proposal", "a",
          f"the reading is filed as found in the literature "
          f"(4 mentions across sources: {m.group(1)})",
          m.group(0), status_note=status)


CURATION = {}


def curate(sign):
    def deco(fn):
        CURATION[sign] = fn
        return fn
    return deco


@curate("M044")
def _(b):
    _phase276(b, "Elamite 'kun' (MC-18)", "Sanskrit 'kona' (SL-04)",
              "DEDR 1638")
    _fails = (
        "DEDR 1638 FAILS in the restored tree (entry 1638 = "
        "kucukucu; register reconciliation 2026-11-21, PR #645 "
        "DEDR pass). Adjudicated under the addendum rule on "
        "2026-11-21 (records/m044-addendum-adjudication-"
        "2026-11-21.md, Red Team Round 2 finding RT2-02): the "
        "DEDR leg is struck, no leg stands verified as filed, "
        "no basis remains, and the reading takes class U; this "
        "log's executed class follows the amended standings")
    for item in b.items:
        if item["kind"] == "dictionary_entry":
            item["status_note"] = _fails
    b.note("the basis-as-recorded segment is empty as filed "
           "('Basis as recorded: ;'); the Phase-276 segment "
           "carries the filed legs")
    b.note("the audit's evidence lines count a CROSSWALK_CORPUS "
           "line for this reading, but no crosswalk step is "
           "stated in the basis text as filed")


@curate("M047")
def _(b):
    b.add("positional_statistic", "a",
          "distributional assignment 'par' (LOW, Round 2), "
          "overridden within the filed basis by the crosswalk "
          "evidence",
          "Distributional assignment 'par' (LOW, Round 2) "
          "overridden by crosswalk evidence.",
          status_note="superseded within the filed basis by the "
                      "2026-05-11 fact-check correction")
    b.add("crosswalk_identity", "a",
          "crosswalk identity: M047 = P47 = 'fish (plain)' per "
          "mahadevan_parpola_crosswalk.json (sourced from "
          "Parpola 1994a + Mahadevan)",
          "M047 = P47 = 'fish (plain)' per "
          "mahadevan_parpola_crosswalk.json (sourced from "
          "Parpola 1994a + Mahadevan",
          status_note="an identity at most, never a value: the "
                      "identity rests on catalogue correspondence "
                      "between the two sign lists, not on this "
                      "reading (spec section 3.3); the basis as "
                      "filed truncates mid-clause at this item. "
                      "Re-verification outcome: VERIFIED AS FILED, "
                      "provenance only (relabel execution record)")


@curate("M124")
def _(b):
    _phase276(b, "Elamite 'kun' (MC-18)", "Sanskrit 'kona' (SL-04)",
              "DEDR 1651")
    for item in b.items:
        if item["kind"] == "comparative_lexical":
            item["status_note"] = (
                "leg inherited from M044's Phase-276 package; the "
                "adjudication records that the reuse does not derive "
                "kuTam. Re-verification: PARTIALLY VERIFIED (DEDR "
                "legs only)")
        elif item["kind"] == "dictionary_entry":
            item["status_note"] = (
                "re-verification: PARTIALLY VERIFIED (the DEDR legs "
                "check out as filed)")


@curate("M329")
def _(b):
    _phase276(b, "Elamite 'bur/pur' (MC-21)",
              "Sanskrit 'pura' (SL-14)", "DEDR 4524",
              status="FAILS on its checkable part: Sanskrit pura "
                     "means stronghold/city, not gold "
                     "(re-verification record). The claim stands "
                     "in E under the addendum: PARTIALLY VERIFIED, "
                     "the dictionary leg checks out as filed and "
                     "the remaining legs are not contradicted in "
                     "their named sources")
    for item in b.items:
        if item["kind"] == "dictionary_entry":
            item["status_note"] = (
                "the DEDR leg is verified at the print entry cited; "
                "the restored tree's entry 4524 is a different entry "
                "and the numbering divergence is unresolved (register "
                "reconciliation section (c); relabel execution "
                "record, Round 2 amendment)")


@curate("M202")
def _(b):
    _mentions(b, "Mahadevan_2009_vestiges",
              status="CONTRADICTED on re-verification: Mahadevan "
                     "2009 (Vestiges) contains no 'can' reading; "
                     "the claim was struck under the addendum rule "
                     "and the reading reclassed U (relabel "
                     "execution record, section 4)")
    _su_slot(b)
    b.note("the Phase-276 segment is truncated in the basis as "
           "filed ('dual external corroborati'); its legs are "
           "not stated and no items are entered for it")


@curate("M330")
def _(b):
    _mentions(b, "Parpola_1994",
              status="NOT VERIFIABLE from lawfully reachable "
                     "material: the held Parpola 1994 text is an "
                     "OCR scan, and a negative result from it is "
                     "weaker than a contradiction from a clean "
                     "text (relabel execution record)")
    _su_slot(b)
    b.note("the Phase-276 segment is truncated in the basis as "
           "filed ('dual external corroboration — Elamit'); its "
           "legs are not stated and no items are entered for it")


@curate("M165")
def _(b):
    _mentions(b, "Parpola_1994")
    _su_slot(b)


@curate("M267")
def _(b):
    b.add("corpus_count", "a",
          "M267 has freq=400 in the Holdat corpus and appears "
          "across all motif types (unicorn 127, zebu bull 72, "
          "elephant 37, rhinoceros 25, etc.)",
          "M267 has freq=400 in the Holdat corpus and appears "
          "across ALL motif types (unicorn 127, zebu bull 72, "
          "elephant 37, rhinoceros 25, etc.)",
          status_note="the Holdat corpus is unheld in every "
                      "working clone and no written Miller "
                      "permission is on file (custody statement "
                      "2026-11-21); the counts are as filed")
    b.add("positional_statistic", "a",
          "Phase-74 grammar statistic for the genitive pattern: "
          "z=8.04, p<0.0001",
          "Phase-74 grammar z=8.04 p<0.0001",
          status_note="figures withdrawn as evidence "
                      "(standings supplement section 2, RT1-14): "
                      "the 4.3x lift and z = 8.038 are withdrawn; "
                      "the raw counts stand (26 observed vs null "
                      "mean 6)")
    b.add("consistency_score", "ambiguous",
          "Phase-64 score=7.0 for this reading",
          "Phase-64 score=7.0",
          reason="an internal candidate-system score whose "
                 "inputs the filed basis does not state; "
                 "recorded ambiguous under spec section 3.4")
    b.add("slot_label", "b",
          "the filed pattern [AGENT]-M267-[TITLE]: M267 read as "
          "the genitive between an AGENT slot and a TITLE slot "
          "(4.3x above null as filed)",
          "[AGENT]-M267-[TITLE] 4.3x above null",
          targets=["M176", "M328", "M099", "M073"],
          target_source="standings-supplement-2026-11-21.md",
          reason="the AGENT and TITLE slots are constructs of "
                 "the candidate system, and the pattern's "
                 "markers are themselves readings: the AGENT "
                 "markers of record include M176 and M328, the "
                 "TITLE markers M099 and M073 (standings "
                 "supplement section 2). The adjudication's "
                 "words: conditional circularity — not "
                 "independent confirmation unless the labels "
                 "are independently justified",
          status_note="figures withdrawn as evidence "
                      "(standings supplement section 2, RT1-14)")
    b.note("the 2026-05-11 fact-check correction records that "
           "the original V6 assignment 'min/min' (HIGH) for "
           "this sign was wrong; the correction is part of the "
           "filed basis")
    b.note("the dictionary-reference segment (494) is carried "
           "as a dictionary item by the template pass")


@curate("M347")
def _(b):
    span = ("slot=MEDIAL_BETWEEN_CONF, n_contexts=7, "
            "patterns=['M342-[M347]-M293', 'M028-[M347]-M367', "
            "'M211-[M347]-M099']")
    b.add("slot_label", "b",
          "grammar inference: this sign occupies the slot "
          "MEDIAL_BETWEEN_CONF in 7 contexts, under the "
          "Dravidian grammar slot model (Phases 74-112)",
          span,
          reason="the slot and the slot model are constructs of "
                 "the candidate system; the inference is filed "
                 "as 'inferred from Dravidian grammar slot model "
                 "(Phases 74-112)'",
          target_note="the slot is a model construct; the basis "
                      "names no single reading as its premise")
    b.add("positional_statistic", "a",
          "the filed sequence patterns place this sign between "
          "named signs in 7 contexts", span)
    b.add("interpreted_anchor", "b",
          "the filed patterns read this sign between M342, "
          "M293, M028, M367, M211 and M099 in their interpreted "
          "roles",
          span,
          targets=["M342", "M293", "M028", "M367", "M211", "M099"],
          reason="the patterns are stated over the other signs "
                 "in their interpreted roles in the slot model; "
                 "three of the targets (M293, M028, M211) stand "
                 "outside the strict core and carry no standings")
    b.note("the adjudication's Q3 item 6 struck interpreted-"
           "anchor premises M342, M328, M367, M099 from this "
           "reading's basis ('essentially all stated grammatical "
           "motivation lost'); the M328 premise is not named in "
           "the appendix basis as filed and is recorded here, "
           "not itemized, so the log does not state what the "
           "basis does not")
    b.note("the basis truncates at '[Phase-120: grammar ;' — "
           "the Phase-120 segment is not stated and no item is "
           "entered for it")


@curate("M351")
def _(b):
    b.add("comparative_lexical", "a",
          "substrate match: Munda 'bi' (seed/sprout), Witzel "
          "tradition as filed",
          "Phase-123 substrate match: Munda 'bi' (seed/sprout)")
    b.add("comparative_lexical", "a",
          "stated sound correspondence: Munda 'bi' -> Dravidian "
          "'vi' (voiced bilabial shift p/b->v)",
          "Phonological: Munda 'bi' → Dravidian 'vī' (voiced "
          "bilabial shift p/b→v)")
    b.add("positional_statistic", "a",
          "positional statement: MEDIAL (the basis truncates "
          "after 'after')",
          "Positional: MEDIAL after",
          status_note="the basis as filed truncates mid-clause "
                      "at this item")


@curate("M374")
def _(b):
    b.add("comparative_lexical", "a",
          "substrate match: Munda 'kul' (tiger/king-tiger, "
          "Witzel 1999)",
          "Phase-123 substrate match: Munda 'kul' "
          "(tiger/king-tiger, Witzel 1999)")
    b.add("interpreted_anchor", "b",
          "positional context: MEDIAL between authority signs "
          "(M328=al/man, M073=kon/king) and vessel/cargo signs",
          "Positional: MEDIAL between authority signs "
          "(M328=āl/man, M073=kōṉ/king) and vessel/cargo signs",
          targets=["M328", "M073"],
          reason="the context is stated through the other "
                 "signs under their readings (M328 as al/man, "
                 "M073 as kon/king): an interpreted context, "
                 "struck as such by the adjudication's Q3 item 7")


@curate("M375")
def _(b):
    b.add("iconographic_interpretation", "a",
          "folded-arm sign, read tan 'cool/refreshing' (DEDR "
          "3009) or tantu 'staff/rod'",
          "Folded-arm sign ~ taṇ 'cool/refreshing' (DEDR 3009) "
          "or taṇṭu 'staff/rod'")
    b.add("dictionary_entry", "a", "DEDR 3009 cited for tan",
          "DEDR 3009")
    b.add("positional_statistic", "a",
          "the filed sequence pattern [M375]-M342-M176 occurs "
          "as a sign sequence",
          "[M375]-M342-M176")
    b.add("interpreted_anchor", "b",
          "the NAME_AY_AN pattern read as tan-ay-an = 'cool/"
          "noble man'",
          "Phase-103 NAME_AY_AN pattern: [M375]-M342-M176 "
          "(taṇ-ay-an = 'cool/noble man')",
          targets=["M342", "M176"],
          reason="the pattern's reading rests on M342's and "
                 "M176's readings (ay, an); the adjudication's "
                 "Q3 item 8 removed this translated pattern as "
                 "a major argument")
    b.add("literary_parallel", "a",
          "Sangam Akam poetry: tan- is a common personal name "
          "prefix",
          "Sangam Akam poetry: taṇ- is a common personal name "
          "prefix")
    b.add("corpus_count", "a", "frequency 7 as filed", "Freq=7")


@curate("M362")
def _(b):
    b.add("iconographic_interpretation", "a",
          "starburst / asterisk iconography, read ani "
          "'ornament/adorn' (DEDR 0145)",
          "Starburst / asterisk iconography ~ aṇi "
          "'ornament/adorn' (DEDR 0145)")
    b.add("dictionary_entry", "a", "DEDR 145 cited for ani",
          "DEDR 0145")
    b.add("slot_label", "b",
          "the sign appears in name-slot patterns between "
          "animal classifiers and titles (Phase-103)",
          "appears in name-slot patterns between animal "
          "classifiers and titles",
          reason="the name-slot pattern and its classifier/"
                 "title roles are constructs of the candidate "
                 "system; the adjudication's Q3 item 11 removed "
                 "interpreted-context credit for this reading "
                 "pending provenance",
          target_note="the basis names the slot pattern but "
                      "no individual reading as its premise")
    b.add("literary_parallel", "a",
          "Sangam literature: ani- prefix in personal names "
          "(Ani-van, Ani-tan)",
          "Sangam literature: aṇi- prefix in personal names "
          "(Aṇi-van, Aṇi-tan)")
    b.note("the basis truncates at 'Po;' — the following "
           "segment is not stated and no item is entered for it")


@curate("M398")
def _(b):
    b.add("iconographic_interpretation", "a",
          "hook+ring iconography, read kuri 'mark/sign' (DEDR "
          "1769) or kuru 'small/short'",
          "Hook+ring iconography ~ kuṟi 'mark/sign' (DEDR "
          "1769) or kuṟu 'small/short'")
    b.add("dictionary_entry", "a", "DEDR 1769 cited for kuri",
          "DEDR 1769")
    b.add("slot_label", "b",
          "the sign is filed under the NAME_AY_AN + "
          "GENITIVE_NAME_SUFFIX patterns (Phase-103)",
          "Phase-103: NAME_AY_AN + GENITIVE_NAME_SUFFIX patterns",
          reason="the named patterns are constructs of the "
                 "candidate system's name grammar",
          target_note="the pattern names are constructs; the "
                      "concrete pattern instance is carried as "
                      "its own item")
    b.add("positional_statistic", "a",
          "the filed sequence pattern [M267]-[M398]-[M342] "
          "occurs as a sign sequence",
          "Pattern [M267]-[M398]-[M342]")
    b.add("interpreted_anchor", "b",
          "the pattern read as 'of-kuri-belonging' = genitive "
          "personal name",
          "Pattern [M267]-[M398]-[M342]: 'of-kuṟi-belonging' = "
          "genitive personal name",
          targets=["M267", "M342"],
          reason="the reading of the pattern rests on M267's "
                 "genitive reading and M342's suffix reading; "
                 "struck as a premise by the adjudication's Q3 "
                 "item 9")
    b.add("consistency_score", "ambiguous",
          "a score of 1.2 is filed for this reading (the basis "
          "truncates at '(hi')",
          "Score 1.2 (hi",
          reason="an internal score whose definition and "
                 "inputs the filed basis does not state, and "
                 "whose statement is itself truncated; recorded "
                 "ambiguous under spec section 3.4",
          status_note="the basis as filed truncates mid-clause "
                      "at this item")


@curate("M222")
def _(b):
    b.add("slot_label", "b",
          "the reading was promoted on evidence_type="
          "compound_slot_coherence (anchor staging archive)",
          "evidence_type=compound_slot_coherence",
          reason="slot coherence is a construct of the "
                 "candidate system; the adjudication's Q3 item "
                 "10 removed interpreted-context credit for "
                 "this reading pending provenance",
          target_note="the basis names no individual reading "
                      "as the coherence premise")
    b.add("consistency_score", "ambiguous",
          "staging score=1.00, status=verified as filed",
          "score=1.00; status=verified",
          reason="an internal staging score whose inputs the "
                 "filed basis does not state; recorded "
                 "ambiguous under spec section 3.4")
    b.add("dictionary_entry", "a",
          "DEDR gloss as filed: shine / lightning (verb); no "
          "DEDR number is filed",
          "DEDR: shine / lightning (verb)")
    b.note("SOURCE CONFLICT as filed: the paper's public "
           "anchor table lists this sign's reading as 'kur'; "
           "the canonical anchor register and the audit record "
           "'min' (MEDIUM), with 'kur' a superseded earlier "
           "reading. The log follows the register/audit value, "
           "as the appendix row does")
    b.note("class P as executed is 'pending — no documented "
           "expert or referral' (standings supplement "
           "section 5)")


@curate("M063")
def _(b):
    b.add("motif_association", "a",
          "M063 appears on 3/18 seals with gharial motif; the "
          "measured gharial lift is 4.35",
          "M063 appears on 3/18 seals with gharial motif (vs.",
          status_note="the original filed claim (lift > 5.0 on "
                      "gharial seals, HIGH) FAILED as specified: "
                      "measured lift 4.35 < 5.0 (standings "
                      "supplement section 4; the 2026-05-11 "
                      "fact-check correction in the basis)")
    b.note("the basis truncates at '(vs. ;' — the comparison "
           "clause is not completed in the basis as filed")


@curate("M176")
def _(b):
    b.add("internal_label", "b",
          "the filed basis is the candidate system's own "
          "functional label for the sign: masculine suffix",
          "Masculine suffix",
          reason="no corpus count, dictionary entry, or "
                 "published proposal is filed for this sign; "
                 "the basis is the system's suffix-inventory "
                 "label restated",
          target_note="the label names no other reading; it is "
                      "the system's own assignment")
    b.note("the standings companion records a corrected "
           "terminal-position rate for this sign of 19.1% "
           "(68 of 356 occurrences), replacing an earlier "
           "published rate (appendix row)")


@curate("M342")
def _(b):
    b.add("internal_label", "b",
          "the filed basis is the candidate system's own "
          "functional label for the sign: terminal marker, "
          "Dravidian case suffix",
          "Terminal marker, Dravidian case suffix",
          reason="no corpus count, dictionary entry, or "
                 "published proposal is filed for this sign; "
                 "the basis is the system's suffix-inventory "
                 "label restated",
          target_note="the label names no other reading; it is "
                      "the system's own assignment")
    b.note("the standings companion records a corrected "
           "terminal-position rate for this sign of 12.0% "
           "(70 of 584 occurrences), replacing an earlier "
           "published rate (appendix row)")
    b.note("this sign is the most-depended-on premise in the "
           "94: the dependency record names it as a premise "
           "for M005, M030, M068, M089, M347, M375, M398 and "
           "the already-U checks; those edges are carried on "
           "the depending readings' entries, not here")


@curate("M012")
def _(b):
    b.add("iconographic_interpretation", "a",
          "single stroke, read as the numeral 1",
          "single stroke = numeral 1",
          status_note="numerical claim WEAKENED (standings "
                      "supplement section 6: stroke-count "
                      "pattern 1/141 for this sign)")


@curate("M059")
def _(b):
    b.add("iconographic_interpretation", "a",
          "the sign read as the numeral 7", "Numeral 7",
          status_note="numerical claim WEAKENED (standings "
                      "supplement section 6: stroke-count "
                      "pattern 1/210 for this sign)")


@curate("M391")
def _(b):
    b.add("iconographic_interpretation", "a",
          "numeral/stroke sign, read ka/kan",
          "Numeral/stroke sign",
          status_note="numerical claim WEAKENED (standings "
                      "supplement section 6: stroke-count "
                      "pattern 2/187 for this sign, against "
                      "SUFFIX_ONLY 74/187)")


@curate("M051")
def _(b):
    b.add("iconographic_interpretation", "a",
          "comb/flower sign, read pu/pul", "Comb/flower sign")


@curate("M099")
def _(b):
    b.add("iconographic_interpretation", "a",
          "jar/vessel sign, read kol/kol", "Jar/vessel sign")
    b.note("the audit's evidence lines count a GRAMMAR line "
           "for this reading, but the basis as filed states no "
           "grammatical evidence beyond the iconographic "
           "identification; the falsifiers annex records this "
           "reading's basis as too thin to falsify")


@curate("M162")
def _(b):
    b.add("iconographic_interpretation", "a",
          "house/dwelling sign, read il/il", "House/dwelling sign")


@curate("M233")
def _(b):
    b.add("iconographic_interpretation", "a",
          "settlement/place marker, read ur (town/settlement)",
          "Settlement/place marker")


@curate("M328")
def _(b):
    b.add("iconographic_interpretation", "a",
          "man/person sign, read a/al", "Man/person sign")


@curate("M007")
def _(b):
    b.note("the basis carries two dictionary references that "
           "do not agree: the Phase-255 corroboration cites "
           "DEDR 7 (PDr 'akatti' = agate, a commodity claim "
           "that does not state this reading's own gloss) and "
           "the dictionary-reference segment records DEDR 0340 "
           "(gloss as recorded: person). Both are entered as "
           "filed; the disagreement is recorded, not resolved")


@curate("M065")
def _(b):
    b.note("the Phase-255 corroboration names PDr 'akatti' = "
           "agate (DEDR 7), which is not this reading's gloss "
           "as recorded (jar/pot); the corroboration is "
           "entered as filed and the mismatch recorded, not "
           "resolved")


@curate("M010")
def _(b):
    b.note("the Phase-255 segment truncates in the basis as "
           "filed at 'appears'; the seal-count clause is not "
           "completed and no motif item is entered for it")


@curate("M023")
def _(b):
    b.note("the Phase-255 segment truncates in the basis as "
           "filed at 'appears'; the seal-count clause is not "
           "completed and no motif item is entered for it")


@curate("M025")
def _(b):
    b.note("the Phase-255 segment truncates in the basis as "
           "filed at 'appe'; the seal-count clause is not "
           "completed and no motif item is entered for it")


@curate("M089")
def _(b):
    for item in b.items:
        if item["kind"] in ("corpus_count", "interpreted_anchor"):
            item["status_note"] = (
                "counts unreliable: the Tranche 2 rerun record "
                "filed contradictory pairs for each collocate "
                "(falsifiers annex, Round 2 row annotations, "
                "2026-11-21); the counts are entered as filed")
    b.note("the basis opens with the unelaborated label "
           "'Positional analysis' and truncates at 'collocat;' "
           "after the third collocate; no further premise is "
           "stated and none is entered")
    b.note("the adjudication records this reading's upgrade "
           "counts as internally inconsistent (Q5 tranche "
           "record); the counts are entered as filed")
    b.note("Round 2 amendment (standings supplement): this "
           "reading's class rests on its filed corrected-"
           "battery result (score 2), not on the collocation "
           "counts")


@curate("M048")
def _(b):
    b.note("the basis truncates at 'collocat;' after the "
           "third collocate; no further premise is stated and "
           "none is entered")
    b.note("Round 2 amendment (standings supplement): no "
           "corrected battery result is filed for this sign; "
           "its class rests on the absence of a qualifying "
           "filed result")


@curate("M145")
def _(b):
    b.add("consistency_score", "ambiguous",
          "Phase-95 retroflex expansion score=1.90",
          "Phase-95 retroflex expansion (score=1.90",
          reason="an internal expansion score whose inputs "
                 "the filed basis does not state; recorded "
                 "ambiguous under spec section 3.4")


@curate("M194")
def _(b):
    b.add("consistency_score", "ambiguous",
          "Phase-95 retroflex expansion score=1.90",
          "Phase-95 retroflex expansion (score=1.90",
          reason="an internal expansion score whose inputs "
                 "the filed basis does not state; recorded "
                 "ambiguous under spec section 3.4")


REBUS_GLOSSES = {
    "M049": "fish+mark -> puL (bird/mark on fish)",
    "M052": "fish+stroke -> taNal (mark on fish)",
    "M053": "fish variant -> miiN (fish variant)",
    "M054": "fish+two -> miiNDu (fish again)",
    "M055": "fish+3",
    "M061": "bull+sign -> kaNan (bull+marker)",
    "M076": "comb+3 strokes",
    "M082": "plant+stroke -> pal (plant with mark)",
}

for _sign, _gloss in REBUS_GLOSSES.items():
    def _rebus(b, gloss=_gloss):
        b.add("iconographic_interpretation", "a",
              f"rebus derivation as filed: {gloss}",
              f"Gloss as recorded: {gloss}")
    CURATION.setdefault(_sign, _rebus)


@curate("M087")
def _(b):
    b.add("iconographic_interpretation", "a",
          "gloss as recorded: white / two strokes",
          "Gloss as recorded: white / two strokes")
    b.note("the filed source attributes the reading to "
           "Parpola 1994 (via Phase-51); no DEDR entry number "
           "is filed for this sign")


@curate("M264")
def _(b):
    b.add("iconographic_interpretation", "a",
          "gloss as recorded: female / woman",
          "Gloss as recorded: female / woman")
    b.note("the filed source attributes the reading to "
           "Parpola 1994 (via Phase-51); no DEDR entry number "
           "is filed for this sign")


@curate("M311")
def _(b):
    b.add("iconographic_interpretation", "a",
          "gloss as recorded: north star",
          "Gloss as recorded: north star")
    b.note("the filed source attributes the reading to "
           "Parpola 1994 (via Phase-51); no DEDR entry number "
           "is filed for this sign")


# ---------------------------------------------------------------- main


def build(appendix_text: str, standings_text: str) -> dict:
    appendix = parse_appendix(appendix_text)
    standings = parse_standings(standings_text)
    # Round 2 amendment to the standings record (2026-11-21):
    # M044 was adjudicated under the addendum rule and takes
    # class U. The amendment is an appended section, not a
    # table edit, so it is applied here — and asserted, so a
    # standings text that loses the amendment fails the build
    # rather than silently restoring the superseded class.
    if "## Round 2 amendment" in standings_text:
        assert "M044 takes class U" in standings_text
        assert standings["M044"]["executed_class"] == "E"
        standings["M044"]["executed_class"] = "U"
    assert len(appendix) == 94, len(appendix)
    assert len(standings) == 94, len(standings)
    assert set(appendix) == set(standings), (
        set(appendix) ^ set(standings))
    entries = []
    for sign, st in standings.items():
        ap = appendix[sign]
        assert ap["reading"] == st["reading"], (
            sign, ap["reading"], st["reading"])
        b = EntryBuilder(sign, ap["basis"])
        seg_items(b)
        if sign in CURATION:
            CURATION[sign](b)
        assert b.items, sign
        # The corrected-battery / site-statistics outcome is the
        # appendix's trailing sentence for the row; it renders
        # last. Renumber after the stable sort.
        b.items.sort(key=lambda i: 1 if i["kind"] ==
                     "corrected_validation" else 0)
        for n, item in enumerate(b.items, 1):
            item["id"] = f"{sign}-{n:02d}"
        entries.append({
            "sign": sign,
            "reading": st["reading"],
            "executed_class": st["executed_class"],
            "q4_flag": st["q4_flag"],
            "basis_as_filed": ap["basis"],
            "items": b.items,
            "entry_notes": b.notes,
        })
    census = {"a": 0, "b": 0, "ambiguous": 0}
    for e in entries:
        for i in e["items"]:
            census[i["type"]] += 1
    return {
        "artifact": "inference-log",
        "spec": "099-inference-log",
        "version": "1.0 (Stage 1, 2026-11-21)",
        "sources": {
            "bases": "coscientist-audit-94 package appendix "
                     "(APPENDIX-94.md), the basis text as filed "
                     "from the register",
            "standings": "specs/091-anchor-comparison-integrity/"
                         "records/standings-relabel-execution-"
                         "2026-11-21.md (executed classes and Q4 "
                         "flags), as amended by its Round 2 "
                         "amendment (M044 to class U; records/"
                         "m044-addendum-adjudication-2026-11-21.md)",
            "annotations": "standings-supplement-2026-11-21.md; "
                           "dependency-record-2026-11-21.md; "
                           "coscientist-audit-94-adjudication-"
                           "2026-11-21.md (status notes only)",
        },
        "edge_census": census,
        "entries": entries,
    }


def render(log: dict) -> str:
    c = log["edge_census"]
    total = sum(c.values())
    lines = [
        "# The inference log for the 94 strict-core readings",
        "",
        "Spec 099 Stage 1, filed 2026-11-21. Generated from "
        "`inference-log.json` by `tools/build_inference_log.py`; "
        "the JSON is the record of record and this rendering is "
        "never edited separately.",
        "",
        f"Entries: {len(log['entries'])}. Items: {total} "
        f"({c['a']} primary (a), {c['b']} other-reading / "
        f"candidate-system (b), {c['ambiguous']} ambiguous).",
        "",
        "Item types: **a** = primary evidence; **b** = another "
        "reading or a candidate-system construct used as "
        "evidence; **ambiguous** = the filed basis does not "
        "state the item's inputs. Status notes carry the "
        "landed annotations (withdrawn, FAILED, struck, "
        "not reproducible) with their sources.",
        "",
    ]
    for e in log["entries"]:
        lines.append(f"## {e['sign']} — {e['reading']} "
                     f"(class {e['executed_class']}, Q4 {e['q4_flag']})")
        lines.append("")
        lines.append(f"> {e['basis_as_filed']}")
        lines.append("")
        lines.append("| Item | Kind | Type | Statement | Targets | Notes |")
        lines.append("|---|---|---|---|---|---|")
        for i in e["items"]:
            notes = []
            if i.get("reason"):
                notes.append("Reason: " + i["reason"])
            if i.get("target_note"):
                notes.append("Target note: " + i["target_note"])
            if i.get("target_source"):
                notes.append("Target source: " + i["target_source"])
            if i.get("status_note"):
                notes.append("Status: " + i["status_note"])
            lines.append(
                f"| {i['id']} | {i['kind']} | {i['type']} | "
                f"{i['statement']} | "
                f"{', '.join(i['targets']) or '—'} | "
                f"{' '.join(notes) or '—'} |")
        lines.append("")
        for n in e["entry_notes"]:
            lines.append(f"- Note: {n}")
        if e["entry_notes"]:
            lines.append("")
    return "\n".join(lines)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("appendix")
    ap.add_argument("relabel")
    ap.add_argument("--out", required=True)
    ap.add_argument("--render", required=True)
    args = ap.parse_args(argv)
    log = build(open(args.appendix, encoding="utf-8").read(),
                open(args.relabel, encoding="utf-8").read())
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=1,
                  sort_keys=False)
        fh.write("\n")
    with open(args.render, "w", encoding="utf-8") as fh:
        fh.write(render(log))
    c = log["edge_census"]
    print(f"built {len(log['entries'])} entries; census "
          f"a={c['a']} b={c['b']} ambiguous={c['ambiguous']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
