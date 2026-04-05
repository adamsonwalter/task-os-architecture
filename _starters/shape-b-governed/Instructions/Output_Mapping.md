# Output Mapping

## Purpose

This file is the output contract. It defines every section, field, or component in the deliverable — what it contains, where the data comes from, and what happens when the source is missing.

This file is written BEFORE the output template is built. The template implements this contract, not the other way around.

## Output Format

**Deliverable type**: [HTML page / Word doc / Excel workbook / PDF / Markdown report / other]
**Template location**: `templates/[filename]`
**Output location**: `jobs/{slug}/builds/[filename]`

## Field-Level Contract

[NOTE: One row per section or field in your deliverable. For generative workflows, these are the sections of the page/document. For extractive workflows, these are the rows/fields of the template.]

| Section / Field | Source Basis | If Source Missing | Format |
|---|---|---|---|
| [Field 1] | [Extracted from input / Looked up in Reference / AI synthesis within rules] | [LEAVE BLANK / FLAG / HARD STOP] | [Format spec] |
| [Field 2] | [Source] | [Missing action] | [Format] |
| [Field 3] | [Source] | [Missing action] | [Format] |

## Allowed States

Every field in the output exists in exactly one of three states:

| State | Meaning | Visual Marker |
|---|---|---|
| **POPULATE** | Defensible source exists. Value is written. | None — clean output |
| **FLAG** | Value exists but source is provisional. | [Define your flag marker: yellow highlight, asterisk, "(provisional)", etc.] |
| **LEAVE BLANK** | No defensible source. Do not populate. Do not estimate. | Empty cell / "—" / omitted section |

## Pre-Population Checklist

Before writing ANY value to the output, confirm:
- [ ] Source is identified and traceable
- [ ] No double-counting (same data mapped to multiple fields)
- [ ] No invented data masquerading as extracted data
- [ ] Format matches the specification in this file
- [ ] The field's allowed state matches the evidence available

## Output Summary Requirement

Every run MUST also produce `jobs/{slug}/_system/run_log.md` entry containing:
- What was populated and from what source
- What was flagged and why
- What was left blank and why
- What assumptions were made
- What failed or was unexpected

---

*[Delete all `[NOTE:]` annotations and `[PLACEHOLDER]` text before going live.]*
