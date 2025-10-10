#!/usr/bin/env python3
"""
Comprehensive Pattern 1 Fix: 'str' object has no attribute 'get'

This script finds ALL instances of data.get('key', []) and converts them to
list(data.get('key', {}).values()) to handle dictionary data structures.

It doesn't rely on a hardcoded list of keys - it finds them dynamically!
"""

import re
from pathlib import Path
from typing import Dict, Set


def find_and_fix_file(file_path: Path, dry_run: bool = True) -> Dict[str, int]:
    """
    Find and fix all data.get(..., []) patterns in a file.
    Returns dict with stats.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = {}
        
        # Pattern 1: data.get('key', []) or data.get("key", [])
        pattern = r"data\.get\(['\"](\w+)['\"]\s*,\s*\[\]\)"
        
        matches = list(re.finditer(pattern, content))
        
        for match in matches:
            key = match.group(1)
            old_text = match.group(0)
            
            # Determine quote style
            if f"'{key}'" in old_text:
                new_text = f"list(data.get('{key}', {{}}).values())"
            else:
                new_text = f'list(data.get("{key}", {{}}).values())'
            
            # Replace this occurrence
            content = content.replace(old_text, new_text, 1)
            
            fixes[key] = fixes.get(key, 0) + 1
        
        if content != original_content:
            if not dry_run:
                # Backup original
                backup_path = Path(str(file_path) + '.pattern1_backup')
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return {'fixes': sum(fixes.values()), 'keys': fixes}
        
        return {'fixes': 0, 'keys': {}}
    
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return {'fixes': 0, 'keys': {}}


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Comprehensive Pattern 1 fix")
    parser.add_argument("--execute", action="store_true", help="Actually fix files (default is dry run)")
    parser.add_argument("--envs", nargs='+', help="Specific environments to fix (default: all)")
    args = parser.parse_args()
    
    tau_envs = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_envs.exists():
        print(f"❌ Directory not found: {tau_envs}")
        return
    
    mode = "EXECUTING" if args.execute else "DRY RUN"
    print(f"{'='*80}")
    print(f"🔍 Comprehensive Pattern 1 Fix ({mode})")
    print(f"{'='*80}")
    print()
    
    total_files = 0
    total_fixes = 0
    affected_envs = set()
    all_keys = {}
    
    # Get list of environments to process
    env_dirs = []
    if args.envs:
        for env_name in args.envs:
            env_dir = tau_envs / env_name
            if env_dir.exists():
                env_dirs.append(env_dir)
            else:
                print(f"⚠️  Environment not found: {env_name}")
    else:
        env_dirs = [d for d in tau_envs.iterdir() if d.is_dir() and not d.name.startswith('__')]
    
    for env_dir in sorted(env_dirs):
        tools_dir = env_dir / "tools"
        
        if not tools_dir.exists():
            continue
        
        env_fixes = 0
        env_files = 0
        
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == '__init__.py':
                continue
            
            total_files += 1
            env_files += 1
            
            result = find_and_fix_file(tool_file, dry_run=not args.execute)
            
            if result['fixes'] > 0:
                total_fixes += result['fixes']
                env_fixes += result['fixes']
                affected_envs.add(env_dir.name)
                
                for key, count in result['keys'].items():
                    all_keys[key] = all_keys.get(key, 0) + count
                
                if not args.execute:
                    print(f"  📝 {env_dir.name}/{tool_file.name}: {result['fixes']} fixes")
                    for key in result['keys']:
                        print(f"      • {key}")
        
        if env_fixes > 0 and args.execute:
            print(f"  ✅ {env_dir.name}: {env_fixes} fixes in {env_files} files")
    
    print()
    print(f"{'='*80}")
    print("📊 SUMMARY")
    print(f"{'='*80}")
    print()
    print(f"Files scanned:        {total_files}")
    print(f"Total fixes:          {total_fixes}")
    print(f"Environments affected: {len(affected_envs)}")
    print()
    
    if total_fixes > 0:
        print("Affected environments:")
        for env in sorted(affected_envs):
            print(f"  • {env}")
        print()
        
        print(f"Keys fixed ({len(all_keys)} unique):")
        for key, count in sorted(all_keys.items(), key=lambda x: -x[1])[:30]:
            print(f"  • {key}: {count} occurrences")
        if len(all_keys) > 30:
            print(f"  ... and {len(all_keys) - 30} more")
        print()
    
    if not args.execute and total_fixes > 0:
        print("🔄 This was a DRY RUN. To apply fixes, run:")
        if args.envs:
            print(f"   python3 fix_pattern1_comprehensive.py --execute --envs {' '.join(args.envs)}")
        else:
            print("   python3 fix_pattern1_comprehensive.py --execute")
    elif args.execute and total_fixes > 0:
        print("✅ All fixes applied! Backups saved as *.pattern1_backup")
        print()
        print("🧪 Next steps:")
        print("1. Test a few affected environments:")
        for env in list(sorted(affected_envs))[:3]:
            print(f"   cd tau && PYTHONPATH=. python3 run.py --env {env} --end-index 1")
        print()
        print("2. Re-run error analysis:")
        print(f"   python3 run_error_analysis_all_envs.py --run-tests --envs {' '.join(list(sorted(affected_envs))[:5])}")
    else:
        print("✅ No fixes needed - all files already correct!")
    
    print(f"{'='*80}")


if __name__ == "__main__":
    main()

