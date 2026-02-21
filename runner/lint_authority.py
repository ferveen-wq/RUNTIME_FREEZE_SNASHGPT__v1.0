#!/usr/bin/env python3
"""
lint_authority.py

Purpose:
- Enforce single-writer authority boundaries.
- Enforce bilingual integrity in PHASE4_6 phrase blocks.

Run:
  python runner/lint_authority.py
Exit code:
  0 = pass
  1 = fail
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RUNTIME_DIR = ROOT / "00__LOCKED__UPLOAD_SET" / "00__Runtime"
ENGINES_DIR = ROOT / "00__LOCKED__UPLOAD_SET" / "01__Engines"

QUAL_ENGINE = ENGINES_DIR / "QUALIFICATION_ENGINE.md"
ASSEMBLY_MAP = RUNTIME_DIR / "PHASE4_8_MESSAGE_ASSEMBLY_MAP.md"
PHRASE_LIB = RUNTIME_DIR / "PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

# Add a global regex for assignment detection (single '=')
REQUEST_TYPE_ASSIGN_RE = re.compile(r"\brequest_type\b\s*=\s*(?![=])", re.IGNORECASE)


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def lint_request_type_single_writer(failures: list[str]) -> None:
    """
    Enforce: request_type assignment only allowed in QUALIFICATION_ENGINE.md
    """
    # Match single "=" only (not "==")
    assign_re = re.compile(r"(?m)^\s*-\s*request_type\s*=\s*(?![=])")
    set_re = re.compile(r"(?im)\bset\s+request_type\s*=\s*")

    # Scan all markdown files under runtime + engines
    scan_roots = [
        ROOT / "00__LOCKED__UPLOAD_SET" / "00__Runtime",
        ROOT / "00__LOCKED__UPLOAD_SET" / "01__Engines",
    ]

    for base in scan_roots:
        for path in base.rglob("*.md"):
            if path.resolve() == QUAL_ENGINE.resolve():
                continue
            txt = read_text(path)
            if assign_re.search(txt):
                fail(
                    f"[AUTHORITY] Forbidden writer: request_type assignment found in {path}",
                    failures,
                )
            if set_re.search(txt):
                fail(
                    f"[AUTHORITY] Forbidden writer: 'set request_type =' found in {path}", failures
                )

    # Assembly must not “force request_type”
    assembly_txt = read_text(ASSEMBLY_MAP)
    if re.search(r"(?im)\bforce\s+request_type\b", assembly_txt):
        fail(
            "[AUTHORITY] Assembly contains 'force request_type' wording; forbidden by AUTHORITY_INDEX.",
            failures,
        )


def extract_placeholders(s: str) -> set[str]:
    # {vehicle_model}, {vehicle_year}, etc.
    return set(re.findall(r"\{[a-zA-Z0-9_]+\}", s))


def lint_phrase_library_bilingual_parity(failures: list[str]) -> None:
    """
    Enforce:
    - Each block has at least one EN: and one AR:
    - Placeholder parity between EN and AR (set match)
    """
    txt = read_text(PHRASE_LIB)
    if not txt:
        fail(f"[PHRASES] Missing phrase library: {PHRASE_LIB}", failures)
        return

    # Split by blocks using headings: ### <ID>
    blocks = re.split(r"(?m)^\s*###\s+", txt)
    # blocks[0] is preamble
    for b in blocks[1:]:
        lines = b.splitlines()
        block_id = lines[0].strip() if lines else "UNKNOWN_BLOCK"

        en_lines = [ln for ln in lines if ln.strip().startswith("EN:")]
        ar_lines = [ln for ln in lines if ln.strip().startswith("AR:")]

        if not en_lines or not ar_lines:
            fail(f"[PHRASES] Block '{block_id}' missing EN: or AR: line(s).", failures)
            continue

        en_text = "\n".join(en_lines)
        ar_text = "\n".join(ar_lines)

        en_slots = extract_placeholders(en_text)
        ar_slots = extract_placeholders(ar_text)

        if en_slots != ar_slots:
            fail(
                f"[PHRASES] Slot parity mismatch in block '{block_id}': EN={sorted(en_slots)} AR={sorted(ar_slots)}",
                failures,
            )


def main() -> int:
    failures: list[str] = []

    lint_request_type_single_writer(failures)
    lint_phrase_library_bilingual_parity(failures)

    if failures:
        print("\nLINT FAILED:\n")
        for f in failures:
            print(f"- {f}")
        print("\nFix the above violations before running UAT.\n")
        return 1

    print("LINT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
