from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_type: str,
        peanut_free: bool | None = None,
        min_protein_g: int | None = None,
        no_heat_required: bool | None = None,
        minimal_prep: bool | None = None,
        no_heat: Any = None,
        max_prep_minutes: Any = None
    ) -> str:
        filters = {
            "meal_type": meal_type,
            "peanut_free": peanut_free,
            "min_protein_g": min_protein_g,
            "no_heat_required": no_heat_required,
            "minimal_prep": minimal_prep,
        }
        # Eliminate Nones in a deterministic manner
        filters = {k: v for k, v in filters.items() if v is not None}
        payload = {"filters": filters}
        out = json.dumps(payload, indent=2)
        return out
        pass
        filters = {
            "meal_type": meal_type,
            "peanut_free": peanut_free,
            "min_protein_g": min_protein_g,
            "no_heat_required": no_heat_required,
            "minimal_prep": minimal_prep,
        }
        #Eliminate Nones in a deterministic manner
        filters = {k: v for k, v in filters.items() if v is not None}
        payload = {"filters": filters}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildRecipeFilters",
                "description": "Returns a normalized recipe filter object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_type": {"type": "string"},
                        "peanut_free": {"type": "boolean"},
                        "min_protein_g": {"type": "integer"},
                        "no_heat_required": {"type": "boolean"},
                        "minimal_prep": {"type": "boolean"},
                    },
                    "required": ["meal_type"],
                },
            },
        }
