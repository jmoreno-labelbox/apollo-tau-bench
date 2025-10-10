# Modular Tools Structure Guide

This guide explains the two different tool organization patterns in tau-bench and how to convert between them.

---

## 📊 Two Organization Patterns

### Pattern 1: Modular (airline base)

```
airline/
├── env.py
├── tools/                    ← Directory
│   ├── __init__.py          ← Exports ALL_TOOLS
│   ├── book_reservation.py   ← One tool per file
│   ├── calculate.py
│   ├── cancel_reservation.py
│   └── ... (14 separate files)
├── data.py
├── tasks_test.py
└── wiki.py
```

**Advantages:**
- ✅ Easier to navigate and find specific tools
- ✅ Better git diffs (changes isolated to one file)
- ✅ Parallel development (multiple people can edit different tools)
- ✅ Clearer organization and separation of concerns
- ✅ Easier to reuse individual tools

**Disadvantages:**
- ❌ More files to manage
- ❌ Slightly more complex import structure

---

### Pattern 2: Monolithic (all warrior variations)

```
airline_1/
├── env.py
├── tools.py                  ← Single file (~86KB)
├── data.py
├── tasks_test.py
└── wiki.py
```

**Advantages:**
- ✅ Single file to copy/sync
- ✅ Simpler imports
- ✅ All tools visible in one place
- ✅ Easier to search across all tools

**Disadvantages:**
- ❌ Large files (can be 80-200KB+)
- ❌ Harder to navigate
- ❌ Merge conflicts more likely
- ❌ Slower editor performance with large files

---

## 🔄 How They Import Tools

### Modular Structure

**env.py:**
```python
from tau_bench.envs.airline.tools import ALL_TOOLS

class MockAirlineDomainEnv(Env):
    def __init__(self, ...):
        super().__init__(
            tools=ALL_TOOLS,  # ← List of tool classes
            ...
        )
```

**tools/__init__.py:**
```python
from .book_reservation import BookReservation
from .calculate import Calculate
from .cancel_reservation import CancelReservation
# ... more imports

ALL_TOOLS = [
    BookReservation,
    Calculate,
    CancelReservation,
    # ... all tool classes
]
```

**tools/book_reservation.py:**
```python
from tau_bench.envs.tool import Tool

class BookReservation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # ... implementation
```

---

### Monolithic Structure

**env.py:**
```python
from tau_bench.envs.airline_1.tools import TOOLS

class MockAirlineDomainEnv(Env):
    def __init__(self, ...):
        super().__init__(
            tools=TOOLS,  # ← List of tool classes
            ...
        )
```

**tools.py:**
```python
from tau_bench.envs.tool import Tool

class BookReservation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # ... implementation

class Calculate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # ... implementation

# ... 12 more classes ...

TOOLS = [BookReservation, Calculate, ...]
```

---

## 🛠️ Converting Monolithic → Modular

Use the provided conversion script:

### 1. Preview the conversion (dry-run)

```bash
python3 convert_to_modular_tools.py academic_search_1
```

This shows what will be created without making changes.

### 2. Execute the conversion

```bash
python3 convert_to_modular_tools.py academic_search_1 --execute
```

This will:
1. ✅ Create `tools/` directory
2. ✅ Split each tool class into its own file
3. ✅ Create `tools/__init__.py` with imports
4. ✅ Update `env.py` to use `ALL_TOOLS`
5. ✅ Rename `tools.py` → `tools.py.monolithic` (backup)

### 3. Test the converted environment

```bash
cd tau
python3 run.py --env academic_search_1 --end-index 1
```

### 4. If successful, clean up

```bash
rm tau/tau_bench/envs/academic_search_1/tools.py.monolithic
```

---

## 📋 What the Script Does

### Step-by-Step Process

1. **Parses tools.py** using Python AST
2. **Extracts each Tool class** and its code
3. **Creates tools/ directory**
4. **Generates individual files:**
   - `SearchUsers` → `search_users.py`
   - `GetUserProfile` → `get_user_profile.py`
   - `UpdateResearchPaper` → `update_research_paper.py`
   
5. **Creates __init__.py:**
   ```python
   from .search_users import SearchUsers
   from .get_user_profile import GetUserProfile
   # ... all imports
   
   ALL_TOOLS = [SearchUsers, GetUserProfile, ...]
   ```

6. **Updates env.py:**
   ```python
   # Before
   from tau_bench.envs.X.tools import TOOLS
   tools=TOOLS
   
   # After
   from tau_bench.envs.X.tools import ALL_TOOLS
   tools=ALL_TOOLS
   ```

7. **Backs up original:**
   ```bash
   tools.py → tools.py.monolithic
   ```

---

## 🎯 When to Use Each Pattern

### Use Modular When:
- 🔧 Actively developing/iterating on tools
- 👥 Multiple developers working on same environment
- 📝 Want better code organization
- 🔍 Tools are complex and need their own files
- 🚀 Environment has 10+ tools

### Use Monolithic When:
- 📦 Distributing/sharing environments
- 🔄 Frequently syncing tools across systems
- 🎯 Small number of simple tools (< 5 tools)
- 📋 Want everything in one searchable file
- 🚀 Tools are simple and don't change often

---

## 🔄 Converting Modular → Monolithic

If you need to go the other way (combine separate files into one):

```bash
# Manual process:
# 1. Create new tools.py
# 2. Copy all imports from tools/__init__.py
# 3. Copy all class definitions from tools/*.py
# 4. Create TOOLS list
# 5. Update env.py imports
# 6. Remove tools/ directory
```

Or write a reverse conversion script (not provided).

---

## ❓ FAQ

**Q: Why does only `airline` (base) use modular structure?**  
A: It's the original legacy structure from tau-bench. The warrior variations all use monolithic for easier copying/syncing.

**Q: Should I convert all environments to modular?**  
A: Only if you're actively developing them. For production use, monolithic is fine.

**Q: Will conversion break anything?**  
A: No, as long as the conversion completes successfully and tests pass. The script preserves all functionality.

**Q: Can I mix patterns in the same codebase?**  
A: Yes! Each environment is independent. `airline` can be modular while `airline_1` is monolithic.

**Q: Which pattern is "better"?**  
A: Depends on your use case:
- **Development** → Modular
- **Distribution** → Monolithic

---

## 🚀 Quick Reference

```bash
# Preview conversion
python3 convert_to_modular_tools.py <env_name>

# Execute conversion
python3 convert_to_modular_tools.py <env_name> --execute

# Test converted environment
cd tau
python3 run.py --env <env_name> --end-index 1

# Clean up backup if successful
rm tau/tau_bench/envs/<env_name>/tools.py.monolithic
```

---

## 📚 Examples

### Example 1: Convert academic_search_1

```bash
# 1. Preview
python3 convert_to_modular_tools.py academic_search_1

# 2. Execute
python3 convert_to_modular_tools.py academic_search_1 --execute

# 3. Test
cd tau
python3 run.py --env academic_search_1 --end-index 1

# 4. Cleanup
rm tau/tau_bench/envs/academic_search_1/tools.py.monolithic
```

### Example 2: Convert banking_services_1

```bash
python3 convert_to_modular_tools.py banking_services_1 --execute
cd tau && python3 run.py --env banking_services_1 --end-index 1
```

---

## ✅ Summary

- **airline (base)** = Modular (legacy structure)
- **All warrior variations** = Monolithic (easier to sync)
- **Conversion script** = Automates modular conversion
- **Both patterns work** = Choose based on your needs
- **Test after conversion** = Always verify functionality

The choice is yours! 🎉

