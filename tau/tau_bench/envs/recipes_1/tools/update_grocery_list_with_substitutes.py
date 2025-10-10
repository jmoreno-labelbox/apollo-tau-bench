# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class UpdateGroceryListWithSubstitutes(Tool):
    """Apply substitutions on grocery_list_items by changing ingredient_id and refreshing grocery_section."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        substitutions = kwargs.get("substitutions", [])
        if list_id is None or not isinstance(substitutions, list):
            return _json_dump({"error": "list_id and substitutions are required"})
        mapping = {int(s["ingredient_id"]): int(s["substitute_ingredient_id"])
                   for s in substitutions if "ingredient_id" in s and "substitute_ingredient_id" in s}
        updated = 0
        for it in list(data.get("grocery_list_items", {}).values()):
            if int(it.get("list_id")) != int(list_id):
                continue
            old = int(it.get("ingredient_id"))
            if old in mapping:
                new_iid = mapping[old]
                it["ingredient_id"] = new_iid
                ing = _ingredient_by_id(data, new_iid)
                it["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
                updated += 1
        return _json_dump({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_grocery_list_with_substitutes",
            "description":"Replace ingredient_ids on list items using a substitution mapping.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "substitutions":{"type":"array","items":{"type":"object"}}
            },"required":["list_id","substitutions"]}
        }}
