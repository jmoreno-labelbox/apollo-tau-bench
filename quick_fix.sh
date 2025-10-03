#!/bin/bash

# Fix 1: Restore file_system/variation_1 from earlier backup
cp domains/file_system/variations/variation_1/tasks_test.py.backup3 domains/file_system/variations/variation_1/tasks_test.py
echo "✓ Restored file_system/variation_1"

# Fix 2-3: Delete problematic tools/__init__.py and let env.py import directly from tools.py
# For github_mcp/variation_7
rm -rf domains/github_mcp/variations/variation_7/tools
echo "✓ Removed github_mcp/variation_7/tools/ directory"

# For sports_analytics/variation_5
rm -rf domains/sports_analytics/variations/variation_5/tools  
echo "✓ Removed sports_analytics/variation_5/tools/ directory"

# Fix 4: Check rbac/variation_4 for extra fields
echo "✓ Checking rbac/variation_4..."
grep -n "Task(" domains/rbac/variations/variation_4/tasks_test.py | head -3
