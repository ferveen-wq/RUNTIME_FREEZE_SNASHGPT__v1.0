# ISSUE_011 — Wrap Phase 3A Specialist Handover Flow

## Type
Runtime Flow / Handover Architecture

## Problem
Wrap is not intended to follow the same fully automated pricing workflow as PPF/Ceramic/Tint/Polishing.

Current wrap flow:
- Phase 0–2 recognizes wrap
- Phase 3A asks `PHASE3A_Q_WRAP_FINISH`
- After finish answer, downstream handover point is not clearly defined

## Evidence
- `HANDOVER_REQUIRED_FLAG` already exists in `RUNTIME_STATE_MACHINE.md`
- If `HANDOVER_REQUIRED_FLAG == TRUE`, automation stops and `AGENT_TAKEOVER_FLAG = TRUE`
- `RUNTIME_EXECUTION_FLOW.md` has `handover_required_flag` and `handover_reason`
- `PHASE4_6_HUMAN_PHRASE_LIBRARY.md` has no dedicated wrap specialist handover phrase
- `PRICE_LADDER_ENGINE.md` still has wrap price ladder references
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md` says do NOT ask `WRAP_SCOPE` in automated runtime flow

## Intended Flow
After customer answers `PHASE3A_Q_WRAP_FINISH`, SNASHGPT should:
- acknowledge wrap needs specialist coordination
- ask for contact number or offer quick visit
- set `HANDOVER_REQUIRED_FLAG = TRUE`
- set `handover_reason = wrap_specialist_required`
- avoid `READY_FOR_NEGOTIATION`
- avoid price ladder
- stop automation

## Customer-Facing Message Direction

AR:
تمام 👌 بالنسبة للتغليف (Wrap)، يحتاج تنسيق بسيط مع المختص حسب التصميم والتغطية. تقدر ترسل رقمك وبيكلمك الفريق على الواتساب؟ أو إذا تحب نحدد لك موعد زيارة سريعة.

EN:
Got it 👌 For wrapping, it needs a quick check with our specialist depending on the design and coverage. You can share your number and our team will contact you on WhatsApp, or we can book a quick visit for you.

## Patch Constraints
- Do not create full automated wrap pricing.
- Do not ask `WRAP_SCOPE` automatically.
- Do not set `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION` for wrap handover.
- Use existing handover signals.
- Add one dedicated phrase block only.
- Patch only after owner confirmation.

## Status
OPEN

## Output Template Escalation Finding — 2026-04-25

Raw wrap handover UAT produced:
- `selected_phrase_id = ESCALATION_BLOCK_WRAP_QUOTE`
- `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION`
- `phase = 4`
- `price_ladder_state = NONE`

Inspection found:
- `ESCALATION_BLOCK_WRAP_QUOTE` is not an explicit phrase-library block.
- `OUTPUT_RESPONSE_TEMPLATE.md` contains a generic `ESCALATION BLOCK (Quote / Human Handoff)`.
- This formatting block can behave like a customer-facing phrase generator.

Architecture risk:
- `OUTPUT_RESPONSE_TEMPLATE.md` should format only.
- It should not create competing selected_phrase_id behavior against `PHASE4_6_HUMAN_PHRASE_LIBRARY.md` and `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`.

Decision:
- Patch must ensure wrap specialist handover uses approved phrase block:
  `PHASE3A_WRAP_SPECIALIST_HANDOVER`
- Output template escalation must not override wrap handover routing.
- Future patch due diligence must search for generic labels:
  `ESCALATION`, `HANDOVER`, `QUOTE`, `SPECIALIST`, `CONTACT`
  before adding new handover/quote phrases.
