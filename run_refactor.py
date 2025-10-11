#!/usr/bin/env python3
"""Script to run the kwargs refactoring on all tau/**/tools/*.py files."""

import subprocess
import sys
from pathlib import Path

def find_tool_files(base_path: Path):
    """Find all tau/**/tools/*.py files."""
    # Start from tau directory
    tau_path = base_path / "tau"
    if not tau_path.exists():
        print(f"Error: {tau_path} does not exist")
        return []
    
    # Find all .py files in tools directories under tau
    tool_files = []
    for tools_dir in tau_path.rglob("tools"):
        if tools_dir.is_dir():
            for py_file in tools_dir.glob("*.py"):
                tool_files.append(py_file)
    
    return sorted(tool_files)

def main():
    base_path = Path(__file__).parent
    refactor_script = base_path / "refactor_kwargs.py"
    
    if not refactor_script.exists():
        print(f"Error: {refactor_script} not found")
        sys.exit(1)
    
    tool_files = find_tool_files(base_path)
    print(f"Found {len(tool_files)} files to refactor")
    
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    for i, file_path in enumerate(tool_files, 1):
        try:
            print(f"[{i}/{len(tool_files)}] Processing {file_path.relative_to(base_path)}...", end=" ")
            
            # Run the refactor script
            result = subprocess.run(
                [sys.executable, str(refactor_script), str(file_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print("✓")
                success_count += 1
            else:
                print(f"✗ (exit code {result.returncode})")
                if result.stderr:
                    print(f"  Error: {result.stderr[:200]}")
                error_count += 1
                
        except subprocess.TimeoutExpired:
            print("✗ (timeout)")
            error_count += 1
        except Exception as e:
            print(f"✗ ({type(e).__name__}: {e})")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Success: {success_count}")
    print(f"  Errors:  {error_count}")
    print(f"  Total:   {len(tool_files)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

