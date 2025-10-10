# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CategorizeGroceryListSections(Tool):
    """Refresh grocery_section for all items in a list from ingredient definitions."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        updated = 0
        for item in list(data.get("grocery_list_items", {}).values()):
            if int(item.get("list_id")) != int(list_id):
                continue
            ing = _ingredient_by_id(data, int(item.get("ingredient_id")))
            item["grocery_section"] = (ing or {}).get("grocery_section", "Misc")
            updated += 1
        return _json_dump({"updated_items": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"categorize_grocery_list_sections",
            "description":"Set grocery_section on each item in a list from ingredients table.",
            "parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":["list_id"]}
        }}
