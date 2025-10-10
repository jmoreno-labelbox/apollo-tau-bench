#!/bin/bash
# Quick test script to verify tau-bench is working with synced tools

cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau

echo "🧪 Quick Test: Running tau-bench with synced environments"
echo "=========================================================="
echo ""
echo "Testing: academic_search_1 (1 task only)"
echo ""

# Run a single task as a smoke test
python3 run.py \
  --env academic_search_1 \
  --model gpt-4o-mini \
  --start-index 0 \
  --end-index 1 \
  --max-concurrency 1

EXIT_CODE=$?

echo ""
echo "=========================================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Test completed!"
    echo ""
    echo "Results saved to: results/"
    echo ""
    echo "Latest result file:"
    ls -lt results/*.json | head -1 | awk '{print "  " $9}'
    echo ""
    echo "Next steps:"
    echo "  1. Check the results file above"
    echo "  2. Try more tasks: python3 run.py --env academic_search_1 --end-index 5"
    echo "  3. Try other environments: python3 run.py --env banking_services_1 --end-index 3"
    echo "  4. See HOW_TO_RUN.md for full documentation"
else
    echo "❌ Test failed with exit code: $EXIT_CODE"
    echo ""
    echo "Common issues:"
    echo "  - Check API keys in .env file"
    echo "  - Make sure dependencies are installed: pip install -e ."
    echo "  - Check error messages above for details"
fi
echo "=========================================================="

