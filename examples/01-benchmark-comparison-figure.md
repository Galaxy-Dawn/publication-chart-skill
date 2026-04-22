# Example 1 — Benchmark comparison figure

## Real user prompt

Help me make a publication-quality benchmark comparison figure for three datasets. I want the overall improvement pattern to be easy to read, and I need paper-ready export files.

## Why this route

- artifact: **figure**
- maturity: **publication-ready generation**
- structure: **single panel**
- recommended CLI kind: **`bar_scatter`**

Why not a raw grouped bar first?

- there are repeated runs per dataset, so showing the scatter points helps communicate spread,
- the chart still stays readable because there are only two series,
- exact values can stay in a companion table if the paper also needs lookup-friendly numbers.

## Runnable route (CLI-first, validated locally)

Run from the repository root:

```bash
mkdir -p temp/example-01-benchmark

cat > temp/example-01-benchmark/benchmark.spec.json <<'JSON'
{
  "schema_version": 1,
  "plot": {
    "kind": "bar_scatter",
    "kwargs": {
      "data": [
        [[0.73, 0.77, 0.78, 0.80, 0.82, 0.79], [0.90, 0.94, 0.97, 0.99, 1.01, 0.96]],
        [[0.83, 0.87, 0.89, 0.91, 0.90, 0.88], [1.02, 1.05, 1.08, 1.10, 1.12, 1.07]],
        [[0.78, 0.82, 0.84, 0.87, 0.86, 0.83], [0.94, 0.98, 1.00, 1.03, 1.05, 0.99]]
      ],
      "category_names": ["Dataset A", "Dataset B", "Dataset C"],
      "series_names": ["Baseline", "Method"],
      "title": "Benchmark comparison",
      "show_statistics": false,
      "random_seed": 0
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
JSON

cd temp/example-01-benchmark
MPLBACKEND=Agg pubfig validate-spec benchmark.spec.json
MPLBACKEND=Agg pubfig render benchmark.spec.json
ls -1 benchmark.pdf benchmark.png
```

## Expected artifacts

- `temp/example-01-benchmark/benchmark.spec.json`
- `temp/example-01-benchmark/benchmark.pdf`
- `temp/example-01-benchmark/benchmark.png`

## What to inspect

- the category ordering should match the story you want to tell,
- the legend should stay compact because there are only two series,
- the title can be removed later if this becomes one panel inside a larger composite figure,
- if exact benchmark values matter in the same section, add a companion table instead of over-annotating the figure.

## Publication QA

- **claim fit** — good for quick pattern perception across datasets
- **readability** — labels and legend remain readable after downscaling
- **uncertainty/spread** — scatter points justify this route over a plain bar chart
- **handoff rule** — if the paper needs exact metrics, pair this with a table rather than stuffing more text into the panel
