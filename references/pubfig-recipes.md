# pubfig Recipes

`pubfig>=0.3.0` is the default engine for scientific figures. For agents, prefer the **JSON CLI** over ad-hoc Python plotting code.

Primary commands:

```bash
pubfig list-kinds
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

Use the Python API only when the user is explicitly working inside a notebook/script or needs custom logic not representable in a CLI JSON spec.

## Core CLI route

A minimal single-figure spec:

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "line",
    "kwargs": {
      "data": [[0.78, 1.03, 1.15], [0.87, 1.01, 1.04]],
      "series_names": ["Baseline", "Method"]
    }
  },
  "export": {
    "mode": "save_figure",
    "path": "figure1.pdf",
    "spec": "nature",
    "width": "single"
  }
}
```

Validate before rendering:

```bash
pubfig validate-spec figure.spec.json
pubfig render figure.spec.json
```

For headless CLI/agent/CI environments, prepend `MPLBACKEND=Agg` if the local Matplotlib backend tries to open a GUI window:

```bash
MPLBACKEND=Agg pubfig render figure.spec.json
```

## Common figure families

| Need | Preferred `plot.kind` values |
|---|---|
| benchmark comparison | `bar_scatter`, `grouped_scatter`, `bar`, `line` |
| ablation | `bar_scatter`, `dumbbell`, `paired`, `bar` |
| distribution | `box`, `violin`, `raincloud`, `histogram`, `density`, `ecdf`, `qq` |
| relationship | `scatter`, `bubble`, `contour2d`, `hexbin` |
| trend | `line`, `area` |
| diagnostic / evaluation | `calibration`, `forest_plot`, `bland_altman`, `volcano`, `roc`, `pr_curve` |
| composition / hierarchy | `donut`, `upset`, `radial_hierarchy`, `circular_grouped_bar`, `circular_stacked_bar`, `stacked_ratio_barh` |
| matrix / map | `heatmap`, `corr_matrix`, `clustermap` |

Use `pubfig list-kinds` to confirm the supported kind names in the installed version.

## Export modes

### Single explicit artifact

```text
"export": {
  "mode": "save_figure",
  "path": "figure1.pdf",
  "spec": "nature",
  "width": "single"
}
```

Use this when the agent needs one manuscript-facing file.

### Multiple publication outputs

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

Use this when the same figure needs PDF for manuscript submission, SVG for editing, and PNG for review threads or slides.

### Panel export

Use `export_panels` only when multi-panel assembly is genuinely needed:

```json
{
  "schema_version": 1,
  "panels": [
    {
      "panel_id": "a",
      "kind": "bar_scatter",
      "kwargs": {
        "data": {"$load": "data/panel_a.npy"},
        "category_names": ["Dataset A", "Dataset B"],
        "series_names": ["Baseline", "Method"]
      }
    },
    {
      "panel_id": "b",
      "kind": "line",
      "kwargs": {
        "data": {"$load": "data/panel_b.npy"}
      }
    }
  ],
  "export": {
    "mode": "export_panels",
    "output_dir": "panels",
    "format": "svg",
    "overwrite": true
  }
}
```

Then:

```bash
pubfig validate-spec panels.spec.json
pubfig render panels.spec.json
```

## Data inputs in JSON specs

Small arrays can be inline JSON lists. Larger arrays should be referenced from files:

```text
"data": {"$load": "data/benchmark.npy"}
```

Supported reference patterns include JSON/CSV/NPY/NPZ files in `pubfig 0.3.0`.

## Minimal recipe patterns

### Benchmark comparison

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "grouped_scatter",
    "kwargs": {
      "data": {"$load": "data/benchmark.npy"},
      "category_names": ["Dataset A", "Dataset B", "Dataset C"],
      "group_names": ["Baseline", "Method A", "Method B"],
      "title": "Benchmark comparison"
    }
  },
  "export": {
    "mode": "batch_export",
    "base_path": "benchmark",
    "formats": ["pdf", "png"],
    "spec": "nature",
    "width": "single",
    "dpi": 300
  }
}
```

### Ablation

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "dumbbell",
    "kwargs": {
      "start": [0.72, 0.81, 0.77],
      "end": [0.79, 0.86, 0.83],
      "category_names": ["Metric A", "Metric B", "Metric C"],
      "left_label": "Without module",
      "right_label": "With module",
      "show_delta_labels": true
    }
  },
  "export": {"mode": "save_figure", "path": "ablation.pdf"}
}
```

### Calibration

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "calibration",
    "kwargs": {
      "y_true": [0, 1, 1, 0, 1],
      "y_prob": [0.10, 0.72, 0.83, 0.31, 0.91]
    }
  },
  "export": {"mode": "save_figure", "path": "calibration.pdf"}
}
```

### Forest plot

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "forest_plot",
    "kwargs": {
      "effect": [1.12, 0.84, 1.36],
      "ci_low": [0.98, 0.71, 1.10],
      "ci_high": [1.29, 0.99, 1.68],
      "labels": ["Age", "BMI", "Smoking"],
      "reference": 1.0
    }
  },
  "export": {"mode": "save_figure", "path": "forest.pdf"}
}
```

### Heatmap

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "heatmap",
    "kwargs": {
      "data": [[1.0, 0.3], [0.3, 1.0]],
      "title": "Correlation matrix"
    }
  },
  "export": {"mode": "save_figure", "path": "heatmap.pdf"}
}
```

## Agent response rule

When producing a `pubfig` route, include:

1. a concrete JSON spec,
2. `pubfig validate-spec ...`,
3. `pubfig render ...`,
4. expected output paths from the export block,
5. a short QA note.
