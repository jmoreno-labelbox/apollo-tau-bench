from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildRecipeFilters(Tool):
    """
    Construct a compact token that encodes filters:
      token = "F:<meal_type>:P<min_protein>:PF<0|1>:EX<csv_excluded_cuisines>"
    """

    @staticmethod
    def invoke(data: dict[str, Any], meal_type: str = "Dinner", min_protein_g: int = 0, peanut_free: bool = False, cuisines_exclude: list = None,
        no_heat: Any = None,
        max_prep_minutes: Any = None,
    ) -> str:
        if cuisines_exclude is None:
            cuisines_exclude = []
        if not isinstance(cuisines_exclude, list):
            cuisines_exclude = []
        ex = ",".join(sorted(str(c) for c in cuisines_exclude)
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}:EX{ex}"
        return _json_dump({"filter_token": token})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildRecipeFilters",
                "description": "Construct a compact string token that encodes recipe filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "min_protein_g": {"type": "integer"},
                        "peanut_free": {"type": "boolean"},
                        "cuisines_exclude": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["meal_type"],
                },
            },
        }
