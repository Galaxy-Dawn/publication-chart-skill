# publication-chart-skill

publication-chart-skill is a standalone cross-platform skill for turning research results into **publication-grade scientific figures and tables**.

It is designed for agents running in **Claude Code**, **Codex**, or **OpenCode**, with **`pubfig`** as the default figure engine and **`pubtab`** as the default table engine.

The goal is to help an agent choose the right artifact, produce a runnable route, export paper-ready outputs, and review the result against publication-quality expectations.

**Upstream toolchain references**

- **pubfig** — GitHub: <https://github.com/Galaxy-Dawn/pubfig> · PyPI: <https://pypi.org/project/pubfig/> · Examples: <https://github.com/Galaxy-Dawn/pubfig/tree/main/examples>
- **pubtab** — GitHub: <https://github.com/Galaxy-Dawn/pubtab> · PyPI: <https://pypi.org/project/pubtab/> · Examples: <https://github.com/Galaxy-Dawn/pubtab/tree/main/examples>

## How it works

<p align="center">
  <a href="https://github.com/Galaxy-Dawn/pubfig/blob/main/examples/bar_scatter.png"><img src="https://raw.githubusercontent.com/Galaxy-Dawn/pubfig/main/examples/bar_scatter.png" width="48%" alt="pubfig bar scatter example"></a>
  <a href="https://github.com/Galaxy-Dawn/pubtab/blob/main/examples/table7.xlsx"><img src="https://raw.githubusercontent.com/Galaxy-Dawn/pubtab/main/examples/table7.png" width="48%" alt="pubtab table example"></a>
</p>
<p align="center">
  <a href="https://github.com/Galaxy-Dawn/pubfig/blob/main/examples/calibration.png"><img src="https://raw.githubusercontent.com/Galaxy-Dawn/pubfig/main/examples/calibration.png" width="48%" alt="pubfig calibration example"></a>
  <a href="https://github.com/Galaxy-Dawn/pubtab/blob/main/examples/table10.xlsx"><img src="https://raw.githubusercontent.com/Galaxy-Dawn/pubtab/main/examples/table10.png" width="48%" alt="pubtab table10 example"></a>
</p>

When this skill is triggered, the agent should not jump straight into plotting. It should first determine what the user is trying to communicate: a comparison, an ablation, a calibration result, a diagnostic summary, a benchmark table, or a mixed figure-plus-table deliverable.

From there, the skill chooses whether the result should be expressed as:

- a **figure**,
- a **table**,
- or a **figure + companion table**.

Once the representation is clear, the skill routes the request to:

- **`pubfig`** for figures,
- **`pubtab`** for publication tables,
- or both when the section needs one visual summary and one exact-value artifact.

A strong default response should:

1. recommend the artifact type,
2. recommend the `pubfig` / `pubtab` route,
3. provide the minimum runnable command or code snippet,
4. specify the expected export files,
5. run a publication QA pass,
6. suggest targeted revisions if the request or current artifact is weak.

The repository also includes a small helper script, `scripts/ensure_publication_tooling.py`, so the agent can probe whether `pubfig` and `pubtab` are installed, force-install missing dependencies into the active environment when runnable execution is required, and then continue with the real workflow instead of stopping at generic guidance.

### Quick examples from pubfig and pubtab

A few representative routes from the underlying toolchain:

**pubfig example**

```python
import numpy as np
import pubfig as pf

rng = np.random.default_rng(0)
data = rng.normal(size=(3, 2, 18))
fig = pf.bar_scatter(data)
pf.save_figure(fig, "figure1.pdf")
```

Related upstream examples:
- <https://github.com/Galaxy-Dawn/pubfig/blob/main/examples/gallery.py>
- <https://github.com/Galaxy-Dawn/pubfig/blob/main/examples/new_plot_showcases.py>
- <https://github.com/Galaxy-Dawn/pubfig/blob/main/examples/figma_workflow_demo.md>

**pubtab example**

```bash
pubtab xlsx2tex table.xlsx -o table.tex
pubtab preview table.tex -o table.png --dpi 300
```

Related upstream examples:
- <https://github.com/Galaxy-Dawn/pubtab/blob/main/examples/table4.xlsx>
- <https://github.com/Galaxy-Dawn/pubtab/blob/main/examples/table7.xlsx>
- <https://github.com/Galaxy-Dawn/pubtab/blob/main/examples/table10.xlsx>

## Installation

This repository is structured as a **single-skill repo** that works with the `skills` CLI.

Install it with:

```bash
npx skills add Galaxy-Dawn/publication-chart-skill
```

To inspect what the repo exposes before installing, run:

```bash
npx skills add Galaxy-Dawn/publication-chart-skill --list
```

If you want the skill installed globally for a specific agent, use the corresponding `skills` CLI flags. See the `skills` CLI documentation for agent-specific options and target paths.

## What's inside

The canonical payload lives directly in the repository root:

- `SKILL.md` — the main skill entrypoint
- `references/` — workflow guidance, recipes, QA guidance, and source-driven docs from `pubfig` / `pubtab`
- `examples/` — example prompts and expected output shapes
- `scripts/ensure_publication_tooling.py` — environment probe + forced-install helper

The `references/` directory is where the skill explains how to map research communication tasks to concrete `pubfig` and `pubtab` routes. The `examples/` directory shows the expected interpretation style for benchmark figures, ablations, calibration plots, diagnostic figures, publication tables, and mixed figure-plus-table requests.

## Example requests

Typical requests that should trigger this skill include:

- “Make a publication-quality benchmark figure for these results.”
- “Should this ablation be a figure or a table?”
- “Turn this Excel benchmark sheet into a publication-ready LaTeX table.”
- “Review this weak scientific chart and give me a stronger figure/table route.”
- “I need one figure and one companion table for the Results section.”
- “Export a multi-panel paper figure and tell me whether Figma assembly is actually necessary.”
- “Use `pubfig` to turn these evaluation results into a paper-ready figure.”
- “Use `pubtab` to convert this workbook into a manuscript-ready table.”
