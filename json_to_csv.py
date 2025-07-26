import json
import csv
import sys
from pathlib import Path
from typing import Iterable, Dict, Any

from parse_messages import parse_concatenated_json


def iter_messages(obj: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    """Yield message dictionaries from a parsed log object."""
    for msg in obj.get("data", []):
        yield msg


def main(argv: Iterable[str]) -> int:
    if len(argv) < 3:
        print(f"Usage: {argv[0]} <input.json> <output.csv>")
        return 1
    input_path = Path(argv[1])
    output_path = Path(argv[2])

    objs = parse_concatenated_json(str(input_path))
    rows = []
    for obj in objs:
        for msg in iter_messages(obj):
            rows.append({
                "id": msg.get("id"),
                "role": msg.get("role"),
                "content": msg.get("content"),
            })

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "role", "content"])
        writer.writeheader()
        writer.writerows(rows)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
