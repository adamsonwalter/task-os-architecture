# [WorkflowName] — Governed Task Execution System

**Version:** 1.0
**Mode:** [Mode 2 — Claude Code / Cowork]
**Domain:** [What domain this operates in]

---

## What This Is

[One paragraph: what this system does, what input it takes, what output it produces.]

## 30-Second Orientation

| Question | Answer |
|---|---|
| Where are the instructions? | `Instructions/` — 4 files, always |
| Where is the reference data? | `Reference/` — static grounding the AI looks up, never invents |
| Where do inputs go? | `Inputs/` — job-specific source material |
| Where do outputs go? | `Output/` — generated artifacts (derivative files only) |
| What does the output look like? | `Golden_Templates/` — locked output format |
| How does it work step-by-step? | `docs/sop_source.md` → `docs/sop.html` |
| What governs quality? | `OS_Constitution.md` + `Instructions/Validation_and_Failure_Modes.md` |
| Practice context? | `../../company/identity.md` |

## Folder Rules

- `Inputs/`, `Reference/`, `Golden_Templates/` are **immutable** — never edit originals.
- `Output/` is the **only** location where derivative files are created.
- Every output run produces the deliverable AND an internal summary.

---

*[Replace all placeholder text before going live.]*
