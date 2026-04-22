# Example 8 — Review an existing figure or table draft

## User-style prompt

Here is my current results figure screenshot and the draft benchmark table. Please tell me what is weak, whether the figure should stay a figure or become a figure + table pair, and give me the recommended pubfig/pubtab revision path.

## Expected skill interpretation

- artifact: review / revision
- maturity: existing deliverable upgrade
- structure: figure-only or figure + companion table
- goal: keep the strongest communication role for each artifact instead of polishing a weak form blindly

## Preferred route

- inspect the current figure/table role split first,
- recommend whether the figure should stay visual and the table should preserve exact values,
- use `pubfig>=0.3.0` JSON CLI for the figure revision,
- use `pubtab` for the table revision when both are needed.

## Minimum acceptable output shape

- identify the concrete publication weaknesses in the current artifact(s),
- say whether the final deliverable should be figure-only, table-only, or figure + table,
- provide one runnable `figure.spec.json` plus `pubfig validate-spec` / `pubfig render` route for figure revision when needed,
- provide one runnable `pubtab` route for table revision when needed,
- define explicit export filenames and a short QA checklist.
