# Episode Task Instructions Policy

## Purpose
Define a repeatable workflow to generate quiz and code assets from transcript parts with consistent naming, structure, and quality.

## Sequence Mapping Policy (Mandatory)
- Keep strict transcript order: Part 1 -> Part 2 -> Part 3 -> ...
- One set must map to one part only.
- Do not mix topics from multiple parts inside the same quiz set or code set.
- Mapping rule:
  - Quiz Set 1 uses only Episode Part 1
  - Quiz Set 2 uses only Episode Part 2
  - Quiz Set 3 uses only Episode Part 3
  - Code Set/Exercise 1 uses only Episode Part 1
  - Code Set/Exercise 2 uses only Episode Part 2
  - Code Set/Exercise 3 uses only Episode Part 3
- If fewer sets are requested than available parts, use the earliest parts first in order.

## Output Scope
- Generate quiz/code counts as requested by the task.
- Use **JSON** format only for quiz/code deliverables.
- Keep outputs consolidated:
  - Quiz: one file only
  - Code: one file only

## Naming Policy
- Quiz file: `Episode{n}-Task-Quiz.json`
- Code file: `Episode{n}-Task-Code.json`
- Here, `{n}` is the episode number from transcript names.

## Placement Policy
- Quiz file location: `quiz/during_class/Section {n}/`
- Code file location: `code/`

## Content Policy
- Quiz requirements:
  - Include the required number of quiz sets inside one JSON file.
  - Each question includes: `id`, `question`, `type`, `difficulty`, `tags`, 4 `options`, `correctAnswers`, `explanation`, and `hints`.
  - Each quiz set must be sourced from exactly one transcript part based on sequence mapping.
- Code practice requirements:
  - Include the required number of exercise objects in the JSON file.
  - Include: `title`, `instructions`, `difficulty`, `language_key`, `time_limit`, `memory_limit`, `starter_code`, `execute_template`, `solution_code`, `test_cases`.
  - Each code exercise must be sourced from exactly one transcript part based on sequence mapping.
  - Keep implementation aligned with taught concepts and beginner-friendly progression.

## Quality and Validation Policy
- Verify JSON syntax before finalizing.
- Ensure file paths and names match the naming policy exactly.
- Avoid creating multiple output files for the same episode task type.
- Validate that no quiz/code set mixes concepts across transcript parts.
- Keep explanations and hints instructional, clear, and transcript-aligned.

## Documentation Policy
- Record completed work in a history file with date and output paths.
- If a new/unique task format appears, add a reusable prompt template.
- Keep policy documents concise and update them when workflow changes.

## Breakdown Policy
- If the system stops due to any reason, then instead of writing the whole file, write into chunks into the same file, and update the order into history.md for the reference.