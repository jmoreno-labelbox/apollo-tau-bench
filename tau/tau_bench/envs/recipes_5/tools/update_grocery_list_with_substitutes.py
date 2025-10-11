# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _latest_list_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    lists_ = [l for l in data.get("grocery_lists", []) if l.get("household_id") == household_id]
    if not lists_:
        return None
    return sorted(lists_, key=lambda l: int(l.get("list_id", 0)), reverse=True)[0]

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _latest_list_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    gl = _latest_list_for_household(data, household_id)
    return int(gl["list_id"]) if gl else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _ingredient_by_id(data: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next((i for i in data.get("ingredients", []) if i.get("ingredient_id") == ingredient_id), None)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class UpdateGroceryListWithSubstitutes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id, substitutions = []) -> str:
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None:
            return _json_dump({"updated_items": 0})
        replaced = 0
        mapping = {int(s["ingredient_id"]): int(s["substitute_ingredient_id"]) for s in substitutions if "ingredient_id" in s and "substitute_ingredient_id" in s}
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            old = int(item.get("ingredient_id"))
            if old in mapping:
                new_ing_id = mapping[old]
                item["ingredient_id"] = new_ing_id
                ing = _ingredient_by_id(data, new_ing_id)
                item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                replaced += 1
        return _json_dump({"updated_items": replaced})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_grocery_list_with_substitutes","description":"Replace ingredient_id for grocery items; defaults to latest list.","parameters":{"type":"object","properties":{"list_id":{"type":"integer"},"substitutions":{"type":"array","items":{"type":"object"}}},"required":[]}}}