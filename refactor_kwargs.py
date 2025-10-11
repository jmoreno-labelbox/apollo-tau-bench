# refactor_kwargs.py
import argparse
import sys
from typing import Dict, Optional, Set, Tuple

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
        self.func_stack: list["KwargsRefactorTransformer.FunctionContext"] = []

    # ---------- Utility structures ----------

    class ParamSpec:
        def __init__(self, name: str, default: Optional[cst.BaseExpression]):
            self.name = name
            self.default = default  # None => required

    class FunctionContext:
        def __init__(self, func: cst.FunctionDef):
            self.func = func
            self.kwstar_name: Optional[str] = None  # "**kwargs" name
            self.existing_param_names: Set[str] = set()
            self.new_params: Dict[str, "KwargsRefactorTransformer.ParamSpec"] = {}
            # Track assignments like `x = kwargs.get("x", ...)`
            self.assigns_that_can_be_removed: Set[cst.CSTNode] = set()

    # ---------- Helpers ----------

    def _add_param(self, ctx: "KwargsRefactorTransformer.FunctionContext",
                   name: str, default: Optional[cst.BaseExpression]) -> None:
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
            else:
                # If different defaults are encountered, prefer the existing one
                # (could add conflict reporting if you want)
                pass

    def _is_kwargs_name(self, name: str) -> bool:
        if not self.func_stack:
            return False
        return self.func_stack[-1].kwstar_name == name

    # ---------- Function scope mgmt ----------

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
        if not ctx.kwstar_name:
            return updated_node

        # Build new parameter list: remove **kwargs; append new params
        params = updated_node.params

        # Remove **kwargs
        params = params.with_changes(star_kwarg=None)

        # Append new params at the end of normal params (before kwonly to keep simple)
        new_params_nodes = []
        for name, spec in ctx.new_params.items():
            # Avoid collisions with existing names
            if name in ctx.existing_param_names:
                continue
            new_params_nodes.append(cst.Param(name=cst.Name(name), default=spec.default))

        if new_params_nodes:
            params = params.with_changes(params=list(params.params) + new_params_nodes)

        # Remove redundant assigns (like `x = kwargs.get("x", ...)`) when LHS == param name
        new_body = []
        for stmt in updated_node.body.body:
            if stmt in ctx.assigns_that_can_be_removed:
                continue
            new_body.append(stmt)

        updated_node = updated_node.with_changes(params=params,
                                                body=updated_node.body.with_changes(body=new_body))
        return updated_node

    # ---------- Rewriters for expression patterns ----------

    # Pattern: kwargs.get("key", default?)
    def _match_kwargs_get(self, node: cst.Call) -> Optional[Tuple[str, Optional[cst.BaseExpression]]]:
        if not m.matches(node.func, m.Attribute(value=m.Name(), attr=m.Name("get"))):
            return None
        attr: cst.Attribute = node.func  # type: ignore
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
        # Extract key string literal (handles single/double/triple quotes)
        key = first.evaluated_value  # LibCST gives the unescaped literal value
        default_expr = None
        if len(node.args) >= 2:
            default_expr = node.args[1].value
        return key, default_expr

    # Pattern: kwargs["key"]
    def _match_kwargs_subscript(self, node: cst.Subscript) -> Optional[str]:
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

    # Replace kwargs.get(...) with parameter name and register param
    def leave_Call(self, old_node: cst.Call, updated_node: cst.Call) -> cst.BaseExpression:
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

    # Replace kwargs["key"] with parameter name and register REQUIRED param
    def leave_Subscript(self, old_node: cst.Subscript, updated_node: cst.Subscript) -> cst.BaseExpression:
        if not self.func_stack:
            return updated_node
        key = self._match_kwargs_subscript(old_node)
        if not key:
            return updated_node
        ctx = self.func_stack[-1]
        self._add_param(ctx, key, default=None)
        return cst.Name(key)

    # Handle assignments like: x = kwargs.get("x", 0)
    def leave_Assign(self, old_node: cst.Assign, updated_node: cst.Assign) -> cst.BaseStatement:
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
                    # Redundant: "x = x" - mark for removal
                    ctx.assigns_that_can_be_removed.add(old_node)
                    return updated_node  # Don't remove here, remove in leave_FunctionDef
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
                    ctx.assigns_that_can_be_removed.add(old_node)
                    return updated_node  # Don't remove here, remove in leave_FunctionDef
                else:
                    return updated_node.with_changes(value=cst.Name(key))

        return updated_node


def refactor_code(src: str) -> str:
    try:
        mod = cst.parse_module(src)
        out = mod.visit(KwargsRefactorTransformer())
        return out.code
    except Exception as e:
        # If transformation fails, return original code
        return src


def main():
    ap = argparse.ArgumentParser(description="Refactor **kwargs to explicit parameters where used via kwargs.get(...) or kwargs['...'].")
    ap.add_argument("path", help="Python file to rewrite")
    ap.add_argument("--stdout", action="store_true", help="Print to stdout instead of writing back")
    args = ap.parse_args()

    text = open(args.path, "r", encoding="utf-8").read()
    new_text = refactor_code(text)

    if args.stdout:
        sys.stdout.write(new_text)
    else:
        with open(args.path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"Rewrote {args.path}")


if __name__ == "__main__":
    main()
