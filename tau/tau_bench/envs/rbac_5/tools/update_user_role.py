# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserRole(Tool):
    """
    Add or remove a user role assignment.

    kwargs:
      user_id: str (required)
      role_id: str (required)
      action: str = "ADD" | "REMOVE" (required)
      assigned_by: str (required for ADD)
      assigned_on: str ISO (optional for ADD, defaults now)
      expires_on: str ISO (optional for ADD)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], assigned_on, expires_on, action = "", assigned_by = "", role_id = "", user_id = "") -> str:
        action = (action or "").upper()
        assigned_on = assigned_on or get_current_timestamp()

        if action not in ("ADD", "REMOVE"):
            return json.dumps({"error": "action must be ADD or REMOVE"})

        # Presence validations
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})
        if not _find_by_id(list(data.get("roles", {}).values()), "role_id", role_id):
            return json.dumps({"error": f"role_id {role_id} not found"})

        assignments = data.get("user_roles", [])
        existing_index = None
        for i, ur in enumerate(assignments):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                existing_index = i
                break

        if action == "ADD":
            if not assigned_by:
                return json.dumps({"error": "assigned_by is required for ADD action"})

            if existing_index is not None:
                # Revise the current assignment.
                existing = assignments[existing_index]
                updated = dict(existing)
                if expires_on and existing.get("expires_on") != expires_on:
                    updated["expires_on"] = expires_on
                    data["user_roles"][existing_index] = updated
                    return json.dumps({"ok": True, "assignment": updated, "updated_expiry": True})
                else:
                    return json.dumps({"ok": True, "no_op": True, "assignment": existing})
            else:
                # Generate a new task.
                new_ur = {
                    "user_role_id": _next_user_role_id(data, user_id),
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": assigned_on,
                    "expires_on": expires_on,
                }
                data.setdefault("user_roles", []).append(new_ur)
                return json.dumps({"ok": True, "assignment": new_ur, "action": "created"})

        elif action == "REMOVE":
            if existing_index is not None:
                removed = data["user_roles"].pop(existing_index)
                removed["assigned_by"] = assigned_by
                return json.dumps({"ok": True, "assignment": removed, "action": "removed"})
            else:
                return json.dumps({"ok": True, "no_op": True, "message": "Role assignment does not exist"})
        else:
            return json.dumps({"error": "Invalid action"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_role",
                "description": "Add or remove a user role assignment. For ADD: creates new assignment or updates expiry if exists. For REMOVE: deletes the assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id."},
                        "role_id": {"type": "string", "description": "Target role_id."},
                        "action": {"type": "string", "enum": ["ADD", "REMOVE"], "description": "Action to perform."},
                        "assigned_by": {"type": "string", "description": "Actor user_id performing assignment (required)."},
                        "assigned_on": {"type": "string", "description": "ISO timestamp of assignment (optional for ADD)."},
                        "expires_on": {"type": "string", "description": "ISO timestamp for expiry (optional for ADD)."}
                    },
                    "required": ["user_id", "role_id", "action", "assigned_by"],
                    "additionalProperties": False
                }
            }
        }
