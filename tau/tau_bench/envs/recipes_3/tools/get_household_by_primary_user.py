# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdByPrimaryUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: int) -> str:
        hh = next(
            (
                h
                for h in data.get("households", [])
                if int(h.get("primary_user_id")) == int(user_id)
            ),
            None,
        )
        return _json({"household": hh})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_primary_user",
                "description": "Retrieve household row where primary_user_id == user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "integer"}},
                    "required": ["user_id"],
                },
            },
        }
