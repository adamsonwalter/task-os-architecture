# Shape A — Light Workflow

Single-file orchestrator. Best for generative workflows where the AI constructs output through reasoning within voice and framework rules.

## When to Use This Shape

- The AI generates content (reports, pages, copy, analysis) rather than extracting and mapping data
- There are no commercial hard stops or margin firewalls
- Output structure is flexible, not locked to a template
- One or two human review passes, not multiple gates
- Examples: Justine SBR, Conversion Catalyst, content generation, diagnostic reports

## Folder Structure

```
[workflow-name]/
├── SKILL.md              ← The entire system. Hooks, voice, quality gates, everything.
├── references/           ← Grounding material the AI reads (voice guides, frameworks, examples)
├── config/               ← Settings (document formatting, client details, etc.)
├── scripts/              ← Deterministic operations (docx generation, validation, rendering)
└── output/               ← Generated deliverables
```

That's it. Five locations. One instruction file.

## Build Steps

1. Copy this folder. Rename it to your workflow name.
2. Answer the 5 questions from `../_starters/README.md`.
3. Write SKILL.md — put everything in one file. Hooks execute in sequence.
4. Create reference files — voice guide, frameworks, examples, templates.
5. (Optional) Add config JSON for settings that change per client.
6. (Optional) Add scripts for deterministic ops (docx generation, validation).
7. Run a trial with real input. Update quality gates based on what you observe.

## Adding a Jobs Layer (Optional)

If your workflow runs multiple variants or clients in parallel (like Conversion Catalyst's landing pages), add:

```
jobs/
└── {slug}/
    ├── source-data/     ← Input for this specific job
    ├── builds/          ← Output for this job
    └── _system/         ← Job spec, run log, reasoning
```

Most Shape A workflows don't need this. The Justine SBR runs one client at a time — survey in, report out.

## Company Context

Reference the company layer in your SKILL.md:
```
Read `../../company/identity.md` for practice voice and positioning.
```

This gives every workflow access to the stable identity without duplicating it.
