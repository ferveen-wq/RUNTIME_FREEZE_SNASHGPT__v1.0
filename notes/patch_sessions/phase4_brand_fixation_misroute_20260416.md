# Phase 4 Brand Fixation Misroute — 2026-04-16

DEFECT_BUCKET: HARNESS_DEFECT or PROMPT-BRIDGE EXECUTION DEFECT (to confirm)
TARGET_FILE_ROLE: harness / runner prompt
EXECUTABLE_OWNER: runner/context_reset_prompt.txt
ADJACENT_FILES_CHECKED:
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

OBSERVED:
- Input: "is xpel better?"
- Runtime signals already show:
  - active_service_context=ppf
  - PPF_COVERAGE_INTENT=FULL
  - PPF_DRIVING_PATTERN=HIGHWAY
  - QUALIFICATION_STATUS=READY_FOR_NEGOTIATION
  - price_ladder_state=INITIAL
- Actual result:
  - phase=0
  - selected_phrase_id="BRAND DISCLOSURE — PPF (PHASE 0–2)"
  - asked coverage again

WHY THIS IS WRONG:
- It ignored late-stage runtime state.
- It routed to a Phase 0–2 disclosure path instead of a Phase 4 PPF trust/brand family path.
- It re-asked an already-known qualifier.

DUPLICATE_LOGIC_CHECK:
- Need to confirm whether runner prompt contains a broad brand-disclosure override that overrides late-stage runtime state.

VALIDATION_METHOD:
- grep authority lines
- focused strict UAT
- re-run after any patch
