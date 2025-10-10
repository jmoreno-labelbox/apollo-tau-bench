# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogInventoryConsumeByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, user_id: int, ingredient_id: int, delta: float
    ) -> str:
        inv = next(
            (
                i
                for i in data.get("inventory_items", [])
                if int(i.get("household_id")) == int(household_id)
                and int(i.get("ingredient_id")) == int(ingredient_id)
            ),
            None,
        )
        if not inv:
            return json({"error": "inventory row not found for keys"})
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "inventory_items",
            "entity_id": int(inv.get("inv_item_id")),
            "action_enum": "consume",
            "payloadjson": {"ingredient_id": int(ingredient_id), "delta": float(delta)},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_inventory_consume_by_keys",
                "description": "Append audit log consume event using (household_id, ingredient_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "delta": {"type": "number"},
                    },
                    "required": ["household_id", "user_id", "ingredient_id", "delta"],
                },
            },
        }
