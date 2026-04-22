# Deprecated UAT Packs

## phase7_thinking_probe_v1.json.invalid

Reason for deprecation:
- This pack treated THINKING as if it were a standalone Phase 7 behavioral lane.
- Current locked reading is:
  - Phase 5 owns late-stage customer-state behavior (thinking / deferred / silence / closing / handover)
  - Phase 7 is explanation-only support
- Therefore this pack must not be used as rollout truth without a re-authored contract that respects the Phase 5 / Phase 7 boundary.

Rule:
- Do not promote deprecated packs back into active tests/uat without fresh evidence and a corrected contract.
