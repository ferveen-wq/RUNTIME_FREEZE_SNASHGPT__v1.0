
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

