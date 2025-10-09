from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], filter_token: str = None, meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False, no_heat: Any = None) -> str:
        token = filter_token
        if token:
            meal_type, min_protein, pf = _decode_filter_token(token)
        else:
            min_protein = int(min_protein_g)
            pf = bool(peanut_free)
        out = _all_recipe_ids_filtered(data, meal_type, min_protein, pf)
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRecipesByFilters",
                "description": "List recipe_ids as JSON from a token or direct parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_token": {"type": "string"},
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                    },
                    "required": [],
                },
            },
        }
