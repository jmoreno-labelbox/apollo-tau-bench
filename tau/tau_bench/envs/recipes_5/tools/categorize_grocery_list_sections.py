# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class CategorizeGroceryListSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id) -> str:
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        cnt = 0
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            ingr = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ingr or {}).get("grocery_section", "Misc")
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"categorize_grocery_list_sections","description":"Refresh grocery_section on all items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}
