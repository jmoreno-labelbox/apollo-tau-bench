from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class ApplyCuisineLimit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], max_per_cuisine: int = 2, candidate_recipe_ids_json: Any = None,
    recipe_ids_json: Any = None,
    ) -> str:
        ids = _ids_from_kwargs_or_defaults(data, {"max_per_cuisine": max_per_cuisine})
        cuisine_counts: dict[str, int] = {}
        selected: list[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = r.get("cuisine", "Unknown")
            cnt = cuisine_counts.get(cz, 0)
            if cnt < max_per_cuisine:
                selected.append(rid)
                cuisine_counts[cz] = cnt + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyCuisineLimit",
                "description": "Limit a list of recipes to at most N per cuisine; defaults to 2 and Dinner pool if none provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "filter_token": {"type": "string"},
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "max_per_cuisine": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
