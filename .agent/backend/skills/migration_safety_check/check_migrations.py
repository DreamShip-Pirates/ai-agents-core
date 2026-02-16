import argparse
import os
import re

DANGEROUS_KEYWORDS = [
    (r"DROP TABLE", "Destructive: Drops a table."),
    (r"TRUNCATE", "Destructive: Removes all data."),
    (r"DELETE FROM", "Destructive: Deletes rows (check for WHERE clause!)."),
    (r"ALTER TABLE .* DROP COLUMN", "Destructive: Drops a column."),
    (r"full scan", "Performance: Potential full table scan (if in comments of queries).")
]

def check_file(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for pattern, warning in DANGEROUS_KEYWORDS:
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append(f"Line {i+1}: Found '{pattern}'. {warning}")
    return issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="scripts", help="Directory to scan")
    parser.add_argument("--file", help="Specific file to scan")
    args = parser.parse_args()

    if args.file:
        files = [args.file]
    elif os.path.exists(args.dir):
        files = []
        for root, _, filenames in os.walk(args.dir):
            for name in filenames:
                if name.endswith(".ts") or name.endswith(".js") or name.endswith(".sql") or name.endswith(".py"):
                    files.append(os.path.join(root, name))
    else:
        print(f"Directory {args.dir} not found.")
        return

    print(f"Scanning {len(files)} files for dangerous patterns...")
    
    found_issues = False
    for f in files:
        issues = check_file(f)
        if issues:
            found_issues = True
            print(f"\n[WARN] {f}:")
            for issue in issues:
                print(f"  - {issue}")

    if not found_issues:
        print("\nNo dangerous patterns found.")
    else:
        print("\n[ALERT] Please review the warnings above.")

if __name__ == "__main__":
    main()
