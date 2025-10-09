#!/bin/bash
# Quick smoke test wrapper script with common configurations

set -e

echo "=================================================="
echo "Tau-Bench Quick Smoke Test"
echo "=================================================="
echo ""

# Parse arguments
MODE="${1:-quick}"

case "$MODE" in
  quick)
    echo "🚀 Running QUICK smoke test (5 environments, tool-calling only)..."
    python smoke_test_all_variations.py \
      --limit 5 \
      --output "smoke_test_quick_$(date +%Y%m%d_%H%M%S).json"
    ;;
  
  sample)
    echo "📊 Running SAMPLE smoke test (one env per domain, all strategies)..."
    python smoke_test_all_variations.py \
      --envs retail_1 airline_1 banking_services_1 academic_search_1 \
            career_planner_1 consulting_accounting_1 data_science_1 \
            dev_ops_1 digital_commerce_1 figma_gmail_mcp_pipeline_1 \
      --all-strategies \
      --continue-on-failure \
      --output "smoke_test_sample_$(date +%Y%m%d_%H%M%S).json"
    ;;
  
  domain)
    if [ -z "$2" ]; then
      echo "Error: Please specify a domain pattern"
      echo "Usage: $0 domain <pattern>"
      echo "Example: $0 domain retail"
      exit 1
    fi
    DOMAIN="$2"
    echo "🎯 Running smoke test for domain: $DOMAIN..."
    python smoke_test_all_variations.py \
      --filter-pattern "$DOMAIN" \
      --continue-on-failure \
      --output "smoke_test_${DOMAIN}_$(date +%Y%m%d_%H%M%S).json"
    ;;
  
  full)
    echo "🌍 Running FULL smoke test (all environments, all strategies)..."
    echo "⚠️  This will take a long time!"
    read -p "Continue? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      echo "Cancelled."
      exit 0
    fi
    python smoke_test_all_variations.py \
      --all-strategies \
      --continue-on-failure \
      --timeout 600 \
      --output "smoke_test_full_$(date +%Y%m%d_%H%M%S).json"
    ;;
  
  help|--help|-h)
    echo "Usage: $0 [MODE] [OPTIONS]"
    echo ""
    echo "Modes:"
    echo "  quick     - Test first 5 environments with tool-calling (default)"
    echo "  sample    - Test one environment per domain with all strategies"
    echo "  domain    - Test all environments for a specific domain"
    echo "              Usage: $0 domain <pattern>"
    echo "              Example: $0 domain retail"
    echo "  full      - Test ALL environments with all strategies (slow!)"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 quick"
    echo "  $0 sample"
    echo "  $0 domain retail"
    echo "  $0 full"
    echo ""
    echo "For more options, use the Python script directly:"
    echo "  python smoke_test_all_variations.py --help"
    ;;
  
  *)
    echo "❌ Unknown mode: $MODE"
    echo "Run '$0 help' for usage information"
    exit 1
    ;;
esac

