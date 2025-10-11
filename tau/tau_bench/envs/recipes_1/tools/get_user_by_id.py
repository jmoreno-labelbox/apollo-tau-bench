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

class GetUserById(Tool):
    """Return a user row by user_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if user_id is None:
            return _json_dump({"error": "user_id is required"})
        row = _require(data, "users", "user_id", user_id)
        return _json_dump(row or {"error": f"user_id {user_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "get_user_by_id",
            "description": "Return user by user_id.",
            "parameters": {"type": "object", "properties": {"user_id": {"type": "integer"}}, "required": ["user_id"]}
        }}