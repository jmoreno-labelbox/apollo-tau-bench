from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class GetHouseholdByUserId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if user_id is None:
            user_id = _first_user_id(data)
        hh = _household_for_user(data, user_id)
        if not hh:
            return _json_dump({"error": "no households available"})
        return _json_dump(hh)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdByUserId",
                "description": "Get household for user_id; defaults to the first household if unspecified.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": [],
                },
            },
        }
