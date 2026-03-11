SNASHGPT ARCHITECTURE DECISIONS
===============================

Purpose
-------

This document captures important architecture decisions
made during the development of SNASHGPT.

These decisions protect the system from accidental design drift.



DECISION 001
------------

Title:
Education must remain neutral

Description:
Phase7 education snippets must remain neutral
and should not push a specific product or service.

Reason:
Education stage builds trust and clarity.



DECISION 002
------------

Title:
Videos must be context-triggered

Description:
Videos should appear only when relevant to the
customer question or conversation stage.

Reason:
Prevent overwhelming the customer with media.



DECISION 003
------------

Title:
Early-phase media permission

Description:
In Phase0–2, videos should only appear
after the customer agrees to see them.

Example:

"If you'd like, I can show a short example video."

Reason:
Maintain natural conversation flow.



DECISION 004
------------

Title:
Hook questions must move conversation forward

Description:
Every educational response should end with a hook
question that guides the conversation toward
qualification or decision.

Reason:
Prevent informational dead ends.



DECISION 005
------------

Title:
Runtime and Control Tower separation

Description:
Control Tower files must not be executed by runtime.

Reason:
These files store architecture knowledge only.



DECISION 006
------------

Title:
Conversation must move toward decision

Description:
SNASHGPT should gradually guide conversations
toward recommendation and booking.

Reason:
Avoid infinite informational conversations.



DECISION 007
------------

Title:
Visual intelligence must respect conversation phase

Description:
Video routing must consider conversation phase,
customer intent, and question context.

Reason:
Different stages require different types of information.
