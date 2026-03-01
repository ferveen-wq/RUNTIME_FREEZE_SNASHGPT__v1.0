#!/usr/bin/env python3
"""
Sync test cases from a source JSON array into a wrapper JSON array.

Use-case:
  - Maintain a dedicated suite file (e.g., regression_ppf_matte_audit.json)
  - Mirror those cases into a wrapper pack (e.g., regression_cases_uat__ppf_matte_audit.json)
    so the wrapper stays representative without manual copy/paste.

Behavior:
  - Loads source + wrapper files as JSON arrays of objects
  - Appends any source cases missing in wrapper (by case_id)
  - Preserves existing wrapper order; new cases appended at end
  - Writes back pretty-printed JSON (2-space indent)
  - Exits non-zero if inputs are not valid JSON arrays
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set


def _load_json_array(path: Path) -> List[Dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise ValueError(f"Failed to parse JSON: {path} ({e})")
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array at: {path}")
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Expected each array element to be an object at: {path} (index {i})")
    return data  # type: ignore[return-value]


def _index_case_ids(cases: List[Dict[str, Any]], path: Path) -> Set[str]:
    ids: Set[str] = set()
    for i, c in enumerate(cases):
        cid = c.get("case_id")
        if not isinstance(cid, str) or not cid.strip():
            raise ValueError(f"Missing/invalid case_id at {path} index {i}")
        if cid in ids:
            raise ValueError(f"Duplicate case_id '{cid}' inside {path}")
        ids.add(cid)
    return ids


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="Source JSON array file (cases to mirror)")
    ap.add_argument("--wrapper", required=True, help="Wrapper JSON array file (destination pack)")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write; just print what would change",
    )
    args = ap.parse_args()

    source_path = Path(args.source)
    wrapper_path = Path(args.wrapper)

    if not source_path.exists():
        print(f"ERROR: source not found: {source_path}", file=sys.stderr)
        return 2
    if not wrapper_path.exists():
        print(f"ERROR: wrapper not found: {wrapper_path}", file=sys.stderr)
        return 2

    try:
        source_cases = _load_json_array(source_path)
        wrapper_cases = _load_json_array(wrapper_path)
        source_ids = _index_case_ids(source_cases, source_path)
        wrapper_ids = _index_case_ids(wrapper_cases, wrapper_path)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    missing = [c for c in source_cases if c["case_id"] not in wrapper_ids]

    if not missing:
        print("OK: wrapper already contains all source case_id entries.")
        return 0

    print(f"INFO: {len(missing)} case(s) will be appended to wrapper:")
    for c in missing:
        print(f"  - {c['case_id']}")

    if args.dry_run:
        print("DRY-RUN: no files written.")
        return 0

    new_wrapper = wrapper_cases + missing

    # Safety: ensure we didn't introduce duplicates
    _ = _index_case_ids(new_wrapper, wrapper_path)

    wrapper_path.write_text(json.dumps(new_wrapper, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"DONE: wrote {wrapper_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
