# PHASE 9 — TRUST WORKING REFERENCE

Purpose:
Define the current working logic for trust / credibility behavior before runtime promotion.

Status:
- Logic discussed and manually validated in chat
- Not yet runtime-patched
- Must be revisited before rollout freeze

------------------------------------------------------------
TRIGGERS
------------------------------------------------------------

Phase 9 trust behavior may activate when customer shows:

1. TRUST_DOUBT
- "how do I know this is original?"
- "is this genuine?"
- "what brand do you use?"

2. RISK_DOUBT
- "what if it damages the paint?"
- "what if it peels?"
- "what if installation is bad?"

3. DECISION_HESITATION
- "i'll think and come back"
- "still thinking"
- "not sure"

------------------------------------------------------------
RESPONSE TYPES
------------------------------------------------------------

- Trust doubt -> credibility reassurance
- Risk doubt -> safety reassurance
- Hesitation -> calm reassurance

------------------------------------------------------------
VISUAL PRIORITY
------------------------------------------------------------

If visual is allowed, preferred order:

1. TESTIMONIAL
2. TRUST
3. RESULT

Do NOT prefer:
- PROOF
- PROCESS

unless the intent clearly changes.

------------------------------------------------------------
RULES
------------------------------------------------------------

- No technical deep dive by default
- No pricing push
- No overload
- Max 1 visual
- Max 1 soft forward question
- No urgency pressure
- No trust video during silence state
- Price resistance remains Phase 7 primary, not Phase 9 primary

------------------------------------------------------------
MANUAL VALIDATION SUMMARY
------------------------------------------------------------

Scenarios manually checked in working session:

- hesitation -> no visual, calm tone
- trust doubt -> trust visual allowed
- price resistance -> Phase 7 takes priority
- risk concern -> reassurance first, visual optional

------------------------------------------------------------
NEXT STEP
------------------------------------------------------------

- Build final test pack
- Then decide whether Phase 9 needs runtime patch
