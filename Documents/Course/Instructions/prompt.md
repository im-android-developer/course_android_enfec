# Generation Prompt

Use this prompt when generating new quizzes and code exercises from transcript files.

---

## Prompt

```
I have transcript files for Section {SECTION_NUMBER}, Episodes {EPISODE_RANGE}.

### Transcript Content:
{PASTE_TRANSCRIPT_CONTENT_HERE}

### Generate the following:

**Quizzes:**
- {NUM_QUIZZES} quiz(es), {NUM_QUESTIONS} questions each
- Difficulty: {DIFFICULTY} (easy/medium/hard mix)
- Follow the quiz JSON template from Instructions/template.md
- ID format: S{N}-E{N}-P{X}-Q{Y}
- Name format: Section{N}-Episode{N}-Part{X}
- Each question must have: 4 options (a-d), 1 correct answer, explanation, 3 hints
- Tags should reflect the specific topics covered

**Code Exercises:**
- {NUM_EXERCISES} exercise(s), difficulty: {EXERCISE_DIFFICULTY}
- Follow the code exercise JSON template from Instructions/template.md
- Language: Kotlin
- Include: Problem, What we want, Syntax, at least 2 Examples
- Provide starter_code with guiding comments
- Provide complete solution_code
- Include test_cases with expected output

### Output Files:
- Quiz: `quiz/during_class/Section {SECTION_NUMBER}/Section{SECTION_NUMBER}-Episodes{EPISODE_RANGE}.json`
- Code: `code/Section{SECTION_NUMBER}-CodeExercises.json`
```

---

## Placeholders

| Placeholder | Description | Example |
|---|---|---|
| `{SECTION_NUMBER}` | Section number | `18` |
| `{EPISODE_RANGE}` | Episode range covered | `1-3` |
| `{NUM_QUIZZES}` | Number of quizzes to generate | `2` |
| `{NUM_QUESTIONS}` | Questions per quiz | `10` |
| `{DIFFICULTY}` | Overall difficulty level | `medium` |
| `{NUM_EXERCISES}` | Number of code exercises | `2` |
| `{EXERCISE_DIFFICULTY}` | Code exercise difficulty | `medium` |
| `{PASTE_TRANSCRIPT_CONTENT_HERE}` | Full transcript text | (paste content) |

---

## Unique Task Prompt (Episode n Task Format)

Use this when the requirement is: **2 quizzes + 1 code practice**, but output must stay consolidated into one quiz file and one code file for a single episode.

```
I have transcript files for Episode {EPISODE_NUMBER}:
- Part 1
- Part 2
- Part 3

### Transcript Content:
{PASTE_TRANSCRIPT_CONTENT_HERE}

### Generate the following:

**Quizzes:**
- 2 quiz sets in one JSON file
- Cover concepts from all provided parts
- Follow quiz template fields (options, correct answer, explanation, hints, tags)

**Code Practice:**
- 1 code practice in one JSON file
- Follow code exercise template fields (instructions, starter_code, solution_code, test_cases)
- Language: Kotlin

### Naming Rules:
- Quiz file name: `Episode{EPISODE_NUMBER}-Task-Quiz.json`
- Code file name: `Episode{EPISODE_NUMBER}-Task-Code.json`

### Output Paths:
- Quiz: `quiz/during_class/Section {SECTION_NUMBER}/Episode{EPISODE_NUMBER}-Task-Quiz.json`
- Code: `code/Episode{EPISODE_NUMBER}-Task-Code.json`

### Documentation Updates:
- Update history with what was created
- If this is a unique format, add/update reusable prompt guidance
- Add/update an instructions policy describing workflow and validation checks
```
