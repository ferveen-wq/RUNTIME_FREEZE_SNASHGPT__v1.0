# PHASE 5.2 — HANDOVER WORKFLOW (BOOKING, FOLLOW-UP, HUMAN TAKEOVER) — v1.0 (DRAFT)

## A) Booking workflow (WhatsApp ops)
Goal: move from “intent” to “confirmed next action” with minimal steps.

### Booking data (collect only what is needed)
- Service type (if not already known)
- Preferred date/time window OR “next available”
- Location / area
- Special notes (optional)

### Booking steps
1) Confirm intent (TPL_BOOKING_CONFIRM_INTENT)
2) Ask for key details: date/time + location (TPL_BOOKING_ASK_DETAILS)
3) Confirm summary back (TPL_BOOKING_CONFIRM_SUMMARY)
4) Close politely (TPL_CLOSE_BOOKED)

### Route to human during booking if
- Customer asks for exceptions / disputes / complaint tone
- Customer refuses to provide critical info after 2 tries
- Customer explicitly wants a call or a human

Use template:
- TPL_HUMAN_ACK_HANDOVER (+ optional TPL_HUMAN_ONE_DETAIL)

---

## B) Follow-up workflow
Use follow-up when:
- Customer said later / will confirm
- Customer went silent after progress toward a decision

Principles:
- 1 clear nudge, then 1 gentle final, then stop.
- Never guilt-trip.
- Always give an easy option to reply.

Follow-up cap:
- Max 2 follow-up messages total per thread unless customer re-engages.

Use templates:
- TPL_SILENCE_FOLLOWUP_1
- TPL_SILENCE_FOLLOWUP_2_FINAL
- TPL_CLOSE_OPEN_DOOR

---

## C) Human takeover workflow
Trigger takeover when:
- Customer asks for human/agent/call
- Complaint / anger / trust issue
- Confusing loop: 2+ cycles without progress
- Exceptions are needed

Steps:
1) Acknowledge and set expectation (TPL_HUMAN_ACK_HANDOVER)
2) Ask for 1 key detail only if needed (TPL_HUMAN_ONE_DETAIL)
3) Close politely and stop automation until human responds