---
name: GND_SOP
version: 1.0 | Mar 2026
purpose: >
  Human-facing Standard Operating Procedure for GND Optus civil quoting.
  Governs the manual steps that surround, gate, and verify the AI system's
  outputs. Covers RC4 data integrity, quarterly audit, rate card maintenance,
  two-file separation discipline, and amendment protocols.
  This file is NOT an AI governing document — it does not affect how the
  Constitution, Router, or Ingestion protocol execute. It documents the
  human wrapper around the AI system.
maintainer: Karan (content) + Damian (sign-off)
amendment: Same protocol as all instruction files — Damian proposes, Karan drafts, Damian signs off.
---

# GND Standard Operating Procedure
## Human Discipline Guide for Optus Fibre Civil Quoting

> **Browser-readable version:** `docs/sop.html` — open in any browser for
> a formatted view of this content.

---

## 1. Purpose

This document is the single human-readable reference for how GND quotes
Optus fibre civil works using the GND Quote Cowork system. It covers the
entire lifecycle: receiving a drawing, generating a priced quote, separating
internal governance from the commercial submission, maintaining quote
history, and the quarterly audit cycle.

The AI system (Claude Cowork) executes phases automatically based on
the three governing files in this folder. This SOP governs the *human*
steps that surround, gate, and verify the AI's outputs.

**Scope boundary:** This file does not affect AI behaviour. Changes here
do not require re-testing the Constitution, Router, or Ingestion protocol.

---

## 2. People & Roles

| Person | Role | Key Responsibilities |
|--------|------|---------------------|
| Damian | Owner / Commercial | Market Overrides, Hard Stop decisions, rate validation sign-off, field intelligence |
| Karan | Estimating / Admin | Rate card maintenance, RC4 updates, quote submission, knowledge capture completion |
| Craig | Crew Chief / Field | DCAF execution, site walks, evidence capture, field observations |

---

## 3. Folder Architecture

| Folder | Purpose | Rule |
|--------|---------|------|
| `Instructions/` | AI governing documents + this SOP | **IMMUTABLE** — never edit originals in-session |
| `Reference/` | Master BoM, rate cards (RC1–RC4), variation triggers | **IMMUTABLE** — update only via documented amendment |
| `Golden_Templates/` | Example quote workbook layout | **IMMUTABLE** — read-only template shape |
| `Inputs/` | Job PDFs and source workbooks per engagement | Source material — do not modify originals |
| `Output/` | All derivative files (quotes, DCAF packs, knowledge capture) | **ONLY location where new files are created** |
| `docs/` | Human-readable SOP (HTML version) | Reference only |

**The Immutability Rule:** Violating folder immutability is equivalent to
violating the margin firewall. It destroys the audit trail. All work
produces new files in `Output/` only.

---

## 4. Quoting Workflow — End to End

### 4.1 Receive Drawing

1. Karan receives a job PDF (work order / drawing) from Optus
2. Save the PDF into `Inputs/` — do not rename the original
3. Open a Claude Cowork session linked to this project folder

### 4.2 AI Phase Execution

The AI runs the following phases automatically on `/full`:

| Phase | Output | Audience |
|-------|--------|----------|
| 1 | BoQ Verification (rate matching, gap detection) | Karan |
| 2 | Priced Quote (sell + buy rates, Market Override column) | Karan / Damian |
| V-B | Quote Integrity Validation (Pub Test, Missing Work, Rate Inversions, Quantity Reconciliation, Damian's 3 Questions) | Damian |
| 3 | Variation Risk Register (Hard Stops, Amber Gates, provisional sums) | Damian / Optus PE |
| 4 | Wave 1 DCAF Instructions (crew-readable, plain English) | Craig |
| 5 | Project Timeline & Wave Schedule (with calculation working) | Damian / Karan |
| 6 | Cashflow Forecast (assumptions stated before numbers) | Damian |
| 7 | Knowledge Capture (provisional RC4 row) | Karan |
| 8 | Output Assembly (two-file separation — see §5) | Karan / Damian |

### 4.3 Human Review Gates

After the AI completes `/full`, the following human steps are required:

1. **Damian reads Phase V-B** (Quote Integrity) before looking at the
   priced quote. If any item is 🔴 BLOCKED, the quote does not get
   submitted until the flag is resolved.
2. **Damian reviews `/validate`** output — marks each top-value line
   item ✓ or ✗. Returns to Karan for any adjustments.
3. **Karan updates rate cards** if Damian flagged any rates, then
   re-runs `/quote` to regenerate.
4. **Damian confirms the Submission_Clean file** is "drama-free"
   before Karan submits to Optus.

---

## 5. Two-File Output Separation

**This protocol is mandatory for every bid. No exceptions.**

Every priced quote run produces exactly two derivative files in `Output/`:

### Master Internal Control
`[ORDER]_Master_Internal_Control_[DATE].xlsx`

- Contains every annotation, margin view, rate-card flag, variation
  register, V-B findings, knowledge capture
- Header banner: *"INTERNAL — DO NOT SHARE — Contains margin, rate-card
  flags, and live variation tracker."*
- Retained permanently — GND's forensic record for the job

### Commercial Submission
`[ORDER]_Submission_Clean_[DATE].xlsx`

- Golden-template-compliant, visually polished
- Zero flags, zero unresolved items, zero margin data
- Minimal "Job Context" sheet with 3 neutral risk bullets:
  1. Design version status
  2. Third-party asset issues (no owners or $ exposure)
  3. Council/permit notes
- Must never allow purchaser to reconstruct margins or internal data

### Sanitisation Checklist (Submission_Clean)

```
☐ All colour-coded flags removed (🔴, ⚠, ❓)
☐ All "MISSING QTY/RATE", "HARD STOP", "RATE CARD ERROR" text removed
☐ All provisional $0 values for unconfirmed items removed
☐ Detailed quote notes replaced with minimal 3-line version
☐ All internal governance sheets deleted
☐ Subtotal/total formulas verified after deletions
☐ Golden template structure preserved
```

### Separation Verification

```
☐ Submission_Clean contains zero buy rates
☐ Submission_Clean contains zero flags or annotations
☐ Submission_Clean total matches Internal Control sell-side total
☐ No master files in Inputs/, Reference/, or Golden_Templates/ modified
☐ Both files reside exclusively in Output/
```

**Human gate:** Before final submission, a human reviewer must confirm
the Submission_Clean is "drama-free" while the Internal Control remains
"forensically complete."

---

## 6. RC4 Quote History — Data Integrity

### The Rule

The "GND Quoted ($)" value in `GND_RC4_Quote_History.xlsx` must **always**
be the TOTAL QUOTED PRICE from the `_Submission_Clean` file — never the
Internal Control total.

**Why:** RC4 tracks what Optus actually received. Logging the internal
full-risk number corrupts every downstream market signal, win-rate
calculation, and Market Override recommendation.

### Update Workflow (Karan — after every submission)

1. Open the `_Submission_Clean` file from `Output/`
2. Copy the final TOTAL QUOTED PRICE
3. Open `Reference/GND_RC4_Quote_History.xlsx`
4. Paste the total into Column G (GND Quoted) for the relevant row
5. Enter the submission date in Column B
6. Add a one-line note in Key Notes explaining any deliberate deviation
   from the internal total (e.g. "Clean submission used conservative
   bore estimates for drama-free bid")
7. Save — Market Signal Summary auto-updates

### AI Sequencing Note

Phase 7 generates a provisional RC4 row *before* Phase 8 (Output Assembly)
runs. Phase 8 emits a confirmation comparing the Submission_Clean total
against the Phase 7 provisional. If they differ, Phase 8 provides the
corrected RC4 row. Karan uses whichever is final.

---

## 7. Rate Card Maintenance

1. After Damian returns a `/validate` review, Karan updates any flagged
   rates in the rate cards (RC1-SELL, RC2 Materials), entering the date
   in the version header
2. Damian signs off. Karan re-runs `/quote` to generate the updated quote
3. Any rate change in either RC1-SELL or RC1-COST is reviewed by Damian
   before the next quote run
4. Gap register items (❓ MISSING) are added to the rate card before
   submission. Recurring items are promoted to the Master BoM

**Rate card drift:** RC1-SELL and RC1-COST must never diverge. Any update
to one requires verification of the other. The margin calculation is only
reliable when both cards are synchronised.

---

## 8. Knowledge Capture & /learn Protocol

1. Phase 7 auto-generates a knowledge capture entry at the end of every
   `/full` run — outcome marked PENDING
2. After Optus responds, Karan triggers `/learn [ORDER]` and provides:
   - Win or Loss
   - Winning bid amount (if known)
   - How the job played out vs the drawing
3. The entry is formatted for paste into the GND Market Intelligence Doc,
   with tags for suburb, council, PE, carrier, and complexity tier
4. An RC4 row is also generated for paste into Quote History

---

## 9. Quarterly Audit

Every quarter, Damian and Karan conduct a review covering four areas:

### 9a. RC4 Integrity Audit

```
☐ Every "GND Quoted ($)" value matches the corresponding _Submission_Clean
  file in Output/
☐ Any mismatch triggers immediate RC4 correction — log the Submission_Clean
  total, add a correction note
☐ Win/Loss and Winning Bid columns populated for all closed jobs
☐ Market Signal Summary reflects accurate data
```

### 9b. Rate Card Audit

```
☐ RC1-SELL and RC1-COST are aligned — no unreviewed divergence
☐ All gap register items from the quarter resolved or excluded with rationale
☐ Market Overrides reviewed: justified? Should any become permanent?
☐ Subcontractor rates still current — no structural rate inversions
```

### 9c. Folder & File Hygiene

```
☐ No files in Inputs/, Reference/, or Golden_Templates/ modified outside
  the documented amendment protocol
☐ Every job in Output/ has both _Master_Internal_Control and
  _Submission_Clean files
☐ Golden template still current — update if Optus format changed
```

### 9d. Knowledge & Intelligence Review

```
☐ All closed jobs have a completed Knowledge Capture entry
☐ Market Intelligence Doc entries reviewed — PE behaviour changes, council
  patterns, carrier infrastructure updates
☐ New failure modes or anti-patterns identified → proposed as Constitution
  amendments
```

---

## 10. Five Constitutional Principles (Reference)

These govern every AI output. They are reasoning principles, not rules.
The AI executes them silently — this section is for human understanding.

1. **The Margin Firewall** — Buy rates (RC1-COST) never appear in any
   external output. Folders are immutable.
2. **Provisional Sums Are Not Excuses** — Every provisional sum needs a
   specific trigger, resolution action, and gate wave.
3. **Hard Stops Are Hard** — GND does not accept commercial responsibility
   for elements it cannot control at fixed price.
4. **Irreversible Evidence Windows** — Depth of cover, cable serials, bore
   GPS, duct allocation. Payment conditions, not compliance niceties.
5. **The Two-Audience Rule** — Karan/Damian get tables with numbers. Craig
   gets imperative checklists in plain English.

---

## 11. Amendment Protocol

1. Damian proposes the change
2. Karan drafts the amendment in the relevant instruction file
3. Damian signs off
4. Version number increments. Previous version archived, not deleted

**Constitution-level changes** (Hard Stop definitions, margin firewall,
new principles): Damian sign-off mandatory.

**Router or Ingestion tuning** (output formats, anomaly patterns,
productivity rates): Karan and the Claude expert can implement, with
Damian review if it affects Hard Stop classification.

**This SOP:** Same amendment protocol. Changes here do not require
re-testing the AI governing files.

---

*GND Quote Cowork SOP v1.0 · 26 Mar 2026 · Internal to GND.*
