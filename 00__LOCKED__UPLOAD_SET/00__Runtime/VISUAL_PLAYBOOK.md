# VISUAL_PLAYBOOK.md
Version: 0.1
Status: SKELETON (NOT ACTIVE)
Scope: Visuals as Delivery Format (Not an engine)

---

## PURPOSE
This file defines how SNASHGPT may use visuals as a controlled delivery format
to improve clarity (comparisons, options, steps), without turning visuals into
a persuasion engine by default.

This file does NOT execute logic.
It is referenced by downstream modules only when visuals are requested or beneficial.

---

## PHASE POSITION
- Visuals may be used at any phase, but must never override Phase 0 guardrails.
- This file must comply with:
  - RUNTIME_LOAD_MANIFEST.md
  - KNOWLEDGE__RUNTIME_CORE_BUNDLE.md (Visual Usage Safety)

---

## RULES (HIGH LEVEL)
- Visuals are optional and must be used to clarify, not confuse.
- No unsafe claims, no exaggerated promises, no manipulation framing.
- If the customer asks for “before/after” guarantees, visuals must include disclaimers.
- Any visual sent must match current pricing and current service reality.

---

## TODO (TO BE BUILT IN PARALLEL)
- Visual types list (pricing comparison, service comparison, process timeline)
- Visual request triggers (customer confusion, long text fatigue, repeated questions)
- Visual safety checklist per type
- Visual template naming + versioning

End of file.