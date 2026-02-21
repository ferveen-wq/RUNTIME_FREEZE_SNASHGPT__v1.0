#!/usr/bin/env python3
"""
Phrase authority gate:
- Ensure only ONE "(AUTHORITATIVE" heading exists for a given selector label.
- Ensure heading titles are unique (prevents silent duplicates).

This protects PHASE4_6_HUMAN_PHRASE_LIBRARY.md from "patch drift".
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PHRASES_FILE = (
    REPO_ROOT / "00__LOCKED__UPLOAD_SET" / "00__Runtime" / "PHASE4_6_HUMAN_PHRASE_LIBRARY.md"
)


HEADING_RE = re.compile(r"(?m)^(#{2,6})\s+(.+?)\s*$")


def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"[phrase-authority-gate] Missing file: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_heading(title: str) -> str:
    # Normalize whitespace and casing for stable comparisons
    t = re.sub(r"\s+", " ", title.strip())
    return t.casefold()


def main() -> int:
    text = read_text(PHRASES_FILE)

    headings: list[str] = []
    authoritative_labels: dict[str, list[int]] = {}

    for m in HEADING_RE.finditer(text):
        title = m.group(2).strip()
        line_no = text.count("\n", 0, m.start()) + 1
        headings.append((title, line_no))  # type: ignore[arg-type]

        # Catch any heading that declares AUTHORITATIVE
        if "AUTHORITATIVE" in title.upper():
            # Use the heading itself as the "label" (keeps enforcement simple + explicit)
            label = normalize_heading(title)
            authoritative_labels.setdefault(label, []).append(line_no)

    # 1) Duplicate heading titles (regardless of AUTHORITATIVE)
    seen: dict[str, list[int]] = {}
    for title, line_no in headings:
        key = normalize_heading(title)
        seen.setdefault(key, []).append(line_no)

    dup_titles = {k: v for k, v in seen.items() if len(v) > 1}

    # 2) Duplicate AUTHORITATIVE labels
    dup_authoritative = {k: v for k, v in authoritative_labels.items() if len(v) > 1}

    if not dup_titles and not dup_authoritative:
        return 0

    print("[phrase-authority-gate] FAILED", file=sys.stderr)
    if dup_authoritative:
        print("\nDuplicate AUTHORITATIVE headings found:", file=sys.stderr)
        for label, lines in sorted(dup_authoritative.items(), key=lambda x: x[0]):
            print(f"- {label} at lines: {lines}", file=sys.stderr)

    if dup_titles:
        print("\nDuplicate heading titles found:", file=sys.stderr)
        # Print a smaller list if huge
        for label, lines in sorted(dup_titles.items(), key=lambda x: x[0])[:50]:
            print(f"- {label} at lines: {lines}", file=sys.stderr)

    print(
        "\nFix: keep only ONE authoritative block per selector and remove/rename duplicates.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
