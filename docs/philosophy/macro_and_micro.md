# Macro scale (Task OS) and micro scale (folder execution)

This note is **doctrine**, not a product integration. It keeps **nomenclature and intent** aligned between:

- **Macro** — how this repo structures **practice-level** work: thin company context, self-contained workflows, optional job instances (see root `README.md` and `docs/architecture/Architectural_Constitution.md`).
- **Micro** — how a **single folder** can later hold tight **governance + execution** for one capability (constitution-style rules, stepwise procedures, human-readable summary, closure artifacts)—without requiring clients to learn a second “operating system” on day one.

## Why two scales exist

Clients and operators should be able to adopt **only the macro** template (workflows + `company/`) and succeed. A **micro** layer is **optional** and usually comes **after** a workflow is proven: when you want deterministic runs, explicit handoffs, and receipts **inside one directory** without deepening folder trees for the sake of structure.

Cognitive load is real. **Do not** ask a client to take on a micro folder standard until they are ready; the macro layout already delivers repeatable task systems.

## Shared philosophy (no stack requirement)

| Idea | Macro expression (this repo) | Micro expression (typical pattern) |
|------|------------------------------|-------------------------------------|
| **Truth vs cache** | Canonical workflow / policy files; validators | Folder constitution vs disposable discovery maps |
| **Presence, not orchestration** | Model reads the workflow folder | Model reads `FILEAGENTS`-style + `AGENTS`-style files **in place** |
| **Human vs machine instructions** | Shape B: instructions vs rendered human SOP | Dense execution markdown vs browser summary (no prompts in the human view) |
| **Closure** | Gates, validation, job outputs | Receipt / friction log / self-healing edits to procedures |
| **Flat discipline** | Avoid fake org charts; short folder names | Flat primitives and naming over deep `Input/Process/Output/` trees when context is tight |

The micro column intentionally uses **generic** language. A public **folder-native** spec may implement these ideas with specific filenames and levels; that is **one** reference, not a dependency for OutcomesNow clients.

## For operators

When **you** are ready to apply a micro layer on top of an existing workflow folder, treat it as **SAP at the folder level**: same honesty about batch truth, moves, and staleness as at vault scale—just scoped to one tree you control. Clients only need what you choose to expose in their handoff pack.
