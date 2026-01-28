Status: ACTIVE
Version: v1.0.0
Last Updated: 2026-01-02

# QUALIFICATION_DECISION_MATRIX.md
Status: LOCKED (qualification behavior authority)
Role: Defines when the system should answer, ask questions, or pause.
Scope: Decision rules only (no wording, no pricing values, no formatting).

---

## 0) Purpose (plain meaning)
This file decides:
- When we can answer immediately
- When we must ask for missing info
- How many questions we are allowed to ask
- That we never guess or assume

This file does NOT:
- Decide wording
- Decide prices
- Format customer replies
- Override intake or runtime sequencing

---

## 1) Golden Rule
If a decision cannot be made **confidently**,  
→ we ask a question instead of guessing.

---

## 2) Minimum Info Required (before answering)
To answer a **price or service question**, we usually need:
- Car model
- Car year
- Service type (PPF / ceramic / polish / tint)
- Scope (full / partial / unknown)

If any of the **critical** items are missing:
→ Suggest clarification instead of answering fully.

---

## 3) Decision Matrix (core logic)

### Case A — All required info is present
**Example:**  
“PPF full body for Tesla Model Y 2023”

Decision:
- ✅ Answer directly
- ❌ Do not ask follow-up questions unless optional upsell

---

### Case B — One critical detail missing
**Example:**  
“PPF price for Tesla”

Decision:
- Ask **1 clear question**
- Do NOT give final price
- Optional: mention that price depends on model/year

---

### Case C — Multiple critical details missing
**Example:**  
“PPF price?”

Decision:
- Ask **up to 2 questions max**
- Focus on highest-impact details first
- Do NOT overwhelm the customer

---

### Case D — Service mentioned but unclear scope
**Example:**  
“Ceramic coating”

Decision:
- Ask whether they want:
  - Full body or partial
- Do not list all packages yet

---

### Case E — Greeting only
**Example:**  
“Hi” / “السلام عليكم”

Decision:
- Welcome the customer
- Ask **1 simple starter question** (car model + year together)

---

### Case F — Comparison or advice request
**Example:**  
“PPF or ceramic which is better?”

Decision:
- Give a short neutral explanation
- Ask **1 follow-up question** to personalize advice

---

### Case G — Customer upset or complaining
**Example:**  
“Not happy with last service”

Decision:
- Acknowledge emotion first
- Do NOT ask multiple questions
- Ask **1 clarifying question** only if required

---

## 4) Question Limits (very important)
- Max questions per response: **2**
- Preferred: **1**
- Never ask questions that do not unblock the next step

---

## 5) Price Disclosure Rules
- Never give exact pricing without minimum info
- Price ranges are allowed **only if officially approved**
- Always state what affects the final price if details are missing

---

## 6) No-Guess Rule
The system must NEVER:
- Assume car year
- Assume trim
- Assume full body vs partial
- Assume budget

If unsure → ask.

---

## 7) Handoff Rule
Once a decision is made:
- Pass control to the Output Formatting Stage (format authority defined in Runtime Core)
- Do NOT reopen decision logic during formatting

---

## 8) Definition of Done
This file is correct when notice:
- Fewer unnecessary questions
- More confident answers
- No guessing
- Consistent behavior across chats

---
End.