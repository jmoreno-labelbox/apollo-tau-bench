#!/bin/bash
# Comprehensive fix for Task definitions in test files

echo "Fixing Task definitions in test files..."

# Fix github_mcp_6/tasks_test.py
echo "Fixing github_mcp_6/tasks_test.py..."

# Pattern 1: Fix instruction=("..."), Action( -> instruction=("..."), actions=[ Action(
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_6/tasks_test.py

# Pattern 2: Fix instruction=("..."), Action( -> instruction=("..."), actions=[ Action(
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_6/tasks_test.py

# Fix github_mcp_2/tasks_test.py
echo "Fixing github_mcp_2/tasks_test.py..."

# Pattern 1: Fix instruction=("..."), Action( -> instruction=("..."), actions=[ Action(
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_2/tasks_test.py

# Pattern 2: Fix instruction=("..."), Action( -> instruction=("..."), actions=[ Action(
sed -i '' 's/instruction=(".*"),$/instruction=(".*"),\n        actions=[/g' tau/tau_bench/envs/github_mcp_2/tasks_test.py

echo "Done!"
