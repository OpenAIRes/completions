"""Utility script to flatten the prompt structure in completions_old.json."""

import json

FILENAME = 'completions_old.json'

with open(FILENAME, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = False
for item in data:
    prompts = item.get('prompt')
    if isinstance(prompts, list):
        for p in prompts:
            if isinstance(p, dict) and isinstance(p.get('content'), dict) and 'text' in p['content']:
                p['content'] = p['content']['text']
                changed = True
if changed:
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated' if changed else 'No changes needed')
