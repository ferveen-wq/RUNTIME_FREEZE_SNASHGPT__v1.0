# Phase 5 Ownership Inventory — 2026-04-20

## Goal
Identify which live Phase 5 selectors are:
- central owner
- side authority
- safe guard only
- competing authority

## Live Phase 5 authorities seen in runner/context_reset_prompt.txt

### 1) PHASE5_PPF_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK
Type:
- render lock only

Role:
- does not choose service
- does not choose branch family
- only controls exact rendering after selection

Decision:
- keep
- not a routing owner

---

### 2) PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1 VERBATIM LOCK
Type:
- render lock only

Role:
- does not choose service
- does not choose branch family
- only controls exact rendering after selection

Decision:
- keep
- not a routing owner

---

### 3) PHASE 5 VERBATIM RENDERING
Type:
- render authority only

Role:
- outputs selected PHASE5 block verbatim
- does not decide service family

Decision:
- keep
- not a routing owner

---

### 4) CERAMIC REPEAT OBJECTION MUST NARROW
Type:
- side selector

Role:
- directly assigns PHASE5_CERAMIC_NARROW_L2 before central router

Risk:
- duplicates Phase 5 branch-selection authority
- competes with central selector model
- may be harmless in one lane but violates single-owner design

Decision:
- treat as competing Phase 5 selection authority
- review for demotion/removal from runtime ownership

---

### 5) PHASE 5 SERVICE-OWNER ROUTER
Type:
- central selector candidate

Role:
- chooses service family
- chooses branch inside service
- matches intended target model most closely

Decision:
- keep as primary runtime owner candidate

---

### 6) PHASE 5 TINT PHRASE SELECTION
Type:
- side selector

Role:
- directly assigns tint PHASE5 branch outside central router

Risk:
- duplicates branch-selection ownership
- violates single central selector model

Decision:
- treat as competing Phase 5 selection authority
- review for demotion/removal from runtime ownership

## Current planning conclusion

Phase 5 currently has:
- one central selector candidate
- plus side selectors that still assign PHASE5 selected_phrase_id directly

This is not fully aligned with the intended model:
- service already locked
- objection detected
- one central selector decides branch inside that service
- only that service speaks

## Safe planning direction

Do not patch yet until this rule is accepted:

Runtime Phase 5 ownership should be:
- render locks stay
- central selector stays
- side selectors that assign PHASE5 selected_phrase_id outside the central selector should be demoted or removed unless proven to be true guards that cannot be expressed inside the central selector

## Files
- runner/context_reset_prompt.txt
- notes/patch_sessions/gap_tr004_patch_plan_v1_20260420.md
