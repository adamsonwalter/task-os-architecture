# [WorkflowName] — Standard Operating Procedure

**Version:** 1.0
**Last updated:** [YYYY-MM-DD]
**Deployment mode:** [Mode 1 / Mode 2 / Mode 3]

---

## Overview

[WorkflowName] takes [input description] and produces [output description].

The workflow runs in [N] steps, takes approximately [time estimate] with a complete input and available reference data, and produces [output type] plus an internal summary.

---

## When to use this workflow

- [Condition 1 — when this workflow is appropriate]
- [Condition 2]
- [Condition 3]

## When NOT to use this workflow

- [Condition 1 — when to escalate or use a different approach]
- [Condition 2]

---

## Required before starting

**Input:** [What must be in `jobs/{slug}/source-data/`]
**Reference data:** [Which Reference files must be available and current]
**Template:** [Which template file must be loaded, if applicable]
**Access:** [Any system access, credentials, or context required]

---

## Step-by-Step Procedure

### Step 1 — Load and Orient

Load the input from `jobs/{slug}/source-data/`. Read completely.

Extract and record:
- [Key element 1]
- [Key element 2]
- [Key element 3]

**Gate:** If input is incomplete or unidentifiable, stop. State the issue. Request the correct input.

---

### Step 2 — Extract and Normalise

[What is extracted from the input and how it is structured internally]

Output of this step: an internal structured list of [N] items with classification pending.

**Gate:** If fewer than [threshold] items can be extracted with confidence, flag the input as insufficient.

---

### Step 3 — Analyse Context

[What contextual factors are identified that affect classification or generation]

Record all contextual factors explicitly. Do not carry them as silent assumptions.

**Gate:** If a required contextual factor cannot be determined, escalate before proceeding.

---

### Step 4 — Map to Reference Data

Consult:
- [Reference file 1] for [what it provides]
- [Reference file 2] for [what it provides]

For each item: record whether a reference source was found (YES / NO / PARTIAL).

**Gate:** Items with no reference source are classified per `Instructions/Domain_Policy.md`.

---

### Step 5 — Classify and Plan

[For extractive workflows: apply the three-tier classification from Policy.md]
[For generative workflows: select strategic direction and declare the generation plan]

**Gate:** If more than [threshold]% of items are HARD STOP or if source data is inadequate for the declared plan, pause and present the assessment to the operator.

---

### Step 6 — Inspect Output Format

Load the output specification from `templates/`. Cross-reference with `Instructions/Output_Mapping.md`.

Confirm the allowed state and source mapping for every field or section. Do not write anything yet.

**Gate:** If a field has no mapping in Output_Mapping.md, flag it and do not populate.

---

### Step 7 — Produce Output

[For extractive workflows: populate only defensible fields]
[For generative workflows: execute the phase sequence, producing each section with reasoning]

Write output to `jobs/{slug}/builds/`.

---

### Step 8 — Document Assumptions and Gaps

Write to `jobs/{slug}/_system/run_log.md`:
- All populated items and their source references
- All flagged items and why
- All blanks and why
- All assumptions made
- All hard stops encountered

This entry is required. A run without it is not complete.

---

### Step 9 — Validate

Run the pre-flight checklist in `Instructions/Validation_and_Failure_Modes.md`. Check every item. Document any failures.

**Gate:** If validation fails at a fundamental level, do not deliver. Escalate to operator.

---

### Step 10 — Deliver

Produce:
1. `jobs/{slug}/builds/[deliverable]` — primary output
2. `jobs/{slug}/_system/run_log.md` — updated with this run's entry

State the validation result explicitly: **PASS** / **PASS WITH FLAGS** / **FAIL**.

---

## Escalation Contacts

| Condition | Contact | Method |
|---|---|---|
| [Hard stop type 1] | [Name / role] | [How] |
| [Hard stop type 2] | [Name / role] | [How] |

---

## Change Log

| Version | Date | Change | Reason |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | Initial version | [Context] |
