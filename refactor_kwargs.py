#!/usr/bin/env python3
"""
Refactor **kwargs to explicit parameters using LibCST.

This script transforms functions that accept **kwargs and use kwargs.get(...) or kwargs["..."]
into functions with explicit parameters and direct parameter usage.

Usage:
    python refactor_kwargs.py path/to/file.py  # writes changes in-place
    python refactor_kwargs.py --stdout path/to/file.py  # dry run to stdout
    python refactor_kwargs.py --dir path/to/directory  # process all .py files in directory
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, Optional, Set

import libcst as cst
import libcst.matchers as m
from libcst import RemovalSentinel


class KwargsRefactorTransformer(cst.CSTTransformer):
    """
    Transform functions that take **kwargs and use kwargs.get(...) or kwargs["..."]
    into functions with explicit parameters and direct param usage.
    """

    def __init__(self):
        # Stack of function contexts to handle nesting correctly
        self.func_stack = []

    class ParamSpec:
        def __init__(self, name: str, default: Optional[cst.BaseExpression]):
            self.name = name
            self.default = default  # None => required

    class FunctionContext:
        def __init__(self, func: cst.FunctionDef):
            self.func = func
            self.kwstar_name: Optional[str] = None  # "**kwargs" name
            self.existing_param_names: Set[str] = set()
            self.new_params: Dict[str, 'KwargsRefactorTransformer.ParamSpec'] = {}
            # Track assignments like `x = kwargs.get("x", ...)`
            self.assigns_that_can_be_removed: Set[cst.CSTNode] = set()

    def _add_param(self, ctx, name: str, default: Optional[cst.BaseExpression]) -> None:
        if name in ctx.existing_param_names:
            # Already explicitly present; do not override default
            return
        prev = ctx.new_params.get(name)
        if prev is None:
            ctx.new_params[name] = self.ParamSpec(name, default)
        else:
            # Merge defaults: if any usage has no default -> keep as required
            if prev.default is None:
                return
            if default is None:
                prev.default = None

    def _is_kwargs_name(self, name: str) -> bool:
        if not self.func_stack:
            return False
        return self.func_stack[-1].kwstar_name == name

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        ctx = self.FunctionContext(node)
        # Capture existing param names
        p = node.params
        for param in list(p.params) + list(p.posonly_params or []) + list(p.kwonly_params or []):
            ctx.existing_param_names.add(param.name.value)
        if p.star_kwarg is not None and isinstance(p.star_kwarg, cst.Param):
            ctx.kwstar_name = p.star_kwarg.name.value
        self.func_stack.append(ctx)
        return True

    def leave_FunctionDef(
        self, old_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        ctx = self.func_stack.pop()

        # If no **kwargs, or we didn't find any kwargs usage, return as is
        if not ctx.kwstar_name or not ctx.new_params:
            return updated_node

        # Build new parameter list: remove **kwargs; append new params
        params = updated_node.params

        # Remove **kwargs
        params = params.with_changes(star_kwarg=None)

        # Append new params at the end of normal params
        new_params_nodes = []
        for name, spec in sorted(ctx.new_params.items()):
            # Avoid collisions with existing names
            if name in ctx.existing_param_names:
                continue
            new_params_nodes.append(cst.Param(name=cst.Name(name), default=spec.default))

        if new_params_nodes:
            params = params.with_changes(params=list(params.params) + new_params_nodes)

        # Remove redundant assigns (like `x = kwargs.get("x", ...)`)
        new_body = []
        for stmt in updated_node.body.body:
            if stmt in ctx.assigns_that_can_be_removed:
                continue
            new_body.append(stmt)

        updated_node = updated_node.with_changes(
            params=params,
            body=updated_node.body.with_changes(body=new_body)
        )
        return updated_node

    def _match_kwargs_get(self, node: cst.Call):
        """Match kwargs.get("key", default?) pattern."""
        if not m.matches(node.func, m.Attribute(value=m.Name(), attr=m.Name("get"))):
            return None
        attr = node.func
        obj = attr.value
        if not isinstance(obj, cst.Name):
            return None
        if not self._is_kwargs_name(obj.value):
            return None
        # First arg must be string literal
        if len(node.args) == 0:
            return None
        first = node.args[0].value
        if not isinstance(first, cst.SimpleString):
            return None
        # Extract key string literal
        key = first.evaluated_value
        default_expr = None
        if len(node.args) >= 2:
            default_expr = node.args[1].value
        return key, default_expr

    def _match_kwargs_subscript(self, node: cst.Subscript):
        """Match kwargs["key"] pattern."""
        if not isinstance(node.value, cst.Name):
            return None
        if not self._is_kwargs_name(node.value.value):
            return None
        if len(node.slice) != 1:
            return None
        sl = node.slice[0]
        if not isinstance(sl, cst.SubscriptElement) or not isinstance(sl.slice, cst.Index):
            return None
        idx = sl.slice.value
        if not isinstance(idx, cst.SimpleString):
            return None
        return idx.evaluated_value

    def leave_Call(self, old_node: cst.Call, updated_node: cst.Call):
        """Replace kwargs.get(...) with parameter name."""
        if not self.func_stack:
            return updated_node
        mres = self._match_kwargs_get(old_node)
        if not mres:
            return updated_node
        key, default_expr = mres
        ctx = self.func_stack[-1]
        # Register a new param
        self._add_param(ctx, key, default_expr)
        # Replace call expression with Name(key)
        return cst.Name(key)

    def leave_Subscript(self, old_node: cst.Subscript, updated_node: cst.Subscript):
        """Replace kwargs["key"] with parameter name."""
        if not self.func_stack:
            return updated_node
        key = self._match_kwargs_subscript(old_node)
        if not key:
            return updated_node
        ctx = self.func_stack[-1]
        self._add_param(ctx, key, default=None)
        return cst.Name(key)

    def leave_Assign(self, old_node: cst.Assign, updated_node: cst.Assign):
        """Handle assignments like: x = kwargs.get("x", 0)."""
        if not self.func_stack:
            return updated_node
        # Only handle simple "a = <expr>" (single target)
        if len(old_node.targets) != 1 or not isinstance(old_node.targets[0].target, cst.Name):
            return updated_node

        target_name = old_node.targets[0].target.value
        value = old_node.value

        # kwargs.get pattern?
        if isinstance(value, cst.Call):
            mres = self._match_kwargs_get(value)
            if mres:
                key, default_expr = mres
                ctx = self.func_stack[-1]
                self._add_param(ctx, key, default_expr)

                if key == target_name:
                    # Redundant: "x = x"
                    ctx.assigns_that_can_be_removed.add(updated_node)
                    return RemovalSentinel.REMOVE
                else:
                    # Keep assignment but rewrite RHS to param name
                    return updated_node.with_changes(value=cst.Name(key))

        # kwargs["key"] pattern?
        if isinstance(value, cst.Subscript):
            key = self._match_kwargs_subscript(value)
            if key:
                ctx = self.func_stack[-1]
                self._add_param(ctx, key, default=None)

                if key == target_name:
                    ctx.assigns_that_can_be_removed.add(updated_node)
                    return RemovalSentinel.REMOVE
                else:
                    return updated_node.with_changes(value=cst.Name(key))

        return updated_node


def refactor_code(src: str) -> str:
    """Refactor source code to replace **kwargs with explicit parameters."""
    mod = cst.parse_module(src)
    out = mod.visit(KwargsRefactorTransformer())
    return out.code


def process_file(file_path: Path, stdout: bool = False) -> bool:
    """Process a single file. Returns True if successful."""
    try:
        text = file_path.read_text(encoding="utf-8")
        new_text = refactor_code(text)

        if stdout:
            sys.stdout.write(new_text)
        else:
            file_path.write_text(new_text, encoding="utf-8")
            print(f"Refactored: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    ap = argparse.ArgumentParser(
        description="Refactor **kwargs to explicit parameters where used via kwargs.get(...) or kwargs['...']."
    )
    ap.add_argument("path", help="Python file or directory to process")
    ap.add_argument("--stdout", action="store_true", help="Print to stdout instead of writing back")
    ap.add_argument("--recursive", "-r", action="store_true", help="Process directory recursively")
    args = ap.parse_args()

    path = Path(args.path)
    
    if not path.exists():
        print(f"Error: Path not found: {path}")
        sys.exit(1)

    if path.is_file():
        success = process_file(path, args.stdout)
        sys.exit(0 if success else 1)
    
    elif path.is_dir():
        if args.recursive:
            py_files = list(path.rglob("*.py"))
        else:
            py_files = list(path.glob("*.py"))
        
        py_files = [f for f in py_files if '__pycache__' not in str(f)]
        
        print(f"Found {len(py_files)} Python files to process")
        
        processed = 0
        failed = 0
        
        for py_file in py_files:
            if process_file(py_file, args.stdout):
                processed += 1
            else:
                failed += 1
        
        print(f"\nSummary: {processed} processed, {failed} failed")
        sys.exit(0 if failed == 0 else 1)
    
    else:
        print(f"Error: {path} is neither a file nor a directory")
        sys.exit(1)


if __name__ == "__main__":
    main()

