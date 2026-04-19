# TIER 3 — PPF PHASE 5 BRANCH COLLAPSE

Status: TRUSTED_FAILURE
Date: 2026-04-19

## Pack
- tests/uat/phase5_ppf_verbatim_strict_v1.json

## Result after runner trust fix
- FAILED (3/5 cases)

## Observed pattern
Multiple distinct Phase 5 branches collapse into a single route:

Returned repeatedly:
- selected_phrase_id: PHASE5_PPF_PRICE_GAP_DEEPEN_L1

## Failed cases

### 1) Repeat objection
Expected:
- PHASE5_PPF_NARROW_L2
Actual:
- PHASE5_PPF_PRICE_GAP_DEEPEN_L1

### 2) Technical deepen
Expected:
- PHASE5_PPF_TECHNICAL_DEEPEN_L1
Actual:
- PHASE5_PPF_PRICE_GAP_DEEPEN_L1

### 3) Exit fork
Expected:
- PHASE5_PPF_EXIT_FORK_L3
Actual:
- PHASE5_PPF_PRICE_GAP_DEEPEN_L1
- phase dropped to 4 (incorrect)

## Conclusion
Phase 5 PPF routing is not preserving branch-level differentiation.
Multiple late-stage decision paths collapse into a generic price-gap deepen response.

## Classification
- Trusted failure
- Branch collapse
- Late-stage routing failure
- Phase-boundary inconsistency (exit fork)
