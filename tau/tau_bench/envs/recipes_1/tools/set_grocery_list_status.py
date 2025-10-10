# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class SetGroceryListStatus(Tool):
    """Update grocery_lists.status_enum for list_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_id = kwargs.get("list_id")
        status_enum = kwargs.get("status_enum")
        if list_id is None or not status_enum:
            return _json_dump({"error": "list_id and status_enum are required"})
        row = _require(data, "grocery_lists", "list_id", int(list_id))
        if not row:
            return _json_dump({"error": f"list_id {list_id} not found"})
        row["status_enum"] = str(status_enum)
        return _json_dump(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"set_grocery_list_status",
            "description":"Set the status of a grocery list.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "status_enum":{"type":"string"}
            },"required":["list_id","status_enum"]}
        }}
