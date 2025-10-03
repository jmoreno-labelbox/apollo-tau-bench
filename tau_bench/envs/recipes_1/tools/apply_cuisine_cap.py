from tau_bench.envs.tool import Tool
import json
from typing import Any

class ApplyCuisineCap(Tool):
    """Restrict a list of recipe_ids to a maximum of N for each cuisine."""

    @staticmethod
    def invoke(data: dict[str, Any], recipe_ids_json: str = "[]", max_per_cuisine: int = 2, exclude_recipe_ids: Any = None) -> str:
        ids = _parse_json_list_ids(recipe_ids_json)
        counts: dict[str, int] = {}
        selected: list[int] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cz = str(r.get("cuisine"))
            c = counts.get(cz, 0)
            if c < max_per_cuisine:
                selected.append(rid)
                counts[cz] = c + 1
        return _json_dump({"cuisine_limited_recipe_ids_json": json.dumps(selected)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyCuisineCap",
                "description": "Apply a per-cuisine maximum to a recipe set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids_json": {"type": "string"},
                        "max_per_cuisine": {"type": "integer"},
                    },
                    "required": ["recipe_ids_json", "max_per_cuisine"],
                },
            },
        }
