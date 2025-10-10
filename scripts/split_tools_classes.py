#!/usr/bin/env python3

import argparse
import ast
import os
import re
from pathlib import Path
from typing import List, Tuple, Set


def to_snake_case(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    snake = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    return snake


def extract_segments_by_nodes(lines: List[str], nodes: List[ast.AST]) -> List[str]:
    segments: List[str] = []
    for node in nodes:
        start = getattr(node, "lineno", None)
        end = getattr(node, "end_lineno", None)
        if start is None or end is None:
            continue
        # Convert to 0-based index
        seg = lines[start - 1 : end]
        segments.extend(seg)
    return segments


def split_tools_file(tools_path: Path) -> None:
    text = tools_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Parse AST
    tree = ast.parse(text)

    # Collect top-level imports and classes
    import_nodes: List[ast.AST] = []
    class_nodes: List[ast.ClassDef] = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            import_nodes.append(node)
        elif isinstance(node, ast.ClassDef):
            class_nodes.append(node)

    if not class_nodes:
        return

    # Extract import text segments
    import_text_lines = extract_segments_by_nodes(lines, import_nodes)
    import_text = "\n".join(import_text_lines)

    # Rewrite Tool import
    # Remove any 'from domains.dto import Tool' lines entirely, we'll add the new one
    new_import_lines: List[str] = []
    for line in import_text.splitlines():
        if re.match(r"^\s*from\s+domains\.dto\s+import\s+Tool(\s*,.*)?\s*$", line):
            continue
        new_import_lines.append(line)

    # Always include the new Tool import
    new_import_lines.insert(0, "from tau_bench.envs.tool import Tool")

    # Deduplicate while preserving order
    seen: Set[str] = set()
    dedup_imports: List[str] = []
    for l in new_import_lines:
        if not l.strip():
            continue
        if l not in seen:
            dedup_imports.append(l)
            seen.add(l)

    # Prepare destination directory
    dest_dir = tools_path.parent / "tools"
    dest_dir.mkdir(parents=True, exist_ok=True)
    init_file = dest_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("", encoding="utf-8")

    # For each class, write to its own file
    for cls in class_nodes:
        start = getattr(cls, "lineno", None)
        end = getattr(cls, "end_lineno", None)
        if start is None or end is None:
            continue
        class_source = "\n".join(lines[start - 1 : end]) + "\n"
        class_filename = to_snake_case(cls.name) + ".py"
        out_path = dest_dir / class_filename

        # Compose file content
        content_lines: List[str] = []
        content_lines.extend(dedup_imports)
        content_lines.append("")
        content_lines.append(class_source.rstrip())
        content_lines.append("")
        out = "\n".join(content_lines)
        out_path.write_text(out, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Split tools.py or tasks_test.py into per-class files with snake_case names")
    parser.add_argument(
        "--root",
        type=str,
        default=str(Path(__file__).resolve().parent.parent),
        help="Repo root (defaults to project root)",
    )
    parser.add_argument(
        "--target",
        type=str,
        choices=["domains", "tau", "both"],
        default="domains",
        help="Target directory: domains, tau (tau_bench/envs), or both",
    )
    parser.add_argument(
        "--file-type",
        type=str,
        choices=["tools", "tasks", "both"],
        default="tools",
        help="File type to process: tools.py, tasks_test.py, or both",
    )
    args = parser.parse_args()

    root = Path(args.root)
    files_to_process = []
    
    if args.target in ["domains", "both"]:
        # Check both domains_apollo and domains_warrior
        for domains_dir_name in ["domains", "domains_apollo", "domains_warrior"]:
            domains_dir = root / domains_dir_name
            if domains_dir.exists():
                if args.file_type in ["tools", "both"]:
                    files_to_process.extend(list(domains_dir.glob("**/variations/**/tools.py")))
                if args.file_type in ["tasks", "both"]:
                    files_to_process.extend(list(domains_dir.glob("**/variations/**/tasks_test.py")))
    
    if args.target in ["tau", "both"]:
        # Process tau/tau_bench/envs
        tau_envs = root / "tau" / "tau_bench" / "envs"
        if tau_envs.exists():
            if args.file_type in ["tools", "both"]:
                files_to_process.extend(list(tau_envs.glob("*/tools.py")))
            if args.file_type in ["tasks", "both"]:
                files_to_process.extend(list(tau_envs.glob("*/tasks_test.py")))

    print(f"Found {len(files_to_process)} files to process")
    
    processed = 0
    failed = 0
    for p in files_to_process:
        try:
            split_tools_file(p)
            print(f"✓ Processed {p.relative_to(root)}")
            processed += 1
        except Exception as e:
            print(f"✗ Failed to process {p.relative_to(root)}: {e}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {processed} processed, {failed} failed")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()


