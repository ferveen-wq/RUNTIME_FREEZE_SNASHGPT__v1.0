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
RESOLVED — validated and committed.

## Resolution
- Routing owner confirmed: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md.
- First post-price PPF objection now remains Phase 4.
- objection_repeat_count == 0 routes to PHASE4_PPF_PRICE_PRESSURE_L1.
- Phase 5 starts only at repeat/deeper objection.
- Clean focused active UAT passed 3/3 after patch.
- SNASH Guard passed on commit 74346cd.

---

## Patch update — 2026-04-29

Business decision:
- First "expensive" after price exposure must stay in Phase 4.
- Phase 5 starts only after repeat/deeper objection.

Patch status:
- RESOLVED_COMMITTED

Patch owner:
- 00__ACTIVE_ROLLOUT_UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

Patch summary:
- PPF-only Route G boundary correction.
- objection_repeat_count == 0 routes to PHASE4_PPF_PRICE_PRESSURE_L1.
- objection_repeat_count == 1 may enter PHASE5_PPF_PRICE_GAP_DEEPEN_L1.

Validation completed:
- Focused clean active UAT repeat run: 3/3 PASS.
- SNASH Guard: PASS.
- Commit: 74346cd fix: stabilize phase4 first objection routing.
