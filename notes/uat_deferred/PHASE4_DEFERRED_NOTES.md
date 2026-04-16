# Phase 4 Deferred UAT Notes

## Kept active
- tests/uat/phase4_ppf_strict_v1.json
- tests/uat/phase4_price_resistance_v2.json

Reason:
- both use clearer executable ownership
- both use runtime-signal-based setup
- both passed focused validation

## Kept deferred
- notes/uat_deferred/phase4_entry_audit_v1.json
- notes/uat_deferred/phase4_entry_strict_v1.json
- notes/uat_deferred/phase4_reassurance_multiturn_v1.json

Reason:
- input-only or weak-negative assertions
- phase-family assumptions not yet tied tightly enough to runtime signals
- multi-turn harness shape remains historically weaker than single-turn strict runtime-signal validation

## Superseded
- notes/uat_deferred/phase4_price_resistance_v1.json

Reason:
- replaced by tests/uat/phase4_price_resistance_v2.json
- v2 is cleaner and runtime-signal-based
