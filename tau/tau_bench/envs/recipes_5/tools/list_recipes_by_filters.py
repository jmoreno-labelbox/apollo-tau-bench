# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class ListRecipesByFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        token = kwargs.get("filter_token")
        if token:
            meal_type, min_protein, pf = _decode_filter_token(token)
        else:
            meal_type = kwargs.get("meal_type", "Dinner")
            min_protein = int(kwargs.get("min_protein_g", 0))
            pf = bool(kwargs.get("peanut_free", False))
        out = _all_recipe_ids_filtered(data, meal_type, min_protein, pf)
        return _json_dump({"candidate_recipe_ids_json": json.dumps(out)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_recipes_by_filters","description":"List recipe_ids as JSON from a token or direct parameters.","parameters":{"type":"object","properties":{"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"}},"required":[]}}}
