#!/usr/bin/env python3
"""
Fix duplicate wiki=WIKI in env.py files
"""

import re
from pathlib import Path

def fix_env_file(env_file: Path):
    """Remove duplicate wiki=WIKI from env.py."""
    content = env_file.read_text()
    
    # Check for the pattern where wiki appears twice in super().__init__()
    if content.count('wiki=WIKI,') >= 2:
        # Use regex to find and replace the super().__init__() block
        # Match the super().__init__( ... ) block and remove one wiki=WIKI,
        pattern = r'(super\(\).__init__\([^)]*?wiki=WIKI,)(\s*wiki=WIKI,)'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
            env_file.write_text(content)
            return True
    
    return False

def main():
    tau_envs_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_envs_dir.exists():
        print(f"❌ tau/tau_bench/envs directory not found at {tau_envs_dir}")
        return
    
    print("🔧 Fixing duplicate wiki=WIKI in env.py files...\n")
    
    fixed_count = 0
    
    # Process each environment directory
    for env_dir in tau_envs_dir.iterdir():
        if not env_dir.is_dir() or env_dir.name.startswith('_') or env_dir.name == '__pycache__':
            continue
        
        env_file = env_dir / "env.py"
        if env_file.exists():
            if fix_env_file(env_file):
                fixed_count += 1
                print(f"  ✅ Fixed {env_dir.name}/env.py")
    
    print(f"\n✅ Fixed {fixed_count} env.py files!")

if __name__ == "__main__":
    main()

