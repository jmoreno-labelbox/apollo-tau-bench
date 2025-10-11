# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


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
