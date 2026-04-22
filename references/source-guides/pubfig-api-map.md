# pubfig API map (source-driven)

This guide maps the public `pubfig>=0.3.0` surface to the agent-first CLI surface.

Primary source files:

- `pubfig/src/pubfig/__init__.py`
- `pubfig/src/pubfig/plot_registry.py`
- `pubfig/src/pubfig/render_spec.py`

## 1. Public implementation layer

### Source facts

`pubfig.__init__` re-exports public Python functions such as:

- `bar_scatter`
- `grouped_scatter`
- `dumbbell`
- `forest_plot`
- `calibration`
- `heatmap`
- `line`
- `scatter`

It also re-exports export helpers:

- `save_figure`
- `batch_export`
- `export_panel`
- `export_panels`

### Operational interpretation

These functions remain the native implementation surface. Agents should usually reach them through the JSON CLI unless the user explicitly asks for Python code.

## 2. CLI plot-kind layer

### Source facts

`plot_registry.py` provides stable `plot.kind` names for the JSON CLI. The installed version can be queried with:

```bash
pubfig list-kinds
```

A JSON spec calls a public plot function through:

```json
{
  "plot": {
    "kind": "bar_scatter",
    "kwargs": {
      "data": [
        [[0.73, 0.77, 0.80], [0.90, 0.94, 0.97]],
        [[0.83, 0.87, 0.90], [1.02, 1.05, 1.08]]
      ],
      "category_names": ["Dataset A", "Dataset B"],
      "series_names": ["Baseline", "Method"]
    }
  }
}
```

### Operational interpretation

When writing a skill response, name the CLI `plot.kind` first. Mention the corresponding Python function only if useful for source-level explanation.

## 3. Recommended mapping by task

| Task | Preferred CLI `plot.kind` | Notes |
|---|---|---|
| repeated benchmark runs | `bar_scatter`, `grouped_scatter` | shows spread instead of hiding all runs behind bars |
| compact ablation | `dumbbell`, `paired`, `bar_scatter` | make baseline and module effect explicit |
| calibration | `calibration` | diagnostic probability calibration, not a generic trend plot |
| confidence intervals | `forest_plot` | effect estimate plus uncertainty |
| correlation or confusion-style matrix | `heatmap`, `corr_matrix` | use labels and colorbar carefully |
| distributions | `box`, `violin`, `raincloud`, `ecdf`, `qq` | choose by the claim about spread/shape |
| ranking/trend | `line`, `area`, `grouped_scatter` | keep exact values in a companion table when needed |

## 4. CLI validation contract

### Source facts

`render_spec.py` validates:

- schema version,
- top-level keys,
- required plot/panel fields,
- unknown fields,
- output paths,
- callable argument binding,
- data references.

### Operational interpretation

Always recommend `pubfig validate-spec ...` before `pubfig render ...`. This gives agents a reviewable failure point before writing final files.

## 5. Python fallback boundary

Use Python API examples only when:

- the user is already in a notebook or Python script,
- the task needs custom preprocessing inside the plotting call,
- the target plot behavior is not representable in the JSON spec,
- or the user explicitly asks for Python code.

Do not present Python plotting code as the default agent route for `pubfig>=0.3.0`.
