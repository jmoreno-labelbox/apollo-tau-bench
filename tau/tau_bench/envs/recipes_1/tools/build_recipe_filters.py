# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildRecipeFilters(Tool):
    """
    Build a compact token encoding filters:
      token = "F:<meal_type>:P<min_protein>:PF<0|1>:EX<csv_excluded_cuisines>"
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        meal_type = kwargs.get("meal_type", "Dinner")
        min_protein_g = int(kwargs.get("min_protein_g", 0))
        peanut_free = bool(kwargs.get("peanut_free", False))
        cuisines_exclude = kwargs.get("cuisines_exclude", [])
        if not isinstance(cuisines_exclude, list):
            cuisines_exclude = []
        ex = ",".join(sorted(str(c) for c in cuisines_exclude))
        token = f"F:{meal_type}:P{min_protein_g}:PF{1 if peanut_free else 0}:EX{ex}"
        return _json_dump({"filter_token": token})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function":{
            "name":"build_recipe_filters",
            "description":"Construct a compact string token that encodes recipe filters.",
            "parameters":{"type":"object","properties":{
                "meal_type":{"type":"string"},
                "min_protein_g":{"type":"integer"},
                "peanut_free":{"type":"boolean"},
                "cuisines_exclude":{"type":"array","items":{"type":"string"}}
            },"required":["meal_type"]}
        }}
