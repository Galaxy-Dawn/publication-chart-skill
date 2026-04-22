# pubfig architecture (source-driven)

This guide reads `pubfig>=0.3.0` from the source tree rather than from high-level overview material.

Primary source files:

- `pubfig/src/pubfig/__init__.py`
- `pubfig/src/pubfig/plot_registry.py`
- `pubfig/src/pubfig/render_spec.py`
- `pubfig/src/pubfig/cli.py`
- `pubfig/src/pubfig/plots/`
- `pubfig/src/pubfig/export/`
- `pubfig/src/pubfig/specs.py`
- `pubfig/src/pubfig/themes/`
- `pubfig/src/pubfig/colors/`

## 1. Core architecture

### Source facts

- `pubfig.__init__` re-exports the public Python plot functions and export helpers.
- `plot_registry.py` maps stable CLI `plot.kind` strings to those public plot functions.
- `render_spec.py` implements the agent-first JSON render pipeline.
- `cli.py` exposes `render`, `validate-spec`, `list-kinds`, and `figma` subcommands.
- `export/io.py` and `export/panels.py` remain the underlying export implementation.

### Operational interpretation

For agents, the primary route is now:

1. write a JSON render spec,
2. run `pubfig validate-spec figure.spec.json`,
3. run `pubfig render figure.spec.json`,
4. inspect the emitted `output_paths` and generated files.

The Python API is still the native implementation layer and remains useful in notebooks or custom scripts. It is no longer the default interface this skill should recommend for agent-generated figures.

## 2. Agent-first CLI surface

### Source facts

`pubfig 0.3.0` exposes these stable commands:

```bash
pubfig list-kinds
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

`list-kinds` reports the stable `plot.kind` names. `validate-spec` builds and checks the figure route without writing output files. `render` executes the same spec and writes the requested artifacts.

### Operational interpretation

A figure answer should normally include:

- the `plot.kind`,
- a complete JSON spec,
- the validation command,
- the render command,
- expected output files.

## 3. JSON render spec contract

### Source facts

`render_spec.py` accepts exactly one of:

- `plot` for one figure,
- `panels` for a panel export package.

Top-level keys are:

- `schema_version`
- `plot` or `panels`
- `export`

For single figures, `export.mode` must be one of:

- `save_figure`
- `batch_export`

For panel packages, `export.mode` must be:

- `export_panels`

Data references support JSON, CSV, NPY, and NPZ through `{"$load": "..."}`.

### Operational interpretation

Keep specs explicit. Do not hide important output behavior inside prose. If the user needs PDF and PNG, use `batch_export` in the JSON spec rather than two ad-hoc Python calls.

## 4. Plot family surface

### Source facts

The public plot families are still implemented in `plots/` and re-exported through `pubfig.__init__`. The CLI reaches them through `plot_registry.py`.

Representative `plot.kind` values include:

- comparison: `bar`, `bar_scatter`, `grouped_scatter`, `dumbbell`, `paired`
- distribution: `box`, `violin`, `raincloud`, `histogram`, `density`, `ecdf`, `qq`
- trend: `line`, `area`
- relationship: `scatter`, `bubble`, `contour2d`, `hexbin`
- matrix/map: `heatmap`, `corr_matrix`, `clustermap`
- evaluation/diagnostic: `calibration`, `roc`, `pr_curve`, `bland_altman`, `forest_plot`, `volcano`
- composition/hierarchy: `upset`, `stacked_bar`, `stacked_ratio_barh`, `donut`, `radial_hierarchy`, `circular_grouped_bar`, `circular_stacked_bar`

### Operational interpretation

Use `pubfig list-kinds` as the installed-version truth. Choose the plot family by scientific claim, not by novelty.

## 5. Export architecture

### Source facts

The CLI export modes call the same underlying export primitives:

- `save_figure(...)` for one explicit target,
- `batch_export(...)` for multi-format publication export,
- `export_panels(...)` for structured panel directories.

The export layer handles publication sizing, format suffixes, DPI, trim behavior, vector text behavior, and panel metadata.

### Operational interpretation

For agents, describe the export block first. Mention Python functions only as the underlying implementation or as an optional notebook/script path.

## 6. Source-guided caution points

- Require `pubfig>=0.3.0`; older `pubfig` versions do not provide the agent-first render CLI.
- Do not route ordinary figure generation through the Figma bridge.
- Use Figma only after valid panel exports exist and composite assembly is genuinely needed.
- Do not use Python API examples as the default answer for agent figure generation.
- Do not mix up plot-time design size with export-time publication size.
- Use `batch_export` when multiple formats are required.
