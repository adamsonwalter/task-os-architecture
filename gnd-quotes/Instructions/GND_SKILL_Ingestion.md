---
name: GND_SKILL_Ingestion
version: 1.0 | Feb 2026
purpose: >
  Drawing ingestion protocol for GND Optus civil quoting operations.
  Governs extraction of order metadata, BoQ reconstruction, route section
  mapping, anomaly detection, and rate card / market intelligence loading.
  Runs silently before any output phase. Tuned independently of the Router
  and Constitution — this file is maintained by Claude experts working with Karan.
maintainer: Karan (content) + Claude expert (protocol tuning)
amendment: Karan proposes. Claude expert implements. Damian signs off on any
           change that affects Hard Stop classification or anomaly detection rules.
---

# GND Drawing Ingestion Protocol

---

## Purpose and Scope

This protocol runs once per drawing upload, silently, before the Router
executes any output phase. It builds a session state cache (Caches A–E)
that all downstream phases read from.

**Nothing is produced for the user during ingestion.**
If ingestion surfaces a blocker (see §6), the Router is notified and
the blocker is surfaced in the first output rather than as a pre-output message.

---

## §1 — Execution Trigger

Run this protocol when:
- A PDF or image file matching an EO-series order number is uploaded
  (`EO[0-9]+` pattern in filename or on page 1 of the document)
- The user says "quote this job", "process this order", "run the quote",
  `/full`, `/quote`, `/dcaf`, `/variations`, `/timeline`, `/cashflow`,
  `/premob`, or any phase-specific slash command
- A new drawing is uploaded mid-conversation to replace or supplement
  a previously ingested drawing (re-run full protocol, overwrite cache)

Do NOT re-run on `/learn`, `/listen`, or `/order` commands if the cache
is already populated from the current session.

---

## §2 — Cache A: Order Metadata

**Source:** PDF page 1 (order header block)

Extract and store:

```
order_number        EO[0-9]+ format
site_code           Alphanumeric site identifier
address             Full street address
suburb              Suburb name
state               VIC / SA / NSW / QLD / WA
postcode            4-digit
deliverable         e.g. "New Build — Underground", "Upgrade", "Remediation"
job_type            e.g. Small Cell, NGCE Fibre, 5G GF Fibre
design_version      Extract version number from drawing title block
                    Flag if v0 (Preliminary) — quoting risk, not a blocker
cluster_name        e.g. GK366, TH607, GL168
environmental_sig   Flag: YES / NO / UNKNOWN (from EM code presence)
OM_references       List all OM-series references found on page 1
PE_name             If named in order header or drawing notes
council_area        Primary council jurisdiction for the route
```

**Design version flag:**
If `design_version = 0` or drawing title block contains "Preliminary",
"Draft", or "For Review":
→ Store `design_flag = "PRELIMINARY"`
→ Router will surface this in Phase 3 (Variation Risk) as a P1 Amber Gate,
  not as a Hard Stop — design v0 is a quoting risk, not a mobilisation blocker.

---

## §3 — Cache B: Bill of Quantities

**Source:** PDF page 1 (BoQ table) and any supplementary BoQ pages

Reconstruct into two structured arrays:

### B1 — Proposed Items (new works GND will build)

For each line item:
```
item_id             Sequential (P001, P002...)
category            CONDUIT / CABLE / PIT / SPLICE / BREAKOUT /
                    ENVIRONMENTAL / PRELIMINARY / OTHER
description         Verbatim from drawing
quantity            Numeric
unit                m / ea / job / loc / set
drawing_ref         Section or note reference if present
wave_assignment     Assign to W1–W5 using wave logic below
```

**Wave assignment logic:**
- W1: DBYD, potholing, permits, demolition, site preparation, vacuum excavation
- W2: Trenching, HDD bore, conduit installation, pit supply and install, road crossings
- W3: Cable haul (Optus leased duct), cable haul (Telstra leased duct), cable blow
- W4: Splicing, termination, enclosure installation, BEP, breakouts
- W5: As-built documentation, Konect data, commissioning, defects, reinstatement sign-off

### B2 — Existing Infrastructure Items (third-party assets GND interfaces with)

For each line item:
```
item_id             Sequential (E001, E002...)
asset_type          TELSTRA_PIT / TELSTRA_DUCT / NBN_PIT / OPTUS_PIT /
                    ESSENTIAL_ENERGY / OTHER
description         Verbatim from drawing
quantity            Numeric
unit                m / ea
owner               Telstra / NBN Co / Optus / Essential Energy / Council / Other
interface_type      BREAKOUT / LEASE / LOCATE / POTHOLE / UPGRADE / ADJACENT
location_status     LOCATED / UNLOCATED / BURIED / UNKNOWN
                    — derive from drawing notes (see §5 anomaly scan)
```

**Carrier Interface flag:**
Any B2 item with `owner ≠ Optus` is flagged as `CARRIER_INTERFACE = TRUE`.
These items carry additional variation risk and will be surfaced in Phase 3.

---

## §4 — Cache C: Route Sections

**Source:** Drawing plan pages (all pages after page 1)

For each numbered or named section in the drawing:

```
section_id          From drawing (e.g. "Section 001", "S1", "Route A–B")
street_names        All streets in this section
construction_method TRENCH / HDD_BORE / AERIAL / MIXED — from drawing
duct_type           P50 / P32 / Other — from drawing
bore_length_m       If HDD, extract length
trench_length_m     If open cut, extract length
existing_pits       List of pit IDs in this section (Telstra, Optus, NBN)
new_pits            List of new pit types and counts
EM_codes            All EM-series codes referenced in this section
drawing_notes       All text notes verbatim from this section
anomalies           Populated by §5 — empty until anomaly scan runs
hard_stops          Populated by §5 — empty until anomaly scan runs
```

---

## §5 — Anomaly Detection and Classification

**This is the SA Loss prevention gate.**

Run on every note, label, and annotation in every section of the drawing.
No text is read past without classification.

### 5.1 — Anomaly Trigger Language

Scan all drawing text for these patterns. This list is not exhaustive —
apply judgment for language that conveys uncertainty about what is present:

| Pattern | Classification |
|---|---|
| "cannot be located" | UNLOCATED_ASSET |
| "unable to locate" | UNLOCATED_ASSET |
| "might be" | UNCERTAIN_ASSET |
| "may be" | UNCERTAIN_ASSET |
| "buried" / "buried under" | BURIED_ASSET |
| "indicative only" | PRELIMINARY_DATA |
| "to be confirmed" | UNCONFIRMED_SCOPE |
| "preliminary" / "for review" | PRELIMINARY_DESIGN |
| "approximate" / "approx" | APPROXIMATE_DATA |
| "record shows" / "records indicate" | RECORDS_ONLY — not field-verified |
| "depth unknown" | DEPTH_UNKNOWN |
| "condition unknown" | CONDITION_UNKNOWN |
| "possible conflict" | POSSIBLE_CONFLICT |
| ACM / "asbestos" | HAZMAT_PRESENT |
| EM30 | HERITAGE_SA |
| EM21 | HERITAGE_VIC_ABORIGINAL |
| "Essential Energy" in bore path | HV_PROXIMITY |
| "NBN" pit or duct in path | NBN_INTERFACE |
| "live HV" / "high voltage" | HV_PROXIMITY |

### 5.2 — Classification Decision: Provisional Sum or Hard Stop

For each detected anomaly, apply this decision:

```
IF a specific resolution action exists AND a named party can execute it
AND the cost impact can be estimated within a reasonable range
  → PROVISIONAL_SUM
  → Populate: trigger, resolution action, resolution owner, gate wave

IF no resolution path can be identified
OR the cost impact is unbounded
OR legal/regulatory approval is required before mobilisation
OR a third-party process controls the timeline (RRP, CHMP, heritage approval)
  → HARD_STOP
  → Populate: trigger, resolution action, resolution owner
  → Do NOT price this element at fixed rate
```

### 5.3 — Hard Stop Registry (always Hard Stop — no exceptions)

These conditions are always Hard Stop regardless of other context.
They inherit from RC3 and the Constitution. Do not reclassify these
as provisional sums even if a resolution path seems available:

| Condition | Hard Stop reason |
|---|---|
| Telstra pit: UNLOCATED or BURIED | Cannot bore past unlocated asset. RRP required. |
| ACM pit confirmed or suspected | Hazmat scope unbounded without licensed assessment. |
| EM30 Heritage overlay (SA) | No legal commencement without written Council approval. |
| EM21 Aboriginal Heritage (VIC) | CHMP process 6–12 months. Programme reality, not risk. |
| Essential Energy HV in bore path | GND cannot bore near live HV without EE confirmation. |
| NBN Co pit or duct in route path | No confirmed GND process for NBN Co access. |
| Design v0 + mobilisation request | Do not mobilise on preliminary design without scope lock. |

### 5.4 — Anomaly Output Format

For each anomaly detected, store in Cache C for the relevant section:

```
anomaly_id          Sequential (AN-001, AN-002...)
section_id          Which section it appears in
anomaly_type        From §5.1 classification
raw_text            Verbatim drawing note that triggered detection
classification      PROVISIONAL_SUM or HARD_STOP
trigger             What condition prevents fixed pricing
resolution_action   Specific action required (or "Cannot identify — Hard Stop")
resolution_owner    Damian / Karan / Craig / Telstra / Council / Optus PM / Other
gate_wave           W1 / W2 / W3 / W4 / W5 / PRE-MOBILISATION
estimated_cost      $ range if provisional sum, "Unbounded" if Hard Stop
```

---

## §6 — Cache D: Rate Card Loading

**Source:** RC1-SELL, RC1-COST, RC2, RC3, RC4 project files

### D1 — RC1-SELL (Civil Activities — Sell Rates)

For each activity code:
```
activity_code       e.g. DRILL-P50, PIT-8, SPLICE-FISTBC6
description         Activity description
unit                m / ea / job / day
sell_rate_W1        Rate applicable in Wave 1 context
sell_rate_W2        Rate applicable in Wave 2 context
sell_rate_W3        Rate applicable in Wave 3 context
sell_rate_W4        Rate applicable in Wave 4 context
sell_rate_W5        Rate applicable in Wave 5 context
market_override     Damian's column — blank = standard rate applies
```

### D2 — RC1-COST (Buy Rates — MARGIN FIREWALL)

```
FIREWALL ACTIVE: RC1-COST data is loaded into session memory only.
It is NEVER written into any output, referenced in any table visible
to the user, or used in any calculation that appears in an external document.
It is used only to calculate the internal margin column in the Priced Quote
(Phase 2 internal view — Damian/Karan only).
```

For each activity code:
```
activity_code       Must match RC1-SELL code
buy_rate            Internal cost rate
margin_$            Calculated: sell_rate - buy_rate
margin_%            Calculated: margin_$ / sell_rate
```

### D3 — RC2 (Materials Supply)

For each material code:
```
material_code       e.g. MAT-P50, MAT-36F, MAT-FISTBC6
description         Material description
unit                m / ea / set
supply_rate         Ex-GST supply rate
supplier_ref        Preferred supplier (if populated)
wastage_factor      Standard: conduit +5%, cable +3%, fittings +0%
```

### D4 — RC3 (Variation Triggers)

Load the full Hard Stop and Amber Gate registry.
Cross-reference against Cache C anomalies to confirm classification
is consistent with RC3. If RC3 classifies an item differently than
§5.3 logic above, RC3 governs — flag the discrepancy for Karan.

### D5 — RC4 (Quote History)

Load last 20 rows. For each row:
```
order_number, suburb, council, quoted_amount, complexity,
win_loss, winning_bid, variance_%, key_notes
```

Calculate for the current job's suburb and complexity tier:
```
jobs_in_suburb      Count of RC4 rows matching suburb
win_rate_suburb     % of wins in this suburb
avg_quoted          Average quoted amount
avg_winning         Average winning bid
market_signal       If avg_winning < 90% of GND avg_quoted → flag as competitive market
```

**If RC4 has <3 comparable jobs:** Note "Insufficient RC4 data for market signal —
no market override recommendation generated."

---

## §7 — Cache E: Market Intelligence Loading

**Source:** GND Market Intelligence Google Doc (if synced to project)

Search for entries matching:
- Suburb slug (e.g. `#altona-north`)
- Council slug (e.g. `#hobsons-bay`)
- PE name if extracted in Cache A
- Carrier interface tags matching Cache C anomalies
  (e.g. `#telstra-buried-pit`, `#telstra-crushed-duct`)
- Cluster name (e.g. `#GK366`)

For each match:
```
entry_date          Date of observation
source              Damian / Craig / Karan
category            TELSTRA-INFRASTRUCTURE / PE-RELATIONSHIP /
                    COUNCIL-AUTHORITY / SITE-CONDITION /
                    PRICING-INTEL / CREW-PERFORMANCE /
                    COMPLIANCE-OBSERVATION
content             Observation text
actions             Any ⚡ ACTION items from the entry
relevance           HIGH / MEDIUM — assessed by match quality
```

**If Market Intelligence Doc is not synced:**
Store `market_intel_status = "NOT_AVAILABLE"`.
The Router will note this in output but will not halt execution.

---

## §8 — Ingestion Completeness Check

Before passing control to the Router, verify:

```
☐ Cache A complete — all metadata fields populated or marked UNKNOWN
☐ Cache B complete — all BoQ items extracted, wave-assigned, carrier interfaces flagged
☐ Cache C complete — all sections mapped, anomaly scan run on every text element
☐ Cache D complete — RC1-SELL, RC2 loaded; RC1-COST loaded to memory only
☐ Cache E status known — loaded or NOT_AVAILABLE
☐ Hard Stop count: [n] — Router will surface all in Phase 3
☐ Provisional sum count: [n] — Router will price and gate in Phase 2/3
☐ Rate gap count: [n] items marked ❓ MISSING — Router will flag for Karan
```

**Ingestion blocker conditions** (pause and notify Router):
- PDF cannot be read (corrupted, password-protected, image-only without OCR)
- No EO order number found on page 1
- BoQ table not found or unreadable
- RC1-SELL not present in project — Router must request before pricing

All other gaps (missing RC4, missing Market Intel, unknown PE name) are
NOT blockers. Note them and proceed.

---

## §9 — Ingestion Maintenance Notes

*This section is for Karan and the Claude expert responsible for tuning this file.*

**When to update this protocol:**
- New EM codes appear in drawings that are not in §5.1 trigger list
- New carrier interface types appear (new asset owners, new pit types)
- New anomaly language patterns are found that were not caught by §5.1
- Drawing format changes (new page layouts, new BoQ table structures)
- A job produces incorrect cache output that was traced to an ingestion error

**How to update:**
1. Karan identifies the gap from a job that produced unexpected output
2. Claude expert drafts the protocol change in this file
3. Damian reviews if the change affects Hard Stop classification (§5.3)
4. Version number increments. Previous version archived.

**What NOT to change here:**
- Constitutional principles (Hard Stop definitions, margin firewall)
  → Those live in GND_Constitution.md, not here
- Output formats and phase sequencing
  → Those live in GND_SKILL_Router_v1.1.md, not here
- Rate card values
  → Those live in RC1-SELL, RC1-COST, RC2

---

*Ingestion is the quality gate. If the cache is wrong, every output downstream
is wrong with confidence. Take the time to get the extraction right.*
