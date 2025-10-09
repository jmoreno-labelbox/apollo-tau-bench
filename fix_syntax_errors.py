#!/usr/bin/env python3
"""
Identify and report all Python syntax errors in environments.
This will help us fix them systematically.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "tau"))

def check_environment(env_name):
    """Try to load environment and report syntax errors"""
    try:
        # Try importing tools module
        tools_module = __import__(f'tau_bench.envs.{env_name}.tools', fromlist=[''])
        return env_name, None
    except SyntaxError as e:
        return env_name, {
            'type': 'SyntaxError',
            'line': e.lineno,
            'msg': e.msg,
            'text': e.text.strip() if e.text else '',
            'offset': e.offset,
            'file': e.filename
        }
    except Exception as e:
        return env_name, {
            'type': type(e).__name__,
            'msg': str(e)[:200]
        }

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    env_names = sorted([d.name for d in base.iterdir() 
                       if d.is_dir() and not d.name.startswith('_') and d.name != '__pycache__'])
    
    print("=" * 70)
    print(f"CHECKING SYNTAX ERRORS IN {len(env_names)} ENVIRONMENTS")
    print("=" * 70)
    print()
    
    errors_found = []
    
    for env in env_names:
        env_name, error = check_environment(env)
        if error and error.get('type') == 'SyntaxError':
            errors_found.append((env_name, error))
            print(f"❌ {env_name}")
            print(f"   Line {error['line']}: {error['msg']}")
            if error['text']:
                print(f"   Text: {error['text']}")
            print()
    
    print("=" * 70)
    print(f"SUMMARY: {len(errors_found)} environments with syntax errors")
    print("=" * 70)
    
    # Save detailed report
    with open('syntax_errors_report.txt', 'w') as f:
        for env_name, error in errors_found:
            f.write(f"{env_name}\n")
            f.write(f"  Line: {error['line']}\n")
            f.write(f"  Error: {error['msg']}\n")
            f.write(f"  Text: {error['text']}\n")
            f.write(f"  File: {error.get('file', 'N/A')}\n")
            f.write("\n")
    
    print(f"✅ Detailed report saved to syntax_errors_report.txt")

if __name__ == "__main__":
    main()

