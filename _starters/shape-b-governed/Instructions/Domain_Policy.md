# [Domain] Policy

## Purpose

This file is the operational firewall. It defines what the AI may and may not do, independent of the execution sequence. The System file says HOW to work. This file says WHERE THE LINES ARE.

## Classification System

Every input element must be classified into one of these tiers before any output is produced:

| Tier | Definition | Action |
|---|---|---|
| **EXECUTE NOW** | Defensible source exists. Reference data confirms. No ambiguity. | Proceed to populate. |
| **FLAG FOR REVIEW** | Source exists but is provisional, ambiguous, or requires human judgement. | Populate with explicit flag marker and reason. |
| **HARD STOP** | No defensible source. Or: output would violate a prohibition below. | Do not populate. Document and escalate. |

[NOTE: Adapt the three tiers to your domain. For creative workflows, this might be: GENERATE / GENERATE WITH CAVEAT / DO NOT GENERATE. The principle is the same — every element gets classified before work begins.]

## Hard Prohibitions

These are non-negotiable. Violation of any prohibition invalidates the entire output.

1. [DOMAIN-SPECIFIC] Never [specific dangerous action for your domain].
2. [DOMAIN-SPECIFIC] Never [second prohibition].
3. [DOMAIN-SPECIFIC] Never [third prohibition].
4. **Never invent data that should come from the Reference layer.** If the reference is missing, flag or hard-stop — do not fabricate.
5. **Never silently drop scope.** If an input element cannot be processed, it must appear in the output as explicitly unresolved, not omitted.

[NOTE: Write at least 5 prohibitions. The first 3 should be specific to your domain. The last 2 above are universal. Add more as real runs reveal failure patterns.]

## Evidence Requirements

Before any claim, recommendation, or populated field:

| Claim Type | Required Evidence |
|---|---|
| Factual assertion | Direct extraction from input OR lookup from Reference |
| Recommendation | Stated reasoning chain traceable to input + reference |
| Synthesised content | Governed by the protocols in `Instructions/Domain_System.md` |
| Statistical claim | Source citation required — never state a number without provenance |

## Escalation Triggers

The AI must pause and request human decision when:
- [Trigger 1 — domain-specific]
- [Trigger 2]
- [Trigger 3]
- More than [N]% of input elements are classified as HARD STOP
- The output would be materially different from a previous run on similar input (if run history exists)

## Internal vs External Separation

[NOTE: If your workflow produces both internal working documents and client-facing deliverables, define the boundary here. What stays internal? What goes to the client? What can never appear in external output?]

- **Internal only**: [List what stays internal]
- **External deliverable**: [List what the client sees]
- **Never external**: [List what must never appear in client-facing output]

---

*[Delete all `[NOTE:]` annotations and `[PLACEHOLDER]` text before going live.]*
