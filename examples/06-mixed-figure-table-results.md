# Example 6 — Mixed figure + table deliverable

## Real user prompt

For this results section, I want one summary figure and one companion table: the figure should show the overall trend, and the table should preserve the exact metrics.

## Why this route

- artifact: **mixed deliverable**
- maturity: **publication-ready generation**
- structure: **one figure + one table**

Role split:

- the **figure** carries fast visual comparison,
- the **table** preserves exact benchmark values for lookup and citation.

## Runnable route (CLI-first for figure, validated locally)

Run from the repository root:

```bash
mkdir -p temp/example-06-mixed

cat > temp/example-06-mixed/results_summary.spec.json <<'JSON'
{
  "schema_version": 1,
  "plot": {
    "kind": "grouped_scatter",
    "kwargs": {
      "data": [
        [[0.76, 0.77, 0.78, 0.79, 0.80], [0.88, 0.90, 0.91, 0.92, 0.94], [0.93, 0.95, 0.96, 0.97, 0.98]],
        [[0.80, 0.82, 0.83, 0.84, 0.85], [0.92, 0.94, 0.95, 0.96, 0.97], [0.99, 1.01, 1.02, 1.03, 1.04]],
        [[0.77, 0.79, 0.80, 0.81, 0.82], [0.90, 0.92, 0.93, 0.94, 0.95], [0.96, 0.98, 0.99, 1.00, 1.01]]
      ],
      "category_names": ["Dataset A", "Dataset B", "Dataset C"],
      "group_names": ["Baseline", "Method A", "Method B"],
      "title": "Overall benchmark pattern",
      "random_seed": 0
    }
  },
  "export": {
    "mode": "batch_export",
    "base_path": "results_summary",
    "formats": ["pdf", "png"],
    "spec": "nature",
    "width": "single",
    "dpi": 300
  }
}
JSON

cd temp/example-06-mixed
MPLBACKEND=Agg pubfig validate-spec results_summary.spec.json
MPLBACKEND=Agg pubfig render results_summary.spec.json
cd ../..

python3 - <<'PY'
from pathlib import Path
from openpyxl import Workbook

out = Path("temp/example-06-mixed")
wb = Workbook()
ws = wb.active
ws.title = "Results"
rows = [
    ["Method", "Dataset A", "Dataset B", "Dataset C", "Average"],
    ["Baseline", 0.770, 0.820, 0.790, 0.793],
    ["Method A", 0.901, 0.941, 0.919, 0.920],
    ["Method B", 0.951, 1.011, 0.981, 0.981],
]
for row in rows:
    ws.append(row)
wb.save(out / "results_table.xlsx")
PY

pubtab xlsx2tex \
  temp/example-06-mixed/results_table.xlsx \
  -o temp/example-06-mixed/results_table_preview.tex \
  --sheet Results

pubtab preview \
  temp/example-06-mixed/results_table_preview.tex \
  -o temp/example-06-mixed/results_table.png \
  --dpi 200

pubtab xlsx2tex \
  temp/example-06-mixed/results_table.xlsx \
  -o temp/example-06-mixed/results_table_final.tex \
  --sheet Results \
  --caption "Exact benchmark metrics for the results section." \
  --label "tab:results-main"
```

## Expected artifacts

Figure:

- `temp/example-06-mixed/results_summary.spec.json`
- `temp/example-06-mixed/results_summary.pdf`
- `temp/example-06-mixed/results_summary.png`

Table:

- `temp/example-06-mixed/results_table.xlsx`
- `temp/example-06-mixed/results_table_preview.tex`
- `temp/example-06-mixed/results_table.png`
- `temp/example-06-mixed/results_table_final.tex`

## What to inspect

- the figure should answer “what is the overall pattern?” quickly,
- the table should answer “what are the exact numbers?” without duplicating the entire figure logic,
- the preview step should validate the table body before final caption/label are added,
- the section should not overload the figure with exact annotations that belong in the table.

## Publication QA

- **role separation** — figure for pattern, table for exact values
- **redundancy control** — avoid repeating every number inside the figure
- **section fit** — good for Results sections that need one quick visual and one precise lookup artifact
- **handoff** — if the figure later becomes one panel inside a composite figure, keep the table unchanged
