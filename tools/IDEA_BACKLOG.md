
------------------------------------------------------------
IDEA: PHASE7 EDUCATION SNIPPET — PPF THICKNESS
------------------------------------------------------------

ID: IDEA_PHASE7_EDU_PPF_THICKNESS

Description:
Customers frequently ask how thick PPF film is and whether thickness
affects protection.

Potential snippet:

EDU_PPF_THICKNESS

Topics to cover:

• typical micron range of quality films
• thickness vs flexibility trade-off
• why thickness alone does not define quality
• relation to impact resistance

Possible visual pairing:

VIDEO_TECH_PPF_THICKNESS_EXPLAINED

Status: BACKLOG
Priority: MEDIUM


------------------------------------------------------------
IDEA: PHASE7 EDUCATION SNIPPET — CERAMIC MAINTENANCE
------------------------------------------------------------

ID: IDEA_PHASE7_EDU_CERAMIC_MAINTENANCE

Description:
Customers often believe ceramic coating is permanent and requires
no maintenance. Education is needed about washing and refresh cycles.

Potential snippet:

EDU_CERAMIC_MAINTENANCE

Topics to cover:

• ceramic coating is not maintenance-free
• importance of proper washing
• periodic inspection or booster layer
• environmental factors in GCC climate

Possible visual pairing:

VIDEO_MAINTENANCE_CERAMIC_GUIDE

Status: BACKLOG
Priority: MEDIUM


------------------------------------------------------------
IDEA: DEFERRED VISUAL TRIGGER (CUSTOMER DOUBT CLARIFICATION)
------------------------------------------------------------

ID: IDEA_PHASE8_DEFERRED_VISUAL_TRIGGER

Description:
If a customer asks about a technical topic early in the conversation
(e.g., precut patterns, PPF thickness, ceramic durability), the system
may initially provide only a text explanation during Phase0–2.

Later in the conversation, when the discussion progresses toward
service selection or objection handling, the runtime may trigger a
related visual asset even if the customer does not explicitly ask again.

Purpose:

• reinforce earlier explanation
• remove lingering doubt
• support closing stage clarification

Example flow:

Customer early:
"Do you use precut patterns?"

Phase0–2 response:
text explanation only

Later Phase4 discussion:
attach video

VIDEO_TECH_PPF_PRECUT_VS_MANUAL

Rules:

• only trigger if topic was previously discussed
• do not interrupt conversation flow
• maximum 1 deferred visual per topic

Status: BACKLOG
Priority: MEDIUM


------------------------------------------------------------
IDEA: VISUAL MEMORY (PREVENT VIDEO REPETITION)
------------------------------------------------------------

ID: IDEA_PHASE8_VISUAL_MEMORY

Description:
Track which visual assets have already been shown during the
conversation to prevent repeating the same video multiple times.

Purpose:

• avoid customer fatigue
• keep conversation natural
• allow progressive proof presentation

Example behavior:

VIDEO_PROOF_PPF_SELF_HEAL shown
↓
do not show same video again

If another proof is required, use:

VIDEO_RESULT_PPF_SHOWCASE
or
VIDEO_TESTIMONIAL_PPF_CUSTOMER

Possible runtime variable:

visuals_already_shown = []

Rules:

• prevent repeating same visual
• allow different category visuals
• reset memory on new conversation

Status: BACKLOG
Priority: MEDIUM


------------------------------------------------------------
IDEA: PHASE8 STARTER VIDEO LIBRARY (15 CORE ASSETS)
------------------------------------------------------------

Purpose:
Define the initial visual production set that will cover
approximately 80% of customer persuasion scenarios.

Videos follow the Visual Priority Ladder.

LEVEL 1 — TECHNICAL PROOF

VIDEO_PROOF_PPF_SELF_HEAL
VIDEO_PROOF_STONE_IMPACT_TEST
VIDEO_PROOF_CERAMIC_HYDROPHOBIC
VIDEO_PROOF_TINT_HEAT_REJECTION


LEVEL 2 — INSTALLATION TRANSPARENCY

VIDEO_INSTALL_PPF_PROCESS
VIDEO_INSTALL_CERAMIC_PROCESS
VIDEO_INSTALL_TINT_PROCESS


LEVEL 3 — RESULT SHOWCASE

VIDEO_RESULT_WHITE_SUV_PPF
VIDEO_RESULT_BLACK_SUV_CERAMIC
VIDEO_RESULT_LUXURY_POLISH


LEVEL 4 — CUSTOMER TESTIMONIALS

VIDEO_TESTIMONIAL_PPF_CUSTOMER
VIDEO_TESTIMONIAL_CERAMIC_CUSTOMER


LEVEL 5 — BRAND CREDIBILITY

VIDEO_SHOP_TOUR
VIDEO_TEAM_EXPERTISE
VIDEO_DAY_OF_INSTALLATION_PROCESS


Notes:

• Videos should be 20–40 seconds.
• Follow production structure:

3 sec  — problem
10 sec — demonstration
10 sec — result
5 sec  — closing shot

Status: BACKLOG
Priority: HIGH


------------------------------------------------------------
IDEA: PRE-PATCH DUE DILIGENCE CHECKLIST
------------------------------------------------------------

ID: IDEA_ARCH_PREPATCH_DUE_DILIGENCE

Description:
Define a lightweight pre-patch checklist that must be reviewed before
any runtime or control-tower patch is applied.

Purpose:

• reduce duplicate logic
• reduce wrong-file patching
• improve architecture safety
• keep patching disciplined during rollout preparation

Proposed checklist items:

• confirm target file role
• inspect surrounding section before patch
• inspect adjacent authority file if relevant
• confirm logic is missing (not already present)
• define validation path before commit

Status: BACKLOG
Priority: HIGH


------------------------------------------------------------
IDEA: ROLLOUT TESTING AND AUDIT FRAMEWORK
------------------------------------------------------------

ID: IDEA_ROLLOUT_TEST_AUDIT_FRAMEWORK

Description:
Define a practical rollout-readiness framework for validating the
architecture with limited resources before assistant adoption.

Purpose:

• improve rollout confidence
• test phase flow and state carry-forward
• detect behavior drift before production usage
• create a repeatable audit path for future releases

Suggested components:

• must-pass rollout pack
• golden multi-turn chat pack
• assistant shadow-use review
• phase coverage map
• mismatch / drift review checklist

Status: BACKLOG
Priority: HIGH


------------------------------------------------------------
IDEA: ARCHITECTURE-AWARE PATCH AUDIT TOOL
------------------------------------------------------------

ID: IDEA_ARCH_PATCH_AUDIT_TOOL

Description:
Future helper tool that checks whether a proposed patch may duplicate,
overlap, or conflict with existing authority across runtime and
control-tower files.

Purpose:

• detect competing logic before patching
• improve enforcement beyond formatting and governance checks
• support safer rollout and future maintenance

Possible checks:

• similar rule already exists elsewhere
• stronger authority file already owns the logic
• runtime vs control-tower boundary conflict
• duplicate selection or routing behavior
• missing validation / UAT path

Status: BACKLOG
Priority: MEDIUM


------------------------------------------------------------
ITEM: Asset Schema Expansion (Post-Rollout)
------------------------------------------------------------

Purpose:
Expand current rollout asset schema into full scalable asset-routing system.

Includes:
- Support for multiple asset types (VIDEO / LINK / DOC / MAP)
- Advanced metadata routing:
  - BRAND
  - TEXTURE
  - WARRANTY_TIER
  - SPEC_TOPIC
  - VEHICLE_MAKE / MODEL / SEGMENT / COLOR
- Advanced matching ladder:
  - exact match → partial → fallback
- New categories:
  - AFTERCARE
  - AUTHENTICITY
  - TECHNICAL
  - GENERAL_CARE
  - UPSELL
- Non-video asset routing (links, maps, docs)

Status:
- NOT ACTIVE in rollout
- To be revisited post-rollout

Risk if ignored:
- scaling difficulty
- inconsistent asset additions
- duplicated logic later

Priority:
MEDIUM (post-rollout phase)


------------------------------------------------------------
IDEA: PHASE 9 TRUST RUNTIME PROMOTION REVIEW
------------------------------------------------------------

ID: IDEA_PHASE9_TRUST_RUNTIME_PROMOTION

Description:
Review whether the currently validated Phase 9 trust behavior should be promoted
from working reference into runtime authority before rollout.

Current state:
- Logic manually validated in working session
- Not yet runtime-patched
- Requires final test-pack confirmation

Questions to resolve:
- Is existing runtime already sufficient?
- Does trust behavior need explicit runtime routing rules?
- Which file should own the behavior if promoted?

Status: BACKLOG
Priority: HIGH

