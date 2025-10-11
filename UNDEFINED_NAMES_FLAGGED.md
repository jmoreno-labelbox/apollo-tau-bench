# Undefined Names - Pattern 4: Missing Helper Functions

## Summary
4 environments have undefined_name errors due to missing helper function imports or definitions.

---

## 🚨 banking_services_2: `load_json` not found

**Error**: `name 'load_json' is not defined`

**Issue**: Function is not being used in current tools (search returned no results)

**Status**: ⚠️ **NEEDS INVESTIGATION**
- The error mentions `load_json` but no current tool files use it
- May have been removed or refactored
- Check if error is from old test data

**Files to check**:
```bash
# No files currently use load_json in this environment
tau/tau_bench/envs/banking_services_2/tools/*.py
```

**Action needed**: 
1. Check test trajectories to see which tool triggered the error
2. Verify if `load_json` was removed during refactoring
3. If needed, add to `tools/__init__.py` following banking_services_4 pattern

---

## 🚨 banking_services_5: `get_next_account_id` missing import

**Error**: `name 'get_next_account_id' is not defined`

**Root Cause**: Function defined in `tools/__init__.py` but not imported by tool files

**Location**:
```python
# DEFINED HERE:
File: tau/tau_bench/envs/banking_services_5/tools/__init__.py
Line: 46
def get_next_account_id(data, account_type='checking'):
    ...

# USED HERE (without import):
File: tau/tau_bench/envs/banking_services_5/tools/create_new_account_for_customer.py
Line: 22
    account_id = get_next_account_id()  # ❌ Not imported!
```

**Fix Required**:
```python
# Add to create_new_account_for_customer.py
from . import get_next_account_id

# OR at top of file after imports:
# from tau_bench.envs.banking_services_5.tools import get_next_account_id
```

---

## 🚨 dev_ops_4: `_idx_by_id` helper function issues

**Error**: `name '_idx_by_id' is not defined`

**Root Cause**: Helper function `_idx_by_id` is defined locally in some files but not in others

**Locations**:

**DEFINED in these files** (local helper):
```python
File: tau/tau_bench/envs/dev_ops_4/tools/attach_symbolicated_stack_to_run.py
Line: 10-14
def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, row in enumerate(rows):
        if row.get("id") == _id or row.get("run_id") == _id:
            return i
    return None

File: tau/tau_bench/envs/dev_ops_4/tools/complete_automation_run.py
Line: 10-14
def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    ...
```

**USED WITHOUT DEFINITION**:
```python
File: tau/tau_bench/envs/dev_ops_4/tools/get_build_run_details.py  
Line: 6
    idx = _idx_by_id(rows, _id)  # ❌ Function not defined in this file!
```

**Fix Required**:
Option 1: Add `_idx_by_id` helper to each file that uses it
Option 2: Move `_idx_by_id` to `tools/__init__.py` and import from there
```python
# In tools/__init__.py:
def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, row in enumerate(rows):
        if row.get("id") == _id or row.get("run_id") == _id:
            return i
    return None

# Then in files that use it:
from . import _idx_by_id
```

---

## 🚨 retail_5: `get_current_timestamp` not defined

**Error**: `name 'get_current_timestamp' is not defined`

**Root Cause**: Function used in multiple tools but never defined

**Locations using it**:
```python
File: tau/tau_bench/envs/retail_5/tools/update_order_status.py
Line: 29
    'updated_at': get_current_timestamp()  # ❌

File: tau/tau_bench/envs/retail_5/tools/update_tracking_status.py  
Line: 24, 30
    tracking_info['tracking_history'][status] = get_current_timestamp()  # ❌
    'updated_at': get_current_timestamp(),  # ❌

File: tau/tau_bench/envs/retail_5/tools/update_supply_order_status.py
Line: 39
    'updated_at': get_current_timestamp()  # ❌

File: tau/tau_bench/envs/retail_5/tools/create_promotional_campaign.py
Line: 26
    'created_at': get_current_timestamp()  # ❌
```

**Fix Required**:
Add function definition to `tools/__init__.py`:
```python
# In tau/tau_bench/envs/retail_5/tools/__init__.py:
def get_current_timestamp() -> str:
    """Return fixed timestamp for testing consistency."""
    return "2025-08-01T12:00:00Z"  # Or appropriate fixed time

# Then in each file that uses it, add import:
from . import get_current_timestamp
```

---

## Summary Table

| Environment | Missing Function | Location | Files Affected | Fix Type |
|-------------|-----------------|----------|----------------|----------|
| **banking_services_2** | `load_json` | ❓ Unknown | ❓ | Investigate |
| **banking_services_5** | `get_next_account_id` | Defined but not imported | 1 file | Add import |
| **dev_ops_4** | `_idx_by_id` | Missing in 1+ files | 1+ files | Add helper or import |
| **retail_5** | `get_current_timestamp` | Not defined anywhere | 5 files | Define + import |

---

## Recommended Actions

### Priority 1: retail_5 (most files affected)
1. Define `get_current_timestamp()` in `tools/__init__.py`
2. Add imports to all 5 affected files
3. Test that timestamps are consistent

### Priority 2: banking_services_5 (clear fix)
1. Add `from . import get_next_account_id` to `create_new_account_for_customer.py`
2. Verify function signature matches usage

### Priority 3: dev_ops_4 (needs investigation)
1. Find all files using `_idx_by_id`
2. Choose: duplicate helper in each file OR centralize in `__init__.py`
3. Implement chosen approach

### Priority 4: banking_services_2 (needs investigation)
1. Review error analysis and test trajectories
2. Determine if `load_json` is actually still needed
3. If yes, follow banking_services_4 pattern to add it

---

## Files to Review/Modify

```
tau/tau_bench/envs/banking_services_2/tools/__init__.py      # Investigate load_json
tau/tau_bench/envs/banking_services_5/tools/__init__.py      # Already has function
tau/tau_bench/envs/banking_services_5/tools/create_new_account_for_customer.py  # Add import
tau/tau_bench/envs/dev_ops_4/tools/__init__.py               # Add _idx_by_id
tau/tau_bench/envs/dev_ops_4/tools/get_build_run_details.py  # Add import or helper
tau/tau_bench/envs/retail_5/tools/__init__.py                # Define get_current_timestamp
tau/tau_bench/envs/retail_5/tools/update_order_status.py     # Add import
tau/tau_bench/envs/retail_5/tools/update_tracking_status.py  # Add import
tau/tau_bench/envs/retail_5/tools/update_supply_order_status.py  # Add import
tau/tau_bench/envs/retail_5/tools/create_promotional_campaign.py  # Add import
```

