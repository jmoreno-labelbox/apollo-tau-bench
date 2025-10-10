# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        meal_type: str,
        min_protein_g: int = 0,
        peanut_free: bool = False,
        cuisines_exclude: Optional[List[str]] = None,
    ) -> str:
        ex = ",".join(sorted((cuisines_exclude or [])))
        token = f"F:{meal_type}:P{int(min_protein_g)}:PF{1 if peanut_free else 0}:EX{ex}"
        return json.dumps({"filter_token": token})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_recipe_filters",
                "description": "Construct a deterministic filter token for recipes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "cuisines_exclude": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["meal_type"],
                },
            },
        }
