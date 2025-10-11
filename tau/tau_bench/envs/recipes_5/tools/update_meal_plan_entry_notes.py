# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id












def _latest_meal_plan_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    mp = _latest_meal_plan_for_household(data, household_id)
    return int(mp["meal_plan_id"]) if mp else None

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = _parse_json_list_ids(kwargs.get("recipe_ids_json"))
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

class UpdateMealPlanEntryNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], meal_plan_id, notes_map) -> str:
        if meal_plan_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            meal_plan_id = _latest_meal_plan_id(data, household_id)
        if notes_map is None:
            rec_ids = [int(e.get("recipe_id")) for e in data.get("meal_plan_entries", []) if e.get("meal_plan_id") == meal_plan_id]
            gen = json.loads(GenerateChildModifications.invoke(data, recipe_ids_json=json.dumps(rec_ids)))["child_mod_notes"]
            notes_map = gen
        updated = 0
        for e in data.get("meal_plan_entries", []):
            if e.get("meal_plan_id") != meal_plan_id:
                continue
            rid = str(e.get("recipe_id"))
            if rid in notes_map:
                e["notes"] = notes_map[rid]
                updated += 1
        return _json_dump({"updated_entries": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_meal_plan_entry_notes","description":"Set notes for entries; defaults to child-friendly notes for latest plan.","parameters":{"type":"object","properties":{"meal_plan_id":{"type":"integer"},"notes_map":{"type":"object"}},"required":[]}}}