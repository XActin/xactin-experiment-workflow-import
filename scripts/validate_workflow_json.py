# -*- coding: utf-8 -*-
"""Validate an XActin experiment workflow import JSON against nodes-catalog.json.

Usage:
  python scripts/validate_workflow_json.py path/to/workflow.json
  python scripts/validate_workflow_json.py path/to/workflow.json --catalog path/to/nodes-catalog.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)
    return json.loads(text)


def normalize(spec: dict):
    if not isinstance(spec, dict):
        raise ValueError("root must be object")
    if isinstance(spec.get("steps"), list) and spec["steps"]:
        nodes = []
        for i, code in enumerate(spec["steps"]):
            if not isinstance(code, str) or not code.strip():
                raise ValueError(f"steps[{i}] must be non-empty string")
            pos = None
            if isinstance(spec.get("step_positions"), list) and i < len(spec["step_positions"]):
                p = spec["step_positions"][i]
                if isinstance(p, dict) and p.get("x") is not None and p.get("y") is not None:
                    pos = {"x": float(p["x"]), "y": float(p["y"])}
            swapped = (
                isinstance(spec.get("step_ports_swapped"), list)
                and i < len(spec["step_ports_swapped"])
                and spec["step_ports_swapped"][i] is True
            )
            step_ids = spec.get("step_ids") or []
            node_id = step_ids[i] if i < len(step_ids) and step_ids[i] else f"step_{i}"
            nodes.append(
                {
                    "id": node_id,
                    "code": code.strip(),
                    "position": pos,
                    "ports_swapped": swapped,
                }
            )
        edges = [
            {"source": nodes[i]["id"], "target": nodes[i + 1]["id"]}
            for i in range(len(nodes) - 1)
        ]
        return nodes, edges

    nodes_raw = spec.get("nodes")
    if not isinstance(nodes_raw, list):
        raise ValueError("missing nodes[] or steps[]")
    nodes = []
    for i, n in enumerate(nodes_raw):
        if not isinstance(n, dict):
            raise ValueError(f"nodes[{i}] must be object")
        code = n.get("code") or n.get("node_code") or n.get("type")
        if not isinstance(code, str) or not code.strip():
            raise ValueError(f"nodes[{i}] missing code")
        pos = n.get("position")
        position = None
        if isinstance(pos, dict) and pos.get("x") is not None and pos.get("y") is not None:
            position = {"x": float(pos["x"]), "y": float(pos["y"])}
        nodes.append(
            {
                "id": str(n["id"]) if n.get("id") not in (None, "") else f"node_{i}",
                "code": code.strip(),
                "position": position,
                "ports_swapped": n.get("ports_swapped") is True or n.get("portsSwapped") is True,
            }
        )
    edges_raw = spec.get("edges") or []
    if not isinstance(edges_raw, list):
        raise ValueError("edges must be array")
    edges = []
    for i, e in enumerate(edges_raw):
        if not isinstance(e, dict) or not e.get("source") or not e.get("target"):
            raise ValueError(f"edges[{i}] needs source and target")
        edge = {"source": str(e["source"]), "target": str(e["target"])}
        if e.get("sourceHandle"):
            edge["sourceHandle"] = str(e["sourceHandle"])
        edges.append(edge)
    return nodes, edges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow")
    parser.add_argument("--catalog", default=str(SKILL_ROOT / "nodes-catalog.json"))
    args = parser.parse_args()

    catalog = load_json(Path(args.catalog))
    codes = {n["code"] for n in catalog.get("nodes") or []}
    nodes, edges = normalize(load_json(Path(args.workflow)))

    errors = []
    ids = set()
    for n in nodes:
        if n["id"] in ids:
            errors.append(f"duplicate id: {n['id']}")
        ids.add(n["id"])
        if n["code"] not in codes:
            errors.append(f"unknown code: {n['code']}")

    for e in edges:
        if e["source"] not in ids:
            errors.append(f"edge source missing: {e['source']}")
        if e["target"] not in ids:
            errors.append(f"edge target missing: {e['target']}")

    by_id = {n["id"]: n for n in nodes}
    meta = {n["code"]: n for n in catalog.get("nodes") or []}
    warnings = []
    for e in edges:
        src = by_id.get(e["source"])
        tgt = by_id.get(e["target"])
        if not src or not tgt:
            continue
        sm = meta.get(src["code"]) or {}
        tm = meta.get(tgt["code"]) or {}
        down = sm.get("downstream_compatibility") or []
        up = tm.get("upstream_compatibility") or []
        if down and tgt["code"] not in down:
            warnings.append(
                f'{src["code"]} -> {tgt["code"]}: target not in source downstream_compatibility'
            )
        if up and src["code"] not in up:
            warnings.append(
                f'{src["code"]} -> {tgt["code"]}: source not in target upstream_compatibility'
            )

    if errors:
        print("FAIL")
        for err in errors:
            print("  error:", err)
        for w in warnings:
            print("  warn:", w)
        sys.exit(1)
    print("OK", f"{len(nodes)} nodes,", f"{len(edges)} edges")
    for w in warnings:
        print("  warn:", w)


if __name__ == "__main__":
    main()
