# Workflow Starter Templates

This folder is the **template kit** for the meta-structure in the root `README.md`. Use it when you spin up: **(1)** your own exploratory or internal workflows, **(2)** client workflows **you** run, or **(3)** client workflows **they** run—same shapes; different reference data, voice packs, and gates. Client contexts vary (industrial mid-market, franchises, consulting shops, etc.); the two shapes stay stable.

Two shapes. Pick the one that fits your workflow. Copy it. Rename it. Fill it in.

## Which Shape?

| Question | Shape A (Light) | Shape B (Governed) |
|---|---|---|
| How many instruction files? | **1** — everything in SKILL.md | **4+** — System, Policy, Output Mapping, Validation |
| Does the AI construct or extract? | Constructs through reasoning (generative) | Maps input to constrained output (extractive) |
| Can the AI invent content? | Yes, within voice/framework rules | No — only what reference data supports |
| Are there commercial hard stops? | Unlikely | Yes — things the AI must never do |
| Is there a golden template? | No — output structure is flexible | Yes — output format is locked |
| Does a human gate the output? | Light review | Multiple review gates before delivery |
| Example | Justine SBR, manu-lp | GND Quotes, Compliance workflows |

**If in doubt, start with Shape A.** You can always add governance files later. You can't easily remove governance files once people depend on them.

## After Copying

1. Copy the shape folder to the same level as `company/`
2. Rename it to your workflow name
3. Follow the HOW_TO_USE.md inside the shape folder
4. Wire context in your SKILL.md: reference `../../company/identity.md` and `knowledge/` when practice positioning applies; use workflow-local references when the client’s brand and rules should dominate (especially for client-run handoffs)

## The 5 Questions (Answer Before Building Either Shape)

1. **What is the trigger and input?** What initiates this, what does the input look like?
2. **What reference data grounds the output?** What must the AI look up, never invent?
3. **What can the AI NEVER do?** At least 5 domain-specific prohibitions.
4. **What does the output look like exactly?** Every section/field defined.
5. **In what 5-6 ways can this fail silently?** Not crashes — correct-looking but wrong outputs.
