#!/usr/bin/env python3
"""
Analyze all 667 remaining errors to extract code patterns
"""
import json
import sys
from pathlib import Path
import re

sys.path.insert(0, str(Path(__file__).parent / "tau"))

with open('direct_tool_test_results.json') as f:
    results = json.load(f)

# For each error, find the actual code causing it
patterns_found = set()

for env_name, errors in results.items():
    if not errors:
        continue
    
    tools_file = Path(f"tau/tau_bench/envs/{env_name}/tools.py")
    
    if not tools_file.exists():
        continue
    
    with open(tools_file) as f:
        tools_content = f.read()
    
    for err in errors:
        tool_name = err['tool']
        error_msg = err['error']
        
        # Find the tool class in the file
        match = re.search(rf'class {tool_name}\(Tool\):.*?(?=class \w+\(Tool\):|TOOLS = \[|$)', 
                         tools_content, re.DOTALL)
        
        if match:
            tool_code = match.group(0)
            
            # Extract specific error patterns
            if "'str' object has no attribute 'get'" in error_msg:
                # Find "for X in Y" patterns in this tool
                for_patterns = re.findall(r'for \w+ in (\w+)(?:\s|:|\])', tool_code)
                for var in for_patterns:
                    # Check if this var comes from data.get
                    if f'{var} = data.get(' in tool_code or f'{var} = data[' in tool_code:
                        patterns_found.add(f'for X in {var} (from data)')
            
            elif "'dict' object has no attribute 'append'" in error_msg:
                # Find .append() calls
                append_patterns = re.findall(r'(\w+)\.append\(', tool_code)
                for var in append_patterns:
                    if f'{var} = data.get(' in tool_code:
                        patterns_found.add(f'{var}.append() (from data.get)')

print("UNIQUE CODE PATTERNS CAUSING ERRORS:")
print("="*70)
for i, pattern in enumerate(sorted(patterns_found), 1):
    print(f"{i}. {pattern}")

print()
print(f"Total unique patterns: {len(patterns_found)}")
print("="*70)

