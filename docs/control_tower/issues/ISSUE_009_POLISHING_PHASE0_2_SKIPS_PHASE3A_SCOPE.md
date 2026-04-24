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

## Mixed Raw Result — 2026-04-24

Polishing-only raw determinism check produced mixed results:

- Run 1 failed:
  - selected_phrase_id: `PHASE3B_POLISHING_RANGE`
  - QUALIFICATION_STATUS: `READY_FOR_NEGOTIATION`
  - price_ladder_state: `INITIAL`

- Run 2 behaved correctly:
  - selected_phrase_id: `PHASE3A_Q_POLISHING_SCOPE`
  - QUALIFICATION_STATUS: `NOT_READY`
  - price_ladder_state: `NONE`
  - only phase label mismatch: `PHASE_3`

- Run 3 behaved correctly:
  - selected_phrase_id: `PHASE3A_Q_POLISHING_SCOPE`
  - QUALIFICATION_STATUS: `NOT_READY`
  - price_ladder_state: `NONE`
  - only phase label mismatch: `3`

Current classification:
- Mixed / execution instability
- Not patchable yet as deterministic runtime defect

Decision:
- Do not patch runtime from this evidence alone.
- Keep ISSUE_009 open/monitored.
- Phase label normalization may need separate harness handling, but must not hide true PHASE3B jumps.
