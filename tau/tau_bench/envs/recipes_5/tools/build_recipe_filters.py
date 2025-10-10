# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class BuildRecipeFilters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_type = kwargs.get("meal_type", "Dinner")
        min_protein_g = int(kwargs.get("min_protein_g", 0))
        peanut_free = bool(kwargs.get("peanut_free", False))
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}"
        return _json_dump({"filter_token": token})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_recipe_filters","description":"Construct a filter token; defaults to Dinner with no protein minimum.","parameters":{"type":"object","properties":{"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"}},"required":[]}}}
