---
name: publication-chart-skill
description: This skill should be used when the user asks for a publication-quality scientific figure or table, wants help choosing the right chart for results, needs a paper-ready figure/table generated with pubfig or pubtab, wants an existing figure/table reviewed and improved, or needs panel export and optional composite assembly for a paper figure.
version: 0.1.0
---

# Publication Chart Skill

## Goal

Use this skill to help an agent turn research results into **publication-grade figures and tables**.

The primary production stack is:

- **`pubfig`** for figures
- **`pubtab`** for publication tables

The skill is not generation-only. Its job is to carry the whole workflow from:

1. understanding the communication goal,
2. choosing the right visual/table form,
3. mapping to the correct toolchain,
4. generating concrete code or commands,
5. exporting paper-ready assets,
6. checking publication quality,
7. proposing targeted revisions.

## Use this skill when

Trigger this skill for requests like:

- “make a publication-quality figure”
- “choose the right chart for these results”
- “turn these results into a paper-ready figure”
- “make a benchmark / ablation / calibration / forest / heatmap / scatter / line / bar figure”
- “convert this Excel table into publication-ready LaTeX”
- “review and improve this scientific figure/table”
- “export panels for a paper figure”
- “prepare a figure + table pair for a results section”

## Primary contract

### Inputs

Expect some combination of:

- the scientific communication goal,
- available data shape,
- target venue or style constraints,
- whether the artifact is a figure, table, or mixed deliverable,
- optional existing assets such as code, spreadsheets, `.tex`, screenshots, or plot drafts.

### Outputs

The minimum useful output is:

- the recommended figure or table form,
- the recommended `pubfig` or `pubtab` route,
- a minimal runnable code snippet or CLI command,
- an export plan,
- a publication QA summary,
- and, when needed, a revision plan.

## Default workflow

### 1. Classify the task

First classify the request along three axes:

- **artifact type**: figure / table / mixed deliverable
- **maturity**: exploratory draft / publication-ready generation / revision of an existing artifact
- **structure**: single panel / multi-panel / figure-plus-table package

Do not jump into plotting code before the communication target is clear.

### 2. Choose the representation

Choose the representation based on the claim the user wants to communicate, not on novelty or visual flair.

Common families:

- **comparison** — bar, grouped scatter, line comparison, benchmark summary, companion table
- **ablation** — bar/grouped comparison, compact summary table, paired comparison, dumbbell
- **distribution** — box, violin, raincloud, histogram, density, ECDF, QQ
- **relationship** — scatter, bubble, contour2d, hexbin
- **trend** — line, area
- **evaluation / diagnostic** — ROC, PR, calibration, Bland–Altman, forest plot, volcano
- **composition / hierarchy** — donut, stacked ratio, radial hierarchy, circular grouped or stacked bars, UpSet
- **table** — formatted benchmark table, ablation table, dataset summary, error breakdown, appendix table

Avoid weak defaults:

- avoid pie/donut when exact comparison matters and a bar/table is clearer,
- avoid radar unless the comparison is genuinely profile-like and low-cardinality,
- avoid 3D, decorative gradients, and dense legends used only for style,
- avoid forcing every result into a figure when a publication table communicates the evidence better.

If the request is ambiguous, explicitly say what scientific claim the chart/table is supposed to support.

### 3. Map to the toolchain

Use this default mapping:

- **Figures** → `pubfig`
- **Tables** → `pubtab`
- **Mixed deliverables** → use both, with each artifact having a distinct role

Tool roles:

- `pubfig` is the default figure engine for publication-style scientific plots and clean export.
- `pubtab` is the default table engine for Excel ↔ LaTeX workflows, preview, and publication-ready table export.
- Figma or composite assembly is an **optional secondary branch** for multi-panel finishing. Do not make it the default if a normal single-panel figure is enough.

### 4. Generate artifact instructions

Prefer the smallest production-ready artifact first:

- minimal runnable Python for `pubfig`, or
- minimal CLI/Python for `pubtab`

Then add publication parameters only when they are justified by the task:

- labels, captions, width, export format, backend, panel packaging, preview, or composite layout.

Keep filenames and export suffixes explicit.

Good defaults:

- figures: start with one `pubfig` call + one `save_figure(...)`
- tables: start with one `pubtab xlsx2tex ...` or `pubtab.preview ...`
- mixed requests: clearly separate the figure route and table route

### 5. Run publication QA

After generation, check:

- title and legend density,
- axis labels and units,
- category ordering and baseline clarity,
- color accessibility and grayscale robustness,
- font / line-weight consistency,
- caption readiness,
- figure/table readability after downscaling,
- panel consistency for multi-panel figures,
- venue-fit issues such as width, crowding, or over-annotation.

The QA output should be concrete. Do not say “looks better” without naming why.

### 6. Revise

If the result is weak, revise by giving specific changes such as:

- switch chart family,
- remove chartjunk,
- reorder categories,
- move exact values into a table,
- split a crowded panel,
- add or simplify the caption,
- change export width,
- or convert the artifact from figure-first to table-first.

## Missing dependency behavior

If `pubfig` or `pubtab` is not available:

- do **not** fail immediately,
- degrade to a design/specification workflow,
- provide installation guidance,
- provide pseudocode or draft commands,
- and preserve the recommended visual or table structure so the user can execute it later.

That means the skill should still help with:

- chart/table selection,
- parameter planning,
- export planning,
- QA,
- and revision guidance.

## Composite assembly rule

Treat composite or Figma assembly as **secondary**:

- use it when the user explicitly wants a multi-panel paper figure,
- or when panel-level export and layout polishing are genuinely needed.

Do not escalate simple figure tasks into composite/Figma workflows by default.

## Output style rules

- Prefer direct, implementation-usable outputs.
- Explain the **why** of chart/table choice briefly, then give the runnable route.
- When a table is stronger than a figure, say so explicitly.
- When a figure is stronger than a table, say so explicitly.
- Keep revision guidance actionable and falsifiable.

## Recommended response shape

A strong response using this skill usually has 5 parts:

1. **Recommended artifact** — what figure/table type to use and why
2. **Tool route** — `pubfig`, `pubtab`, or both
3. **Minimal implementation** — runnable code or CLI
4. **Export plan** — filenames, formats, width/backend/preview choices
5. **Publication QA / next revisions** — what to check or change before submission

## Resources

Load these as needed:

- `references/workflow.md` — full end-to-end handoff checklist
- `references/chart-selection.md` — task-to-chart mapping and anti-patterns
- `references/pubfig-recipes.md` — shortest useful figure patterns and export routes
- `references/pubtab-recipes.md` — shortest useful table routes and backend guidance
- `references/publication-qa-checklist.md` — figure/table QA checklist
- `references/composite-assembly.md` — optional multi-panel and Figma branch

For prompt-shaped examples, see `examples/`.
