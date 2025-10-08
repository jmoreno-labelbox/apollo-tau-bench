#!/usr/bin/env python3
"""
Fix common JSON Schema issues across tau_bench/envs:
 - Replace invalid types: int->integer, float->number, bool->boolean
 - Remove top-level oneOf/anyOf/allOf/not from parameters objects
 - Add default items to array properties missing "items"

Usage:
  Dry run:  python scripts/fix_schema_common_issues.py --dry-run
  Write:    python scripts/fix_schema_common_issues.py --write
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENVS_DIR = REPO_ROOT / "tau_bench" / "envs"


TYPE_FIX_PATTERNS = [
    (re.compile(r"(\"type\"\s*:\s*)\"int\""), r"\1\"integer\""),
    (re.compile(r"(\'type\'\s*:\s*)\'int\'"), r"\1\"integer\""),
    (re.compile(r"(\"type\"\s*:\s*)\"float\""), r"\1\"number\""),
    (re.compile(r"(\'type\'\s*:\s*)\'float\'"), r"\1\"number\""),
    (re.compile(r"(\"type\"\s*:\s*)\"bool\""), r"\1\"boolean\""),
    (re.compile(r"(\'type\'\s*:\s*)\'bool\'"), r"\1\"boolean\""),
    (re.compile(r"(\"type\"\s*:\s*)\"list\""), r"\1\"array\""),
    (re.compile(r"(\'type\'\s*:\s*)\'list\'"), r"\1\"array\""),
    (re.compile(r"(\"type\"\s*:\s*)\"date\""), r"\1\"string\""),
    (re.compile(r"(\'type\'\s*:\s*)\'date\'"), r"\1\"string\""),
    (re.compile(r"(\"type\"\s*:\s*)None\b"), r"\1\"object\""),
    (re.compile(r"(\'type\'\s*:\s*)None\b"), r"\1\"object\""),
    (re.compile(r"(\"type\"\s*:\s*)\"str\""), r"\1\"string\""),
    (re.compile(r"(\'type\'\s*:\s*)\'str\'"), r"\1\"string\""),
    (re.compile(r"(\"type\"\s*:\s*)\"dict\""), r"\1\"object\""),
    (re.compile(r"(\'type\'\s*:\s*)\'dict\'"), r"\1\"object\""),
    # Occasionally schemas use the non-standard "dictionary"
    (re.compile(r"(\"type\"\s*:\s*)\"dictionary\""), r"\1\"object\""),
    (re.compile(r"(\'type\'\s*:\s*)\'dictionary\'"), r"\1\"object\""),
]


ONEOF_LINE_RE = re.compile(r"^\s*\"(oneOf|anyOf|allOf|not)\"\s*:\s*\[", re.M)


def strip_top_level_combinators_in_parameters(text: str) -> tuple[str, int]:
    """Naively remove top-level oneOf/anyOf/allOf/not blocks that appear directly under a "parameters": { ... } section.
    This uses a simple bracket counter starting at the opening '[' after the key and removes up to the matching ']'.
    """
    total_removed = 0
    out = []
    i = 0
    n = len(text)
    while i < n:
        m = ONEOF_LINE_RE.search(text, i)
        if not m:
            out.append(text[i:])
            break
        # append up to start of match
        out.append(text[i:m.start()])
        # find matching closing ']' starting at m.end()-1
        j = m.end()
        depth = 1
        while j < n and depth > 0:
            if text[j] == '[':
                depth += 1
            elif text[j] == ']':
                depth -= 1
            j += 1
        # skip optional trailing comma and whitespace/newlines
        k = j
        while k < n and text[k] in ' \t\r\n,':
            # stop at next non-space or at closing brace that likely ends the entry
            if text[k] == '}':
                break
            k += 1
        i = k
        total_removed += 1
    return ("".join(out), total_removed)


def add_items_to_arrays(text: str) -> tuple[str, int]:
    """Heuristically add items to array properties lacking items.
    Looks for lines with '"type": "array"' where within the next 8 non-empty lines there is no '"items"'.
    Inserts '"items": {"type": "string"},' on the next line with matching indentation.
    """
    lines = text.splitlines(keepends=False)
    changed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.search(r"\"type\"\s*:\s*\"array\"\s*,?\s*$", line):
            # scan ahead for items
            has_items = False
            for j in range(i + 1, min(i + 9, len(lines))):
                if re.search(r"\"items\"\s*:\s*", lines[j]):
                    has_items = True
                    break
                if re.search(r"^\s*}\s*,?\s*$", lines[j]):
                    # property block likely ends before items
                    break
            if not has_items:
                # determine indent
                indent = re.match(r"^(\s*)", line).group(1) or ""
                insert = indent + "\"items\": {\"type\": \"string\"},"
                lines.insert(i + 1, insert)
                changed += 1
                i += 1
        i += 1
    return ("\n".join(lines) + ("\n" if text.endswith("\n") else ""), changed)


def fix_file(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8")
    total = 0
    # Type fixes
    for pat, repl in TYPE_FIX_PATTERNS:
        text, n = pat.subn(repl, text)
        total += n
    # Remove combinators under parameters
    text, n = strip_top_level_combinators_in_parameters(text)
    total += n
    # Add items to arrays
    text, n = add_items_to_arrays(text)
    total += n
    return text, total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--envs-root", type=str, default=str(DEFAULT_ENVS_DIR), help="Path to envs root (default: tau_bench/envs)")
    args = ap.parse_args()

    scanned = 0
    changed_files = 0
    changes = 0
    envs_dir = Path(args.envs_root)
    for path in envs_dir.rglob("*.py"):
        try:
            fixed, n = fix_file(path)
        except Exception:
            continue
        scanned += 1
        if n > 0:
            changed_files += 1
            changes += n
            print(f"fix: {path} (+{n})")
            if args.write and not args.dry_run:
                path.write_text(fixed, encoding="utf-8")

    print("\n==== Summary ====")
    print(f"Scanned: {scanned}")
    print(f"Changed files: {changed_files}")
    print(f"Total fixes: {changes}")
    if not args.write:
        print("(dry-run) Not writing changes")


if __name__ == "__main__":
    main()


