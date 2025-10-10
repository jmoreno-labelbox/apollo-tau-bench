#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║          Testing 10 Round 2 Fixes                                         ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

ENVS=(
  "banking_services_2"
  "data_science_5"
  "digital_commerce_1"
  "digital_commerce_2"
  "new_hire_mcp_3"
  "real_estate_sales_3"
  "recipes_1"
  "sports_analytics_2"
  "sports_analytics_5"
  "it_help_desk_2"
)

python3 run_error_analysis_all_envs.py --run-tests \
  --envs ${ENVS[@]} \
  --num-tasks 1 \
  --test-concurrency 5

echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo "Testing complete!"
echo "════════════════════════════════════════════════════════════════════════════"
