# OutcomesNow — AI Operating Structure

**Meta-template.** This repository is a reusable pattern for designing and shipping **AI workflows**—not a single application. Use it to build repeatable, folder-based “task systems” that frontier models can execute from what’s present on disk, without a central orchestrator.

## Who this is for (three modes)

| Mode | What you’re building | Typical `company/` use |
|------|----------------------|-------------------------|
| **1. Your own workflows** | Experiments, demos, and internal repeatability—many parallel workflows to see what works | **OutcomesNow** `company/identity.md` + `strategy.md` + `knowledge/` |
| **2. Client workflows you run** | Engagements where you operate the workflow on their behalf (same repo or a copy per client) | Practice identity for *how you work*; per-client facts in `knowledge/client-history/` or a client-scoped pack inside the workflow |
| **3. Client workflows they run** | Handoff: the client (or their team) executes the workflow in Cursor, Claude, or similar | Often a **client-specific** identity/voice pack in the workflow folder; practice `company/` optional or referenced only for “delivery standards” |

Clients differ widely (e.g. mid-market industrial, accounting franchises, small-business consulting). The **shapes** stay the same; **reference data, gates, and voice** change per engagement.

### What you generate for a client (example)

A **client workspace** is usually a **flat or lightly grouped set of workflow folders**—each one a real capability: e.g. strategic business reports *for their* end-clients, specialised cashflow reports, marketing strategy packs, onboarding diagnostics—whatever matches **operations and thinking** needs. Workflows sit **next to each other** as siblings (and may use optional `jobs/` inside a workflow). This template does **not** imply a fabricated operating system: **no** pseudo **Chief of Staff** layer, **no** numbered department trees like `01_Human_Resources/` hanging under `company/` as if the repo were an org chart. The folder name **`company/`** here means **identity and knowledge for the practice (or a forked client identity)**—not “every department in the enterprise.”

**Exploration → production.** It’s normal to prototype in **Claude.ai Projects, Skills, Gems**, or ad hoc chats, then **promote** the winning pattern into a folder here (or a client repo) so it’s versioned, repeatable, and eventually **executable by the client** without re-inventing prompts each time.

---

Three layers. No orchestration. The model reads what's present.

```
task-os-architecture/
│
├── company/                          ← LAYER 1: IDENTITY & KNOWLEDGE (low cadence)
│   ├── identity.md                   ← Who we are, voice, positioning, trade-offs
│   ├── strategy.md                   ← Current priorities, quarterly theme
│   └── knowledge/                    ← Accumulated intelligence across all workflows
│       ├── client-history/
│       ├── market-intel/
│       └── lessons/
│
├── _starters/                        ← TEMPLATES (copy to create a new workflow)
│   ├── README.md                     ← Which shape to pick + the 5 questions
│   ├── shape-a-light/                ← Single-file orchestrator (generative workflows)
│   └── shape-b-governed/             ← Multi-file governed system (extractive workflows)
│
├── justine-sbr/                        ← LIVE WORKFLOW (Shape A)
├── gnd-quotes/                         ← LIVE WORKFLOW (Shape B)
├── manu-lp/                            ← LIVE WORKFLOW (Shape A + jobs layer — Manu landing pages)
│
└── unified-task-template/              ← ARCHIVE (full reference — superseded by _starters for new work)
```

## How It Works

**Layer 1 — `company/`** — Practice identity and knowledge surface. `identity.md` holds OutcomesNow positioning: completeness-gap framing, organised judgment, credentials, trade-off hierarchy, voice, and patterns to avoid. `strategy.md` is for your current quarterly theme and priorities. `knowledge/` holds `client-history/`, `market-intel/`, and `lessons/` for intelligence that compounds across workflows. **Nothing downstream writes here**—only you, on a deliberate cadence. Workflows **may** read this layer when the deliverable should sound like the practice or when you want one update to propagate; **client-native** workflows can instead anchor on files inside their workflow folder (see modes above).

**Layer 2 — Workflows** are self-contained task systems: a folder with SKILL.md (or equivalent instructions), reference data, and output conventions. **`_starters/`** supplies two shapes: **Shape A (light)** — minimal files, generative/hooks-style (e.g. Justine SBR pattern). **Shape B (governed)** — constitution, instruction files, validation, SOP source + rendered HTML, render script (e.g. GND pattern). See `_starters/README.md` for the “which shape?” table and the **five questions** before you build.

**Layer 3 — Jobs** (optional) are execution instances inside a workflow: `source-data/`, `builds/`, and reasoning metadata. Use when you need multiple runs or variants; many workflows never need this layer.

## Creating a New Workflow

1. Read `_starters/README.md` — decide Shape A or Shape B
2. Copy the shape folder to this level. Rename it.
3. Answer the 5 questions. Fill in the files.
4. Decide how context merges: reference `company/identity.md` and `knowledge/` where practice voice and shared intel apply; use workflow-local `references/` (or a client identity file) where the client’s voice and rules dominate—especially for mode **3**.
5. Run a trial with real input. Update validation based on what you observe.

## Fit for purpose (operator + client)

| Role | What “good” looks like |
|------|-------------------------|
| **You (operator)** | Fast to spin workflows, easy to copy `_starters/`, one place for practice truth (`company/`), per-client facts in `knowledge/client-history/`, no make-work folder tax. Prototype in Claude Skills/Projects; promote winners here. |
| **Client (user)** | They open **one workflow folder**, read `HOW_TO_USE` + `SKILL` (or constitution), drop inputs where told, get outputs where promised—no navigation through fake departments. If they **run** it themselves, instructions must be **self-contained** and voice anchored in **their** references when practice voice would confuse. |

This is **judgment infrastructure**, not SAP cosplay—see `company/README.md` (“Fit for purpose, not SAP theatre”).

## Operator playbooks

**New client workspace from the IDE:** say *“read the README and `BOOTSTRAP.md` — I need a new company instance”* and have the assistant run `scripts/scaffold_client_workspace.sh` after the interview in `BOOTSTRAP.md`. That creates a **new Git repo** with `company/`, `knowledge/`, `_starters/`, and a first commit—no fake org chart.

Use the same mechanical steps below when adding workflows; what changes is whether the **client workspace** already exists.

### A. New client **and** a new workflow

1. **Choose the home** — New **repo** per client (recommended for handoff and boundaries) or a **client-named folder** in your meta repo. Not a department tree—just a root for that relationship.
2. **Seed the client workspace** — Copy in `company/` (fork: client-specific `identity.md` / `strategy.md` if *they* are the “brand” in the folder), `_starters/`, and this `README`’s mental model—or clone from your template once you snapshot it.
3. **Record the relationship** — Add `company/knowledge/client-history/{client}.md` **in your practice repo** (or the client repo’s `company/knowledge/` if you keep knowledge there) with engagement facts, contacts, constraints, and what “good” means for them.
4. **Pick Shape A or B** — Use `_starters/README.md` (generative vs extractive / gates). Default to Shape A unless hard stops or golden templates demand Shape B.
5. **Spawn the workflow** — Copy `shape-a-light/` or `shape-b-governed/` to the **client workspace root**, rename to a **short folder name** (e.g. `cashflow-reports/`, `sbr-for-their-clients/`).
6. **Answer the five questions** — In the new folder; fill `SKILL.md` / instructions, `references/`, validation. Wire **either** `../../company/identity.md` (your practice) **or** client-local identity—see “Who this is for.”
7. **Trial** — Real inputs, log failure modes in the workflow, tighten validation. If you need repeat runs or variants, add `jobs/{job-name}/` under that workflow.
8. **Handoff (if they run it)** — Strip or relabel anything that assumes your machine; confirm paths; give one page “how to run this folder.”

### B. Existing client — **add** another workflow

1. **Open their existing workspace** — Same repo or folder as their other workflows; keep naming consistent (short, stable folder names).
2. **Refresh context** — Append to `client-history/{client}.md` if the engagement has new constraints, offerings, or people.
3. **Pick Shape A or B** — Same decision table; don’t default to Shape B just because the last workflow used it.
4. **Copy the starter again** — New sibling folder; new name. **Do not** duplicate the whole `company/` tree unless you’re forking identity for a new brand (rare).
5. **Answer the five questions for *this* capability only** — Triggers, reference data, prohibitions, output shape, silent-failure modes.
6. **Trial and tighten** — Same as above; add `jobs/` only when this workflow needs multiple parallel runs or builds.

## Design Principles

- **Context through presence, not orchestration.** No routing layer, no faux **Chief of Staff**, no departmental folder hierarchy standing in for an org chart. The model reads what's in the workflow folder.
- **Two shapes, not one universal template.** Generative workflows need hooks and voice. Extractive workflows need firewalls and validation. Don't force one into the other's shape.
- **The company layer is a knowledge surface, not a governance layer.** It provides context. It doesn't constrain execution.
- **Start with what works, add structure when you feel the pain.** Shape A is 5 files. Shape B is 12. If Shape A stops being adequate, promote governance files. Don't start governed.
- **Systems improve through use, not redesign.** Run logs and post-run observations feed back into instruction files. The self-improvement loop is the architecture's most valuable feature.
