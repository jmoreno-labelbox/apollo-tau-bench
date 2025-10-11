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

class GetHouseholdById(Tool):
    """Return household by household_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], household_id) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        row = _require(data, "households", "household_id", household_id)
        return _json_dump(row or {"error": f"household_id {household_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "get_household_by_id",
            "description": "Return a household row by household_id.",
            "parameters": {"type": "object", "properties": {"household_id": {"type": "integer"}}, "required": ["household_id"]}
        }}