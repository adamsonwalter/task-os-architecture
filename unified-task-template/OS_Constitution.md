# [WorkflowName] Constitution

## What Is Going On Here

[2-3 sentences: why this system exists and what problem it solves. Not marketing — the honest reason.]

## Governing Principles

1. **Prefer legibility over taxonomic perfection.** If a simpler structure communicates the same information, use the simpler structure.

2. **One canonical source per concern.** Workflow steps live in `sop_source.md`. Policy lives in `Policy.md`. Output shape lives in `Output_Mapping.md`. No duplication across files.

3. **Validation before generation.** The system checks what it knows before producing anything. Gaps are stated, not filled with invention.

4. **Incompleteness over fabrication.** A partial but trustworthy output is always preferred over a complete but invented one. [Adapt this to your domain: "partial but defensible quote," "flagged but honest report," etc.]

5. **The instruction layer is always exactly 4 files.** System, Policy, Output Mapping, Validation. Adding a fifth file is a signal that one of the four needs restructuring, not that the architecture needs expanding.

6. **Jobs are self-contained.** Everything needed to understand a job's inputs, outputs, and reasoning lives inside `jobs/{slug}/`. Deleting a job folder has zero impact on the system.

7. **The system improves through use, not redesign.** Run summaries feed back into Policy and Validation files. After 3-5 real runs, patterns emerge. Those patterns sharpen the instruction layer.

## What This System Is Not

- Not a philosophically complete operating system. It is a [domain] workflow that works in practice.
- Not a replacement for human judgement at decision points. Gates exist to pause and escalate, not to bypass the operator.
- Not a static artefact. It improves with each real run and should be treated as living documentation.

## Anti-Goals

[List 3-5 things this system explicitly does NOT try to do. Be specific to your domain.]

- [Anti-goal 1]
- [Anti-goal 2]
- [Anti-goal 3]

---

*[Delete all `[PLACEHOLDER]` text before going live.]*
