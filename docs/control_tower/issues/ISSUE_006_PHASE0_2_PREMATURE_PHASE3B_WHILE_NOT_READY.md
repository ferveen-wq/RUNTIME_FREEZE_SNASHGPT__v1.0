# ISSUE_006 — Phase 0–2 service recognition routes to Phase 3B while NOT_READY

## Type
Runtime / Assembly Routing Bug

## Surface
Phase 0–3 transition:
- service recognition
- Phase 3A qualifier routing
- Phase 3B price-entry suppression

## Problem
Strict active UAT revealed that basic service recognition for PPF, Ceramic, and Tint selected Phase 3B price/range phrases while qualification was still NOT_READY.

## Evidence
Active UAT:
`tests/active_rollout_uat/phase0_2_service_recognition_smoke_pack.json`

Failed cases:
- `phase0_2_ppf_recognition`
  - selected_phrase_id: `PHASE3B_PPF_RANGE`
  - QUALIFICATION_STATUS: `NOT_READY`
- `phase0_2_ceramic_recognition`
  - selected_phrase_id: `PHASE3B_CERAMIC_RANGE`
  - QUALIFICATION_STATUS: `NOT_READY`
- `phase0_2_tint_recognition`
  - selected_phrase_id: `PHASE3B_TINT_RANGE`
  - QUALIFICATION_STATUS: `NOT_READY`

Passed cases:
- Polishing correctly routed to `PHASE3A_Q_POLISHING_SCOPE`
- Wrap correctly routed to `PHASE3A_Q_WRAP_FINISH`

## Why This Matters
A Phase 3B phrase must never be selected while `QUALIFICATION_STATUS = NOT_READY`.

This creates:
- false pricing
- premature quotation
- Phase 3A skip
- customer-facing policy violation

## Current Classification
Deterministic failure under strict active UAT.

## Patch Constraint
Do not patch until owner is confirmed.

Candidate owner surfaces:
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `QUALIFICATION_ENGINE.md`
- `PRICE_LADDER_ENGINE.md`
- runner contradiction guard / harness validation

## Status
OPEN
