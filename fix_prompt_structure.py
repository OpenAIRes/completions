import json
import sys

FILENAME = 'completions_old.json'

with open(FILENAME, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = False
for item in data:
    if 'prompt' in item:
        prompt_val = item['prompt']
        # if it's already in desired format, skip
        if isinstance(prompt_val, dict) and 'content' in prompt_val and isinstance(prompt_val['content'], dict) and 'text' in prompt_val['content']:
            continue
        if isinstance(prompt_val, dict) and 'text' in prompt_val:
            text_val = prompt_val['text']
        else:
            text_val = prompt_val
        item['prompt'] = { 'content': { 'text': text_val } }
        changed = True

if changed:
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated' if changed else 'No changes needed')
