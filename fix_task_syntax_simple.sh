#!/bin/bash
# Fix Task syntax errors by adding missing actions=[] parameters

echo "Fixing Task syntax errors in test files..."

# Fix github_mcp_6/tasks_test.py
echo "Fixing github_mcp_6/tasks_test.py..."
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_6/tasks_test.py

# Fix github_mcp_2/tasks_test.py  
echo "Fixing github_mcp_2/tasks_test.py..."
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_2/tasks_test.py

echo "Done!"
