# publication-chart-skill

A standalone installable skill that helps agents produce **publication-grade scientific figures and tables** using **pubfig** and **pubtab**.

This repository is intentionally shaped so the **repo root is the skill root**. You can copy the whole directory into a Codex or Claude Code skill folder directly.

## What this skill covers

- choose the right figure / table form for a research communication goal
- decide whether a result should be a figure, a table, or a figure + companion table
- map the request to `pubfig` or `pubtab`
- generate minimal runnable code or CLI commands
- export paper-ready assets
- run publication QA
- propose targeted revisions when the current artifact is weak

## What's new in v2

- stronger trigger surface for **figure + companion table** workflows
- clearer first-response contract: artifact decision, tool route, implementation, export, QA, revision
- explicit environment-probing and graceful-degradation guidance
- tighter alignment with current `pubfig` / `pubtab` capabilities
- new review example for upgrading an existing weak figure/table draft
- new source-driven docs mapped directly from `pubfig/src/pubfig` and `pubtab/src/pubtab`

## Repository layout

- `SKILL.md` — the installable skill entrypoint
- `agents/openai.yaml` — optional UI metadata
- `references/` — workflow guidance, recipes, and source-driven architecture docs
- `examples/` — prompt-to-output-shape examples

## Install

### Codex

Copy this repository into your skill directory, for example:

```bash
cp -R publication-chart-skill ~/.codex/skills/publication-chart-skill
```

### Claude Code

Copy this repository as one complete skill folder into the directory where your Claude Code skills live. Keep the repository root unchanged so `SKILL.md`, `references/`, and `examples/` stay at the skill root.

## Notes

- This is a **workflow-first** skill; it still does not ship helper scripts.
- `pubfig` is the default engine for figures.
- `pubtab` is the default engine for publication tables.
- Figma/composite assembly is supported as an **optional secondary branch**, not the default path.
