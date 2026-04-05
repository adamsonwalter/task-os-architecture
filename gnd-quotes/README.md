# GND Quote Cowork

Minimal **Claude Cowork** workspace for **GND Optus civil / HDD quoting**.

## Layout

| Path | Purpose |
|------|---------|
| `Instructions/` | Constitution, SKILLs, ingestion, system prompt, SOP |
| `Reference/` | Master BOM/BOQ, rates, standards |
| `Inputs/` | Job PDFs per engagement |
| `Output/` | **Live** quotes and deliverables — two files per job (Internal Control + Submission Clean). If you see `.~lock.*` here, that is LibreOffice’s **lock sidecar** (created while an `.xlsx` is open), not the workbook; it is git-ignored. Commit the real `.xlsx` files when you want them versioned. |
| `Golden_Templates/` | **Example** xlsx shape / quality bar — copy from here, save work in `Output/` |
| `docs/` | Human-readable SOP (`sop.html`) — open in browser |

## Cowork

Link **this folder** as the project Context (no extra wrapper folder). Paste methodology or GND-specific instructions in the project **Instructions** field as needed.

## Relation to cowork-systems-architect

The [cowork-systems-architect](https://github.com/adamsonwalter/cowork-systems-architect) repo is a **general** Exec AI OS methodology — **not** copied into this folder. This project stays self-contained.
