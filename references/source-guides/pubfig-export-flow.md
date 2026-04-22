# pubfig export flow (source-driven)

This guide explains how `pubfig>=0.3.0` moves from a JSON render spec to paper-ready files.

Primary source files:

- `pubfig/src/pubfig/render_spec.py`
- `pubfig/src/pubfig/export/io.py`
- `pubfig/src/pubfig/export/panels.py`
- `pubfig/src/pubfig/specs.py`

## 1. Agent-facing export contract

### Source facts

`render_spec.py` accepts these export modes:

- `save_figure`
- `batch_export`
- `export_panels`

For a single figure, the spec uses `plot` plus either `save_figure` or `batch_export`. For a panel package, the spec uses `panels` plus `export_panels`.

### Operational interpretation

Agents should describe export through the JSON `export` block, then validate and render:

```bash
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

## 2. `save_figure` mode

Use this mode for one explicit manuscript-facing file:

```text
"export": {
  "mode": "save_figure",
  "path": "figure1.pdf",
  "spec": "nature",
  "width": "single"
}
```

### Source facts

The underlying `save_figure(...)` requires an explicit suffix and supports publication sizing through `spec`, `width`, `height_mm`, and `aspect_ratio`.

### Operational interpretation

Write `figure1.pdf`, `figure1.svg`, or `figure1.png` explicitly. Do not rely on an implicit default suffix.

## 3. `batch_export` mode

Use this mode when the same figure needs multiple output formats:

```text
"export": {
  "mode": "batch_export",
  "base_path": "figure1",
  "formats": ["pdf", "svg", "png"],
  "spec": "nature",
  "width": "single",
  "dpi": 300
}
```

### Source facts

The underlying `batch_export(...)` appends each format suffix, applies publication-aware layout for each target, and restores the in-memory figure state after export.

### Operational interpretation

Use this for paper PDF, editable SVG, and review PNG from one validated figure spec.

## 4. Publication sizing path

### Source facts

`export/io.py` uses `FigureSpec` definitions from `specs.py`. Built-in specs include `nature`, `science`, and `cell`. Width can be `single`, `double`, or a numeric millimeter value. Height can be explicit or derived from `aspect_ratio`.

### Operational interpretation

For paper-ready figures, specify at least:

- `spec`
- `width`
- output suffix or formats

For quick drafts, keep the export block minimal but still explicit.

## 5. `export_panels` mode

Use this mode for multi-panel handoff:

```text
"export": {
  "mode": "export_panels",
  "output_dir": "panels",
  "format": "svg",
  "overwrite": true
}
```

### Source facts

`export_panels(...)` writes panel assets and can write `panel-index.json`. Panel records carry `panel_id`, path, format, export timestamp, pubfig version, optional title, and optional label.

### Operational interpretation

Panel export is a structured asset workflow, not just a file dump. Use it before optional composite/Figma assembly.

## 6. Title handling in panel export

### Source facts

Panel export strips titles by default unless `include_title=True`.

### Operational interpretation

Panel-first composite workflows usually want clean panel artwork. Add global titles, labels, and final layout text downstream.

## 7. Underlying Python export primitives

The CLI modes call the same underlying primitives:

- `save_figure(...)`
- `batch_export(...)`
- `export_panels(...)`

Mention these functions when explaining source behavior or notebook/script usage. For agent output, lead with the JSON CLI.

## 8. Recommended source-faithful patterns

### Single paper figure

- create `figure.spec.json` with `export.mode = "save_figure"`
- run `pubfig validate-spec figure.spec.json`
- run `pubfig render figure.spec.json`

### Same figure in several formats

- create `figure.spec.json` with `export.mode = "batch_export"`
- set `formats` explicitly
- validate and render through the CLI

### Multi-panel downstream assembly

- create `panels.spec.json` with `panels` and `export.mode = "export_panels"`
- validate and render through the CLI
- use the panel directory and `panel-index.json` for composite/Figma-aware downstream handling
