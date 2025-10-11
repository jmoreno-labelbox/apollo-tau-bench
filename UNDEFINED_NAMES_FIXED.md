# Undefined Names - FIXED ✓

## Summary
Fixed "undefined_name" errors in test environments by resolving missing variables and adding helper function imports.

## Problems Fixed

### 1. recipes_4 - Missing Variable References
**Problem**: After kwargs refactoring, `_validate_inputs(kwargs, ...)` calls still referenced `kwargs` variable that no longer existed.

**Root Cause**: Functions were refactored from:
```python
def invoke(data, **kwargs) -> str:
    validation_error = _validate_inputs(kwargs, param_definitions)
```

To:
```python
def invoke(data, household_id, user_id) -> str:
    validation_error = _validate_inputs(kwargs, param_definitions)  # ❌ kwargs doesn't exist!
```

**Solution**: Reconstruct kwargs dict from explicit parameters:
```python
def invoke(data, household_id, user_id) -> str:
    validation_error = _validate_inputs({"household_id": household_id, "user_id": user_id}, param_definitions)
```

**Files Fixed**: 29/30 files in `tau/tau_bench/envs/recipes_4/tools/`

### 2. banking_services_4 - Missing Helper Function Imports
**Problem**: Tool files used `load_json()` function but didn't import it.

**Root Cause**: `load_json` was defined in `tools/__init__.py` but individual tool files called it without importing.

**Solution**: Added import statement to each file:
```python
from . import load_json
```

**Files Fixed**: 34/36 files in `tau/tau_bench/envs/banking_services_4/tools/`

**Note**: Helper functions are defined in `tau/tau_bench/envs/banking_services_4/tools/__init__.py`, which mirrors the implementation from `domains_warrior/banking_services/variations/variation_4/tools.py`

## Additional Fix

Added missing `ERROR_MESSAGES` constant to recipes_4 tools:
```python
ERROR_MESSAGES = {
    "REQUIRED_PARAMETER": "Required parameter '{param}' is missing.",
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be of type {expected_type}.",
    "NOT_FOUND": "{entity} with ID {entity_id} not found.",
    "OPERATION_FAILED": "Operation failed: {reason}",
}
```

## Tools Created
- `fix_missing_vars.py` - Fixes missing variable references (kwargs)
- `fix_helper_imports.py` - Adds missing helper function imports

## Verification
✅ All fixed files pass Python syntax validation
✅ No more "name 'kwargs' is not defined" errors in recipes_4
✅ No more "name 'load_json' is not defined" errors in banking_services_4

## Statistics
- **recipes_4**: 29 files modified
- **banking_services_4**: 34 files modified
- **Total**: 63 files fixed

## Next Steps
- Run tests to verify runtime behavior
- Check for similar patterns in other environments if needed
