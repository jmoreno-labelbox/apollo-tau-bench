from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EnableUserMFATool(Tool):
    """Activate MFA for a specified user (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        users = data.get("users", {}).values()

        if not isinstance(user_id, str):
            payload = {"error": "user_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for u in users.values():
            if u.get("user_id") == user_id:
                u["mfa_enabled"] = True
                payload = {"success": f"MFA enabled for {user_id}", "user": u}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"User {user_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnableUserMfa",
                "description": "Enable MFA for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to enable MFA for",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
