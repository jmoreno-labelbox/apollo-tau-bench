# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUser(Tool):
    """
    Update user information like department, status, or name.

    Also supports name changes by accepting first_name and/or last_name independently,
    which will deterministically update the username and corporate email using the
    convention:
      - username: <first_initial><last_name> (lowercase, alphanumeric)
      - email: <first_name>.<last_name>@taucorp.com (lowercase, alphanumeric in local-part)

    kwargs:
      user_id: str (required)
      department: str (optional)
      status: str (optional)
      mfa_enabled: bool (optional)
      first_name: str (optional; can be provided independently)
      last_name: str (optional; can be provided independently)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        department = kwargs.get("department")
        status = kwargs.get("status")
        mfa_enabled = kwargs.get("mfa_enabled")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")

        if not user_id:
            return json.dumps({"error": "user_id is required"})

        # Find the user
        users = list(data.get("users", {}).values())
        user_index = None
        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_index = i
                break

        if user_index is None:
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Update the user
        updated_user = dict(users[user_index])
        if department is not None:
            updated_user["department"] = department
        if status is not None:
            updated_user["status"] = status
        if mfa_enabled is not None:
            updated_user["mfa_enabled"] = mfa_enabled

        # Handle name change -> update username and email deterministically
        if (first_name is not None) or (last_name is not None):
            # Get current user data to use existing name components if not provided
            current_user = users[user_index]
            current_email = current_user.get("email", "")

            # If current email follows the pattern first.last@taucorp.com, extract names
            if "@taucorp.com" in current_email:
                local_part = current_email.split("@")[0]
                if "." in local_part:
                    current_first, current_last = local_part.split(".", 1)
                else:
                    # Fallback: try to extract from username (first_initial + last_name)
                    current_username = current_user.get("username", "")
                    if len(current_username) >= 2:
                        current_first = current_username[0]
                        current_last = current_username[1:]
                    else:
                        current_first = current_last = ""
            else:
                current_first = current_last = ""

            # Use provided names or fall back to current names
            effective_first = first_name if first_name is not None else current_first
            effective_last = last_name if last_name is not None else current_last

            if not effective_first or not effective_last:
                return json.dumps({"error": "Cannot determine both first and last name for username/email generation"})

            # Normalize names: lowercase alphanumerics only for id parts
            def _norm(s: str) -> str:
                s = (s or "").strip().lower()
                return "".join(ch for ch in s if ch.isalnum())

            fn = _norm(effective_first)
            ln = _norm(effective_last)
            if not fn or not ln:
                return json.dumps({"error": "first_name and last_name must contain at least one alphanumeric character"})

            new_username = f"{fn[0]}{ln}"
            new_email_local = f"{fn}.{ln}"
            new_email = f"{new_email_local}@taucorp.com"

            # Ensure username uniqueness (excluding current user)
            for u in users:
                if u.get("user_id") == user_id:
                    continue
                if str(u.get("username", "")).strip().lower() == new_username:
                    return json.dumps({"error": f"username {new_username} already exists"})

            updated_user["username"] = new_username
            updated_user["email"] = new_email

        data["users"][user_index] = updated_user
        return json.dumps({"ok": True, "user": updated_user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user",
                "description": "Update user information like department, status, or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User identifier (e.g., U-001)."},
                        "department": {"type": "string", "description": "New department for the user."},
                        "status": {"type": "string", "description": "New status for the user."},
                        "mfa_enabled": {"type": "boolean", "description": "Enable/disable MFA for user."},
                        "first_name": {"type": "string", "description": "New legal first name (can be provided independently to update username/email)."},
                        "last_name": {"type": "string", "description": "New legal last name (can be provided independently to update username/email)."}
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }
            }
        }
