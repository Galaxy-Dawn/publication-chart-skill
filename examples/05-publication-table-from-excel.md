# Example 5 — Publication-ready LaTeX table from Excel

## User-style prompt

Convert this Excel benchmark sheet into a publication-ready LaTeX table and give me a preview path before I paste it into the paper.

## Expected skill interpretation

- artifact: table
- maturity: publication-ready generation
- structure: single table
- goal: exact benchmark values in LaTeX

## Preferred route

- primary tool: `pubtab`
- likely route: `xlsx2tex` + `preview`
- `tabularray` only if the manuscript/backend requires it

## Minimum acceptable output shape

- provide the exact `pubtab` command or Python route
- include caption/label guidance when appropriate
- include preview generation
- mention table width/span concerns if relevant
