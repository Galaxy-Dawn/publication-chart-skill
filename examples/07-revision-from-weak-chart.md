# Example 7 — Revision from a weak chart request

## Real user prompt

I was thinking of using a radar chart for these benchmark results. Can you improve this into something publication-quality?

## Why the original route is weak

A radar chart is risky here because:

- precise cross-method comparison is hard,
- shape and filled area can exaggerate differences,
- the reader needs exact method-to-method comparison more than profile aesthetics.

For a benchmark-style claim, a grouped comparison figure is usually stronger. If exact values are equally important, add a companion table.

## Recommended revision route

- replacement artifact: **figure**
- recommended CLI kind: **`grouped_scatter`**
- optional companion artifact: **`pubtab` table** if the paper needs exact numeric lookup in the same section

## Runnable route (CLI-first, validated locally)

Run from the repository root:

```bash
mkdir -p temp/example-07-revision

cat > temp/example-07-revision/radar_replacement.spec.json <<'JSON'
{
  "schema_version": 1,
  "plot": {
    "kind": "grouped_scatter",
    "kwargs": {
      "data": [
        [[0.70, 0.72, 0.73, 0.74, 0.75], [0.77, 0.79, 0.80, 0.81, 0.82], [0.82, 0.83, 0.84, 0.85, 0.86], [0.85, 0.86, 0.87, 0.88, 0.89]],
        [[0.66, 0.68, 0.69, 0.70, 0.71], [0.73, 0.75, 0.76, 0.77, 0.78], [0.78, 0.80, 0.81, 0.82, 0.83], [0.82, 0.84, 0.85, 0.86, 0.87]],
        [[0.72, 0.74, 0.75, 0.76, 0.77], [0.80, 0.82, 0.83, 0.84, 0.85], [0.86, 0.88, 0.89, 0.90, 0.91], [0.89, 0.91, 0.92, 0.93, 0.94]]
      ],
      "category_names": ["Dataset A", "Dataset B", "Dataset C"],
      "group_names": ["Model 1", "Model 2", "Model 3", "Model 4"],
      "title": "Radar replacement: benchmark comparison",
      "random_seed": 0
    }
  },
  "export": {
    "mode": "batch_export",
    "base_path": "radar_replacement",
    "formats": ["pdf", "png"],
    "spec": "nature",
    "width": "single",
    "dpi": 300
  }
}
JSON

cd temp/example-07-revision
MPLBACKEND=Agg pubfig validate-spec radar_replacement.spec.json
MPLBACKEND=Agg pubfig render radar_replacement.spec.json
ls -1 radar_replacement.pdf radar_replacement.png
```

## Expected artifacts

- `temp/example-07-revision/radar_replacement.spec.json`
- `temp/example-07-revision/radar_replacement.pdf`
- `temp/example-07-revision/radar_replacement.png`

## What to inspect

- the replacement should make cross-model ranking easier than a radar chart,
- category labels should stay readable even with four methods,
- if the panel starts to feel dense, reduce method count per panel or add a companion table rather than reverting to radar.

## Publication QA

- **revision quality** — this is a real chart replacement, not just a style tweak
- **comparability** — grouped comparison is clearer for benchmark claims than radial shape comparison
- **fallback rule** — if exact numbers become central, pair the replacement figure with a table instead of over-annotating the chart
