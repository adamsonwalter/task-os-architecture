# Architectural Constitution

## Purpose

This document defines the preferred architecture for an AI-enabled business operating system.

It is not a runtime prompt.
It is not a task SOP.
It is not a client workflow.

It is a governing doctrine for how to structure the overall system so that:
- shared company context is stable
- task execution remains legible
- project work is runnable
- frontier models can operate effectively without drowning in irrelevant context

It should be strong enough to guide an OS Orchestrator AI that is asked to:
- set up a new implementation
- audit an existing implementation
- reduce unnecessary complexity
- correct folder drift
- restore canonical structure

## Core Decision

The preferred architecture is:

1. `Company Core`
2. `Task OS`
3. `Project Instance`

This is the default pattern.

Do not default to:
- a giant monolithic company OS that tries to contain all work directly
- a pile of unrelated project folders with duplicated logic and no shared canon

The system should be platform, application, runtime:

- `Company Core` = platform
- `Task OS` = application
- `Project Instance` = runtime

## Why This Decision Was Made

Two extremes both fail in practice.

### Pure Company OS Failure Mode

A fully centralized “company AI OS” tends to become:
- too broad
- too abstract
- too context-heavy
- too hard to navigate
- too slow to change safely

It often turns into architecture theatre: elegant in theory, poor in execution.

### Pure Project Pack Failure Mode

A purely project-based approach tends to become:
- repetitive
- drift-prone
- unclear about what is canonical
- expensive to maintain across many similar workflows

It works well locally, but weakens at scale unless disciplined.

### Chosen Resolution

Use a thin shared core plus small task operating systems plus live project instances.

This preserves:
- reuse
- legibility
- update control
- operational focus
- compatibility with frontier-model reasoning

## Architectural Layers

### 1. Company Core

The Company Core is thin.

It should contain only what is genuinely cross-cutting and stable.

Typical contents:
- company profile
- brand voice
- mission / positioning
- common policies
- shared naming conventions
- shared validation principles
- shared tool access conventions
- common memory rules

The Company Core must not become a dumping ground for every idea.

A rule belongs in Company Core only if:
- it applies across multiple task systems
- it is stable enough to be canonical
- centralizing it reduces drift more than it increases complexity

### 2. Task OS

The Task OS is the main operating unit.

Examples:
- Quote OS
- Content OS
- Course Launch OS
- Sales Follow-up OS
- Compliance Review OS

Each Task OS should be:
- small
- legible
- independently runnable
- independently testable
- understandable in minutes by a new human or AI collaborator

Each Task OS should define:
- its purpose
- its canonical workflow source
- its task-specific policies
- its output contract
- its validators / failure checks
- its references
- its templates

The Task OS is where real operational logic should live.

### 3. Project Instance

A Project Instance is a live run of a Task OS against specific inputs.

Typical contents:
- job inputs
- current working notes
- generated outputs
- project-specific overrides
- review comments

A Project Instance should not redefine the whole task system.
It should consume the Task OS.

## Canonicality Rules

Every meaningful layer must have a clear source of truth.

### Workflow Canonicality

If a mini-SOP contains the operational steps, it is a first-class artifact.

Preferred pattern:
- one canonical workflow source
- one rendered human-facing HTML mini-SOP

Example:
- `mini_sop_source.md` is canonical
- `sop.html` is rendered

Do not maintain two manually edited operational SOPs as co-equal truths.

### Policy Canonicality

Permanent business rules must live in policy files, not in scattered examples or duplicated prompts.

### Reference Canonicality

Client-specific terms, workbook mappings, and rate references should live in compact reference files or templates, not in broad narrative documents.

### Validation Canonicality

If something can be checked after generation, prefer putting it in validation rather than in long prose instructions.

## Design Heuristic

For each instruction or file, ask:

1. Is this a permanent business rule?
Keep it in policy.

2. Is this client-specific vocabulary, mapping, or template logic?
Keep it in reference or template files.

3. Is this just telling the model how to think step by step?
Compress or remove it unless it is genuinely necessary.

4. Could this be checked automatically after generation?
Move it into validation instead of prompt prose.

This heuristic is mandatory for architecture review.

## Preferred Repo Shape

### Company Core

The exact names may vary, but the shape should stay thin and obvious.

Example:
- `README.md`
- `00_Governance/`
- `01_Shared_Context/`
- `Shared_Validators/`
- `Shared_Templates/`

### Task OS

A Task OS should usually resemble:
- `README.md`
- `Instructions/`
- `docs/`
- `Reference/`
- `Inputs/`
- `Golden_Templates/`
- `Output/`
- `scripts/`

The task repo should answer quickly:
- where are the instructions?
- where are the references?
- where do inputs go?
- where do outputs go?
- what is canonical?

### Project Instance

A project folder should be even simpler:
- `Inputs/`
- `Output/`
- `Notes/` or equivalent
- optional local overrides

## File Count Discipline

Do not multiply files unless the split improves runtime clarity.

Over-fragmentation is a real failure mode.

Warning signs:
- charter, constitution, runtime modes, human operations, sync protocol, migration plan, and reduction notes all coexisting in one task repo
- multiple files describing the same workflow from different angles
- architecture files outnumbering runtime files

When this happens, compress.

## Frontier Model Principle

Frontier models benefit from structure, but not from clutter.

They work best when given:
- a small number of strong canonical files
- explicit policy boundaries
- compact reference files
- clear output contracts
- validators
- examples or gold tests when useful

They do not materially benefit from:
- excessive folder ideology
- theatrical org charts
- duplicated instruction sets
- too many overlapping doctrine files

## View On Company OS vs Task OS

The company-level OS should be thin.
The task-level OS should do the real operational work.

Therefore:
- `Company OS` is the platform
- `Task OS` is the application
- `Project Instance` is the runtime

This is the preferred architecture unless a strong reason exists to deviate.

## OS Orchestrator AI Mandate

An OS Orchestrator AI responsible for setting up or correcting an implementation should:

1. Identify the Company Core.
2. Verify that the Company Core is thin.
3. Identify the Task OS units.
4. Verify that each Task OS is independently legible and runnable.
5. Identify Project Instances.
6. Verify that projects consume task logic rather than redefining it.
7. Identify canonical workflow sources.
8. Identify rendered or derived artifacts.
9. Identify reference files, templates, and validators.
10. Remove duplication and compress unnecessary layers.

It should optimize for:
- clarity
- maintainability
- reproducibility
- low cognitive load
- strong canonicality

It should not optimize for:
- conceptual grandeur
- maximum number of agents
- folder symmetry for its own sake
- unnecessary decomposition

## Audit Procedure

When auditing a folder that claims to implement the full system, check:

### A. Layer Integrity
- Is there a thin Company Core?
- Are there separate Task OS units?
- Are there live Project Instances?

### B. Canonicality
- Is there one clear source for workflow logic?
- Are rendered artifacts clearly derived?
- Are policy and reference separated?

### C. Runtime Legibility
- Can a new collaborator identify the important files in minutes?
- Is it obvious where to put inputs and find outputs?
- Is the folder structure operational rather than theoretical?

### D. Drift And Duplication
- Are the same rules duplicated across multiple task repos?
- Are there multiple conflicting SOPs?
- Are architecture notes being mistaken for runtime instructions?

### E. Validation
- Are key failure checks explicit?
- Are known failure modes documented where useful?
- Is correctness being enforced by validation where possible?

## Correction Rules

If an implementation is too monolithic:
- carve out Task OS units
- reduce Company Core to true shared context

If an implementation is too duplicated:
- centralize true shared rules into Company Core
- keep task-specific logic local

If a task repo is too fragmented:
- merge overlapping doctrine files
- reduce to a small canonical runtime set

If a task repo is too vague:
- add a clearer workflow source
- add a clearer output contract
- add validation rules

If HTML and Markdown workflows drift:
- restore one canonical source
- regenerate the rendered artifact

## HTML Mini-SOP Rule

An HTML mini-SOP is not merely decorative if it contains the real steps.

Treat it as an operational artifact.
But unless there is a strong reason otherwise, keep a simpler canonical source underneath it.

Preferred model:
- source file is canonical
- HTML is rendered
- live client feedback updates the source first

## Compression Rule

A mature implementation should tend toward fewer, stronger files.

Early design may require more notes.
Production systems should compress once the architecture is understood.

If a document explains something that is already obvious from the live structure, archive or merge it.

## Success Criteria

The architecture is successful when:
- the Company Core is thin and durable
- Task OS repos are clear and runnable
- Project Instances are easy to execute
- the canonical workflow source is obvious
- rendered SOPs stay synchronized
- shared rules do not drift
- frontier models can run workflows without drowning in noise
- humans can understand the system without reverse-engineering it

## Final Doctrine

Build small, strong Task OSs on top of a thin shared Company Core.
Run live work through Project Instances.
Keep canonical sources explicit.
Render human-facing artifacts from them.
Move checkable concerns into validation.
Compress relentlessly once the design is proven.
