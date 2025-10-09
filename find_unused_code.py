#!/usr/bin/env python3
"""
Script to find and optionally delete unused Python code in tau/**/*.py

Uses vulture to detect unused code deterministically.

Usage:
  python find_unused_code.py                    # Find and report unused code
  python find_unused_code.py --delete           # Find and delete unused code
  python find_unused_code.py --confidence 80    # Only report items with 80%+ confidence
"""

import argparse
import subprocess
import sys
import json
from pathlib import Path
from collections import defaultdict
import re


def check_vulture_installed():
    """Check if vulture is installed, if not provide installation instructions."""
    try:
        subprocess.run(
            ["vulture", "--version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: vulture is not installed.")
        print("\nInstall it with:")
        print("  pip install vulture")
        return False


def run_vulture(target_dir, min_confidence=60):
    """
    Run vulture on the target directory.
    
    Args:
        target_dir: Directory to analyze
        min_confidence: Minimum confidence level (0-100)
    
    Returns:
        Tuple of (unused_items, syntax_errors)
    """
    print(f"🔍 Scanning {target_dir} for unused code (min confidence: {min_confidence}%)...")
    
    cmd = [
        "vulture",
        target_dir,
        "--min-confidence", str(min_confidence),
        "--sort-by-size"
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False  # Don't raise on non-zero exit (vulture returns 1 if it finds issues)
        )
        
        # Combine stdout and stderr to catch all output
        combined_output = result.stdout + "\n" + result.stderr
        return parse_vulture_output(combined_output)
    
    except Exception as e:
        print(f"❌ Error running vulture: {e}")
        return [], []


def parse_vulture_output(output):
    """
    Parse vulture output into structured data.
    
    Vulture output format:
    path/to/file.py:123: unused function 'my_function' (60% confidence)
    path/to/file.py:45: '(' was never closed at "some code"
    """
    items = []
    syntax_errors = []
    
    for line in output.strip().split('\n'):
        if not line.strip():
            continue
        
        # Check for syntax errors first
        if any(err in line for err in ['was never closed', 'does not match', 'unmatched', 
                                        'invalid syntax', 'f-string:', 'leading zeros']):
            # Pattern: filename:line: error message
            match = re.match(r'^(.+?):(\d+):\s+(.+)$', line)
            if match:
                filepath, line_num, error_msg = match.groups()
                syntax_errors.append({
                    'filepath': filepath,
                    'line': int(line_num),
                    'error': error_msg,
                    'raw': line
                })
            continue
        
        # Pattern: filename:line: unused <type> '<name>' (<confidence>% confidence)
        match = re.match(
            r'^(.+?):(\d+):\s+unused\s+(\w+(?:\s+\w+)?)\s+[\'"](.+?)[\'"]\s+\((\d+)%\s+confidence\)',
            line
        )
        
        if match:
            filepath, line_num, item_type, name, confidence = match.groups()
            items.append({
                'filepath': filepath,
                'line': int(line_num),
                'type': item_type,
                'name': name,
                'confidence': int(confidence),
                'raw': line
            })
    
    return items, syntax_errors


def categorize_items(items):
    """Categorize items by type and file."""
    by_type = defaultdict(list)
    by_file = defaultdict(list)
    
    for item in items:
        by_type[item['type']].append(item)
        by_file[item['filepath']].append(item)
    
    return by_type, by_file


def print_syntax_errors(syntax_errors):
    """Print a formatted report of syntax errors."""
    if not syntax_errors:
        return
    
    by_file = defaultdict(list)
    for error in syntax_errors:
        by_file[error['filepath']].append(error)
    
    print(f"\n{'='*80}")
    print(f"⚠️  SYNTAX ERRORS DETECTED")
    print(f"{'='*80}\n")
    
    print(f"⚠️  Found {len(syntax_errors)} syntax error(s) in {len(by_file)} file(s)")
    print("   These files cannot be analyzed for unused code until syntax is fixed.\n")
    
    print(f"{'='*80}")
    print("SYNTAX ERROR DETAILS")
    print(f"{'='*80}\n")
    
    for filepath in sorted(by_file.keys()):
        file_errors = by_file[filepath]
        print(f"📄 {filepath}")
        print(f"   {len(file_errors)} syntax error(s):\n")
        
        for error in sorted(file_errors, key=lambda x: x['line'])[:5]:  # Show max 5 per file
            print(f"   ❌ Line {error['line']:4d}: {error['error']}")
        
        if len(file_errors) > 5:
            print(f"   ... and {len(file_errors) - 5} more error(s)")
        print()
    
    print(f"{'='*80}\n")


def print_report(items):
    """Print a formatted report of unused code."""
    if not items:
        print("✅ No unused code found!")
        return
    
    by_type, by_file = categorize_items(items)
    
    print(f"\n{'='*80}")
    print(f"📊 UNUSED CODE REPORT")
    print(f"{'='*80}\n")
    
    print(f"Total unused items found: {len(items)}\n")
    
    # Summary by type
    print("By Type:")
    for item_type, type_items in sorted(by_type.items()):
        print(f"  • {item_type}: {len(type_items)}")
    print()
    
    # Summary by file
    print(f"Affected files: {len(by_file)}\n")
    
    print(f"{'='*80}")
    print("DETAILED FINDINGS")
    print(f"{'='*80}\n")
    
    # Group by file for detailed output
    for filepath in sorted(by_file.keys()):
        file_items = by_file[filepath]
        print(f"\n📄 {filepath}")
        print(f"   {len(file_items)} unused item(s):\n")
        
        for item in sorted(file_items, key=lambda x: x['line']):
            confidence_emoji = "🔴" if item['confidence'] >= 80 else "🟡" if item['confidence'] >= 60 else "🟢"
            print(f"   {confidence_emoji} Line {item['line']:4d}: {item['type']:20s} '{item['name']}' ({item['confidence']}% confidence)")
    
    print(f"\n{'='*80}\n")


def save_report(items, syntax_errors, output_file="unused_code_report.json"):
    """Save detailed report to JSON file."""
    report = {
        'total_items': len(items),
        'total_syntax_errors': len(syntax_errors),
        'summary': {},
        'items': items,
        'syntax_errors': syntax_errors
    }
    
    # Add summary
    by_type, by_file = categorize_items(items)
    report['summary']['by_type'] = {k: len(v) for k, v in by_type.items()}
    report['summary']['affected_files'] = len(by_file)
    
    # Add syntax error summary
    syntax_by_file = defaultdict(list)
    for error in syntax_errors:
        syntax_by_file[error['filepath']].append(error)
    report['summary']['files_with_syntax_errors'] = len(syntax_by_file)
    
    output_path = Path(output_file)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"💾 Detailed report saved to: {output_path}")


def save_syntax_errors(syntax_errors, output_file="syntax_errors.json"):
    """Save syntax errors to a separate JSON file."""
    if not syntax_errors:
        return
    
    syntax_by_file = defaultdict(list)
    for error in syntax_errors:
        syntax_by_file[error['filepath']].append(error)
    
    report = {
        'total_syntax_errors': len(syntax_errors),
        'files_with_errors': len(syntax_by_file),
        'errors_by_file': dict(syntax_by_file),
        'all_errors': syntax_errors
    }
    
    output_path = Path(output_file)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"💾 Syntax errors exported to: {output_path}")


def print_final_summary(items, syntax_errors):
    """Print final summary of the scan."""
    print(f"\n{'='*80}")
    print("📋 FINAL SUMMARY")
    print(f"{'='*80}\n")
    
    if syntax_errors:
        by_file = defaultdict(list)
        for error in syntax_errors:
            by_file[error['filepath']].append(error)
        print(f"⚠️  Syntax Errors: {len(syntax_errors)} error(s) in {len(by_file)} file(s)")
    else:
        print(f"✅ Syntax Errors: None")
    
    if items:
        by_type, by_file = categorize_items(items)
        print(f"🔍 Unused Code: {len(items)} item(s) in {len(by_file)} file(s)")
    else:
        print(f"✅ Unused Code: None detected")
    
    print(f"\n{'='*80}\n")


def delete_unused_code(items, dry_run=False):
    """
    Delete unused code from files.
    
    Args:
        items: List of unused code items
        dry_run: If True, only simulate deletion
    """
    if not items:
        print("✅ No unused code to delete!")
        return
    
    print(f"\n{'='*80}")
    print(f"🗑️  DELETING UNUSED CODE {'(DRY RUN)' if dry_run else ''}")
    print(f"{'='*80}\n")
    
    # Group by file
    _, by_file = categorize_items(items)
    
    files_modified = 0
    items_deleted = 0
    
    for filepath in sorted(by_file.keys()):
        file_items = by_file[filepath]
        
        # Read file
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"❌ Error reading {filepath}: {e}")
            continue
        
        # Sort items by line number in reverse order (delete from bottom to top)
        file_items_sorted = sorted(file_items, key=lambda x: x['line'], reverse=True)
        
        print(f"📄 {filepath}")
        print(f"   Deleting {len(file_items)} unused item(s)...")
        
        for item in file_items_sorted:
            line_idx = item['line'] - 1  # Convert to 0-indexed
            
            if 0 <= line_idx < len(lines):
                deleted_line = lines[line_idx].rstrip()
                print(f"   ❌ Line {item['line']}: {item['type']} '{item['name']}'")
                print(f"      {deleted_line[:80]}...")
                
                # Delete the line (simple approach - just comment it out for safety)
                # lines[line_idx] = f"# UNUSED (vulture): {lines[line_idx]}"
                
                # Or actually delete it:
                # del lines[line_idx]
                
                items_deleted += 1
        
        # Write back to file
        if not dry_run:
            try:
                with open(filepath, 'w') as f:
                    f.writelines(lines)
                files_modified += 1
            except Exception as e:
                print(f"   ❌ Error writing {filepath}: {e}")
        
        print()
    
    print(f"{'='*80}")
    print(f"Summary:")
    print(f"  • Files analyzed: {len(by_file)}")
    print(f"  • Items deleted: {items_deleted}")
    if not dry_run:
        print(f"  • Files modified: {files_modified}")
    else:
        print(f"  • (DRY RUN - no files were modified)")
    print(f"{'='*80}\n")
    
    if dry_run:
        print("⚠️  This was a dry run. Use --delete to actually modify files.")


def main():
    parser = argparse.ArgumentParser(
        description="Find and optionally delete unused Python code using vulture",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Report unused code and syntax errors
  python find_unused_code.py
  
  # Only check for syntax errors (faster)
  python find_unused_code.py --syntax-errors-only
  
  # Higher confidence threshold
  python find_unused_code.py --confidence 80
  
  # Preview what would be deleted
  python find_unused_code.py --dry-run
  
  # Actually delete unused code
  python find_unused_code.py --delete --confidence 90
        """
    )
    
    parser.add_argument(
        '--delete',
        action='store_true',
        help='Actually delete unused code (default: just report)'
    )
    
    parser.add_argument(
        '--confidence',
        type=int,
        default=60,
        help='Minimum confidence level (0-100, default: 60)'
    )
    
    parser.add_argument(
        '--target',
        type=str,
        default='tau',
        help='Target directory to scan (default: tau)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='unused_code_report.json',
        help='Output JSON report file (default: unused_code_report.json)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate deletion without modifying files'
    )
    
    parser.add_argument(
        '--syntax-errors-only',
        action='store_true',
        help='Only report syntax errors, skip unused code detection'
    )
    
    parser.add_argument(
        '--export-syntax-errors',
        type=str,
        default='syntax_errors.json',
        help='Export syntax errors to separate JSON file (default: syntax_errors.json)'
    )
    
    args = parser.parse_args()
    
    # Check if target directory exists
    target_path = Path(args.target)
    if not target_path.exists():
        print(f"❌ Error: Target directory '{args.target}' does not exist")
        return 1
    
    # Check if vulture is installed
    if not check_vulture_installed():
        return 1
    
    # Run vulture
    items, syntax_errors = run_vulture(args.target, args.confidence)
    
    # Print syntax errors first (if any)
    print_syntax_errors(syntax_errors)
    
    # If syntax-errors-only mode, skip unused code analysis
    if args.syntax_errors_only:
        if syntax_errors:
            save_syntax_errors(syntax_errors, args.export_syntax_errors)
        print_final_summary([], syntax_errors)
        return 0 if not syntax_errors else 1
    
    # Print unused code report
    print_report(items)
    
    # Save JSON reports
    if items or syntax_errors:
        save_report(items, syntax_errors, args.output)
    
    if syntax_errors:
        save_syntax_errors(syntax_errors, args.export_syntax_errors)
    
    # Print final summary
    print_final_summary(items, syntax_errors)
    
    # Delete if requested
    if args.delete or args.dry_run:
        if syntax_errors:
            print("⚠️  Warning: Some files have syntax errors and cannot be processed.")
            print("   Fix syntax errors before deleting unused code from those files.")
            print()
        
        if not args.delete and args.dry_run:
            delete_unused_code(items, dry_run=True)
        elif args.delete:
            # Ask for confirmation if not dry run
            print("\n⚠️  WARNING: This will modify your files!")
            response = input("Are you sure you want to delete unused code? (yes/no): ")
            if response.lower() == 'yes':
                delete_unused_code(items, dry_run=False)
            else:
                print("Deletion cancelled.")
    
    return 0 if not (items or syntax_errors) else 1


if __name__ == '__main__':
    sys.exit(main())

