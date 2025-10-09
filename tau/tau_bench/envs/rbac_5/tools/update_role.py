from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateRole(Tool):
    """
    Modify any aspect of a role in roles.json.

    kwargs:
      role_id: str (mandatory)
      role_name: str (optional)
      description: str (optional)
      is_temporary: bool (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = "", role_name: str = None, description: str = None, is_temporary: bool = None) -> str:
        if not role_id:
            payload = {"error": "role_id is required"}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", {}).values()
        role_index = None
        for i, role in enumerate(roles.values()):
            if role.get("role_id") == role_id:
                role_index = i
                break

        if role_index is None:
            payload = {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        updated_role = dict(roles[role_index])
        if role_name is not None:
            updated_role["role_name"] = role_name
        if description is not None:
            updated_role["description"] = description
        if is_temporary is not None:
            updated_role["is_temporary"] = is_temporary

        data["roles"][role_index] = updated_role
        payload = {"ok": True, "role": updated_role}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRole",
                "description": "Update any detail of a role in roles.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Role identifier (e.g., ROL-001).",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "New role name (optional).",
                        },
                        "description": {
                            "type": "string",
                            "description": "New description (optional).",
                        },
                        "is_temporary": {
                            "type": "boolean",
                            "description": "Set if role is temporary (optional).",
                        },
                    },
                    "required": ["role_id"],
                    "additionalProperties": False,
                },
            },
        }
