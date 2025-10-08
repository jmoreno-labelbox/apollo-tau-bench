#!/bin/bash

# Simple sed replacements that preserve file structure

for f in \
  "airline/variations/variation_5/tasks_test.py" \
  "banking_services/variations/variation_2/tasks_test.py" \
  "career_planner/variations/variation_4/tasks_test.py" \
  "career_planner/variations/variation_5/tasks_test.py" \
  "consulting_accounting/variations/variation_5/tasks_test.py" \
  "file_system/variations/variation_1/tasks_test.py" \
  "rbac/variations/variation_4/tasks_test.py"; do
  
  # Only replace single-line outputs statements
  # outputs={...} -> outputs=[]
  # outputs=[...] -> outputs=[]
  # But keep outputs=[] as is
  
  python3 << EOF
from pathlib import Path
f = Path("$f")
lines = f.read_text().split('\n')
new_lines = []
skip_mode = False
skip_depth = 0

for line in lines:
    # Skip annotator lines
    if 'annotator=' in line.strip() and line.strip().startswith('annotator='):
        continue
    
    # Handle instruction=( ... ), tuples
    if 'instruction=(' in line and line.strip().startswith('instruction=('):
        # Replace ( with " and ), with ",
        line = line.replace('instruction=(', 'instruction="').replace('),', '",')
        new_lines.append(line)
    # Handle single-line outputs
    elif line.strip().startswith('outputs=') and not skip_mode:
        indent = len(line) - len(line.lstrip())
        if 'outputs=[]' in line:
            new_lines.append(line)
        elif 'outputs={' in line or 'outputs=[' in line:
            # Check if multi-line
            open_count = line.count('{') + line.count('[')
            close_count = line.count('}') + line.count(']')
            if open_count == close_count:
                # Single line
                new_lines.append(' ' * indent + 'outputs=[]')
            else:
                # Multi-line - start skip
                skip_mode = True
                skip_depth = open_count - close_count
                new_lines.append(' ' * indent + 'outputs=[]')
        else:
            new_lines.append(line)
    elif skip_mode:
        # Skip lines inside outputs structure
        skip_depth += line.count('{') + line.count('[') - line.count('}') - line.count(']')
        if skip_depth <= 0:
            skip_mode = False
    else:
        new_lines.append(line)

f.write_text('\n'.join(new_lines))
print(f"✓ Fixed {Path('$f').name}")
EOF

done
