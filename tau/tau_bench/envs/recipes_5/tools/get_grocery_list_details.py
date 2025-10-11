# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id












def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _ensure_list_id(data: Dict[str, Any], list_id: int) -> Dict[str, Any]:
    for gl in data.get("grocery_lists", []):
        if gl.get("list_id") == list_id:
            return gl
    return {}

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class GetGroceryListDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id) -> str:
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