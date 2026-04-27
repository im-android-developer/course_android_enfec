# Essentials History

## 2026-04-23 - Policy Update (Sequence-Based Sets)
- Updated essentials policy to enforce part-wise sequence mapping.
- New mandatory rule:
  - Quiz Set 1 must use only Episode Part 1
  - Quiz Set 2 must use only Episode Part 2
  - Code Set 1 must use only Episode Part 1
  - Next sets continue in the same order (Part 3, Part 4, ...)
- Mixing concepts from multiple parts in a single set is now disallowed.
- Updated files:
  - `essentials/instructions.md`
  - `essentials/prompt.md`

## 2026-04-23 - Code Generation Fix Under /code
- Updated `code/Episode19-Task-Code.json` to include sequence-based code sets under the `/code` section.
- Current mapping in the single code file:
  - Code Set 1 -> Episode 19 Part 1
  - Code Set 2 -> Episode 19 Part 2
  - Code Set 3 -> Episode 19 Part 3
- Kept single-file naming convention: `Episode19-Task-Code.json`.

## 2026-04-23 - Episode 19 Task Generation
- Created quiz file: `quiz/during_class/Section 19/Episode19-Task-Quiz.json`
  - Contains 2 quizzes in one JSON file.
  - Quiz 1 is mapped to Episode 19 Part 1 only.
  - Quiz 2 is mapped to Episode 19 Part 2 only.
- Created code file: `code/Episode19-Task-Code.json`
  - Contains 1 Kotlin code practice in one JSON file.
  - Code Set 1 is mapped to Episode 19 Part 1 only (safe call + Elvis + if/else-if validation).
- Created new folder and documentation set: `essentials/`
  - Added `history.md`, `prompt.md`, and `instructions.md`.
- Updated existing generation records in `Instructions/history.md` and extended reusable prompt guidance in `Instructions/prompt.md` for the unique Episode task naming convention.

## 2026-04-27 - Episode 20 Task Quiz Generation
- Created quiz file: `quiz/during_class/Section 20/Episode20-Task-Quiz.json`
  - Contains 3 quiz sets in one JSON file.
  - Quiz Set 1 is mapped to transcript Part 1 only (TextInputLayout login migration, null safety, validation order, finish navigation behavior).
  - Quiz Set 2 is mapped to transcript Part 2 only (function basics via input-process-output analogy and reusability motivation).
  - Quiz Set 3 is mapped to transcript Part 3 only (Kotlin function syntax, parameters, return type, function calls, and output flow).
