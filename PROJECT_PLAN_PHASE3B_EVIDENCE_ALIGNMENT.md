# PROJECT PLAN — PHASE 3B EVIDENCE ALIGNMENT

Status: ACTIVE
Mode: EVIDENCE-FIRST (NO RUNTIME PATCHING)

## OBJECTIVE

Verify Phase 3B pricing-readiness behavior across applicable services using:
- live runtime files
- git history (if needed)
- dependency validation

## AUDIT MODEL

Focus:
- readiness gates
- price-entry conditions
- price ladder ownership boundaries
- dependency usage
- service-specific exceptions
- downstream handoff correctness

## SERVICES (IN ORDER)

- [x] PPF
- [ ] Ceramic
- [ ] Tint
- [ ] Polishing
- [ ] Wrap (special-case validation only)

## RULES

1. Do NOT assume readiness behavior — prove from runtime files
2. Do NOT mix Phase 3A qualifier rules into Phase 3B pricing rules
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
