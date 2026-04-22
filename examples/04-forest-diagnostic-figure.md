# Example 4 — Forest / diagnostic figure

## User-style prompt

Help me convert these effect estimates and confidence intervals into a paper-quality figure.

## Expected skill interpretation

- artifact: figure
- maturity: publication-ready generation
- structure: single panel
- goal: communicate effect size with uncertainty

## Preferred route

- primary tool: `pubfig>=0.3.0` JSON CLI
- likely `plot.kind`: `forest_plot`
- table may accompany it in the appendix if exact values are numerous

## Minimum acceptable output shape

- identify forest plot as the default route,
- provide the required arrays/arguments shape,
- run `pubfig validate-spec figure.spec.json`,
- run `pubfig render figure.spec.json`,
- export a paper-ready artifact,
- include QA on reference line, label clarity, and ordering.

## Minimal CLI spec pattern

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "forest_plot",
    "kwargs": {
      "effect": [1.12, 0.84, 1.36],
      "ci_low": [0.98, 0.71, 1.10],
      "ci_high": [1.29, 0.99, 1.68],
      "labels": ["Cohort A", "Cohort B", "Cohort C"],
      "reference": 1.0,
      "title": "Effect estimates with 95% CI"
    }
  },
  "export": {
    "mode": "save_figure",
    "path": "forest.pdf",
    "spec": "nature",
    "width": "single"
  }
}
```
