# [Domain] System

## Purpose

[One sentence: what this file controls. Example: "Prepare defensible quotes from design packs." or "Generate high-converting landing pages from source material."]

This file is the main runtime instruction layer. It should be readable enough for a human and compact enough for a frontier model to load without unnecessary drift.

## Inputs

Typical inputs:
- [Input type 1 in `jobs/{slug}/source-data/`]
- [Input type 2]
- [Any supplementary material]

## Required Outputs

Typical outputs:
- [Primary deliverable]
- [Internal notes / summary]
- [Secondary deliverable if applicable]

## Runtime Sequence

[NOTE: For EXTRACTIVE workflows (quoting, reporting, compliance), write this as a linear step sequence with gates. For GENERATIVE workflows (landing pages, content, creative), write this as a phase sequence with state tracking. Both are valid. Choose based on whether the output is constrained by reference data or constructed through reasoning.]

### Extractive Pattern (reference-constrained)

1. Load the input and reconstruct the scope.
2. Extract structured data into a normalised internal list.
3. Identify contextual factors that affect classification.
4. Map supported items to reference data in `Reference/`.
5. Classify items: EXECUTE NOW / FLAG FOR REVIEW / HARD STOP / UNRESOLVED GAP.
6. Inspect the output format and confirm which fields can be populated.
7. Populate only defensible fields.
8. Generate internal notes for anything provisional, unresolved, or excluded.
9. Run validation before treating the output as usable.

### Generative Pattern (reasoning-constructed)

Phase 0 — **Pre-flight**: Validate source data. Halt if inadequate.
Phase 1 — **[Phase name]**: [What this phase produces]
Phase 2 — **[Phase name]**: [What this phase produces]
...
Phase N — **[Phase name]**: [What this phase produces]

Each phase outputs: [section/component] + [quality score or impact assessment]

[NOTE: Delete the pattern you don't use. If your workflow needs both (e.g. extract reference data THEN generate content from it), combine them: extractive steps first, then generative phases.]

## Core Rules

- [Hard rule 1 — domain-specific prohibition]
- [Hard rule 2]
- [Hard rule 3]
- Prefer a partial but trustworthy output over a complete but invented one.

## Canonical Workflow Source

The operational step sequence lives in `docs/sop_source.md`.
The rendered human-facing version lives in `docs/sop.html`.
If workflow steps change, update the source first and regenerate the HTML.

## When To Stop

Pause and hold for review when:
- [Condition 1]
- [Condition 2]
- [Condition 3]

---

*[Delete all `[NOTE:]` annotations and `[PLACEHOLDER]` text before going live.]*
