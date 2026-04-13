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
- `claude-plugin/publication-chart-skill/` — Claude Code plugin wrapper
- `plugins/publication-chart-skill/` — Codex plugin wrapper
- `.agents/plugins/marketplace.json` — repo-local Codex marketplace entry for the plugin wrapper
- `scripts/ensure_publication_tooling.py` — bundled probe + force-install helper for `pubfig` / `pubtab`
- `scripts/sync_plugin_wrappers.py` — maintainer script that refreshes both plugin wrappers from the canonical root skill

## Install

### Direct skill install

If you want the lightest-weight path, copy the repository root directly into your skill directory and keep the root unchanged.

```bash
cp -R publication-chart-skill /path/to/your/skills/publication-chart-skill
```

### Claude Code plugin wrapper

This repository also ships a Claude Code plugin wrapper at:

- `claude-plugin/publication-chart-skill/`

For local testing, point Claude Code at that plugin root:

```bash
claude --plugin-dir /absolute/path/to/publication-chart-skill/claude-plugin/publication-chart-skill
```

### Codex plugin wrapper

This repository also ships a Codex plugin wrapper at:

- `plugins/publication-chart-skill/`

The repo includes a marketplace entry at:

- `.agents/plugins/marketplace.json`

so the wrapper can be surfaced through Codex's plugin flow from this repository layout.

## Maintainer note

The canonical source of truth remains the repository root skill:

- `SKILL.md`
- `references/`
- `examples/`

If you update the root skill and want the plugin wrappers to stay in sync, run:

```bash
python3 scripts/sync_plugin_wrappers.py
```

## Notes

- This is a **workflow-first** skill with one small bundled helper script for deterministic environment probing and forced installation.
- `pubfig` is the default engine for figures.
- `pubtab` is the default engine for publication tables.
- The skill probes for `pubfig` / `pubtab` availability and force-installs missing dependencies into the active environment before continuing when runnable execution is required.
- Figma/composite assembly is supported as an **optional secondary branch**, not the default path.
