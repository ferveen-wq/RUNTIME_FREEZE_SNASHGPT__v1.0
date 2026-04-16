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
Status: NO ACTIVE OPEN DEFECT
- Prior objection routing work already stabilized on branch history
- Do not reopen unless a fresh failing case appears

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
Status: DEFERRED ARCHITECTURE DECISION
Business direction:
- Prefer qualification + manual handoff after initial qualification
- Do NOT continue ad hoc runtime patching

Observed authority conflict:
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md still describes WRAP_SCOPE
- QUALIFICATION_ENGINE.md says wrap automation is full-vehicle only and do NOT ask WRAP_SCOPE

Rule:
- Do NOT patch wrap runtime directly until final authority model is chosen

## 4. CURRENT ACTIVE TRACK
### Wrap
Status: DEFERRED ARCHITECTURE DECISION ONLY
- Do not continue runtime patching
- Only architecture decision / manual-handoff model discussion is allowed

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
