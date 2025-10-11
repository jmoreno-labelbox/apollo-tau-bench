# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump






def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _ingredient_by_id(data: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next((i for i in data.get("ingredients", []) if int(i.get("ingredient_id")) == ingredient_id), None)

class FlagPantryStaplesOnList(Tool):
    """Set pantry_staple_flag on list items based on ingredients table."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id) -> str:
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