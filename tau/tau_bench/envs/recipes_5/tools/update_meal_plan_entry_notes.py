# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class UpdateMealPlanEntryNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_plan_id = kwargs.get("meal_plan_id")
        notes_map = kwargs.get("notes_map")
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
