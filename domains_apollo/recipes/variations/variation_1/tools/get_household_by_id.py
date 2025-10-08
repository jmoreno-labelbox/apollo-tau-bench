from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetHouseholdById(Tool):
    """Retrieve household using household_id."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            return _json_dump({"error": "household_id is required"})
        row = _require(data, "households", "household_id", household_id)
        return _json_dump(row or {"error": f"household_id {household_id} not found"})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdById",
                "description": "Return a household row by household_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
