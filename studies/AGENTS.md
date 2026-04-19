# Studies

## Audience
- Assume the reader may not remember facts, figures, conclusions from prior sources, studies

## Workflow
- A study consists of a _framing_ (the README and possibly support files), and
- Scripts (python preferred, use lib where possible/applicablee)
- Findings (one or more files, depending on the size/complexity)
- Outputs (charts, graphs, spreadsheets, etc.)
- Be disciplined: if an investigation is warranted, build the track, then perform it upon user's approval

## Framing
- Stay focused on the purpose of the project (../README.md) and the particular study (./README.md)
- Explain how we got here (reference past studies outcomes, findings, open questions, etc)
- Design and lay out the approach of the study (what we hope to do)
- Break the study into separate tracks, phases as appropriate
- Clearly identify and state:
  - Goals: what we are trying to accomplish (theories)
  - Strategy: how we expect to accomplish the goals (equations, models, approaches)
  - Tactics: computational approach to the strategy (scripts, functions, mathematics)
- Frame early track(s) in detail, keep later (dependent) tracks general as things may change
- A good pattern is to number only the next track, keep future tracks in a pool to pick from as appropriate

## Findings
- When a study is complete, perform the writeup:
- Keep findings and outputs correlated to their track
- State the results in a clear, simple, understandable way -- no jargon
- Also explain how each result affects the applicable hypothesis (helps or hurts)
- Review meaning of variables, terminology where not already obvious
- Interpret the results as can be done without guessing
- Don't rely on the reader to remember all meanings, implications
- Keep an open mind about execution possible errors:
  - The study might have been framed incorrectly
  - The approach might have been wrong
  - The implementation might have been wrong
- This means to not be overconfident about either positive or negative results
- Summarize results in plain language: What does this mean for the study hypotheses
- Project next possible steps: Where do we go from here

## Repo Management
- The user will typically want to commit at regular milestones:
  - When a new study is framed
  - When a track has be completed or a study is closed
  - New entries entered to the INBOX

## Tracking
- Studies are tracked in ./STATUS.md
- Maintain the file structure as studies progress
  - Acive studies: Short summary
  - Backlog: Intended future studies
  - Done: studies concluded whether positively or negatively
- Inbox tracked in qa/INBOX.md
  - Any questions we can think of that might spawn future studies or analyses
  - Questions that can be answered easily are addressed in a qa/Q*.md
  - More extensive projects become a study
- Scan the INBOX at the end of each study when evaluating possible next subjects to pursue

## Scripting
- Python scripts should use the shared lib/*.py resources where helpful
- Numpy and others available throut the virtual environment (venv)

## Nomenclature
- See ./Taxonomy.md
