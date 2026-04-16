# Phase 4 Warranty Sensitivity Misroute — 2026-04-16

DEFECT_BUCKET: HARNESS_DEFECT
TARGET_FILE_ROLE: harness / runner
EXECUTABLE_OWNER: runner/context_reset_prompt.txt
ADJACENT_FILES_CHECKED:
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

OBSERVED:
- Input: "will this affect warranty?"
- Runtime signals already show:
  - active_service_context=ppf
  - PPF_COVERAGE_INTENT=FULL
  - PPF_DRIVING_PATTERN=HIGHWAY
  - QUALIFICATION_STATUS=READY_FOR_NEGOTIATION
  - price_ladder_state=INITIAL
  - objection_signal=TRUST_OR_RISK
  - objection_repeat_count=0
- Actual result:
  - phase=4
  - selected_phrase_id=PHASE4_PPF_BRAND_FIXATION_L1

WHY THIS IS NOT CLEAN ENOUGH:
- The turn stayed in late-stage PPF Phase 4 correctly.
- But a warranty-specific question should prefer the warranty-sensitivity authority path, not the brand-fixation path.
- This is still runner-side misselection inside the correct phase family.

DUPLICATE_LOGIC_CHECK:
- Tighten the existing late-stage PPF guard only.
- Do not add a parallel authority block.

VALIDATION_METHOD:
- focused strict UAT
- raw report review
- authority phrase-id check
