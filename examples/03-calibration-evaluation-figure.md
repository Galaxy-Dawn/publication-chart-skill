# Example 3 — Calibration / evaluation figure

## User-style prompt

I need a publication-quality evaluation figure showing whether my predicted probabilities are calibrated.

## Expected skill interpretation

- artifact: figure
- maturity: publication-ready generation
- structure: single panel
- goal: diagnostic evaluation, not generic trend plotting

## Preferred route

- primary tool: `pubfig>=0.3.0` JSON CLI
- likely `plot.kind`: `calibration`
- related alternatives: `roc` / `pr_curve` only if the scientific question changes

## Minimum acceptable output shape

- explain why calibration is the right diagnostic form,
- provide a runnable `figure.spec.json`,
- run `pubfig validate-spec figure.spec.json`,
- run `pubfig render figure.spec.json`,
- export to PDF or SVG,
- include QA on labels, reference lines, and downscaled readability.

## Minimal CLI spec pattern

```json
{
  "schema_version": 1,
  "plot": {
    "kind": "calibration",
    "kwargs": {
      "y_true": [[0, 1, 1, 0, 1, 0, 1, 1]],
      "y_prob": [[0.10, 0.72, 0.83, 0.31, 0.91, 0.22, 0.67, 0.88]],
      "series_names": ["Model"],
      "title": "Probability calibration"
    }
  },
  "export": {
    "mode": "save_figure",
    "path": "calibration.pdf",
    "spec": "nature",
    "width": "single"
  }
}
```
