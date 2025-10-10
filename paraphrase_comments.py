#!/usr/bin/env python3
"""
Paraphrase all inline comments in Python files using GPT-4o-mini.
Preserves code structure and docstrings, only changes # comments.
"""

import os
import re
from pathlib import Path
from openai import OpenAI
import argparse
from typing import List, Tuple
import time

def extract_comments(content: str) -> List[Tuple[int, str, str]]:
    """
    Extract inline comments from Python code.
    Returns list of (line_number, full_line, comment_text)
    """
    lines = content.split('\n')
    comments = []
    
    for i, line in enumerate(lines):
        # Skip docstrings and empty lines
        if '"""' in line or "'''" in line:
            continue
        
        # Find inline comments (not in strings)
        match = re.search(r'(?<!["\'])#\s*(.+)$', line)
        if match:
            comment_text = match.group(1).strip()
            # Skip special comments
            if not any(comment_text.startswith(x) for x in ['!', 'type:', 'noqa', 'pylint:', 'pragma:']):
                comments.append((i, line, comment_text))
    
    return comments

def paraphrase_comment(comment: str, client: OpenAI, max_retries: int = 3) -> str:
    """Use GPT-4o-mini to paraphrase a comment with retry logic."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a code comment paraphraser. Rewrite the given comment to express the same meaning with different wording. Keep it concise and technical. Return ONLY the paraphrased comment text, no quotes or extra text."},
                    {"role": "user", "content": comment}
                ],
                temperature=0.7,
                max_tokens=100,
                timeout=30.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"  Retry {attempt + 1}/{max_retries} after error: {str(e)[:50]}")
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print(f"  Failed after {max_retries} attempts: {str(e)[:50]}")
                return comment
    return comment

def process_file(file_path: Path, client: OpenAI, dry_run: bool = False) -> Tuple[int, bool]:
    """Process a single Python file. Returns (num_changes, success)."""
    try:
        content = file_path.read_text(encoding='utf-8')
        comments = extract_comments(content)
        
        if not comments:
            return 0, True
        
        print(f"\n  Processing: {file_path.relative_to(file_path.parent.parent.parent.parent)}")
        print(f"  Found {len(comments)} comments to paraphrase")
        
        lines = content.split('\n')
        changes = 0
        
        for line_num, full_line, original_comment in comments:
            # Paraphrase the comment
            paraphrased = paraphrase_comment(original_comment, client)
            
            if paraphrased != original_comment:
                # Replace the comment in the line
                # Find where the # starts
                comment_pos = full_line.rfind('#')
                if comment_pos != -1:
                    new_line = full_line[:comment_pos] + '# ' + paraphrased
                    lines[line_num] = new_line
                    changes += 1
                    
                    if not dry_run:
                        print(f"    Line {line_num + 1}:")
                        print(f"      Old: # {original_comment[:60]}...")
                        print(f"      New: # {paraphrased[:60]}...")
            
            # Rate limiting - increased to avoid hitting limits
            time.sleep(0.5)
        
        if not dry_run and changes > 0:
            # Write back the modified content
            new_content = '\n'.join(lines)
            file_path.write_text(new_content, encoding='utf-8')
            print(f"  Saved {changes} changes")
        
        return changes, True
        
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return 0, False

def main():
    parser = argparse.ArgumentParser(description="Paraphrase inline comments in Python files")
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
        "--limit",
        type=int,
        default=None,
        help="Limit number of files to process (for testing)"
    )
    args = parser.parse_args()
    
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        return
    
    client = OpenAI(api_key=api_key)
    
    # Find all Python files
    target_path = Path(__file__).parent / args.target_dir
    if not target_path.exists():
        print(f"Error: Target directory not found: {target_path}")
        return
    
    py_files = list(target_path.rglob("*.py"))
    
    # Filter out __pycache__ and __init__.py
    py_files = [f for f in py_files if '__pycache__' not in str(f)]
    
    if args.limit:
        py_files = py_files[:args.limit]
    
    print(f"Found {len(py_files)} Python files to process")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified\n")
    
    total_changes = 0
    files_processed = 0
    files_failed = 0
    
    for py_file in py_files:
        changes, success = process_file(py_file, client, args.dry_run)
        total_changes += changes
        if success:
            files_processed += 1
        else:
            files_failed += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Files processed: {files_processed}")
    print(f"Files failed: {files_failed}")
    print(f"Total comments paraphrased: {total_changes}")
    if args.dry_run:
        print("\nThis was a DRY RUN - no files were modified")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

