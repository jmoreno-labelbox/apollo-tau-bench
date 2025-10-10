# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListHouseholdMembers(Tool):
    """List all members for a household."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        rows = [m for m in list(data.get("members", {}).values()) if int(m.get("household_id")) == int(household_id)]
        return _json_dump(rows)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_household_members",
            "description": "List all members belonging to a household.",
            "parameters": {"type": "object", "properties": {"household_id": {"type": "integer"}}, "required": ["household_id"]}
        }}
