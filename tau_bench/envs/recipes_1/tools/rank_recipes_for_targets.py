from tau_bench.envs.tool import Tool
import json
from typing import Any

class RankRecipesForTargets(Tool):
    """Evaluate recipes based on proximity to (target_calories, target_protein); a lower score is preferable."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids_json: str = "[]",
        target_calories: int = 2000,
        target_protein: int = 100,
        needed_count: int = 7
    ) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        scored: list[tuple[float, int, float]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cal = int(r.get("calories_per_serving", 0))
            prot = int(r.get("protein_g_per_serving", 0))
            dev = abs(cal - target_calories) / max(1, target_calories) + 10.0 * abs(
                prot - target_protein
            ) / max(1, target_protein)
            scored.append((dev, rid, float(prot)))
        picked = [
            rid
            for _, rid, _ in sorted(scored, key=lambda x: (x[0], -x[2], x[1]))[
                :needed_count
            ]
        ]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RankRecipesForTargets",
                "description": "Select up to N recipes closest to nutrition targets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "target_calories": {"type": "integer"},
                        "target_protein": {"type": "integer"},
                    },
                    "required": [
                        "recipe_ids_json",
                        "needed_count",
                        "target_calories",
                        "target_protein",
                    ],
                },
            },
        }
