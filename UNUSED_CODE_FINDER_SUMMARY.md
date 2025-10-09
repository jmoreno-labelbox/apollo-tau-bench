# Unused Code Finder - Quick Summary

## ✅ What Was Created

1. **`find_unused_code.py`** - Main script for finding unused and inaccessible Python code
2. **`UNUSED_CODE_FINDER_README.md`** - Comprehensive documentation
3. **`unused_code_report.json`** - Generated report with unused code and syntax errors
4. **`syntax_errors.json`** - Separate export of just syntax errors

## 🔍 What It Does

The script uses **Vulture**, a deterministic static analysis tool that:
- Finds unused functions, classes, methods, variables, imports, and properties
- Detects Python files with syntax errors that prevent analysis
- Provides confidence scores (60-100%) for each finding
- Exports detailed JSON reports for further processing
- Can automatically delete unused code (with confirmation)

## 🚀 Quick Start

### 1. Scan for unused code and syntax errors
```bash
python find_unused_code.py
```

### 2. Only check syntax errors (fast)
```bash
python find_unused_code.py --syntax-errors-only
```

### 3. High confidence scan
```bash
python find_unused_code.py --confidence 90
```

### 4. Preview deletions (dry run)
```bash
python find_unused_code.py --confidence 80 --dry-run
```

### 5. Actually delete unused code
```bash
python find_unused_code.py --confidence 90 --delete
```

## 📊 Current Status for `tau/` Directory

Running the scan revealed:
- **278 Python files with syntax errors** - These must be fixed before unused code analysis works
- **0 unused code items detected** - In files without syntax errors

## 🎯 Key Features

| Feature | Flag | Description |
|---------|------|-------------|
| **Report Mode** | (default) | Scans and reports, no modifications |
| **Syntax Check Only** | `--syntax-errors-only` | Fast scan for syntax errors only |
| **Confidence Filter** | `--confidence N` | Only show items with N% confidence |
| **Dry Run** | `--dry-run` | Preview what would be deleted |
| **Delete Mode** | `--delete` | Actually delete unused code (asks confirmation) |
| **Custom Target** | `--target DIR` | Scan a different directory |

## 📁 Output Files

### unused_code_report.json
Complete report including:
- All unused code items with locations and confidence scores
- All syntax errors with file paths and line numbers
- Summary statistics by type and file

### syntax_errors.json
Focused export of syntax errors:
- Organized by file for easy processing
- Includes line numbers and error descriptions
- Can be used to create automated fixes

## ⚠️ Important Notes

1. **Syntax errors must be fixed first** - Files with syntax errors cannot be analyzed for unused code
2. **Review before deleting** - Always use `--dry-run` first and review the reports
3. **Confidence matters** - Start with 90+ confidence to avoid false positives
4. **Backup your code** - Commit to git before using `--delete`
5. **False positives exist** - Code called via `getattr()`, used in templates, or external APIs may be flagged

## 🔧 Common Use Cases

### Find all syntax errors
```bash
python find_unused_code.py --syntax-errors-only
```
Output: `syntax_errors.json` with all 278 syntax errors

### Scan with high confidence
```bash
python find_unused_code.py --confidence 90
```
Only shows unused code Vulture is 90%+ certain about

### Clean up imports and dead code
```bash
# Step 1: Preview
python find_unused_code.py --confidence 80 --dry-run

# Step 2: Review reports
cat unused_code_report.json

# Step 3: Backup
git commit -am "Before cleanup"

# Step 4: Delete
python find_unused_code.py --confidence 80 --delete
```

## 📈 Next Steps

1. **Fix syntax errors** - Use `syntax_errors.json` to identify and fix the 278 files
2. **Re-scan** - After fixing syntax errors, re-run to find unused code
3. **Review findings** - Check the JSON reports for detailed analysis
4. **Clean up** - Use `--delete` to remove confirmed unused code

## 🆘 Getting Help

```bash
python find_unused_code.py --help
```

Full documentation: `UNUSED_CODE_FINDER_README.md`

---

**Tool**: Vulture v2.14  
**Deterministic**: Yes (same input = same output)  
**Safe**: Yes (requires confirmation for deletions)  
**Fast**: Yes (syntax-only mode scans 278 files in seconds)

