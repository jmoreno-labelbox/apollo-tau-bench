# Quick Error Analysis Guide - Concurrent Edition

## 🚀 TL;DR - Run All Environments Fast

**Run 1 task per environment across all 122 environments with concurrency:**

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench

# Fast: 3 concurrent tests, 1 task per env (~40 minutes, ~$10)
python3 run_error_analysis_all_envs.py --run-tests \
  --num-tasks 1 \
  --test-concurrency 3 \
  --analysis-concurrency 5
```

---

## ⚙️ Updated Default Settings

- ✅ **1 task per environment** (down from 3)
- ✅ **3 concurrent test workers** (tests 3 envs at once)
- ✅ **5 concurrent analysis workers** (analyzes 5 envs at once)

**Speed improvement:** ~3-5x faster than sequential! 🚀

---

## 🎯 Common Use Cases

### 1. Quick Sample (5 environments, fast)
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --envs academic_search_1 banking_services_1 retail_1 airline_1 project_management_1 \
  --test-concurrency 5
```
**Time:** ~2 minutes | **Cost:** <$1

### 2. All Environments (recommended)
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --test-concurrency 3
```
**Time:** ~40 minutes | **Cost:** ~$10  
**Processing:** 122 environments × 1 task = 122 tasks  
**Parallelism:** 3 tests + 5 analyses running concurrently

### 3. Maximum Speed (higher concurrency)
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --test-concurrency 5 \
  --analysis-concurrency 10
```
**Time:** ~25 minutes | **Cost:** ~$10  
⚠️ **Warning:** May hit rate limits - use with caution

### 4. Conservative (lower concurrency)
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --test-concurrency 1 \
  --analysis-concurrency 1
```
**Time:** ~2 hours | **Cost:** ~$10  
**Best for:** Avoiding rate limits, debugging

---

## 📊 Performance Comparison

| Mode | Concurrency | Time | Cost | When to Use |
|------|-------------|------|------|-------------|
| Sequential | 1 | ~2 hours | ~$10 | Debugging, rate limit concerns |
| Default | 3/5 | ~40 mins | ~$10 | **Recommended** - balanced |
| Fast | 5/10 | ~25 mins | ~$10 | When you need results quickly |
| Quick Sample | 5 envs | ~2 mins | <$1 | Testing, validation |

---

## 🎛️ All Options

```bash
python3 run_error_analysis_all_envs.py \
  --run-tests \                        # Run tests if no results exist
  --num-tasks 1 \                      # Tasks per environment (default: 1)
  --test-concurrency 3 \               # Concurrent test workers (default: 3)
  --analysis-concurrency 5 \           # Concurrent analysis workers (default: 5)
  --envs env1 env2 env3 \              # Specific envs (default: all)
  --skip-analysis                      # Just run tests, no analysis
```

---

## 📈 Expected Timeline (All 122 Environments)

**With default settings (3 test workers, 5 analysis workers):**

```
0:00 - Start
0:20 - ~60 environments tested (3 at a time)
0:40 - All 122 environments tested
0:50 - ~100 environments analyzed (5 at a time)
0:55 - All 122 environments analyzed
✅ Complete!
```

**Output:**
- 122 results files in `tau/results/`
- 122 analysis files in `tau/error_analyses/`
- 1 comprehensive report

---

## 💡 Tips for Concurrent Execution

### ✅ Do:
- Use default settings (3/5) for most cases
- Monitor API usage on OpenAI dashboard
- Let it run in background with `nohup` for all envs
- Check logs if any environment fails

### ❌ Don't:
- Set concurrency too high (>10) - rate limits!
- Run multiple scripts at once - conflicts!
- Interrupt during analysis - may corrupt files

---

## 🐛 Troubleshooting

### "Rate limit exceeded"
**Solution:** Lower concurrency:
```bash
--test-concurrency 1 --analysis-concurrency 2
```

### Output looks jumbled
**Cause:** Multiple threads printing concurrently  
**Solution:** This is normal! Check the final summary for results.

### Some environments failed
**Solution:** Check individual error messages, re-run failed ones:
```bash
python3 run_error_analysis_all_envs.py --run-tests --envs failed_env_1 failed_env_2
```

---

## 📊 Sample Output (Concurrent)

```
🔍 Auto Error Identification - All Environments
================================================================================

Found 122 environments

Using 3 concurrent workers

[1/122] academic_search_1
[2/122] academic_search_2
[3/122] academic_search_3
  Running 1 task(s) for academic_search_1...
  Running 1 task(s) for academic_search_2...
  Running 1 task(s) for academic_search_3...
[4/122] academic_search_4
  ✅ Analysis complete
  ✅ Analysis complete
  ✅ Analysis complete
[5/122] academic_search_5
...

================================================================================
📊 SUMMARY
================================================================================

Total environments:        122
Tests run:                 122
Analyses completed:        118
Skipped (no results):      0
Failed:                    4

Environments with failures:
  • environment_1: 2 failures
  • environment_2: 1 failures
  ...
```

---

## 🎯 Recommended Workflow

### Step 1: Quick Test (5 minutes)
Test a sample to verify everything works:
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --envs academic_search_1 banking_services_1 retail_1 \
  --test-concurrency 3
```

### Step 2: Full Run (40 minutes)
Run all environments:
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --test-concurrency 3 \
  --analysis-concurrency 5
```

### Step 3: Review Results
```bash
cd tau/error_analyses
cat comprehensive_report.json | python3 -m json.tool
```

### Step 4: Fix Issues
Based on findings, fix environment bugs or agent issues.

### Step 5: Re-run Failed Environments
```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --envs failed_env_1 failed_env_2
```

---

## ✅ What Changed

### Before (Sequential)
- 1 environment at a time
- 3 tasks per environment
- ~3-4 hours for all
- Simple but slow

### After (Concurrent)
- **1 task per environment** (faster tests)
- **3 environments tested concurrently** (3x speed)
- **5 environments analyzed concurrently** (5x speed)
- **~40 minutes for all** (5x faster overall)
- Thread-safe logging

---

## 🚀 Ready to Run!

**Default command (recommended):**
```bash
python3 run_error_analysis_all_envs.py --run-tests
```

This will:
- ✅ Run 1 task per environment
- ✅ Test 3 environments concurrently
- ✅ Analyze 5 environments concurrently
- ✅ Complete all 122 environments in ~40 minutes
- ✅ Cost ~$10 in API calls

**Let it run and check back in 40 minutes!** ☕

