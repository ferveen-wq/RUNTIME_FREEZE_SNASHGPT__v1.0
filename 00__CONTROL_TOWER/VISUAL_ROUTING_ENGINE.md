SNASHGPT VISUAL ROUTING ENGINE
==============================

Purpose
-------

The Visual Routing Engine decides which video should appear
during a conversation based on customer questions,
service interest, and conversation phase.



INPUT SIGNALS
-------------

The routing engine evaluates the following signals:

• conversation_phase
• service_intent
• customer_question
• vehicle_model
• vehicle_color
• objection_type



PHASE RULES
-----------


Phase0 – Phase2
---------------

Videos should NOT appear automatically.

Instead the system asks permission.

Example:

"If you'd like, I can show a short video demonstrating that."

Only display the video if the customer agrees.



Phase3
------

Videos may appear when the customer is evaluating options.

Example:

installation process
service explanation



Phase4
------

Videos appear automatically when customers ask
technical or educational questions.

Example triggers:

self healing
installation method
coating durability
difference between services



Phase5
------

Videos reinforce trust and decision making.

Examples:

customer testimonials
finished vehicle results
before/after comparisons



ROUTING EXAMPLES
----------------


Trigger:
"Is PPF self healing?"

Route to:
PPF_SELF_HEALING_DEMO



Trigger:
"How is PPF installed?"

Route to:
PPF_INSTALLATION_PROCESS



Trigger:
"What is ceramic coating?"

Route to:
CERAMIC_COATING_PROCESS



Trigger:
"PPF or ceramic which is better?"

Route to:
PPF_VS_CERAMIC_DIFFERENCE



Trigger:
Customer unsure about decision

Route to:
CUSTOMER_TESTIMONIAL



FUTURE ROUTING CAPABILITIES
---------------------------

Vehicle-based routing
Example:

Toyota Land Cruiser → show large SUV example


Color-based routing
Example:

Black vehicle → show black vehicle result


Service-package routing
Example:

Full body PPF → show full body installation video



VIDEO DISPLAY STRUCTURE
-----------------------

Educational snippet
↓

Short explanation

↓

Video

↓

Hook question guiding the conversation forward



Example structure:


"Yes — high quality PPF has a self-healing top layer.

Light scratches can disappear when heat is applied.

This clip shows a real example of the film healing."

[VIDEO]

"Would you like to see how the film is installed as well?"



DESIGN PRINCIPLES
-----------------

Videos should:

• support explanations
• increase trust
• demonstrate real results

Videos should NOT:

• overwhelm the customer
• interrupt conversation flow
• replace conversation logic
