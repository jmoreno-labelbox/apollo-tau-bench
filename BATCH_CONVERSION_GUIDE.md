# Batch Conversion Guide: All Environments to Modular Structure

This guide explains how to convert all 121 environments from monolithic `tools.py` to modular `tools/` structure.

---

## 🎯 Quick Start

### 1. Preview (Dry Run)
See what will be converted without making changes:

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench
./convert_all_to_modular.sh
```

### 2. Execute Conversion
Actually convert all environments:

```bash
./convert_all_to_modular.sh --execute
```

### 3. Test
Verify a few environments work:

```bash
cd tau
python3 run.py --env academic_search_1 --end-index 1
python3 run.py --env banking_services_1 --end-index 1
python3 run.py --env retail_1 --end-index 1
```

### 4. Clean Up (If Successful)
Remove backup files:

```bash
find tau/tau_bench/envs -name 'tools.py.monolithic' -delete
```

---

## 📋 What the Batch Script Does

### Step-by-Step Process

1. **Scans** all environments in `tau/tau_bench/envs/`
2. **Excludes**:
   - `__pycache__` (not an environment)
   - `airline` (already modular)
3. **For each environment**:
   - Checks if `tools.py` exists
   - Runs `convert_to_modular_tools.py`
   - Logs success/failure
4. **Reports** summary statistics
5. **Creates** detailed log file

---

## 📊 Expected Results

### Before Conversion
```
academic_search_1/
├── env.py
├── tools.py          ← 40-200KB monolithic file
├── data.py
├── tasks_test.py
└── wiki.py
```

### After Conversion
```
academic_search_1/
├── env.py
├── tools/            ← New modular directory
│   ├── __init__.py
│   ├── search_users.py
│   ├── create_log_entry.py
│   └── ... (20+ individual tool files)
├── tools.py.monolithic  ← Backup of original
├── data.py
├── tasks_test.py
└── wiki.py
```

---

## 🔍 Monitoring Progress

The script provides real-time progress:

```
🔄 Converting All Environments to Modular Structure
========================================================

📊 Found 121 environments to convert

[1/121] Processing: academic_search_1
  ✅ Converted successfully

[2/121] Processing: academic_search_2
  ✅ Converted successfully

[3/121] Processing: academic_search_3
  ✅ Converted successfully

...

========================================================
📊 CONVERSION SUMMARY
========================================================

Total environments: 121
✅ Converted:       120
⏭️  Skipped:         1
❌ Failed:          0

📝 Full log saved to: conversion_log_20251010_160230.txt
```

---

## 🔄 Rollback Instructions

If something goes wrong, restore everything:

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench

# Restore all backups
find tau/tau_bench/envs -name 'tools.py.monolithic' | while read f; do
    dir=$(dirname $f)
    echo "Restoring: $dir"
    mv $f $dir/tools.py
    rm -rf $dir/tools/
    # Restore env.py if needed
    if [ -f "$dir/env.py.backup" ]; then
        mv $dir/env.py.backup $dir/env.py
    fi
done

echo "✅ All environments restored to monolithic structure"
```

---

## ⚠️ Important Notes

### What Gets Modified

For each environment:
1. ✅ Creates `tools/` directory with individual files
2. ✅ Backs up `tools.py` → `tools.py.monolithic`
3. ✅ Updates `env.py` imports (`TOOLS` → `ALL_TOOLS`)
4. ❌ **Does NOT delete** original `tools.py` (creates backup)

### Safety Features

- ✅ **Dry run by default** - Preview before executing
- ✅ **Backups created** - Original files preserved
- ✅ **Detailed logging** - Every action recorded
- ✅ **Error handling** - Failed conversions don't stop the batch
- ✅ **Skips already modular** - Won't re-process

### Environments That Will Be Skipped

- `airline` (already modular - has `tools/` directory)
- Any environment without `tools.py` (edge cases)

---

## 🧪 Testing Strategy

### Test a Sample First

Before converting all environments, test on a few:

```bash
# Convert just one environment
python3 convert_to_modular_tools.py academic_search_1 --execute

# Test it
cd tau
python3 run.py --env academic_search_1 --end-index 1

# If successful, proceed with batch
cd ..
./convert_all_to_modular.sh --execute
```

### Comprehensive Testing

After batch conversion, test multiple domains:

```bash
cd tau

# Test different domain types
python3 run.py --env academic_search_1 --end-index 1
python3 run.py --env airline_1 --end-index 1
python3 run.py --env banking_services_1 --end-index 1
python3 run.py --env career_planner_1 --end-index 1
python3 run.py --env data_science_1 --end-index 1
python3 run.py --env retail_1 --end-index 1
```

---

## 📈 Performance Impact

### File System
- **Before:** 121 files × ~100KB = ~12MB
- **After:** 121 dirs × ~25 files × ~3KB = ~9MB + 12MB backups = ~21MB total

### Git
- Better diffs (changes isolated to individual tool files)
- More files to track (but better organized)

### IDE
- Faster file navigation
- Better search performance
- Easier to find specific tools

---

## 🤔 FAQ

### Q: Will this break anything?
**A:** No, if conversion succeeds. The functionality is identical. Test before cleaning up backups.

### Q: Can I convert just some environments?
**A:** Yes, use the individual conversion script:
```bash
python3 convert_to_modular_tools.py <env_name> --execute
```

### Q: What if a conversion fails?
**A:** The batch script continues with other environments. Check the log file for details. Failed environments remain unchanged.

### Q: Can I go back to monolithic?
**A:** Yes, restore from `.monolithic` backups (see Rollback Instructions above).

### Q: How long does batch conversion take?
**A:** Approximately 1-2 minutes for all 121 environments (depends on system speed).

### Q: Should I commit the modular structure?
**A:** That's up to you:
- **Commit modular** if you want better organization and git history
- **Keep monolithic** if you prioritize simplicity and single-file syncing

---

## 🚀 Complete Workflow

```bash
# 1. Navigate to project
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench

# 2. Preview conversion (dry run)
./convert_all_to_modular.sh

# 3. Execute conversion
./convert_all_to_modular.sh --execute

# 4. Test multiple environments
cd tau
python3 run.py --env academic_search_1 --end-index 1
python3 run.py --env banking_services_1 --end-index 1
python3 run.py --env retail_1 --end-index 1

# 5. If all tests pass, clean up backups
cd ..
find tau/tau_bench/envs -name 'tools.py.monolithic' -delete

# 6. Optional: Commit changes
git status
git add tau/tau_bench/envs/
git commit -m "Convert all environments to modular tools/ structure"
```

---

## 📝 Log File Format

The script creates a detailed log with timestamps:

```
conversion_log_20251010_160230.txt
```

**Contents:**
```
[1/121] academic_search_1 - SUCCESS
🔍 Analyzing academic_search_1/tools.py...
✅ Found 23 tool classes
✅ Created directory: envs/academic_search_1/tools
...

[2/121] academic_search_2 - SUCCESS
...

[42/121] some_env_5 - FAILED
Error: ...
```

---

## ✅ Benefits of Modular Structure

After conversion, you'll have:

✅ **Better Organization** - One tool per file  
✅ **Easier Navigation** - Find tools quickly  
✅ **Better Git History** - Isolated changes  
✅ **Parallel Development** - Multiple developers can work simultaneously  
✅ **Clearer Code** - Smaller, focused files  
✅ **IDE Performance** - Faster loading and searching  

---

## 📚 Related Documentation

- `convert_to_modular_tools.py` - Individual environment conversion
- `MODULAR_TOOLS_GUIDE.md` - Detailed guide on modular structure
- `HOW_TO_RUN.md` - How to run environments after conversion

---

## 🎉 Summary

```bash
# One command to convert everything:
./convert_all_to_modular.sh --execute

# Test it works:
cd tau && python3 run.py --env academic_search_1 --end-index 1

# Clean up:
find tau/tau_bench/envs -name 'tools.py.monolithic' -delete
```

That's it! All 121 environments converted to modular structure! 🚀

