# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class GetHouseholdById(Tool):
    """Return household by household_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
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
