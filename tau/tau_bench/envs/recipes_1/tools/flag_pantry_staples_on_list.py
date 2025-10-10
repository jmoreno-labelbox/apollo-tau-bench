# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class FlagPantryStaplesOnList(Tool):
    """Set pantry_staple_flag on list items based on ingredients table."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in list(data.get("grocery_list_items", {}).values()):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["pantry_staple_flag"] = bool((ing or {}).get("pantry_staple_flag", False))
            updated += 1
        return _json_dump({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"flag_pantry_staples_on_list",
            "description":"Fill pantry_staple_flag for items in a list.",
            "parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":["list_id"]}
        }}
