"""Spec 098 Stage 1 runner: provenance census (T101), M044/M374
resolution (T102), power grid (T103), and the seal (T104).

Run on tower-compute from a fresh clone. Modes:
  census  — T101 census + T102 resolution + T103 grid data.
            Writes records/stage1-grid-2026-11-21.json and prints
            payload verdict lines. Exit 0 iff every check passes.
  seal    — T104: generate the held-out cluster list under the
            frozen rule, write it to the custody path outside the
            repository, print count + seal hash only, and verify
            the seal recomputes via tools/seal_and_score.py.

The population is the frozen annex population as amended by the
WS2 relabel execution of 2026-11-21 (M202 struck from Arm E to
class U): Arm I 65 signs + Arm E 5 signs (M044, M047, M124,
M329, M330) = 70 signs.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC_DIR = HERE.parent
REPO = SPEC_DIR.parents[1]
sys.path.insert(0, str(HERE))
from seal_and_score import seal_hash, split_clusters, verify_seal  # noqa: E402

EXPORT = REPO / "glossa-corpus/indus/exports/indus_research.jsonl"
EXPORT_SHA_PIN = "08fc96c8dbc22a37effb65e789b22b144f4baf22be1da55dc3d84db5dc44505e"
CROSSWALK = REPO / "backend/glossa_lab/data/mahadevan_parpola_crosswalk_v2.json"
ANNEX = SPEC_DIR / "records/population-annex-2026-11-21.md"
GRID_OUT = SPEC_DIR / "records/stage1-grid-2026-11-21.json"
CUSTODY = Path.home() / "glossa-custody/spec098/heldout-clusters-v1.txt"

ARM_E = ["M044", "M047", "M124", "M329", "M330"]  # as amended by WS2 (M202 struck)


def load_records():
    sha = hashlib.sha256(EXPORT.read_bytes()).hexdigest()
    assert sha == EXPORT_SHA_PIN, f"corpus pin mismatch: {sha}"
    return [json.loads(l) for l in EXPORT.open(encoding="utf-8") if l.strip()]


def seq_bearing(r):
    return any(t is not None for t in (r.get("canonical_grapheme_ids") or []))


def clusters(records):
    """Deduplicate sequence-bearing records on the normalized
    diplomatic code; cluster_id is the lowest glossa_id (freeze s.2)."""
    by_code = {}
    for r in records:
        if not seq_bearing(r):
            continue
        code = r.get("text_code_diplomatic_normalized") or ""
        by_code.setdefault(code, []).append(r)
    out = {}
    for code, rs in by_code.items():
        rs.sort(key=lambda r: r["glossa_id"])
        out[rs[0]["glossa_id"]] = rs[0]
    return out


def sign_tokens(r):
    """Canonical tokens of one record, normalised to M-form."""
    out = []
    for t in r.get("canonical_grapheme_ids") or []:
        if t is None:
            continue
        t = t.lstrip("*")
        if t.startswith("M"):
            out.append(t)
        elif t.isdigit():
            out.append("M" + t.zfill(3))
        else:
            out.append(t)
    return out


def population():
    text = ANNEX.read_text(encoding="utf-8")
    arm_i = []
    in_i = False
    for line in text.splitlines():
        if line.startswith("## Arm I"):
            in_i = True
            continue
        if line.startswith("## Arm E"):
            in_i = False
        if in_i:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) > 2 and parts[1].startswith("M") and parts[1][1:].isdigit():
                arm_i.append(parts[1])
    assert len(arm_i) == 65, len(arm_i)
    return arm_i, list(ARM_E)


def census(records):
    tot = Counter()
    seq = Counter()
    for r in records:
        tot[r["source_system"]] += 1
        if seq_bearing(r):
            seq[r["source_system"]] += 1
    return tot, seq


def resolve_gaps(records):
    """T102: exhaustive attestation search for M044 and M374 in the
    canonical field and in both diplomatic fields, all decorations
    stripped; resolution of M044 under the frozen crosswalk."""
    cw = json.loads(CROSSWALK.read_text(encoding="utf-8"))["crosswalk"]
    by_pnum = {}
    for mid, e in cw.items():
        if e.get("parpola_num") is not None:
            by_pnum[int(e["parpola_num"])] = (mid, e)

    def bare(tok):
        return tok.strip().lstrip("*").lstrip("+")

    hits = {"M044": [], "M374": []}
    for r in records:
        for field in ("text_code_diplomatic_normalized", "text_code_diplomatic"):
            code = (r.get(field) or "").strip("+")
            if not code:
                continue
            for tok in code.split("-"):
                b = bare(tok)
                if b in ("044", "44") and r["sign_id_scheme"] == "Parpola1982":
                    hits["M044"].append((r["glossa_id"], r["source_system"], field, tok))
                if b == "374":
                    hits["M374"].append((r["glossa_id"], r["source_system"], field, tok,
                                          r.get("sign_id_scheme")))
        for t in r.get("canonical_grapheme_ids") or []:
            if t in ("M044", "M374"):
                hits[t].append((r["glossa_id"], r["source_system"], "canonical", t))

    result = {}
    # M044 resolution: the Parpola-coded attestation(s) under the crosswalk.
    m044_records = sorted({h[0] for h in hits["M044"]})
    resolved = []
    for gid in m044_records:
        r = next(x for x in records if x["glossa_id"] == gid)
        code = (r["text_code_diplomatic_normalized"] or "").strip("+")
        seq = []
        for tok in code.split("-"):
            b = bare(tok)
            if b.isdigit() and int(b) in by_pnum:
                seq.append(by_pnum[int(b)][0])
            else:
                seq.append(None)
        resolved.append({"glossa_id": gid, "diplomatic": code,
                         "resolved_sequence": seq,
                         "m044_crosswalk": cw.get("M044")})
    result["M044"] = {"attestations": hits["M044"], "resolved": resolved,
                      "crosswalk_entry": cw.get("M044")}
    result["M374"] = {"attestations": hits["M374"],
                      "crosswalk_entry": cw.get("M374")}
    return result


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "census"
    records = load_records()
    print(f"corpus pin verified: {EXPORT_SHA_PIN[:12]}... records={len(records)}")
    tot, seq = census(records)
    print("T101 census (source: total / sequence-bearing):")
    for s in sorted(tot):
        print(f"  {s}: {tot[s]} / {seq[s]}")
    print(f"  TOTAL: {sum(tot.values())} / {sum(seq.values())}")

    cl = clusters(records)
    print(f"clusters over sequence-bearing records: {len(cl)}")
    dev_ids, held_ids = split_clusters(sorted(cl))
    print(f"split: dev={len(dev_ids)} held={len(held_ids)}")

    if mode == "seal":
        CUSTODY.parent.mkdir(parents=True, exist_ok=True)
        CUSTODY.write_text("".join(c + "\n" for c in held_ids), encoding="utf-8")
        h = seal_hash(held_ids)
        ok = verify_seal(held_ids, h)
        reread = [l.strip() for l in CUSTODY.read_text(encoding="utf-8").splitlines() if l.strip()]
        ok = ok and verify_seal(reread, h) and len(reread) == len(held_ids)
        print(f"PAYLOAD VERDICT T104: clusters={len(cl)} held_out={len(held_ids)} "
              f"seal_sha256={h} custody={CUSTODY} verify={ok}")
        return 0 if ok else 1

    gaps = resolve_gaps(records)
    g44 = gaps["M044"]
    print(f"T102 M044: attestations={len(g44['attestations'])} "
          f"crosswalk={'yes' if g44['crosswalk_entry'] else 'no'}")
    for rr in g44["resolved"]:
        print(f"  resolved {rr['glossa_id']}: {rr['diplomatic']} -> {rr['resolved_sequence']}")
    g374 = gaps["M374"]
    print(f"T102 M374: attestations={len(g374['attestations'])} "
          f"crosswalk={'yes' if g374['crosswalk_entry'] else 'no'}")
    m044_ok = (len(g44["resolved"]) >= 1 and g44["crosswalk_entry"] is not None
               and all("M044" in (rr["resolved_sequence"] or []) for rr in g44["resolved"]))
    m374_ok = len(g374["attestations"]) == 0 and g374["crosswalk_entry"] is None
    print(f"PAYLOAD VERDICT T102: M044_resolved={m044_ok} M374_unattested={m374_ok}")

    arm_i, arm_e = population()
    pop = arm_i + arm_e
    devset = set(dev_ids)
    dev_tokens = Counter()
    for cid, r in cl.items():
        if cid in devset:
            dev_tokens.update(sign_tokens(r))
    grid = []
    for s in pop:
        d = dev_tokens.get(s, 0)
        exp_held = d / 4.0
        grid.append({
            "sign": s,
            "arm": "I" if s in arm_i else "E",
            "dev_tokens": d,
            "expected_heldout_tokens": round(exp_held, 2),
            "meets_count_floor_expected": exp_held >= 5,
            "min_detectable_margin_nats_per_token": (round(10.0 / exp_held, 3)
                                                     if exp_held > 0 else None),
        })
    GRID_OUT.write_text(json.dumps({"population": len(pop), "grid": grid},
                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_floor = sum(1 for g in grid if g["meets_count_floor_expected"])
    print(f"T103 grid: population={len(pop)} signs; expected to meet the 5-token "
          f"floor: {n_floor}; below: {len(pop) - n_floor}")
    print(f"PAYLOAD VERDICT T103: grid_written={GRID_OUT.name} population={len(pop)}")
    ok = m044_ok and m374_ok and sum(seq.values()) == 3033
    print(f"PAYLOAD VERDICT STAGE1-CENSUS: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
