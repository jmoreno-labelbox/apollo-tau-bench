from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: int) -> str:
        members = _get_table(data, "members")
        rows = [m for m in members if m.get("household_id") == household_id]
        payload = {"members": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": "Lists all member rows for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
