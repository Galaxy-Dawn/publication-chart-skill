# Example 2 — Ablation figure

## User-style prompt

Turn these ablation results into a paper-ready figure that makes the contribution of each module easy to read.

## Expected skill interpretation

- artifact: figure
- maturity: publication-ready generation
- structure: single panel or compact paired panel
- goal: isolate incremental effect clearly

## Preferred route

- primary tool: `pubfig>=0.3.0` JSON CLI
- likely `plot.kind`: `dumbbell` or `paired` for low-cardinality paired ablations, otherwise `bar_scatter` / `grouped_scatter` plus a compact companion table
- do not default to a crowded decorative chart

## Minimum acceptable output shape

- recommend the ablation-focused visual form and why,
- provide a runnable `figure.spec.json`,
- run `pubfig validate-spec figure.spec.json`,
- run `pubfig render figure.spec.json`,
- export to a paper-ready format,
- include a QA note on baseline clarity and ordering.

## Minimal CLI spec pattern

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
      "show_delta_labels": true,
      "title": "Ablation effect by metric"
    }
  },
  "export": {
    "mode": "save_figure",
    "path": "ablation.pdf",
    "spec": "nature",
    "width": "single"
  }
}
```
