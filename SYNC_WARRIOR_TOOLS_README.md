# Sync Warrior Tools Script

## Purpose

Copies `tools.py` files from `domains_warrior` variations to the corresponding `tau/tau_bench/envs` directories.

## What It Does

**Maps:**
```
domains_warrior/<domain>/variations/variation_<N>/tools.py
  → tau/tau_bench/envs/<domain>_<N>/tools.py
```

**Example:**
```
domains_warrior/banking_services/variations/variation_6/tools.py
  → tau/tau_bench/envs/banking_services_6/tools.py
```

## Usage

### 1. Preview (Dry Run)
See what would be copied without making changes:

```bash
python3 sync_warrior_tools.py
```

**Output:**
```
🔍 DRY RUN MODE - No files will be modified

Found 121 tools.py files in domains_warrior

📋 WOULD COPY: banking_services/variations/variation_6/tools.py
         → tau/tau_bench/envs/banking_services_6/tools.py
...

DRY RUN SUMMARY:
  Would copy: 121 files
  Would skip: 0 files
```

### 2. Execute the Sync
Actually copy the files (with automatic backups):

```bash
python3 sync_warrior_tools.py --execute
```

**What happens:**
- ✅ Existing files are backed up to `.backup` extension
- ✅ New files are copied from `domains_warrior`
- ✅ Summary shows what was done

### 3. Sync Specific Domain
Only sync one domain:

```bash
python3 sync_warrior_tools.py --execute --domain banking_services
```

## Safety Features

### Automatic Backups
Before overwriting any file, the script creates a backup:
```
tau/tau_bench/envs/banking_services_6/tools.py
  → tau/tau_bench/envs/banking_services_6/tools.py.backup
```

### Dry Run by Default
The script defaults to dry-run mode to prevent accidents:
- ✅ Must explicitly use `--execute` to make changes
- ✅ Shows exactly what will happen before doing it

### Error Handling
- Checks if target directories exist
- Reports any errors during copying
- Continues on errors (doesn't crash)

## Example Run

```bash
$ python3 sync_warrior_tools.py --execute

⚠️  EXECUTE MODE - Files will be modified!
   Existing files will be backed up with .backup extension

Found 121 tools.py files in domains_warrior

📝 COPYING: banking_services/variations/variation_6/tools.py
         → tau/tau_bench/envs/banking_services_6/tools.py
   💾 Backed up existing file to tools.py.backup
   ✅ Copied successfully

... (120 more files)

============================================================
SYNC COMPLETE:
  ✅ Copied: 121 files
  ⚠️  Skipped: 0 files
============================================================
```

## Files Found

The script syncs **121 tools.py files** from these domains:

- `academic_search` (variations 1-5)
- `airline` (variations 1-3, 5)
- `banking_services` (variations 1, 2, 4-6)
- `career_planner` (variations 1-5)
- `consulting_accounting` (variations 1, 2, 4-6)
- `data_science` (variations 1-6)
- `dev_ops` (variations 1-6)
- `digital_commerce` (variations 1-5)
- `figma_gmail_mcp_pipeline` (variations 1-6)
- `file_system` (variations 1, 7-9)
- `github_mcp` (variations 1, 2, 5-7)
- `it_help_desk` (variations 2, 4-6)
- `logistics_supply_chain` (variations 1-3, 5-6)
- `new_hire_mcp` (variations 1-5)
- `org_chart` (variations 1-5)
- `project_management` (variations 1-5)
- `rbac` (variations 1-5)
- `real_estate_sales` (variations 1-4, 7)
- `recipes` (variations 1-5)
- `retail` (variations 1-6)
- `retail_point_of_sale_and_inventory_system` (variations 1, 2, 4-6)
- `smart_home` (variations 1-5)
- `social_media_advertising` (variations 1-6)
- `sports_analytics` (variations 2-5)

## Common Commands

```bash
# Preview what will happen
python3 sync_warrior_tools.py

# Do the actual sync
python3 sync_warrior_tools.py --execute

# Sync only banking_services
python3 sync_warrior_tools.py --execute --domain banking_services

# Show help
python3 sync_warrior_tools.py --help
```

## Rollback

If you need to undo the sync:

```bash
# Restore all backups
find tau/tau_bench/envs -name "tools.py.backup" -exec sh -c '
    mv "$1" "${1%.backup}"
' sh {} \;

# Or restore one file
mv tau/tau_bench/envs/banking_services_6/tools.py.backup \
   tau/tau_bench/envs/banking_services_6/tools.py
```

## Troubleshooting

### "target directory doesn't exist"
If a variation exists in `domains_warrior` but not in `tau/tau_bench/envs`:
```
⚠️  Skipping banking_services_3: target directory doesn't exist
   Missing: tau/tau_bench/envs/banking_services_3
```

**Solution:** The variation doesn't exist in the tau environment. This is normal - not all variations exist in both places.

### Permission errors
Make sure the script is executable:
```bash
chmod +x sync_warrior_tools.py
```

## Notes

- ✅ The script preserves file permissions and timestamps
- ✅ Existing files are always backed up before overwriting
- ✅ The script is idempotent (safe to run multiple times)
- ✅ No files are deleted, only copied/replaced

