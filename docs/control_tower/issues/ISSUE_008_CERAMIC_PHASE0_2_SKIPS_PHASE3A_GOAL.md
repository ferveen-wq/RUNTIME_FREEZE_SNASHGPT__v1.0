# ISSUE_008 — Ceramic service recognition skips Phase 3A goal despite complete vehicle info

## Type
Raw Runtime Defect

## Surface
Phase 0–2 to Phase 3A transition

## Evidence
Raw active UAT:
`tests/active_rollout_uat/phase0_2_ceramic_only_raw_check.json`

Input:
`ceramic camry 2022`

Observed debug:
- phase: `0`
- service_intent: `ceramic`
- active_service_context: `ceramic`
- missing_fields: `[]`
- QUALIFICATION_STATUS: `NOT_READY`
- selected_phrase_id: `C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)`

Observed customer message:
- asks for vehicle model/year even though `missing_fields` is empty

Expected:
- route to Phase 3A
- selected_phrase_id: `PHASE3A_Q_CERAMIC_GOAL`
- QUALIFICATION_STATUS: `NOT_READY`
- no vehicle model/year question

Classification:
- deterministic raw runtime defect
- not legacy runner contamination
- not missing vehicle extraction

Patch constraint:
- Do not patch until owner is confirmed.
