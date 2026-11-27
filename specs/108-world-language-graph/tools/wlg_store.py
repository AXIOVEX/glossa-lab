"""Canonical stream IO and hashing for the World Language Graph.

The canonical serialisation (design 5.4) is the stream files
themselves: records in ID order, one JSON object per line,
UTF-8, keys sorted. The graph snapshot hash is SHA-256 over
the concatenation of nodes, edges, assertions, and gaps
streams in that order; the source-manifest hash is SHA-256
over the sources stream.
"""

import hashlib
import json
import sys
import time

STREAMS = ["sources", "nodes", "edges", "assertions", "gaps", "releases", "baseline-links"]


def progress(done, total, label):
    """Timestamped progress indicator (fleet constraint, 2026-11-26)."""
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{ts}] PROGRESS {label}: {done}/{total}", flush=True, file=sys.stderr)


def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def dump_jsonl(path, rows, id_field):
    rows = sorted(rows, key=lambda r: r[id_field])
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return rows


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot_hash(graph_dir):
    h = hashlib.sha256()
    for name in ["nodes", "edges", "assertions", "gaps"]:
        with open(f"{graph_dir}/{name}.jsonl", "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()


def manifest_hash(graph_dir):
    return file_sha256(f"{graph_dir}/sources.jsonl")
