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
Status: ACTIVE
- Phase 3A validated
- Phase 3B validated
- Phase 5 continuity / render leakage fixed
- Runtime path broadly stable
- Phase 4 authority-alignment / strict UAT promotion is now active
- Treat Ceramic as under active Phase 4 completion, not fully closed

### Tint
Status: CLOSED
- Phase 0-2 recognition validated
- Real Phase 3A validated
- Phase 3B validated
- Phase 5 L1 / L2 / L3 validated
- Runtime path considered stable

### PPF
Status: ACTIVE
- Phase 3B price-ready path validated
- Phase 5 PPF verbatim rendering validated
- Earlier leakage concern was resolved as test-fixture / runner enforcement, not runtime drift
- Runtime path broadly stable
- Phase 4 strict UAT promotion now covers entry, first objection, silence, warranty sensitivity, technical sensitivity, brand fixation, and price resistance on branch
- Treat PPF as materially advanced in Phase 4, but not fully closed until overall active-service Phase 4 completion is reflected cleanly

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
Status: CLOSED
- Architecture path: qualification + manual handoff (CONFIRMED)
- Phase 3A finish capture validated
- Post-finish handoff behavior validated (ESCALATION_BLOCK_WRAP_QUOTE)
- Correct debug state enforced (phase=4, READY_FOR_NEGOTIATION, no price ladder)
- Earlier blockage traced to runner/harness execution-state enforcement, not runtime authority drift
- Runtime path considered stable

Rule:
- Do NOT expand wrap automation beyond handoff model
- Do NOT introduce Phase 5 wrap negotiation logic
- Only revisit if fresh runtime evidence contradicts current behavior

## 5. DO NOT TOUCH WITHOUT NEW EVIDENCE
- Ceramic runtime path outside active Phase 4 authority-alignment work
- Tint runtime path
- PPF runtime path outside active Phase 4 authority-alignment work
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

- Wrap is CLOSED.
- Do not reopen wrap unless fresh failing evidence appears.
- Current allowed work:
  - complete Phase 4 authority-alignment and strict UAT promotion for active services
  - keep using classified single-turn, state-injected UAT where harness continuity is not yet trusted
- Only after Phase 4 completion should Phase 5 completion review proceed service by service.
