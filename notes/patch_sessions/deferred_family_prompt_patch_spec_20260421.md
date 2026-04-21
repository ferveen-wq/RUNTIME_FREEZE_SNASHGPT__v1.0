# Deferred Family Prompt Patch Spec — 2026-04-21

## Purpose
Define the exact prompt-routing patch to evaluate next inside `runner/context_reset_prompt.txt`.

This is a design spec only.
It is NOT the runtime patch itself.

## Problem confirmed
Current prompt bridge recognizes:
- READINESS_STALL
- AUTHORITY_SHIFT
- SILENCE_AFTER_PRICE

But the Phase 5 service-owner routers still mostly resolve these into generic service-family deepen/default branches.

Observed effect:
- "let me think" -> generic deepen or silence
- "check with wife / family" -> generic deepen or wrong fallback
- "travelling / later / after salary" -> generic silence/deepen
- "car in garage / not received" -> generic deepen or wrong service family

## Working design decision
Deferred-family routing should branch BEFORE generic Phase 5 deepen/default routing.

## Proposed routing order

### A. Shared deferred-family pre-branch
Insert a shared pre-branch before the existing service-family default deepen logic.

Applies when ALL are true:
- request_type != PRICE_REQUEST
- QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
- price_ladder_state == FINAL_PRICE_REACHED
- active_service_context is present
- objection_signal is one of:
  - READINESS_STALL
  - AUTHORITY_SHIFT
  - SILENCE_AFTER_PRICE

## B. Internal split inside deferred-family pre-branch

### 1) AUTHORITY_SHIFT
Meaning:
- customer needs approval from wife / husband / family / friend / manager

Design intent:
- do NOT send to generic price-gap deepen by default
- do NOT send back to Phase 0–2 explanation
- prefer pause / open-door / later-safe handling family

### 2) READINESS_STALL
Meaning:
- let me think
- later
- after salary
- not now

Design intent:
- do NOT send to generic price-gap deepen by default
- prefer pause / open-door / later-safe handling family

### 3) SILENCE_AFTER_PRICE
Meaning:
- no reply / delayed stall / parked conversation

Design intent:
- keep silence-specific handling distinct from generic deepen
- do not let silence become service-specific objection deepen by default

## C. Temporary rule for this patch lane
Before dedicated deferred-family phrase IDs exist:
- patch must focus on routing separation only
- do NOT invent new phrase text
- do NOT patch runner hooks
- do NOT expand UAT broadly yet

## D. Main design choice to resolve
Open question:
- Should deferred-family pre-branch map temporarily to existing pause/open-door/exit-safe phrases,
  or should it only block generic deepen and stop with controlled fallback instructions?

## Preferred implementation direction
Preferred:
- add one shared deferred-family guard section before generic service-family deepen fallthrough
- then keep existing service-family routers for:
  - PRICE_TOO_HIGH
  - PRICE_COMPARISON
  - CONTROL_TEST
  - TRUST_OR_RISK
  - MISUNDERSTANDING
- but exclude deferred-family ownership cases from default deepen path

## Why this is safer
- avoids duplicating logic across ppf / ceramic / polishing / tint
- keeps ownership clean
- reduces wrong-phrase drift without touching phrase text yet
- matches control-tower reading already recorded

## Status
- Draft spec only
- Awaiting insertion-point review before live prompt patch
