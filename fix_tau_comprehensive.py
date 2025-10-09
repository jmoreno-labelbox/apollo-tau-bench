#!/usr/bin/env python3
"""
Comprehensive fix for tau/ directory:
1. Convert rules.py to wiki.py (string format)
2. Fix data structure handling (dict -> list conversion)
3. Update env.py to use wiki instead of rules
4. Fix tool invocations
"""

import os
import re
from pathlib import Path

def convert_rules_to_wiki(env_dir: Path):
    """Convert rules.py to wiki.py and change format from list to string."""
    rules_file = env_dir / "rules.py"
    wiki_file = env_dir / "wiki.py"
    
    if not rules_file.exists():
        print(f"  ⚠️  No rules.py in {env_dir.name}")
        return
    
    content = rules_file.read_text()
    
    # Extract the rules content from the list
    if match := re.search(r'RULES\s*=\s*\[(.*?)\]', content, re.DOTALL):
        rules_content = match.group(1).strip()
        # Remove quotes and clean up
        if rules_content.startswith('"') and rules_content.endswith('"'):
            rules_content = rules_content[1:-1]
        elif rules_content.startswith("'") and rules_content.endswith("'"):
            rules_content = rules_content[1:-1]
        
        # Create wiki.py with string format
        wiki_content = f'''WIKI = """
{rules_content}
"""
'''
        wiki_file.write_text(wiki_content)
        print(f"  ✅ Created wiki.py for {env_dir.name}")
    else:
        print(f"  ⚠️  Could not parse RULES from {env_dir.name}")

def fix_env_py(env_dir: Path):
    """Update env.py to import wiki instead of rules."""
    env_file = env_dir / "env.py"
    
    if not env_file.exists():
        return
    
    content = env_file.read_text()
    
    # Replace rules imports with wiki imports
    content = content.replace(
        "from tau_bench.envs." + env_dir.name + ".rules import RULES",
        "from tau_bench.envs." + env_dir.name + ".wiki import WIKI"
    )
    
    # Replace RULES with WIKI in constructor
    content = re.sub(r'rules=RULES', 'wiki=WIKI', content)
    content = re.sub(r'wiki=""', 'wiki=WIKI', content)
    
    env_file.write_text(content)
    print(f"  ✅ Updated env.py for {env_dir.name}")

def add_data_conversion_helper(tools_file: Path):
    """Add helper function to convert dict data to list at the start of tools.py."""
    content = tools_file.read_text()
    
    # Check if helper already exists
    if "_convert_db_to_list" in content:
        return
    
    helper_code = '''

def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

'''
    
    # Insert after imports, before first function/class
    # Find the last import line
    lines = content.split('\n')
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_idx = i + 1
        elif line.strip() == '' and insert_idx > 0:
            insert_idx = i + 1
        elif line.startswith('def ') or line.startswith('class '):
            break
    
    lines.insert(insert_idx, helper_code)
    content = '\n'.join(lines)
    
    # Now update all db.get calls to use the helper
    content = re.sub(
        r'db = data\.get\((\w+|"[^"]+"),\s*\[\]\)',
        r'db = _convert_db_to_list(data.get(\1, {}))',
        content
    )
    content = re.sub(
        r'db = data\.get\((\w+|"[^"]+"),\s*\{\}\)',
        r'db = _convert_db_to_list(data.get(\1, {}))',
        content
    )
    content = re.sub(
        r'db = data\.get\((\w+|"[^"]+"),\s*None\)',
        r'db = _convert_db_to_list(data.get(\1, {}))',
        content
    )
    content = re.sub(
        r'db = data\.get\(([^\)]+)\)(?!\s*\))',
        r'db = _convert_db_to_list(data.get(\1, {}))',
        content
    )
    
    # Also fix cases where database_name is used directly
    content = re.sub(
        r'db = data\.get\(database_name,\s*\[\]\)',
        r'db = _convert_db_to_list(data.get(database_name, {}))',
        content
    )
    content = re.sub(
        r'db = data\.get\(database_name,\s*\{\}\)',
        r'db = _convert_db_to_list(data.get(database_name, {}))',
        content
    )
    content = re.sub(
        r'db = data\.get\(database_name\)(?!\s*\))',
        r'db = _convert_db_to_list(data.get(database_name, {}))',
        content
    )
    
    tools_file.write_text(content)
    print(f"  ✅ Added data conversion helper to {tools_file.parent.name}/tools.py")

def fix_individual_tool_files(tools_dir: Path):
    """Fix individual tool files in the tools/ subdirectory."""
    if not tools_dir.exists():
        return
    
    for tool_file in tools_dir.glob("*.py"):
        if tool_file.name == "__init__.py":
            continue
        
        content = tool_file.read_text()
        
        # Check if it needs the helper function
        if 'data.get(' in content and '_convert_db_to_list' not in content:
            # Add the helper function at the top after imports
            lines = content.split('\n')
            insert_idx = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') or line.startswith('from '):
                    insert_idx = i + 1
                elif line.strip() == '' and insert_idx > 0:
                    insert_idx = i + 1
                elif line.startswith('def ') or line.startswith('class '):
                    break
            
            helper_code = '''

def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db
'''
            
            lines.insert(insert_idx, helper_code)
            content = '\n'.join(lines)
            
            # Fix data.get calls
            content = re.sub(
                r'db = data\.get\(([^,\)]+),\s*\[\]\)',
                r'db = _convert_db_to_list(data.get(\1, {}))',
                content
            )
            content = re.sub(
                r'db = data\.get\(([^,\)]+),\s*\{\}\)',
                r'db = _convert_db_to_list(data.get(\1, {}))',
                content
            )
            content = re.sub(
                r'db = data\.get\(([^,\)]+)\)(?!\s*[,\)])',
                r'db = _convert_db_to_list(data.get(\1, {}))',
                content
            )
            
            tool_file.write_text(content)

def main():
    tau_envs_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_envs_dir.exists():
        print(f"❌ tau/tau_bench/envs directory not found at {tau_envs_dir}")
        return
    
    print("🔧 Starting comprehensive tau/ fixes...\n")
    
    # Process each environment directory
    for env_dir in tau_envs_dir.iterdir():
        if not env_dir.is_dir() or env_dir.name.startswith('_') or env_dir.name == '__pycache__':
            continue
        
        print(f"📦 Processing {env_dir.name}...")
        
        # 1. Convert rules.py to wiki.py
        convert_rules_to_wiki(env_dir)
        
        # 2. Fix env.py
        fix_env_py(env_dir)
        
        # 3. Fix tools.py
        tools_file = env_dir / "tools.py"
        if tools_file.exists():
            add_data_conversion_helper(tools_file)
        
        # 4. Fix individual tool files
        tools_dir = env_dir / "tools"
        if tools_dir.exists():
            fix_individual_tool_files(tools_dir)
        
        print()
    
    print("✅ All fixes completed!")
    print("\nNext steps:")
    print("1. Test with: cd tau && python run.py --env retail_1 --model gpt-4o-mini --model-provider openai --user-model gpt-4o --user-model-provider openai --agent-strategy tool-calling --start-index 0 --end-index 1")
    print("2. Check for any remaining errors")
    print("3. Create zip file of tau/ directory")

if __name__ == "__main__":
    main()

