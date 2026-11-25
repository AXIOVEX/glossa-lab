#!/usr/bin/env python3
"""Spec 105 Stage 1 execution: build the three stripped sandbox
datasets and run the L0-L1 derivations (spec.md sections 3 and 5;
test cases TC-105-02..TC-105-06).

Run on tower-compute. Datasets are written to the custody directory
(~/glossa-custody/spec105/) and never committed. The script prints a
JSON summary to stdout; the summary is filed as the raw output of
record. Each sandbox is processed independently: a failure stops
that sandbox only and is reported with its step and evidence.
"""
import csv, hashlib, io, json, os, subprocess, sys

HOME = os.path.expanduser("~")
CUSTODY = os.path.join(HOME, "glossa-custody", "spec105")
REPO = os.path.join(HOME, ".syncyard", "worktrees", "glossa", "spec105-stage1")

PINS = {
    "holdat_csv": "62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e",
    "ete_corpus": "2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597",
    "ete_intake": "8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a",
    "mer_jsonl": "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4",
}
PATHS = {
    "holdat_csv": os.path.join(CUSTODY, "sources", "indus_corpus_2.csv"),
    "ete_corpus": os.path.join(REPO, "specs/096-eteocypriot-program/corpus/corpus.json"),
    "ete_intake": os.path.join(REPO, "specs/096-eteocypriot-program/corpus/corpus-androkles-intake-2026-11-22.json"),
    "mer_jsonl": os.path.join(HOME, ".syncyard/worktrees/glossa/kovetsky-src/data/inscriptions.jsonl"),
}

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def write_dataset(name, artifacts):
    path = os.path.join(CUSTODY, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(artifacts, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    return path, sha256_file(path)

def census(artifacts):
    lines = sum(len(a["lines"]) for a in artifacts)
    groups = sum(len(l) for a in artifacts for l in a["lines"])
    tokens = sum(len(g) for a in artifacts for l in a["lines"] for g in l)
    return {"artifacts": len(artifacts), "lines": lines,
            "groups": groups, "tokens": tokens}

def inventory_impl_a(dataset_path):
    """L0-L1, implementation A: parse the dataset JSON and collect
    the set of distinct marks (sameness as recorded)."""
    data = json.load(open(dataset_path, encoding="utf-8"))
    marks = set()
    for art in data:
        for line in art["lines"]:
            for group in line:
                for m in group:
                    marks.add(m)
    return marks

def inventory_impl_b(dataset_path):
    """L0-L1, implementation B (independent): a jq + sort pipeline
    over the dataset's raw bytes; no shared code with A."""
    jq = subprocess.run(
        ["jq", "-r", ".[].lines[][][]", dataset_path],
        capture_output=True, text=True, check=True)
    srt = subprocess.run(
        ["sort", "-u"], input=jq.stdout, capture_output=True,
        text=True, check=True,
        env={**os.environ, "LC_ALL": "C"})
    return set(srt.stdout.splitlines())

# ---------------------------------------------------------------- Indus
def build_indus():
    if sha256_file(PATHS["holdat_csv"]) != PINS["holdat_csv"]:
        return {"status": "STOPPED", "step": "source pin check",
                "evidence": "Holdat CSV hash differs from the Spec 100 pin"}
    with open(PATHS["holdat_csv"], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_form = {}
    for r in rows:
        by_form.setdefault(r["form"], []).append(r)
    seal_ids = []
    for form, rs in by_form.items():
        sids = {r["seal_id"] for r in rs}
        assert len(sids) == 1, f"form {form} carries multiple seal_ids"
        seal_ids.append((rs[0]["seal_id"], form))
    def sid_key(v):
        return (0, int(v)) if v.lstrip("-").isdigit() else (1, v)
    ordered = [form for _, form in sorted(seal_ids, key=lambda t: sid_key(t[0]))]
    artifacts = []
    for form in ordered:
        rs = sorted(by_form[form], key=lambda r: int(r["position"]))
        positions = [int(r["position"]) for r in rs]
        assert positions == list(range(len(rs))), \
            f"positions not contiguous from 0 in {form}: {positions[:8]}"
        artifacts.append({"lines": [[[r["letters"] for r in rs]]]})
    derivation = [a for i, a in enumerate(artifacts) if i % 5 != 4]
    reserve = [a for i, a in enumerate(artifacts) if i % 5 == 4]
    dp, dhash = write_dataset("indus-derivation.json", derivation)
    rp, rhash = write_dataset("indus-reserve.json", reserve)
    return {"status": "BUILT", "artifacts_total": len(artifacts),
            "derivation": {**census(derivation), "path": dp, "sha256": dhash},
            "reserve": {**census(reserve), "path": rp, "sha256": rhash}}

def check_indus(built):
    """TC-105-02: independent re-read of the CSV; token-for-token
    comparison against both datasets, in order."""
    with open(PATHS["holdat_csv"], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    forms = {}
    for r in rows:
        forms.setdefault(r["form"], []).append(
            (int(r["position"]), r["seal_id"], r["letters"]))
    order = sorted(forms, key=lambda fm: (
        (0, int(forms[fm][0][1])) if forms[fm][0][1].lstrip("-").isdigit()
        else (1, forms[fm][0][1])))
    expected = []
    for fm in order:
        toks = [t for _, _, t in sorted(forms[fm])]
        expected.append({"lines": [[toks]]})
    got = []
    for name in ("indus-derivation.json", "indus-reserve.json"):
        got.append(json.load(open(os.path.join(CUSTODY, name), encoding="utf-8")))
    merged = [None] * len(expected)
    di = ri = 0
    for i in range(len(expected)):
        if i % 5 == 4:
            merged[i] = got[1][ri]; ri += 1
        else:
            merged[i] = got[0][di]; di += 1
    assert merged == expected, "Indus datasets differ from the recorded streams"
    return {"tc": "TC-105-02", "result": "PASS",
            "artifacts_compared": len(expected)}

# ----------------------------------------------------------- Eteocypriot
def _ete_segments(line_objs):
    return [[list(seg) for seg in obj["segments"]] for obj in line_objs]

def build_eteocypriot():
    for key in ("ete_corpus", "ete_intake"):
        if sha256_file(PATHS[key]) != PINS[key]:
            return {"status": "STOPPED", "step": "source pin check",
                    "evidence": f"{key} hash differs from the recorded bytes pinned in spec section 3.2"}
    corpus = json.load(open(PATHS["ete_corpus"], encoding="utf-8"))
    intake = json.load(open(PATHS["ete_intake"], encoding="utf-8"))
    by_id = {r["id"]: r for r in corpus["inscriptions"]}
    by_id_i = {r["id"]: r for r in intake["inscriptions"]}
    ics196 = by_id["ICS196"]
    assert ics196.get("split") == "development"
    art1 = {"lines": _ete_segments(ics196["eteocypriot_lines"])}
    andr = by_id_i["ANDROKLES-A"]
    art2 = {"lines": _ete_segments(andr["eteocypriot_side"]["lines"])}
    artifacts = [art1, art2]
    p, h = write_dataset("eteocypriot.json", artifacts)
    return {"status": "BUILT", **census(artifacts), "path": p, "sha256": h}

def check_eteocypriot(built):
    """TC-105-03 (Eteocypriot half): independent re-read and
    token-for-token comparison."""
    corpus = json.load(open(PATHS["ete_corpus"], encoding="utf-8"))
    intake = json.load(open(PATHS["ete_intake"], encoding="utf-8"))
    by_id = {r["id"]: r for r in corpus["inscriptions"]}
    by_id_i = {r["id"]: r for r in intake["inscriptions"]}
    expected = [
        {"lines": [[list(s) for s in o["segments"]]
                   for o in by_id["ICS196"]["eteocypriot_lines"]]},
        {"lines": [[list(s) for s in o["segments"]]
                   for o in by_id_i["ANDROKLES-A"]["eteocypriot_side"]["lines"]]},
    ]
    got = json.load(open(os.path.join(CUSTODY, "eteocypriot.json"), encoding="utf-8"))
    assert got == expected, "Eteocypriot dataset differs from the recorded streams"
    return {"tc": "TC-105-03 (Eteocypriot)", "result": "PASS",
            "artifacts_compared": 2}

# -------------------------------------------------------------- Meroitic
def build_meroitic():
    if sha256_file(PATHS["mer_jsonl"]) != PINS["mer_jsonl"]:
        return {"status": "STOPPED", "step": "source pin check",
                "evidence": "inscriptions.jsonl hash differs from the pin in spec section 3.3"}
    artifacts = []
    with open(PATHS["mer_jsonl"], encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            if row.get("text") is None:
                continue
            groups = [list(g) for g in row["text"].split(" ")]
            artifacts.append({"lines": [groups]})
    p, h = write_dataset("meroitic.json", artifacts)
    return {"status": "BUILT", **census(artifacts), "path": p, "sha256": h}

def check_meroitic(built):
    """TC-105-03 (Meroitic half): independent re-read and
    token-for-token comparison."""
    expected = []
    with open(PATHS["mer_jsonl"], encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            if row.get("text") is None:
                continue
            expected.append({"lines": [[list(g) for g in row["text"].split(" ")]]})
    got = json.load(open(os.path.join(CUSTODY, "meroitic.json"), encoding="utf-8"))
    assert got == expected, "Meroitic dataset differs from the recorded streams"
    return {"tc": "TC-105-03 (Meroitic)", "result": "PASS",
            "artifacts_compared": len(expected)}

# ------------------------------------------------- stripping verification
BLOCKLIST = ["gloss", "translation", "transliteration", "mahadevan",
             "cisi", "seal_id", "iconography", "sign_id", "rem_no",
             "reading", "lexicon", "grammar", "site", "upos", "xpos",
             "morpheme", "lemma", "ICS196", "ICS 196", "ANDROKLES",
             "ICS193", "ICS194", "ICS217"]

def check_stripping():
    """TC-105-04: schema exactness, blocklist scan, and absence of
    source identifiers over all four datasets."""
    findings = []
    for name in ("indus-derivation.json", "indus-reserve.json",
                 "eteocypriot.json", "meroitic.json"):
        path = os.path.join(CUSTODY, name)
        raw = open(path, encoding="utf-8").read()
        data = json.loads(raw)
        assert isinstance(data, list)
        for art in data:
            assert set(art.keys()) == {"lines"}, f"{name}: artifact keys {set(art.keys())}"
            for line in art["lines"]:
                assert isinstance(line, list)
                for group in line:
                    assert isinstance(group, list)
                    for m in group:
                        assert isinstance(m, str) and m != "", f"{name}: bad mark {m!r}"
        for term in BLOCKLIST:
            if term in raw:
                findings.append(f"{name}: blocklist term present: {term}")
    assert not findings, "; ".join(findings)
    return {"tc": "TC-105-04", "result": "PASS",
            "datasets_scanned": 4, "blocklist_terms": len(BLOCKLIST)}

# ------------------------------------------------------------------ main
def derive(name, dataset_file):
    a = inventory_impl_a(os.path.join(CUSTODY, dataset_file))
    b = inventory_impl_b(os.path.join(CUSTODY, dataset_file))
    assert a == b, f"{name}: implementations disagree ({len(a)} vs {len(b)})"
    return {"sandbox": name, "inventory_size": len(a),
            "inventory": sorted(a), "implementations_agree": True}

def main():
    os.makedirs(CUSTODY, exist_ok=True)
    out = {"custody": CUSTODY, "sandboxes": {}, "checks": []}

    indus = build_indus()
    out["sandboxes"]["indus"] = indus
    if indus["status"] == "BUILT":
        out["checks"].append(check_indus(indus))
        out["sandboxes"]["indus"]["derivation_result"] = derive(
            "indus", "indus-derivation.json")
        # TC-105-06: reserve seal + partition discipline.
        assert indus["derivation"]["artifacts"] + indus["reserve"]["artifacts"] \
            == indus["artifacts_total"]
        out["checks"].append({
            "tc": "TC-105-06", "result": "PASS",
            "reserve_sha256": indus["reserve"]["sha256"],
            "derivation_artifacts": indus["derivation"]["artifacts"],
            "reserve_artifacts": indus["reserve"]["artifacts"]})

    ete = build_eteocypriot()
    out["sandboxes"]["eteocypriot"] = ete
    if ete["status"] == "BUILT":
        out["checks"].append(check_eteocypriot(ete))
        out["sandboxes"]["eteocypriot"]["derivation_result"] = derive(
            "eteocypriot", "eteocypriot.json")

    mer = build_meroitic()
    out["sandboxes"]["meroitic"] = mer
    if mer["status"] == "BUILT":
        out["checks"].append(check_meroitic(mer))
        out["sandboxes"]["meroitic"]["derivation_result"] = derive(
            "meroitic", "meroitic.json")

    if all(s["status"] == "BUILT" for s in out["sandboxes"].values()):
        out["checks"].append(check_stripping())
        out["checks"].append({
            "tc": "TC-105-05", "result": "PASS",
            "note": "both L0-L1 implementations agree in all three sandboxes; "
                    "each derivation read only its own sandbox's derivation dataset"})

    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
