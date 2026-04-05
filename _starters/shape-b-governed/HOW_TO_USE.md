# Shape B — Governed Workflow

Multi-file system with constitution, policy firewalls, and validation gates. Best for extractive workflows where the AI maps inputs to constrained outputs and must never fabricate.

## When to Use This Shape

- The AI extracts and maps data rather than generating creative content
- There are commercial hard stops — things the AI must absolutely never do
- Output format is locked to a template (spreadsheet, structured document)
- Multiple human review gates before delivery
- Audit trail matters — you need to know what was decided and why
- Examples: GND Quotes, compliance workflows, regulated reporting, financial modelling

## Folder Structure

```
[workflow-name]/
├── README.md                         ← 30-second orientation for anyone opening this folder
├── OS_Constitution.md                ← Governing philosophy and hard limits
│
├── Instructions/                     ← THE RUNTIME BRAIN (always exactly 4 files)
│   ├── [Domain]_System.md            ← Execution sequence — the step-by-step
│   ├── [Domain]_Policy.md            ← Operational firewall — what may never happen
│   ├── Output_Mapping.md             ← Output contract — every field defined
│   └── Validation_and_Failure_Modes.md  ← Pre-flight + domain failure patterns
│
├── Reference/                        ← STATIC GROUNDING DATA (AI looks up, never invents)
│   ├── [reference files]
│   └── README.md
│
├── Golden_Templates/                 ← LOCKED OUTPUT FORMAT (the exact shape of the deliverable)
│
├── Inputs/                           ← JOB-SPECIFIC INPUT (PDFs, spreadsheets, briefs)
│
├── Output/                           ← GENERATED ARTIFACTS (derivative files only)
│
├── docs/                             ← OPERATIONAL DOCUMENTATION
│   ├── sop_source.md                 ← Canonical step sequence (single source of truth)
│   └── sop.html                      ← Client-ready rendered version
│
└── scripts/
    └── render_sop.py                 ← Renders sop_source.md → sop.html
```

## Build Steps

1. Copy this folder. Rename it to your workflow name.
2. Answer the 5 questions from `../_starters/README.md`.
3. Write `OS_Constitution.md` — what this system is, is not, and will never do.
4. Write `docs/sop_source.md` — the step-by-step procedure. Run `python scripts/render_sop.py` to generate the client-facing HTML.
5. Build the 4 instruction files **in order**: System → Policy → Output Mapping → Validation. Each references the previous.
6. Gather reference data into `Reference/`. Document each file in `Reference/README.md`.
7. Build or place the golden template in `Golden_Templates/`.
8. Write `README.md` — the 30-second orientation for this specific workflow.
9. Run a trial with REAL input. Not synthetic.
10. Update `Validation_and_Failure_Modes.md` with what you actually observed.

## Input Handling

Shape B uses flat `Inputs/` and `Output/` folders — one job at a time. For each new job:
1. Clear or archive previous files in `Inputs/` and `Output/`
2. Drop the new input into `Inputs/`
3. Run the workflow
4. Output appears in `Output/`

If you need to track multiple concurrent jobs, add the jobs layer:
```
jobs/{slug}/source-data/   ← input
jobs/{slug}/builds/        ← output
jobs/{slug}/_system/       ← metadata
```

Most Shape B workflows don't need this. GND runs one quote at a time.

## Company Context

Reference the company layer in your constitution or system prompt:
```
For practice-level voice and positioning, read ../../company/identity.md
```

## SOP as Client Deliverable

The rendered `docs/sop.html` is a client-facing explanation of the workflow. Open in a browser, print, or include in a handover package. To regenerate after edits:

```bash
python scripts/render_sop.py
```

Source is always canonical. HTML is always generated. Changes flow source → HTML, never the reverse.
