# ISSUE_009 — Polishing service recognition skips Phase 3A scope and jumps to Phase 3B

## Type
Raw Runtime Defect

## Surface
Phase 0–2 to Phase 3A transition

## Evidence
Raw active UAT:
`tests/active_rollout_uat/phase0_2_service_recognition_smoke_pack.json`

Input:
`polishing camry 2022`

Observed debug:
- phase: `3B`
- request_type: `PRICE_REQUEST`
- selected_phrase_id: `PHASE3B_POLISHING_RANGE`
- QUALIFICATION_STATUS: `READY_FOR_NEGOTIATION`
- price_ladder_state: `INITIAL`

Expected:
- phase: `3A`
- selected_phrase_id: `PHASE3A_Q_POLISHING_SCOPE`
- QUALIFICATION_STATUS: `NOT_READY`
- price_ladder_state: `NONE`

Problem:
Polishing jumps to pricing before asking polishing scope.

Classification:
- deterministic raw runtime defect unless repeat test proves otherwise
- not legacy runner contamination

Patch constraint:
- Do not patch until owner is confirmed.
