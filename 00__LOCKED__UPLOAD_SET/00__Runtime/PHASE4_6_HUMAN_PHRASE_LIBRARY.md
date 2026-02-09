## PHASE 3A — QUALIFIER QUESTIONS (ONE QUESTION ONLY)
# LOCK_METADATA
# LOCK_STATUS: LOCKED
# LOCK_SCOPE: PHASE 3A — qualifier questions (IDs + bilingual phrasing)
# LOCK_DATE: 2026-02-09
# LOCK_REASON: Phase 3A UAT passed; phrase drift would break mapping
# CHANGE_CONTROL: Architecture approval required

### PHASE3A_Q_PPF_COVERAGE_INTENT
EN: For PPF, are you thinking full protection, front protection, or still deciding?
AR: للـ PPF، تفكر بحماية كاملة، حماية أمامية، أو لسه تقرر؟

### PHASE3A_Q_PAINT_CONDITION_REPAINT_SCRATCH
EN: Before we proceed, is there any repaint work or deep scratches on the panels?
AR: قبل لا نكمل، هل في رش/صبغ أو خدوش عميقة على القطع؟

### PHASE3A_Q_PPF_DRIVING_PATTERN
EN: Is your driving mostly highways/travel (stone chips), or mostly city (parking/contact)?
AR: استخدامك أكثر على الخطوط/سفر (ضربات حصى)، أو داخل المدينة (مواقف/احتكاك)؟

### PHASE3A_Q_PPF_COMPARISON_FOCUS
EN: When you compare, is it mainly about coverage, film quality, or headline price?
AR: لما تقارن، تركيزك أكثر على التغطية، جودة الفيلم، ولا السعر فقط؟

### PHASE3A_Q_CERAMIC_GOAL
EN: For ceramic, is your main goal easy cleaning and stable gloss long-term, or mainly to make it look fresh again?
AR: للسيراميك، هدفك تنظيف أسهل ولمعة ثابتة على المدى الطويل، أو بس تخليه يرجع شكله فريش؟

### PHASE3A_Q_CERAMIC_WASH_PATTERN
EN: How do you usually wash the car — normal bucket washing in the locality/public parking, automatic tunnel wash, waterless washing at malls, a professional washing center, or a mix?
AR: شلون عادة تغسل السيارة — غسيل عادي بالسطل في المنطقة/المواقف العامة، غسيل نفق/آلي، غسيل بدون ماء في المولات، مركز غسيل محترف، أو خليط؟

### PHASE3A_Q_TINT_GOAL
EN: For tint, is your main goal heat comfort, privacy, or both?
AR: للتظليل، هدفك الأساسي راحة من الحرارة، خصوصية، أو الاثنين؟

### PHASE3A_Q_TINT_COVERAGE
EN: For tint, do you want front only, sides and back, or full coverage?
AR: للتظليل، تبي الأمامي فقط، الجوانب والخلف، أو كامل؟

### PHASE3A_Q_WRAP_FINISH
EN: For wrap, which finish are you leaning toward — gloss, satin, or matte?
AR: للتغليف، أي لمسة تفضّل — لامع، ساتان، أو مطفي؟

### PHASE3A_Q_POLISHING_SCOPE
EN: For polishing, do you want exterior only, or a full detail that includes interior and engine bay?
AR: للتلميع، تبي الخارجي فقط، أو تلميع كامل يشمل الداخلي وغرفة المكينة؟

## PHASE 3B — TRANSITION TO PRICING (ACK)

### PHASE3B_CERAMIC_HAND_WASH
EN: Got it. I’ll line up the ceramic coating options and move to the pricing step next.
AR: تم. بجهّز لك خيارات السيراميك وبننتقل لخطوة التسعير بعدها.

### PHASE3B_CERAMIC_AUTO_WASH
EN: Got it. I’ll line up the ceramic coating options and move to the pricing step next.
AR: تم. بجهّز لك خيارات السيراميك وبننتقل لخطوة التسعير بعدها.

### PHASE3B_CERAMIC_WATERLESS
EN: Got it. I’ll line up the ceramic coating options and move to the pricing step next.
AR: تم. بجهّز لك خيارات السيراميك وبننتقل لخطوة التسعير بعدها.

### PHASE3B_CERAMIC_PRO_WASH
EN: Got it. I’ll line up the ceramic coating options and move to the pricing step next.
AR: تم. بجهّز لك خيارات السيراميك وبننتقل لخطوة التسعير بعدها.

### PHASE3B_PPF_CITY
EN: Got it. Based on your driving habits, I’ll line up the PPF options and move to pricing next.
AR: تم. بناءً على عادات قيادتك، بجهّز لك خيارات الـPPF وبننتقل للتسعير بعدها.

### PHASE3B_PPF_HIGHWAY
EN: Got it. Based on your driving habits, I’ll line up the PPF options and move to pricing next.
AR: تم. بناءً على عادات قيادتك، بجهّز لك خيارات الـPPF وبننتقل للتسعير بعدها.

────────────────────────────────────────────────────────────
PHASE 4 — BALANCED RESPONSE LIBRARY (POST-PRICE / POST-OPTIONS)
────────────────────────────────────────────────────────────

# ────────────────────────────────────────────────────────────
# PRODUCT METADATA AUTHORITY (HARD RULE)
# ────────────────────────────────────────────────────────────
#
# Human-facing phrases MUST NOT contain:
# - Product descriptions
# - Warranty explanations
# - Technical capability summaries
#
# All product facts (name, warranty, capability framing) are sourced from:
#   02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
#
# This file controls:
# - Tone
# - Flow
# - Question sequencing
# - Value framing
#
# Product metadata is injected at runtime via:
# - display_name
# - warranty_years
# - service_type
#
# SKU IDs must NEVER be exposed to customers.
# ────────────────────────────────────────────────────────────

Purpose:
- Control conversation momentum AFTER options or pricing
- Pre-empt silence, comparison, and hesitation
- Maintain authority without pressure
- Preserve customer dignity and trust

This section is PHRASES ONLY.
No logic. No routing. No signal emission.

────────────────────────────────────────────────────────────
4.1 AFTER-PRICE / AFTER-OPTION ANCHOR (REQUIRED)
────────────────────────────────────────────────────────────

EN:
"The difference here isn’t how it looks on day one — it’s how stable the protection stays over time with heat, washing, and daily use."

AR:
"الفرق هنا مو في الشكل من أول يوم — الفرق في ثبات الحماية مع الوقت، مع الحرارة والغسيل والاستخدام اليومي."

Rules:
- Use once immediately after price or options
- Do NOT repeat in price loops

────────────────────────────────────────────────────────────
4.2 WARRANTY REASSURANCE (NON-DEFENSIVE)
────────────────────────────────────────────────────────────

EN:
"The warranty period is about coverage, not that the product suddenly stops working after it ends — similar to how devices stay stable well beyond their warranty."

AR:
"مدة الضمان تخص التغطية، مو إن المنتج يوقف فجأة بعدها — مثل الأجهزة اللي تظل مستقرة حتى بعد انتهاء الضمان."

Use when:
- Warranty duration is mentioned
- Customer shows warranty fixation

────────────────────────────────────────────────────────────
4.3 OLD CAR GUIDANCE (7+ YEARS — PAINT-FIRST)
────────────────────────────────────────────────────────────

EN:
"For a car of this age, the main factor is paint condition rather than where it’s driven — that’s why we usually look at polishing or ceramic first."

AR:
"لهذا العمر من السيارات، العامل الأهم هو حالة الطلاء أكثر من طريقة الاستخدام — وعشان كذا غالباً نبدأ بالتلميع أو السيراميك."

Rules:
- Redirects away from default PPF
- Keeps recommendation respectful

────────────────────────────────────────────────────────────
4.4 PASSIVE INTEREST MODE (OK / HMM / I’LL THINK)
────────────────────────────────────────────────────────────

EN:
"No rush at all. Would it help if I summarize the option we discussed so it’s easy to come back to?"

AR:
"على راحتك. تحب ألخص لك الخيار اللي تكلمنا عنه عشان يكون سهل ترجع له؟"

Rules:
- Do NOT say “take your time”
- Invite ONE clear next step

────────────────────────────────────────────────────────────
4.5 PRICE PUSHY / JUST PRICE REQUEST
────────────────────────────────────────────────────────────

EN:
"I can give you a clean starting range, then fine-tune it once we lock the exact option — that way there are no surprises later."

AR:
"أقدر أعطيك نطاق مبدئي واضح، وبعدها نثبّت السعر بدقة حسب الخيار النهائي — بدون مفاجآت لاحقاً."

Rules:
- Allowed once
- Do NOT loop ranges

────────────────────────────────────────────────────────────
4.6 SILENT COMPARISON (PRE-EMPTIVE)
────────────────────────────────────────────────────────────

EN:
"Many owners compare a few places before deciding — what usually helps is looking at how the work holds up after a few months, not just the number."

AR:
"كثير من الناس يقارنون قبل ما يقررون — واللي يفرق فعلاً هو كيف يثبت الشغل بعد فترة، مو الرقم فقط."

Rules:
- Use BEFORE explicit competitor mention
- Never confrontational

────────────────────────────────────────────────────────────
4.7 TECHNICAL QUESTION REDIRECT (NON-CONFRONTATIONAL)
────────────────────────────────────────────────────────────

EN:
"Happy to explain — the practical difference shows more in real ownership than specs on paper."

AR:
"أكيد أشرح لك — الفرق الحقيقي يبان أكثر مع الاستخدام الفعلي، مو بالأرقام فقط."

────────────────────────────────────────────────────────────
4.8 MULTI-SERVICE JUMP REASSURANCE
────────────────────────────────────────────────────────────

EN:
"Noted — let’s lock this one first, and I’ll line up the other service right after."

AR:
"تمام — نثبت هذا الخيار أولاً، وبعدها أرتب لك الخدمة الثانية مباشرة."

────────────────────────────────────────────────────────────
4.9 PROOF / MEDIA REQUEST (PERMISSION-BASED)
────────────────────────────────────────────────────────────

EN:
"If you want, I can share a quick example of a similar car we’ve done — it usually makes the difference clearer."

AR:
"إذا حاب، أقدر أرسل لك مثال لسيارة مشابهة اشتغلنا عليها — غالباً يوضح الفرق أكثر."

Rules:
- Permission-based only
- ONE asset maximum

────────────────────────────────────────────────────────────
4.10 WHATSAPP CONTINUATION (OPTIONAL)
────────────────────────────────────────────────────────────

EN:
"If it’s easier, you can share your WhatsApp and I’ll send the summary there so it’s simple to come back to."

AR:
"إذا تحب يكون أسهل، تقدر تعطيني رقم واتسابك وأرسل لك الملخص هناك."

Rules:
- Convenience framing only
- Never forced

────────────────────────────────────────────────────────────
4.11 VISIT INVITATION (TRUST-BASED)
────────────────────────────────────────────────────────────

EN:
"If you’d rather see the place and process before deciding, you’re welcome to visit — no pressure."

AR:
"إذا تحب تشوف المكان وطريقة العمل بنفسك قبل القرار، أهلاً وسهلاً بأي وقت — بدون أي ضغط."

────────────────────────────────────────────────────────────
END — PHASE 4 BALANCED RESPONSE LIBRARY
────────────────────────────────────────────────────────────


# PHASE 4.6 — HUMAN PHRASE LIBRARY

Status: locked
Purpose: Approved customer-facing phrases only.
Scope:
- Phase 0–2 phrases must be short, neutral, and qualification-focused
- Max 1 question per phrase
- No pricing, negotiation, or persuasion

## PHASE 0–2 NOTE
Phrases below may have 2–3 micro-variants.
All variants are SEMANTICALLY EQUIVALENT and interchangeable.
No variant may add facts, persuasion, or new intent.


PHASE 4.6 — UPDATE LOCK

Locked additions:
- Section A — Service Inquiry
  • A1 Generic Service Inquiry
  • A4 Greeting + Service Context
  • A5 Non-Specific Automotive Inquiry

Guarantees:
- No pricing language
- No service recommendation
- No negotiation framing
- Phrase authority only

END — PHASE 4.6 UPDATE LOCK

GLOBAL RULES:
- No control / hook questions
- No booking or urgency language
- No tone adjectives (premium, best, amazing)
- No discounts or negotiation logic
- Simple spoken language only
- Each phrase must stand alone

Languages:
- EN (English)
- AR (Arabic)

---



## A. OPENING PHRASES
Purpose: Establish human presence and conversational safety at message start.

### Neutral Openings (Default)

- EN: Hello, happy to assist.
  AR: مرحباً، سعيد بمساعدتك.

- EN: Hi, thanks for reaching out.
  AR: أهلاً، شكراً لتواصلك معنا.

- EN: Hello, welcome.
  AR: مرحباً، أهلاً وسهلاً.

- EN: Hello.
  AR: مرحباً.

### Regional / Arabic Cultural Opening (Optional)

- EN: Peace be upon you.
  AR: السلام عليكم.

### Arabic Greeting Responses (Reply Usage)

- EN: And peace be upon you.
  AR: وعليكم السلام.

---

## A. SERVICE INQUIRY

Purpose:
Handle first-contact questions about services in a neutral, human way, and guide the conversation toward basic vehicle context without selling or pressure.

---

A1 — GENERIC SERVICE INQUIRY (UNKNOWN / BROAD)

EN:
We offer paint protection and appearance services like ceramic coating, PPF, tint, wrap, and paint correction.
Which car is this for, and what model year?

AR:
نقدم خدمات حماية ومظهر السيارة مثل السيراميك، الحماية الشفافة، التظليل، التغليف، وتصحيح الطلاء.
ما نوع السيارة، وما سنة الموديل؟

---

A2 — SERVICE LIST REQUEST (“what services do you offer?”)

EN:
We specialize in protecting and improving car paint and interiors.
Our services include ceramic coating, PPF, tint, wrap, and polishing.
Which car are you considering this for?

AR:
نحن متخصصون في حماية وتحسين طلاء ومقصورة السيارة.
تشمل خدماتنا السيراميك، الحماية الشفافة، التظليل، التغليف، والتلميع.
ما هي السيارة التي تفكر بها؟

---

A3 — SERVICE CONFIRMATION (“do you do ceramic / PPF / tint?”)

EN:
Yes, we do.
To guide you properly, what’s the car model and year?

AR:
نعم، متوفر.
حتى نقدر نرشح لك الخيار الأنسب، ما موديل السيارة وسنة الصنع؟

---

A4 — GREETING (NEUTRAL, NO QUALIFICATION) (“hi”, “hello”, “salam”)

### A4_GREETING_SERVICE_CONTEXT

- EN: Hello, welcome. We do PPF, ceramic coating, tint, wrap, and polishing. What’s the car model and year?
- AR: هلا ومرحباً. خدماتنا PPF، السيراميك، التظليل، التغليف، والتلميع. شنو موديل السيارة وأي سنة؟

---

### A6_REENTERED_CONTINUE

- EN: Welcome back. We can continue from where we stopped.
- AR: حياك الله من جديد. نكمل من حيث وقفنا.

---

A5 — NON-SPECIFIC AUTOMOTIVE INQUIRY (SAFE REDIRECT)

EN:
We focus on paint protection and appearance services.
If it’s about improving or protecting your car, let me know the model and year.

AR:
نحن نختص بخدمات حماية ومظهر السيارة.
إذا كان الموضوع يخص حماية أو تحسين شكل سيارتك، ما الموديل وسنة الصنع؟

## B. CONTEXT ACKNOWLEDGEMENT
Purpose: Confirm understanding and reduce friction without advancing the conversation.

- EN: I understand.
  AR: فهمت.

- EN: Got it.
  AR: تمام.

- EN: Understood, thanks for sharing.
  AR: واضح، شكراً لمشاركتك.

- EN: I understand what you’re looking for.
  AR: فهمت ما تبحث عنه.

- EN: Thanks for the details.
  AR: شكراً على التفاصيل.

- EN: Noted.
  AR: تم.

- EN: Yes, that makes sense.
  AR: نعم، هذا منطقي.

---



## C. GENERIC SERVICE EDUCATION
Purpose: Explain what the service category is and how to think about it, without selling or overwhelming.

### C.1 PPF EXPLANATION + QUALIFIER (PHASE 0–2)

EN:
Paint Protection Film (PPF) is like a screen protector for your car’s paint. It helps absorb everyday impacts like stone chips and light scratches, giving you peace of mind and helping the paint stay looking new for years. What’s the car model and year?

AR:
حماية PPF مثل سكرين بروتكتور لطلاء السيارة. تمتص ضربات الحصى والخدوش الخفيفة اليومية وتعطيك راحة بال وتساعد الطلاء يظل شكله جديد لسنين. شنو موديل السيارة وأي سنة؟

### C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)

EN:
Ceramic coating is like skincare for your car’s paint. It keeps the finish glossy, helps reduce wash marks over time, and makes the car easier to clean so it keeps looking fresh for years. To guide you correctly, what’s the car model and year?

AR:
السيراميك مثل العناية بالبشرة لطلاء السيارة. يحافظ على اللمعة، يقلّل آثار الغسيل مع الوقت، ويخلّي التنظيف أسهل عشان تظل السيارة شكلها فريش لسنين. عشان أوجّهك صح، شنو موديل السيارة وأي سنة؟

- EN: Ceramic coating involves proper paint preparation before application.
  AR: طلاء السيراميك يتضمن تجهيز الطلاء بشكل مناسب قبل التطبيق.

- EN: Ceramic coating protects the exterior paint, while interior ceramic focuses separately on interior surfaces.
  AR: طلاء السيراميك يختص بحماية الطلاء الخارجي، بينما السيراميك الداخلي يركّز بشكل منفصل على الأسطح الداخلية.

### INTERIOR CERAMIC — CORE ANCHOR (PRE-PRICE)

- EN: Interior ceramic is like a non-stick layer for the interior — everyday spills and dirt don’t stick easily, making cleaning much simpler.
  AR: السيراميك الداخلي يشبه طبقة مانعة للالتصاق داخل السيارة — الأوساخ والسوائل اليومية ما تمسك بسهولة، والتنظيف يصير أسهل.

### C.3 CERAMIC WASH PATTERN QUALIFIER (PHASE 0–2)

EN:
To guide this properly, how do you usually wash the car — bucket/hand wash, tunnel/automatic wash, mall waterless wash, or a mix?

AR:
عشان أوجّهك صح، شلون عادة تغسل السيارة — غسيل يدوي/سطل، غسيل نفق/آلي، غسيل بدون ماء في مواقف المولات، أو خليط؟

### TINT — CORE ANCHOR (PRE-PRICE)

- EN: Window tint is about sun protection for your family, not just making the glass dark.
  AR: تظليل الزجاج يركّز على حماية عائلتك من الشمس، مو بس تعتيم الزجاج.

- EN: Good tint reduces heat, glare, and harmful rays while keeping clear visibility inside the car.
  AR: التظليل الجيد يقلل الحرارة والوهج والأشعة الضارة مع الحفاظ على وضوح الرؤية داخل السيارة.

- EN: The difference is felt in daily comfort, not in how dark the windows look.
  AR: الفرق الحقيقي يبان في الراحة اليومية، مو في درجة التظليل فقط.

### TINT — COVERAGE FRAMING (EXPOSURE ZONES)

- EN: Some drivers focus protection on the front for eye comfort, others on the sides and back for privacy, and some prefer full coverage for balanced comfort all around.
  AR: بعض السائقين يفضّلون حماية الزجاج الأمامي لراحة العين، وآخرين الجوانب والخلفية للخصوصية، والبعض يختار تغطية كاملة لراحة متوازنة داخل السيارة.

### WRAP — CORE ANCHOR (PRE-PRICE)

- EN: Wrap is about presence — like someone who changes the room the moment they arrive, the car is noticed before it’s explained.
  AR: التغليف يتعلق بالحضور — مثل الشخص الذي يغيّر أجواء المكان عند دخوله، السيارة تُلاحظ قبل ما تحتاج شرح.

- EN: It’s a visual statement that gives the car a distinct character and stand-out appeal.
  AR: هو تعبير بصري يعطي السيارة شخصية واضحة وحضور لافت.

### WRAP — STYLE DIRECTION (FINISH SELECTION)

- EN: Some prefer a bold, clean gloss look, others go for a muted matte feel, and some choose satin for a balance in between.
  AR: البعض يفضّل اللمسة اللامعة الجريئة، والبعض يختار المظهر المطفي الهادئ، وآخرون يفضلون الساتان للتوازن بين الاثنين.

### POLISHING — CORE ANCHOR (PRE-PRICE)

- EN: Polishing is like a factory reset for the paint — it brings the finish and gloss back toward how it was meant to look.
  AR: التلميع يشبه إعادة ضبط المصنع للطلاء — يعيد اللمعة والمظهر أقرب لما كانت عليه السيارة في الأصل.

- EN: Different car care services exist for different goals.
  AR: توجد خدمات عناية مختلفة بالسيارات حسب الهدف.

- EN: Some focus on physical protection, others on ease of maintenance or appearance.
  AR: بعض الخدمات تركز على الحماية الفعلية، وأخرى على سهولة العناية أو الشكل.

- EN: There is no single option that suits everyone.
  AR: لا يوجد خيار واحد مناسب للجميع.

- EN: The right service depends on how the car is used and what matters most to you.
  AR: الخدمة المناسبة تعتمد على طريقة استخدام السيارة وما يهمك أكثر.

- EN: Some owners prioritize long-term protection, others prefer keeping the car looking fresh.
  AR: بعض المالكين يفضلون الحماية طويلة المدى، وآخرون يهتمون بالمظهر الدائم.

- EN: The idea is to choose based on your needs, not just the service name.
  AR: الفكرة هي الاختيار حسب احتياجك، وليس حسب اسم الخدمة فقط.

- EN: I can keep the explanation simple and clear.
  AR: أقدر أشرح لك الموضوع بشكل بسيط وواضح.

---



## D. GENERIC FACTUAL BENEFITS
Purpose: State objective benefits in a neutral, non-sales manner.

- EN: It helps reduce the impact of daily wear.
  AR: يساعد على تقليل تأثير الاستخدام اليومي.

- EN: It supports keeping the car in good condition over time.
  AR: يساعد في الحفاظ على السيارة بحالة جيدة مع الوقت.

- EN: It can make regular cleaning and maintenance easier.
  AR: قد يجعل التنظيف والصيانة أسهل.

- EN: It helps maintain the original look of the car.
  AR: يساعد في الحفاظ على الشكل الأصلي للسيارة.

- EN: It adds a layer of care suited for daily driving.
  AR: يضيف مستوى عناية مناسب للاستخدام اليومي.

- EN: Results depend on usage and how the car is handled.
  AR: النتائج تعتمد على طريقة الاستخدام والتعامل مع السيارة.

---



## E. GENERIC COMPARISON LANGUAGE
Purpose: Explain differences between options without ranking or pressure.

- EN: Different options focus on different outcomes.
  AR: الخيارات تختلف حسب النتيجة المطلوبة.

- EN: One option may focus more on protection, while another focuses on ease of care.
  AR: بعض الخيارات تركز أكثر على الحماية، وأخرى على سهولة العناية.

- EN: Some options cover more areas, others focus on specific parts.
  AR: بعض الخيارات تشمل مناطق أكثر، وأخرى تركز على أجزاء محددة.

- EN: The difference is usually in purpose, not quality.
  AR: الفرق غالباً يكون في الهدف، وليس في الجودة.

- EN: Each option suits a different type of usage.
  AR: كل خيار يناسب نوع استخدام مختلف.

- EN: Comparing options helps narrow down what fits you best.
  AR: المقارنة تساعد في تحديد ما يناسبك أكثر.

---

## F. PACKAGE & COVERAGE DIFFERENCES
Purpose: Clarify how packages and coverage vary without persuasion.

- EN: Packages mainly differ by coverage level.
  AR: الباقات تختلف بشكل أساسي في مستوى التغطية.

- EN: Some packages cover more areas, others focus on specific parts.
  AR: بعض الباقات تشمل مناطق أكثر، وأخرى تركز على أجزاء محددة.

- EN: Higher coverage usually means more time and materials.
  AR: التغطية الأعلى تعني عادة وقتاً ومواد أكثر.

- - EN: Essential packages focus on key areas.
  AR: الباقات الأساسية تركز على المناطق المهمة.

- EN: Each package is designed for a different type of usage.
  AR: كل باقة مصممة لنوع استخدام مختلف.

- EN: The difference is about scope, not quality.
  AR: الفرق يكون في النطاق، وليس في الجودة.

---

## G. COMMON CONCERNS (NORMALIZATION)
Purpose: Acknowledge hesitation and questions as normal and reasonable.

- EN: This is a common question.
  AR: هذا سؤال شائع.

- EN: Many customers ask about this.
  AR: كثير من العملاء يسألون عن هذا الموضوع.

- EN: It’s normal to compare options.
  AR: من الطبيعي مقارنة الخيارات.

- EN: It’s okay to take time before deciding.
  AR: من الطبيعي أخذ وقت قبل اتخاذ القرار.

- EN: Everyone looks for something different.
  AR: كل شخص يبحث عن شيء مختلف.

- EN: It depends on what feels right for you.
  AR: يعتمد على ما تشعر أنه مناسب لك.

---

## H. OBJECTION EXPLANATION LANGUAGE
Purpose: Explain common objections calmly without argument or pressure.

- EN: Pricing usually reflects the scope of work and materials involved.
  AR: السعر يعكس عادة نطاق العمل والمواد المستخدمة.

- EN: The value depends on how long you plan to keep the car.
  AR: القيمة تعتمد على مدة استخدامك للسيارة.

- EN: Different options are designed for different comfort levels.
  AR: الخيارات مصممة لمستويات راحة مختلفة.

- EN: Different customers prioritize different things — it’s about choosing what fits you best.
  AR: يختلف تركيز العملاء من شخص لآخر — الموضوع هو اختيار ما يناسبك أكثر.

- EN: It’s not about needing everything, but choosing what fits.
  AR: الموضوع ليس الحاجة لكل شيء، بل اختيار ما يناسبك.

- EN: Expectations and usage play a big role in deciding.
  AR: التوقعات وطريقة الاستخدام لها دور كبير في القرار.

### TINT — SPEC & BRAND CONFUSION (SAFE RESPONSE)

- EN: Darkness and percentages don’t always reflect protection — performance comes from the film technology itself.
  AR: درجة التعتيم أو النسب ما تعكس دائماً مستوى الحماية — الأداء الحقيقي يعتمد على تقنية الفيلم.

- EN: We keep one high heat-rejection standard, and only use specific brands like XPEL when a customer asks for it.
  AR: نعتمد معيار واحد عالي لعزل الحرارة، ونستخدم علامات مثل XPEL فقط إذا طلبها العميل.



## I. NEGOTIATION-SAFE VALUE FRAMING
Purpose: Frame value and options safely without offering discounts or pressure.

- EN: The idea is to choose what makes sense for you.
  AR: الفكرة هي اختيار ما يناسبك.

- EN: Value looks different for different people.
  AR: القيمة تختلف من شخص لآخر.

- EN: It’s about balancing what you want with how you use the car.
  AR: الموضوع هو الموازنة بين ما تريده وطريقة استخدامك للسيارة.

- EN: There’s no single right option for everyone.
  AR: لا يوجد خيار واحد صحيح للجميع.

- EN: The best choice is the one you’re comfortable with.
  AR: الخيار الأفضل هو الذي تشعر بالراحة معه.

- EN: We can keep things aligned with what matters most to you.
  AR: نقدر نخلي الأمور متوافقة مع ما يهمك أكثر.

---

## J. TRUST & CREDIBILITY STATEMENTS
Purpose: Build confidence through neutrality and industry-normal language.

- EN: We follow standard processes used in the industry.
  AR: نتبع إجراءات معتمدة ومستخدمة في المجال.

- EN: The focus is on doing things properly, not rushing.
  AR: التركيز يكون على التنفيذ الصحيح، وليس السرعة.

- EN: Each step is handled carefully.
  AR: يتم التعامل مع كل خطوة بعناية.

- EN: Clear communication is important to us.
  AR: التواصل الواضح مهم بالنسبة لنا.

- EN: We prefer to keep expectations clear from the start.
  AR: نحرص على وضوح التوقعات من البداية.

- EN: You can ask anything if you need clarity.
  AR: تقدر تسأل عن أي شيء إذا احتجت توضيح.

---

## K. PRICE CONTEXT (NO NUMBERS)

Purpose: Prepare the customer for pricing discussion without quoting, anchoring, or pressure.

- EN: Pricing usually depends on the scope of work and materials involved.
  AR: عادةً يعتمد السعر على نطاق العمل والمواد المستخدمة.

- EN: Different options come with different levels of coverage and effort.
  AR: تختلف الخيارات حسب مستوى التغطية والجهد المبذول.

- EN: The right option is more about fit than just cost.
  AR: الخيار المناسب يعتمد على التوافق أكثر من السعر فقط.

- EN: Some setups focus on essential areas, others include more comprehensive coverage.
  AR: بعض الباقات تركز على الأساسيات، وأخرى تشمل تغطية أوسع.

- EN: The idea is to match the option to how you use the car.
  AR: الفكرة هي اختيار ما يناسب طريقة استخدامك للسيارة.

- EN: Once we understand what matters most to you, pricing becomes clearer.
  AR: عندما نفهم ما يهمك أكثر، تصبح الصورة أوضح من ناحية السعر.

- EN: We can go through the details step by step when you’re ready.
  AR: يمكننا مراجعة التفاصيل خطوة بخطوة عندما تكون جاهزًا.

### TINT — PRICE CONTEXT (NO NUMBERS)

- EN: Tint pricing mainly depends on the coverage area and the film type used, not just darkness.
  AR: سعر التظليل يعتمد بشكل أساسي على مساحة التغطية ونوع الفيلم، وليس فقط على درجة التعتيم.

### WRAP — PRICE CONTEXT (NO NUMBERS)

- EN: Wrap pricing mainly depends on the finish choice and the amount of coverage needed.
  AR: سعر التغليف يعتمد بشكل أساسي على نوع اللمسة المختارة ومساحة التغطية المطلوبة.

---

# ------------------------------------------------------------
# PHASE 4.6 — PRE-PRICE & OPTION FRAMING (NO PRICES)
# ------------------------------------------------------------

## PRE-PRICE REASSURANCE BRIDGE (VALUE ALIGNMENT)
Purpose:
- Summarize customer signals
- Reassure fit BEFORE pricing
- Reduce sticker shock

EN:
Based on how you use and care for the car, this is the option that usually makes the most sense.
That way, when we look at pricing, it feels logical rather than surprising.

AR:
بناءً على طريقة استخدامك والعناية بالسيارة، هذا الخيار غالباً هو الأنسب.
علشان كذا لما نشوف السعر يكون منطقي ومفهوم.

---

## OPTION SELECTION LOGIC (WHY YOU’RE SEEING THESE)
Purpose:
- Explain option appearance
- Avoid feature comparison
- Maintain authority

EN:
I’m showing you these two options because they’re the most suitable for this type of car and usage.
We can narrow further once you see which direction feels right.

AR:
أعرض لك هالخيارين لأنهم الأنسب لهذا النوع من السيارات وطريقة الاستخدام.
وبعدها نقدر نضيّق الاختيار حسب اللي يناسبك أكثر.

---

## ANALOGY REINFORCEMENT (SHORT VARIANTS)
Purpose:
- Reinforce understanding
- Use only when helpful

PPF — EN:
Think of PPF like a screen protector — it’s about peace of mind against everyday impacts.

PPF — AR:
الـPPF مثل واقي الشاشة — راحة بال ضد الضربات اليومية.

CERAMIC — EN:
Ceramic is more like skincare — it keeps the paint healthy and looking fresh over time.

CERAMIC — AR:
السيراميك مثل العناية بالبشرة — يحافظ على الطلاء نظيف ولمّاع مع الوقت.

---

## SOFT VISIT / INSPECTION / CONTINUATION INVITE
Purpose:
- Offer next step without pressure
- Use when scope or confidence needs support

### Z_DEPRECATED__VISIT_SUGGESTION_LINE (DO NOT USE IN PHASE 0–2)
DEPRECATED.
Reason:
- Visit / inspection suggestions belong to Phase 4 (pre-price / decision support).
- This line must never be selected during Phase 0–2.

EN: If you’d like, we can also do a quick visit or inspection so everything is clear before moving ahead.
AR: وإذا حاب، نقدر نسوي زيارة أو فحص بسيط علشان يكون كل شيء واضح قبل ما نكمل.

---

## L. NEUTRAL TRANSITION STATEMENTS

Purpose: Smoothly conclude explanation and prepare the conversation for a natural next step without prompting, pressure, or hooks.

### L.0 BROWSING SAFE PRIMER (ONE QUESTION — SERVICE-ANCHORED) (AUTHORITATIVE)

Usage rule:
- Used ONLY when request_type = BROWSING_GENERIC
- Used ONLY when no vehicle details are present
- MUST include exactly 1 soft question (not vehicle qualification)
- MUST NOT mention prices
- MUST NOT suggest a specific service
- MUST NOT trigger qualification

EN: No problem at all. We do PPF, ceramic coating, tint, wrap, and polishing. Which one are you mainly looking at?
AR: ما في مشكلة. خدماتنا PPF، السيراميك، التظليل، التغليف، والتلميع. أي خدمة في بالك أكثر؟

### SERVICE LIST — PHASE 0–2
- EN: We can help with PPF, ceramic, tint, wrap, and polishing. What’s the car model and year?
- AR: نقدر نخدمك في PPF، سيراميك، تظليل، تغليف، وتلميع. شنو موديل السيارة وأي سنة؟

- EN_ALT: Our services include PPF, ceramic coating, tinting, wrapping, and polishing. What’s the car model and year?
- AR_ALT: خدماتنا تشمل PPF، سيراميك، تظليل، تغليف، وتلميع. شنو موديل السيارة وأي سنة؟

### SERVICE CONFIRMED — PHASE 0–2
- EN: Yes, we do that. What’s the car model and year?
- AR: نعم نقدر نخدمك. شنو موديل السيارة وأي سنة؟

- EN_ALT: Sure. Can you share the car model and year?
- AR_ALT: أكيد. تقدر تعطيني موديل السيارة وأي سنة؟

### DRIVING PATTERN QUALIFIER — PHASE 0–2 (VEHICLE KNOWN)
- EN: Do you mostly drive in the city, or do you often travel long distances on highways?
- AR: استخدامك أغلبه داخل المدينة، ولا تسافر كثير على الخطوط السريعة؟

- EN_ALT: Is your driving mainly city use, or more highway trips?
- AR_ALT: قيادتك أكثر داخل المدينة ولا على الخطوط السريعة؟

### PRICE REQUEST HOLD — PHASE 0–2
- EN: Pricing depends on the car and coverage. What’s the car model and year?
- AR: السعر يعتمد على السيارة والتغطية. شنو موديل السيارة وأي سنة؟

- EN_ALT: To guide you properly on pricing, I just need the car model and year.
- AR_ALT: عشان أوجهك صح بالسعر، أحتاج موديل السيارة وأي سنة؟

### COMPARISON — PHASE 0–2 (VEHICLE KNOWN)
- EN: I can explain it simply: PPF protects against chips and scratches, while ceramic is mainly for gloss and easier washing. Which one do you want to go with?
- AR: أشرحها لك ببساطة: الـPPF يحمي من ضربات الحصى والخدوش، والسيراميك للّمعان وسهولة الغسيل. شنو تحب تختار؟

- EN_ALT: In short, PPF is for protection, ceramic is more about shine and easy cleaning. Which option would you prefer?
- AR_ALT: باختصار، الـPPF للحماية، والسيراميك للّمعان وسهولة التنظيف. أي خيار تفضل؟

### BRAND DISCLOSURE — PHASE 0–2 (APPROVED)
- EN: Yes, we work with approved PPF brands like XPEL and Global Hi-Tech Films. What’s the car model and year?
- AR: نعم، نركّب علامات PPF المعتمدة مثل XPEL وGlobal Hi-Tech Films. شنو موديل السيارة وأي سنة؟

### COMPETITOR CHEAPER — PHASE 0–2
- EN: Understood. To compare properly, what’s the car model and year?
- AR: مفهوم. عشان نقدر نقارن بشكل صحيح، شنو موديل السيارة وأي سنة؟

### TECHNICAL QUESTION HOLD — PHASE 0–2
- EN: I can explain it clearly once I know the car details. What’s the car model and year?
- AR: أقدر أشرح لك بشكل واضح بعد ما أعرف تفاصيل السيارة. شنو موديل السيارة وأي سنة؟

### POST-SERVICE / OFF-SCOPE — PHASE 0–2
- EN: Noted — the concerned team will respond to you.
- AR: تم — الفريق المختص بيرد عليك.

### L.3X COMPARISON HOLD (PHASE 0–2)
- EN: I can explain it simply: PPF protects against chips and scratches, while ceramic is mainly gloss and easier washing. Which one do you want to go with?
- AR: أشرحها لك ببساطة: الـPPF يحمي من ضربات الحصى والخدوش، والسيراميك للّمعان وسهولة الغسيل. شنو تحب تختار؟

### BRAND DISCLOSURE — PPF (PHASE 0–2)
- EN: Yes, we work with approved PPF brands like XPEL and Global Hi-Tech Films. What’s the car model and year?
- AR: نعم، نركّب علامات PPF المعتمدة مثل XPEL وGlobal Hi-Tech Films. شنو موديل السيارة وأي سنة؟

### OFFSCOPE — NON-AUTOMOTIVE (PHASE 0–2)
- EN: Thanks — I’ll forward this to the concerned team and they will get back to you.
- AR: شكرًا — بحوّل الموضوع للفريق المختص وراح يرجعون لك.

### POST-SERVICE SUPPORT (PHASE 0–2)
- EN: Sure — I’ll forward this to the team to assist you.
- AR: أكيد — بحوّل طلبك للفريق عشان يساعدونك.

### MULTI_SERVICE_INTENT_SAFE (PHASE 0–2)
EN: Got it — you’re looking at more than one service. What’s the car model and year?
AR: تمام — واضح إنك تفكر بأكثر من خدمة. شنو موديل السيارة وأي سنة؟
EN_ALT: Got it — you’re looking at more than one service. Which service should we start with first?
AR_ALT: تمام — واضح إنك تفكر بأكثر من خدمة. أي خدمة نبدأ فيها أول؟

### LONG_RAMBLING_GROUNDING (PHASE 0–2)
EN: I know it can feel confusing — I can help. What’s the car model and year?
AR: أفهم إن الموضوع ممكن يكون محيّر — أقدر أساعدك. شنو موديل السيارة وأي سنة؟

### L.2 BROWSING_GENERIC — SERVICE OVERVIEW (NO BULLETS)

- EN: We do Ceramic Coating, PPF (paint protection film), Window Tint, and Wrapping. If you tell me your car model and year, I’ll guide you to the right option.
  AR: خدماتنا تشمل سيراميك، PPF (حماية الطلاء)، تظليل، وتغليف. إذا تعطيني موديل السيارة وسنة الصنع أقدر أرشدك للخيار المناسب.

### Z_DEPRECATED__L.1_QUALIFICATION_CLARIFIERS__LEGACY_BLOCK (DO NOT USE)
DEPRECATED — kept for history only.
Reason:
- Prevent duplicate selector targets in runtime.
- Authoritative L.1 (V1/V2/V3) is defined below.

- EN: What’s the car model and year?
  AR: شنو موديل السيارة وسنة الصنع؟
- EN: That gives a general idea of how things work.
  AR: هذا يعطي فكرة عامة عن كيفية سير الأمور.

- EN: This should help clarify the overall picture.
  AR: هذا يساعد في توضيح الصورة بشكل عام.

- EN: I wanted to explain it clearly before moving ahead.
  AR: أردت توضيح الأمر بشكل واضح قبل المتابعة.

- EN: Now that you have the context, we can take it step by step.
  AR: الآن بعد أن أصبحت الصورة أوضح، يمكننا المتابعة خطوة بخطوة.

- EN: There’s no rush — we can continue whenever you’re comfortable.
  AR: لا يوجد أي استعجال — يمكننا المتابعة عندما تشعر بالراحة.

- EN: Let me know how you’d like to proceed.
  AR: أخبرني كيف تفضل المتابعة.

- EN: We can explore this further based on what matters most to you.
  AR: يمكننا التعمق أكثر بناءً على ما يهمك أكثر.

  ### L.3 SERVICE CONTEXT CLARIFIER (ONE QUESTION)

- EN: Just to confirm — do you want to switch services now, or should we stay on the current one?
  AR: بس للتأكيد — تبي نغيّر الخدمة الحين، ولا نكمل على نفس الخدمة؟

---
---

---

### Z_DEPRECATED__L0_BROWSING_SAFE_PRIMER__SERVICE_ANCHORED (DO NOT USE)
DEPRECATED — duplicate selector risk.
Reason:
- Phase 1–2 browsing is enforced by Assembly Map to use ONLY: "L.0 BROWSING SAFE PRIMER (ONE QUESTION)".
This block is retained for history only.

Usage rule (LOCKED):
- Applies when request_type == BROWSING_GENERIC AND service_intent == unknown
- MUST be business-specific (mention services)
- MUST ask exactly ONE minimal car question (model + year in one sentence)
- MUST NOT ask “what’s available”, “inventory”, or anything that sounds like car sales
- MUST NOT give pricing, durations, or brand pushing

- EN: [DEPRECATED — DO NOT ROUTE IN PHASE 0–2]
- AR: ما في مشكلة. نشتغل على PPF، السيراميك، التظليل، التغليف، والتلميع. شنو السيارة وأي سنة موديل؟

---

### Z_DEPRECATED__L0_BROWSING_SAFE_PRIMER__ALT (DO NOT USE)
DEPRECATED — duplicate selector risk. Retained for history only.

- EN: [DEPRECATED — DO NOT ROUTE IN PHASE 0–2]
- AR: [محذوف — لا يستخدم]

---

### L.1 QUALIFICATION CLARIFIERS (VEHICLE DETAILS) — V1/V2/V3 (AUTHORITATIVE)
AUTHORITATIVE — this is the ONLY selectable L.1 block.
Reason:
- Assembly Map requires the single-question variant (V1/V2/V3) based on missing_info_ask_count.

Usage rule:
- Used ONLY when qualification_state = NOT_READY
- Used ONLY when missing_fields includes vehicle_model or vehicle_year
- Must be 1 question only
- Use variant by missing_info_ask_count:
  - 1 = V1
  - 2 = V2
  - 3 = V3 (final attempt)

EN (V1): To guide you correctly, what’s the car model and year?
AR (V1): عشان أوجهك صح، شنو موديل السيارة وأي سنة؟

EN (V2): Quick check — what’s the car model and year?
AR (V2): سؤال سريع — شنو موديل السيارة وأي سنة؟

EN (V3): Last detail I need: car model and year?
AR (V3): آخر معلومة أحتاجها: موديل السيارة وأي سنة؟

EN: What’s the exact car model?
AR: شنو موديل السيارة بالضبط؟

EN: What’s the model year?
AR: شنو سنة الموديل؟

---


## L.2. BROWSING_GENERIC — SERVICE OVERVIEW (NO BULLETS)

Usage rule:
- Used ONLY when request_type = BROWSING_GENERIC
- Used ONLY when vehicle_model/year is missing
- Must be short (overview + 1 question comes from L.1)

EN:
We do:
Ceramic coating
Paint protection film (PPF)
Window tint
Polishing / paint correction
Interior detailing

AR:
خدماتنا:
سيراميك
حماية PPF
تظليل
تلميع / تصحيح طلاء
تنظيف وحماية داخلي
---

## SERVICE MODULE TEMPLATE
Service Name: [SERVICE_NAME]

### 1. What This Service Is
[PLACEHOLDER — SERVICE DEFINITION PHRASES]

### 2. What Problem It Solves
[PLACEHOLDER — PROBLEM-SOLUTION PHRASES]

### 3. Typical Use Cases
[PLACEHOLDER — USE CASE PHRASES]

### 4. How It Differs From Other Services
[PLACEHOLDER — SERVICE DIFFERENCE PHRASES]

---

## SERVICE MODULE — [SERVICE_NAME_1]
[USE TEMPLATE ABOVE]

---

## SERVICE MODULE — [SERVICE_NAME_2]
[USE TEMPLATE ABOVE]

---

# BRAND & WARRANTY SUPPORT BLOCKS
Rule: These blocks are referenced by services, not duplicated.

---

## BRAND CREDIBILITY PHRASES
Purpose: Express brand reliability without marketing language.

[PLACEHOLDER — BRAND CREDIBILITY PHRASES]

---

## WARRANTY EXPLANATION PHRASES
Purpose: Explain warranty scope and intent in simple terms.

[PLACEHOLDER — WARRANTY EXPLANATION PHRASES]

---

# HARD CONSTRAINTS
- Phase 4.6 does NOT decide when phrases are used
- Phase 4.6 does NOT include hooks or next-step questions
- Phase 4.6 does NOT contain tone strength or escalation logic
- Phase 4.6 is a phrase source only

---

# LOCK BLOCK (APPLY AFTER CONTENT FILLING OR STRUCTURE APPROVAL)

Lock Status: PENDING
Phase: 4.6
Name: Human Phrase Library
Status: LOCKED (wording authority)

Dependencies:
- Phase 4.5 Tone Engine
- Phase 4.7 Hook Engine
- Phase 4.8 Message Assembly Map