#!/bin/bash
# Quick script to test and identify 'str' .get() errors

echo "🔍 Testing environments with 'str' object .get() errors..."
echo "════════════════════════════════════════════════════════════════"
echo ""

# List of 19 environments with 'str' .get() errors
ENVS=(
  "consulting_accounting_1"
  "consulting_accounting_4"
  "data_science_2"
  "data_science_5"
  "dev_ops_5"
  "digital_commerce_2"
  "figma_gmail_mcp_pipeline_2"
  "file_system_9"
  "logistics_supply_chain_5"
  "new_hire_mcp_3"
  "project_management_2"
  "rbac_2"
  "real_estate_sales_1"
  "real_estate_sales_4"
  "recipes_1"
  "retail_3"
  "social_media_advertising_2"
  "sports_analytics_2"
  "sports_analytics_3"
)

cd tau

for env in "${ENVS[@]}"; do
  echo "Testing $env..."
  
  # Try to load the environment
  python3 -c "
import sys
sys.path.insert(0, '.')
from tau_bench.envs import get_env
try:
    e = get_env('$env')
    print('  ✅ Environment loads')
except Exception as ex:
    print(f'  ❌ Load error: {ex}')
    sys.exit(1)
" 2>&1 | grep -E "✅|❌"
  
  # Try to run a task
  timeout 30 python3 run.py --env "$env" --end-index 1 2>&1 | \
    grep -E "str.*has no attribute.*get|Error|Exception" | head -3 | \
    sed 's/^/  🔍 /'
  
  echo ""
done

cd ..

echo "════════════════════════════════════════════════════════════════"
echo "📊 Summary: Tested ${#ENVS[@]} environments"
echo ""
echo "Next steps:"
echo "  1. Review the errors above"
echo "  2. Use: ./investigate_failure.sh <env_name>"
echo "  3. Fix the specific tools.py file"
echo "  4. See: ENVIRONMENT_BUG_FIX_GUIDE.md"
echo "════════════════════════════════════════════════════════════════"

