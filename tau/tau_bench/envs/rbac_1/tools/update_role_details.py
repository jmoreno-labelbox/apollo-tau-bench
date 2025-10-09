from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateRoleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, new_name: str = None, new_description: str = None) -> str:
        for role in data.get("roles", []):
            if role.get("role_id") == role_id:
                if new_name:
                    role["role_name"] = new_name
                if new_description:
                    role["description"] = new_description
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": "Role not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRoleDetails",
                "description": "Updates the name and/or description of an existing role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"},
                        "new_name": {
                            "type": "string",
                            "description": "The new name for the role.",
                        },
                        "new_description": {
                            "type": "string",
                            "description": "The new description for the role.",
                        },
                    },
                    "required": ["role_id"],
                },
            },
        }
