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

## Owner Proof — 2026-04-24

Owner-map evidence:

- `QUALIFICATION_STATUS`
  - Writer: `QUALIFICATION_ENGINE.md`
  - Readers include:
    - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
    - `PRICE_LADDER_ENGINE.md`
    - `RUNTIME_EXECUTION_FLOW.md`

- `phase3a_required`
  - Written/defined by `QUALIFICATION_ENGINE.md`
  - Read by `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`

- `phase3a_qualifier_id`
  - Written/defined by `QUALIFICATION_ENGINE.md`
  - Read by `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`

- `PHASE3B_*_RANGE`
  - Routed by `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - Phrase content exists in `PHASE4_6_HUMAN_PHRASE_LIBRARY.md`

Current owner conclusion:
- `QUALIFICATION_ENGINE.md` is producing NOT_READY.
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` is the likely owner surface for preventing PHASE3B phrase selection while NOT_READY.

Patch direction:
- Add/strengthen assembly-level suppression:
  - If `QUALIFICATION_STATUS != READY_FOR_NEGOTIATION`, `selected_phrase_id` MUST NOT be any `PHASE3B_*`.
  - If `phase3a_required == true` and `phase3a_qualifier_id` is present, assembly MUST select that `PHASE3A_Q_*` phrase and STOP.
