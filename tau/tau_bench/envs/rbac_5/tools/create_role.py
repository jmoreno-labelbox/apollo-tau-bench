# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRole(Tool):
    """
    Create a new role with deterministic ID generation.

    kwargs:
      role_name: str (required)
      description: str (required)
      is_temporary: bool = False (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_name = (kwargs.get("role_name", "") or "").strip()
        description = kwargs.get("description", "")
        is_temporary = kwargs.get("is_temporary", False)

        if not role_name or not description:
            return json.dumps({"error": "role_name and description are required"})

        # Ensure role_name is unique (ignoring case).
        existing_roles = list(data.get("roles", {}).values())
        for r in existing_roles:
            if str(r.get("role_name", "")).strip().lower() == role_name.lower():
                return json.dumps({"error": f"role_name '{role_name}' already exists"})

        new_role = {
            "role_id": _next_id(data, "roles", "ROL"),
            "role_name": role_name,
            "description": description,
            "is_temporary": bool(is_temporary),
        }

        data.setdefault("roles", []).append(new_role)
        return json.dumps({"ok": True, "role": new_role})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_role",
                "description": "Create a new role with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {"type": "string", "description": "Unique role name (case-insensitive)."},
                        "description": {"type": "string", "description": "Role description."},
                        "is_temporary": {"type": "boolean", "description": "Whether the role is temporary.", "default": False}
                    },
                    "required": ["role_name", "description"],
                    "additionalProperties": False
                }
            }
        }
