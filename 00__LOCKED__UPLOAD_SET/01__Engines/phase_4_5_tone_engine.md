# phase 4.5 — tone engine

status: LOCKED
phase: 4.5
scope: tone selection & enforcement
dependencies:
- Phase 4.6 (Human Phrase Library) LOCKED
- Phase 4.7 (Hook Question Engine) LOCKED
- Phase 4.8 (Message Assembly Map) LOCKED

---

## purpose

Define *how* messages should feel — not *what* they say.

The Tone Engine:
- Selects the appropriate conversational tone
- Enforces emotional and behavioral boundaries
- Governs urgency, softness, neutrality, and restraint
- Does NOT generate phrases or sentences

All language output comes exclusively from Phase 4.6.

---

## core principles

1. Tone influences selection, not wording
2. Tone must never override Human Phrase Library constraints
3. Tone cannot introduce urgency unless explicitly allowed
4. Tone selection must be reversible (until closing lock)
5. Tone must feel human, calm, and adaptive — never scripted

---

## supported tones (initial set)

These tones are **contextual states**, not styles.

### T1 — Neutral / Informational
Use when:
- Customer is asking factual questions
- No resistance or urgency is detected

Constraints:
- No persuasion
- No hooks unless explicitly requested
- No emotional framing

---

### T2 — Reassuring / Supportive
Use when:
- Customer shows hesitation or uncertainty
- Clarification is needed without pressure

Constraints:
- Calm pacing
- No urgency
- Hooks suppressed unless customer invites next step

---

### T3 — Exploratory / Guiding
Use when:
- Customer is engaged but undecided
- Options are being discussed

Constraints:
- One soft directional cue allowed
- No price pressure
- Hooks allowed only if Phase 4.7 permits

---

### T4 — Reserved / De-escalation
Use when:
- Objections, resistance, or silence detected
- Emotional tension is present

Constraints:
- Hooks fully suppressed
- No persuasion
- Focus on normalization and space

---

### T5 — Closing-Ready (Soft)
Use when:
- Customer intent is explicit
- Decision momentum exists

Constraints:
- No hard urgency
- No price push
- Tone must remain respectful and optional

---

## tone selection inputs

Tone Engine evaluates:

- Customer intent (question / compare / decide)
- Emotional signal (neutral / hesitant / resistant)
- Conversation stage (early / mid / late)
- Prior tone already used (avoid repetition)
- Suppression signals from Silence or Objection engines

---

## tone & assembly interaction

The Tone Engine may:
- Allow or suppress hooks
- Limit block types selectable in Phase 4.8
- Enforce softness or neutrality

The Tone Engine may NOT:
- Change phrase wording
- Reorder message structure
- Override safety rules defined elsewhere

---

## hard safety rules

- Tone may never combine urgency + persuasion
- Tone may never escalate after resistance
- Tone may never contradict Phase 4.6 phrasing intent
- Tone may never bypass Phase 4.8 assembly constraints

---

## governance notes

this file defines tone logic only.
it may be locked once:
- phase 4.7 (hook question engine) is LOCKED
- phase 4.8 (message assembly map) is FINALIZED

this file may be reviewed but must not be locked until phase 4.8 is finalized.