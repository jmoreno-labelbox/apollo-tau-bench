# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug

def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], **crit):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class UpsertContextRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        segment_name: str,
        rule_name_hint: str,
        attributes: Dict[str, Any],
        bind_to_offer_code: Optional[str] = None,
    ) -> str:
        rules = _ensure_table(data, "context_rules")
        binds = _ensure_table(data, "context_rule_bindings")

        context_rule_id = _stable_id("ctx", segment_name, rule_name_hint)
        title = f"{segment_name} – {rule_name_hint}"
        row = _find_one(rules, context_rule_id=context_rule_id)
        if row:
            row.update(
                {
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            rules.append(
                {
                    "context_rule_id": context_rule_id,
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "created_at": FIXED_NOW,
                }
            )

        binding_id = None
        if bind_to_offer_code:
            binding_id = _stable_id("bind", context_rule_id, bind_to_offer_code)
            existing = _find_one(binds, binding_id=binding_id)
            if existing:
                existing.update({"offer_code": bind_to_offer_code, "updated_at": FIXED_NOW})
            else:
                binds.append(
                    {
                        "binding_id": binding_id,
                        "context_rule_id": context_rule_id,
                        "offer_code": bind_to_offer_code,
                        "created_at": FIXED_NOW,
                    }
                )

        return _json({"context_rule_id": context_rule_id, "binding_id": binding_id, "title": title})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_context_rule",
                "description": "Create/update a context rule and optionally bind it to an offer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "segment_name": {"type": "string"},
                        "rule_name_hint": {"type": "string"},
                        "attributes": {"type": "object"},
                        "bind_to_offer_code": {"type": "string"},
                    },
                    "required": ["segment_name", "rule_name_hint", "attributes"],
                },
            },
        }