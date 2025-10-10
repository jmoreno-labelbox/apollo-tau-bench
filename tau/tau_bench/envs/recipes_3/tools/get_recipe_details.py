# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRecipeDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_id: int) -> str:
        return json.dumps({"recipe": _recipe_by_id(data, int(recipe_id))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_recipe_details",
                "description": "Get recipe row by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"recipe_id": {"type": "integer"}},
                    "required": ["recipe_id"],
                },
            },
        }
