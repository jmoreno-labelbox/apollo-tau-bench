#!/bin/bash
# Quick script to view failure details

echo "🔍 Environment Failures Summary"
echo "════════════════════════════════════════════════"
echo ""

for file in *_error_analysis.json; do
    env_name=$(basename "$file" _error_analysis.json)
    failures=$(jq '.metadata.total_failures // 0' "$file" 2>/dev/null)
    
    if [ "$failures" -gt 0 ]; then
        agent=$(jq '.metadata.failures_due_to_agent // 0' "$file" 2>/dev/null)
        env=$(jq '.metadata.failures_due_to_environment // 0' "$file" 2>/dev/null)
        user=$(jq '.metadata.failures_due_to_user // 0' "$file" 2>/dev/null)
        
        echo "📦 $env_name: $failures failure(s)"
        [ "$agent" -gt 0 ] && echo "   └─ 🤖 Agent: $agent"
        [ "$env" -gt 0 ] && echo "   └─ 🐛 Environment: $env"
        [ "$user" -gt 0 ] && echo "   └─ 👤 User: $user"
        echo ""
    fi
done

echo "════════════════════════════════════════════════"
