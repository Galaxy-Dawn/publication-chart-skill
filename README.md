# publication-chart-skill

A standalone installable skill that helps agents produce **publication-grade scientific figures and tables** using **pubfig** and **pubtab**.

This repository is intentionally shaped so the **repo root is the skill root**. You can copy the whole directory into a Codex or Claude Code skill folder directly.

## What this skill covers

- choose the right figure / table form for a research communication goal
- map the request to `pubfig` or `pubtab`
- generate minimal runnable code or CLI commands
- export paper-ready assets
- run publication QA
- propose targeted revisions when the result is weak

## Repository layout

- `SKILL.md` — the installable skill entrypoint
- `agents/openai.yaml` — optional UI metadata
- `references/` — workflow guidance and recipes
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

- This is a **workflow-first** skill. It does not ship helper scripts in v1.
- `pubfig` is the default engine for figures.
- `pubtab` is the default engine for publication tables.
- Figma/composite assembly is supported as an **optional secondary branch**, not the default path.
