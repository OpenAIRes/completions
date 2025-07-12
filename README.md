# Completions Dataset

This repository contains a sample `completions.json` file with logprob
information produced by the OpenAI API.  The `analyze.py` script can
be used to inspect token probabilities.

## Usage

```
python3 analyze.py completions.json
```

The script prints each token in the completion, its probability, and
the top alternatives. It also computes the average log probability for
the full completion.
