# Cleanup Summary: Removed Unused tasks.py Files

## Why Both tasks.py and tasks_test.py Existed

**TL;DR:** `tasks.py` files were unused leftovers with the wrong format. The runtime only uses `tasks_test.py`.

### The Problem

The codebase had **two versions** of task definitions in each environment:

1. **`tasks.py`** ❌ (Unused, wrong format)
   - Lowercase variable: `tasks = [...]`
   - Plain dictionaries
   - Used `"arguments"` key instead of `"kwargs"`
   - Invalid Python syntax in outputs field
   - **Never imported by any env.py file**

2. **`tasks_test.py`** ✅ (Active, correct format)
   - Uppercase variable: `TASKS = [...]`
   - Proper Pydantic models: `Task()` and `Action()`
   - Uses `kwargs` parameter
   - Valid Python syntax
   - **Imported by all 123 env.py files**

### Example Comparison

**Bad format (tasks.py):**
```python
tasks = [
    {
        "annotator": 0,
        "user_id": "task_01",
        "actions": [
            {
                "name": "SearchCustomer",
                "arguments": {"name": "John"}  # Wrong key
            }
        ],
        "outputs": [
            "balance": 100  # Invalid syntax!
        ]
    }
]
```

**Correct format (tasks_test.py):**
```python
from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_01",
        actions=[
            Action(
                name="SearchCustomer",
                kwargs={"name": "John"}  # Correct key
            )
        ],
        outputs=[]  # Valid list of strings
    )
]
```

### What env.py Files Import

**All 123 environments** import from `tasks_test.py`:
```python
# From tau/tau_bench/envs/*/env.py
match task_split:
    case "test":
        from tau_bench.envs.banking_services_6.tasks_test import TASKS as tasks
```

## What Was Done

### 1. Created Cleanup Script: `cleanup_unused_tasks.py`

The script:
- ✅ Finds all `tasks.py` files in `tau/tau_bench/envs/*/`
- ✅ Verifies they're NOT imported by `env.py` files
- ✅ Deletes them (with `--delete` flag)
- ✅ Reports what was deleted

**Usage:**
```bash
# Preview mode (no deletion)
python3 cleanup_unused_tasks.py

# Actually delete the files
python3 cleanup_unused_tasks.py --delete
```

### 2. Executed Cleanup

**Results:**
- ✅ Successfully deleted **123 unused tasks.py files**
- ✅ Verified all **123 tasks_test.py files** remain
- ✅ Tested multiple environments - all work correctly
- ✅ No files need to be renamed (runtime already uses correct names)

### 3. Verification

**Before cleanup:**
```bash
$ find tau/tau_bench/envs -name "tasks.py" -type f | wc -l
123

$ find tau/tau_bench/envs -name "tasks_test.py" -type f | wc -l
123
```

**After cleanup:**
```bash
$ find tau/tau_bench/envs -name "tasks.py" -type f | wc -l
0

$ find tau/tau_bench/envs -name "tasks_test.py" -type f | wc -l
123
```

**Environment tests:**
```python
from tau_bench.envs.banking_services_6 import MockBankingServicesDomainEnv
from tau_bench.envs.airline_1 import MockAirlineDomainEnv

# Both load tasks successfully:
# ✅ banking_services_6: 100 tasks loaded, current task: task_01
# ✅ airline_1: 100 tasks loaded, current task: task_001
```

## Summary

- **Deleted:** 123 unused `tasks.py` files with wrong format
- **Kept:** 123 correct `tasks_test.py` files (in use by runtime)
- **Renamed:** None (runtime already uses correct file names)
- **Status:** ✅ All environments work correctly after cleanup

## Key Takeaway

The runtime environment **already used the correct files** (`tasks_test.py`). The `tasks.py` files were orphaned leftovers from an old format that were never actually used by the application.

