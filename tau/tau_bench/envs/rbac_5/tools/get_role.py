# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRole(Tool):
    """
    Fetch a role by role_id or role_name.

    kwargs:
      role_id: str (optional) - Role identifier (e.g., ROL-001)
      role_name: str (optional) - Human-readable role name (case-insensitive)

    Note: Provide either role_id OR role_name, not both.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        role_name = kwargs.get("role_name")

        # Validate that exactly one parameter is provided
        if not role_id and not role_name:
            return json.dumps({"error": "Must provide either role_id or role_name"})

        if role_id and role_name:
            return json.dumps({"error": "Provide either role_id OR role_name, not both"})

        roles = list(data.get("roles", {}).values())

        # Search by role_id
        if role_id:
            role = _find_by_id(roles, "role_id", role_id)
            return json.dumps(role or {"error": f"role_id {role_id} not found"})

        # Search by role_name (case-insensitive)
        if role_name:
            name_lower = role_name.strip().lower()
            for r in roles:
                if str(r.get("role_name", "")).strip().lower() == name_lower:
                    return json.dumps(r)
            return json.dumps({"error": f"role_name '{role_name}' not found"})

        return json.dumps({"error": "Invalid parameters"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role",
                "description": "Fetch a role by role_id or role_name (case-insensitive match). Provide exactly one parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "Role identifier (e.g., ROL-001)."},
                        "role_name": {"type": "string", "description": "Human-readable role name (case-insensitive)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
