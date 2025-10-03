from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class RankRecipesForTargets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        needed_count: int = 7,
        member_id: str = None,
        target_calories: int = None,
        target_protein: int = None, recipe_ids_json: Any = None) -> str:
        ids = _ids_from_kwargs_or_defaults(data, {
            "needed_count": needed_count,
            "member_id": member_id,
            "target_calories": target_calories,
            "target_protein": target_protein
        })
        if target_calories is None or target_protein is None:
            tc2, tp2 = _pick_target_from_member(data, member_id)
            target_calories = int(target_calories if target_calories is not None else tc2)
            target_protein = int(target_protein if target_protein is not None else tp2)
        else:
            target_calories = int(target_calories)
            target_protein = int(target_protein)
        scored: list[tuple[float, int]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            dc = abs(int(r.get("calories_per_serving", 0)) - target_calories)
            dp = abs(int(r.get("protein_g_per_serving", 0)) - target_protein)
            score = float(dc) + float(dp) * 10.0
            scored.append((score, rid))
        picked = [
            rid for _, rid in sorted(scored, key=lambda x: (x[0], x[1]))[:needed_count]
        ]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RankRecipesForTargets",
                "description": "Select up to N recipes closest to nutrition targets; targets default from a household member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "filter_token": {"type": "string"},
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "needed_count": {"type": "integer"},
                        "target_calories": {"type": "integer"},
                        "target_protein": {"type": "integer"},
                        "member_id": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
