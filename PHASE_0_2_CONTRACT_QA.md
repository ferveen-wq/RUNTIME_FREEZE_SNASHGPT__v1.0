# PHASE 0–2 CONTRACT — Q&A FORMAT
VERSION: 1.1
STATUS: DRAFT → LOCK AFTER PRO AUDIT
SCOPE: INTAKE → INTERPRETATION → ROUTING → OUTPUT (ONLY)

==================================================
SECTION 1 — WHAT IS PHASE 0–2?
==================================================

Q: What is Phase 0–2 responsible for?
A:
Phase 0–2 is the SINGLE INTAKE + ROUTING KERNEL for SNASHGPT.
It accepts ANY inbound content and converts it into a stable structured state,
then decides ONE next action.

Key outputs:
- customer_stage
- service_intent
- vehicle_identity
- constraints
- tone_profile (metadata)
- allowed_routes
- next_action

---

Q: What is Phase 0–2 NOT responsible for?
A:
Phase 0–2 must NOT:
- price, discount, negotiate
- deep educate
- competitor comparisons
- objection resolution
- closing
- persuasion

These belong to Phase 3+ and must be gated via allowed_routes.

PROS:
- prevents patch loops
- keeps later phases modular
CONS:
- less “smart” upfront
RECOMMENDATION:
Stability first. Intelligence later.

==================================================
SECTION 2 — ENVIRONMENTS (UAT vs PRODUCTION)
==================================================

Q: How does Phase 0–2 support two environments?
A:
We operate:
1) UAT / Project Runtime (testing): may include logs, debug artifacts, extra files.
2) Production / GPT Runtime: minimal (<15 files), stable, no test contamination.

Rule:
Behavior must be IDENTICAL.
File shape may differ (bundling), but decisions and outputs must match.

Phase 0–2 MUST identify test-only artifacts and prevent them overriding production logic.

==================================================
SECTION 3 — INPUTS (WHAT PHASE 0–2 MUST ACCEPT)
==================================================

Q: What kinds of inputs are accepted?
A:
ALL:
- new customer message
- mid-chat message
- returning customer message
- post-silence message
- objections
- unrelated questions
- assistant pasted notes
- long transcripts
- screenshots (OCR text)
- cross-channel chats (WhatsApp/Instagram/etc)
- voice notes (as transcribed text)

Q: How are voice notes handled?
A:
Transcription occurs upstream.
Phase 0–2 receives text + optional metadata.
Voice is treated as normal chat; ignore filler words.

==================================================
SECTION 4 — CORE PROCESS (INTAKE → INTERPRETATION → OUTPUT)
==================================================

Q: What is the first step?
A:
Normalize the input into signals:
- service_hint
- vehicle_hint
- off_scope_hint
- post_service_support_hint
- competitor/brand_hint
- transcript/multi-speaker flags
- confidence score

No customer-facing output yet.

Q: What is the last step?
A:
Choose EXACTLY ONE next_action:
- ASK_ONE_CLARIFIER
- ROUTE_TO_ENGINE
- SUPPRESS_RESPONSE

And provide allowed_routes for downstream gating.

==================================================
SECTION 5 — QUESTIONS & MINIMUM BACK-AND-FORTH
==================================================

Q: How many questions can Phase 0–2 ask?
A:
Maximum 1 question per turn.

Q: When is a question allowed?
A:
Only when routing cannot be legally done without one missing piece.

Q: What if the customer gives full details in one long first message?
A:
Extract all known info, tag any extra intents (brand/competitor/etc),
set qualification complete, then ROUTE. Do not debate or educate in Phase 0–2.

==================================================
SECTION 6 — VEHICLE HANDLING (AMBIGUITY & REPO-MISSING)
==================================================

Q: Where does vehicle resolution come from?
A:
Only from Vehicle Repository + alias rules.
No guessing.

Vehicle states:
- resolved
- ambiguous
- repo_missing
- unknown

Q: If ambiguous (e.g., x90), what happens?
A:
Ask ONE clarifier that disambiguates brand/model.
Suppress all other output.

EN:
"Just to confirm, is it Volvo XC90 or Jetour X90?"
AR:
"للتأكيد فقط، هل تقصد فولفو XC90 أو جيتور X90؟"

Rule:
Preserve service_intent if already known.

Q: If repo_missing, what happens?
A:
Set constraint vehicle_repo_missing=true.
Ask ONE clarifier (brand or photo).
Suppress other blocks.

EN:
"I couldn’t find this model in our list yet. Could you share the brand or a photo?"
AR:
"الموديل غير موجود حالياً عندنا. ممكن تشاركنا اسم الشركة أو صورة للسيارة؟"

Q: What about alias collisions and close matches?
A:
Always treat as ambiguous.
Never auto-pick if more than one plausible match.
Ask the smallest clarifying question.

Loop Prevention:
When VR override triggers:
- do NOT populate missing_fields in that turn
- do NOT ask model/year again
- do NOT overwrite active_service_context

==================================================
SECTION 7 — SERVICE HANDLING & CLOSEST MATCH (NO INVENTION)
==================================================

Q: Where do services come from?
A:
Only from the Master Service Canon / Service Canon Bundle.

Q: If a customer asks for unsupported services (AC repair, mechanical, painting)?
A:
Do NOT promise.
Either:
- redirect to the closest supported service category
- or politely state out-of-scope

Examples:
AC repair redirect:
EN: "We don’t handle mechanical AC repairs, but we do offer heat-rejection solutions like tint and ceramic that help reduce cabin heat."
AR: "ما نقدم صيانة ميكانيكية للمكيف، لكن نوفر حلول تقليل الحرارة مثل العازل الحراري والسيراميك."

Painting redirect:
EN: "We don’t repaint cars, but polishing and correction can restore paint very close to new."
AR: "ما نقوم بإعادة دهان، لكن التلميع ومعالجة الطلاء ترجع المظهر قريب جداً للجديد."

Rule:
Approximation must map to supported services without inventing capabilities.

==================================================
SECTION 8 — BRAND / COMPETITOR / HEARSAY IN FIRST MESSAGE
==================================================

Q: What if the customer mentions a competitor, says cheaper elsewhere, or asks brand comparisons?
A:
Phase 0–2 must:
- acknowledge calmly
- tag intent (comparison_pressure / brand_curiosity)
- ROUTE downstream
It must NOT debate or educate.

EN: "Got it, thanks for sharing. Let me first understand your car and needs so I can guide you properly."
AR: "تمام، شكراً للتوضيح. خلينا أولاً نفهم سيارتك واحتياجك عشان أقدر أساعدك بشكل أدق."

==================================================
SECTION 9 — POST-SERVICE SUPPORT REQUESTS (INVOICE / COMPLAINT / VIDEO / MAINTENANCE)
==================================================

Q: If the customer asks for invoice, complaint, video footage, maintenance, bill?
A:
Phase 0–2 must detect post_service_support intent and route to support/escalation.

Rules:
- do NOT re-qualify
- do NOT ask vehicle/service again if already known
- acknowledge only; no promises beyond routing

Phase 0–2 must ensure Human Phrase Library contains proper acknowledgement blocks.

==================================================
SECTION 10 — TRANSCRIPTS, WRONG PASTES, CROSS-CHANNEL STITCHING
==================================================

Q: Can assistants paste long histories or screenshots?
A:
Yes. Phase 0–2 must accept them.

Behavior:
- stitch into chronological order when timestamps exist
- detect multi-speaker transcript
- extract latest actionable customer intent
- do not respond line-by-line
- do not overwrite state from unrelated pasted content

Q: What if assistant pastes another customer’s transcript into wrong window?
A:
Phase 0–2 must:
- detect mismatch signals
- suppress qualification
- ask ONE neutral clarification
- do not overwrite this customer’s state

Q: How does timestamp normalization work?
A:
Priority:
1) explicit transcript timestamps
2) screenshot timestamps
3) paste time (flag uncertainty internally)

Customer never sees these rules.

==================================================
SECTION 11 — TONE GOVERNANCE (METADATA ONLY)
==================================================

Q: Do we fix tone here?
A:
Yes, but via metadata only (no sentence writing).

Tone rules:
- no emojis
- no negative framing
- no bot-like wording
- simple language (especially AR)

If a phrase violates tone:
- suppress it via Assembly Map
- do not rewrite it here

==================================================
SECTION 12 — TITLING RULES (ADMIN ONLY)
==================================================

Q: When do we title the chat?
A:
Only once qualification is complete:
- vehicle resolved
- service resolved
- confidence threshold met

Rules:
- title created ONCE
- never overwritten by later phases
- used for admin clarity only

==================================================
SECTION 13 — OUTPUT RULES (CUSTOMER FACING)
==================================================

Q: What can Phase 0–2 output?
A:
ONLY ONE of:
- one clarifying question
- one neutral acknowledgment + route
- one polite redirect
- suppress response (spam/unsafe)

Must include required timestamp format per global template.

Q: What must never be output here?
A:
- prices, discounts, negotiation
- deep education blocks
- competitor debate
- multiple questions
- emojis
- aggressive sales pressure

==================================================
SECTION 14 — INTERNAL OUTPUT (NON-CUSTOMER)
==================================================

Phase 0–2 must output internally:
- customer_stage
- service_intent
- vehicle_identity
- constraints
- allowed_routes
- next_action
- tone_profile
- profile_signals (passive only)

Not shown to customer.

==================================================
SECTION 15 — FREEZE CONDITIONS
==================================================

Phase 0–2 can be LOCKED only if:
- coverage for all scenarios above is confirmed
- no duplicate authority conflicts remain
- VR ambiguity/repo-missing loop prevention verified
- post_service_support routing verified
- transcript/wrong-paste normalization verified
- titling logic verified and unique
- tone violations are suppressed
- production pack can be reduced safely (<15 files) without behavior change

END OF CONTRACT
