# Manu LP v1.3.0

**Manu landing pages** — folder: `manu-lp/`  
**Orchestrator Architecture**: Value Equation State Machine  
**Governing Logic**: Value = (Dream Outcome × Perceived Likelihood) ÷ (Time Delay × Effort)  
**Primary Goal**: Transforming raw operational data into high-converting, system-led landing pages.

---

## 1. System Overview
Manu LP is an AI-orchestrated landing page architect. It operates as a deterministic engine that maximizes conversion by manipulating the four variables of the **Hormozi Value Equation**. Unlike generic copy generators, this system treats a landing page as a "Certainty Engine" for B2B operations.

### Nodes & Flows (The Systems Model)
*   **Source Data (Nodes)**: Raw assets (PDFs, images, briefs) located in `/source-data`.
*   **Protocols (Flows)**: A 7-phase transformation sequence that converts raw data into optimized section copy.
*   **State Machine**: The `protocols/state_engine.md` tracks session context and "Value Score" throughout the build.

---

## 2. The 7-Phase Execution Protocol
Every landing page generated follows this strict architectural sequence:

1.  **Nano-Orchestration (Phase 0)**: Strategic pre-flight, source-data validation, and "Delta Reasoning" for multi-variant generation.
2.  **Hero Forge (Phase 1)**: Above-the-fold headline + subhead designed to stop the scroll and trigger the primary action.
2.  **Value Architect (Phase 2)**: Structural mapping of the core value proposition.
3.  **Trust Constructor (Phase 3)**: Integration of high-fidelity social proof and trust signals.
4.  **Benefit Transformer (Phase 4)**: Outcome-led feature mapping.
5.  **Objection Crusher (Phase 5)**: FAQ and friction-reduction handling.
6.  **CTA Optimizer (Phase 6)**: Strategic placement of action triggers.
7.  **Final Accelerator (Phase 7)**: Urgency and scarcity induction to close the conversion loop.

---

## 3. Technical Standards

### Image & Media Preference
To minimize **Time Delay (↓)** and maximize page speed, the following standards are preferred:
*   **WebP / Optimized JPEG**: Preferred for hero images and product visuals to maintain performance.
*   **SVG**: The required "Gold Standard" for logos and icons to ensure crisp scaling with zero load penalty.
*   **PNG**: Use only when transparency is mandatory.

### Visual Aesthetic
Landing pages must be premium, professional, and mobile-responsive by default. Avoid generic stock photography; favor "Transformation Visuals" (Before/After or product UI) that enhance **Perceived Likelihood (↑)**.

---

## 4. Repository Structure
*   `source-data/`: Raw brand/category assets and input files.
*   `protocols/`: Step-by-step logic gates for each phase of page construction.
*   `ontology/`: JSON taxonomies for conversion archetypes, trust signals, and psychological hooks.
*   `scripts/`: Automation tools, including `wireframe_generator.py`.
*   `templates/`: UI component patterns and section specifications.
*   `standards/`: Explicit rules for output formatting and conversion benchmarks.
*   `jobs/`: **Variable data layer** — one folder per engagement (see Job Container below).

---

## 5. Job Container Architecture

Each engagement is a **self-contained, portable job folder** under `jobs/`. The job folder is the unit of work — drop it in to activate, delete it to remove, zip it to share.

```
jobs/
└── {job-slug}/
    ├── source-data/      raw inputs (PDFs, images, briefs)
    ├── builds/           generated HTML outputs (ephemeral)
    └── _system/          machine-generated metadata
        ├── job_spec.md       product, audience, vectors
        ├── preflight_audit.md  nano-orchestrator pre-flight results
        ├── delta_reasoning.md  strategic delta analysis per build
        └── run_log.md        append-only history of all runs
```

**Invariant layer** (never changes between jobs): `protocols/`, `ontology/`, `standards/`, `templates/`, `SKILL.md`  
**Variable layer** (everything job-specific): `jobs/{slug}/`

The `_system/` folder is machine-written and human-readable. It preserves full reasoning provenance across re-runs, so a future session can read the run log and resume intelligently without re-deriving context.


---

## 5. Quick Commands
*   **"Build landing page for [product]"**: Initiates the full 7-phase sequence.
*   **"Audit this page"**: Triggers the Audit Protocol against the Hormozi Value Equation.
*   **"Wireframe this"**: Runs the ASCII wireframe generator for visual layout.

---

## 6. Strategic Intent
The core differentiator of this system is its focus on **"Operational systems that run on AI."** We build for the mid-market B2B owner who values single sources of truth, zero version drift, and systems that survive model changes.

> "Clarity converts. Complexity kills."

---
*Created by Walter Adamson • Manu LP v1.0.0*
