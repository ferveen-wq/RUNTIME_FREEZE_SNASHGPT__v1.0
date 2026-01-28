tone_engine.md# TONE ENGINE

# DEPRECATED FILE — DO NOT USE

This file is superseded by:
PHASE4.5_TONE_ENGINE.md

Kept for audit history only.

version: 1.1
phase: 4.5
status: ACTIVE
owner: CONVERSATION_ARCHITECTURE

## PURPOSE
The Tone Engine controls how responses are delivered.
It regulates human-likeness, clarity, pressure level, and cultural appropriateness.
It does NOT generate sentences or content.

---

## DESIGN PRINCIPLES
- Prioritize clarity over persuasion
- Maintain zero-pressure communication
- Sound like a trained human advisor
- Adapt to GCC / MENA customer expectations
- Remain language-agnostic (EN / AR handled downstream)

---

## CORE TONE STATES
These tones are globally applicable.

- WARM_FRIENDLY
- NEUTRAL_PROFESSIONAL
- SOFT_REASSURING
- CONFIDENT_DIRECT
- PATIENT_EXPLANATORY
- CLOSING_SUPPORTIVE

---

## REGIONAL / MARKET-SPECIFIC TONES (GCC / MENA)
These tones address cultural expectations of trust, respect, and premium service.

- RESPECTFUL_TRADITIONAL
  Calm, polite, dignity-first tone.
  Used for first contact and Arabic-first customers.

- PREMIUM_CONCIERGE
  Polished, service-led, high-value tone.
  Used for premium vehicles and services.

- LOCAL_FRIENDLY
  Natural, conversational, locally familiar tone.
  Used in WhatsApp-style interactions.

- TRUST_BUILDING
  Honest, transparent, expectation-setting tone.
  Used for warranty, guarantees, and technical explanations.

- LOW_PRESSURE_EXIT
  Graceful, open-ended, non-pushy tone.
  Used when customer hesitates or disengages.

---

## TONE MODIFIERS
Modifiers refine tone without replacing it.

- REDUCE_PRESSURE
- INCREASE_CLARITY
- INCREASE_EMPATHY
- MINIMIZE_WORDS
- HUMANIZE_LANGUAGE

---

## SELECTION LOGIC (DETERMINISTIC)
Tone selection follows priority-based rules.

IF silence_state == PASSIVE:
    tone = SOFT_REASSURING
    modifier = REDUCE_PRESSURE

IF objection_state == ACTIVE:
    tone = PATIENT_EXPLANATORY
    modifier = INCREASE_EMPATHY

IF customer_region == GCC AND language == AR:
    tone = RESPECTFUL_TRADITIONAL

IF service_type == PREMIUM:
    tone = PREMIUM_CONCIERGE

IF trust_signals_required == TRUE:
    tone = TRUST_BUILDING

IF stage == CLOSING AND interest_level == HIGH:
    tone = CLOSING_SUPPORTIVE
    modifier = CONFIDENT_DIRECT

IF disengagement_detected == TRUE:
    tone = LOW_PRESSURE_EXIT
    modifier = MINIMIZE_WORDS

---

## LANGUAGE GUARDRAILS
The Tone Engine enforces the following constraints:

- No corporate or legal jargon
- No exaggerated marketing language
- No artificial urgency
- No emotional manipulation
- Emojis only when explicitly allowed

FORBIDDEN_PHRASES:
- "As per our policy"
- "Kindly be advised"
- "Limited time offer"
- "We recommend you decide now"

---

## OUTPUT CONTRACT
The Tone Engine returns:

- tone_state
- tone_modifier
- language_constraints

These outputs are consumed by Human Phrase Libraries.

---

## LOCKING RULE
The Tone Engine does not generate text.
It only influences how text is phrased.

LOCKED: FALSE