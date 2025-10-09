from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserMfaStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, mfa_enabled: bool = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                user["mfa_enabled"] = mfa_enabled
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserMfaStatus",
                "description": "Enables or disables multi-factor authentication for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                    },
                    "required": ["user_id", "mfa_enabled"],
                },
            },
        }
