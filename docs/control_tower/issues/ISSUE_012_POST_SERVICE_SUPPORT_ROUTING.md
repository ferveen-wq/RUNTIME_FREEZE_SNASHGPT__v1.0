# ISSUE_012 — Post-Service Support Routed as Offscope

## Problem
Customer messages that are still SNASH-service related but indicate a problem after service are routed as non-automotive offscope.

Example:
Input:
"عندي مشكلة بعد التظليل"

Actual:
- request_type = OTHER
- selected_phrase_id = OFFSCOPE — NON-AUTOMOTIVE (PHASE 0–2)
- QUALIFICATION_STATUS = NOT_READY

Expected:
- Route to POST-SERVICE SUPPORT (PHASE 0–2)
- Do not classify as non-automotive offscope
- Do not enter pricing or sales qualification

## Classification
Runtime bug — Phase 0–2 support/service-adjacent routing gap

## Owner Candidates
- QUALIFICATION_ENGINE.md should classify service-adjacent support separately from non-automotive offscope.
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md should route that support signal to POST-SERVICE SUPPORT (PHASE 0–2).

## Evidence
- POST-SERVICE SUPPORT phrase exists in PHASE4_6_HUMAN_PHRASE_LIBRARY.md.
- No active routing was found for POST-SERVICE SUPPORT.
- Active UAT case after_service_support failed.

## Status
CLOSED — VALIDATED IN ACTIVE UAT (2026-04-25)
