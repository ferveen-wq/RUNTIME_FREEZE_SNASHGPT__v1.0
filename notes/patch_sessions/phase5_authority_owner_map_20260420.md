# Phase 5 Authority Owner Map — 2026-04-20

## Purpose
To identify ALL Phase 5 authority layers and isolate:
- selection owner
- boundary guards
- render locks
- competing logic

This file is REQUIRED before any GAP-TR-004 patch.

--------------------------------------------------
## 1. RENDER LOCKS (SAFE — KEEP)
--------------------------------------------------

- PHASE5_PPF_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK
- PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK
- PHASE 5 VERBATIM RENDERING (global)

Role:
- output enforcement only
- NOT routing / NOT selection

Decision:
- KEEP as-is
- NOT part of routing fixes

--------------------------------------------------
## 2. PHASE BOUNDARY GUARDS (SAFE — KEEP OUTSIDE ROUTER)
--------------------------------------------------

- CERAMIC SILENCE AFTER PRICE → Phase 4
- PPF SILENCE AFTER PRICE → Phase 4
- PPF FIRST PRICE PUSH → stay in Phase 4

Role:
- prevent premature Phase 5 entry
- boundary enforcement

Decision:
- KEEP outside router
- NOT part of GAP-TR-004 fix

--------------------------------------------------
## 3. PRE-ROUTER SELECTION AUTHORITY (CONFLICT ZONE)
--------------------------------------------------

- CERAMIC REPEAT OBJECTION MUST NARROW

Characteristics:
- Phase 5 selection logic
- executes BEFORE router
- contains STOP
- blocks router execution

Risk:
- creates split ownership
- bypasses router
- leads to inconsistent behavior across services

Decision:
- CONFLICTING AUTHORITY
- must be evaluated for:
  - merge into router
  - or remain as justified special override

--------------------------------------------------
## 4. MAIN ROUTER (PRIMARY OWNER — INTENDED)
--------------------------------------------------

- PHASE 5 SERVICE-OWNER ROUTER

Characteristics:
- service-based branching (ppf / ceramic / polishing)
- contains full L1 / L2 / L3 logic
- intended single owner

Observed issue:
- does not fully override earlier blocks
- coexists with pre-router overrides

Risk:
- not true single authority
- subject to precedence leakage

--------------------------------------------------
## 5. PARALLEL SERVICE AUTHORITY (TINT)
--------------------------------------------------

- PHASE 5 TINT L1 / L2 / L3 blocks (outside router)

Characteristics:
- full selection logic
- separate from router
- STOP-based execution

Risk:
- second independent Phase 5 owner
- inconsistent architecture vs router model

--------------------------------------------------
## CORE PROBLEM
--------------------------------------------------

Phase 5 selection authority is SPLIT across:
- pre-router overrides
- shared router
- parallel tint blocks

This violates:
- single authority per behavior
- deterministic routing

--------------------------------------------------
## KEY PLANNING QUESTION
--------------------------------------------------

Choose ONE model:

OPTION A — Single Router Model
- all Phase 5 selection inside router
- remove pre-router and parallel service blocks

OPTION B — Service-Isolated Model
- each service has its own block
- remove shared router

Current system = hybrid (UNSAFE)

--------------------------------------------------
## SAFE NEXT MOVE
--------------------------------------------------

- DO NOT PATCH YET
- decide ownership model first
- then patch ONLY one authority layer
- validate with:
  - GAP-TR-004 focused pack
  - no regression in ceramic/tint

--------------------------------------------------
