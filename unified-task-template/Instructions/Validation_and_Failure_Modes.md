# Validation and Failure Modes

## Purpose

This file is the pre-flight system. It defines what must be true before the output is considered usable, and catalogues the domain-specific ways this workflow can fail silently.

**Standing Rule (non-negotiable)**: State failures explicitly. Preserve uncertainty in structure. Prefer incompleteness over invention.

## Pre-Flight Checklist

Run this checklist against every output before delivery. Every item must pass.

- [ ] All required sections/fields are present (populated, flagged, or explicitly blank)
- [ ] No field is populated without a traceable source
- [ ] No reference data was fabricated or assumed
- [ ] Output format matches the contract in `Output_Mapping.md`
- [ ] Internal-only content does not appear in client-facing output
- [ ] Run summary is written to `_system/run_log.md`
- [ ] [DOMAIN-SPECIFIC CHECK 1]
- [ ] [DOMAIN-SPECIFIC CHECK 2]
- [ ] [DOMAIN-SPECIFIC CHECK 3]

## Named Failure Modes

[NOTE: This section MUST be written after a real trial run, not theoretically. Run the workflow with real input, observe where it fails or deviates, and document those patterns here. The examples below are structural prompts — replace them with your actual observed failures.]

### FM-1: [Name this failure]

**What happens**: [Describe the silent failure — the output looks correct but isn't]
**How to detect**: [What to look for in the output or run log]
**Response rule**: [What to do when detected]

### FM-2: [Name this failure]

**What happens**: [Description]
**How to detect**: [Detection method]
**Response rule**: [Response]

### FM-3: [Name this failure]

**What happens**: [Description]
**How to detect**: [Detection method]
**Response rule**: [Response]

### FM-4: [Name this failure]

**What happens**: [Description]
**How to detect**: [Detection method]
**Response rule**: [Response]

### FM-5: [Name this failure]

**What happens**: [Description]
**How to detect**: [Detection method]
**Response rule**: [Response]

## Failure Mode Discovery Prompts

Use these questions after each real run to discover new failure modes:

1. What would a *technically complete but actually dangerous* output look like for this domain?
2. What gets skipped under time pressure?
3. What does the AI invent when the reference data is ambiguous?
4. What format violation would a human reviewer miss on first read?
5. Did the AI silently drop any input elements?

## Post-Run Validation Loop

After every 3-5 real runs, review the run summaries in `jobs/*/_system/run_log.md`. Recurring patterns become amendments to:
- This file (new failure modes)
- `Domain_Policy.md` (new prohibitions or escalation triggers)
- `Reference/` (new or corrected grounding data)

**This is how the system gets better. Not by rewriting the architecture — by reading its own output.**

---

*[Delete all `[NOTE:]` annotations and `[PLACEHOLDER]` text before going live. FM entries MUST be replaced with real observations after trial runs.]*
