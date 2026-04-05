# Phase 0: Nano-Orchestration Protocol

**Purpose**: Strategic pre-flight and reason-led orchestration  
**Governing Rule**: No generation without validation.

---

## 1. Source-Data Audit (Pre-Flight)
Before proceeding to Phase 1, the LLM must validate the inputs in `/source-data`. 

### Validation Checklist:
1.  **Transformation Clarity**: Is the "Before → After" vivid enough?
2.  **Proof Assets**: Are there enough specific social proof signals (numbers, logos, case studies)?
3.  **Offer Definition**: Is the primary action (Step 1 of Hormozi) unambiguous?
4.  **Target Heuristics**: Do we know the awareness level (Problem vs. Solution Aware)?

**Response Logic**: If data is inadequate, the LLM must HALT and request specific missing "Ingredients" before starting the build.

---

## 2. Strategic Direction Selection
The Orchestrator must define 2-3 "Strategic Convergences" based on the brand's positioning.

| Archetype | Focus Lever | Tone/Direction |
|-----------|-------------|----------------|
| **The Speed-Demon** | Time Delay (Min) | Instant results, frictionless onboarding, fast-track success. |
| **The Rock-Solid** | Likelihood (Max) | Heavy trust signals, deep case studies, high-authority logic. |
| **The Visionary** | Dream Outcome (Max) | High-aspiration transformation, vivid future-state painting. |

---

## 3. Delta Reasoning Framework
For every landing page or variant generated, the LLM must provide a **Delta Reasoning Dashboard**.

### Schema:
*   **Strategic Vector**: [Which model was prioritized?]
*   **The "Delta"**: [What specific change was made to the copy vs. the other variant?]
*   **Hormozi Impact**: [How does this change the Value Equation calculation?]
*   **Conviction Level**: [How certain is the AI that this variant will outperform in a raw A/B test, and why?]

---

## 4. Multi-Page Orchestration Loop
1.  **Scan Source**: Evaluate assets in `jobs/{slug}/source-data/`.
2.  **Initialize `_system/`**: Create or update `job_spec.md`, `preflight_audit.md`, `run_log.md` before generation begins.
3.  **Declare Deltas**: "I will generate 3 pages: [A], [B], and [C]. Here is the logic for each..."
4.  **Execute Phases**: Run Protocols 01-07 for each branch. Output builds to `jobs/{slug}/builds/`.
5.  **Write Delta Reasoning**: Save `delta_reasoning.md` to `_system/` after all builds complete.
6.  **Append Run Log**: Add a new run entry to `run_log.md` with inputs, outputs, issues, and next-run triggers.

---

## 5. Job Container Convention

Every job lives under `jobs/{slug}/`. Source data, builds, and system metadata are co-located:

```
jobs/{slug}/
├── source-data/      ← bring your own (PDFs, images, briefs)
├── builds/           ← machine output (HTML, assets) — ephemeral
└── _system/          ← machine metadata — persistent
    ├── job_spec.md
    ├── preflight_audit.md
    ├── delta_reasoning.md
    └── run_log.md
```

**Rule**: Never write builds to the repo root `builds/` folder. Always use `jobs/{slug}/builds/`.  
**Rule**: The `_system/` folder is append-on-rerun — never overwrite `run_log.md`, only append.

---
**END PHASE 0 PROTOCOL**
