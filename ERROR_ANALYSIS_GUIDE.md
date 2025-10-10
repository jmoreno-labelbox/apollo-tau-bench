# Error Analysis Guide for All Environments

## 📋 Overview

The `run_error_analysis_all_envs.py` script runs automated error identification across all tau-bench environments.

---

## ⚙️ Options

### Option 1: Analyze Existing Results Only (Fast, Free)
Analyzes environments that already have results files.

```bash
python3 run_error_analysis_all_envs.py
```

**Time:** 5-10 minutes  
**Cost:** ~$1-2 (only GPT-4o for analysis)  
**Environments:** Only those with existing results (~3-5)

---

### Option 2: Specific Environments (Recommended)
Test and analyze a curated subset of environments.

```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --envs academic_search_1 banking_services_1 retail_1 \
         airline_1 data_science_1 project_management_1
```

**Time:** 10-15 minutes  
**Cost:** ~$2-3  
**Environments:** 6 representative domains

---

### Option 3: All Environments (Expensive, Slow)
Test and analyze all 122 environments.

```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 3
```

**Time:** 1.5-3 hours  
**Cost:** ~$15-30  
**Environments:** All 122

**⚠️ Warning:** This will make ~500-1000 API calls to OpenAI.

---

### Option 4: Just Run Tests (No Analysis)
Generate results files without running error analysis.

```bash
python3 run_error_analysis_all_envs.py --run-tests --skip-analysis
```

Then analyze later:
```bash
python3 run_error_analysis_all_envs.py
```

---

## 📊 What Gets Generated

### Per Environment
- **Results file:** `results/tool-calling-...-{env}.json`
- **Analysis file:** `error_analyses/{env}_error_analysis.json`

### Comprehensive Report
- **Location:** `error_analyses/comprehensive_report.json`
- **Contents:**
  - Total environments analyzed
  - Failure counts by fault author (user/agent/environment)
  - Fault type distributions
  - Summary statistics

---

## 🎯 Recommended Workflow

### 1. Start Small (Representative Sample)
Test 5-10 diverse environments:

```bash
python3 run_error_analysis_all_envs.py --run-tests \
  --envs academic_search_1 banking_services_1 retail_1 \
         airline_1 career_planner_1 project_management_1 \
         digital_commerce_1 smart_home_1
```

### 2. Review Results
Check the analyses:
```bash
cd tau/error_analyses
ls -lh
cat comprehensive_report.json | python3 -m json.tool
```

### 3. Identify Patterns
Look for:
- Environments with high failure rates
- Common fault types (wrong tool, wrong args, etc.)
- Environment bugs vs agent issues

### 4. Fix Issues
Based on findings:
- Fix environment bugs
- Update tool schemas
- Improve prompts

### 5. Scale Up
Once satisfied, run on more or all environments.

---

## 📈 Expected Results

### Typical Fault Distribution
```
User faults:    5-10%  (unclear instructions)
Agent faults:   30-40% (wrong tool choice, bad arguments)
Env faults:     50-60% (bugs in environment code)
```

### Common Fault Types
- `wrong_tool`: Agent chose incorrect tool
- `wrong_argument`: Correct tool, wrong parameters
- `missing_action`: Agent didn't call required tool
- `incorrect_output`: Wrong response format

---

## 🐛 Troubleshooting

### "No results file found"
**Solution:** Run with `--run-tests` to generate results.

### "Timeout running tests"
**Solution:** Some environments have long-running tasks. Increase timeout or skip.

### "Analysis failed"
**Possible causes:**
- Results file is corrupted
- No failures to analyze (all tasks passed)
- API rate limits hit

**Solution:** Check error message, verify results file, or retry.

### "ZeroDivisionError"
**Cause:** All tasks passed (no failures to analyze).  
**Solution:** This is actually good! No bugs found.

---

## 💡 Tips

1. **Start small:** Test 5-10 environments first
2. **Check costs:** Monitor OpenAI usage dashboard
3. **Use caching:** Results files are reused if they exist
4. **Parallelize carefully:** Max concurrency of 3-5 to avoid rate limits
5. **Review manually:** Auto-analysis isn't perfect - verify findings

---

## 📚 Output Files

### Structure
```
tau/
├── results/
│   ├── tool-calling-...-academic_search_1.json
│   ├── tool-calling-...-banking_services_1.json
│   └── ...
└── error_analyses/
    ├── academic_search_1_error_analysis.json
    ├── banking_services_1_error_analysis.json
    ├── comprehensive_report.json
    └── ...
```

### Analysis File Format
```json
{
  "fault_assignment_analysis": [
    {
      "task_id": 0,
      "author": "environment",
      "description": "Bug in search_projects tool..."
    }
  ],
  "fault_type_analysis": [
    {
      "task_id": 1,
      "fault_type": "wrong_argument",
      "explanation": "Agent passed string instead of int..."
    }
  ]
}
```

---

## 🎯 Quick Commands

```bash
# Analyze existing results only
python3 run_error_analysis_all_envs.py

# Test + analyze 3 environments
python3 run_error_analysis_all_envs.py --run-tests \
  --envs academic_search_1 banking_services_1 retail_1

# Test all, analyze later
python3 run_error_analysis_all_envs.py --run-tests --skip-analysis

# Analyze all (if tests already run)
python3 run_error_analysis_all_envs.py

# View comprehensive report
cat tau/error_analyses/comprehensive_report.json | python3 -m json.tool
```

---

## ✅ Success Criteria

After running error analysis, you should:
1. ✅ Identify all environment bugs
2. ✅ Understand common failure patterns
3. ✅ Have data to improve agent performance
4. ✅ Know which environments need fixes

Use findings to iterate and improve the benchmark!

