#!/usr/bin/env python3
"""
Restore all copyright comments to standard "# Copyright Sierra" format.
"""

import re
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def restore_copyright_in_file(file_path: Path, dry_run: bool = False) -> bool:
    """Restore copyright comment in a file. Returns True if changed."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        if not lines:
            return False
        
        # Check first line for copyright
        first_line = lines[0]
        
        # Match various copyright formats
        copyright_pattern = r'^#\s*Copyright.*Sierra.*$'
        
        if re.match(copyright_pattern, first_line, re.IGNORECASE):
            if first_line != "# Copyright Sierra":
                # Replace with standard format
                lines[0] = "# Copyright Sierra"
                
                if not dry_run:
                    new_content = '\n'.join(lines)
                    file_path.write_text(new_content, encoding='utf-8')
                
                return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Restore copyright comments to standard format")
    parser.add_argument(
        "--target-dir",
        type=str,
        default="tau/tau_bench/envs",
        help="Target directory to process (default: tau/tau_bench/envs)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=20,
        help="Number of parallel workers (default: 20)"
    )
    args = parser.parse_args()
    
    # Find all Python files
    target_path = Path(__file__).parent / args.target_dir
    if not target_path.exists():
        print(f"Error: Target directory not found: {target_path}")
        return
    
    py_files = list(target_path.rglob("*.py"))
    py_files = [f for f in py_files if '__pycache__' not in str(f)]
    
    print(f"Scanning {len(py_files)} Python files...")
    print(f"Using {args.workers} parallel workers")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified\n")
    
    changed_files = []
    
    def process_file(py_file):
        if restore_copyright_in_file(py_file, args.dry_run):
            rel_path = py_file.relative_to(target_path.parent.parent.parent)
            print(f"{'Would restore' if args.dry_run else 'Restored'}: {rel_path}")
            return py_file
        return None
    
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(process_file, py_file) for py_file in py_files]
        for future in as_completed(futures):
            result = future.result()
            if result:
                changed_files.append(result)
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Files scanned: {len(py_files)}")
    print(f"Copyright comments restored: {len(changed_files)}")
    if args.dry_run:
        print("\nThis was a DRY RUN - no files were modified")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

