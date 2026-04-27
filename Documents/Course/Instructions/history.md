# Generation History

## Section 15 — Episodes 1–2
- **Quiz:** `quiz/during_class/Section 15/Section15-Episodes1-2.json`
  - 2 quizzes, 5 questions each
  - Part 1: Comparison operators (`!=`, `>`, `<`, `>=`, `<=`), voting age example
  - Part 2: XML IDs, `setContentView`, `R` = Resources, `val` for immutability, `setOnClickListener`
- **Code:** `code/Section15-CodeExercises.json`
  - 1 easy exercise: "Voting Eligibility Check with Comparison Operators" — `>=` vs `>` with age=18

## Section 16 — Episodes 1–3
- **Quiz:** `quiz/during_class/Section 16/Section16-Episodes1-3.json`
  - 3 quizzes, 10 questions each
  - Part 1: `.text.toString()` collection from EditText, `var` vs `val` for components, `setOnClickListener`, component type casting, three-step text flow, logic inside click listeners
  - Part 2: `if` statement true/false execution, `==` comparison for login, Toast messages (`makeText`, `.show()`, `this` context), behavior without `else`
  - Part 3: `else` statement syntax (no parentheses), invalid credentials feedback, `&&` logical AND operator, truth table, combining conditions, code quality
- **Code:** `code/Section16-CodeExercises.json`
  - 2 medium exercises:
    1. "Login Credential Check with If-Else" — if-else to verify username, userId="android", output "Login Successful"
    2. "Combined Login Check with Logical AND Operator" — && to check both username+password, userId="admin", userPassword="pass@456"

## Section 17 — Episodes 1–2
- **Quiz:** `quiz/during_class/Section 17/Section17-Episodes1-2.json`
  - 2 quizzes, 10 questions each
  - Part 1: What is Intent, explicit intents, `this` keyword as source, Intent constructor (context + class), `startActivity()`, intent inside if block, `Dashboard::class.java`, importing Intent class, static pages without intents, map/path analogy
  - Part 2: Multi-destination navigation, TextView for sign-up, separating click listeners, component setup flow, variable naming (`intentValue` vs `intent`), full navigation sequence, creating activities, importing via context actions, code placement, dual-destination result
- **Code:** `code/Section17-CodeExercises.json`
  - 2 medium exercises:
    1. "Navigate to Dashboard After Login Validation" — && check, userId="android", userPassword="android@123", output "Login Successful\nNavigating to Dashboard"
    2. "Multi-Destination Navigation Selector" — if-else if-else on userRole="admin", output "Navigating to Admin Dashboard"

## Section 18 — Episodes 1–2
- **Quiz:** `quiz/during_class/Section 18/Section18-Episodes1-2.json`
  - 2 quizzes, 10 questions each
  - Part 1: TextInputLayout as outer container, TextInputEditText as inner input, `boxStrokeColor`, `boxStrokeWidth`, full package name in XML, floating label animation, overriding default inactive border colour via `mtrl_textinput_default_box_stroke_color`, `android:hint`, `android:textColorHint`, `inputType` attribute
  - Part 2: `passwordToggleEnabled`, `passwordToggleTint`, `textPassword` inputType, `counterEnabled`, `counterMaxLength`, `findViewById<TextInputLayout>`, collecting text via `.editText?.text.toString()`, difference from EditText text collection, `setOnClickListener` for sign-up, full sign-up form workflow
- **Code:** `code/Section18-CodeExercises.json`
  - 2 medium exercises:
    1. "Sign-Up Form Field Collection with TextInputLayout" — collect fields, check password == confirmPassword, print fields or "Passwords do not match"
    2. "Password Strength Validator with Character Counter" — if-else if-else on password.length vs maxLength/min 6, output "Password accepted\nCharacter count: 8/20"

## Section 19 — Episode 19 (Task Format)
- **Quiz:** `quiz/during_class/Section 19/Episode19-Task-Quiz.json`
  - 1 consolidated quiz file containing 2 quiz sets
  - Quiz 1: Null/blank handling, safe call (`?.`), Elvis (`?:`), length validation, else-if placement, ID mismatch debugging
  - Quiz 2: `when` as switch alternative, arrow operator (`->`), `isEmpty`, TextInputLayout inline errors (`.error`), default `else`, Intent navigation, `finish()`, error text color
- **Code:** `code/Episode19-Task-Code.json`
  - 1 medium exercise:
    1. "Episode 19 Task Code - Sign-Up Validation with Null Safety and When" — safe-call + Elvis defaults, ordered `when` validation checks, success flow simulation with navigation and screen close messages

## Section 20 — Episode 20 (Task Format)
- **Quiz:** `quiz/during_class/Section 20/Episode20-Task-Quiz.json`
  - 1 consolidated quiz file containing 3 quiz sets
  - Quiz Set 1 (Part 1 only): TextInputLayout migration on login, ID consistency, null-safe text collection, `if-else` ordering, inline errors, and `finish()` behavior
  - Quiz Set 2 (Part 2 only): Function fundamentals using input-process-output analogies and code reusability motivation
  - Quiz Set 3 (Part 3 only): Kotlin function declaration syntax, parameters, return type, `return`, and calling `square`/`add` with `println`
