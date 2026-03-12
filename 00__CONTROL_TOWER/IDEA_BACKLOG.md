SNASHGPT IDEA BACKLOG
=====================

Purpose
-------

This document stores architecture ideas discussed during development
so they are not lost or forgotten.

Ideas can be implemented immediately or in future phases.


IDEA STATUS TYPES
-----------------

IDEA
PLANNED
IMPLEMENTED
DEFERRED



IDEA LIST
---------


IDEA 001
--------

Title:
Permission-based video display

Description:
When a technical question appears in early phases (Phase0–2),
the system should ask permission before showing a video.

Example:
"If you'd like, I can show a short clip demonstrating that."

Phase:
Phase8

Status:
PLANNED



IDEA 002
--------

Title:
Visual routing engine

Description:
Automatically select videos based on conversation context,
customer questions, and service interest.

Phase:
Phase8

Status:
PLANNED



IDEA 003
--------

Title:
Vehicle-specific result videos

Description:
Show finished results using the same vehicle model
or similar vehicle class.

Example:
Jetour T2 → similar SUV results.

Phase:
Phase8

Status:
IDEA



IDEA 004
--------

Title:
Color-matched vehicle examples

Description:
Show results with similar vehicle color when available.

Example:
Black SUV → black vehicle example video.

Phase:
Phase8

Status:
IDEA



IDEA 005
--------

Title:
Customer testimonial routing

Description:
Display testimonials from customers with similar vehicles
or services.

Phase:
Phase8

Status:
IDEA



IDEA 006
--------

Title:
Maintenance education videos

Description:
Explain what happens to PPF or ceramic coating
during normal driving and washing.

Phase:
Phase8

Status:
IDEA



IDEA 007
--------

Title:
Competitor objection videos

Description:
Videos explaining common objections such as:

• Why some shops are cheaper
• Why some offer free wash
• Brand authenticity concerns

Phase:
Phase8

Status:
IDEA



IDEA 008
--------

Title:
Video expiration links

Description:
Protect internal sales strategy by using temporary
video links that expire after a time.

Phase:
Phase8

Status:
IDEA



IDEA 009
--------

Title:
Conversation intelligence learning

Description:
Real customer chats will be analyzed and architecture
improvements will be logged.

Phase:
Phase10

Status:
IDEA



IDEA 010
--------

Title:
Psychological trigger integration

Description:
Use psychological triggers to guide customer decisions.

Examples:

• loss aversion
• social proof
• authority
• ownership pride

Phase:
Phase4–5

Status:
IDEA



IDEA AUTO
---------

Timestamp:
2026-03-11 21:09

Description:
anchor pricing for partial qualification

Status:
IDEA


### 2026-03-11 21:35
context aware hook questions after video

### 2026-03-11 21:38
test idea capture system

### 2026-03-11 22:15
video responses must always include a context-aware hook question to prevent conversational dead ends

### 2026-03-11 22:17
phase8: define the 7 high-converting detailing video types used by the visual routing engine

### 2026-03-11 22:49
build runtime bundler to consolidate architecture files before GPT deployment to meet file limits

### 2026-03-11 23:07
video responses must never end a conversation; every video must be followed by a context-aware hook question that moves the customer toward decision

### 2026-03-12 00:23
define the 7 high-converting detailing video categories and map them into Phase 8 visual intelligence routing

### 2026-03-12 00:40
visual router must select videos based on vehicle model, color, segment, service, conversation phase and customer concern

### 2026-03-12 00:40
video routing must follow hierarchical fallback: exact model+color → model → segment → color → generic service

### 2026-03-12 00:40
Phase 8 video taxonomy includes service explanation, proof tests, installation process, results showcase, testimonials, brand credibility, maintenance education, long term reality, mistake prevention, booking confidence, technical questions, price objections and authenticity verification

### 2026-03-12 00:40
video responses must follow delivery format: short explanation + video + follow up question

### 2026-03-12 00:40
maximum one video should be delivered per conversation segment

### 2026-03-12 00:40
education snippets from Phase 7 should trigger visual demonstrations in Phase 8

### 2026-03-12 00:40
initial visual library should start with around 15 videos and scale to 40-60 videos without architecture modification

### 2026-03-12 00:41
video library should use structured metadata including video id, service, trigger condition, conversation phase, language and notes

### 2026-03-12 00:41
visual router must trigger videos based on customer questions such as self healing, installation quality, protection strength and service comparisons

### 2026-03-12 00:41
videos should only be triggered in appropriate conversation phases (technical videos in Phase 4 and testimonial trust videos in Phase 5)

### 2026-03-12 00:41
video library should support bilingual assets (EN/AR) to match conversation language

### 2026-03-12 00:42
video library should map videos to services such as PPF, ceramic coating, tint and educational comparisons

### 2026-03-12 01:10
introduce runtime architecture consolidation layer to reduce file count by merging compatible runtime authorities without breaking separation of concerns

### 2026-03-12 02:15
Add GitHub CI governance pipeline

### 2026-03-12 02:15
Reduce runtime architecture files from 28 to ~18

### 2026-03-12 02:15
Idea lifecycle tracker for automatic DONE tagging

### 2026-03-12 02:17
Add architecture visualization map showing runtime, engines, parameters, and dependency graph

### 2026-03-12 02:19
Add architecture visualization map showing runtime, engines, parameters, and dependency graph

### 2026-03-12 03:18
Make architecture_graph auto-discover repo structure instead of manual node definition

### 2026-03-12 03:27
Make architecture graph auto-discover repo structure

### 2026-03-12 03:28
Build SNASHGPT conversation interface connected to database

### 2026-03-12 03:28
Add runtime architecture drift detection

### 2026-03-12 03:32
Design SNASHGPT conversation interface architecture (assistant UI + runtime + database integration)

### 2026-03-12 03:48
Restructure SNASHGPT database schema into customers, conversations, and messages tables for scalable conversation history and analytics

### 2026-03-12 03:53
Assistant Dashboard interface (Phase 8.1 prototype implemented — UI connected to database, conversation viewer and runtime integration pending)

### 2026-03-12 03:57
Future visual recognition engine: analyze customer photos to detect paint defects and trigger runtime recommendations

### 2026-03-12 03:57
Assistant-assisted visual review workflow: assistant tags customer photo conditions (scratches, swirl marks, matte paint) to assist runtime decision logic
