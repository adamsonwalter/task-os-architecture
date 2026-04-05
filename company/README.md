# Company Layer — OutcomesNow

This folder is the stable knowledge surface for **OutcomesNow** (your practice). It is part of the **meta-template**: workflows you build for **your** exploration, for **clients you run**, or for **clients who run** their own copies may each use this layer differently—see the root `README.md` (“Who this is for”).

Workflows **can** read from here when shared positioning, voice, or cross-client intel should apply. Workflows that are **wholly client-branded** may rely instead on identity and reference files inside the workflow folder; that avoids forcing practice voice into client-owned execution.

Nothing writes here except you, on a deliberate cadence.

**Fit for purpose, not SAP theatre.** This layer is **not** simulating SAP or hanging a fake org chart under `company/`. OutcomesNow builds **small, inspectable, composable** workflows—organised judgment for real operations and thinking—not a monolithic ERP shell. The principal has worked at the **large-systems** end of town (including SAP-era production planning in Australia—e.g. steel-industry scale work whose methods later folded into the product line). That background is **why** this stays **light**: you know what the big end is for; **this** template is for repeatable AI execution without the cost or pretence of a client-side “mini-SAP.”

## Contents

| File | Purpose | Update Cadence |
|---|---|---|
| `identity.md` | Who we are, how we work, voice, positioning, trade-offs | Quarterly or on positioning shift |
| `strategy.md` | Current priorities, quarterly theme, what we're saying no to | Quarterly |
| `knowledge/` | Accumulated intelligence that crosses workflow boundaries | Ongoing |

## Knowledge Subfolders

| Folder | What Goes Here |
|---|---|
| `knowledge/client-history/` | Per-client context files (engagement history, preferences, outcomes) |
| `knowledge/market-intel/` | Market observations, competitor patterns, pricing intelligence |
| `knowledge/lessons/` | Cross-workflow learnings — failures, patterns, things that worked |

## Live workflow folders (canonical names)

These directories sit next to `company/` at the repo root. Names are short and stable; product titles inside each folder can be longer.

| Folder | Role |
|--------|------|
| `justine-sbr/` | Strategic Business Reviews (Shape A) |
| `gnd-quotes/` | GND Quote Cowork — Optus fibre civil quoting (Shape B) |
| `manu-lp/` | Manu landing pages — Hormozi-style LP builds, optional jobs layer (Shape A + jobs) |

## How Downstream Workflows Use This

When a workflow **does** use this layer, the model reads `identity.md` for practice voice and positioning, `strategy.md` for current priorities, and `knowledge/client-history/{client}.md` (or files under `market-intel/` and `lessons/`) for engagement and accumulated intelligence. **Compounding:** update `identity.md` or add a knowledge file once; every workflow that references those paths inherits the change—no duplication across folders.

No orchestration layer routes anything. The context is present if you point the SKILL or constitution at it. Frontier models use what’s loaded and what’s relevant.

## Rules

1. This folder is read-only for all downstream workflows.
2. Only Walter updates these files.
3. Knowledge entries are append-friendly — add new files, don't restructure old ones.
