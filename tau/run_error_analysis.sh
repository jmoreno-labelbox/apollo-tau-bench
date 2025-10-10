#!/bin/bash
# Example script to run auto_error_identification.py with a real results file

cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau

# Set PYTHONPATH so tau_bench module can be found
export PYTHONPATH=.

# Run error analysis on academic_search_1 results
# Note: API keys will be automatically loaded from .env file
# Make sure you have a .env file with OPENAI_API_KEY set
OUTPUT_FILE="results/academic_search_1_error_analysis.json"

python3 tau_bench/auto_error_identification.py \
  --platform openai \
  --model gpt-4o \
  --env academic_search_1 \
  --results-path results/tool-calling-gpt-4o-mini-0.0_range_0--1_user-gpt-4o-llm_1009152652.json \
  --output-path "$OUTPUT_FILE" \
  --max-concurrency 3 \
  --max-num-failed-results 10

# Check if the script succeeded by checking if output file was created
if [ -f "$OUTPUT_FILE" ]; then
    echo ""
    echo "✅ Analysis complete! Results saved to $OUTPUT_FILE"
    echo "File size: $(ls -lh "$OUTPUT_FILE" | awk '{print $5}')"
else
    echo ""
    echo "❌ Analysis failed! No output file was created."
    echo "Check the error messages above for details."
    exit 1
fi
