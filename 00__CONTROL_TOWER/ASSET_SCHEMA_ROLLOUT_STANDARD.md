# ASSET SCHEMA — ROLLOUT STANDARD (ACTIVE)

Purpose:
Define the minimum required asset structure for rollout.

This is a rollout-active reference.
Future extensions are tracked in IDEA_BACKLOG.md.

------------------------------------------------------------
ACTIVE FIELDS (MANDATORY)
------------------------------------------------------------

ASSET_ID
ASSET_NAME
ASSET_TYPE (VIDEO / LINK)

SERVICE (PPF / CERAMIC / TINT / POLISH / MULTI / GENERAL)

CATEGORY
- PROOF
- EDUCATION
- COMPARISON
- PROCESS
- RESULT
- TESTIMONIAL
- TRUST

PRIMARY_TRIGGER

PHASE_DEFAULT
SECONDARY_PHASE

LANGUAGE

LINK
STATUS

------------------------------------------------------------
SELECTION RULE (ROLLOUT)
------------------------------------------------------------

Selection must consider only:

1. PRIMARY_TRIGGER
2. PHASE
3. SERVICE
4. CATEGORY
5. LANGUAGE

Do NOT depend on advanced metadata during rollout.

------------------------------------------------------------
RESERVED FIELDS (FUTURE — NOT ACTIVE)
------------------------------------------------------------

BRAND
TEXTURE
WARRANTY_TIER
SPEC_TOPIC

VEHICLE_MAKE
VEHICLE_MODEL
VEHICLE_SEGMENT
VEHICLE_COLOR

REGION
AFTERCARE_TYPE

------------------------------------------------------------
RULES
------------------------------------------------------------

- Do not introduce new categories during rollout
- Do not depend on optional fields for selection
- MULTI is allowed only for comparison / cross-service
- GENERAL is allowed only for trust / brand

------------------------------------------------------------
STATUS
------------------------------------------------------------

ACTIVE FOR ROLLOUT

Future expansion tracked in IDEA_BACKLOG.md
