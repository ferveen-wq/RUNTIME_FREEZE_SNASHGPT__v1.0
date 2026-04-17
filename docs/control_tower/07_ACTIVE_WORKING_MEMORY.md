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
- Phase 4 strict UAT promotion now covers silence, brand fixation, and price resistance on branch
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
  - PHASE5_CERAMIC_NARROW_L2
  - PHASE5_CERAMIC_EXIT_FORK_L3
- Canonical UAT is now 35 / 35 PASS on branch
- Treat Ceramic as complete for Phase 5 in the trusted lane, while overall multi-turn harness continuity remains untrusted

### Tint
Status: CLOSED
- Phase 0-2 recognition validated
- Real Phase 3A validated
- Phase 3B validated
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_TINT_COMPARE_DEEPEN_L1
  - PHASE5_TINT_NARROW_L2
  - PHASE5_TINT_EXIT_FORK_L3
- Canonical UAT is now 38 / 38 PASS on branch
- Runtime path considered stable

### PPF
Status: ACTIVE
- Phase 3B price-ready path validated
- Phase 5 PPF verbatim rendering validated
- Phase 5 PPF strict canonical coverage is now complete in the trusted single-turn, state-injected lane and includes:
  - PHASE5_PPF_PRICE_GAP_DEEPEN_L1
  - PHASE5_PPF_NARROW_L2
  - PHASE5_PPF_TECHNICAL_DEEPEN_L1
  - PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
  - PHASE5_PPF_EXIT_FORK_L3
- Earlier leakage concern was resolved as test-fixture / runner enforcement, not runtime drift
- Runtime path broadly stable
- Phase 4 strict UAT promotion now covers entry, first objection, silence, warranty sensitivity, technical sensitivity, brand fixation, and price resistance on branch
- Canonical UAT is now 32 / 32 PASS on branch
- Treat PPF as complete for Phase 5 in the trusted lane, while overall multi-turn harness continuity remains untrusted

### Polishing
Status: CLOSED
- Phase 0-2 recognition validated
- Phase 3A known-vehicle entry validated
- Phase 3A second qualifier continuity validated
- True Phase 3B readiness validated
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_POLISH_EXPECTATION_DEEPEN_L1
  - PHASE5_POLISH_NARROW_L2
  - PHASE5_POLISH_EXIT_FORK_L3
- Canonical UAT is now 41 / 41 PASS on branch
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
  - begin Phase 5 completion review service by service
  - keep using classified single-turn, state-injected UAT where harness continuity is not yet trusted
- Phase 4 active-service strict promotion is complete on branch for current active services.
