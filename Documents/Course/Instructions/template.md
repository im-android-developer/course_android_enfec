# Templates

## Quiz JSON Template

```json
{
  "items": [
    {
      "name": "Section{N}-Episode{N}-Part{X}",
      "difficulty": "easy | medium | hard",
      "content": [
        {
          "id": "S{N}-E{N}-P{X}-Q{Y}",
          "question": "The question text",
          "type": "mcq",
          "difficulty": "easy | medium | hard",
          "tags": ["Tag1", "Tag2"],
          "options": [
            { "id": "a", "text": "Option A" },
            { "id": "b", "text": "Option B" },
            { "id": "c", "text": "Option C" },
            { "id": "d", "text": "Option D" }
          ],
          "correctAnswers": ["a"],
          "explanation": "Why the correct answer is correct",
          "hints": ["Hint 1", "Hint 2", "Hint 3"]
        }
      ]
    }
  ]
}
```

### Field Rules
- **name**: `Section{N}-Episode{N}-Part{X}` where N = section number, X = part number
- **id**: `S{N}-E{N}-P{X}-Q{Y}` where Y = question number (sequential within part)
- **type**: Always `"mcq"` for multiple-choice questions
- **options**: Exactly 4 options labeled a, b, c, d
- **correctAnswers**: Array with one correct option id
- **hints**: Exactly 3 hints per question, progressively more revealing
- **difficulty**: Spread across easy/medium/hard based on topic complexity
- **tags**: Relevant topic tags (e.g., "Kotlin", "Android Development", "Control Flow")

---

## Code Exercise JSON Template

```json
{
  "items": [
    {
      "title": "Exercise Title",
      "instructions": "**Problem:**\\nDescription\\n\\n**What we want:**\\nDetailed requirements\\n\\n**Syntax:**\\n```\\nCode example\\n```\\n\\n**Example 1:**\\nInput/setup description\\nOutput: expected\\nExplanation: why",
      "difficulty": "easy | medium | hard",
      "language_key": "kotlin",
      "time_limit": 2,
      "memory_limit": 256,
      "starter_code": "fun main() {\n    // Comments guiding the student\n}",
      "execute_template": "",
      "solution_code": "fun main() {\n    // Full working solution\n}",
      "test_cases": [
        { "input": "", "output": "Expected output", "is_sample": true }
      ]
    }
  ]
}
```

### Field Rules
- **title**: Short, descriptive exercise name
- **instructions**: Markdown with sections: Problem, What we want, Syntax, Examples (at least 2)
- **language_key**: Always `"kotlin"`
- **time_limit**: Default `2` (minutes)
- **memory_limit**: Default `256` (MB)
- **starter_code**: Skeleton with comments as hints
- **execute_template**: Always `""` (empty string)
- **solution_code**: Complete, working Kotlin code
- **test_cases**: Array of objects with `input`, `output`, and `is_sample` (boolean)
