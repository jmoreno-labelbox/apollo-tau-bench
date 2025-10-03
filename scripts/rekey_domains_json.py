#!/usr/bin/env python3
import argparse
import glob
import json
import os
import sys
from collections import Counter
from typing import Any, Dict, Iterable, List, Optional, Tuple


def detect_indent_string(file_text: str) -> Optional[str]:
    """Infer indentation string from an existing JSON file.

    - Returns "\t" if tabs are used.
    - Returns a string of spaces representing the minimal indent step if spaces are used.
    - Returns None if indentation cannot be determined (e.g., minified single-line JSON).
    """
    lines = file_text.splitlines()
    indent_samples: List[str] = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        # Collect leading whitespace
        leading = line[: len(line) - len(line.lstrip(" \t"))]
        if not leading:
            continue
        # If the line starts with mixed indentation, skip it to avoid mixing styles
        if " " in leading and "\t" in leading:
            continue
        indent_samples.append(leading)

    if not indent_samples:
        return None

    # If any sample uses tabs and none use spaces, prefer tabs
    uses_tab = any("\t" in s for s in indent_samples)
    uses_space = any(" " in s for s in indent_samples)
    if uses_tab and not uses_space:
        return "\t"
    if uses_space and not uses_tab:
        # Determine minimal positive number of spaces used as a step
        space_counts = [len(s) for s in indent_samples if set(s) == {" "}]
        if not space_counts:
            return None
        minimal = min(c for c in space_counts if c > 0)
        # Some files may have inconsistent steps; pick the most common minimal step
        counts = Counter(space_counts)
        most_common_step = counts.most_common(1)[0][0]
        step = min(minimal, most_common_step)
        if step <= 0:
            return None
        return " " * step

    # Mixed or undetectable; do not force indentation
    return None


def determine_primary_key(event_obj: Dict[str, Any]) -> Optional[str]:
    """Return the first key in the object (preserving original order)."""
    for key in event_obj.keys():
        return key
    return None


def rekey_events(
    events: List[Dict[str, Any]],
) -> Tuple[Optional[Dict[str, Dict[str, Any]]], Optional[str], List[str]]:
    """Rekey a list of event dicts into a dict by the first field in each event.

    Returns (result, primary_key, warnings)
    - result: dict keyed by the primary key values, or None if cannot proceed
    - primary_key: detected key name
    - warnings: list of warnings encountered
    """
    warnings: List[str] = []
    if not events:
        return {}, None, warnings

    first_event = events[0]
    if not isinstance(first_event, dict):
        warnings.append("First item is not an object; skipping rekey")
        return None, None, warnings

    primary_key = determine_primary_key(first_event)
    if not primary_key:
        warnings.append("Could not determine primary key (empty object)")
        return None, None, warnings

    # Verify consistency across events (optional but helpful)
    inconsistent = False
    for idx, ev in enumerate(events):
        if not isinstance(ev, dict):
            warnings.append(f"Item {idx} is not an object; skipping file")
            return None, None, warnings
        pk = determine_primary_key(ev)
        if pk != primary_key:
            inconsistent = True
            break
    if inconsistent:
        warnings.append(
            f"Inconsistent first key across events; expected '{primary_key}' but found different keys"
        )

    rekeyed: Dict[str, Dict[str, Any]] = {}
    for idx, ev in enumerate(events):
        if primary_key not in ev:
            warnings.append(f"Item {idx} missing primary key '{primary_key}'")
            continue
        pk_value = ev[primary_key]
        if not isinstance(pk_value, (str, int)):
            # Force to string to be a valid JSON object key
            pk_value = str(pk_value)
        key_str = str(pk_value)
        if key_str in rekeyed:
            warnings.append(
                f"Duplicate key '{key_str}' encountered; overwriting previous entry"
            )
        rekeyed[key_str] = ev

    return rekeyed, primary_key, warnings


def process_file(path: str, backup_suffix: str, dry_run: bool = False) -> Tuple[bool, List[str]]:
    """Process a single JSON file. Returns (changed, warnings)."""
    warnings: List[str] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            original_text = f.read()
        indent_str = detect_indent_string(original_text)

        data = json.loads(original_text)

        if not isinstance(data, list):
            # Not a list of events; skip
            return False, warnings

        rekeyed, primary_key, rekey_warnings = rekey_events(data)
        warnings.extend(rekey_warnings)
        if rekeyed is None:
            return False, warnings

        # Prepare output JSON with preserved indentation style
        if indent_str is None:
            indent_param = None
        elif indent_str == "\t":
            indent_param = "\t"
        else:
            indent_param = len(indent_str)

        out_text = json.dumps(
            rekeyed,
            ensure_ascii=False,
            indent=indent_param,
            sort_keys=False,
        )
        # Keep trailing newline if original had it
        if original_text.endswith("\n"):
            out_text += "\n"

        if dry_run:
            return True, warnings

        # Backup
        backup_path = path + backup_suffix
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding="utf-8") as bf:
                bf.write(original_text)

        with open(path, "w", encoding="utf-8") as f:
            f.write(out_text)

        return True, warnings

    except Exception as e:
        warnings.append(f"Error processing {path}: {e}")
        return False, warnings


def find_domain_json_files(root: str) -> List[str]:
    pattern = os.path.join(root, "domains", "*", "data", "*.json")
    return sorted(glob.glob(pattern))


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Rekey domains JSON files by first field")
    parser.add_argument(
        "--root",
        default=os.getcwd(),
        help="Repository root (defaults to CWD)",
    )
    parser.add_argument(
        "--backup-suffix",
        default=".backup_rekey",
        help="Suffix to use for backups (default: .backup_rekey)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write changes, only report what would change",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)
    root = os.path.abspath(args.root)
    files = find_domain_json_files(root)
    if not files:
        print("No JSON files found under domains/*/data")
        return 0

    total = 0
    changed = 0
    skipped = 0
    warnings_total: List[str] = []

    for path in files:
        total += 1
        did_change, warnings = process_file(path, args.backup_suffix, dry_run=args.dry_run)
        if did_change:
            changed += 1
            action = "Would update" if args.dry_run else "Updated"
            print(f"{action}: {path}")
        else:
            skipped += 1
            print(f"Skipped: {path}")
        for w in warnings:
            warnings_total.append(f"{os.path.relpath(path, root)}: {w}")

    print(
        f"Processed {total} files: {changed} changed, {skipped} skipped"
    )
    if warnings_total:
        print("Warnings:")
        for w in warnings_total:
            print(f" - {w}")

    return 0


if __name__ == "__main__":
    sys.exit(main())


