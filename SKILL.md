---
name: publication-chart-skill
description: This skill should be used when the user asks for a publication-quality scientific figure or table, wants help choosing the right chart for results, needs a paper-ready pubfig>=0.3.0 CLI or pubtab workflow, wants a figure + companion table for a results section, wants an Excel sheet turned into publication-ready LaTeX, or wants an existing scientific figure/table reviewed and upgraded.
version: 0.3.0
---

# Publication Chart Skill

## Goal

Use this skill to turn research results into **publication-grade figures and tables**.

Primary production stack:

- **`pubfig>=0.3.0` JSON CLI** for figures
- **`pubtab`** for publication tables

Default delivery chain:

1. identify the scientific communication goal,
2. decide figure / table / mixed deliverable,
3. choose the strongest representation,
4. route to `pubfig`, `pubtab`, or both,
5. generate a runnable route,
6. export paper-ready assets,
7. run publication QA,
8. propose revisions when needed.

## Use this skill when

Trigger this skill for requests like:

- “make a publication-quality figure”
- “choose the right chart for these results”
- “turn these results into a paper-ready figure”
- “make a benchmark / ablation / calibration / forest / heatmap / scatter / line / bar figure”
- “make a benchmark / appendix / ablation table from Excel”
- “convert this Excel table into publication-ready LaTeX”
- “prepare one summary figure plus one companion table for the results section”
- “review and improve this scientific figure/table”
- “I already have a weak chart / screenshot / draft plot — make it publication-ready”
- “export panels for a paper figure”

## Do not use this skill for

Do **not** use this skill when the task is mainly:

- manuscript prose writing,
- statistical testing without artifact design,
- raw exploratory analysis with no publication deliverable,
- Figma-first layout work before the figure or table content is solid.

Composite assembly is a **secondary branch**. Do not escalate ordinary figure tasks into panel/Figma workflows by default.

## Primary contract

### Inputs

Expect some combination of:

- the scientific communication goal,
- available data shape,
- venue or style constraints,
- whether the artifact is a figure, table, or mixed deliverable,
- optional assets such as code, spreadsheets, `.tex`, screenshots, or draft plots,
- whether the task is first-draft generation, publication-ready export, or review/revision.

### Minimum useful outputs

A strong response should provide:

- the recommended artifact form,
- the recommended `pubfig` CLI / `pubtab` route,
- a minimal runnable JSON spec, CLI command, or code snippet,
- explicit output filenames and formats,
- a publication QA summary,
- a revision plan when the current artifact is weak.

## Default workflow

### 0. Probe environment and task state

Before generating anything, identify:

- whether `pubfig>=0.3.0` or `pubtab` is available,
- whether the user already has code, spreadsheets, `.tex`, screenshots, or draft plots,
- whether the deliverable is fresh generation or revision,
- whether the result needs visual pattern perception, exact value lookup, or both.

Keep this step light. Prefer the bundled helper script when runnable execution matters.

If a required dependency is missing, install it into the active environment first. The canonical pip commands are:

- `python -m pip install --upgrade "pubfig>=0.3.0"`
- `python -m pip install --upgrade pubtab`

When the bundled helper script is available, it is still the preferred route:

- `python3 scripts/ensure_publication_tooling.py --require pubfig --json`
- `python3 scripts/ensure_publication_tooling.py --require pubtab --json`

After installation:

- re-check availability,
- continue with the runnable workflow if install succeeds,
- otherwise degrade to a design/specification answer instead of failing.

For `uv`-managed and other fallback variants, see `references/execution-and-verification.md`.

### 1. Classify the task

Classify along these axes:

- **artifact type** — figure / table / mixed deliverable
- **maturity** — exploratory draft / publication-ready generation / revision
- **structure** — single panel / multi-panel / figure-plus-table package
- **evidence mode** — pattern perception / exact lookup / both

Do not jump into plotting before the communication target is clear.

### 2. Choose the representation

Choose the representation from the scientific claim, not from visual novelty.

Useful families:

- **comparison** — grouped scatter, bar, line comparison, benchmark summary, companion table
- **ablation** — grouped comparison, dumbbell, paired comparison, compact table
- **distribution** — box, violin, raincloud, histogram, density, ECDF, QQ
- **relationship** — scatter, bubble, contour2d, hexbin
- **trend** — line, area
- **evaluation / diagnostic** — calibration, ROC, PR, Bland–Altman, forest plot, volcano
- **composition / hierarchy** — UpSet, stacked ratio, donut, radial hierarchy, circular grouped or stacked bars
- **table** — benchmark table, ablation table, dataset summary, appendix table, error breakdown

Avoid weak defaults:

- avoid pie/donut when a bar or table communicates exact comparison better,
- avoid radar unless the claim is genuinely low-cardinality and profile-like,
- avoid 3D, decorative gradients, and style-only complexity,
- avoid forcing exact-value heavy results into a figure when a table is stronger.

For detailed task-to-chart rules, read `references/chart-selection.md`.

### 3. Map to the toolchain

Default mapping:

- **Figures** → `pubfig>=0.3.0` JSON CLI by default
- **Tables** → `pubtab`
- **Mixed deliverables** → use both, with distinct communication roles

Route rules:

- prefer the `pubfig` JSON CLI for agent-generated figures,
- use `pubfig` Python API only when the user is explicitly working in a notebook/script or needs unsupported custom logic,
- prefer `pubtab` CLI for file-driven table workflows,
- keep figure and table responsibilities separate in mixed requests,
- treat panel export / composite assembly as optional downstream work.

For exact route selection and verification behavior, see:

- `references/workflow.md`
- `references/execution-and-verification.md`
- `references/pubfig-recipes.md`
- `references/pubtab-recipes.md`

### 4. Generate the smallest runnable artifact

Prefer the smallest production-ready route first:

- for figures: one `figure.spec.json` plus `pubfig validate-spec` and `pubfig render`,
- for tables: one `pubtab` route that produces a previewable `.tex` or rendered preview,
- for mixed requests: one figure route plus one table route, clearly separated.

Keep filenames and export formats explicit.

For figure-specific export patterns such as `save_figure`, `batch_export`, and `export_panels`, use `references/pubfig-recipes.md`.

### 5. Define the delivery contract

For every response, make these explicit when possible:

- the scientific claim the artifact supports,
- which artifact type was chosen and why,
- which part is handled by `pubfig` and which by `pubtab`,
- output filenames and formats,
- whether the artifact is draft / final / revision,
- what still needs user-provided data or manuscript context.

### 6. Run publication QA

After generation, check:

- title and legend density,
- axis labels and units,
- category ordering and baseline clarity,
- color accessibility and grayscale robustness,
- font and line-weight consistency,
- caption readiness,
- readability after downscaling,
- panel consistency for multi-panel exports,
- venue-fit issues such as width, crowding, or over-annotation.

The QA output must be concrete. Name the actual issue and the actual fix.

For a fuller checklist, see `references/publication-qa-checklist.md`.

### 7. Revise when the result is weak

Typical revisions include:

- switching chart family,
- removing chartjunk,
- reordering categories,
- moving exact values into a table,
- splitting a crowded panel,
- simplifying or strengthening the caption,
- changing export width,
- converting the deliverable from figure-first to table-first.

## Missing dependency behavior

If `pubfig>=0.3.0` or `pubtab` is unavailable:

- do not fail immediately,
- try the bundled install/probe route first,
- report the dependency state clearly,
- continue with the runnable workflow after a successful install,
- otherwise provide a design/specification answer with pseudocode or draft commands,
- still preserve artifact choice, QA, and revision guidance.

All concrete probe/install commands live in `references/execution-and-verification.md`.

## Output style rules

- Prefer direct, implementation-usable outputs.
- Briefly explain **why** this figure or table form is appropriate, then give the route.
- When execution matters, include a short environment status block.
- Say explicitly when a table is stronger than a figure.
- Say explicitly when a figure is stronger than a table.
- When both are needed, assign them different roles.
- Keep revision guidance actionable and falsifiable.

## Recommended response shape

A strong response usually has 6 parts:

1. **Artifact decision** — figure / table / paired deliverable, and why
2. **Tool route** — `pubfig>=0.3.0` JSON CLI, `pubtab`, or both
3. **Minimal implementation** — runnable JSON spec, CLI, or code
4. **Export plan** — filenames, formats, width/backend/preview choices
5. **Publication QA** — what to verify before paper submission
6. **Revision plan** — what to change if the current artifact is weak

## Resources

Load these as needed:

- `references/workflow.md` — decision order, delivery contract, figure/table split rules
- `references/chart-selection.md` — task-to-chart mapping and anti-patterns
- `references/execution-and-verification.md` — environment probing, install behavior, runnable verification
- `scripts/ensure_publication_tooling.py` — bundled probe + auto-install helper for `pubfig>=0.3.0` / `pubtab`
- `references/pubfig-recipes.md` — agent-first JSON CLI figure specs and export patterns
- `references/pubtab-recipes.md` — shortest useful table routes and backend guidance
- `references/source-guides/pubfig-architecture.md` — package layout and figure-generation boundaries from source
- `references/source-guides/pubfig-api-map.md` — stable public pubfig surface and chart-family map from `__init__.py`
- `references/source-guides/pubfig-export-flow.md` — figure export, publication sizing, and panel-export flow from source
- `references/source-guides/pubtab-architecture.md` — package layout and forward/reverse conversion architecture from source
- `references/source-guides/pubtab-cli-api-flow.md` — CLI-to-API control flow and batch/sheet behavior from source
- `references/source-guides/pubtab-backend-and-preview.md` — backend/theme split and preview compile pipeline from source
- `references/publication-qa-checklist.md` — figure/table QA checklist
- `references/composite-assembly.md` — optional multi-panel and Figma branch

For prompt-shaped examples, see `examples/`.
