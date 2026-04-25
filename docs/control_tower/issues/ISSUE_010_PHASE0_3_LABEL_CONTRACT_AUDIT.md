# ISSUE_010 — Phase 0–3 Label Contract Audit

## Type
Architecture Authority / Runtime Stability

## Problem
Raw active UAT exposed unstable labels across Phase 0–3.

Same service+vehicle inputs sometimes produce different labels:
- `SERVICE_CONFIRMED`
- `PRICE_REQUEST`
- `READY_FOR_NEGOTIATION`
- `PHASE3A_Q_*`
- `PHASE3B_*`
- `SERVICE CONFIRMED — PHASE 0–2`

This causes inconsistent routing between:
- Phase 0–2 service recognition
- Phase 3A qualifier questions
- Phase 3B price entry

## Goal
Create a strict label contract for Phase 0–3.

## Labels / Signals to Audit
- `phase`
- `request_type`
- `service_intent`
- `active_service_context`
- `detected_service_intent_in_message`
- `missing_fields`
- `phase3a_required`
- `phase3a_complete`
- `phase3a_qualifier_id`
- `QUALIFICATION_STATUS`
- `selected_phrase_id`
- `price_ladder_state`

## Required Proof
For each label/signal:
1. Allowed values
2. Sole writer
3. Readers
4. When it may change
5. Forbidden combinations
6. Service-specific exceptions if any

## Forbidden Combination Examples
- `PHASE3B_*` with `QUALIFICATION_STATUS != READY_FOR_NEGOTIATION`
- `PRICE_REQUEST` without direct price token
- `READY_FOR_NEGOTIATION` before Phase 3A completion
- `SERVICE CONFIRMED — PHASE 0–2` when vehicle model/year are already known and Phase 3A qualifier is required

## Status
OPEN

## Core Label Owner Audit Finding — 2026-04-25

Owner-map audit found several important Phase 0–3 label contract risks.

### 1. `phase` label ambiguity
`QUALIFICATION_ENGINE.md` states:
- runtime `phase` MUST remain `PHASE_3` throughout Phase 3
- do NOT emit `PHASE_3A` or `PHASE_3B` as runtime phase values

But active UAT currently expects `phase = 3A` in several checks.

Conclusion:
- Some failures are likely test expectation / label-normalization issues, not runtime behavior defects.
- Phase 3A validation should prioritize:
  - `selected_phrase_id`
  - `QUALIFICATION_STATUS`
  - `price_ladder_state`
  over exact phase label variants (`3`, `PHASE_3`, `3A`).

### 2. `request_type` ownership
Declared intent:
- `QUALIFICATION_ENGINE.md` is the sole writer of `request_type`.
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` must only read `request_type`.

Risk:
- Assembly-map wording around PRICE_REQUEST routes can look writer-like and may confuse runtime interpretation.
- Need strict contract wording that Assembly reads only and must not reclassify.

### 3. `selected_phrase_id` ownership
Declared intended flow:
- `QUALIFICATION_ENGINE.md` decides `phase3a_qualifier_id`.
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` selects `selected_phrase_id`.
- `OUTPUT_RESPONSE_TEMPLATE.md` formats only.

Risk:
- Phrase selection rules are scattered, making competing routes possible.

### 4. `QUALIFICATION_STATUS`
Owner appears clean:
- Writer: `QUALIFICATION_ENGINE.md`
- Readers: execution/assembly/pricing/objection layers

Risk:
- Wrong or early `READY_FOR_NEGOTIATION` allows premature Phase 3B.

### 5. `price_ladder_state`
Owner appears clean:
- Writer: `PRICE_LADDER_ENGINE.md`

Risk:
- If `price_ladder_state = INITIAL` appears while qualifiers are incomplete, something allowed Price Ladder to run too early.

## Current Decision
Do not patch runtime from mixed raw results yet.

Next steps:
1. Normalize/clarify active UAT phase expectations.
2. Strengthen label contract documentation.
3. Audit request_type and Phase3 readiness rules before more API runs.
