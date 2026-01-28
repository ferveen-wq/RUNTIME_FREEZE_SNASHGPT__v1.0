PHASE 0 — GOVERNANCE & RULES (STATIC, ALWAYS ON)
│
│  • Business rules
│  • Allowed / disallowed behavior
│  • Language discipline
│  • Ethics, tone limits, boundaries
│  • What SNASHGPT is / is NOT
│
│  (Phase 0 NEVER talks to customers)
│
└───────────────▶ feeds constraints & laws
                │
                ▼
PHASE 1 — QUALIFICATION ENGINE (LOCKED)
│
│  INPUTS:
│  • Raw customer message
│  • Session metadata
│  • Language detection
│  • Phase 0 constraints
│
│  INTERNAL ACTIONS (NO RESPONSE):
│  • Identify: customer vs non-customer
│  • Classify: on-scope / off-scope / adjacent
│  • Check: minimum context completeness
│  • Detect: blocking constraints
│  • Assign: qualification_state
│  • Assign: confidence (classification certainty)
│
│  STRICT BLOCKS:
│  • No pricing
│  • No negotiation
│  • No tone control
│  • No persuasion
│  • No redirection
│
│  OUTPUT (INTERNAL ONLY):
│  • qualification_state
│  • constraints
│  • missing_fields
│  • allowed_next_actions
│
└───────────────▶ handoff (one-way)
                │
                ▼
PHASE 2 — SOLUTION / NEGOTIATION (DYNAMIC)
│
│  Uses Phase-1 outputs ONLY
│
│  • Human conversation starts
│  • Problem → service mapping
│  • Adjacent service suggestions
│  • Objection handling
│  • Trust & value building
│
└───────────────▶ conditional feedback
                │   (never rewrites Phase 1)
                ▼
PHASE 3 — PRICING & CLOSURE
│
│  • Pricing logic
│  • Offers / discounts
│  • Final commitment
│  • Sales handover
│
└───────────────▶ POST-SALE / OPS (later)