# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class GetGroceryListDetails(Tool):
    """Return grocery_list header and all items for list_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        header = _require(data, "grocery_lists", "list_id", int(list_id))
        if not header:
            return _json_dump({"error": f"list_id {list_id} not found"})
        items = [i for i in list(data.get("grocery_list_items", {}).values()) if int(i.get("list_id")) == int(list_id)]
        return _json_dump({"grocery_list": header, "items": items})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_grocery_list_details",
            "description":"Get a grocery_list header plus items.",
            "parameters":{"type":"object","properties":{"list_id":{"type":"integer"}},"required":["list_id"]}
        }}
