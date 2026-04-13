# publication-chart-skill

publication-chart-skill is a standalone cross-platform skill for turning research results into **publication-grade scientific figures and tables**.

It is designed for agents running in **Claude Code**, **Codex**, or **OpenCode**, with **`pubfig`** as the default figure engine and **`pubtab`** as the default table engine.

The goal is to help an agent choose the right artifact, produce a runnable route, export paper-ready outputs, and review the result against publication-quality expectations.

## How it works

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

This keeps the repository focused on one canonical skill payload.

## Example requests

Typical requests that should trigger this skill include:

- “Make a publication-quality benchmark figure for these results.”
- “Should this ablation be a figure or a table?”
- “Turn this Excel benchmark sheet into a publication-ready LaTeX table.”
- “Review this weak scientific chart and give me a stronger figure/table route.”
- “I need one figure and one companion table for the Results section.”
- “Export a multi-panel paper figure and tell me whether Figma assembly is actually necessary.”
