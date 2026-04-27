# Episode Task Prompt

Use this prompt when you need quiz/code generation from one episode transcript set (Part 1, Part 2, Part 3, ...) and must output a **single quiz file** and **single code file**.

## Prompt

```text
I have transcript files for Episode {EPISODE_NUMBER}:
- Part 1
- Part 2
- Part 3

Generate the following in JSON format:
1. {NUM_QUIZ_SETS} quiz set(s) in one JSON file.
2. {NUM_CODE_SETS} code exercise set(s) in one JSON file.

Rules:
- Use the existing project schema for quiz and code JSON.
- Keep all quiz content in one file named: Episode{EPISODE_NUMBER}-Task-Quiz.json
- Keep code practice in one file named: Episode{EPISODE_NUMBER}-Task-Code.json
- Place quiz file under: quiz/during_class/Section {SECTION_NUMBER}/
- Place code file under: code/
- Quiz questions must include: 4 options, one correct answer, explanation, and hints.
- Code practice must include: title, instructions, starter_code, solution_code, and test_cases.
- Follow strict sequence mapping by part:
	- Quiz Set 1 -> Part 1 only
	- Quiz Set 2 -> Part 2 only
	- Quiz Set 3 -> Part 3 only
	- Code Set 1 -> Part 1 only
	- Code Set 2 -> Part 2 only
	- Code Set 3 -> Part 3 only
- Do not mix concepts from multiple transcript parts inside one set.
- If requested set count is less than total parts, start from earliest parts in order.

Also:
- Update history logs with what was created.
- If this is a unique task pattern, add a reusable prompt entry.
- Add/update a policy-style instructions file describing the workflow and quality checks.
```

## Placeholders
- `{EPISODE_NUMBER}`: e.g., `19`
- `{SECTION_NUMBER}`: e.g., `19`
- `{NUM_QUIZ_SETS}`: e.g., `2`
- `{NUM_CODE_SETS}`: e.g., `1`
