# {CLIENT_ENTITY} — AI workspace

This repository holds **repeatable AI workflows** for one business: instructions, reference data, and outputs—**not** a simulated ERP or departmental org chart.

## Layout

| Path | Role |
|------|------|
| `company/identity.md` | Who this business is, voice, boundaries |
| `company/strategy.md` | Current priorities and what you’re not doing |
| `company/knowledge/` | `client-history/`, `market-intel/`, `lessons/` — append-only intelligence |
| `_starters/` | Template kit to copy when adding a **new workflow folder** (Shape A or B) |
| `*/` (sibling folders) | One folder per workflow—e.g. reporting, quotes, marketing |

Add new capabilities by copying `_starters/shape-a-light/` or `shape-b-governed/` to the repo root, renaming, and following `_starters/README.md` (five questions).

## Meta-template source

Scaffolded from the OutcomesNow **task-os-architecture** meta-template. Update upstream docs there if the pattern evolves.
