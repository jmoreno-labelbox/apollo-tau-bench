from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRoleDetailsById(Tool):
    """Locate a specific role by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            roles = data.get("roles", [])
        except:
            roles = []

        for role in roles:
            if role.get("role_id") == role_id:
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": f"Role with ID '{role_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleDetailsById",
                "description": "Retrieves the full details of a specific role by providing its unique role_id (e.g., 'ROL-013').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique identifier of the role to retrieve (e.g., 'ROL-011').",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
