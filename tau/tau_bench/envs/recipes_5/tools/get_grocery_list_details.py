# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"error": "no grocery_list available"})
        header = _ensure_list_id(data, list_id)
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [i for i in data.get("grocery_list_items", []) if i.get("list_id") == list_id]
        return _json_dump({"grocery_list": header, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_grocery_list_details","description":"Get a grocery_list header and items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}
