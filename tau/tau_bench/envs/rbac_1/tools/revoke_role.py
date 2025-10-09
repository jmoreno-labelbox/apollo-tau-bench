from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RevokeRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None) -> str:
        data["user_roles"] = [
            ur
            for ur in data.get("user_roles", [])
            if not (ur.get("user_id") == user_id and ur.get("role_id") == role_id)
        ]
        payload = {"user_id": user_id, "role_id": role_id, "status": "revoked"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRole",
                "description": "Removes a role from a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }
