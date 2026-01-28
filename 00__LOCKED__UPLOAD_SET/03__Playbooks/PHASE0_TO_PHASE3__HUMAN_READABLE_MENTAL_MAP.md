# PHASE0_TO_PHASE3__HUMAN_READABLE_MENTAL_MAP.md
Version: 1.0
Status: REFERENCE ONLY (NON-EXECUTING)
Audience: Human operators, architects, auditors
Scope: SNASHGPT Runtime — Phase 0 to Phase 3

---

## WHY THIS DOCUMENT EXISTS

This document explains SNASHGPT **in human terms**.

It does NOT define logic.
It does NOT control runtime.
It does NOT override locked files.

It exists so that:
- the architecture can be understood without rereading specs
- future changes don’t accidentally break fundamentals
- humans can reason about the system like a real-world process

---

## THE STORY: SNASHGPT AS A REAL SALES ENVIRONMENT

Imagine a **car showroom with a strict operating protocol**.

Before a salesperson talks price, tone, or offers:
- the customer must be identified
- the context must be stable
- the system must confirm it is safe to proceed

SNASHGPT is built the same way.

---

## PHASE 0 — INTAKE & CONTROL  
*(Security gate + receptionist + rulebook)*

### Files Involved
- RUNTIME_LOAD_MANIFEST.md
- KNOWLEDGE__RUNTIME_CORE_BUNDLE.md

### What Phase 0 Represents (Human View)

Phase 0 is the **front gate of the building**.

Nothing enters the sales floor unless:
- the identity makes sense
- the conversation is not corrupted
- pricing pressure is not misread
- safety rules are respected

Phase 0 does **not sell**, **not persuade**, **not negotiate**.

It only decides:
> “Is it safe and valid to continue?”

---

## RUNTIME_LOAD_MANIFEST.md — THE CONSTITUTION

### Role (Storytelling)

This file is the **constitution + traffic controller**.

It defines:
- which phase runs first
- which files are allowed to load
- who wins if two files disagree
- what must NEVER exist here (pricing, tone, negotiation)

### Mental Model

Think of it as:
- airport control tower  
- bootloader  
- legal constitution  

It says:
> “Here is the order.  
> Break it, and nothing runs.”

It **references** the Core Bundle — it never duplicates it.

---

## KNOWLEDGE__RUNTIME_CORE_BUNDLE.md — THE IMMUTABLE GATEKEEPER

### Role (Storytelling)

This file is the **head of security**.

It enforces non-negotiable truths:
- one customer at a time
- no silent merges
- no learning from one incident
- no discount framing tricks
- no engine overrides

### What It Does NOT Do

It does not:
- calculate prices
- offer discounts
- handle objections
- recover silence
- persuade

### Mental Model

If RUNTIME_LOAD_MANIFEST is the law,
this file is the **judge that enforces it**.

---

## HOW PHASE 0 PROTECTS SALES (REAL SCENARIOS)

### Example: Discount Pressure

Customer says:
> “Can you do something on price?”

Phase 0:
- allows this signal to be classified
- blocks discount framing
- prevents “original price vs discounted price” tricks

Actual discount logic happens **later**, safely.

---

## PHASE 1 — QUALIFICATION  
*(Salesperson asking the right questions)*

### Files
- QUALIFICATION_ENGINE.md

### Role

Only after Phase 0 says “safe”,
qualification is allowed to begin.

This is where:
- needs are clarified
- intent is refined
- fit is determined

---

## PHASE 2 — KNOWLEDGE  
*(Facts, prices, timelines)*

### Files
- PRICE_REPOSITORY.md
- SERVICE_TIMELINE_REPOSITORY.md
- PRODUCT_KNOWLEDGE_CANON.md

### Role

These files:
- contain facts
- must never improvise
- must never override Phase 0 rules

They answer:
> “What is true?”

---

## PHASE 3 — PERSUASION & NEGOTIATION  
*(Human conversation skills)*

### Files
- NEGOTIATION_PRICE_LADDER_ENGINE.md
- SILENCE_HANDLING.md
- OBJECTIONS_AND_FRICTION_HANDLING.md
- TONE_PLAYBOOK.md

### Role

This is where:
- tone matters
- persuasion happens
- silence is handled
- objections are addressed

But even here:
- Phase 0 authority cannot be overridden
- pricing rules remain enforced
- safety always wins

---

## HOW ALL FILES INTERACT (MENTAL MAP)

1. Manifest decides order
2. Core Bundle enforces guardrails
3. Qualification clarifies intent
4. Knowledge provides facts
5. Persuasion delivers the message

If any layer breaks → flow stops.

---

## WHY THIS ARCHITECTURE IS FUTURE-PROOF

- Guardrails are centralized
- Engines are replaceable
- Sales logic cannot corrupt safety
- Learning cannot mutate behavior silently
- Humans can audit every decision

---

## FINAL NOTE (IMPORTANT)

If something feels “hard to do” in SNASHGPT,
that usually means:
> Phase 0 is protecting you from future damage.

This is intentional.

End of document.