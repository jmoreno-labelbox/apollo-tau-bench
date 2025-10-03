from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateUserAddress(Tool):
    """Modify a user's address to the supplied fields."""

    @staticmethod
    def invoke(data, user_id=None, address=None) -> str:
        if not user_id or not isinstance(address, dict):
            payload = {"error": "user_id and address (object) are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        user = _find_user(data, user_id)
        if not user:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        user["address"] = address
        payload = {"success": True, "user_id": user_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateUserAddress",
                "description": "Replace a user's address with the provided object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["user_id", "address"],
                },
            },
        }
