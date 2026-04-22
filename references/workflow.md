# Workflow

## Default decision order

1. Identify the scientific communication goal.
2. Probe the environment and available assets lightly.
3. Decide whether the evidence should be a figure, a table, or a paired figure+table deliverable.
4. Choose the strongest representation family.
5. Route figures to the `pubfig>=0.3.0` JSON CLI and tables to `pubtab`.
6. Produce the smallest runnable implementation.
7. Validate the route before treating it as final.
8. Specify export outputs explicitly.
9. Run publication QA.
10. Propose revisions if the result is weak.

## Handoff checklist

For every task, try to make these explicit:

- claim the artifact is supposed to support
- data shape and grouping structure
- target audience or venue expectations
- figure vs table role
- exact output filenames and formats
- whether the artifact is final, draft, or revision
- whether the current environment can execute the proposed route immediately

## Delivery contract

A strong response should make clear:

- which artifact type was chosen,
- why it was chosen,
- which tool owns each artifact,
- for figures: the `figure.spec.json` route plus `pubfig validate-spec` and `pubfig render`,
- for tables: the `pubtab` CLI/API route,
- what output files should be produced,
- what still needs user input or upstream data.

## Default output priorities

Prioritize in this order:

1. clarity of claim
2. correct artifact type
3. minimal runnable implementation
4. validation before final export
5. publication-ready export
6. QA and revision guidance

## Graceful degradation when tools are missing

If `pubfig>=0.3.0` or `pubtab` is not installed:

- first try the bundled auto-install helper,
- if the helper is unavailable, give the explicit install command,
- keep the design workflow going if installation fails,
- provide a JSON spec or pseudocode route the user can run after installing,
- preserve the QA and revision guidance.

## Figure / table split rules

Use a **figure** when the reader needs to quickly perceive:

- trend
- distribution shape
- relationship
- calibration or diagnostic behavior
- composition or hierarchy
- visual comparison across a moderate number of groups

Use a **table** when the reader needs:

- exact numbers
- many metrics side by side
- benchmark grids
- ablation matrices
- appendix-style detail
- reproducible value lookup

Use **both** when:

- the figure carries the visual claim,
- the table preserves exact values,
- or the paper section benefits from a fast visual summary plus precise numeric evidence.
