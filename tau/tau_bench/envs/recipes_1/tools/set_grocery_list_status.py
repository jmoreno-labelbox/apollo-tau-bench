# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require, _json_dump






def _require(data: Dict[str, Any], table: str, key: str, value: Any) -> Optional[Dict[str, Any]]:
    row = next((r for r in data.get(table, []) if r.get(key) == value), None)
    return row

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class SetGroceryListStatus(Tool):
    """Update grocery_lists.status_enum for list_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id, status_enum) -> str:
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