from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateUser(Tool):
    """
    Modify user details such as department, status, or name.

    Also accommodates name changes by allowing first_name and/or last_name to be provided separately,
    which will deterministically adjust the username and corporate email following the
    format:
      - username: <first_initial><last_name> (lowercase, alphanumeric)
      - email: <first_name>.<last_name>@sigmatech.com (lowercase, alphanumeric in local-part)

    kwargs:
      user_id: str (mandatory)
      department: str (optional)
      status: str (optional)
      mfa_enabled: bool (optional)
      first_name: str (optional; can be provided separately)
      last_name: str (optional; can be provided separately)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        department: str = None,
        status: str = None,
        mfa_enabled: bool = None,
        first_name: str = None,
        last_name: str = None
,
    updated_by: Any = None,
    ) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        # Locate the user
        users = data.get("users", {}).values()
        user_index = None
        for i, user in enumerate(users.values():
            if user.get("user_id") == user_id:
                user_index = i
                break

        if user_index is None:
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        # Modify user details
        updated_user = dict(users[user_index])
        if department is not None:
            updated_user["department"] = department
        if status is not None:
            updated_user["status"] = status
        if mfa_enabled is not None:
            updated_user["mfa_enabled"] = mfa_enabled

        # Manage name changes by deterministically updating the username and email
        if (first_name is not None) or (last_name is not None):
            # Retrieve current user information to utilize existing name elements if not supplied
            current_user = users[user_index]
            current_email = current_user.get("email", "")

            # If the current email matches the format first.last@taucorp.com, derive names
            if "@sigmatech.com" in current_email:
                local_part = current_email.split("@")[0]
                if "." in local_part:
                    current_first, current_last = local_part.split(".", 1)
                else:
                    # Alternative: attempt to derive from username (first_initial + last_name)
                    current_username = current_user.get("username", "")
                    if len(current_username) >= 2:
                        current_first = current_username[0]
                        current_last = current_username[1:]
                    else:
                        current_first = current_last = ""
            else:
                current_first = current_last = ""

            # Utilize supplied names or revert to existing names
            effective_first = first_name if first_name is not None else current_first
            effective_last = last_name if last_name is not None else current_last

            if not effective_first or not effective_last:
                payload = {
                    "error": "Cannot determine both first and last name for username/email generation"
                }
                out = json.dumps(payload)
                return out

            # Standardize names: use only lowercase alphanumeric characters for ID segments
            def _norm(s: str) -> str:
                s = (s or "").strip().lower()
                return "".join(ch for ch in s if ch.isalnum())

            fn = _norm(effective_first)
            ln = _norm(effective_last)
            if not fn or not ln:
                payload = {
                    "error": "first_name and last_name must contain at least one alphanumeric character"
                }
                out = json.dumps(payload)
                return out

            new_username = f"{fn[0]}{ln}"
            new_email_local = f"{fn}.{ln}"
            new_email = f"{new_email_local}@sigmatech.com"

            # Guarantee username uniqueness (excluding the current user)
            for u in users.values():
                if u.get("user_id") == user_id:
                    continue
                if str(u.get("username", "")).strip().lower() == new_username:
                    payload = {"error": f"username {new_username} already exists"}
                    out = json.dumps(payload)
                    return out

            updated_user["username"] = new_username
            updated_user["email"] = new_email

        data["users"][user_index] = updated_user
        payload = {"ok": True, "user": updated_user}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUser",
                "description": "Update user information like department, status, or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., U-001).",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department for the user.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status for the user.",
                        },
                        "mfa_enabled": {
                            "type": "boolean",
                            "description": "Enable/disable MFA for user.",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "New legal first name (can be provided independently to update username/email).",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "New legal last name (can be provided independently to update username/email).",
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }
