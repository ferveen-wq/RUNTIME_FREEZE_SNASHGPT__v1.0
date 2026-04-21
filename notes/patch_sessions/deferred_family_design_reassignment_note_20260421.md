# Deferred Family Design Reassignment Note — 2026-04-21

## Purpose
Define the next patch lane at design level only.
This is NOT a runtime patch.
This note decides what kind of patch is allowed later.

## Real problem
Current evidence shows the system often understands deferred-family messages as generic late friction, but routes them into the wrong branch:
- generic silence
- generic deepen
- wrong service-family phrase
- or even back to Phase 0-2 explanation

So the issue is not “missing examples”.
The issue is “missing ownership-specific routing design”.

## Deferred-family groups

### 1) Thinking / timing-later
Examples:
- let me think
- later
- next month
- after salary
- I will confirm later

Current owner reading:
- Phase 3 PIM blockers
- READINESS_STALL in objection resolution
- Phase 5 follow-up / open-door if conversation is parked

Design question:
- Should this family get:
  A) dedicated deferred-family phrase IDs
  or
  B) a dedicated routing branch before generic Phase 5 deepen branches?

### 2) Third-party approval
Examples:
- I need to ask my wife
- I need to ask my husband
- I need to ask family
- I need to ask my friend
- I need manager approval

Current owner reading:
- AUTHORITY_SHIFT in objection resolution
- Phase 5 pause / follow-up / handover if needed

Design question:
- Should AUTHORITY_SHIFT route to:
  A) dedicated authority-shift phrases
  or
  B) a controlled open-door / pause family inside Phase 5?

### 3) Car unavailable / logistics blocked
Examples:
- car is in garage
- car is in workshop
- I did not receive the car yet
- car is not with me

Current owner reading:
- Phase 3 PIM_CAR_NOT_AVAILABLE
- Phase 5 later/follow-up if parked

Design question:
- Should car-unavailable cases stay suppression-first in orchestration,
  with no deepen phrase by default?

### 4) Travelling / unavailable
Examples:
- I am travelling
- out of country
- busy these days
- will come back later

Current owner reading:
- Phase 3 PIM_TRAVELLING
- Phase 5 later/follow-up if parked

Design question:
- Should travel cases be treated like timing blockers,
  with silence suppression first and no generic objection deepen?

## Working design guardrails
Any future patch in this lane must follow:

1. Do NOT patch runner first
2. Do NOT patch phrase text first
3. Do NOT patch from cheat cards / helper notes
4. First decide:
   - owner
   - routing entry point
   - fallback order
   - whether dedicated phrase family is needed

## Recommended next patch type
Preferred next lane:
- prompt-routing design patch only

Not yet allowed:
- phrase library expansion
- runner normalization hooks
- broad UAT expansion
- support-material retrieval for wording

## Proposed design decision to evaluate next
Candidate:
- Deferred-family cases should branch BEFORE generic Phase 5 deepen/default routing.
- AUTHORITY_SHIFT and READINESS_STALL should not fall through to normal price-gap deepen branches by default.
- PIM travel / car-unavailable / timing-not-ready should prefer suppression-or-park logic before phrase deepen logic.

## Status
- Design note only
- Awaiting next controlled patch lane
