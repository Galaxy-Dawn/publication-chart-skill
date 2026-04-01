# Workflow

## Default decision order

1. Identify the scientific communication goal.
2. Decide whether the evidence should be a figure, a table, or a paired figure+table deliverable.
3. Choose the strongest representation family.
4. Route to `pubfig`, `pubtab`, or both.
5. Produce the smallest runnable implementation.
6. Specify export outputs explicitly.
7. Run publication QA.
8. Propose revisions if the result is weak.

## Handoff checklist

For every task, try to make these explicit:

- claim the artifact is supposed to support
- data shape and grouping structure
- target audience or venue expectations
- figure vs table role
- exact output filenames and formats
- whether the artifact is final, draft, or revision

## Default output priorities

Prioritize in this order:

1. clarity of claim
2. correct artifact type
3. minimal runnable implementation
4. publication-ready export
5. revision guidance

## Graceful degradation when tools are missing

If `pubfig` or `pubtab` is not installed:

- keep the workflow going,
- provide installation guidance,
- provide pseudocode or draft commands,
- specify the recommended artifact structure,
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
