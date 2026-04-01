# pubtab Recipes

`pubtab` is the default engine for publication-ready tables.

## Core routes

### Excel to LaTeX

```bash
pubtab xlsx2tex results.xlsx -o results.tex
```

### LaTeX to Excel

```bash
pubtab tex2xlsx tables.tex -o tables.xlsx
```

### Preview

```bash
pubtab preview results.tex -o results.png --dpi 300
```

## Python route

```python
import pubtab

pubtab.xlsx2tex("results.xlsx", output="results.tex", theme="three_line")
pubtab.preview("results.tex", output="results.png", dpi=300)
```

## When to use `tabularray`

Use `--latex-backend tabularray` when:

- the user explicitly wants `tblr`,
- the workflow already uses `tabularray`,
- or the table backend needs to match an existing manuscript setup.

Example:

```bash
pubtab xlsx2tex results.xlsx -o results_tblr.tex --theme three_line --latex-backend tabularray
```

## Common publication controls

Use these when they are justified:

- `--caption`
- `--label`
- `--span-columns`
- `--with-resizebox`
- `--resizebox-width`
- `--sheet`
- `--preview`
- `--latex-backend`

## Default guidance

- start with the smallest `xlsx2tex` route,
- preview before treating the table as final,
- use a publication table when exact values matter more than quick pattern perception,
- keep figure and table roles distinct in mixed deliverables.

## Minimal recipe patterns

### Benchmark table from Excel

```bash
pubtab xlsx2tex benchmark.xlsx -o benchmark.tex --caption "Main benchmark results." --label "tab:benchmark"
```

### Two-column table

```bash
pubtab xlsx2tex benchmark.xlsx -o benchmark.tex --span-columns
```

### Preview before submission

```bash
pubtab preview benchmark.tex -o benchmark.png --dpi 300
```
