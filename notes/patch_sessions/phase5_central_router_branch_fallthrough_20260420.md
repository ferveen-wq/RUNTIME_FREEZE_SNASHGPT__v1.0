# Phase 5 Central Router Branch Fallthrough — 2026-04-20

## Finding

After removing the competing ceramic side-selector, Phase 5 still has two residual routing failures inside the central router itself.

## Confirmed residual failures

### 1) Ceramic L2 fallthrough
Expected:
- PHASE5_CERAMIC_NARROW_L2

Actual:
- PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1

Signals:
- active_service_context = ceramic
- objection_signal = PRICE_TOO_HIGH
- objection_repeat_count = 2
- QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- price_ladder_state = FINAL_PRICE_REACHED

### 2) PPF L3 exit fallthrough
Expected:
- PHASE5_PPF_EXIT_FORK_L3

Actual:
- PHASE5_PPF_PRICE_GAP_DEEPEN_L1

Signals:
- active_service_context = ppf
- objection_signal = READINESS_STALL
- objection_repeat_count = 3
- QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- price_ladder_state = FINAL_PRICE_REACHED

## What is now ruled out

- not repeat-count contract mismatch
- not phrase-library mismatch
- not runner signal injection
- not debug parser corruption
- not ceramic side-selector competition
- not cross-service ownership leak for PPF L2 anymore

## Current likely owner

- runner/context_reset_prompt.txt
- specifically:
  - HARD OVERRIDE — PHASE 5 SERVICE-OWNER ROUTER

## Likely defect shape

The nested service-owner router is not reliably holding branch differentiation for:
- ceramic repeat_count == 2
- ppf READINESS_STALL with repeat_count >= 3

Observed behavior suggests fallthrough to generic L1 deepen branch.

## Safe next move

Do not patch phrase library.
Do not reopen repeat-count theory.

Inspect whether the central router should be rewritten from nested branch form into explicit service-isolated hard overrides while preserving single-owner model.
