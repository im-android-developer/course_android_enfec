import json
from pathlib import Path

base = Path('quiz/during_class/Section 8')
files = sorted([p for p in base.iterdir() if p.suffix=='.json'])

expected_question_keys = {"id","question","type","difficulty","tags","options","correctAnswers","explanation","hints"}

results = {}

for f in files:
    errors = []
    try:
        data = json.loads(f.read_text())
    except Exception as e:
        results[f.name] = {"valid": False, "errors": [f"JSON parse error: {e}"]}
        continue
    # top-level items
    if 'items' not in data or not isinstance(data['items'], list) or len(data['items'])==0:
        errors.append('missing or invalid top-level "items" array')
        results[f.name] = {"valid": False, "errors": errors}
        continue
    group = data['items'][0]
    if 'content' not in group or not isinstance(group['content'], list):
        errors.append('missing or invalid "content" in items[0]')
        results[f.name] = {"valid": False, "errors": errors}
        continue
    for i, q in enumerate(group['content'], start=1):
        if not isinstance(q, dict):
            errors.append(f'question {i} is not an object')
            continue
        missing = expected_question_keys - set(q.keys())
        if missing:
            errors.append(f'question {i} missing keys: {sorted(list(missing))}')
        # tags
        if 'tags' in q and not isinstance(q['tags'], list):
            errors.append(f'question {i} tags not a list')
        # options
        if 'options' in q:
            opts = q['options']
            if not isinstance(opts, list):
                errors.append(f'question {i} options not a list')
            else:
                if len(opts) != 4:
                    errors.append(f'question {i} has {len(opts)} options (expected 4)')
                ids = []
                for oi, opt in enumerate(opts, start=1):
                    if not isinstance(opt, dict):
                        errors.append(f'question {i} option {oi} not an object')
                        continue
                    if 'id' not in opt or 'text' not in opt:
                        errors.append(f'question {i} option {oi} missing id/text')
                    else:
                        ids.append(str(opt['id']))
                # correctAnswers
                if 'correctAnswers' in q:
                    ca = q['correctAnswers']
                    if not isinstance(ca, list) or len(ca)==0:
                        errors.append(f'question {i} correctAnswers must be a non-empty list')
                    else:
                        for answer in ca:
                            if str(answer) not in ids:
                                errors.append(f'question {i} correctAnswer "{answer}" not present in option ids {ids}')
        # hints
        if 'hints' in q and not isinstance(q['hints'], list):
            errors.append(f'question {i} hints not a list')
    results[f.name] = {"valid": len(errors)==0, "errors": errors}

print(json.dumps({"files": [p.name for p in files], "results": results}, indent=2))
