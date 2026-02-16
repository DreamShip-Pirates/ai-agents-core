import argparse
import re
from collections import Counter

def analyze(file_path):
    print(f"Analyzing logs from: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    error_patterns = [
        r"ERROR",
        r"Exception",
        r"Error:",
        r"status[:\s]*5\d{2}",  # 500 range
        r"ReferenceError",
        r"TypeError"
    ]

    counts = Counter()
    details = []

    for i, line in enumerate(lines):
        for pattern in error_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                counts[pattern] += 1
                details.append(f"Line {i+1}: {line.strip()[:200]}") # Truncate long lines

    print("\n--- Summary ---")
    if not counts:
        print("No obvious errors found.")
    else:
        for k, v in counts.items():
            print(f"Pattern '{k}': {v} matches")

    print("\n--- Details (First 10) ---")
    for d in details[:10]:
        print(d)
    if len(details) > 10:
        print(f"... and {len(details) - 10} more.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to log file")
    args = parser.parse_args()
    analyze(args.file)
