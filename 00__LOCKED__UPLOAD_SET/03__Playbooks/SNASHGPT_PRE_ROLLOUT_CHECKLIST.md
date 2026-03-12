################################################################
SNASHGPT PRE-ROLLOUT CHECKLIST
################################################################

Purpose

This document defines the final validation steps before deploying
SNASHGPT for real customer conversations.

It ensures that:

• Runtime architecture is stable
• Education and persuasion layers are complete
• Video persuasion library is available
• Conversation routing is validated
• Production environment is ready


################################################################
SECTION 1 — RUNTIME ARCHITECTURE VALIDATION
################################################################

Verify system integrity.

Required checks

Run runtime integrity check:

python tools/runtime_integrity_check.py

Run architecture audit:

python tools/control_tower.py --audit

Run phrase coverage audit:

python tools/phrase_coverage_heatmap.py

Expected result

• No runtime errors
• Governance pipeline passes
• Engines present
• Phrase routing intact


################################################################
SECTION 2 — CONVERSATION SIMULATION TESTS
################################################################

Run all conversation simulators.

python simulator/edge_case_simulator.py
python simulator/conversation_simulator_v2.py

Test scenarios include:

• Price-only customers
• Multi-question messages
• Brand comparison questions
• Protection confusion (PPF vs Ceramic)
• Technical questions
• Short messages / chaotic input

Goal

Ensure correct phase transitions:

Phase0 → greeting
Phase3 → price context
Phase4 → qualification
Phase7 → education
Phase9 → persuasion


################################################################
SECTION 3 — EDUCATION COVERAGE VALIDATION
################################################################

Verify Phase-7 education coverage.

Key snippets must exist for:

PPF protection
PPF self-healing
Ceramic coating role
Tint heat rejection
Wrap styling
Durability realism
Warranty realism
Installation quality
Protection level comparison


################################################################
SECTION 4 — PERSUASION LAYER VALIDATION
################################################################

Confirm Phase-9 persuasion triggers.

Persuasion anchors:

Installation quality
Surface preparation
Edge finishing quality
Stone impact protection
Self-healing demonstration
Ceramic hydrophobic behavior
GCC climate durability
Long-term performance
Visual verification
Honest limitation explanation
Customer experience proof


################################################################
SECTION 5 — VIDEO LIBRARY (PHASE 8)
################################################################

Video persuasion library must exist.

Minimum rollout set (7 videos)

1. PPF self-healing demo
2. Stone chip protection example
3. Ceramic hydrophobic demo
4. Tint heat rejection comparison
5. Installation edge finishing close-up
6. Installation process walkthrough
7. Customer testimonial

Recommended extended library

15 total videos including:

• Installation demonstrations
• Protection comparisons
• Finished vehicle showcases
• Customer experiences


################################################################
SECTION 6 — VIDEO HOSTING
################################################################

Videos must be hosted on a stable CDN.

Recommended hosting options:

Cloudflare R2 + CDN
AWS S3
Vimeo private links

Requirements

• Stable HTTPS links
• Fast mobile loading
• Direct video playback


################################################################
SECTION 7 — VIDEO TOKEN MAPPING
################################################################

Video links must be mapped to runtime tokens.

Examples

VIDEO_PROOF_PPF_SELF_HEAL
VIDEO_PROOF_CERAMIC_HYDROPHOBIC
VIDEO_PROOF_TINT_HEAT_REJECTION

Mapping must be defined in:

PHASE8_VIDEO_LIBRARY.md


################################################################
SECTION 8 — PRICE TABLE VALIDATION
################################################################

Verify correct pricing configuration.

File

03__Parameters/PRICE_TABLE_VAT_INCL.md

Ensure:

• Prices match shop pricing
• All service tiers exist
• No SKU mismatch


################################################################
SECTION 9 — PRODUCTION CONVERSATION TEST SET
################################################################

Run real-world conversation tests.

Example scenarios

1. "hi price"
2. "price full ppf land cruiser"
3. "ceramic or ppf which better"
4. "my friend got cheaper"
5. "what thickness is ppf"
6. "does ppf self heal"
7. "xpel vs other brands"
8. "tint price"
9. "how long does ceramic last"

Goal

Confirm natural conversation flow.


################################################################
SECTION 10 — DEPLOYMENT ENVIRONMENT
################################################################

Define runtime interface.

Possible environments

• WhatsApp API
• Web chat widget
• CRM integration
• Internal sales dashboard

Ensure

• message formatting works
• video links render correctly
• responses remain natural


################################################################
SECTION 11 — SOFT LAUNCH
################################################################

Run limited real conversations.

Recommended test

First 30-50 customer conversations.

Monitor

• conversation completion
• customer questions
• objection patterns
• phrase effectiveness


################################################################
SECTION 12 — POST-LAUNCH IMPROVEMENTS
################################################################

After deployment track:

• objection patterns
• price sensitivity
• most requested services
• persuasion effectiveness

Use findings to improve:

• Phase-7 education snippets
• Phase-9 persuasion phrases
• video library


################################################################
END DOCUMENT
################################################################
