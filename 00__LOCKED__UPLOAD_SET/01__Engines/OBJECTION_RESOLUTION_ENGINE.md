## 1. PURPOSE & HARD BOUNDARIES

### 1.1 Purpose
This engine deterministically handles objections that occur **after pricing has been exposed**.

It decides ONLY:
- CONTINUE / PAUSE / ESCALATE / EXIT
- quote_required (TRUE/FALSE)
- automation_allowed (TRUE/FALSE)

### 1.2 Hard Boundaries (Non-Negotiable)
This engine MUST NOT:
- Generate customer-facing language (Arabic/English or any wording)
- Negotiate, persuade, pressure, or emotionally frame
- Modify, override, or reinterpret Price Ladder outputs
- Create new prices, discounts, bundles, or offers
- Introduce service steering or solution recommendation
- Use marketing scripts, hooks, or “selling” content
- Call external tools, repos, or runtime execution

### 1.3 Allowed Inputs (Read-Only)
This engine may read signals produced by:
- NEGOTIATION_LOGIC_MODULE.md (state + permissions)
- PRICE_LADDER_ENGINE.md (price exposure stage only)
- CUSTOMER_CHAT_INTAKE_RULES.md (objection classification signal)
- Alias note: Treat any reference token like `OBJECTIONS_AND_FRICTION_HANDLING` as pointing to the canonical file `OBJECTIONS_AND_FRICTION_HANDLING.md` (do not create duplicates).

### 1.4 Outputs (Decision Only)
This engine outputs a decision object for orchestration use only.
No customer message text is produced here.

### 1.5 Audit-Only Analytics Tags (AUDIT-ONLY)
These tags are attached for internal QA/training/win-loss review only.

Hard rules:
- MUST NOT change decision logic (CONTINUE/PAUSE/ESCALATE/EXIT)
- MUST NOT change routing or orchestration behavior
- MUST NOT generate customer-facing text

Audit tags (internal-only):
- audit_phase: ENUM
- audit_category: ENUM
- audit_severity: ENUM
- audit_outcome: ENUM

## 2. INPUT CONTRACT

### 2.1 Required Inputs
This engine operates only on pre-classified system signals.

It does NOT parse raw customer messages.

```yaml
INPUTS:
  QUALIFICATION_STATUS: ENUM
  negotiation_state: ENUM
  price_ladder_state: ENUM
  objection_signal: ENUM
  objection_repeat_count: INTEGER
  customer_response_latency: ENUM

  2.2 ENUM Definitions

  QUALIFICATION_STATUS:
  - QUALIFIED
  - PARTIALLY_QUALIFIED
  - NOT_QUALIFIED
  # NOTE: negotiation_state reflects FLOW CONTROL, not bargaining

negotiation_state:
  - PRICE_PRESENTED
  - PRICE_ACKNOWLEDGED
  - OBJECTION_RAISED
  - STALLED
  - TERMINATED

price_ladder_state:
  - IN_PROGRESS
  - FINAL_PRICE_REACHED
  - ESCALATED_TO_QUOTE
  - TERMINATED_NO_PRICE

customer_response_latency:
  - IMMEDIATE
  - DELAYED
  - SILENT

  audit_phase:
  - POST_PRICING
  - UNKNOWN

audit_category:
  - PRICE_TOO_HIGH
  - CHEAPER_ELSEWHERE
  - DISCOUNT_REQUEST
  - SCOPE_MISMATCH
  - TRUST_OR_QUALITY_DOUBT
  - DECISION_DELAY
  - INFO_GAP
  - POLICY_OR_APPROVAL
  - OTHER

audit_severity:
  - LOW
  - MEDIUM
  - HIGH

audit_outcome:
  - CONTINUING
  - PAUSED_WAITING_INFO
  - ESCALATED_HUMAN
  - EXITED_NO_COMMITMENT
  - UNKNOWN

  2.3 Input Assumptions
	•	All inputs are produced by upstream locked engines.
	•	Objection classification is completed before this engine runs.
	•	This engine treats all inputs as read-only.

  ---

### Quick sanity check for you (important)
If tomorrow you forget everything else, remember this:
> **This engine never “listens” to words — only to tags.**

That’s why it stays clean.

---

When ready, say **“NEXT SECTION”** and we’ll move to  
**Step 3: Objection Taxonomy (mapping your A–H matrix into system signals)**.

<span style="color:#7f8c8d">2026-01-07 00:00 +0300</span>

## 3. OBJECTION TAXONOMY (SYSTEM LABELS)

### 3.1 Definition
Objections are represented as **system labels**, not customer wording.

The label is provided by upstream classification.
This engine does not infer the label from raw text.

### 3.2 Objection Labels

```yaml
objection_signal:
  # Price resistance (emotion / sticker shock)
  - PRICE_TOO_HIGH

  # “Cheaper elsewhere”, “same thing there”, comparisons
  - PRICE_COMPARISON

  # “Best price?”, “discount?”, control/authority test
  - CONTROL_TEST

  # Trust, fear, quality, warranty doubt, risk hesitation
  - TRUST_OR_RISK

  # Confusion about service meaning (PPF vs ceramic, warranty terms, process)
  - MISUNDERSTANDING

  # “Let me think”, “later”, readiness stall (not explicit objection)
  - READINESS_STALL

  # “Need to ask wife/partner/manager” (decision authority moved)
  - AUTHORITY_SHIFT

  # No reply after pricing / explanation (silence)
  - SILENCE_AFTER_PRICE

  # Anything not classifiable
  - UNKNOWN_OR_AMBIGUOUS

  3.3 Classification Notes (Non-Behavioral)
	•	PRICE_TOO_HIGH = emotional cost reaction without comparison proof
	•	PRICE_COMPARISON = explicit external comparison or screenshot / “other shop”
	•	CONTROL_TEST = direct push for discount / final price / “best price”
	•	TRUST_OR_RISK = fear-based hesitation (quality, warranty, damage risk)
	•	AUTHORITY_SHIFT = decision moved to a third party
	•	SILENCE_AFTER_PRICE = no reply + no reaction after price exposure

## 4. RESOLUTION PATHS (DETERMINISTIC ROUTING)

### 4.1 Default Rule
If an objection is present, negotiation_state MUST be treated as OBJECTION_RAISED for downstream orchestration.

### 4.2 Routing Rules by Objection Signal

```yaml
ROUTING_RULES:

  # 1) PRICE_TOO_HIGH (sticker shock)
  - IF: objection_signal == PRICE_TOO_HIGH
    THEN:
      IF_FINAL_PRICE_REACHED:
        decision: ESCALATE
        quote_required: TRUE
        automation_allowed: FALSE
      ELSE:
        decision: CONTINUE
        quote_required: FALSE
        automation_allowed: TRUE

  # 2) PRICE_COMPARISON (cheaper elsewhere / same thing)
  - IF: objection_signal == PRICE_COMPARISON
    THEN:
      decision: PAUSE
      quote_required: FALSE
      automation_allowed: TRUE

  # 3) CONTROL_TEST (best price / discount push)
  - IF: objection_signal == CONTROL_TEST
    THEN:
      IF_FINAL_PRICE_REACHED:
        decision: ESCALATE
        quote_required: TRUE
        automation_allowed: FALSE
      ELSE:
        decision: CONTINUE
        quote_required: FALSE
        automation_allowed: TRUE

  # 4) TRUST_OR_RISK (warranty doubt / fear / credibility)
  - IF: objection_signal == TRUST_OR_RISK
    THEN:
      decision: ESCALATE
      quote_required: TRUE
      automation_allowed: FALSE

  # 5) MISUNDERSTANDING (confusion about service/process)
  - IF: objection_signal == MISUNDERSTANDING
    THEN:
      decision: CONTINUE
      quote_required: FALSE
      automation_allowed: TRUE

  # 6) READINESS_STALL (later / let me think)
  - IF: objection_signal == READINESS_STALL
    THEN:
      decision: PAUSE
      quote_required: FALSE
      automation_allowed: TRUE

  # 7) AUTHORITY_SHIFT (need approval)
  - IF: objection_signal == AUTHORITY_SHIFT
    THEN:
      decision: PAUSE
      quote_required: TRUE
      automation_allowed: FALSE

  # 8) SILENCE_AFTER_PRICE (no reply + no reaction)
  - IF: objection_signal == SILENCE_AFTER_PRICE
    THEN:
      decision: PAUSE
      quote_required: FALSE
      automation_allowed: TRUE

  # 9) UNKNOWN_OR_AMBIGUOUS
  - IF: objection_signal == UNKNOWN_OR_AMBIGUOUS
    THEN:
      decision: ESCALATE
      quote_required: TRUE
      automation_allowed: FALSE

      HELPERS:
  IF_FINAL_PRICE_REACHED: (price_ladder_state == FINAL_PRICE_REACHED)

  ## 5. REPEAT GUARDRAILS (ANTI-LOOP RULES)

### 5.1 Purpose
Prevent repetitive cycles and enforce deterministic escalation when objections repeat.

### 5.2 Definitions

```yaml
REPEAT_POLICY:
  repeat_count_meaning:
    0: first occurrence of this objection signal after price exposure
    1: second occurrence
    2: third occurrence or more

  hard_thresholds:
    max_automation_repeats: 1
    force_escalation_repeat_count: 2

    5.3 Global Guardrail (Applies to All Objections)

    GLOBAL_REPEAT_GUARDRAIL:
  - IF: objection_repeat_count >= force_escalation_repeat_count
    THEN:
      decision: ESCALATE
      quote_required: TRUE
      automation_allowed: FALSE

      5.4 Exception Handling (Silence)

      SILENCE_EXCEPTION:
  - IF: objection_signal == SILENCE_AFTER_PRICE
    THEN:
      # Silence is handled by recovery rules elsewhere.
      # This engine only pauses and permits automation.
      decision: PAUSE
      quote_required: FALSE
      automation_allowed: TRUE

      5.5 Notes (Non-Behavioral)
	•	This section overrides CONTINUE rules when repetition threshold is reached.
	•	This section does not change pricing or language behavior.

  ## 6. TERMINAL CONDITIONS & HUMAN HANDOFF

### 6.1 Terminal Conditions (EXIT)
EXIT is permitted only when any of the following are true:

```yaml
EXIT_RULES:
  - IF: QUALIFICATION_STATUS == NOT_READY
    THEN:
      decision: EXIT
      quote_required: FALSE
      automation_allowed: FALSE

  - IF: negotiation_state == TERMINATED
    THEN:
      decision: EXIT
      quote_required: FALSE
      automation_allowed: FALSE

      6.2 Human Handoff (ESCALATE)

ESCALATE means: stop automation and require human handling.

HUMAN_HANDOFF_RULES:
  - IF: decision == ESCALATE
    THEN:
      automation_allowed: FALSE
      quote_required: TRUE

      6.3 Conflict Priority (Deterministic Precedence)

If multiple rules apply, use this priority order (highest first):

RULE_PRIORITY_ORDER:
  1: EXIT_RULES
  2: GLOBAL_REPEAT_GUARDRAIL
  3: ROUTING_RULES
  4: SILENCE_EXCEPTION

  7. OUTPUT CONTRACT (DECISION OBJECT ONLY)

  OUTPUT:
  decision: ENUM            # CONTINUE | PAUSE | ESCALATE | EXIT
  quote_required: BOOLEAN   # TRUE | FALSE
  automation_allowed: BOOLEAN # TRUE | FALSE
  objection_signal: ENUM
  objection_repeat_count: INTEGER
  negotiation_state: ENUM
  price_ladder_state: ENUM

    # AUDIT-ONLY (non-behavioral analytics tags)
  audit_phase: ENUM
  audit_category: ENUM
  audit_severity: ENUM
  audit_outcome: ENUM

  ---

## ENGINE LOCK STATUS

STATUS: LOCKED  
ENGINE: OBJECTION_RESOLUTION_ENGINE  
PHASE: 3  
LOCK_REASON:  
- Post-pricing objection logic finalized  
- Decision outputs validated (CONTINUE / PAUSE / ESCALATE / EXIT)  
- AUDIT-ONLY analytics tags added (phase, category, severity, outcome)  
- Dry-run scenarios validated  
- No runtime behavior mutation  

LOCK_DATE: 2026-01-07  
LOCK_SCOPE:
- Decision logic frozen
- Audit tags observational only
- No pricing, tone, phrasing, or silence logic permitted here

---