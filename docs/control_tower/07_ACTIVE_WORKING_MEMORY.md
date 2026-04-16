# 07_ACTIVE_WORKING_MEMORY.md

Purpose:
Single active working-memory file for runtime patch sessions.
Do not rely on chat memory. Read this file first in every new session.

## 1. SOURCE OF TRUTH ORDER
1. Locked runtime authorities
2. Engine authorities
3. Parameter / repository authorities
4. Control-tower architecture notes
5. Deferred patch notes
6. Prompt-bridge alignment last

## 2. CLOSED SERVICE TRACKS
### Ceramic
Status: CLOSED
- Phase 3A validated
- Phase 3B validated
- Phase 5 continuity / render leakage fixed
- Runtime path considered stable

### Tint
Status: CLOSED
- Phase 0-2 recognition validated
- Real Phase 3A validated
- Phase 3B validated
- Phase 5 L1 / L2 / L3 validated
- Runtime path considered stable

### PPF
Status: CLOSED
- Phase 3B price-ready path validated
- Phase 5 PPF verbatim rendering validated
- Earlier leakage concern was resolved as test-fixture / runner enforcement, not runtime drift
- Runtime path considered stable

### Polishing
Status: CLOSED
- Phase 0-2 recognition validated
- Phase 3A known-vehicle entry validated
- Phase 3A second qualifier continuity validated
- True Phase 3B readiness validated
- Phase 5 L1 / L2 / L3 validated
- Runtime path considered stable

## 3. DEFERRED / DO NOT PATCH NOW
### Wrap
Status: RUNTIME_BLOCKED
Business direction:
- Qualification + manual handoff is the decided architecture path
- Authority alignment has already been documented
- Runtime execution is still blocked by signal-honoring / orchestration-owner issues

Rule:
- Do NOT continue prompt/bridge patching for wrap
- Do NOT expand wrap automation
- Only runtime execution analysis is allowed

## 4. CURRENT ACTIVE TRACK
### Wrap
Status: RUNTIME_DEBUG ONLY
- Architecture decision is complete
- Authority alignment is complete
- Remaining work is runtime execution analysis only
- No further prompt/bridge patching is allowed

## 5. DO NOT TOUCH WITHOUT NEW EVIDENCE
- Ceramic runtime path
- Tint runtime path
- PPF runtime path
- Polishing runtime path
- Wrap runtime bridge for deep automation

## 6. SESSION START RULE
At the beginning of every new chat/session, run:

1. cat docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
2. git status --short
3. git log --oneline -n 8

Then continue only from:
- CLOSED
- ACTIVE
- DEFERRED
states in this file.

## 7. PATCH RULE
Before any patch:
- confirm target file role
- inspect surrounding authority logic
- check for duplicate logic
- define validation method
- do not patch closed tracks without fresh failing evidence

## 8. NEXT ALLOWED TASK

- Do NOT continue any prompt/bridge-level patching for wrap.

- Wrap is now:
  - Architecturally decided (qualification + handoff)
  - Authority-aligned
  - Runtime-blocked (signal honoring issue)

- Next work MUST be:
  1. Deep runtime execution analysis
  2. Trace why WRAP_FINISH in runtime_signals is not honored
  3. Identify where Phase 3A loop is re-triggered incorrectly
  4. Validate engine behavior (QUALIFICATION_ENGINE vs runtime signals)

- Allowed actions:
  - Add debug traces
  - Inspect runtime execution flow
  - Create focused UAT to isolate signal override behavior

- NOT allowed:
  - Adding new prompt overrides
  - Adding new phrase logic
  - Expanding wrap automation behavior

- Goal:
  Fix signal honoring at engine/runtime level, not surface logic.
