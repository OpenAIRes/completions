import json
import argparse
import math


def analyze(path: str) -> None:
    with open(path, 'r') as f:
        data = json.load(f)
    choices = data.get('choices', [])
    if not choices:
        print('No choices found')
        return

    logprobs = choices[0].get('logprobs', {}).get('content', [])
    if not logprobs:
        print('No logprobs found')
        return

    total_logprob = 0.0
    print('Token analysis:')
    for idx, entry in enumerate(logprobs, 1):
        token = entry['token']
        lp = entry['logprob']
        prob = math.exp(lp)
        total_logprob += lp
        top_tokens = [t['token'] for t in entry.get('top_logprobs', [])[:5]]
        print(f"{idx:2d}: {token!r} prob={prob:.4f} top={top_tokens}")

    avg_logprob = total_logprob / len(logprobs)
    avg_prob = math.exp(avg_logprob)
    print(f"\nAverage logprob: {avg_logprob:.4f} -> probability {avg_prob:.4f}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Analyze token probabilities in a completion file')
    parser.add_argument('file', help='Path to completions.json')
    args = parser.parse_args()
    analyze(args.file)


if __name__ == '__main__':
    main()
