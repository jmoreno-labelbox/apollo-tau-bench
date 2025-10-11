# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id














def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if r.get("recipe_id") == recipe_id), None)

def _parse_json_list_ids(json_str: Optional[str]) -> List[int]:
    try:
        if not json_str:
            return []
        val = json.loads(json_str)
        if isinstance(val, list) and all(isinstance(x, int) for x in val):
            return val
    except Exception:
        pass
    return []

def _latest_meal_plan_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return None
    return sorted(plans, key=lambda m: int(m.get("meal_plan_id", 0)), reverse=True)[0]

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class GenerateChildModifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids_json) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        if not ids:
            household_id = _default_household_id(data, _first_user_id(data))
            mp = _latest_meal_plan_for_household(data, household_id)
            if mp:
                ids = [int(e.get("recipe_id")) for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == mp.get("meal_plan_id")]
        notes = {}
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            base = r.get("notes") or ""
            add = " Child-friendly: mild seasoning; cut into bite-sized pieces."
            notes[str(rid)] = (base + add).strip()
        return _json_dump({"child_mod_notes": notes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"generate_child_modifications","description":"Return a note per recipe_id; defaults to latest meal plan entries.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"}},"required":[]}}}