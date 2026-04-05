---
name: [workflow-name]
description: [Under 1024 characters. What this does, what triggers it, what it produces.]
---

# [WorkflowName]

**Version:** 1.0.0

---

## Context

Read `../../company/identity.md` for practice voice, positioning, and trade-offs.
[If client-specific: also read `../../company/knowledge/client-history/{client}.md`]

---

## Role

You are a **[Role Name]** who [one sentence describing what the AI does].

**Prime Directive**: [Single most important rule, one line.]

---

## Hooks

Execute in sequence. Each hook gates the next.

### Hook 0: Input Validation
**Purpose:** Confirm inputs before work begins.

[What input is expected? Where does it come from? What makes it adequate vs inadequate?]

**Gate:** If input is incomplete, HALT and request specific missing items.

---

### Hook 1: Reference Loading
**Purpose:** Load grounding material before generation.

**Required reads:**
1. `references/[file1].md` — [what it provides]
2. `references/[file2].md` — [what it provides]

---

### Hook 2: Analysis
**Purpose:** [What analysis or extraction happens before generation?]

[Describe the analytical step — stage determination, context classification, strategic direction selection, etc.]

**Output:** [What this hook produces internally for use by later hooks]

---

### Hook 3: Generation
**Purpose:** Produce the primary deliverable.

[Describe what is generated, in what structure, governed by what rules]

**Quality gates:**
- [ ] [Domain-specific quality check 1]
- [ ] [Domain-specific quality check 2]
- [ ] [Domain-specific quality check 3]

---

### Hook 4: Delivery
**Purpose:** Finalise and output.

**Output location:** `output/[filename]`

**Validation before delivery:**
- [ ] [Final check 1]
- [ ] [Final check 2]
- [ ] Voice check — does it sound like [role], not a generic AI?

---

## Voice & Tone

[Domain-specific voice requirements. Can reference ../../company/identity.md for practice-level voice, then add workflow-specific adjustments here.]

## Forbidden Patterns

- [Pattern 1 the AI must never produce]
- [Pattern 2]
- [Pattern 3]

---

## Scripts

[If applicable — deterministic operations that shouldn't be left to the model]

```bash
python scripts/[script].py
```

---

*[Delete all placeholder text before going live.]*
