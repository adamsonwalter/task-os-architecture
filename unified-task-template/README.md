# Unified Task Template

**This is a meta-template. Do not run it directly. Do not fill it in.**

Copy this entire folder to create a new workflow. The copy becomes your runnable system.

---

## How This Works — The Three Layers

```
LAYER 1 — THIS TEMPLATE (keep one copy, never modify for a specific domain)
    ↓ copy entire folder, rename to your workflow name
LAYER 2 — A SPECIFIC WORKFLOW (e.g. optus-quote-system/, conversion-catalyst/, business-report-engine/)
    ↓ fill in Instructions, Reference, ontology, templates, SOP with domain content
    ↓ this is now a runnable system — point Claude at it
LAYER 3 — JOB INSTANCES (created inside a workflow when you have real work to do)
    ↓ copy jobs/.template/ to jobs/{slug}/, drop inputs into source-data/
    ↓ run the workflow, outputs appear in builds/, reasoning logged to _system/
```

**Analogy**: This template is the blank company structure. A workflow is a specific company. A job is a specific client engagement within that company.

---

## What You're Copying

```
unified-task-template/               ← THIS FOLDER (the meta-template)
├── README.md                        ← You are here (replace with your workflow's orientation)
├── SKILL.md                         ← AI orchestrator manifest (fill in triggers + execution pattern)
├── OS_Constitution.md               ← Governing philosophy (fill in your domain's principles)
├── HOW_TO_FORK.md                   ← This build guide (keep for reference or delete after build)
│
├── Instructions/                    ← THE RUNTIME BRAIN (always exactly 4 files)
│   ├── Domain_System.md             ← Rename to [YourDomain]_System.md — execution sequence
│   ├── Domain_Policy.md             ← Rename to [YourDomain]_Policy.md — operational firewall
│   ├── Output_Mapping.md            ← Output contract — every field defined
│   └── Validation_and_Failure_Modes.md  ← Pre-flight + domain failure patterns
│
├── docs/                            ← OPERATIONAL DOCUMENTATION
│   ├── sop_source.md                ← Write your step-by-step procedure here (canonical)
│   └── sop.html                     ← Generated from source — client-ready (run render_sop.py)
│
├── Reference/                       ← STATIC GROUNDING DATA (empty — fill with your domain's data)
│   └── README.md                    ← Document what you put here
│
├── ontology/                        ← DOMAIN KNOWLEDGE (optional — for generative workflows)
│                                       Empty unless your workflow reasons against JSON taxonomies
│
├── templates/                       ← OUTPUT PATTERNS (empty — fill with your output format specs)
│                                       Section structures, component patterns, golden templates
│
├── jobs/                            ← EXECUTION INSTANCES
│   └── .template/                   ← Job starter kit — copy this for each new engagement
│       ├── source-data/             ← Where input files go
│       ├── builds/                  ← Where outputs appear
│       └── _system/                 ← Machine metadata (job_spec.md, run_log.md)
│
├── Outputs/                         ← STANDALONE OUTPUTS (for quick runs without a full job)
│
└── scripts/
    └── render_sop.py                ← Renders sop_source.md → sop.html (works out of the box)
```

## Why Folders Are Empty

`templates/`, `ontology/`, `Reference/` (beyond its README), and `jobs/` are **intentionally empty**. They hold domain-specific content that only exists once you've instantiated a real workflow. If they had content, this wouldn't be a template — it would be a specific workflow pretending to be generic.

---

## After You've Built a Workflow — 30-Second Orientation

Once you've copied and filled in this template, your workflow's README should answer these questions:

| Question | Answer |
|---|---|
| Where are the instructions? | `Instructions/` — 4 files, always |
| Where is the reference data? | `Reference/` — static grounding the AI looks up, never invents |
| Where is the domain knowledge? | `ontology/` — structured JSON taxonomies (if applicable) |
| Where do inputs go? | `jobs/{slug}/source-data/` — one folder per engagement |
| Where do outputs go? | `jobs/{slug}/builds/` — machine-generated artefacts |
| What does the output look like? | `templates/` — output format specifications |
| How does it work step-by-step? | `docs/sop_source.md` — canonical, human-readable |
| How does it look for clients? | `docs/sop.html` — rendered from source, client-ready |
| What governs quality? | `OS_Constitution.md` — philosophy + hard limits |

---

## Deployment Modes

| Condition | Mode |
|---|---|
| You run it, low volume, high margin | **Mode 1** — Chat with system prompt |
| You run it, recurring, want audit trail | **Mode 2** — Claude Code / Cowork (this pattern) |
| Client runs it without you, or high volume | **Mode 3** — API application |

---

## Next Step

Read `HOW_TO_FORK.md` for the full build sequence, or jump straight to the 5-question protocol.
