import json
import sys
from pathlib import Path


def parse_concatenated_json(filename):
    text = Path(filename).read_text()
    decoder = json.JSONDecoder()
    idx = 0
    objs = []
    text_len = len(text)
    while idx < text_len:
        obj, end = decoder.raw_decode(text, idx)
        objs.append(obj)
        idx = end
        while idx < text_len and text[idx].isspace():
            idx += 1
    return objs


def main(argv):
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <messages.json> [output.json]")
        return 1
    input_path = argv[1]
    output_path = argv[2] if len(argv) > 2 else None
    objs = parse_concatenated_json(input_path)
    if output_path:
        Path(output_path).write_text(json.dumps(objs, indent=2))
    else:
        json.dump(objs, sys.stdout, indent=2)
        print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
