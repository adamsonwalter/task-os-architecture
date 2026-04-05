# HOW TO FORK: Build a New Workflow

Copy this entire `unified-task-template/` folder. Rename it to your workflow name. Follow the steps below.

---

## Worked Example: Building a Business Report Workflow

This shows the full lifecycle from template to running system to job execution.

### Step 1 — Copy and rename

```
cp -r unified-task-template/ business-report-engine/
```

You now have an identical copy with all the template files, empty folders, and placeholder text.

### Step 2 — Answer the 5 questions (see below), then fill in files

```
business-report-engine/
├── README.md                         ← Rewrite: "Generates $1950 business reports from survey data"
├── SKILL.md                          ← Fill in: triggers, role, execution sequence
├── OS_Constitution.md                ← Fill in: "never invent client data from the survey"
│
├── Instructions/
│   ├── Report_System.md              ← Renamed from Domain_System.md — 10-step report generation sequence
│   ├── Report_Policy.md              ← Renamed from Domain_Policy.md — section structure enforcement, tone rules
│   ├── Output_Mapping.md             ← Filled in: every report section, its source, its missing-data rule
│   └── Validation_and_Failure_Modes.md  ← Filled in AFTER first real trial run
│
├── docs/
│   ├── sop_source.md                 ← Filled in: "Step 1: Load survey. Step 2: Extract themes..."
│   └── sop.html                      ← Generated: python scripts/render_sop.py
│
├── Reference/                        ← NOW POPULATED:
│   ├── the_book_framework.md         ← Key concepts from the author's book
│   ├── style_constitution.md         ← Tone, vocabulary, structure rules
│   ├── report_section_requirements.md ← What each section must contain
│   └── README.md                     ← Updated: what each file is
│
├── ontology/                         ← STILL EMPTY (this workflow is extractive, no taxonomies needed)
│
├── templates/
│   └── report_section_spec.md        ← NOW POPULATED: exact section order, heading levels, length targets
│
├── jobs/                             ← STILL EMPTY (no client work yet)
│   └── .template/                    ← Ready to copy when a client engagement starts
│
└── scripts/
    └── render_sop.py                 ← Unchanged — works for any workflow
```

This is now a **runnable workflow**. Point Claude at this folder and it reads SKILL.md first.

### Step 3 — Run a real job

Client "Acme Corp" submits a survey. You create a job:

```
cp -r jobs/.template/ jobs/acme-corp/
```

Drop the survey into `jobs/acme-corp/source-data/acme_survey_results.pdf`.

Fill in `jobs/acme-corp/_system/job_spec.md`:
- Client: Acme Corp
- Input: Survey results (PDF)
- Objective: Full business report per section spec

Tell Claude: "Run the business report workflow for the acme-corp job."

Claude reads SKILL.md → loads Instructions → consults Reference → processes source-data → writes output to `jobs/acme-corp/builds/acme_report.docx` → logs reasoning to `jobs/acme-corp/_system/run_log.md`.

### Step 4 — Second client, same workflow

```
cp -r jobs/.template/ jobs/beta-industries/
```

Drop Beta's survey into source-data. Run again. The workflow is identical — only the input and output change. All your Reference data, Instructions, and validated failure modes carry forward.

---

## Before You Write Anything

Answer these 5 questions in plain language. Write them down. Do not start writing instruction files until you have all 5 answers.

### Q1 — What is the trigger and input?

What initiates this workflow? What does the input look like (structured form, document, transcript, spreadsheet, paste)? How is it delivered (file upload, folder drop, paste, API)?

*Your answer shapes `Instructions/[Domain]_System.md` and the `jobs/{slug}/source-data/` convention.*

### Q2 — What reference data grounds the output?

What must the AI look up rather than invent? Rate tables, regulatory documents, style guides, frameworks, terminology lists, historical examples, client data?

If a reference item is missing and the output fails silently — that item is load-bearing and needs a validation check.

*Your answer becomes the contents of `Reference/` and is cited in `Domain_Policy.md`.*

### Q3 — What can the AI NEVER do?

Write at least 5 domain-specific prohibitions. "Don't hallucinate" is insufficient — name the exact dangerous actions for your domain.

*Your answer becomes `Instructions/Domain_Policy.md`.*

### Q4 — What does the output look like exactly?

For every section or field: is it always present or conditional? What is its source basis? If source is missing: leave blank, flag, or hard stop? What is the exact format?

*Your answer becomes `Instructions/Output_Mapping.md` and shapes `templates/`.*

### Q5 — In what 5-6 ways can this fail silently?

Not crashes — outputs that look complete but aren't. What would a technically correct but actually dangerous output look like for this domain?

*Your answer becomes `Instructions/Validation_and_Failure_Modes.md` — but only AFTER a real trial run.*

---

## Build Sequence

| Step | Action | Produces |
|---|---|---|
| 1 | Copy `unified-task-template/` and rename it | Your workflow folder |
| 2 | Answer the 5 questions in plain language | Raw notes |
| 3 | Rename `Domain_System.md` and `Domain_Policy.md` to `[YourDomain]_System.md` etc. | Correct filenames |
| 4 | Write `OS_Constitution.md` | 1-2 pages: what this is, what it is not, what it will never do |
| 5 | Write the SOP as a step sequence | `docs/sop_source.md` |
| 6 | Render the SOP | `python scripts/render_sop.py` → `docs/sop.html` |
| 7 | Build the 4 instruction files in order: System → Policy → Output Mapping → Validation | `Instructions/` |
| 8 | Gather the reference data | `Reference/` |
| 9 | Build the output template or specification | `templates/` |
| 10 | (Optional) Build ontology JSON if the workflow reasons against taxonomies | `ontology/` |
| 11 | Write the SKILL.md orchestrator manifest | `SKILL.md` |
| 12 | Rewrite README.md for your specific workflow | `README.md` |
| 13 | Run a trial with REAL input (not synthetic) | First output + observations |
| 14 | Update Validation_and_Failure_Modes.md with what you found | Final validation file |

---

## Workflow Type Decision

Your workflow is one of three types. This affects how you write `Instructions/[Domain]_System.md`:

| Type | Characteristics | System.md Pattern | Example |
|---|---|---|---|
| **Extractive** | Input mapped to constrained output via reference data. AI must not invent. | Linear step sequence with gates and classification. | Quote OS, compliance checks |
| **Generative** | Input feeds a creative/analytical process. AI constructs the output through reasoning. | Numbered phase sequence with state tracking and quality scores. | Conversion Catalyst, content generation |
| **Hybrid** | Extractive grounding phase, then generative construction phase. | Steps 1-5 extractive, then phases for generation. | Business reports (extract survey data, then generate narrative) |

---

## Deployment Mode

| Condition | Mode |
|---|---|
| You run it, low volume, high margin | **Mode 1** — Chat with system prompt |
| You run it, recurring, want improvement over time | **Mode 2** — Claude Code / Cowork (this pattern) |
| Client runs it without you, or high volume | **Mode 3** — API application |

---

## New Job Checklist (once your workflow is built)

To start a new job (engagement) within an existing workflow:

1. Copy `jobs/.template/` to `jobs/{new-slug}/`
2. Drop input files into `jobs/{new-slug}/source-data/`
3. Fill in `jobs/{new-slug}/_system/job_spec.md`
4. Run the workflow — it reads source-data, writes to builds, logs to _system
5. Review output. Update run_log.md if the AI didn't.

---

## The Self-Improvement Rule

Every run that produces output must also produce a run log entry. After every 3-5 runs, review the logs. Recurring patterns become amendments to the instruction files.

**This is how the system gets better. Not by rewriting it — by reading its own output.**

---

## SOP as Client Deliverable

The rendered `docs/sop.html` serves two purposes:

1. **Client communication**: Open in a browser, print, or share. It explains what the system does in a format clients trust.
2. **Handover artefact**: Part of the delivery package when building workflows for customers.

To regenerate after editing `sop_source.md`:
```
python scripts/render_sop.py
```

The source is always canonical. The HTML is always generated. Changes flow source → HTML, never the reverse.
