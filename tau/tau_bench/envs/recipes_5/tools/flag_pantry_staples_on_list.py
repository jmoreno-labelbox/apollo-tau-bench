# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class FlagPantryStaplesOnList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
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
            item["pantry_staple_flag"] = bool((ingr or {}).get("pantry_staple_flag", False))
            cnt += 1
        return _json_dump({"updated_items": cnt})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"flag_pantry_staples_on_list","description":"Set pantry_staple_flag on list items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":[]}}}
