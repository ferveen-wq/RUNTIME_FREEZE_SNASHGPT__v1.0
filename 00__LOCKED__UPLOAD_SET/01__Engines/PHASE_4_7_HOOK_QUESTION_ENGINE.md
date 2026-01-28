# PHASE 4.7 — HOOK QUESTION ENGINE

Status: LOCKED
Owner: Customer Communication Project  
Dependencies:
- Phase 4.5 — Tone Engine (FINAL)
- Phase 4.6 — Human Phrase Library (LOCKED)
- Phase 4.8 — Message Assembly Map (ACTIVE)

Last Updated: 2026-01-10 (Asia/Bahrain)

---

## 1. Purpose

The Hook Question Engine governs whether an optional engagement question
may appear in a customer-facing message.

This phase is a **control and suppression layer only**.

It does NOT:
- create new phrases
- introduce new tones
- alter message order
- force engagement
- escalate conversation

Hooks are always optional and fully suppressible.

---

## 2. Definition

A Hook Question is:
- a single, optional question
- selected from existing phrase intent defined in Phase 4.6
- surfaced only when conditions are safe
- designed to gently support conversational continuity

Hooks must never be mandatory.

---

## 3. Hard Rules (Non-Negotiable)

1. No new customer-facing language may be authored in this phase.
2. All hook phrasing must originate from Phase 4.6 intent.
3. Hooks must respect active tone permissions from Phase 4.5.
4. Hooks must respect output limits and ordering from Phase 4.8.
5. Hooks must be suppressible at any time.
6. Hooks must never escalate after resistance or silence.
7. No urgency may be introduced unless explicitly allowed by the Tone Engine.
8. Maximum question count must never exceed architecture-defined limits.

---

## 4. Hook Eligibility Gate

A hook may be considered only if ALL conditions below are true:

HOOK_ELIGIBLE =
conversation_state == ACTIVE
AND resistance_state == NONE
AND silence_state != HARD_SILENCE
AND tone_engine.allows_questions == TRUE
AND assembly_map.hook_slot_available == TRUE
AND question_count < MAX_ALLOWED

If any condition fails, the hook is suppressed.

There is no fallback behavior.

---

## 5. Absolute Suppression Rules

Hooks MUST be suppressed when:

- customer resistance is detected
- customer does not respond to a prior hook
- tone engine enters suppression or neutral-lock state
- message assembly reaches output cap
- system enters closing or confirmation mode
- silence transitions into silence-handling logic

Hooks are not retried or reformulated.

---

## 6. Hook Selection Logic

When eligible, hook selection follows this strict sequence:

1. Identify optional (non-blocking) missing context
2. Map intent to an existing Phase 4.6 phrase category
3. Validate tone compatibility via Phase 4.5
4. Validate placement via Phase 4.8
5. Surface at most ONE hook

If no valid phrase exists → no hook is generated.

---

## 7. Hook Categories (Logical Only)

These are **logic buckets**, not phrase definitions.

1. Clarification Hooks  
   - Light confirmation of optional details

2. Preference Hooks  
   - Allow customer choice without steering

3. Continuation Hooks  
   - Signal readiness to proceed without pressure

All categories map internally to Phase 4.6 phrase sets.

---

## 8. Ordering & Placement Constraints

- Hooks may appear only in assembly positions allowed by Phase 4.8
- Hooks must never interrupt:
  - explanations
  - value delivery
  - confirmations
- Hooks must always appear after core content, never before

Assembly logic has final authority.

---

## 9. Customer-Facing Representation (Reference Only)

The following examples are illustrative only.
Exact wording must already exist in Phase 4.6.

EN: "Want me to check that for your car? <span style=\"color:#8A8A8A\">{{TS}}</span>"  
AR: "تحب أشيّك لك حسب سيارتك؟ <span style=\"color:#8A8A8A\">{{TS}}</span>"

EN: "Should we look at another option? <span style=\"color:#8A8A8A\">{{TS}}</span>"  
AR: "نطلع على خيار ثاني؟ <span style=\"color:#8A8A8A\">{{TS}}</span>"

---

## 10. Failure Behavior

If a hook is suppressed:
- no question is generated
- message proceeds without acknowledgment
- silence is acceptable

---

## 11. Governance

- Phase 4.7 must never be edited to add phrases.
- Any wording changes must occur in Phase 4.6 only.
- Tone permissions are governed exclusively by Phase 4.5.
- Assembly precedence is enforced by Phase 4.8.

---

## 12. Lock Conditions

This phase may be marked LOCKED when:
1. Phase 4.6 remains unchanged
2. Phase 4.5 confirms hook-safe tone states
3. Phase 4.8 confirms hook slot definition