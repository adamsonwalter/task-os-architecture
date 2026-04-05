# State Engine Protocol

**Purpose**: Manage session state and phase transitions for landing page creation

---

## Context Gathering

Before any phase work, capture this context:

### Required Context
```yaml
product_service: "What are you selling?"
target_audience: "Who is the ideal buyer? (role, industry, pain level)"
single_action: "What ONE action should they take?"
transformation: "What result/outcome do they get?"
price_point: "Free lead magnet / Low ($) / Mid ($$) / High ($$$)"
```

### Optional Context (ask if unclear)
```yaml
awareness_level: "unaware|problem_aware|solution_aware|product_aware|most_aware"
industry: "SaaS|ecommerce|agency|coaching|info_product|other"
existing_assets: "testimonials, logos, stats, case studies available?"
current_conversion: "Do you know your current conversion rate?"
```

---

## Awareness Level Framework (Eugene Schwartz)

| Level | Visitor Knows | Lead With |
|-------|--------------|-----------|
| **Unaware** | Nothing | The problem (agitate) |
| **Problem Aware** | Pain exists | The solution category |
| **Solution Aware** | Solutions exist | Why YOUR solution |
| **Product Aware** | Your product | Differentiation + proof |
| **Most Aware** | Everything | The offer (price, urgency) |

Match headline strategy to awareness level.

---

## Phase Transition Rules

```
ENTRY → CONTEXT CAPTURE → PHASE 1
                              ↓
Phase N complete? → Capture outputs → Advance to N+1
                              ↓
Phase 7 complete? → Compile full page → Offer audit/variants
```

### State Update Pattern
```json
{
  "phase": N,
  "delta": {
    "sections": [{ "name": "hero", "copy": {...}, "valueImpact": {...} }],
    "valueScore": { "dreamOutcome": +2, "likelihood": +1 }
  }
}
```

---

## Value Score Tracking

Track cumulative impact across phases:

| Lever | Score Range | Phase Contributions |
|-------|-------------|---------------------|
| Dream Outcome | 0-10 | Hero +3, Value +2, Benefits +3, Final +2 |
| Likelihood | 0-10 | Trust +4, Testimonials +3, Guarantees +3 |
| Time Delay | 0-10 | Hero -2, CTA -3, Urgency -3, Clear steps -2 |
| Effort | 0-10 | Form simplicity -3, Clear CTA -2, FAQ -3, Mobile -2 |

**Target**: Dream×Likelihood ≥ 50, TimeDelay×Effort ≤ 20

---

## Interrupt Handlers

| User Interrupt | Response |
|----------------|----------|
| "Skip to [phase]" | Mark current as draft, jump to requested |
| "Go back to [phase]" | Preserve current, re-enter previous |
| "Show full page" | Compile all completed sections |
| "Audit mode" | Switch to audit_protocol.md |
| "Just give me copy" | Output copy-only, skip structure |

---

## Session Memory

Between phases, preserve:
- All context variables
- Completed section outputs
- Value score running totals
- User feedback/preferences
- Copy style detected (formal/casual/technical/emotional)

---

## Error States

| Error | Resolution |
|-------|------------|
| Missing context | Prompt for required fields |
| Conflicting objectives | Force single CTA decision |
| No trust assets | Suggest creation strategies |
| Low value score | Trigger optimization recommendations |

---

**END PROTOCOL**
