from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRole(Tool):
    """
    Retrieve a role using role_id or role_name.

    kwargs:
      role_id: str (optional) - Identifier for the role (e.g., ROL-001)
      role_name: str (optional) - Readable name of the role (case-insensitive)

    Note: Supply either role_id OR role_name, not both.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, role_name: str = None) -> str:
        # Confirm that only one parameter is supplied
        if not role_id and not role_name:
            payload = {"error": "Must provide either role_id or role_name"}
            out = json.dumps(payload)
            return out

        if role_id and role_name:
            payload = {"error": "Provide either role_id OR role_name, not both"}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", {}).values()

        # Perform a search using role_id
        if role_id:
            role = _find_by_id(roles, "role_id", role_id)
            payload = role or {"error": f"role_id {role_id} not found"}
            out = json.dumps(payload)
            return out

        # Conduct a search using role_name (case-insensitive)
        if role_name:
            name_lower = role_name.strip().lower()
            for r in roles.values():
                if str(r.get("role_name", "")).strip().lower() == name_lower:
                    payload = r
                    out = json.dumps(payload)
                    return out
            payload = {"error": f"role_name '{role_name}' not found"}
            out = json.dumps(payload)
            return out
        payload = {"error": "Invalid parameters"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRole",
                "description": "Fetch a role by role_id or role_name (case-insensitive match). Provide exactly one parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Role identifier (e.g., ROL-001).",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "Human-readable role name (case-insensitive).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
