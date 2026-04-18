# PROJECT PLAN — PHASE 3A EVIDENCE ALIGNMENT

Status: ACTIVE
Mode: EVIDENCE-FIRST (NO RUNTIME PATCHING)

## OBJECTIVE

Verify Phase 3A qualification behavior across all services using:
- live runtime files
- git history (if needed)
- dependency validation

## AUDIT MODEL

Focus:
- signal writers (ownership)
- state transitions
- qualification triggers
- dependency usage
- downstream handoff correctness

## SERVICES (IN ORDER)

- [x] PPF
- [x] Ceramic
- [ ] Tint
- [ ] Polishing
- [ ] Wrap

## RULES

1. Do NOT assume behavior — prove from runtime files
2. Do NOT mix Phase 0–2 logic into Phase 3A
3. Do NOT patch runtime files
4. Log gaps before any fix
5. Separate:
   - current runtime
   - historical intent
   - open decisions

## OUTPUT

For each service:
- evidence audit file
- gap entries (if any)
- control-doc updates
