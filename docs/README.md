# Docs (reference)

This folder holds **non-runtime** material: doctrine and design history that **informed** the meta-template in the repo root.

## Final design (canonical)

Day-to-day use of this repository is defined by:

- Root **`README.md`** — layers, operator playbooks, client workspace shape (flat workflows, no faux org chart)
- **`BOOTSTRAP.md`** — new client workspace scaffold
- **`company/README.md`** — practice / knowledge surface
- **`_starters/`** — Shape A and Shape B templates

If anything here **conflicts** with those files on **how to lay out a client repo**, prefer the root docs—they reflect the resolved “fit for purpose” design.

## `architecture/`

| File | Role |
|------|------|
| `Architectural_Constitution.md` | Governing doctrine: **Company Core → Task OS → Project Instance** (maps to `company/` → workflow folders → optional `jobs/`). Kept for audit, onboarding, and “why we didn’t build a monolithic company OS.” |
