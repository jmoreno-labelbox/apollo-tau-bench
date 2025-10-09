from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        household_id: int = None, 
        recent_recipe_ids: list[int] = None, 
        days_back: int = 14, 
        anchor_date: str = None
,
    candidate_recipe_ids_json: Any = None,
    ) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        cand = _ids_from_kwargs_or_defaults(data, {
            "household_id": household_id,
            "recent_recipe_ids": recent_recipe_ids,
            "days_back": days_back,
            "anchor_date": anchor_date
        })
        recent = recent_recipe_ids
        if recent is None:
            recent = _recent_recipe_ids(data, household_id, days_back, anchor_date)
        filtered = [rid for rid in cand.values() if rid not in {int(x) for x in recent}]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(filtered)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "excludeRecentRecipes",
                "description": "Remove recipes that appeared in recent history; defaults to last 14 days for default household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_recipe_ids_json": {"type": "string"},
                        "filter_token": {"type": "string"},
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "recent_recipe_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "household_id": {"type": "integer"},
                        "days_back": {"type": "integer"},
                        "anchor_date": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
