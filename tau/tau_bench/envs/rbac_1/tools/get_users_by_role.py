from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUsersByRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, role_name: str = None) -> str:
        if not role_id and not role_name:
            payload = {"error": "Either role_id or role_name must be provided"}
            out = json.dumps(payload)
            return out

        if role_name and not role_id:
            for role in data.get("roles", {}).values():
                if role.get("role_name") == role_name:
                    role_id = role.get("role_id")
                    break
            if not role_id:
                payload = {"error": f"Role '{role_name}' not found"}
                out = json.dumps(payload)
                return out

        user_ids = [
            ur["user_id"]
            for ur in data.get("user_roles", {}).values()
            if ur.get("role_id") == role_id
        ]
        payload = {"users": user_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersByRole",
                "description": "Retrieves all users assigned a specific role, searching by either role_id or role_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to search for.",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'operations-lead').",
                        },
                    },
                },
            },
        }
