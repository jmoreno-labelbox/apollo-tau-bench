# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserAddress(Tool):
    """Update user's address in users.json by user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, address: Dict[str, Any]) -> str:
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("user_id") == user_id:
                user["address"] = address
                return json.dumps({"status": "success", "user_id": user_id, "address": address})
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_address",
                "description": "Update a user's address in users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {"type": "object", "description": "Full address object with address1, address2, city, country, state, zip"}
                    },
                    "required": ["user_id", "address"]
                }
            }
        }
