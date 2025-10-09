# Unused Code Finder

A deterministic tool to find and remove unused Python code in the `tau/` directory using [Vulture](https://github.com/jendrikseipp/vulture).

## Features

- 🔍 **Deterministic scanning** - Uses static analysis to find unused code
- 📊 **Detailed reports** - Shows unused functions, classes, variables, imports, and more
- 🎯 **Confidence levels** - Filter results by confidence percentage
- 💾 **JSON exports** - Save detailed reports for further analysis
- 🗑️ **Safe deletion** - Delete unused code with confirmation prompts
- 🧪 **Dry-run mode** - Preview what would be deleted without modifying files
- ⚠️ **Syntax error detection** - Identifies Python files with syntax errors
- 📈 **Comprehensive summaries** - Get an overview of code health

## Installation

First, install Vulture:

```bash
pip install vulture
```

## Usage

### 1. Find unused code and syntax errors (report only)

```bash
python find_unused_code.py
```

This will:
- Scan all Python files in `tau/`
- Report syntax errors (files that can't be analyzed)
- Report unused code with 60%+ confidence (default)
- Save detailed JSON reports

### 2. Check for syntax errors only (faster)

```bash
python find_unused_code.py --syntax-errors-only
```

Quickly scan for syntax errors without analyzing for unused code. Useful for:
- Quick code health checks
- Pre-commit validation
- CI/CD pipelines

### 3. Find with higher confidence threshold

```bash
python find_unused_code.py --confidence 80
```

Only report items with 80% or higher confidence (reduces false positives).

### 4. Preview what would be deleted (dry run)

```bash
python find_unused_code.py --dry-run
```

Shows what would be deleted without actually modifying any files.

### 5. Actually delete unused code

```bash
python find_unused_code.py --delete
```

This will:
- Find all unused code
- Ask for confirmation
- Delete the unused code from files

⚠️ **Warning**: This modifies your files! Make sure you have backups or use git.

### 6. Delete with high confidence only

```bash
python find_unused_code.py --delete --confidence 90
```

Only delete code that Vulture is 90%+ confident is unused.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--delete` | Actually delete unused code (requires confirmation) | False (report only) |
| `--confidence N` | Minimum confidence level (0-100) | 60 |
| `--target DIR` | Target directory to scan | `tau` |
| `--output FILE` | JSON report output file | `unused_code_report.json` |
| `--dry-run` | Simulate deletion without modifying files | False |
| `--syntax-errors-only` | Only check for syntax errors (skip unused code) | False |
| `--export-syntax-errors FILE` | Export syntax errors to separate JSON | `syntax_errors.json` |

## What Vulture Detects

Vulture can find:

- **Unused functions** - Functions that are never called
- **Unused classes** - Classes that are never instantiated
- **Unused methods** - Methods that are never called
- **Unused variables** - Variables that are assigned but never used
- **Unused attributes** - Class attributes that are never accessed
- **Unused imports** - Imported modules/functions that are never used
- **Unused properties** - Properties that are never accessed

## Understanding Confidence Levels

- **90-100%**: Very likely unused (safe to delete)
- **80-89%**: Probably unused (review before deleting)
- **60-79%**: Possibly unused (may have false positives)
- **Below 60%**: More likely to be false positives

## Example Output

```
🔍 Scanning tau for unused code (min confidence: 60%)...

================================================================================
⚠️  SYNTAX ERRORS DETECTED
================================================================================

⚠️  Found 278 syntax error(s) in 278 file(s)
   These files cannot be analyzed for unused code until syntax is fixed.

================================================================================
SYNTAX ERROR DETAILS
================================================================================

📄 tau/tau_bench/envs/some_env/tools/example.py
   1 syntax error(s):

   ❌ Line   23: '(' was never closed at "total = sum(x for x in items.values()"

================================================================================
📊 UNUSED CODE REPORT
================================================================================

Total unused items found: 42

By Type:
  • unused function: 15
  • unused import: 18
  • unused variable: 7
  • unused class: 2

Affected files: 8

================================================================================
DETAILED FINDINGS
================================================================================

📄 tau/tau_bench/agents/helper.py
   3 unused item(s):

   🔴 Line   15: unused import        'datetime' (95% confidence)
   🟡 Line   87: unused function      'old_helper_func' (75% confidence)
   🟡 Line  142: unused variable      'temp_var' (70% confidence)

================================================================================

💾 Detailed report saved to: unused_code_report.json
💾 Syntax errors exported to: syntax_errors.json

================================================================================
📋 FINAL SUMMARY
================================================================================

⚠️  Syntax Errors: 278 error(s) in 278 file(s)
🔍 Unused Code: 42 item(s) in 8 file(s)

================================================================================
```

## Safety Recommendations

1. **Always commit your changes first** before running with `--delete`
2. **Start with high confidence** - Try `--confidence 90` first
3. **Use dry-run** - Preview deletions with `--dry-run`
4. **Review the JSON report** - Check `unused_code_report.json` before deleting
5. **Test after deletion** - Run your test suite after deleting code

## Understanding Syntax Errors

**Important**: Vulture (and Python's AST parser) cannot analyze files with syntax errors. These must be fixed before unused code analysis can work.

Common syntax errors detected:
- **Unclosed parentheses**: `sum(x for x in items.values(` - missing closing `)`
- **Unmatched brackets**: Mixing `(` with `]` or `{` with `)`
- **Invalid f-strings**: Unmatched braces in f-string expressions
- **Invalid syntax**: Missing colons, commas, or other required syntax elements

The tool exports syntax errors to `syntax_errors.json` for easy processing and fixing.

## JSON Report Formats

### unused_code_report.json

Contains both unused code items and syntax errors:

```json
{
  "total_items": 42,
  "total_syntax_errors": 278,
  "summary": {
    "by_type": {"unused function": 15, "unused import": 18, ...},
    "affected_files": 8,
    "files_with_syntax_errors": 278
  },
  "items": [...],
  "syntax_errors": [...]
}
```

### syntax_errors.json

Contains only syntax errors organized by file:

```json
{
  "total_syntax_errors": 278,
  "files_with_errors": 278,
  "errors_by_file": {
    "path/to/file.py": [
      {"filepath": "...", "line": 23, "error": "...", "raw": "..."}
    ]
  },
  "all_errors": [...]
}
```

## Common False Positives

Vulture may flag as unused:

- Code called via `getattr()` or `eval()`
- Code used in templates or configuration files
- API endpoints that are called externally
- Test fixtures and mocks
- Code used only in subclasses

Always review high-impact deletions manually!

## Example Workflow

```bash
# Step 1: Scan and review
python find_unused_code.py --confidence 80

# Step 2: Check the report
cat unused_code_report.json

# Step 3: Preview deletions
python find_unused_code.py --confidence 80 --dry-run

# Step 4: Commit current state
git add -A && git commit -m "Before unused code cleanup"

# Step 5: Delete unused code
python find_unused_code.py --confidence 80 --delete

# Step 6: Run tests
python -m pytest

# Step 7: Review and commit
git diff
git commit -am "Remove unused code"
```

## Troubleshooting

### "vulture is not installed"

Install it: `pip install vulture`

### Too many false positives

Increase confidence: `--confidence 90`

### Want to exclude certain files

Edit the script and add exclusion patterns, or use vulture's whitelist feature.

## More Information

- [Vulture Documentation](https://github.com/jendrikseipp/vulture)
- [Creating Vulture Whitelists](https://github.com/jendrikseipp/vulture#whitelisting)

