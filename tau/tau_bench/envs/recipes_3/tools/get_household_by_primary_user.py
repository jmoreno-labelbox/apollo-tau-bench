from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetHouseholdByPrimaryUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: int) -> str:
        households = _get_table(data, "households")
        hh = next((h for h in households if h.get("primary_user_id") == user_id), None)
        payload = {"household": hh}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdByPrimaryUser",
                "description": "Returns the household where primary_user_id matches user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }
