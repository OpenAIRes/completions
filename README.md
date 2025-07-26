# completions

This repository contains logs from the OpenAI API and some helper scripts.

## Scripts

- `parse_messages.py`: parse concatenated JSON logs into individual objects.
- `json_to_csv.py`: convert a log file (e.g. `messages.json` or `completions.json`) to a CSV file with columns `id`, `role`, and `content`.

## Usage

To convert a log file to CSV:

```bash
python3 json_to_csv.py messages.json messages.csv
```

The CSV can then be loaded into a spreadsheet or analysis tool.
