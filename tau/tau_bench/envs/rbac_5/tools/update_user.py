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
    def invoke(data: Dict[str, Any], department, first_name, last_name, mfa_enabled, status, user_id = "") -> str:

        if not user_id:
            return json.dumps({"error": "user_id is required"})

        # Locate the user.
        users = list(data.get("users", {}).values())
        user_index = None
        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_index = i
                break

        if user_index is None:
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Notify the user.
        updated_user = dict(users[user_index])
        if department is not None:
            updated_user["department"] = department
        if status is not None:
            updated_user["status"] = status
        if mfa_enabled is not None:
            updated_user["mfa_enabled"] = mfa_enabled

        # Manage name modification -> consistently update username and email.
        if (first_name is not None) or (last_name is not None):
            # Retrieve the current user information to utilize existing name elements if they are not supplied.
            current_user = users[user_index]
            current_email = current_user.get("email", "")

            # Extract names if the current email format is first.last@taucorp.com.
            if "@taucorp.com" in current_email:
                local_part = current_email.split("@")[0]
                if "." in local_part:
                    current_first, current_last = local_part.split(".", 1)
                else:
                    # Alternative method: attempt to derive from username (first_initial + last_name)
                    current_username = current_user.get("username", "")
                    if len(current_username) >= 2:
                        current_first = current_username[0]
                        current_last = current_username[1:]
                    else:
                        current_first = current_last = ""
            else:
                current_first = current_last = ""

            # Utilize the specified names or revert to the existing names.
            effective_first = first_name if first_name is not None else current_first
            effective_last = last_name if last_name is not None else current_last

            if not effective_first or not effective_last:
                return json.dumps({"error": "Cannot determine both first and last name for username/email generation"})

            # Standardize names: use only lowercase alphanumeric characters for identifier segments.
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

            # Verify that the username is unique, disregarding the current user.
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
