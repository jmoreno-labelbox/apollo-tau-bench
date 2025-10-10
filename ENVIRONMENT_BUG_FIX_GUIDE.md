# 🐛 Environment Bug Fix Guide

**Generated:** October 10, 2025  
**Total Environment Bugs:** 50 across 47 environments

---

## 📊 Pattern Summary

| Pattern | Count | % | Priority |
|---------|-------|---|----------|
| **'str' object has no attribute 'get'** | 19 | 38% | 🔥 **#1** |
| **Empty Trajectory (Init Failure)** | 18 | 36% | 🔥 **#2** |
| **Data Validation/Missing Data** | 4 | 8% | ⚠️ **#3** |
| **Undefined Variables/Functions** | 4 | 8% | ⚠️ **#4** |
| **Logic Bugs** | 1 | 2% | ℹ️ **#5** |

---

## 🔥 Priority 1: 'str' object has no attribute 'get' (19 environments)

### Root Cause
**Tools are iterating over dictionary keys (strings) instead of dictionary values (objects).**

This happens when code does:
```python
# ❌ WRONG - iterates over keys (strings)
for item in data['items']:
    name = item.get('name')  # Error: 'str' has no attribute 'get'
```

Instead of:
```python
# ✅ CORRECT - iterates over values (dicts)
for item in data['items'].values():
    name = item.get('name')  # Works!
```

### Affected Environments (19)
- consulting_accounting_1
- consulting_accounting_4
- data_science_2
- data_science_5
- dev_ops_5
- digital_commerce_2
- figma_gmail_mcp_pipeline_2
- file_system_9
- logistics_supply_chain_5
- new_hire_mcp_3
- project_management_2
- rbac_2
- real_estate_sales_1
- real_estate_sales_4
- recipes_1
- retail_3
- social_media_advertising_2
- sports_analytics_2
- sports_analytics_3

### How to Fix

**Step 1: Identify the bug**
```bash
# Run the environment to see the error
cd tau
PYTHONPATH=. python3 run.py --env consulting_accounting_1 --end-index 1

# Look for error: 'str' object has no attribute 'get'
```

**Step 2: Find the problematic code**
```bash
# Search for dict iteration in tools
cd tau/tau_bench/envs/consulting_accounting_1
grep -n "for .* in data\[" tools.py
grep -n "for .* in .*\.get(" tools.py
```

**Step 3: Apply the fix**

The fix pattern is:
```python
# Before:
for item in data['items']:
    result = item.get('name')

# After:
for item in data['items'].values():
    result = item.get('name')
```

Or if it's already using `.values()` but calling it twice:
```python
# Before:
for item in data['items'].values().values():  # Error!
    result = item.get('name')

# After:
for item in list(data['items'].values()):
    result = item.get('name')
```

**Step 4: Test the fix**
```bash
cd tau
PYTHONPATH=. python3 run.py --env consulting_accounting_1 --end-index 1
```

### Example Fix

**File:** `tau/tau_bench/envs/consulting_accounting_1/tools.py`

```python
# ❌ Before (line 45)
def get_invoice_details(invoice_id: str):
    invoices = data.get('invoices', {})
    for invoice in invoices:  # ❌ iterating over keys
        if invoice.get('id') == invoice_id:  # ❌ 'str' has no .get()
            return invoice
    return None

# ✅ After
def get_invoice_details(invoice_id: str):
    invoices = data.get('invoices', {})
    for invoice in invoices.values():  # ✅ iterating over values
        if invoice.get('id') == invoice_id:  # ✅ invoice is a dict
            return invoice
    return None
```

---

## 🔥 Priority 2: Empty Trajectory (18 environments)

### Root Cause
**Environment fails to initialize or load, causing no conversation to occur.**

Common causes:
1. **Syntax errors** preventing module load
2. **Missing imports** causing import errors
3. **Data loading failures** in env.py
4. **Tool registration issues**
5. **Circular import issues**

### Affected Environments (18)
- airline_2
- banking_services_6
- consulting_accounting_5
- dev_ops_1
- dev_ops_2
- digital_commerce_3
- figma_gmail_mcp_pipeline_4
- it_help_desk_5
- project_management_1
- project_management_5
- real_estate_sales_7
- recipes_4
- retail_1
- retail_4
- retail_point_of_sale_and_inventory_system_4
- retail_point_of_sale_and_inventory_system_5
- retail_point_of_sale_and_inventory_system_6
- social_media_advertising_5

### How to Fix

**Step 1: Try to import the environment**
```bash
cd tau
python3 -c "from tau_bench.envs import get_env; env = get_env('retail_1')"
```

If this fails with an error, you've found the problem!

**Step 2: Check for syntax errors**
```bash
cd tau/tau_bench/envs/retail_1
python3 -m py_compile tools.py
python3 -m py_compile env.py
python3 -m py_compile __init__.py
```

**Step 3: Check imports**
```bash
# Look for missing imports
cd tau/tau_bench/envs/retail_1
python3 -c "import tools"
python3 -c "import env"
```

**Step 4: Check the env.py file**
```python
# Common issues in env.py:

# ❌ Missing data import
from .tools import TOOLS
# Missing: from .data import DATA

# ❌ Wrong TASKS import
from .tasks import TASKS  # Should be tasks_test
# Should be: from .tasks_test import TASKS

# ❌ Tool not registered
TOOLS = {
    "tool1": tool1,
    # tool2 defined but not in dict - won't work!
}
```

**Step 5: Run with verbose logging**
```bash
cd tau
PYTHONPATH=. python3 -c "
from tau_bench.envs import get_env
try:
    env = get_env('retail_1')
    print('✅ Environment loaded successfully')
    print(f'Tools: {list(env.tools.keys())}')
    print(f'Tasks: {len(env.tasks)}')
except Exception as e:
    print(f'❌ Failed to load: {e}')
    import traceback
    traceback.print_exc()
"
```

### Common Fixes

**Fix 1: Syntax error**
```bash
# Find and fix syntax errors
cd tau/tau_bench/envs/retail_1
python3 -m compileall .
```

**Fix 2: Missing import**
```python
# env.py - Add missing imports
from .tools import TOOLS
from .data import DATA  # ← Add this if missing
from .tasks_test import TASKS
```

**Fix 3: Tool registration**
```python
# tools.py - Make sure all tools are in TOOLS dict
def my_tool():
    pass

TOOLS = {
    "my_tool": my_tool,  # ← Make sure it's registered
}
```

---

## ⚠️ Priority 3: Data Validation/Missing Data (4 environments)

### Root Cause
**Data is missing from data.json or validation logic is incorrect.**

### Affected Environments (4)
- recipes_5
- smart_home_3
- smart_home_5
- social_media_advertising_1

### How to Fix

**Step 1: Check what data is expected**
```bash
./investigate_failure.sh recipes_5
# Read the error description to understand what data is missing
```

**Step 2: Check data.json**
```bash
cd tau/tau_bench/envs/recipes_5
cat data.json | jq '.recipes' | head -20
```

**Step 3: Add missing data or fix validation**
```python
# Common fix: Add default values
def get_recipe(recipe_id):
    recipes = data.get('recipes', {})
    recipe = recipes.get(recipe_id)
    if recipe is None:
        return {"error": "Recipe not found"}
    # Add default values if needed
    recipe.setdefault('ingredients', [])
    recipe.setdefault('instructions', [])
    return recipe
```

---

## ⚠️ Priority 4: Undefined Variables/Functions (4 environments)

### Root Cause
**Helper functions or variables are referenced but not defined.**

### Affected Environments (4)

**`_fixed_now_iso` not defined:**
- data_science_3

**`get_next_account_id` not defined:**
- banking_services_5

**`_table` not defined:**
- dev_ops_6

**`_json` not defined:**
- recipes_3

### How to Fix

**For `_fixed_now_iso`:**
```python
# Add at top of tools.py
from datetime import datetime

def _fixed_now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()
```

**For `get_next_account_id`:**
```python
# Add helper function
def get_next_account_id(account_type='checking'):
    """Generate next account ID."""
    accounts = data.get('accounts', {})
    max_id = 0
    for acc_id in accounts.keys():
        if account_type in acc_id:
            num = int(acc_id.split('_')[-1])
            max_id = max(max_id, num)
    return f"acc_{account_type}_{max_id + 1}"
```

**For `_table` not defined:**
```python
# Initialize at module level
_table = data.get('table_name', {})
```

**For `_json` not defined:**
```python
# Add import
import json

# Or if it should be a variable:
_json = data.get('json_data', {})
```

---

## ℹ️ Priority 5: Logic Bugs (1 environment)

### Root Cause
**Business logic is incorrectly enforced.**

### Affected Environments (1)
- airline

### Specific Issue
The environment incorrectly enforces a total payment amount of $304 (including travel insurance), even though the user explicitly stated they didn't want insurance. The correct total should be $242.

### How to Fix
```python
# File: tau/tau_bench/envs/airline/tools.py
# Find the payment validation function

def process_payment(amount, include_insurance=False):
    # ❌ Before: Always adds insurance
    total = base_price
    total += insurance_cost  # Always adds!
    
    # ✅ After: Only add if requested
    total = base_price
    if include_insurance:
        total += insurance_cost
    
    if amount != total:
        return {"error": f"Incorrect amount. Expected ${total}"}
```

---

## 🚀 Batch Fix Script

Want to fix multiple environments at once? Use this script:

```bash
#!/bin/bash
# fix_str_get_errors.sh - Fix 'str' object .get() errors

ENVS=(
  "consulting_accounting_1"
  "consulting_accounting_4"
  "data_science_2"
  # ... add all 19 environments
)

for env in "${ENVS[@]}"; do
  echo "Fixing $env..."
  cd tau/tau_bench/envs/$env
  
  # Backup
  cp tools.py tools.py.backup
  
  # Fix: Add .values() where needed
  # This is a simple example - manual review recommended!
  sed -i.bak 's/for \([a-z_]*\) in data\[\([^]]*\)\]:/for \1 in data[\2].values():/g' tools.py
  
  # Test
  cd ../../../../..
  PYTHONPATH=tau python3 -c "from tau_bench.envs import get_env; get_env('$env')" && echo "✅ $env" || echo "❌ $env"
done
```

---

## 📋 Fix Checklist

For each environment you fix:

- [ ] Investigate the specific error
- [ ] Identify the root cause
- [ ] Make the fix
- [ ] Test the environment loads
  ```bash
  cd tau
  python3 -c "from tau_bench.envs import get_env; get_env('<env_name>')"
  ```
- [ ] Test with a real run
  ```bash
  PYTHONPATH=. python3 run.py --env <env_name> --end-index 1
  ```
- [ ] Re-run error analysis
  ```bash
  cd ..
  python3 run_error_analysis_all_envs.py --run-tests --envs <env_name>
  ```
- [ ] Verify fix worked
  ```bash
  ./investigate_failure.sh <env_name>  # Should show 0 failures
  ```

---

## 🎯 Recommended Order

1. **Start with 'str' .get() errors (19 envs)**
   - Most common
   - Easy to fix (add `.values()`)
   - High impact

2. **Fix empty trajectories (18 envs)**
   - Test each env individually
   - Look for import/syntax errors
   - May uncover additional bugs

3. **Fix undefined variables (4 envs)**
   - Quick wins
   - Add missing functions

4. **Fix data validation (4 envs)**
   - Review data.json
   - Add validation logic

5. **Fix logic bugs (1 env)**
   - Case-by-case review

---

## 📊 Progress Tracking

Track your fixes:

```bash
# Check how many environments are fixed
python3 run_error_analysis_all_envs.py --run-tests

# View updated statistics
cd tau/error_analyses
./view_failures.sh | grep "Environment:"
```

**Target:** Reduce environment bugs from 50 → 0

---

## 💡 Pro Tips

1. **Fix similar environments together**
   - retail_1, retail_3, retail_4, retail_6 likely have similar bugs

2. **Use grep to find patterns**
   ```bash
   # Find all dict iterations
   grep -r "for .* in data\[" tau/tau_bench/envs/*/tools.py
   ```

3. **Test frequently**
   - Don't fix 10 environments before testing
   - Fix 1-2, test, repeat

4. **Keep backups**
   ```bash
   cp tools.py tools.py.backup
   ```

5. **Use version control**
   ```bash
   git add tau/tau_bench/envs/*/tools.py
   git commit -m "Fix: 'str' object .get() errors in 19 environments"
   ```

---

## 📞 Need Help?

**For 'str' .get() errors:**
- Look for: `for X in data['Y']:`
- Fix: `for X in data['Y'].values():`

**For empty trajectories:**
- Run: `python3 -c "from tau_bench.envs import get_env; get_env('<env>')"`
- Check for syntax/import errors

**For undefined variables:**
- Search for the variable name
- Add function definition or import

---

**Generated by analyze_env_patterns.py**

