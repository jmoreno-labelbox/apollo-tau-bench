from tau_bench.envs.tool import Tool
import json
from typing import Any

class ExcludeRecentRecipes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        recipe_ids: list[int],
        recent_history: list[dict[str, Any]]
,
    candidate_recipe_ids_json: Any = None,
    ) -> str:
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        kept = [rid for rid in (recipe_ids or []) if rid not in recent_set]
        payload = {"filtered": kept}
        out = json.dumps(payload, indent=2)
        return out
        pass
        recent_set = {row.get("recipe_id") for row in (recent_history or [])}
        kept = [rid for rid in (recipe_ids or []) if rid not in recent_set]
        payload = {"filtered": kept}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "excludeRecentRecipes",
                "description": "Filters out recipe_ids that appear in recent meal_history rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "recent_history": {"type": "array"},
                    },
                    "required": ["recipe_ids", "recent_history"],
                },
            },
        }
