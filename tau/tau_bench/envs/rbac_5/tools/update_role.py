# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRole(Tool):
    """
    Update any detail of a role in roles.json.

    kwargs:
      role_id: str (required)
      role_name: str (optional)
      description: str (optional)
      is_temporary: bool (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], description, is_temporary, role_name, role_id = "") -> str:

        if not role_id:
            return json.dumps({"error": "role_id is required"})

        roles = list(data.get("roles", {}).values())
        role_index = None
        for i, role in enumerate(roles):
            if role.get("role_id") == role_id:
                role_index = i
                break

        if role_index is None:
            return json.dumps({"error": f"role_id {role_id} not found"})

        updated_role = dict(roles[role_index])
        if role_name is not None:
            updated_role["role_name"] = role_name
        if description is not None:
            updated_role["description"] = description
        if is_temporary is not None:
            updated_role["is_temporary"] = is_temporary

        data["roles"][role_index] = updated_role
        return json.dumps({"ok": True, "role": updated_role})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_role",
                "description": "Update any detail of a role in roles.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Role identifier (e.g., ROL-001)."},
                        "role_name": {"type": "string", "description": "New role name (optional)."},
                        "description": {"type": "string", "description": "New description (optional)."},
                        "is_temporary": {"type": "boolean", "description": "Set if role is temporary (optional)."}
                    },
                    "required": ["role_id"],
                    "additionalProperties": False
                }
            }
        }
