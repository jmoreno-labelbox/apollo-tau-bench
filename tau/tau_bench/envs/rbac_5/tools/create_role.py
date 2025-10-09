from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateRole(Tool):
    """
    Establish a new role with consistent ID generation.

    kwargs:
      role_name: str (mandatory)
      description: str (mandatory)
      is_temporary: bool = False (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = "", description: str = "", is_temporary: bool = False) -> str:
        role_name = role_name.strip()

        if not role_name or not description:
            payload = {"error": "role_name and description are required"}
            out = json.dumps(payload)
            return out

        # Ensure uniqueness based on role_name (case-insensitive)
        existing_roles = data.get("roles", {}).values()
        for r in existing_roles.values():
            if str(r.get("role_name", "")).strip().lower() == role_name.lower():
                payload = {"error": f"role_name '{role_name}' already exists"}
                out = json.dumps(payload)
                return out

        new_role = {
            "role_id": _next_id(data, "roles", "ROL"),
            "role_name": role_name,
            "description": description,
            "is_temporary": bool(is_temporary),
        }

        data.setdefault("roles", []).append(new_role)
        payload = {"ok": True, "role": new_role}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRole",
                "description": "Create a new role with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "Unique role name (case-insensitive).",
                        },
                        "description": {
                            "type": "string",
                            "description": "Role description.",
                        },
                        "is_temporary": {
                            "type": "boolean",
                            "description": "Whether the role is temporary.",
                            "default": False,
                        },
                    },
                    "required": ["role_name", "description"],
                    "additionalProperties": False,
                },
            },
        }
