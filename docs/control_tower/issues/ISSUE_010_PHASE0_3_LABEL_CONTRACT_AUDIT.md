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
