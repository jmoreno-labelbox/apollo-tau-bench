from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False,
        no_heat: Any = None,
        max_prep_minutes: Any = None,
    ) -> str:
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}"
        return _json_dump({"filter_token": token})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildRecipeFilters",
                "description": "Construct a filter token; defaults to Dinner with no protein minimum.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                    },
                    "required": [],
                },
            },
        }
