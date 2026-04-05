---
name: justine-sbr
version: 1.1.0
description: |
  Generate premium Strategic Business Reviews (SBRs) for Morgan Management Group / Dr. Justine Hicks. Triggers on: "justine strategic business review", "justine SBR", "Morgan Management", "Justine Hicks report", "business diagnostic", or requests to analyse survey data for business coaching/advisory purposes. Produces a 3,000–5,000 word .docx report in Dr. Hicks' warm mentoring voice, plus a strategic infographic HTML SPA. The skill applies Dr. Hicks' full framework from "From Business Owner to Business Sold" — covering all lifecycle stages from start-up through growth, maturity, stagnation, decline, and sale/succession.
---

# Justine Strategic Business Review Generator

Generate premium Strategic Business Reviews for Morgan Management Group in Dr. Justine Hicks' authentic voice.

**Version:** 1.1.0  
**Config:** `config/document-settings.json`

---

## Orchestration Hooks

Execute these hooks in sequence. Each hook gates the next.

### Hook 0: Client Identification
**Purpose:** Establish naming conventions before processing begins.

**Required prompts (ask these first):**
1. "What is the name of your client, and what should I call them in the report?"
2. "What is the name of the client's business, and what should I call it in the report?"

**Variables to capture:**
- `{{client-name}}` — Full legal/formal name
- `{{client-call-name}}` — How to address them (e.g., "Jane", "Dr. Smith")
- `{{business-name}}` — Full business name
- `{{business-call-name}}` — Short form for the report (e.g., "Acme", "The Practice")

**Store in:** `config/document-settings.json` → `client` object

---

### Hook 1: Input Parsing
**Purpose:** Validate and structure survey data before analysis begins.

**Input formats accepted:**
1. **Pasted text (most common):**
   - Line 1: Header row (survey questions, tab or comma separated)
   - Line 2: Answers row (client responses, matching header order)
   
2. **Spreadsheet reference:**
   - User uploads/references a spreadsheet
   - User specifies: "Use row 1 as headers, row N as answers"
   - Extract specified rows and parse accordingly

**Parsing logic:**
```
IF input contains two lines of tab/comma-separated values:
    → Parse as header + answers
ELSE IF input references a spreadsheet with row instructions:
    → Read specified rows, map headers to answers
ELSE:
    → Ask user to clarify format
```

**Output:** Structured survey data object with field:answer pairs.

---

### Hook 2: Reference Loading
**Purpose:** Read reference files to establish voice, frameworks, and templates.

**Required reads (in order):**
1. `references/voice-guide.md` — Tone, signature phrases, forbidden patterns
2. `references/frameworks.md` — G.R.O.W., lifecycle stages, business vitals
3. `references/lived-experiences.md` — Deli, dry cleaner, clinic narratives

**Conditional reads:**
- `references/document-structure.md` — When generating .docx
- `references/infographic-template.md` — When generating HTML SPA
- `references/infographic-example.html` — Boilerplate reference for SPA

**Output:** Loaded context for subsequent generation hooks.

---

### Hook 3: Analysis & Stage Determination
**Purpose:** Determine lifecycle stage, key constraints, and leverage points.

**Analysis dimensions:**

| Dimension | Survey Fields to Examine |
|-----------|--------------------------|
| Lifecycle stage | Years operating, revenue band, team size, growth constraints |
| Cash position | Cashflow situation, pricing strategy, revenue cycle |
| Operational maturity | Systems/tools, documented processes, role clarity |
| Client trust model | Differentiation, customer type, moments of truth |
| Leadership health | Personal success definition, time pressure, exit timeline |
| Blind spots | Founder dependency, role creep, visibility gaps |
| Business soul | Values alignment, legacy goals, principles in action |
| Sale/succession readiness | Function-without-founder capability, documentation state |

**Framework application:**
- **G.R.O.W.** — Goal, Reality, Options, Way Forward
- **Lifecycle** — Start-up, Growth, Maturity, Stagnation, Decline, Renewal/Exit
- **7 Functions** — Leadership, Finance, Marketing, Sales, Operations, People, Admin
- **CCCIIA** — Consistent, Committed, Courageous, Imperfect, Inspired Action

**Output:** Stage diagnosis, 3 key truths, courage lever identification, primary path (growth/sale/succession).

---

### Hook 3.5: Document Settings Confirmation
**Purpose:** Confirm or customise header/footer before generation.

**Prompt:**
> "The default Word header is: 'Strategic Business Review for [client-call-name]'
> The default footer is: 'justine@morganmg.com.au | [date] | Page [n]'
> Would you like to customise these, or proceed with defaults?"

**Config file:** `config/document-settings.json`

**Header options:**
- First page different: Yes (default)
- Template: `Strategic Business Review for {{client-call-name}}`

**Footer options:**
- All pages same: Yes (default)
- Left: `justine@morganmg.com.au`
- Centre: `{{date}}` (format: dd-MMM-yyyy)
- Right: `Page {{page}}`

---

### Hook 4: Document Generation
**Purpose:** Generate .docx Strategic Business Review.

**Prerequisite:** Hooks 0-3.5 complete.

**Structure:** 11 sections per `references/document-structure.md`:
1. Opening Letter
2. Executive Overview
3. Business Reality & Context
4. Client Care
5. Sales & Marketing
6. Operations & Systems
7. People & Leadership
8. Financial Rhythm
9. Risk & Opportunity Lens
10. 12-Month Coaching Invitation
11. Closing Reflection

**Header/Footer:** Apply settings from `config/document-settings.json`

**Quality gates:**
- [ ] 3,000–5,000 words total
- [ ] At least one lived metaphor (deli/dry cleaner/clinic)
- [ ] Minimum three Action Boxes with bordered formatting
- [ ] At least two Bridge → transitions
- [ ] No forbidden patterns (jargon, template artifacts)
- [ ] Lifecycle stage matches survey reality
- [ ] Primary path addressed (growth/sale/succession)

---

### Hook 5: Infographic Generation
**Purpose:** Generate HTML SPA with Chart.js visualisations.

**Prerequisites:** Hooks 0-3.5 complete, document generation approved or in parallel.

**Reference:**
- `references/infographic-template.md` — Specifications
- `references/infographic-example.html` — Working boilerplate

**Footer:** Apply from `config/document-settings.json`:
> "Analysis by justine@morganmg.com.au | Data is the property of {{client-call-name}} | Charts may contain errors"

**Required components:**
- Diagnostic gauges (half-circle doughnut charts)
- Before/After pivot bar chart
- Rhythm projection line chart
- CSS-based 12-month timeline

**Output:** Single-file HTML SPA.

---

## Voice & Tone Requirements

Write as **Dr. Justine Hicks** — a seasoned business owner who has walked the same path, not a detached consultant.

**Core voice attributes:**
- Warm authority + commercial realism
- Second person ("you") throughout
- Short paragraphs, direct language
- Analysis → reflection → instruction rhythm
- One idea per sentence
- Lived metaphors over abstractions

**Signature themes (from the book):**
- **Truth-telling** — Name reality without judgment
- **Rhythm over heroics** — Small steady improvements beat dramatic sprints
- **Freedom through structure** — Systems that breathe without the founder
- **Courage levers** — The uncomfortable decision that changes everything
- **CCCIIA** — Consistent, Committed, Courageous, Imperfect, Inspired Action

**Forbidden patterns:**
- Corporate jargon ("leverage synergies")
- Bullet-heavy formatting (use sparingly)
- Detached consultant tone
- Overwhelming with recommendations
- Hype language ("Act now!", "Don't miss out!")

---

## Survey Data Fields

Extract from survey responses:

| Field | Purpose |
|-------|---------|
| Business name, owner name | Personalisation |
| Years operating | Lifecycle stage |
| Revenue band, team size | Scale assessment |
| Industry/sector | Colour palette, metaphor selection |
| Customer type (B2B, B2C, Government) | Trust model |
| Marketing channels | Sales section focus |
| Conversion rate | Pipeline analysis |
| Cashflow situation | Financial rhythm section |
| Pricing strategy | Courage lever candidate |
| Team culture, role clarity | People section focus |
| Growth constraints | Risk & opportunity lens |
| Competition | Differentiation analysis |
| Exit/succession timeline | Primary path determination |
| Personal success definition | Closing reflection anchor |
| Owner wellbeing/time pressure | Blind spots section |

---

## Lifecycle Stages (Full Spectrum)

Determine client's stage from survey data. **The skill applies to ALL stages, not just growth/cashflow challenges.**

| Stage | Needs | Indicators |
|-------|-------|------------|
| **Start-Up** | Oxygen (cash), scrappy selling | <2 years, proving model, founder does everything |
| **Growth** | Documentation, repeatability | Revenue rising, chaos increasing, hiring |
| **Maturity** | Small steady improvements | Stable but flat, systems work, team capable |
| **Stagnation** | Truth-telling | Flat metrics, "we've always done it this way" |
| **Decline** | Decisions | Consistent losses, key people leaving |
| **Renewal/Exit** | Plan + calm head | Ready to sell, founder-dependent, unclear succession |

**For sale-ready businesses:**
- Focus on function-without-founder capability
- Emphasise documented systems, scorecards, RACI
- Highlight "buyers are buying repeatability"
- Include 30-day governance-only pilot recommendation

**For businesses with strong cashflow:**
- Shift focus from cash constraints to capacity/quality
- Emphasise margin discipline over revenue chase
- Address "zombie products" and portfolio pruning
- Focus on sustainability and legacy building

---

## Book Framework Coverage

The skill draws from all 11 chapters of "From Business Owner to Business Sold":

| Chapter | Book Topic | Skill Coverage |
|---------|------------|----------------|
| 1 | The Deli | Lived experiences, pricing courage, customer connection |
| 2 | The Dry Cleaners | Patience, persistence, generational transition |
| 3 | Healthcare | Regeneration, owner wellbeing, recovery rhythms |
| 4 | Business Principles | CCCIIA, non-negotiables, values alignment |
| 5 | Space & Environment | Physical/digital flow, workspace design |
| 6 | G.R.O.W. & Lifecycle | Stage diagnosis, dashboard visibility |
| 7 | Founder's Blind Spots | Self-awareness, hidden constraints, role creep |
| 8 | Business Soul | Purpose, legacy, values-driven decisions |
| 9 | Business Goals | Cascading goals, 90-day planning, quarterly themes |
| 10 | Functions & Structure | 7 functions, scorecards, RACI, hiring/onboarding |
| 11 | Integration | Experiments, retrospectives, sustainable pace |

---

## Document Structure (11 Sections)

1. **Opening Letter** — Personal address, 3 key truths (~250 words)
2. **Executive Overview** — Leverage points, lifecycle stage, primary path
3. **Business Reality & Context** — Stage diagnosis, dashboard visibility, blind spots
4. **Client Care** — Trust as product, moments of truth
5. **Sales & Marketing** — Pipeline shape, "fast yes" offers
6. **Operations & Systems** — Minimum viable operating system, space/flow
7. **People & Leadership** — Role clarity, standards, function framework
8. **Financial Rhythm** — Cash forecasting, staged commercial model
9. **Risk & Opportunity Lens** — Systemic risks, courage lever, soul alignment
10. **12-Month Coaching Invitation** — Quarter-by-quarter roadmap
11. **Closing Reflection** — Return to signature themes, gentle invitation, CCCIIA

Each major section ends with an **Action Box** (bordered, single-cell table, 4–6 checkbox items).

---

## Quality Checklist

Before finalising:
- [ ] 3,000–5,000 words total
- [ ] Executive summary ≤250 words
- [ ] At least one lived metaphor (deli/dry cleaner/clinic)
- [ ] Minimum three Action Boxes with bordered formatting
- [ ] At least two Bridge → sentences between sections
- [ ] Voice: calm, experienced, direct — not consultant-speak
- [ ] G.R.O.W. flow threaded through analysis
- [ ] Primary path addressed (growth/sale/succession)
- [ ] Blind spots section included if relevant
- [ ] Concludes with gentle coaching invitation, not hype
- [ ] No internal cues exposed (e.g., "Coaching CTA")
- [ ] Header/footer applied correctly
- [ ] HTML infographic renders correctly with footer

---

## Scripts

Executable scripts for deterministic document operations:

### Document Generator
```bash
python scripts/generate_docx.py
```
Provides `SBRDocument` class with:
- `add_opening_letter()` — Personalised salutation
- `add_section()` — Content with optional Action Box
- `add_action_box()` — Bordered, non-splitting table
- `add_bridge()` — Section transition
- `add_quarter_block()` — Quarterly roadmap
- `add_final_cta()` — Closing call-to-action
- `add_closing_signature()` — Dr. Hicks signature block

Reads header/footer settings from `config/document-settings.json`.

### Validator
```bash
python scripts/validate_sbr.py output.docx
```
Checks:
- Word count (3,000–5,000)
- Lived experience references
- Action Box count (≥3)
- Bridge transitions (≥2)
- Forbidden patterns
- Second person voice density
- G.R.O.W. framework elements
- Closing tone (no hype)

---

## Pricing Context

This is a $1,950 deliverable. Quality must reflect premium positioning — publication-ready, deeply personalised, actionable.
