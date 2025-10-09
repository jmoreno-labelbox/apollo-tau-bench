#!/usr/bin/env python3
"""
Fix all remaining table getter functions that don't call _convert_db_to_list
"""

from pathlib import Path

def fix_file(file_path, old, new, description):
    """Fix a single pattern in a file"""
    if not file_path.exists():
        return False, "File not found"
    
    content = file_path.read_text()
    
    if old not in content:
        return False, f"Pattern not found"
    
    new_content = content.replace(old, new)
    file_path.write_text(new_content)
    
    return True, f"Fixed {description}"

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    fixes = [
        # dev_ops_6: Fix _loc_table
        {
            'file': base / 'dev_ops_6' / 'tools.py',
            'old': 'def _loc_table(db: dict[str, Any]) -> list[dict[str, Any]]:\n    pass\n    return db.get("loc_strings") or db.get("loc_strongs") or []',
            'new': 'def _loc_table(db: dict[str, Any]) -> list[dict[str, Any]]:\n    pass\n    table = db.get("loc_strings") or db.get("loc_strongs") or []\n    return _convert_db_to_list(table)',
            'desc': 'dev_ops_6 _loc_table'
        },
        # digital_commerce_1: Fix _ensure_table
        {
            'file': base / 'digital_commerce_1' / 'tools.py',
            'old': 'def _ensure_table(db: dict[str, Any], name: str):\n    pass\n    if name not in db:\n        db[name] = []\n    return db[name]',
            'new': 'def _ensure_table(db: dict[str, Any], name: str):\n    pass\n    if name not in db:\n        db[name] = []\n    return _convert_db_to_list(db[name])',
            'desc': 'digital_commerce_1 _ensure_table'
        },
    ]
    
    print("=" * 70)
    print("FIXING REMAINING TABLE GETTER FUNCTIONS")
    print("=" * 70)
    print()
    
    success_count = 0
    for fix in fixes:
        success, msg = fix_file(fix['file'], fix['old'], fix['new'], fix['desc'])
        if success:
            print(f"✅ {msg}")
            success_count += 1
        else:
            print(f"❌ {fix['desc']}: {msg}")
    
    print()
    print("=" * 70)
    print(f"FIXED {success_count} / {len(fixes)} FUNCTIONS")
    print("=" * 70)

if __name__ == "__main__":
    main()

