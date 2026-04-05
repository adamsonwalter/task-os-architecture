# Bootstrap a new client workspace (“new company instance”)

Use this when you want a **new Git repo** for **one client’s** AI workflows: `company/` + `knowledge/` + `_starters/`, without ERP-style folder theatre.

---

## What to say in the IDE (copy-paste)

Use this as the user message to your assistant (Cursor, etc.):

```text
Read BOOTSTRAP.md and README.md in this meta-template repo. I need a new client company instance: a new Git repository with the correct folder structure. Run scripts/scaffold_client_workspace.sh with the path and client name I give you, OR create the same structure by hand if the script is not available. Before scaffolding, interview me using the “Data to collect” section in BOOTSTRAP.md. After scaffolding, tell me exactly which files to edit first and how to add the first workflow from _starters/.
```

Then answer the assistant’s questions. Provide:

- **Filesystem path** for the new repo (e.g. `~/GitHub/acme-workspace`)
- **Client legal / trading name** (string for `identity.md` title and README)

---

## What the assistant should do (checklist)

1. **Interview** the operator using **Data to collect** below (do not skip).
2. **Create** the repo using **either**:
   - **Preferred:** from the meta-template root, run:
     ```bash
     ./scripts/scaffold_client_workspace.sh "/absolute/path/to/new-repo" "Client Legal Name"
     ```
   - **Or** replicate the same tree: copy `templates/client-workspace/` contents, copy `_starters/` wholesale, substitute `{CLIENT_ENTITY}` and `{DATE}` in the template markdown files, add `.gitignore`, run `git init`.
3. **Initial commit** (if `user.name` / `user.email` are configured).
4. **Tell the operator** to open `company/identity.md` and `company/strategy.md` next, then copy a shape from `_starters/README.md` for the first real workflow.

---

## Data to collect (interview, in order)

Ask these before touching the filesystem. Use answers to fill `company/identity.md` and `company/strategy.md` (or leave placeholders where TBD).

| # | Question | Feeds |
|---|----------|--------|
| 1 | What is the **client’s legal or trading name** (exact string for titles)? | README, identity header |
| 2 | Where should the new repo live (**absolute path**)? | `scaffold_client_workspace.sh` arg |
| 3 | **One paragraph:** What does this business do, and who do they serve? | identity “Business snapshot” / “What this business does” |
| 4 | **Voice:** tone, words to use / avoid, any compliance or franchise rules? | identity |
| 5 | **Boundaries:** What must AI workflows **never** claim, invent, or do for this client? | identity “Hard boundaries” |
| 6 | **Strategy (near term):** top 2–3 priorities and what they are **not** doing this quarter? | strategy |
| 7 | Will **they** run workflows themselves, or **you** only? (affects how you wire `company/` vs OutcomesNow practice files.) | README note / your practice `knowledge/client-history/` |

Optional depth (if time):

- Primary customer and typical engagement shape.
- Links to brand guidelines or existing docs to mirror later in `references/` when the first workflow exists.

---

## After the repo exists

1. Edit **`company/identity.md`** — replace any remaining TBD sections with the interview answers.
2. Edit **`company/strategy.md`** — priorities and “saying no to.”
3. Add **`company/knowledge/client-history/{slug}.md`** in **your practice** meta-repo if you track all clients centrally—or keep engagement notes only inside the client repo; pick one habit.
4. **First workflow:** follow root `README.md` → **Operator playbooks** → copy `_starters/shape-a-light` or `shape-b-governed`, rename, answer the five questions in `_starters/README.md`.

---

## Not in scope for this scaffold

- No fake departments (`01_HR`, etc.).
- No Chief-of-Staff routing layer.
- No SAP-style module tree—only `company/`, `knowledge/`, `_starters/`, and future **sibling workflow folders**.

See `company/README.md` (“Fit for purpose, not SAP theatre”) and root `README.md` (“What you generate for a client”).
