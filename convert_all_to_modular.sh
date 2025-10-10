#!/bin/bash
# Convert all environments to modular tools/ structure

cd /Users/josemoreno/Desktop/repos/apollo-tau-bench

echo "🔄 Converting All Environments to Modular Structure"
echo "========================================================"
echo ""

# Get all environment directories (excluding __pycache__ and airline base which is already modular)
ENVS=$(ls -d tau/tau_bench/envs/*/ | grep -v "__pycache__" | grep -v "envs/airline/$" | xargs -n1 basename)

# Count total
TOTAL=$(echo "$ENVS" | wc -l | tr -d ' ')
CURRENT=0
CONVERTED=0
SKIPPED=0
FAILED=0

echo "📊 Found $TOTAL environments to convert"
echo ""
echo "Note: Skipping 'airline' (already modular)"
echo ""

# Ask for confirmation if not in execute mode
if [ "$1" != "--execute" ]; then
    echo "🔍 DRY RUN MODE - No changes will be made"
    echo ""
    echo "This will show what would be converted without making changes."
    echo "To actually convert, run: $0 --execute"
    echo ""
    read -p "Continue with dry run? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
    echo ""
fi

# Create log file
LOG_FILE="conversion_log_$(date +%Y%m%d_%H%M%S).txt"
echo "📝 Logging to: $LOG_FILE"
echo ""

for ENV in $ENVS; do
    CURRENT=$((CURRENT + 1))
    echo "[$CURRENT/$TOTAL] Processing: $ENV"
    
    # Check if tools.py exists (not already converted)
    if [ ! -f "tau/tau_bench/envs/$ENV/tools.py" ]; then
        echo "  ⏭️  Skipped (no tools.py found - may already be modular or different structure)"
        SKIPPED=$((SKIPPED + 1))
        echo "[$CURRENT/$TOTAL] $ENV - SKIPPED (no tools.py)" >> "$LOG_FILE"
        echo ""
        continue
    fi
    
    # Run conversion
    if [ "$1" = "--execute" ]; then
        python3 convert_to_modular_tools.py "$ENV" --execute > /tmp/convert_${ENV}.log 2>&1
    else
        python3 convert_to_modular_tools.py "$ENV" > /tmp/convert_${ENV}.log 2>&1
    fi
    
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "  ✅ Converted successfully"
        CONVERTED=$((CONVERTED + 1))
        echo "[$CURRENT/$TOTAL] $ENV - SUCCESS" >> "$LOG_FILE"
        # Save detailed log
        cat /tmp/convert_${ENV}.log >> "$LOG_FILE"
        echo "" >> "$LOG_FILE"
    else
        echo "  ❌ Failed (see log for details)"
        FAILED=$((FAILED + 1))
        echo "[$CURRENT/$TOTAL] $ENV - FAILED" >> "$LOG_FILE"
        cat /tmp/convert_${ENV}.log >> "$LOG_FILE"
        echo "" >> "$LOG_FILE"
    fi
    
    # Clean up temp log
    rm -f /tmp/convert_${ENV}.log
    echo ""
done

echo "========================================================"
echo "📊 CONVERSION SUMMARY"
echo "========================================================"
echo ""
echo "Total environments: $TOTAL"
echo "✅ Converted:       $CONVERTED"
echo "⏭️  Skipped:         $SKIPPED"
echo "❌ Failed:          $FAILED"
echo ""
echo "📝 Full log saved to: $LOG_FILE"
echo ""

if [ "$1" != "--execute" ]; then
    echo "This was a DRY RUN - no files were modified."
    echo "To actually convert, run:"
    echo "  $0 --execute"
else
    echo "✅ Conversion complete!"
    echo ""
    echo "Next steps:"
    echo "  1. Test a few environments:"
    echo "     cd tau"
    echo "     python3 run.py --env academic_search_1 --end-index 1"
    echo "     python3 run.py --env banking_services_1 --end-index 1"
    echo ""
    echo "  2. If successful, clean up backups:"
    echo "     find tau/tau_bench/envs -name 'tools.py.monolithic' -delete"
    echo ""
    echo "  3. If issues, restore from backups:"
    echo "     find tau/tau_bench/envs -name 'tools.py.monolithic' | while read f; do"
    echo "       dir=\$(dirname \$f)"
    echo "       mv \$f \$dir/tools.py"
    echo "       rm -rf \$dir/tools/"
    echo "     done"
fi

echo "========================================================"

