---
name: [workflow-name]
description: [PLACEHOLDER — Write a description under 1024 characters. What this workflow does, what triggers it, what it produces. Be specific about input types, output types, and domain keywords that should activate this skill.]
---

# [WorkflowName] — Orchestrator Manifest

**Version**: 1.0.0
**Architecture**: [Value Equation State Machine / Validation-First Pipeline / Hybrid]

---

## Architecture

| Layer | File | Load When |
|-------|------|-----------|
| **Orchestrator** | `SKILL.md` (this) | Always |
| **System** | `Instructions/[Domain]_System.md` | First interaction |
| **Policy** | `Instructions/[Domain]_Policy.md` | Before any output |
| **Output Contract** | `Instructions/Output_Mapping.md` | Before populating output |
| **Validation** | `Instructions/Validation_and_Failure_Modes.md` | Before delivery |
| **SOP** | `docs/sop_source.md` | Workflow reference |
| **Reference** | `Reference/` | When looking up grounding data |
| **Ontology** | `ontology/` | When reasoning against domain taxonomies (if present) |
| **Templates** | `templates/` | When structuring output |

---

## Role

You are a **[Role Name]** who [one sentence describing what the AI does in this workflow].

**Prime Directive**: [The single most important rule, in one line.]

---

## Session Opening (Always)

1. **Identify the job**: Is there an active job in `jobs/`? If not, create one from `jobs/.template/`.
2. **Load source data**: Scan `jobs/{slug}/source-data/` for inputs.
3. **Pre-flight**: Validate inputs against the requirements in `Instructions/[Domain]_System.md`. If data is inadequate, HALT and request specific missing items.
4. **Check run history**: Read `jobs/{slug}/_system/run_log.md` if it exists. Resume intelligently.
5. **Proceed**: Execute the runtime sequence in `Instructions/[Domain]_System.md`.

---

## Execution Sequence

[NOTE: Choose ONE of the patterns below based on your workflow type, or combine them for hybrid workflows. Delete the one you don't use.]

### Pattern A — Extractive (reference-constrained)

```
LOAD → EXTRACT → CONTEXT → MAP TO REFERENCE → CLASSIFY → INSPECT FORMAT → POPULATE → DOCUMENT → VALIDATE → DELIVER
```

### Pattern B — Generative (reasoning-constructed)

```
PRE-FLIGHT → PHASE 1 → PHASE 2 → ... → PHASE N → COMPILE → VALIDATE → DELIVER
```

[For generative workflows, list the phases here with their protocol file references:]

| Phase | Protocol File | Purpose |
|-------|--------------|---------|
| 0 — Pre-flight | `Instructions/[Domain]_System.md` | Source validation |
| 1 — [Name] | [File if separate, or inline] | [What it produces] |
| ... | ... | ... |

---

## Quick Commands

| User Says | Action |
|-----------|--------|
| "[Trigger phrase 1]" | [What happens] |
| "[Trigger phrase 2]" | [What happens] |
| "Audit this" | Run `Instructions/Validation_and_Failure_Modes.md` against existing output |
| "Show SOP" | Reference `docs/sop_source.md` |

---

## Output Discipline

[NOTE: Customise this checklist to your domain. These are the final quality gates.]

- [ ] [Quality check 1]
- [ ] [Quality check 2]
- [ ] [Quality check 3]
- [ ] Validation checklist passed?
- [ ] Run log entry written?

---

*[Delete all `[NOTE:]` annotations and `[PLACEHOLDER]` text before going live.]*

**END OF ORCHESTRATOR MANIFEST**
