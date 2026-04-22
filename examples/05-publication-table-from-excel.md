# Example 5 — Publication-ready LaTeX table from Excel

## Real user prompt

Convert this benchmark workbook into a publication-ready LaTeX table and give me a preview before I paste it into the paper.

## Why this route

- artifact: **table**
- maturity: **publication-ready generation**
- structure: **single table**
- recommended engine: **`pubtab`**

The main need here is exact value lookup, not visual pattern perception. That makes a publication table the primary artifact.

## Runnable route (validated locally)

Run from the repository root:

```bash
mkdir -p temp/example-05-table

python3 - <<'PY'
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Benchmark"

rows = [
    ["Method", "Dataset A", "Dataset B", "Dataset C", "Average"],
    ["Baseline", 0.782, 0.881, 0.842, 0.835],
    ["Method",   0.961, 1.074, 0.998, 1.011],
]

for row in rows:
    ws.append(row)

wb.save("temp/example-05-table/benchmark.xlsx")
PY

pubtab xlsx2tex \
  temp/example-05-table/benchmark.xlsx \
  -o temp/example-05-table/benchmark_preview.tex \
  --sheet Benchmark

pubtab preview \
  temp/example-05-table/benchmark_preview.tex \
  -o temp/example-05-table/benchmark.png \
  --dpi 200

pubtab xlsx2tex \
  temp/example-05-table/benchmark.xlsx \
  -o temp/example-05-table/benchmark_final.tex \
  --sheet Benchmark \
  --caption "Main benchmark results." \
  --label "tab:benchmark"
```

## Expected artifacts

- `temp/example-05-table/benchmark.xlsx`
- `temp/example-05-table/benchmark_preview.tex`
- `temp/example-05-table/benchmark.png`
- `temp/example-05-table/benchmark_final.tex`

## What to inspect

- the preview should render a real table, not just path text,
- the preview-first body should be checked before final manuscript-facing metadata is added,
- the final `benchmark_final.tex` should carry manuscript-ready caption/label,
- if the final paper is two-column and the table becomes too wide, consider `--span-columns` or a resizebox route,
- if your real workbook has many sheets, remember that `pubtab` exports all sheets by default unless `--sheet` is specified.

## Publication QA

- **artifact fit** — correct choice because exact values matter
- **preview-first check** — PNG preview should be reviewed before treating the table as final
- **manuscript readiness** — caption/label are added in the final export step, not forced into preview-first verification
- **width risk** — if columns become dense, adjust width/span explicitly instead of shrinking blindly
