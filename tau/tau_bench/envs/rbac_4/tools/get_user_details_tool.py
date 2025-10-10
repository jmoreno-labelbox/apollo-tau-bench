# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetailsTool(Tool):
    """Get complete user details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        for u in list(data.get("users", {}).values()):
            if u["user_id"] == uid:
                return json.dumps(u, indent=2)
        return json.dumps({"error": f"user_id {uid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get full details of a user by their user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }
