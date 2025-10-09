from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GenerateChildModifications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = None) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        if not ids:
            household_id = _default_household_id(data, _first_user_id(data))
            mp = _latest_meal_plan_for_household(data, household_id)
            if mp:
                ids = [
                    int(e.get("recipe_id"))
                    for e in data.get("meal_plan_entries", [])
                    if e.get("meal_plan_id") == mp.get("meal_plan_id")
                ]
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateChildModifications",
                "description": "Return a note per recipe_id; defaults to latest meal plan entries.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_ids_json": {"type": "string"}},
                    "required": [],
                },
            },
        }
