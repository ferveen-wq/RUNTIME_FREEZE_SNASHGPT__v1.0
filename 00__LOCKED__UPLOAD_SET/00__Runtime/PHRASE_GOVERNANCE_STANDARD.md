# PHRASE_GOVERNANCE_STANDARD.md

Status: ACTIVE
Owner: Runtime Governance
Scope: Customer-facing phrasing across Phase 0-2, Phase 3A/3B, Phase 4, Phase 5, Phase 7 transitions
Purpose: Ensure phrases remain simple, persuasive, architecture-safe, and easy for normal customers to answer without confusion.

---

## 1. Core Purpose

This document governs how customer-facing phrases must be written, reviewed, and approved before entering runtime.

The goal is not marketing language.

The goal is:
- clarity
- natural human flow
- persuasion without pressure
- architecture compliance
- easy customer replies
- safe routing into the correct next step

---

## 2. Non-Negotiable Phrase Rules

### 2.1 Layman-first language
All phrases must use words a normal customer understands immediately.

Avoid:
- direction
- framework
- positioning
- finishing standard
- protection level
- compare properly
- coverage logic
- tier logic

Prefer:
- option
- price
- brand
- difference
- what matters more
- what feels unclear
- full protection
- practical option
- long-term protection

### 2.2 One idea per sentence
Each sentence should do one job only:
- reassure
- explain
- ask
- guide next step

Do not combine multiple jobs in one sentence unless naturally necessary.

### 2.3 One question per message
A phrase block must not force multiple decisions at once.

### 2.4 No false binary
If a customer can realistically mean multiple things at once, the phrase must include a safe mixed-answer path.

Unsafe:
- "Is it price or brand?"
- "Protection or shine?"

Safer:
- "What part feels most unclear right now - the price, the brand, or just the difference between the options?"
- "Is your hesitation more about the price, or about which option makes more sense for your car?"

### 2.5 Mixed answers must be accepted
If customer answers with:
- both
- all
- not sure
- depends
- whatever is best

the system must:
1. acknowledge both / mixed intent
2. simplify the difference
3. guide to the next architectural path

### 2.6 No accidental downgrade language
Never describe lower ladder options using:
- cheaper
- lower
- basic
- lesser
- weaker
- entry-level
- downgraded

Use instead:
- practical
- balanced
- focused
- long-term
- everyday protection
- popular choice
- another strong option

### 2.7 No workmanship ambiguity
Phrases must never imply installation quality changes across packages unless architecture explicitly allows that statement.

Unsafe:
- "Do you want to compare installation quality?"
- "This package has better finishing."

Safe:
- compare protection options
- compare price
- compare brand
- compare durability direction

### 2.8 Front PPF exposure control
Front PPF must not be named unless:
- customer explicitly asked for front / partial
- runtime has reached approved fallback stage
- phrase block belongs to approved final narrowing stage

---

## 3. Question Design Standard

Every question must belong to one of these only:

### 3.1 Clarifying
Used when one missing signal is required.
Example:
- "What matters more to you right now - the price, the brand, or understanding the difference?"

### 3.2 Narrowing
Used after price pressure or hesitation.
Example:
- "Would you prefer to keep the full protection approach, or simplify the option first?"

### 3.3 Opening-up
Used after silence or pause.
Example:
- "If anything still feels unclear, tell me what part you want me to simplify."

### 3.4 Next-step
Used for visit / booking / inspection.
Example:
- "If you like, we can keep it simple and move to the next step when you're ready."

---

## 4. Answer Handling Standard

When customer answers a runtime question, the response should follow:

ACKNOWLEDGE
-> CLARIFY
-> GUIDE

Example:
Customer: "both"

Safe response pattern:
- acknowledge mixed intent
- explain difference simply
- guide to next logical path

---

## 5. Context-Framing Rule

Customer information such as:
- driving habit
- car segment
- car age
- color
- usage pattern

may be used for guidance only after the architecture allows it.

Context framing must:
- support the current path
- not override the SKU ladder
- not invent a recommendation
- not contradict prior qualification

Safe example:
- "Since most of your driving is in the city, many customers prefer the practical long-term option for everyday protection."

---

## 6. Phase-Safe Use of Education

Phase 7 education content may be used only when the phase architecture allows explanation.

Education must not appear too early.

Safe use:
- customer asks difference
- customer asks why
- customer asks whether something is worth it
- customer shows hesitation after options are already known

Unsafe use:
- before qualification completes
- instead of answering the current stage question
- as a long lecture during silence

---

## 7. Silence Phrase Standard

Silence phrases must do only one of these:
- normalize the pause
- reduce decision load
- invite one simple question

Silence phrases must not:
- reopen the whole sales pitch
- introduce front PPF too early
- create false urgency
- trigger discount thinking
- introduce technical overload

---

## 8. Ladder-Safe Language Standard

When moving down a ladder, phrases must preserve confidence.

Every down-ladder phrase should contain a reassurance fragment such as:
- still a strong option
- still gives solid long-term protection
- many customers choose it for daily use
- practical option without changing the care in installation
- balanced option for long-term ownership

Down-ladder phrases must never make the customer feel they are being moved into an inferior product.

---

## 9. Conversion-Safe Language Standard

Visit / booking / next-step phrases must:
- feel calm
- feel optional
- reduce risk
- not sound like pressure

Safe:
- "If you like, we can also keep the next step simple and arrange a quick visit."

Unsafe:
- "You should come now."
- "Book now before price changes."

---

## 10. Phrase Review Checklist

Before any phrase enters runtime, confirm:

- Would a normal customer understand this instantly?
- Can the customer answer without overthinking?
- Does it allow a realistic answer, including mixed answers if needed?
- Does it avoid sounding like one option is inferior?
- Does it avoid triggering front PPF too early?
- Does it stay inside the phase's job?
- Does it reduce confusion rather than increase it?
- Would this still sound natural on WhatsApp / Instagram chat?

If any answer is NO:
- phrase must not enter runtime

---

## 11. Current Priority Rule for PPF

For PPF-specific phrasing:
- full-body protection remains the main ladder path
- front PPF remains final fallback unless explicitly requested
- phrase wording must reinforce protection confidence, not scope downgrade
- affordability framing must not weaken trust in lower ladder options

---

## 12. Governance

This file governs phrase review only.
It does not override:
- SKU authority
- ladder logic
- qualification logic
- orchestration
- message assembly rules

Any phrase patch touching runtime customer-facing language should be reviewed against this file before commit.


## Silence Handling Standard

When a customer becomes silent during a conversation, the system must follow this recovery order:

1. Clarification opener first  
   - Invite the customer to ask what part needs clarification  
   - Reduce decision pressure

2. If clarification does not reopen the conversation, use a low-friction hook question  
   Examples:
   - car color
   - driving pattern
   - usage

3. Hook questions must connect naturally to the next guidance step using Phase 7 education snippets.

Example flow:

silence  
→ clarification opener  
→ hook question (if needed)  
→ contextual guidance  
→ decision narrowing

Important:
- Silence recovery must not introduce new product narrowing prematurely.
- It must not trigger front-PPF fallback early.
- The objective is to reopen the conversation naturally, not force a decision.




## CONVERSATION ARCHITECTURE RULES

Customer Type Awareness

All phrases and education snippets must support the following behavioral profiles:

- Researcher
- Price Anchor
- Visual Buyer
- Convenience Buyer

Conversation Trap Prevention

Phrase design must avoid:

- Over-education (excessive explanation)
- Early price anchoring before scope clarity
- Defensive brand positioning

Education Snippet Compression

Education snippets must represent **concepts**, not individual questions.

Example:

Correct:
EDU_PRICE_GAP

Incorrect:
EDU_PPF_PRICE
EDU_WRAP_PRICE
EDU_TINT_PRICE

Target limit:

Total Phase7 education snippets < 20
