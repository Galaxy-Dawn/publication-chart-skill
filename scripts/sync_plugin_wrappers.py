#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILL_DIRNAME = "publication-chart-skill"
CANONICAL_REPO_URL = "https://github.com/Galaxy-Dawn/publication-chart-skill"
AUTHOR = {
    "name": "Gaoruizhang",
    "url": "https://github.com/Galaxy-Dawn",
}
KEYWORDS = [
    "research",
    "scientific-figures",
    "scientific-tables",
    "pubfig",
    "pubtab",
]
SKILL_CONTENT_PATHS = ["SKILL.md", "references", "examples", "scripts"]


def parse_skill_version(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    match = re.search(r"^version:\s*([\w.\-]+)\s*$", text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError(f"Could not find version in {skill_md}")
    return match.group(1)


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_skill_payload(dst_skill_dir: Path) -> None:
    reset_dir(dst_skill_dir)
    for rel in SKILL_CONTENT_PATHS:
        src = REPO_ROOT / rel
        dst = dst_skill_dir / rel
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_claude_plugin(version: str) -> None:
    plugin_root = REPO_ROOT / "claude-plugin" / CANONICAL_SKILL_DIRNAME
    copy_skill_payload(plugin_root / "skills" / CANONICAL_SKILL_DIRNAME)
    manifest = {
        "name": CANONICAL_SKILL_DIRNAME,
        "version": version,
        "description": "Claude Code plugin wrapper for the publication-chart-skill research figure/table workflow.",
        "author": AUTHOR,
        "homepage": CANONICAL_REPO_URL,
        "repository": CANONICAL_REPO_URL,
        "keywords": KEYWORDS,
    }
    write_json(plugin_root / ".claude-plugin" / "plugin.json", manifest)


def build_codex_plugin(version: str) -> None:
    plugin_root = REPO_ROOT / "plugins" / CANONICAL_SKILL_DIRNAME
    copy_skill_payload(plugin_root / "skills" / CANONICAL_SKILL_DIRNAME)
    manifest = {
        "name": CANONICAL_SKILL_DIRNAME,
        "version": version,
        "description": "Codex plugin wrapper for the publication-chart-skill research figure/table workflow.",
        "author": AUTHOR,
        "homepage": CANONICAL_REPO_URL,
        "repository": CANONICAL_REPO_URL,
        "keywords": KEYWORDS,
        "skills": "./skills/",
        "interface": {
            "displayName": "Publication Chart Skill",
            "shortDescription": "Choose, build, and review publication-grade figures and tables.",
            "longDescription": "Plugin wrapper for publication-chart-skill, a workflow-first research skill for selecting figure/table forms, routing to pubfig or pubtab, exporting paper-ready assets, and running publication QA.",
            "developerName": "Gaoruizhang",
            "category": "Research",
            "capabilities": ["Read", "Write"],
            "websiteURL": CANONICAL_REPO_URL,
            "defaultPrompt": [
                "Choose the right paper figure or table for these results.",
                "Turn this Excel benchmark sheet into a publication-ready LaTeX table.",
                "Review this weak scientific chart and propose a pubfig/pubtab revision route."
            ],
            "brandColor": "#2563EB"
        }
    }
    write_json(plugin_root / ".codex-plugin" / "plugin.json", manifest)

    marketplace = {
        "name": "publication-chart-skill-catalog",
        "interface": {
            "displayName": "Publication Chart Skill Catalog"
        },
        "plugins": [
            {
                "name": CANONICAL_SKILL_DIRNAME,
                "source": {
                    "source": "local",
                    "path": f"./plugins/{CANONICAL_SKILL_DIRNAME}"
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL"
                },
                "category": "Research"
            }
        ]
    }
    write_json(REPO_ROOT / ".agents" / "plugins" / "marketplace.json", marketplace)


def main() -> None:
    version = parse_skill_version(REPO_ROOT / "SKILL.md")
    build_claude_plugin(version)
    build_codex_plugin(version)
    print("Synced Claude Code and Codex plugin wrappers.")


if __name__ == "__main__":
    main()
