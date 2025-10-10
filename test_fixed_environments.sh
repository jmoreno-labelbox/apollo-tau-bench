#!/bin/bash

# Test all 29 environments we fixed (Patterns 1, 3, 4, 5)

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║          Testing All 29 Fixed Environments                                ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# All unique environments we fixed
ENVS=(
  # Pattern 1 (16 environments)
  "consulting_accounting_1"
  "data_science_2"
  "data_science_4"
  "data_science_5"
  "digital_commerce_2"
  "file_system_9"
  "logistics_supply_chain_3"
  "new_hire_mcp_3"
  "org_chart_4"
  "real_estate_sales_1"
  "recipes_1"
  "smart_home_1"
  "smart_home_3"
  "social_media_advertising_1"
  "social_media_advertising_2"
  "sports_analytics_3"
  
  # Pattern 4 (additional, not in Pattern 1)
  "banking_services_2"
  "retail_5"
  "data_science_1"
  "recipes_5"
  "smart_home_2"
  "data_science_3"
  "digital_commerce_1"
  "it_help_desk_2"
  "real_estate_sales_3"
  "figma_gmail_mcp_pipeline_3"
  "smart_home_5"
  "sports_analytics_5"
  
  # Pattern 5
  "sports_analytics_2"
)

echo "Total environments to test: ${#ENVS[@]}"
echo ""

# Run error analysis with concurrency
python3 run_error_analysis_all_envs.py --run-tests \
  --envs ${ENVS[@]} \
  --num-tasks 1 \
  --test-concurrency 5 \
  --analysis-concurrency 8

echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo "Test complete! Check comprehensive_report.json for results"
echo "════════════════════════════════════════════════════════════════════════════"
