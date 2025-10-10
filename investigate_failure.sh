#!/bin/bash
# Script to investigate specific environment failures in detail

ENV_NAME="$1"

if [ -z "$ENV_NAME" ]; then
    echo "Usage: ./investigate_failure.sh <env_name>"
    echo ""
    echo "Example: ./investigate_failure.sh retail_1"
    echo ""
    echo "Available environments with failures:"
    cd tau/error_analyses 2>/dev/null || exit 1
    for file in *_error_analysis.json; do
        env=$(basename "$file" _error_analysis.json)
        failures=$(jq '.metadata.total_failures // 0' "$file" 2>/dev/null)
        if [ "$failures" -gt 0 ]; then
            echo "  • $env ($failures failure)"
        fi
    done
    exit 1
fi

ANALYSIS_FILE="tau/error_analyses/${ENV_NAME}_error_analysis.json"

if [ ! -f "$ANALYSIS_FILE" ]; then
    echo "❌ Error: Analysis file not found: $ANALYSIS_FILE"
    exit 1
fi

echo "════════════════════════════════════════════════════════════════"
echo "🔍 FAILURE INVESTIGATION: $ENV_NAME"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Count failures
total=$(jq '[.fault_assignment_analysis[]] | length' "$ANALYSIS_FILE")
agent=$(jq '[.fault_assignment_analysis[] | select(.author == "agent")] | length' "$ANALYSIS_FILE")
env=$(jq '[.fault_assignment_analysis[] | select(.author == "environment")] | length' "$ANALYSIS_FILE")
user=$(jq '[.fault_assignment_analysis[] | select(.author == "user")] | length' "$ANALYSIS_FILE")

echo "📊 FAILURE SUMMARY"
echo "   Total failures:     $total"
echo "   Agent faults:       $agent"
echo "   Environment faults: $env"
echo "   User faults:        $user"
echo ""

if [ "$total" -eq 0 ]; then
    echo "✅ No failures found - environment is passing!"
    exit 0
fi

# Show fault assignments
echo "🎯 FAULT ASSIGNMENT ANALYSIS"
echo "════════════════════════════════════════════════════════════════"
jq -r '.fault_assignment_analysis[] | "
Task ID: \(.task_id)
Author:  \(.author | ascii_upcase)

Description:
\(.description)

────────────────────────────────────────────────────────────────
"' "$ANALYSIS_FILE"

# Show fault type analysis if present
if [ "$agent" -gt 0 ]; then
    echo ""
    echo "🤖 FAULT TYPE ANALYSIS (Agent Issues)"
    echo "════════════════════════════════════════════════════════════════"
    jq -r '.fault_type_analysis[]? | "
Task ID:    \(.task_id)
Fault Type: \(.fault_type | ascii_upcase)

Description:
\(.description)

────────────────────────────────────────────────────────────────
"' "$ANALYSIS_FILE"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "📁 Full details: $ANALYSIS_FILE"
echo "════════════════════════════════════════════════════════════════"

