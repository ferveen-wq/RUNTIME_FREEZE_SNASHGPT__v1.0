import re
from pathlib import Path

p = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
s = p.read_text(encoding="utf-8")

EN_PREFIX = "Sure — "
AR_PREFIX = "أكيد — "

# Sections in Phase4_6 where we allow Phase 0–2 question prefixing.
# We will only apply inside these named Phase 0–2 blocks/sections.
PHASE0_2_ANCHORS = [
    "### BIZ_LOCATION__ASK_PIN (PHASE 0–2",
    "### BIZ_HOURS__ASK_DAY (PHASE 0–2",
    "### BIZ_KSA_BRANCH__CONFIRM_COUNTRY (PHASE 0–2",
    "### C.1 PPF EXPLANATION + QUALIFIER (PHASE 0–2)",
    "### C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)",
    "### C.3 CERAMIC WASH PATTERN QUALIFIER (PHASE 0–2)",
    "## DRIVING PATTERN QUALIFIER — PHASE 0–2",
    "## PRICE REQUEST HOLD — PHASE 0–2",
    "## COMPARISON — PHASE 0–2 (VEHICLE KNOWN)",
    "## BRAND DISCLOSURE — PHASE 0–2 (APPROVED)",
    "## COMPETITOR CHEAPER — PHASE 0–2",
    "## TECHNICAL QUESTION HOLD — PHASE 0–2",
    "### MULTI_SERVICE_INTENT_SAFE (PHASE 0–2)",
    "### LONG_RAMBLING_GROUNDING (PHASE 0–2)",
    "### L.1 QUALIFICATION CLARIFIERS (VEHICLE DETAILS)",
    "### L.1 YEAR_ONLY (AUTHORITATIVE — ONE QUESTION)",
]

# A hard guard: never touch Phase 3A blocks
PHASE3A_HEADER_RE = re.compile(r"^###\s+PHASE3A_Q_", re.MULTILINE)

def already_prefixed(line: str, prefix: str) -> bool:
    return line.strip().startswith(prefix.strip())

def is_question_text(text: str) -> bool:
    return "?" in text

def prefix_line(line: str, prefix: str) -> str:
    # line like: "EN: ...?"
    # Preserve "EN:" / "AR:" token exactly, prefix only the content.
    m = re.match(r"^(EN|AR):\s*(.*)$", line)
    if not m:
        return line
    lang, body = m.group(1), m.group(2)
    if not is_question_text(body):
        return line
    if lang == "EN" and already_prefixed(body, EN_PREFIX):
        return line
    if lang == "AR" and already_prefixed(body, AR_PREFIX):
        return line
    if lang == "EN":
        body_new = EN_PREFIX + body
    else:
        body_new = AR_PREFIX + body
    return f"{lang}: {body_new}"

lines = s.splitlines(True)

# Find ranges for each Phase 0–2 anchor block by header positions.
anchor_positions = []
for anchor in PHASE0_2_ANCHORS:
    idx = s.find(anchor)
    if idx != -1:
        anchor_positions.append((idx, anchor))
anchor_positions.sort()

if not anchor_positions:
    raise SystemExit("ABORT: No Phase 0–2 anchors found. No changes applied.")

# Build list of (start_char, end_char) ranges for safe editing
ranges = []
for i, (start, anchor) in enumerate(anchor_positions):
    end = anchor_positions[i + 1][0] if i + 1 < len(anchor_positions) else len(s)
    ranges.append((start, end, anchor))

# Function to check if a character index is inside any editable range
def in_editable_range(pos: int) -> bool:
    for start, end, _ in ranges:
        if start <= pos < end:
            return True
    return False

# Precompute which line-start indices are editable
editable_line_flags = []
pos = 0
for line in lines:
    editable_line_flags.append(in_editable_range(pos))
    pos += len(line)

out_lines = []
in_phase3a = False

for line, editable in zip(lines, editable_line_flags, strict=False):
    # Track Phase 3A block and do not edit inside it
    if PHASE3A_HEADER_RE.match(line):
        in_phase3a = True
    if in_phase3a and line.startswith("### ") and not PHASE3A_HEADER_RE.match(line):
        # new section header; Phase3A ended
        in_phase3a = False

    if editable and (not in_phase3a):
        if line.startswith("EN:") or line.startswith("AR:"):
            out_lines.append(prefix_line(line.rstrip("\n"), EN_PREFIX if line.startswith("EN:") else AR_PREFIX) + "\n")
            continue

    out_lines.append(line)

new_s = "".join(out_lines)

if new_s == s:
    raise SystemExit("ABORT: No changes were necessary (already compliant). No changes applied.")

p.write_text(new_s, encoding="utf-8")
print("OK: patched", p)
