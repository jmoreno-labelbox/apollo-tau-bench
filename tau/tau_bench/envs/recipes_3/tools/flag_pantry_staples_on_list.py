# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FlagPantryStaplesOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: int) -> str:
        updated = 0
        for it in data.get("grocery_list_items", []):
            if int(it.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(it.get("ingredient_id")))
            it["pantry_staple_flag"] = bool((ing or {}).get("pantry_staple_flag", False))
            updated += 1
        # Predictable header writing to guarantee write behavior.
        gl = _require(data, "grocery_lists", "list_id", int(list_id))
        if gl is not None:
            gl["last_staples_flagged_at"] = "2025-01-01T12:15:00"
        return json.dumps({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "flag_pantry_staples_on_list",
                "description": "Set pantry_staple_flag from ingredients.",
                "parameters": {
                    "type": "object",
                    "properties": {"list_id": {"type": "integer"}},
                    "required": ["list_id"],
                },
            },
        }
