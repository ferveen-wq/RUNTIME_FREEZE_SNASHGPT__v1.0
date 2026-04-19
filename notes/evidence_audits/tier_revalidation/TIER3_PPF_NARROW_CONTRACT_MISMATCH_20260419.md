# TIER 3 — PPF NARROW L2 CONTRACT MISMATCH

Status: TRUSTED_FAILURE
Date: 2026-04-19

## Pack
- tests/uat/phase5_ppf_verbatim_strict_v1.json

## Case
- ppf_phase5_repeat_objection_verbatim_strict

## Result after branch-routing reconciliation
- selected_phrase_id is now correct:
  - PHASE5_PPF_NARROW_L2
- phase is correct:
  - 5

## Remaining failure
The strict pack forbids:
- english: "price"
- arabic: "سعر"

But the locked phrase body for PHASE5_PPF_NARROW_L2 includes those words.

## Conclusion
This is no longer a routing failure.
It is a contract mismatch between:
- strict pack expectations
- locked phrase-library content

## Classification
- Trusted failure
- Pack vs phrase-library contradiction
- Not a prompt-bridge branch-selection issue
