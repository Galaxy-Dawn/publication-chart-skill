# Execution and Verification

## Goal

Turn a high-level publication figure/table request into a route that is actually runnable in the current environment.

## Minimum environment probe

Prefer the lightest useful checks.

### Preferred bundled probe

```bash
python3 scripts/ensure_publication_tooling.py --require pubfig --json
python3 scripts/ensure_publication_tooling.py --require pubtab --json
```

The helper probes availability, force-installs missing dependencies into the active interpreter, and returns the post-install status. For `pubfig`, it enforces `pubfig>=0.3.0`.

### Equivalent manual checks

```bash
python -c "import pubfig; print(pubfig.__version__)"   # must be >=0.3.0
pubfig --version
pubfig list-kinds
python -c "import pubtab; print(pubtab.__version__)"
pubtab --help
```

Do not spend the whole turn on setup if the user primarily needs design guidance. Identify whether the route is executable now or should degrade gracefully.

## Automatic installation policy

If a dependency is missing or `pubfig` is older than `0.3.0`, install or upgrade it automatically before continuing when the task requires real execution.

### Preferred bundled route

Use the bundled helper when it is present:

```bash
python3 scripts/ensure_publication_tooling.py --require pubfig
python3 scripts/ensure_publication_tooling.py --require pubtab
```

The helper chooses `uv pip install --python <active-python> --upgrade ...` when the project is clearly `uv`-managed, and otherwise falls back to `python -m pip install --upgrade ...`.

### Equivalent manual install commands

```bash
uv pip install --python "$VIRTUAL_ENV/bin/python" --upgrade "pubfig>=0.3.0"
uv pip install --python "$VIRTUAL_ENV/bin/python" --upgrade pubtab
python -m pip install --upgrade "pubfig>=0.3.0"
python -m pip install --upgrade pubtab
```

### Required follow-up

After installation:

1. re-run the availability probe,
2. confirm `pubfig list-kinds` works for figure tasks,
3. report the updated environment status,
4. continue with the runnable figure/table workflow.

If installation fails, capture the exact error and fall back to design/specification guidance.

## Route selection

### Use the `pubfig>=0.3.0` JSON CLI when

- the task is primarily a figure,
- the user needs an agent/automation-friendly route,
- the result is a plot family listed by `pubfig list-kinds`,
- export quality matters immediately.

The default agent route is:

```bash
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

Use the Python API only when the user is already working inside a notebook/script or the required logic is not expressible in the JSON spec.

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

```bash
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

Check that:

- `validate-spec` returns `ok: true`,
- `render` returns `ok: true`,
- `output_paths` match the requested files,
- the files exist on disk,
- suffixes match the intended formats.

For headless agent/CI environments, prepend `MPLBACKEND=Agg` if Matplotlib attempts to use a GUI backend:

```bash
MPLBACKEND=Agg pubfig render figure.spec.json
```

### `pubtab`

After generating a minimal table route, the first useful verification is:

- can `xlsx2tex` or `tex2xlsx` run,
- can `preview` render PNG or PDF,
- does the chosen backend (`tabular` or `tabularray`) match the manuscript need.

## Current practical notes

### `pubfig`

Useful JSON export modes include:

- `save_figure` for one explicit file,
- `batch_export` for multiple formats from one figure,
- `export_panels` for panel directories used in composite/Figma handoff.

These CLI modes call the same underlying export primitives as the Python API. Prefer the CLI for agent-generated figures because the spec is reviewable, repeatable, and easy to validate before writing final assets.

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

If the tool is missing:

- first try the bundled auto-install helper,
- if that route is unavailable, use the manual install commands above,
- if installation still fails, provide:
  - the artifact recommendation,
  - the exact files the user should prepare,
  - a draft JSON spec, CLI route, or Python fallback,
  - the export targets,
  - and the publication QA checklist.

## Default output wording

When the route is runnable now, say:

- what to run,
- what files should appear,
- what to inspect next.

When the route is not runnable now, say:

- what is missing,
- which helper command or install command was attempted,
- whether the install succeeded or failed,
- what the intended route will be after install,
- and what design decision can already be locked in today.
