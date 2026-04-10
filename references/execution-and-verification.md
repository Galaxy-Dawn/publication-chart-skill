# Execution and Verification

## Goal

Turn a high-level publication figure/table request into a route that is actually runnable in the current environment.

## Minimum environment probe

Prefer the lightest useful checks.

### Check `pubfig`

```bash
python -c "import pubfig; print(pubfig.__version__)"
```

### Check `pubtab`

```bash
pubtab --help
```

or

```bash
python -c "import pubtab; print(pubtab.__version__)"
```

Do not spend the whole turn on setup if the user primarily needs design guidance. Just identify whether the route is executable now or should degrade gracefully.

## Route selection

### Use `pubfig` when

- the task is primarily a figure,
- the user already has Python data structures,
- the result is a plot family already covered by `pubfig`,
- export quality matters immediately.

### Use `pubtab` when

- the task is primarily a publication table,
- the input is an Excel workbook, a `.tex` table, or a file-driven workflow,
- the reader needs exact values,
- previewing the table before manuscript insertion matters.

### Use both when

- the figure carries the visual pattern,
- the table preserves exact benchmark values,
- the paper section benefits from one fast visual plus one exact-value artifact.

## First runnable verification

### `pubfig`

After generating a minimal figure route, the first useful verification is:

- can the code execute,
- does `save_figure(...)` or `batch_export(...)` produce the expected files,
- do output suffixes match the intended formats.

### `pubtab`

After generating a minimal table route, the first useful verification is:

- can `xlsx2tex` or `tex2xlsx` run,
- can `preview` render PNG or PDF,
- does the chosen backend (`tabular` or `tabularray`) match the manuscript need.

## Current practical notes

### `pubfig`

Useful export primitives include:

- `save_figure(...)`
- `batch_export(...)`
- `export_panel(...)`
- `export_panels(...)`

Use panel export only when multi-panel assembly is truly needed.

### `pubtab`

Useful file-oriented routes include:

- `pubtab xlsx2tex ...`
- `pubtab tex2xlsx ...`
- `pubtab preview ...`

Remember:

- `xlsx2tex` exports all sheets by default when `--sheet` is not set,
- `preview` can render PNG or PDF,
- `--latex-backend tabularray` should be chosen only when the manuscript/backend requires `tblr`,
- when preview reliability is the immediate priority, validate the table body first and add final `caption` / `label` in a separate manuscript-facing step if needed.

## Graceful degradation

If the tool is missing, still provide:

- the artifact recommendation,
- the exact files the user should prepare,
- a draft CLI or Python route,
- the export targets,
- and the publication QA checklist.

## Default output wording

When the route is runnable now, say:

- what to run,
- what files should appear,
- what to inspect next.

When the route is not runnable now, say:

- what is missing,
- what the intended route will be after install,
- and what design decision can already be locked in today.
