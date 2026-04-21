# Phase 5 Owner Handoff Contract — 2026-04-20

## Purpose
To enforce single service ownership after Phase 5 routing decision.

--------------------------------------------------

## Rule 1 — Single Owner Selection

- Service MUST be resolved using:
  active_service_context

- This MUST happen in ONE place:
  PHASE 5 SERVICE-OWNER ROUTER

--------------------------------------------------

## Rule 2 — Ownership Lock

Once service is selected:

- Only that service’s logic is allowed
- No other service branch may execute
- No earlier override may replace it

--------------------------------------------------

## Rule 3 — No Cross-Service Leakage

If:
- active_service_context == polishing

Then:
- MUST NOT output any PHASE5_PPF_*
- MUST NOT output any PHASE5_CERAMIC_*

Same applies for all services

--------------------------------------------------

## Rule 4 — Router Authority

- Router is the ONLY selection authority
- Pre-router selection blocks are NOT allowed
- Service-specific logic must exist INSIDE router only

--------------------------------------------------

## Rule 5 — Boundary Exceptions

Allowed outside router:
- Phase 4 guards
- Verbatim rendering locks

NOT allowed outside router:
- Phase 5 selection logic

--------------------------------------------------

## Implication

To fix GAP-TR-004:
- ensure router executes BEFORE any selection
- ensure no competing selection blocks exist before router
- ensure polishing branch fully isolates execution

--------------------------------------------------
