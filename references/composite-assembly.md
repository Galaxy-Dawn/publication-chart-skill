# Composite Assembly

## Principle

Composite assembly is a **secondary branch**, not the default workflow.

Use it when:

- the user explicitly wants a multi-panel paper figure,
- panel-level maintenance matters,
- or the final paper figure needs finishing beyond a single exported plot.

## Default stance

- Single-panel figure → stay in the normal `pubfig>=0.3.0` JSON CLI route.
- Multi-panel figure with real assembly needs → use `export_panels` in a `pubfig` JSON spec.
- Figma is optional and should not be introduced unless it solves a real assembly problem.

## pubfig CLI route

Use a panel spec when the user needs maintainable panel assets:

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

Then run:

```bash
pubfig validate-spec panels.spec.json
pubfig render panels.spec.json
```

The expected outputs are panel files plus `panel-index.json` when `index_file` is enabled.

## Optional Figma handoff

Figma handoff is downstream of panel export. If the environment already uses a pubfig/Figma bridge workflow, keep `figure_id` stable across revisions and use `pubfig figma ...` only after the panel directory is valid.

## Practical rule

Escalate to composite assembly only after the panel content itself is strong.

Do not use Figma/composite assembly to hide weak chart choice, poor labels, or overloaded panels.
