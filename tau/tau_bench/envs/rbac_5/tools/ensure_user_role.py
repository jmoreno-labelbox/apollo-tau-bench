# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnsureUserRole(Tool):
    """
    Ensure a user has a role; idempotent assignment.

    kwargs:
      user_id: str (required)
      role_id: str (required)
      assigned_by: str (required)
      assigned_on: str ISO (defaults now)
      expires_on: str ISO (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        role_id = kwargs.get("role_id", "")
        assigned_by = kwargs.get("assigned_by", "")
        assigned_on = kwargs.get("assigned_on") or get_current_timestamp()
        expires_on = kwargs.get("expires_on")

        # Existence checks
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})
        if not _find_by_id(list(data.get("roles", {}).values()), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})

        assignments = data.get("user_roles", [])
        existing = None
        existing_index = None
        for i, ur in enumerate(assignments):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing = ur
                existing_index = i
                break

        if existing:
            # If expires_on is provided and different from existing, update it
            if expires_on and existing.get("expires_on") != expires_on:
                updated = dict(existing)
                updated["expires_on"] = expires_on
                data["user_roles"][existing_index] = updated
                return json.dumps({"ok": True, "assignment": updated, "updated_expiry": True})
            else:
                return json.dumps({"ok": True, "no_op": True, "assignment": existing})
        else:
            # nothing to update/ensure
            return json.dumps({"error": "no existing assignment found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_user_role",
                "description": "Idempotently ensure a user has a role with optional expiry. Updates expiry date if role exists and new expires_on is provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "assigned_by": {"type": "string", "description": "Actor user_id performing assignment."},
                        "assigned_on": {"type": "string", "description": "ISO timestamp of assignment."},
                        "expires_on": {"type": "string", "description": "ISO timestamp for expiry (optional)."}
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                    "additionalProperties": False
                }
            }
        }
