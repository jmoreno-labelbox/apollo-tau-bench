#!/usr/bin/env python3
"""
Normalize JSON Schema types in tau_bench/envs by replacing 'int' -> 'integer'.

This scans all files under tau_bench/envs/ (both .py and .json), and replaces
occurrences of JSON Schema field types defined as:
  "type": "int"  or  'type': 'int'
with the valid JSON Schema type:
  "type": "integer"

Usage:
  Dry run (show what would change):
    python scripts/fix_schema_types.py --dry-run

  Apply changes in-place:
    python scripts/fix_schema_types.py --write
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
ENVS_DIR = REPO_ROOT / "tau_bench" / "envs"


# Two precise patterns for JSON-like dicts in Python/JSON
PATTERNS = [
    re.compile(r"(\"type\"\s*:\s*)\"int\""),  # "type": "int"
    re.compile(r"(\'type\'\s*:\s*)\'int\'"),      # 'type': 'int'
]


def fix_text(text: str) -> Tuple[str, int]:
    total = 0
    for pat in PATTERNS:
        text, n = pat.subn(r"\1\"integer\"", text)
        total += n
    return text, total


def main() -> None:
    parser = argparse.ArgumentParser(description="Replace JSON Schema type 'int' -> 'integer' in tau_bench/envs")
    parser.add_argument("--dry-run", action="store_true", help="Show planned changes without writing")
    parser.add_argument("--write", action="store_true", help="Write changes to files")
    args = parser.parse_args()

    if not ENVS_DIR.is_dir():
        print(f"Not found: {ENVS_DIR}")
        raise SystemExit(1)

    changed_files = 0
    changed_occurrences = 0
    scanned_files = 0

    for path in ENVS_DIR.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in {".py", ".json"}:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except Exception:
            continue
        scanned_files += 1
        fixed, n = fix_text(original)
        if n > 0:
            changed_files += 1
            changed_occurrences += n
            print(f"fix: {path} (+{n})")
            if args.write and not args.dry_run:
                path.write_text(fixed, encoding="utf-8")

    print("\n==== Summary ====")
    print(f"Scanned files: {scanned_files}")
    print(f"Files needing change: {changed_files}")
    print(f"Total occurrences replaced: {changed_occurrences}")
    if not args.write:
        print("(dry-run) No files were modified. Re-run with --write to apply changes.")


if __name__ == "__main__":
    main()


