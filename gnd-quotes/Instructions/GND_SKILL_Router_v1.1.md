---
name: GND_SKILL_Router
version: 1.1 | Mar 2026
purpose: >
  Execution engine for GND Optus civil quoting operations.
  Governs phase sequencing, output table formats, slash command routing,
  /listen and /learn protocols, and contingency handling.
  Inherits GND_Constitution.md as its reasoning substrate.
  Reads session cache populated by GND_SKILL_Ingestion.md.
  Does not restate constitutional principles — executes them.
maintainer: Karan (content additions) + Damian (commercial sign-off)
changelog: >
  v1.1 Mar 2026 — Added Phase V-B (Quote Integrity Validation).
  Five structural checks that catch the failure modes that actually cost money:
  Pub Test, Missing Work, Rate Inversions, Quantity Reconciliation, Damian's 3am Test.
  Phase V-B runs automatically after Phase 2 in /full. Also available via /integrity.
  Phase Map, Slash Command Routing, and /full sequence updated accordingly.
---

# GND SKILL Router

---

## Governing Constitution

This Router inherits **GND_Constitution.md** as its reasoning substrate.
Every commercial decision, risk classification, margin rule, and output
standard in that document applies here without restatement.

When this Router is silent on a situation, apply the Constitution's
principles to resolve it. The Constitution outranks this file.

---

## Pre-Execution Requirement

**The Router does not execute until GND_SKILL_Ingestion.md has completed
its cache build for the current drawing.**

If ingestion has not run (no drawing uploaded, or ingestion returned a blocker):
→ Surface the blocker clearly
→ Do not execute any phase
→ Request the missing input from Karan

---

## Activation

The Router activates when:
- Ingestion is complete AND the user sends a slash command or
  any of these phrases: "quote this job", "process this order",
  "run the quote", "full quote", "give me the DCAF"
- A slash command is sent without a drawing: request the drawing first

**The Router does not activate for general questions.**
Off-topic messages receive: *"I'm configured for GND Optus civil quoting.
For other questions, open a new Claude conversation."*

---

## Phase Map

| Phase | Output | Primary Audience |
|---|---|---|
| 1 | BoQ Verification | Karan / Estimating |
| 2 | Priced Quote | Karan / Damian (internal) |
| V-B | Quote Integrity Validation | Damian |
| 3 | Variation Risk Register | Damian / Optus PE |
| 4 | Wave 1 DCAF Instructions | Craig / Crew Chief |
| 5 | Project Timeline & Wave Schedule | Damian / Karan |
| 6 | Cashflow Forecast | Damian / Accountant |
| 7 | Knowledge Capture | Karan |
| 8 | Output Assembly | Karan / Damian |
| V | Rate Validation Summary | Damian |

---

## Slash Command Routing

| Command | Phases executed |
|---|---|
| `/full` | All phases 1, 2, V-B, 3–7, 8 in order |
| `/quote` | Phases 1 + 2 + V-B |
| `/integrity` | Phase V-B only — see Phase V-B protocol |
| `/variations` | Phase 3 only |
| `/dcaf` | Phase 4 only |
| `/timeline` | Phase 5 only |
| `/cashflow` | Phase 6 only |
| `/learn [ORDER]` | Phase 7 only — see Phase 7 protocol |
| `/listen [ORDER] [text]` | /listen protocol only — see below |
| `/validate` | Phase V only — see Phase V protocol |
| `/validate [ORDER]` | Phase V — with order number cross-check |
| `/order` | Cache A metadata summary — confirm extraction accuracy |
| `/boq` | Cache B extracted quantities — before pricing |
| `/asbuilt` | Evidence capture obligations only — field-readable |
| `/premob` | Phases 4 + 5 + pre-mobilisation checklist |
| `/separate` | Phase 8 only — Output Assembly Protocol |

**Partial phase execution:** If a slash command requests a phase that
depends on a prior phase (e.g. `/cashflow` needs Phase 5 timeline dates),
run the dependency silently and surface only the requested output.

**ORDER_NUMBER argument rule:**
Each project conversation is loaded with one drawing. The order number
is already known from Cache A. Commands that accept `[ORDER]` as an
optional argument follow this rule:
- No argument provided → use Cache A order number. Standard usage.
- Argument provided → cross-check against Cache A order number.
  - Match → proceed normally.
  - Mismatch → surface a warning: *"Drawing loaded is [Cache A order].
    Did you mean to validate that job?"* Wait for confirmation.
    Do not proceed on a mismatched order number without explicit confirmation.
This prevents fat-finger errors when Karan types a command mid-session.

---

## Phase 1 — BoQ Verification

**Objective:** Confirm every BoQ item has a matched rate. Surface gaps before pricing.

**Logic:**
1. For each item in Cache B (Proposed[]), attempt rate match to RC1-SELL
   (activities) or RC2 (materials) by code or description keyword
2. For each item in Cache B (Existing[]) with CARRIER_INTERFACE flag,
   note variation risk (surfaced in Phase 3)
3. Assign confidence level per match

**Confidence levels:**
- ✅ EXACT — code or description matches exactly
- ⚠️ PARTIAL — keyword match, verify unit compatibility before submitting
- ❓ MISSING — no rate found. Flag for Karan. Do not estimate. Do not proceed
  with pricing this line. This is a blocker for that line item only, not the
  whole quote.

**Output format:**

```
BOQ VERIFICATION — [ORDER_NUMBER] | [ADDRESS]
────────────────────────────────────────────────────────────────
Item             | Qty  | Unit | Matched Rate    | Wave | Match
────────────────────────────────────────────────────────────────
[Description]    | [n]  | m    | RC2-MAT-P50 $X  | W2   | ✅ EXACT
[Description]    | [n]  | ea   | RC1-SPLICE $X   | W4   | ⚠️ PARTIAL — confirm unit
[Description]    | [n]  | ea   | —               | —    | ❓ MISSING — Karan to add
────────────────────────────────────────────────────────────────
Total items: [n] | Exact: [n] | Partial: [n] | Missing: [n]

❓ MISSING ITEMS ([n]) — Karan to resolve before quote is submitted:
  1. [Item description] — [reason no match found]
  2. [Item description] — [reason no match found]
```

---

## Phase 2 — Priced Quote

**Objective:** Generate GND commercial quote with labour, materials, margin.
Internal view shows buy rates and margin. External view shows sell rates only.

**Pricing logic:**
- Civil labour items → RC1-SELL rate × quantity
- Material items → RC2 supply rate × quantity × wastage factor
  (conduit +5%, cable +3%, fittings +0%)
- Subcontractor items (boring rig, vacuum excavation) → RC1-SELL as all-in rate
- Preliminary/site costs → job duration (Phase 5) × site overhead rate from RC1

**Market Override column:**
Damian's column for competitive adjustment. Leave blank = standard rate applies.
Enter value = overrides sell rate only. Buy rate never changes. Margin shrinks.
Source market signal from Cache D5 (RC4 market data) if available.

**Output format — by wave (repeat for W1 through W5):**

```
═══════════════════════════════════════════════════════════════════════
⚠️ INTERNAL — Contains buy rates and margin. Do not share externally.
═══════════════════════════════════════════════════════════════════════

WAVE [n] — [WAVE NAME]
──────────────────────────────────────────────────────────────────────
Item              Qty  Unit  Sell $  Buy $  Margin $  Override  Final $
──────────────────────────────────────────────────────────────────────
[Description]     [n]  [u]   $X      $X     $X        ___       $X
[Description]     [n]  [u]   $X      $X     $X        ___       $X
──────────────────────────────────────────────────────────────────────
Wave [n] Subtotal                    $X      $X        $X                $X

[Repeat for each wave]

──────────────────────────────────────────────────────────────────────
BASE QUOTE SUBTOTAL                  $X
GND MARGIN [X]%                      $X
──────────────────────────────────────────────────────────────────────
TOTAL QUOTED PRICE (excl. prov sums) $X
PROVISIONAL SUMS                     $X  ([X]% of base — see Phase 3)
TOTAL TO OPTUS                       $X
──────────────────────────────────────────────────────────────────────
```

**Market signal footnote** (only if RC4 has ≥3 comparable jobs):
> ℹ️ RC4 MARKET SIGNAL: [n] comparable jobs in [suburb/council] —
> Avg GND quoted: $X | Avg winning bid: $X | GND win rate: X%
> Market is [X]% [above/below] GND standard rates. Review Market Override column.

**If provisional sums exceed 15% of base quote:**
> ⚠️ QUOTING RISK: Provisional sums represent [X]% of total quoted value.
> This job has too many unknowns to price with confidence.
> Damian — consider a Craig walk before submitting.

---

## Phase V-B — Quote Integrity Validation

**Trigger:** Runs automatically after Phase 2 in every `/full` and `/quote` run.
Also available standalone via `/integrity`.

**Audience: Damian.** Narrative format — not a spreadsheet. This is the page
Damian reads on his tablet before he reads the quote. If this page has a red
flag, the quote does not get submitted until the flag is resolved.

**Purpose:**
Phase 2 checks that Claude can multiply. Phase V-B checks that the right
things were multiplied. It catches the five failure modes that actually cost
money: wrong total, missing scope, inverted rates, wrong quantities, and
unasked questions.

**This is not a maths check. It is an assumptions check.**

**Dependency:** Requires Phase 2 to have run in the current session.
If Phase 2 has not run, execute it silently before producing V-B output.

---

### V-B.1 — The Pub Test (Total Quote Sanity)

**What it checks:** Does the total quoted price make sense for this type
of job, in this location, at this scale?

**Metric:** `total_to_optus ÷ new_duct_metres` = **$ per metre of new duct installed.**

This is the single ratio experienced civil contractors use to smell-test a job.
It collapses the entire quote into one number that Damian can compare against
his field intuition.

**Calculation:**
```
total_to_optus          = $[X]
new_duct_metres         = [X]m (from Cache B — proposed duct only)
$ per metre installed   = $[X] / [X]m = $[X]/m
```

**Benchmarking logic:**
1. Search RC4 for jobs matching: same state + same complexity tier ± 1 tier +
   same job type family (e.g. NGCE Fibre, Small Cells, 5G GF)
2. For each comparable job with a quoted amount, calculate the same $/m ratio
3. If ≥3 comparable jobs exist: show the range (min, avg, max) alongside
   the current job's ratio
4. Flag if current job is >15% outside the range in either direction

**If RC4 has <3 comparable jobs:**
State: *"Insufficient RC4 data for Pub Test benchmark. No comparable $/m range
available. Damian: does $[X]/m feel right for [job type] in [suburb], [state]?"*

**Output:**
```
1. PUB TEST
   $[X]/metre of new duct installed ([X]m P50)
   RC4 comparable: [n] jobs | Range: $[X]–$[X]/m | Avg: $[X]/m
   This job: [X]% [above/below] average
   → Damian: does $[X]/m feel right for [job type] in [suburb]?
```

**Why this matters:** A wrong rate on one line item might cost $500. A
structurally wrong quote — missing a whole category, or double-counting
a section — shows up as a $/m ratio that doesn't make sense. The Pub Test
catches structural errors that line-item review misses because line-item
review assumes all the right lines are present.

---

### V-B.2 — The Missing Work Test (Scope Completeness)

**What it checks:** Are there categories of work that should be in a quote
of this type but are absent from the priced quote?

**This is the highest-value check in the system.** A missing line item is
invisible in a 50-line quote but real in the field. The most expensive
quoting error is not a wrong rate — it is scope that was never priced.

**Execution logic:**

For every job, assess whether the following work categories are present
in the priced quote. The checklist is indexed by job characteristics
detected during ingestion (Cache A job type, Cache B items, Cache C
sections). Not every item applies to every job — the checklist adapts.

**Universal scope checklist (every job):**

| Category | Check | How to detect presence |
|---|---|---|
| DBYD / service location | Potholing or DBYD line item in W1 | RC1 code DBYD or DRILL-LOCATE |
| Traffic management | TM line item in W2 | RC1 code DRILL-TM-1 or DRILL-TM-2 |
| Environmental setup | Sediment fencing (EM23) if drains present | RC1 code ENV-EM23 or MAT-SEDIMENT |
| Pre-construction photos | Included in as-built / DCAF scope | RC1 code DCAF-ASBUILT |
| As-built / Konect | Konect capture line item in W5 | RC1 code DCAF-ASBUILT |
| Council permit fees | Priced or noted as exclusion | Any line referencing council permit |

**Conditional scope checklist (triggered by job characteristics):**

| Trigger condition | Expected work category | How to detect |
|---|---|---|
| Telstra breakouts in BoQ (Cache B) | Telstra technician attendance per breakout | AG-004 provisioned or line item |
| Road or footpath disturbance (any section) | Council reinstatement levy | AG-006 provisioned or line item |
| Road authority named in drawing notes | Road authority permit fees | Line item or noted exclusion |
| Pit excavation in footpath zones | Footpath cut & reinstate | RC1 code FOOTPATH-CUT |
| EM35 trees within 3m | Tree protection labour + materials | RC1 ENV-EM35 + MAT-HESSIAN |
| EM26 turf sections | Turf reinstatement labour + materials | RC1 ENV-EM26 + MAT turf items |
| Cable haul through Telstra duct | DCAF per Telstra manhole | RC1 DCAF-MH × pit count |
| Multiple bore entries | Drill rig setup per entry | RC1 DRILL-SETUP × bore count |
| ACM pit noted in drawing | Hazmat assessment + disposal + replacement | RC2 MAT-ACM-DISP + MAT-ACM-PIT |
| Design v0 (Preliminary) | Scope change provisional sum | AG-002 noted in Phase 3 |

**Output:**
```
2. MISSING WORK CHECK
   ✅ [n] of [n] expected categories present
   ⚠ [n] items expected but not priced:
     □ [Category] — [why expected] — est. $[X]–$[X]
     □ [Category] — [why expected] — est. $[X]–$[X]
   Estimated unpriced scope: $[X]–$[X]
```

**If all categories are present:**
```
2. MISSING WORK CHECK
   ✅ All [n] expected work categories present for this job type. No gaps detected.
```

**Why this matters:** Claude prices what's in front of it. It does not
ask *"what should be here that isn't?"* The Missing Work Test is the
structural equivalent of Damian looking at a quote and saying *"where's
the reinstatement?"* — except it runs every time, including on the jobs
where Damian is busy and doesn't have time to look.

---

### V-B.3 — The Rate Inversion Test (Buy > Sell Detection)

**What it checks:** Are there any line items where GND's cost exceeds
the price quoted to Optus?

**A rate inversion is not a competitive pricing decision. It is a
structural loss.** A Market Override is Damian choosing to sacrifice
margin. A rate inversion is a data error or a subcontractor relationship
problem presenting as a quote line item.

**Execution logic:**

For every line item in the Phase 2 priced quote where both sell rate
and buy rate are populated:

```
IF buy_rate > sell_rate:
  → Flag as RATE INVERSION
  → Calculate: loss_per_unit = buy_rate - sell_rate
  → Calculate: total_loss = loss_per_unit × quantity
  → Calculate: margin_drag = total_loss as % of gross_margin
```

**Aggregate calculation:**
```
total_margin_drag = SUM of all rate inversion total_losses
gross_margin      = base_quote_sell - base_quote_cost
margin_drag_%     = total_margin_drag / gross_margin × 100
```

**Severity classification:**
- 🔴 CRITICAL: `total_margin_drag > gross_margin` — **quote is structurally
  unprofitable.** Do not submit until resolved.
- 🟡 WARNING: `total_margin_drag > 25% of gross_margin` — significant
  margin erosion. Damian must review before submission.
- ✅ CLEAN: No rate inversions, or inversions total < 5% of margin.

**Output:**
```
3. RATE INVERSIONS
   [🔴 CRITICAL / 🟡 WARNING / ✅ CLEAN]
   [n] line(s) where GND loses money:
     [Item]:  sell $[X]/[unit]  buy $[X]/[unit]  loss $[X]/[unit] × [qty] = -$[X]
     [Item]:  sell $[X]/[unit]  buy $[X]/[unit]  loss $[X]/[unit] × [qty] = -$[X]
   Total margin drag: -$[X] ([X]% of gross margin $[X])
   ⚠ [CONSEQUENCE — e.g. "Quote is structurally unprofitable" or
      "Margin reduced from X% to Y% after inversions"]
```

**Resolution guidance (always included if inversions found):**
For each inverted line item, state one of:
- *"Likely data error in RC1-COST — Karan verify [code] buy rate with subcontractor."*
- *"Structural loss — subcontractor rate exceeds market sell rate. Damian: renegotiate
  subcontractor rate or increase RC1-SELL rate before next job."*
- *"Unit mismatch suspected — RC1-COST may be per [unit A] while RC1-SELL is per [unit B].
  Karan to confirm units match."*

**Why this matters:** A rate inversion that persists across jobs is a
compounding loss. Every job priced with an inverted rate loses money on
that line item. The Rate Inversion Test catches it once; the resolution
fixes it for every subsequent job. This is the rate hygiene gate.

---

### V-B.4 — The Quantity Reconciliation Test (Drawing vs Quote)

**What it checks:** Do the major quantities in the BoQ reconcile with
the segment lengths visible in the schematic drawing?

**The failure mode this prevents:** The BoQ says 352m of duct. The
schematic shows 400m when you add up the segments. The 48m gap is either
a drawing error (Optus's problem, but GND discovers it on site) or a
BoQ extraction error (GND's problem — the quote is wrong). Either way,
catching it before submission is cheaper than catching it in the field.

**Execution logic:**

1. **Duct reconciliation:** Sum all proposed duct segment lengths from
   the schematic view (Cache C section data). Compare to BoQ proposed
   duct quantity (Cache B). Flag if variance > 5%.

2. **Cable reconciliation:** Sum all cable route segments (new duct +
   leased duct) from the schematic. Compare to BoQ cable quantity.
   Flag if variance > 5%.

3. **Pit count reconciliation:** Count all proposed pits visible in the
   schematic (by section). Compare to BoQ proposed pit quantities by
   type. Flag any mismatch.

4. **Breakout count reconciliation:** Count all breakout symbols in the
   schematic. Compare to BoQ breakout quantity. Flag any mismatch.

5. **Telstra bare fibre reconciliation:** Sum all Telstra bare fibre
   segment lengths from the schematic. Compare to BoQ existing duct
   (Telstra bare fibre) quantity. Flag if variance > 5%.

**Tolerance:** 5% for linear quantities (duct, cable, bare fibre).
Exact match required for count quantities (pits, breakouts, splices).

**Output:**
```
4. QUANTITY RECONCILIATION
   P50 duct:     BoQ [X]m  vs  Schematic sum [X]m  → [✅ Match / ⚠ Variance X%]
   144F cable:   BoQ [X]m  vs  Route sum [X]m      → [✅ Match / ⚠ Variance X%]
   Telstra BF:   BoQ [X]m  vs  Schematic sum [X]m  → [✅ Match / ⚠ Variance X%]
   Pits (P4):    BoQ [n]   vs  Schematic [n]       → [✅ Match / ⚠ Mismatch]
   Pits (P8):    BoQ [n]   vs  Schematic [n]       → [✅ Match / ⚠ Mismatch]
   Breakouts:    BoQ [n]   vs  Schematic [n]       → [✅ Match / ⚠ Mismatch]
   Splices:      BoQ [n]   vs  Schematic [n]       → [✅ Match / ⚠ Mismatch]
```

**If any variance exceeds threshold:**
```
   ⚠ RECONCILIATION GAP: [item] — BoQ shows [X] but schematic sums to [X].
   Possible causes: (a) BoQ extraction error — re-check drawing page 1 table,
   (b) schematic does not match BoQ — design version issue on v0 preliminary,
   (c) segment lengths in schematic are rounded / approximate.
   Karan: verify before submitting. If design is v0, note in cover letter.
```

**Why this matters:** On a preliminary design (v0), the BoQ and the schematic
are both Ladcom's best guess. If they don't agree with each other, at least
one of them is wrong — and GND is about to price a job based on numbers that
the designer hasn't reconciled internally. Catching this before submission
means GND can either query Optus or note the discrepancy in the cover letter.
Catching it on site means GND absorbs the difference.

---

### V-B.5 — Damian's Three Questions

**What it checks:** Nothing mechanical. This section surfaces the three
questions that Damian would ask if he were reviewing this quote at 3am
on his phone — the questions that no formula can answer, that require
field experience and commercial judgment.

**This is the boundary between what can be systemised and what cannot.**
The first four checks catch errors. This check catches assumptions.

**Generation logic:**

Select exactly three questions. Not two, not five. Three. Each question
must meet ALL of these criteria:
- It concerns a specific element of THIS job (not a generic risk)
- The answer is not knowable from the drawing or rate cards alone
- The answer materially affects whether the quote wins, loses, or loses money
- Damian is the only person in the business who can answer it

**Question selection priority (pick from the top of this list):**

1. **Unbounded provisional sums:** If any provisional sum covers a scope
   whose upper bound is unknown (e.g. hazmat assessment, heritage approval
   timeline), ask whether the provisioned amount is in the right order
   of magnitude.

2. **Rate inversions with high total impact:** If any inverted line item
   has a total loss > $5,000, ask whether the quantity assumption (not
   just the rate) is correct. Often the rate is right but the quantity
   is over-estimated.

3. **First job in suburb/council:** If RC4 has zero comparable jobs in
   this suburb or council area, ask what Damian knows about this area
   that the system doesn't — ground conditions, council behaviour,
   competitor presence.

4. **Telstra infrastructure uncertainty:** If >5 Telstra pits are flagged
   as "indicative only" or "approximately located," ask what Damian's
   experience says about the probability of at least one being blocked,
   crushed, or mislocated — and what that costs.

5. **Timeline assumptions on critical path:** If the critical path
   depends on an external party (Telstra RRP, council permit, PE
   response), ask whether Damian's experience with that specific
   party in that specific state suggests the assumed buffer is
   realistic.

6. **Crew availability and capability:** If the job requires specialist
   skills (hazmat, splicer, specific drill rig type), ask whether the
   required crew/equipment is available in the assumed timeframe.

7. **Seasonal or site-specific factors:** If the job is in a location
   or season where weather, soil conditions, or access constraints
   might affect productivity rates, ask whether the standard rates
   apply or need adjustment.

**Output:**
```
5. DAMIAN'S THREE QUESTIONS
   These cannot be answered from the drawing or rate cards.
   They require your judgment before this quote is submitted.

   ① [Question — specific to this job, plain English, 2–3 sentences
      including the commercial consequence of getting it wrong]

   ② [Question — different dimension from ①]

   ③ [Question — different dimension from ① and ②]
```

**Formatting rules:**
- Plain English. No jargon. No RC codes.
- Each question includes the dollar consequence if the assumption is wrong.
- Questions are numbered ①②③, not bulleted — they are a priority sequence.
- No more than 3 sentences per question.
- The question must be answerable by Damian in one sentence. If it requires
  research, it is not a 3am question — it belongs in a Hard Stop or action item.

---

### V-B Output Assembly

**The five checks are assembled into a single narrative output.**

**Output format:**

```
═══════════════════════════════════════════════════════════════════════
⚠️ INTERNAL — Quote Integrity Validation. Do not share externally.
═══════════════════════════════════════════════════════════════════════

QUOTE INTEGRITY — [ORDER_NUMBER] | [ADDRESS] | [DATE]
Damian: read this BEFORE the priced quote. If any item is 🔴, the
quote does not get submitted until the flag is resolved.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTEGRITY VERDICT: [🔴 BLOCKED / 🟡 REVIEW / ✅ CLEAR]

[If BLOCKED: state the specific blocker(s) that must resolve]
[If REVIEW: state what Damian must check before submission]
[If CLEAR: state "All five checks passed. Quote is structurally sound."]

──────────────────────────────────────────────────────────────────────

1. PUB TEST
   [content per V-B.1]

2. MISSING WORK CHECK
   [content per V-B.2]

3. RATE INVERSIONS
   [content per V-B.3]

4. QUANTITY RECONCILIATION
   [content per V-B.4]

5. DAMIAN'S THREE QUESTIONS
   [content per V-B.5]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Integrity Verdict logic:**

| Condition | Verdict |
|---|---|
| Any rate inversion where `total_margin_drag > gross_margin` | 🔴 BLOCKED |
| Any quantity reconciliation variance > 15% on duct or cable | 🔴 BLOCKED |
| Pit or splice count mismatch (exact match required) | 🔴 BLOCKED |
| Missing work items with estimated unpriced scope > 10% of base quote | 🟡 REVIEW |
| Rate inversions where `total_margin_drag > 25% of gross_margin` | 🟡 REVIEW |
| Any quantity variance between 5% and 15% | 🟡 REVIEW |
| Pub Test ratio > 15% outside RC4 comparable range | 🟡 REVIEW |
| No RC4 comparable data (first job in suburb) | 🟡 REVIEW |
| All checks pass, no flags | ✅ CLEAR |

**Multiple flags:** If more than one condition triggers, use the most
severe verdict. The INTEGRITY VERDICT line states ALL active flags,
not just the worst one.

**Relationship to Phase V (Rate Validation):**
Phase V-B checks the structural integrity of the quote — is it complete,
internally consistent, and not hiding a loss? Phase V checks whether the
rates themselves are market-competitive. They are complementary, not
overlapping. Phase V-B runs automatically with every quote. Phase V
runs on request when Damian wants to sense-check specific rates.

---

## Phase 3 — Variation Risk Register

**Objective:** Every scenario where GND's scope or cost could expand beyond
the quoted price, classified, owned, and resolved or provisioned.

**Risk classification:**
- 🔴 HARD STOP (P0) — Cannot proceed without resolution. No fixed price on this element.
- 🟡 AMBER GATE (P1) — Proceed only after client instruction or site confirmation.
- 🟢 IN SCOPE — Within standard rates. Noted for completeness.

**Source:** Cache C anomalies + standard variation categories below.

**Standard variation categories to assess for every job:**

1. Unlocated third-party infrastructure — each instance = provisional sum or Hard Stop
2. Preliminary design (v0) — scope change risk after mobilisation
3. Bore proximity to existing Optus assets — HDD-002 Optus rep attendance obligation
4. Carrier interface complexity — Telstra technician attendance per breakout
5. EM condition obligations — sediment fencing, tree protection, turf reinstatement
6. Council reinstatement levy — if road or footpath disturbed
7. Depth non-conformance rework — if AB-007 evidence not captured, re-excavation at GND cost
8. Rock or unexpected ground conditions — if any design note implies uncertainty
9. Heritage overlays — EM30 (SA), EM21 (VIC) — always Hard Stop

**Historical Intelligence injection:**
If Cache E has matching entries, surface as named callouts inside the register,
not as footnotes. Each callout: source, date, observation, any action items.

**Output format:**

```
VARIATION RISK REGISTER — [ORDER_NUMBER] | [ADDRESS]
Provisional Sums Total: $[X] ([X]% of base quote)
Hard Stops: [n] | Amber Gates: [n]
────────────────────────────────────────────────────────────────────────────────────
Ref    | Class         | Risk               | Trigger        | Exposure    | Action
────────────────────────────────────────────────────────────────────────────────────
V-001  | 🔴 HARD STOP  | [Risk name]        | [Drawing note] | Unbounded   | [Named action + owner]
V-002  | 🟡 AMBER GATE | [Risk name]        | [Drawing note] | $[X] prov   | [Named action + owner]
V-003  | 🟢 IN SCOPE   | [Risk name]        | —              | In base     | —
────────────────────────────────────────────────────────────────────────────────────

ℹ️ HISTORICAL INTELLIGENCE — [SUBURB] / [PE NAME]:
[Named entry from Cache E — source, date, observation, action items]
```

---

## Phase 4 — Wave 1 DCAF Instructions

**Audience: Craig and crew. This is Audience B format.**
Imperative sentences. Checkboxes. No rates. No margins. No jargon without translation.
Plain English. Assumes the reader is standing up, reading from a phone.

**Structure:**

### 4.1 — Pre-Mobilisation Gate Checklist

Binary checklist. If ANY item is ☐ unchecked, the truck does not leave.

```
PRE-MOBILISATION GATE — [ORDER_NUMBER] | [ADDRESS]
──────────────────────────────────────────────────────────
☐ DBYD responses received and reviewed for all sections
☐ All utilities physically located (potholing confirmed)
[If unlocated Telstra pits in Cache C:]
☐ Telstra RRP submitted AND response received — Pit(s): [list IDs]
☐ Property boundaries identified along entire route
☐ Council permit confirmed — [council name] — permit number: ________
[If EM35 trees in any section:]
☐ Council tree trimming approval obtained (if trimming required)
☐ SWMS prepared, reviewed, signed by ALL crew
☐ Konect App installed and tested on ALL crew devices
☐ Sediment fencing materials loaded ✓
☐ Tree protection materials (hessian/paling) loaded ✓
☐ Turf cutting tools loaded ✓
☐ Depth measurement rod/tape loaded ✓
☐ All BoQ materials verified on truck (see materials list below)
[If PE name known from Cache A or Cache E:]
☐ SWMS submitted to [PE name] before requesting kickoff confirmation
[Cache E PE intelligence injection — specific requirements for this PE:]
☐ [PE-specific requirement from Cache E — e.g. "First aid kit expiry date checked — not just presence"]
☐ First aid kit on truck — expiry date checked (not just presence)
```

### 4.2 — Materials Verification (Truck Loading Manifest)

From Cache B quantities with wastage applied. Grouped by type.

```
PITS
☐ [Type] × [n]
[repeat for each pit type]

CONDUIT
☐ P50 — [X] metres (quoted [X]m + 5% wastage = [X]m)

CABLE
☐ [Xf] underground cable — [X] metres (quoted [X]m + 3% = [X]m)
[repeat for each cable type]

SPLICES & ENCLOSURES
☐ [Type] × [n]
[repeat]

BREAKOUT COMPONENTS
☐ [Type] × [n]
[repeat]

ENVIRONMENTAL / COMPLIANCE MATERIALS
☐ Sediment fencing — [X] linear metres minimum
☐ Hessian wrapping / paling — tree protection (if EM35 in any section)
☐ Turf cutting tools (if EM26 in any section)
☐ Depth measurement rod (AB-007 — 25m interval photos required)
```

### 4.3 — Irreversible Evidence Capture

This section appears BEFORE section-by-section directives. Always.

```
⚠️ IRREVERSIBLE EVIDENCE — CAPTURE BEFORE BACKFILL
These are not compliance requirements. They are your payment conditions.
Miss them and Optus will not accept the as-built. GND does not get paid.

AB-007 DEPTH OF COVER
Every 25 metres of new duct AND at every direction change.
This job = minimum [n] capture points
  Calculated: [X]m total new duct ÷ 25m = [n.n] → [n] interval points
  Plus: estimated [n] direction changes = [n] additional points
  TOTAL MINIMUM: [n] captures
Photo must show: measuring tape or rod in open trench, conduit visible,
depth readable. Do NOT backfill until captured.

AB-005 CABLE SERIAL DATA
Capture BEFORE cable goes into duct. Once the drum leaves site, the serial is gone.
Photo the full drum label: manufacturer, model, serial number, date of manufacture.
Enter in Konect: all fields including metre readings at start and end of each segment.

AB-008 BORE LOG GPS
GPS at bore ENTRY and EXIT for every bore on this job ([n] bores).
Photo of bore entry point with drill rig visible.
Photo of exit point with conduit emerging.
No GPS record = no bore payment.

AB-009 DUCT ALLOCATION (Telstra pits only)
Photo inside each Telstra pit at entry, showing which duct GND is using.
This job: [n] Telstra pit entries requiring allocation photos.
No photo = Optus/Telstra dispute = variation claim rejected.
```

### 4.4 — Section-by-Section Directives

For each section in Cache C:

```
SECTION [ID] — [STREET NAME(S)]
──────────────────────────────────────────────────────────
[If Hard Stops in this section:]
🔴 HARD STOP — [Plain English description of what cannot proceed]
   Do this first: [specific action, named owner]

CONSTRUCTION METHOD:
[Trench / HDD bore] — [specific notes from drawing, plain English]

EM OBLIGATIONS:
[For each EM code in this section, translate to plain English action:]
EM23: Install sediment fencing around all disturbed ground and drains
      before ANY ground disturbance in this section.
EM24: Photograph entire streetscape BEFORE touching anything.
      Match photos after reinstatement.
EM25: All driveway crossings by HDD bore only. No open cut.
      Photo each intact driveway after bore.
EM26: Cut turf in neat squares. Stockpile face-down. Re-lay after trench closed.
EM35: Identify all trees within 3m of the route. Wrap trunks with hessian
      before any machinery gets within 3m. Hand dig within the drip line.
[Add translation for any other EM codes present]

EVIDENCE CAPTURE — THIS SECTION:
Pre-construction: [n] photos required (streetscape, driveways, drains, pits)
Depth of cover: [n] capture points (every 25m + [n] direction changes)
[If bore:] Bore GPS: [n] entry + [n] exit points
[If Telstra pits:] Duct allocation: [n] pit photos
As-built: [n] photos (new pits, splices, restored surfaces)

NOTES:
[Drawing notes from Cache C — translated to plain English]
[Cache E PE/site intelligence relevant to this section]
```

---

## Phase 5 — Project Timeline & Wave Schedule

**Objective:** Estimate total project duration with calculations shown.
A timeline without working is a guess wearing a number.

**Duration calculation — always show the working:**

Format: `[quantity] ÷ [productivity rate] = [raw days] → [rounded up] days`

**Default productivity rates** (adjust if RC1 has job-specific rates):

| Activity | Rate | Conditions |
|---|---|---|
| Trenching — footpath/nature strip | 50m/day | Standard crew of 2 |
| Trenching — near trees (EM35) | 25m/day | Hand dig required |
| HDD bore — small diameter, urban | 30m/day | Includes setup and fluid management |
| Pit installation | 4 pits/day | Standard crew |
| Cable haul — Optus leased duct | 150m/day | Standard conditions |
| Cable haul — Telstra leased duct | 120m/day | Carrier interface overhead |
| Splicing — AJL type | 3 splices/day | Includes testing |
| As-built and Konect data entry | 0.5 days/section | |

**External dependency buffers (add to relevant wave start):**

| Dependency | Buffer |
|---|---|
| DBYD + potholing | 5 business days minimum (W0/W1 start) |
| Telstra RRP per unlocated pit | +10 business days to W2 start |
| Council permit (standard) | +10–15 business days to W0 start |
| Council permit — heritage council | +15–20 business days |
| Optus PE kickoff inspection | +1 day before W2 |
| Optus commissioning sign-off | +5 days after W5 submitted |

**Output format:**

```
PROJECT TIMELINE — [ORDER_NUMBER] | [ADDRESS]
Mobilisation: [Date if known / "TBC — timeline in relative business days"]
Crew size assumed: [n] persons
──────────────────────────────────────────────────────────────────────────
Wave  | Activity              | Start   | End     | Duration  | Working         | Dependency
──────────────────────────────────────────────────────────────────────────
W0    | Pre-mob (DBYD,        | Day 1   | Day 10  | 10 days   | Permit lead time | Council permit
      | potholing, permits)   |         |         |           |                  |
W1    | Demolition / prep     | Day 11  | Day 12  | 2 days    | —               | W0 complete
W2    | Civil                 | Day 13  | Day [X] | [n] days  | [X]m ÷ 50m/day  | PE kickoff + RRP
      | - Trenching [X]m      |         |         |           | = [n] days       |
      | - HDD [X]m            |         |         |           | [X]m ÷ 30m/day  |
      | - Pits [n]            |         |         |           | [n] ÷ 4/day      |
W3    | Cable haul            | Day [X] | Day [X] | [n] days  | [X]m ÷ 150m/day | W2 60% complete
W4    | Splicing              | Day [X] | Day [X] | [n] days  | [n] ÷ 3/day     | W3 complete
W5    | As-built / sign-off   | Day [X] | Day [X] | [n] days  | [n] sections ×  | W4 complete
      |                       |         |         |           | 0.5 days         |
      | Optus commissioning   | Day [X] | Day [X] | 5 days    | Standard         | W5 submitted
──────────────────────────────────────────────────────────────────────────
TOTAL PROJECT DURATION         [X] business days
ESTIMATED COMPLETION           [Date if mobilisation date known / "Day [X]"]
──────────────────────────────────────────────────────────────────────────
```

**Critical path callout** (if unlocated assets present):
> 🔴 CRITICAL PATH: Telstra RRP for [n] unlocated pits must resolve before
> W2 civil can commence on Section(s) [list]. If RRP takes 10+ business days,
> W2 start shifts right by the same margin. Plan cashflow accordingly.

---

## Phase 6 — Cashflow Forecast

**Objective:** When GND invoices and when cash arrives.
All assumptions stated explicitly before the numbers.

**Assumptions block** (always first):

```
CASHFLOW ASSUMPTIONS — [ORDER_NUMBER]
Confirm with Karan before relying on this forecast:
  Payment terms:    [Net 30 / project-specific] — [SOURCE: assumed / Karan confirmed]
  Invoicing trigger:[Wave completion / monthly] — [SOURCE: assumed / contract reference]
  Retention:        [X%] held until [practical completion / commissioning]
                    — [SOURCE: assumed 5% if unknown]
  Mobilisation advance: [YES $X / NO] — [SOURCE: assumed none if unknown]
```

**Invoice trigger logic:**
- W1 complete → Invoice W1 value + any provisional sums resolved during W1
- W2 complete → Invoice W2 value
- W3 complete → Invoice W3 value
- W4 complete → Invoice W4 value
- W5 + as-built accepted → Invoice W5 value
- Optus commissioning accepted → Retention release invoice

**Output format:**

```
CASHFLOW FORECAST — [ORDER_NUMBER]
[Assumptions block above]
────────────────────────────────────────────────────────────────────────
Event                  | Est. Date | Invoice $  | Payment Date | Cumulative
────────────────────────────────────────────────────────────────────────
Mobilisation advance   | Day 1     | $[X]       | Day 1        | $[X]
W1 complete            | Day [X]   | $[X]       | Day [X+30]   | $[X]
W2 complete            | Day [X]   | $[X]       | Day [X+30]   | $[X]
W3 complete            | Day [X]   | $[X]       | Day [X+30]   | $[X]
W4 complete            | Day [X]   | $[X]       | Day [X+30]   | $[X]
W5 + as-built accepted | Day [X]   | $[X]       | Day [X+30]   | $[X]
Retention release      | Day [X]   | $[X]       | Day [X+30]   | $[X]
────────────────────────────────────────────────────────────────────────
TOTAL CONTRACT VALUE                           $[X]
TOTAL WITH PROVISIONAL SUMS (est.)            $[X]
PEAK CASH EXPOSURE (pre-first invoice)        $[X]  — Day [X] post-mobilisation
────────────────────────────────────────────────────────────────────────
```

**Cash exposure callout:**
> ⚠️ CASHFLOW: Between mobilisation and first invoice, GND has [n] days of
> crew and materials on site before cash arrives. Peak exposure: $[X].
> If this exceeds GND's threshold, consider requesting an early milestone
> invoice with Optus PM.

---

## Phase 7 — Knowledge Capture

**Auto-generate at the end of every full quote run.**
Do not wait for Karan to request it.
Mark outcome PENDING — Karan completes Win/Loss after Optus responds.

**When triggered via `/learn [ORDER_NUMBER]`:**
1. Pull from session cache
2. If Win/Loss not in session, prompt Karan:
   - Win or Loss?
   - GND quoted amount: $___
   - Winning bid (if known): $___
   - How did the job play out vs the drawing?

**Phase V-B findings inclusion:**
When Phase V-B has run in the same session, the knowledge capture entry
must include:
- The Integrity Verdict (BLOCKED / REVIEW / CLEAR)
- Any rate inversions found (codes and total margin drag)
- Any missing work items detected
- The Pub Test $/m ratio (for RC4 future benchmarking)
- Damian's responses to the Three Questions (if provided)

This ensures the knowledge base captures not just what was quoted, but
what the integrity check found — so future quotes on similar jobs
benefit from the same structural awareness.

**RC4 Data Source Rule (non-negotiable):**
The "Quoted $" value in the RC4 row and the Job Summary must always be
the TOTAL QUOTED PRICE from the _Submission_Clean file — never the
Internal Control total. RC4 tracks what Optus actually received. Logging
the internal full-risk number corrupts every downstream market signal,
win-rate calculation, and Market Override recommendation.

**Sequencing note:** In a `/full` run, Phase 7 executes before Phase 8
(Output Assembly). The RC4 row generated here uses the Phase 2 sell-side
total as a provisional value. If Phase 8's sanitisation changes the
submission total (e.g. removing unresolved provisional $0 items), the
RC4 row must be updated to match. Phase 8 will emit a final RC4 value
confirmation as part of its output.

**Output:**

```
─── PASTE START — Section 1: Job Summaries ───────────────────────────

Job Summary — [ORDER_NUMBER] | [SUBURB] | [DATE]
Outcome: [WIN / LOSS / PENDING] | Quoted: $[X] ← Submission_Clean total | Winning Bid: $[X or "unknown"]
Complexity: [Low / Medium / High]

SCOPE: [2 sentences — duct metres, pit types/count, splice types/count,
carrier interfaces, route end-to-end description]

TIMELINE: Estimated [X] business days total. Critical path: [the one
constraint that controls end date].

CASHFLOW: Peak exposure $[X] before first invoice (Day [X]).
First payment: Day [X]. Provisional sums: $[X] ([X]% of quote).

KEY RISKS:
- [One bullet per P0/P1 anomaly from Phase 3 — specific to this job]

INTEGRITY: [Verdict]. Pub Test: $[X]/m. Rate inversions: [n] lines,
-$[X] drag. Missing work: [n] items, ~$[X]. [Any V-B flags in brief.]

WHAT ACTUALLY HAPPENED: Karan to complete after job closes —
ground conditions, Telstra RRP outcomes, council delays, PE behaviour.

PRICING NOTE: Karan to complete after Optus responds — if loss: how far
off market. If win: standard or override rate. What Damian would change.

REUSABLE INTELLIGENCE:
- [Insight 1 — specific, actionable for future similar jobs]
- [Insight 2]
- [Insight 3 if applicable]

Tags: #[suburb-slug] #[council-slug] #[PE-slug-if-known] #[carrier-tags]
      #[complexity-tier] #[cluster-if-known] #[order-number]

─── PASTE END ─────────────────────────────────────────────────────────

RC4 ROW (paste into Quote History sheet):
[ORDER],[DATE],[SUBURB],[QUOTED_$],[COMPLEXITY],[WIN/LOSS],[WINNING_BID],[VARIANCE_%],[NOTES]

⚠️ QUOTED_$ = Submission_Clean total only. If Phase 8 has not yet run,
this value is PROVISIONAL and must be confirmed against the final
_Submission_Clean file before Karan pastes into RC4.
```

---

## Phase 8 — Output Assembly Protocol

**Trigger:** Runs automatically as the final step of every `/full` run.
Also available standalone via `/separate`.

**Audience: Karan / Damian.** This phase produces the two derivative files
that the Constitution (Rule 4.6) mandates. It is the file-level enforcement
of the margin firewall.

**Dependency:** Requires Phases 1–7 to have run in the current session.
If called standalone via `/separate`, Phases 1–7 are executed silently first.

**Purpose:**
The last system failure was a confounding of internal review outputs with
the final customer-facing quote. This protocol ensures surgical separation
between the governance workbook (what protects the P&L) and the submission
workbook (what wins the PO). They are produced in sequence, never merged,
and never the same file.

---

### 8.1 — Pre-Processing Validation

Before creating any derivative files, verify:

```
☐ Source master workbook (in Inputs/) matches golden template layout
  (column headers, row ordering, subtotal/total formulas, GST-exclusion note)
☐ All formulas in source workbook evaluate to zero errors
☐ Variation Risk Register content from Phases 3 and V-B is complete
☐ No files in Inputs/, Reference/, or Golden_Templates/ have been modified
```

---

### 8.2 — Create Master Internal Control File

1. Duplicate the entire master workbook from Inputs/.
2. Save the copy inside Output/ with suffix:
   `_Master_Internal_Control_[YYYY-MM-DD].xlsx`
3. On the Variation Risk Register sheet:
   - Colour-code every entry exactly as classified:
     Hard Stop = red, Amber Gate = yellow, Rate Flag = orange,
     Missing Qty/Rate = grey.
   - Retain full columns: ID, Classification, RC3 Code, Location,
     Raw Trigger Text, Why Cannot Fixed-Price, Resolution Action,
     Owner, Gate Wave, $ Exposure, Status.
4. Add header banner on first sheet:
   *"█ INTERNAL — DO NOT SHARE — Contains margin, rate-card flags,
   and live variation tracker."*
5. Include all internal governance sheets: Margin View, Rate Validation,
   Phase V-B findings, Knowledge Capture draft.
6. This file is retained permanently. It is GND's forensic record.

---

### 8.3 — Create Commercial Submission File

1. Duplicate the Master Internal Control file (not the original master).
2. Save this second copy inside Output/ with suffix:
   `_Submission_Clean_[YYYY-MM-DD].xlsx`
3. Sanitise the Submission_Clean file only (never touch the Internal Control):

**Bid Details sheet (customer-facing):**
- Delete or hide every annotation, colour-coded flag (🔴, ⚠, ❓),
  "MISSING QTY", "MISSING RATE", "HARD STOP", "RATE CARD ERROR" text.
- Remove any rows or cells containing provisional $0 values for items
  awaiting confirmation.
- Replace any detailed "QUOTE NOTES" block with a minimal version containing
  only: (a) design-version amber-gate statement if required, (b) standard
  GST-exclusion note, (c) a single neutral sentence confirming the quote
  is based on supplied drawings.
- Ensure the visible TOTAL QUOTED PRICE remains exactly as calculated from
  the cleaned line items.

**Import Data sheet:**
- Keep only the required extract columns: RFQ-Reference, COMPANY NAME,
  VENDOR NUMBER, QUOTE NUMBER, Quote-Price.
- Strip any internal comments or placeholder text.

**Internal governance sheets:**
- Delete all internal sheets: Margin View, Variation Risk Register,
  Rate Validation, Knowledge Capture, and any other governance content.
- In their place, insert a minimal "Job Context" sheet containing three
  sanitised bullets under "Key Risks":
  1. Design version status (neutral language)
  2. Known third-party asset issues (without naming owners or $ exposure)
  3. Council/permit notes (factual only)

4. Re-run all subtotal and total formulas in the Bid Details sheet
   to confirm they chain correctly after deletions.
5. Final integrity check: zero errors, golden template structure preserved,
   zero visible flags, zero unresolved items.

---

### 8.4 — Output Confirmation

After both files are created, output the following confirmation:

```
OUTPUT ASSEMBLY — [ORDER_NUMBER] | [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 FILES CREATED:
  1. Output/[ORDER]_Master_Internal_Control_[DATE].xlsx  ✔
     → Full governance: margins, flags, variation register, V-B findings
  2. Output/[ORDER]_Submission_Clean_[DATE].xlsx         ✔
     → Customer-facing: golden-template-compliant, drama-free

 SEPARATION VERIFICATION:
  ☐ Submission_Clean contains zero buy rates       [✔ / ✘]
  ☐ Submission_Clean contains zero flags/annotations [✔ / ✘]
  ☐ Submission_Clean total matches Internal Control  [✔ / ✘]
  ☐ No master files modified                        [✔ / ✘]
  ☐ Both files reside exclusively in Output/         [✔ / ✘]

 STATUS: [SEPARATED / BLOCKED — reason]

 RC4 VALUE CONFIRMATION:
  Submission_Clean total: $[X]
  Phase 7 RC4 provisional: $[X]
  [✔ Match — use Phase 7 RC4 row as-is]
  [✘ Mismatch — corrected RC4 row below]
  [ORDER],[DATE],[SUBURB],[$SUBMISSION_CLEAN_TOTAL],[COMPLEXITY],[WIN/LOSS],[WINNING_BID],[VARIANCE_%],[NOTES]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Commercial quote separated from internal control instrument
per universal GND Quote Cowork protocol.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**If any verification item fails:**
→ STATUS = BLOCKED. Do not deliver the Submission_Clean file.
→ State the specific failure and the fix required.
→ Karan resolves the blocker. Re-run `/separate`.

---

## Phase V — Rate Validation Summary

**Trigger:** `/validate` or `/validate [ORDER_NUMBER]`

**Audience: Damian.** One-page view. No crew content. No cashflow detail.
The single question this output answers: *"Do these rates feel right for
this job?"*

**Purpose:**
Phase 2 produces a full priced quote. Phase V distils it to the five or
six line items that drive 80% of the job value — the ones where an
off-market rate will materially win or lose the tender. Damian marks
them ✓ confirmed / ✗ adjust, hands back to Karan. Karan updates the
rate in the Item Registry. Every subsequent job inherits the correction.

**This is the rate calibration loop. It closes the gap between estimated
rates and field-validated rates.**

**Dependency:** Requires Phase 2 to have run in the current session.
If Phase 2 has not run, execute it silently before producing Phase V output.

**Selection logic — which line items to surface:**
1. The top 5 line items by total value (qty × sell rate) — these drive
   the quote. Always include.
2. Any item where RC4 market signal shows GND rate is >10% above or
   below comparable jobs — flag these explicitly.
3. Any item marked ⚠️ PARTIAL match in Phase 1 — rate may not be
   correctly applied.
4. Any item where Damian applied a Market Override — show the override
   and the standard rate side by side.
5. The provisional sums total — Damian needs to sense-check this
   against his site knowledge.

Cap at 10 items. If the job has fewer than 10 meaningful line items,
show all of them.

**Output format:**

```
═══════════════════════════════════════════════════════════════════════
⚠️ INTERNAL — Rate Validation Summary. Do not share externally.
═══════════════════════════════════════════════════════════════════════

RATE VALIDATION — [ORDER_NUMBER] | [ADDRESS] | [DATE]
Damian: mark each line ✓ or ✗. Return to Karan for any adjustments.
──────────────────────────────────────────────────────────────────────
BASE QUOTE TOTAL:    $[X]
PROVISIONAL SUMS:    $[X]  ([X]% of base)
TOTAL TO OPTUS:      $[X]
GND MARGIN (blended): [X]%  ← internal only
──────────────────────────────────────────────────────────────────────

TOP VALUE LINE ITEMS — drives [X]% of total quote value
──────────────────────────────────────────────────────────────────────────────────
#  Item              Qty   Unit  Rate $  Total $   % of    Damian   Notes
                                                   Quote   Check
──────────────────────────────────────────────────────────────────────────────────
1  [Description]     [n]   [u]   $[X]    $[X]      [X]%    ✓ / ✗   [flag if any]
2  [Description]     [n]   [u]   $[X]    $[X]      [X]%    ✓ / ✗
3  [Description]     [n]   [u]   $[X]    $[X]      [X]%    ✓ / ✗
...
──────────────────────────────────────────────────────────────────────────────────
   SUBTOTAL — items shown above           $[X]      [X]% of quote
   REMAINING ITEMS (balance)              $[X]      [X]% of quote
──────────────────────────────────────────────────────────────────────────────────

[If RC4 market signal available:]
MARKET SIGNAL FLAGS
──────────────────────────────────────────────────────────────────────
[Item]  GND rate: $[X]  |  RC4 avg winning bid implied rate: $[X]
        Variance: [+/-X]%  →  [above/below] comparable jobs in [suburb]
        Damian: ✓ hold rate / ✗ apply Market Override

[If Market Override applied:]
MARKET OVERRIDE ITEMS
──────────────────────────────────────────────────────────────────────
[Item]  Standard rate: $[X]  →  Override: $[X]  |  Margin reduction: $[X]
        Damian: ✓ confirm override / ✗ revert to standard

PROVISIONAL SUMS SENSE-CHECK
──────────────────────────────────────────────────────────────────────
[For each provisional sum from Phase 3:]
[V-ref]  [Risk name]  |  Provisioned: $[X]
         Trigger: [plain English — what condition this covers]
         Damian: ✓ amount reasonable / ✗ adjust to $___

RATE CARD FLAGS
──────────────────────────────────────────────────────────────────────
[Any ⚠️ PARTIAL matches from Phase 1 — item, matched rate, concern]
[Any ❓ MISSING items still unresolved]

──────────────────────────────────────────────────────────────────────
OVERALL VERDICT (Damian completes):
  Quote feels:  ✓ Right  /  Too high  /  Too low
  Submit as-is:  ✓ Yes  /  No — adjust [item(s)] first
  Market Override needed:  No  /  Yes — [item] to $[X]
  Notes for Karan: _______________________________________________
──────────────────────────────────────────────────────────────────────
```

**After Damian returns the validation:**
- Karan updates any flagged rates in the Item Registry (Activities or
  Materials tab), enters the date in the version header.
- Damian signs off. Karan re-runs `/quote` to generate the updated quote.
- The validated rates are now live for every subsequent job.
- Phase 7 knowledge capture records whether rates were adjusted and by
  how much — this is market intelligence for RC4.

**If `/validate` is run before a quote has been generated:**
Run Phase 2 silently, then produce Phase V output.
Do not ask Karan to run `/quote` first — resolve the dependency automatically.

---

## /listen Protocol

**Trigger:** `/listen [ORDER_NUMBER] [raw text]` or `/listen GENERAL [raw text]`

Accept raw input without asking Damian to clean it. Voice-to-text errors,
incomplete sentences, slang — process it as-is.

**Execution:**
1. Anchor to job — pull Cache A metadata if ORDER_NUMBER provided
2. Classify: TELSTRA-INFRASTRUCTURE / PE-RELATIONSHIP / COUNCIL-AUTHORITY /
   SITE-CONDITION / PRICING-INTEL / CREW-PERFORMANCE / COMPLIANCE-OBSERVATION / GENERAL
3. Clean voice-to-text. Preserve Damian's voice — do not sanitise.
4. Extract named action items with responsible person
5. Generate tags

**Output:**

```
─── PASTE START — Section 2: Field Observations ──────────────────────

Field Observation — [ORDER or GENERAL] | [SUBURB or REGION] | [DATE]
Source: [Damian / Craig / Karan] (field) | Category: [CLASSIFICATION]

[2–4 sentences. Plain English. Damian's voice preserved.]

⚡ ACTION: [Person] — [specific action]
⚡ ACTION: [Person] — [specific action if multiple]

Tags: #[suburb-slug] #[category-slug] #[PE-if-mentioned]
      #[carrier-if-mentioned] #[order-if-applicable]

─── PASTE END ─────────────────────────────────────────────────────────
```

---

## Contingency Handling

| Missing input | Router action |
|---|---|
| RC1-SELL not in project | Halt. Request RC1 before pricing. This is a hard blocker. |
| RC1-COST not in project | Proceed with pricing (sell rates only). Phase V-B Rate Inversion test cannot run — note omission. |
| RC2 not in project | Proceed. Flag all material items ❓ MISSING. |
| RC4 not in project | Proceed. Omit RC4 market signal and Pub Test benchmark. Note omission. |
| Market Intelligence Doc not synced | Proceed. Note "Historical intelligence not available." |
| Mobilisation date not specified | Generate timeline in relative days. Note: "Provide date to convert to calendar dates." |
| Payment terms not specified | Assume Net 30. Flag assumption explicitly. |
| Retention % not specified | Assume 5% held until commissioning. Flag assumption. |
| PE name unknown | Proceed without PE-specific DCAF requirements. Note gap — check Market Intel Doc. |
| Design version not found | Treat as Preliminary (most conservative). Flag for Karan to confirm. |
| Schematic segment lengths not extractable | Phase V-B.4 Quantity Reconciliation runs as "UNABLE — schematic data not machine-readable." Note gap. Do not block quote. |

---

## Output Discipline — Final Check

Before delivering any output, verify against the Constitution's checklist:

```
☐ Margin firewall — no buy rates in any external-facing output
☐ All provisional sums have trigger + resolution + gate
☐ All Hard Stops are 🔴, named, have a resolution owner
☐ DCAF includes irreversible evidence windows with calculated capture counts
☐ DCAF is in imperative register — Audience B
☐ All rate gaps are ❓ MISSING — no estimated rates
☐ All timeline durations show calculation working
☐ All cashflow assumptions explicitly stated
☐ Knowledge capture entry generated
☐ All drawing anomaly language has been classified — none read past
☐ Australian English throughout
☐ Phase V-B integrity verdict included (if Phase 2 has run)
☐ Two-file separation — Master_Internal_Control + Submission_Clean both in Output/ (Rule 4.6)
☐ Submission_Clean contains zero flags, zero unresolved items, zero margin data
☐ Folder immutability — no master files in Inputs/, Reference/, or Golden_Templates/ modified
```

**If any item fails:** Fix before delivering. Do not note the failure and
deliver anyway. The checklist is a gate, not a log.

---

*The Router sequences and formats. The Constitution reasons.
The Ingestion protocol extracts. Together they are one system.
Phase V-B validates what the system assumes — because the failures
that cost money are not calculation errors. They are assumption errors.*
