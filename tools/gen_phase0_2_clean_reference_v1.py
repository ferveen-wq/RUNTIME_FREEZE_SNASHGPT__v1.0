#!/usr/bin/env python3
# ------------------------------------------------------------
# PHASE 0–2 CLEAN REFERENCE GENERATOR
# ------------------------------------------------------------
# This script:
# - Reads Phase 0–2 runtime files
# - Generates a human-readable reference file
# - DOES NOT modify any runtime behavior
# ------------------------------------------------------------

import re
from datetime import datetime
from pathlib import Path

# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

ROOT = Path(".").resolve()

PHRASE_LIB = ROOT / "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"
ASSEMBLY_MAP = ROOT / "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md"
LOCK_INDEX = ROOT / "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE0_2_LOCK_INDEX.md"

OUT_FILE = ROOT / "tools/PHASE0_2_CLEAN_REFERENCE.md"


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------


def read_file(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def extract_section(md: str, header_text: str) -> str:
    """
    Extract markdown section starting at header_text
    until next header of same level.
    """
    pattern = re.compile(rf"^(##\s+{re.escape(header_text)})\s*$", re.M)
    match = pattern.search(md)
    if not match:
        return ""

    start = match.start()
    after = md[match.end() :]

    next_header = re.search(r"^##\s+.+$", after, re.M)
    if next_header:
        end = match.end() + next_header.start()
        return md[start:end].strip()
    else:
        return md[start:].strip()


def extract_phase0_2_phrase_blocks(md: str) -> list[str]:
    """
    Extract phrase blocks that contain '(PHASE 0–2'
    """
    blocks = []
    matches = re.finditer(r"^###\s+.*\(PHASE 0–2.*\).*$", md, re.M)

    for m in matches:
        start = m.start()
        remaining = md[m.end() :]
        next_block = re.search(r"^###\s+.*$", remaining, re.M)

        if next_block:
            end = m.end() + next_block.start()
            block = md[start:end]
        else:
            block = md[start:]

        blocks.append(block.strip())

    return blocks


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------


def main():
    phrase_md = read_file(PHRASE_LIB)
    assembly_md = read_file(ASSEMBLY_MAP)
    lock_md = read_file(LOCK_INDEX)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output = []
    output.append("# PHASE 0–2 CLEAN REFERENCE\n")
    output.append(f"_Generated: {now}_\n")
    output.append("This document is READ-ONLY and does not affect runtime.\n")

    # ------------------------------------------------------------
    # Invariants
    # ------------------------------------------------------------
    invariants = extract_section(lock_md, "LOCKED ROUTING INVARIANTS (PHASE 0–2)")
    output.append("\n## Routing Invariants\n")
    output.append(invariants if invariants else "_Not found._")

    # ------------------------------------------------------------
    # Missing Info Selector
    # ------------------------------------------------------------
    if "PHASE 0–2: MISSING INFO QUESTION SELECTOR" in assembly_md:
        output.append("\n## Missing Info Selector (Assembly Map Snippet)\n")
        start = assembly_md.index("PHASE 0–2: MISSING INFO QUESTION SELECTOR")
        snippet = assembly_md[start : start + 800]
        output.append("```")
        output.append(snippet.strip())
        output.append("```")

    # ------------------------------------------------------------
    # Phrase Blocks
    # ------------------------------------------------------------
    output.append("\n## Phase 0–2 Phrase Blocks\n")

    blocks = extract_phase0_2_phrase_blocks(phrase_md)

    if not blocks:
        output.append("_No Phase 0–2 phrase blocks detected._")
    else:
        for b in blocks:
            output.append(b)
            output.append("\n---\n")

    # ------------------------------------------------------------
    # Write Output
    # ------------------------------------------------------------
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(output), encoding="utf-8")

    print("OK: generated", OUT_FILE)
    print("Blocks detected:", len(blocks))


if __name__ == "__main__":
    main()
