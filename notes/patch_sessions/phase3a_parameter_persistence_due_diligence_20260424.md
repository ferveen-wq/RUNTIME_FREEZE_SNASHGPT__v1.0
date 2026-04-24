# Phase 3A Parameter Persistence Due Diligence — 2026-04-24

## Issue
Project UAT shows Phase 3A qualifier state is not consistently preserved between turns:
- PPF front + city re-asks coverage or triggers extra qualifier.
- Ceramic same-service re-entry needed instruction-level stabilization.
- Tint mostly works but depends on same missing persistence pattern.

## Due diligence
Inspected:
- QUALIFICATION_ENGINE.md
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- GLOBAL_CORE_CONTEXT_PARAMETERS.md
- CONVERSATION_DYNAMIC_PARAMETERS.md
- RUNTIME_EXECUTION_FLOW.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- SKU_SELECTION_MATRIX.md
- PRICE_LADDER_ENGINE.md
- negotiation/objection/silence dependencies

## Finding
GLOBAL_CORE_CONTEXT_PARAMETERS.md defines PPF_COVERAGE_INTENT but does not define most Phase 3A qualifier fields:
- PPF_DRIVING_PATTERN
- PPF_COMPARISON_FOCUS
- CERAMIC_GOAL
- CERAMIC_WASH_PATTERN
- TINT_GOAL
- TINT_COVERAGE
- WRAP_FINISH
- POLISHING_SCOPE
- PAINT_CONDITION_REPAINT_SCRATCH
- PAINT_CONDITION_GATE

Also, PPF_FINISH_INTENT exists after END OF FILE and should be moved inside the file body.

## Patch decision
Patch GLOBAL_CORE_CONTEXT_PARAMETERS.md only.
Do not patch Qualification Engine yet.
Patch goal is persistence contract, not flow logic.

## Validation
After patch:
- ruff check .
- pre-commit run --all-files
- inspect diff
- upload updated GLOBAL_CORE_CONTEXT_PARAMETERS.md to Project UAT
- rerun Phase 3A smoke tests for PPF, ceramic, tint, wrap, polishing, roof-black PPF
