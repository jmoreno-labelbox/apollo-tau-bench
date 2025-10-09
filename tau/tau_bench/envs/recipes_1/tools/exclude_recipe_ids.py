from tau_bench.envs.tool import Tool
import json
from typing import Any

class ExcludeRecipeIds(Tool):
    """Eliminate any recipe_ids found in a given exclusion list."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_recipe_ids_json: str = "[]", ExcludeRecipeIds: list = None,
    exclude_recipe_ids: Any = None,
    ) -> str:
        candidates_json = candidate_recipe_ids_json
        exclude_ids = ExcludeRecipeIds or []
        cand = _parse_json_list_ids(candidates_json)
        exset = {int(x) for x in exclude_ids}
        out = [rid for rid in cand.values() if rid not in exset]
        return _json_dump({"filtered_recipe_ids_json": json.dumps(out)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExcludeRecipeIds",
                "description": "Return candidates minus provided recipe_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_recipe_ids_json": {"type": "string"},
                        "ExcludeRecipeIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                    },
                    "required": ["candidate_recipe_ids_json", "ExcludeRecipeIds"],
                },
            },
        }
