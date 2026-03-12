# PHASE 8 — VISUAL INTELLIGENCE MAP

Purpose:
Defines how videos and visual assets are selected and triggered during SNASHGPT conversations.

Visual assets provide:
- Proof of service performance
- Installation transparency
- Result visualization
- Customer trust
- Brand credibility
- Objection handling

This document ensures that the visual system can grow over time without changing the architecture.


------------------------------------------------------------
SECTION 1 — VISUAL ROUTING ENGINE
------------------------------------------------------------

The Visual Router selects the most relevant video based on conversation context.

Context signals used by the router:

- Customer car model
- Vehicle segment (SUV / Sedan / Luxury)
- Vehicle color
- Service requested
- Customer question type
- Conversation phase
- Customer concern

Example logic:

INPUT
car_model = Land Cruiser
color = white
service = PPF

ROUTER SELECTION ORDER

1. Exact model + color video
2. Same model video
3. Same segment video
4. Same color vehicle video
5. Generic service video

Example output:

VIDEO_RESULT_LC_WHITE
VIDEO_RESULT_WHITE_SUV
VIDEO_RESULT_GENERIC_PPF


------------------------------------------------------------
SECTION 2 — VIDEO CATEGORY STRUCTURE
------------------------------------------------------------

Videos are organized into the following scalable categories.


SERVICE_EXPLANATION

Explains what each service does.

Examples:

VIDEO_SERVICE_PPF_EXPLAINED
VIDEO_SERVICE_CERAMIC_EXPLAINED
VIDEO_SERVICE_POLISH_EXPLAINED
VIDEO_SERVICE_TINT_EXPLAINED
VIDEO_SERVICE_WRAP_EXPLAINED



PROOF_TESTS

Demonstrates service performance.

Examples:

VIDEO_PROOF_PPF_SELF_HEAL
VIDEO_PROOF_STONE_IMPACT_TEST
VIDEO_PROOF_CERAMIC_HYDROPHOBIC
VIDEO_PROOF_TINT_HEAT_REJECTION



INSTALLATION_PROCESS

Shows how services are professionally installed.

Examples:

VIDEO_INSTALL_PPF_PROCESS
VIDEO_INSTALL_CERAMIC_PROCESS
VIDEO_INSTALL_POLISH_PROCESS
VIDEO_INSTALL_TINT_PROCESS



RESULT_SHOWCASE

Displays final results on customer vehicles.

Examples:

VIDEO_RESULT_SUV_BLACK_CERAMIC
VIDEO_RESULT_WHITE_SUV_PPF
VIDEO_RESULT_LUXURY_POLISH



CUSTOMER_TESTIMONIALS

Real customer experiences and feedback.

Examples:

VIDEO_TESTIMONIAL_PPF_CUSTOMER
VIDEO_TESTIMONIAL_CERAMIC_CUSTOMER
VIDEO_TESTIMONIAL_TINT_CUSTOMER



BRAND_CREDIBILITY

Explains manufacturer credibility and technology.

Examples:

VIDEO_BRAND_XPEL_TECHNOLOGY
VIDEO_BRAND_GLOBAL_FILM_OVERVIEW
VIDEO_BRAND_MANUFACTURER_HISTORY



MAINTENANCE_EDUCATION

Explains post-installation care.

Examples:

VIDEO_MAINTENANCE_PPF_GUIDE
VIDEO_MAINTENANCE_CERAMIC_GUIDE
VIDEO_MAINTENANCE_TINT_CARE
VIDEO_MAINTENANCE_POLISH_AFTERCARE



LONG_TERM_REALITY

Shows long-term service performance.

Examples:

VIDEO_LONGTERM_PPF_AGING
VIDEO_LONGTERM_CERAMIC_WEAR
VIDEO_LONGTERM_TINT_DURABILITY



CUSTOMER_MISTAKE_PREVENTION

Educates customers about poor quality services.

Examples:

VIDEO_MISTAKE_CHEAP_PPF_FAILURE
VIDEO_MISTAKE_BAD_TINT_INSTALL
VIDEO_MISTAKE_WRONG_CERAMIC_CARE
VIDEO_MISTAKE_OVERPOLISH_DAMAGE



BOOKING_CONFIDENCE

Builds trust before installation.

Examples:

VIDEO_SHOP_TOUR
VIDEO_INSTALLATION_FACILITY
VIDEO_TEAM_EXPERTISE
VIDEO_DAY_OF_INSTALLATION_PROCESS



------------------------------------------------------------
SECTION 3 — TECHNICAL QUESTION VIDEOS
------------------------------------------------------------

These videos answer common technical questions.

Examples:

VIDEO_TECH_PPF_THICKNESS_EXPLAINED
VIDEO_TECH_PPF_SELF_HEALING_LAYER
VIDEO_TECH_PPF_PRECUT_VS_MANUAL
VIDEO_TECH_CERAMIC_LAYER_STRUCTURE
VIDEO_TECH_WINDOW_FILM_TECHNOLOGY

These trigger when customers ask:

- thickness
- self healing
- precut vs manual
- film structure
- coating technology


------------------------------------------------------------
SECTION 4 — PRICE OBJECTION HANDLING
------------------------------------------------------------

Videos explaining why premium services cost more.

Examples:

VIDEO_COMPARE_PREMIUM_VS_CHEAP_PPF
VIDEO_COMPARE_PREMIUM_TINT_VS_CHEAP
VIDEO_COMPARE_CERAMIC_QUALITY_DIFFERENCE
VIDEO_MISTAKE_LOW_COST_INSTALL

These trigger when customers say:

- competitors cheaper
- free services offered
- price comparison questions


------------------------------------------------------------
SECTION 5 — AUTHENTICITY VERIFICATION
------------------------------------------------------------

Videos that show how customers can verify original products.

Examples:

VIDEO_VERIFY_XPEL_AUTHENTIC
VIDEO_VERIFY_PPF_SERIAL_NUMBER
VIDEO_VERIFY_INSTALLER_CERTIFICATION


------------------------------------------------------------
SECTION 6 — VISUAL TRIGGER MAPPING
------------------------------------------------------------

Education snippets from Phase 7 may trigger related visual demonstrations.

Examples:

EDU_PPF_PROTECTION → VIDEO_PROOF_PPF_SELF_HEAL
EDU_CERAMIC_LIMITATIONS → VIDEO_PROOF_CERAMIC_HYDROPHOBIC
EDU_TINT_HEAT_REJECTION → VIDEO_PROOF_TINT_HEAT_REJECTION


------------------------------------------------------------
SECTION 7 — VIDEO DELIVERY GUIDELINES
------------------------------------------------------------

Videos should not flood customer chat.

Recommended format:

1 short explanation sentence
1 video link
1 follow-up question

Example:

"Many PPF films can recover from light scratches with heat."

VIDEO LINK

"Which car model are you planning to protect?"


Maximum rule:

Only one video per conversation segment.



------------------------------------------------------------
SECTION 8 — VIDEO PRODUCTION GUIDELINES
------------------------------------------------------------

Standard structure for SNASH visual assets.

Recommended video length:

20–40 seconds


Recommended structure:

3 sec — problem
10 sec — demonstration
10 sec — result
5 sec — final shot


Production guidelines:

- clean lighting
- tripod camera
- minimal background noise
- visible branding watermark
- bilingual captions when possible


------------------------------------------------------------
SECTION 9 — VIDEO HOSTING STRATEGY
------------------------------------------------------------

Initial hosting recommendation:

Unlisted YouTube or Vimeo private hosting.

Future secure hosting options:

AWS S3
Cloudflare Stream
Private CDN

Optional security features:

expiring links
restricted embedding
watermarked videos


------------------------------------------------------------
SECTION 10 — FUTURE EXPANSION
------------------------------------------------------------

The visual library will grow gradually.

Initial recommended library:

15 videos

Long-term scalable library:

40–60 videos


New videos can be added without modifying architecture by updating:

PHASE8_VIDEO_LIBRARY.md


END PATCH

------------------------------------------------------------
SECTION 11 — VISUAL PRIORITY LADDER
------------------------------------------------------------

Purpose:
Ensures the correct order of visual persuasion during conversations.

When multiple visual assets are eligible, the router must follow
the priority ladder below.

VISUAL PRIORITY ORDER

LEVEL 1 — TECHNICAL PROOF

Demonstrates real performance of the service.

Examples:

VIDEO_PROOF_PPF_SELF_HEAL
VIDEO_PROOF_STONE_IMPACT_TEST
VIDEO_PROOF_CERAMIC_HYDROPHOBIC
VIDEO_PROOF_TINT_HEAT_REJECTION


LEVEL 2 — INSTALLATION TRANSPARENCY

Shows how the service is professionally installed.

Examples:

VIDEO_INSTALL_PPF_PROCESS
VIDEO_INSTALL_CERAMIC_PROCESS
VIDEO_INSTALL_TINT_PROCESS
VIDEO_INSTALL_POLISH_PROCESS


LEVEL 3 — RESULT SHOWCASE

Shows the final result on real vehicles.

Examples:

VIDEO_RESULT_WHITE_SUV_PPF
VIDEO_RESULT_LUXURY_POLISH
VIDEO_RESULT_BLACK_SUV_CERAMIC


LEVEL 4 — CUSTOMER TESTIMONIALS

Provides social proof from real customers.

Examples:

VIDEO_TESTIMONIAL_PPF_CUSTOMER
VIDEO_TESTIMONIAL_CERAMIC_CUSTOMER
VIDEO_TESTIMONIAL_TINT_CUSTOMER


LEVEL 5 — BRAND CREDIBILITY

Builds trust in the shop and installation standards.

Examples:

VIDEO_TEAM_EXPERTISE
VIDEO_SHOP_TOUR
VIDEO_BRAND_XPEL_TECHNOLOGY
VIDEO_BRAND_GLOBAL_FILM_OVERVIEW


LEVEL 6 — BOOKING CONFIDENCE

Final reassurance before scheduling service.

Examples:

VIDEO_DAY_OF_INSTALLATION_PROCESS
VIDEO_INSTALLATION_FACILITY


RULES

1. Always prefer the highest-priority visual available.
2. Do not show more than one visual per response segment.
3. Technical proof should always appear before testimonials or brand content.
4. Brand credibility visuals should appear only after technical proof or installation transparency.

END VISUAL PRIORITY LADDER

