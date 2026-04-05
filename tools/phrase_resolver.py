from __future__ import annotations

import re
from pathlib import Path

PHRASE_LIBRARY_PATH = Path(
    "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"
)


def resolve_phrase(phrase_id: str, language: str = "EN") -> str | None:
    if not PHRASE_LIBRARY_PATH.exists():
        return None

    text = PHRASE_LIBRARY_PATH.read_text(encoding="utf-8")

    block_pattern = rf"^###\s+{re.escape(phrase_id)}\s*$([\s\S]*?)(?=^###\s+|\Z)"
    block_match = re.search(block_pattern, text, flags=re.MULTILINE)
    if not block_match:
        return None

    block = block_match.group(1)

    lang = (language or "EN").upper()
    line_pattern = rf"^{lang}:\s*(.+)$"
    line_match = re.search(line_pattern, block, flags=re.MULTILINE)

    if line_match:
        return line_match.group(1).strip()

    if lang != "EN":
        fallback_match = re.search(r"^EN:\s*(.+)$", block, flags=re.MULTILINE)
        if fallback_match:
            return fallback_match.group(1).strip()

    return None


if __name__ == "__main__":
    print(resolve_phrase("PHASE3A_Q_PPF_DRIVING_PATTERN", "EN"))
    print(resolve_phrase("PHASE3A_Q_PPF_DRIVING_PATTERN", "AR"))
