
ISSUE-034 — Phase3A qualifier loop on price push

SYMPTOM:
- User says "price" repeatedly
- System repeats same qualifier

ROOT CAUSE:
- No ignored qualifier detection
- No UNKNOWN fallback execution

STATUS:
REOPENED

VALIDATION:
Manual project test produced one temporary pass, then failed on repeat retest.
Current evidence: second repeated price push still repeats Phase3A nudge/qualifier instead of entering Phase3B pricing.

REOPEN_REASON:
- Prior closure was based on a single manual pass, not stable repeated validation.
- Behavior is inconsistent because current logic relies on non-durable state / brittle visible-message detection.
- Proper fix requires durable repeated-price interruption state or one final authority for Phase3A repeated price exit.
