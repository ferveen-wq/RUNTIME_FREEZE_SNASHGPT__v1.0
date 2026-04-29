# ISSUE_016 — Phase 4 Routing Instability After Price

## Problem
After correct Phase 3B price delivery, the user objection "expensive" does not consistently route to Phase 4.

## Expected
- phase = PHASE_4
- selected_phrase_id = PHASE4_PPF_PRICE_PRESSURE_L1
- price_ladder_state = INITIAL
- prior PPF front context remains preserved

## Actual
Repeated clean-lane active UAT produced mixed outputs:
- Run 1: PHASE_3 / PHASE3B_PPF_RANGE / FINAL_PRICE_REACHED
- Run 2: PHASE_3 / PHASE5_PPF_PRICE_GAP_DEEPEN_L1 / FINAL_PRICE_REACHED
- Run 3: PHASE_3 / PHASE3B_PPF_RANGE / FINAL_PRICE_REACHED

Runtime-critical price context remained mostly correct in repeat runs:
- selected_skus = [PPF_FRONT_GLOBAL]
- price = 295
- no 790 / 880 leakage in repeat runs

## Classification
Instruction / execution instability.

## Status
OPEN — DO NOT PATCH runtime until routing owner is confirmed and deterministic defect is proven.

## Next Step
Trace Phase 3B -> Phase 4 transition ownership:
- who reads objection_signal / "expensive"
- who owns phase change from PHASE_3 to PHASE_4
- who decides PHASE4_PPF_PRICE_PRESSURE_L1 vs PHASE5_PPF_PRICE_GAP_DEEPEN_L1
- whether Phase 3B final price state blocks Phase 4 routing

---

## Patch update — 2026-04-29

Business decision:
- First "expensive" after price exposure must stay in Phase 4.
- Phase 5 starts only after repeat/deeper objection.

Patch status:
- PATCHED_LOCAL

Patch owner:
- 00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

Patch summary:
- PPF-only Route G boundary correction.
- objection_repeat_count == 0 routes to PHASE4_PPF_PRICE_PRESSURE_L1.
- objection_repeat_count == 1 may enter PHASE5_PPF_PRICE_GAP_DEEPEN_L1.

Pending validation:
- Full guard.
- Focused clean active UAT repeat run.
