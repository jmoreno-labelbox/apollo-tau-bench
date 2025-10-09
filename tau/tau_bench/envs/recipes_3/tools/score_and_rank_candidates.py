from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScoreAndRankCandidates(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], recipe_ids: list[int], targets: dict[str, Any], no_heat: Any = None) -> str:
        pass
        # Deterministic ranking: prioritize higher protein, then lower calories, followed by ascending recipe_id
        recipes = _get_table(data, "recipes")
        subset = [r for r in recipes.values() if r.get("recipe_id") in (recipe_ids or [])]
        ranked = sorted(
            subset,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        payload = {"ranked": [r.get("recipe_id") for r in ranked]}
        out = json.dumps(payload, indent=2)
        return out
        pass
        #Deterministic ranking: prioritize higher protein, then lower calories, followed by ascending recipe_id
        recipes = _get_table(data, "recipes")
        subset = [r for r in recipes.values() if r.get("recipe_id") in (recipe_ids or [])]
        ranked = sorted(
            subset,
            key=lambda r: (
                -(r.get("protein_g_per_serving") or 0),
                (r.get("calories_per_serving") or 0),
                r.get("recipe_id"),
            ),
        )
        payload = {"ranked": [r.get("recipe_id") for r in ranked]}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scoreAndRankCandidates",
                "description": "Ranks candidate recipe_ids deterministically by protein desc, calories asc, id asc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "targets": {"type": "object"},
                    },
                    "required": ["recipe_ids", "targets"],
                },
            },
        }
