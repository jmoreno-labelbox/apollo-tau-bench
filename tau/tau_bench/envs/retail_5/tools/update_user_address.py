from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateUserAddress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, address: str = None) -> str:
        if not user_id or not address:
            payload = {"error": "user_id and address are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"].values() if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        user["address"] = address
        payload = {"success": True, "user_id": user_id, "message": "Address updated."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateUserAddress",
                "description": "Update a user's primary shipping address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to update.",
                        },
                        "address": {
                            "type": "object",
                            "description": "A complete address object.",
                        },
                    },
                    "required": ["user_id", "address"],
                },
            },
        }
