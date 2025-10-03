from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [
            m for m in data.get("members", []) if m.get("household_id") == household_id
        ]
        return _json_dump(rows)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListHouseholdMembers",
                "description": "List members for a household; household defaults if omitted.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
