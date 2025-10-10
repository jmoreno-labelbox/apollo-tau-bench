# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateUser(Tool):
    """
    Create a new user account with deterministic ID generation.

    kwargs:
      username: str (required)
      email: str (required)
      department: str (required)
      status: str = "ACTIVE" (optional)
      mfa_enabled: bool = True (optional)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username", "")
        email = kwargs.get("email", "")
        department = kwargs.get("department", "")
        status = kwargs.get("status", "ACTIVE")
        mfa_enabled = kwargs.get("mfa_enabled", True)

        if not username or not email or not department:
            return json.dumps({"error": "username, email, and department are required"})

        # Verify if the username is already in use.
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("username") == username:
                return json.dumps({"error": f"username {username} already exists"})

        # Add a new user.
        new_user = {
            "user_id": _next_id(data, "users", "U"),
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": mfa_enabled
        }

        data.setdefault("users", []).append(new_user)
        return json.dumps({"ok": True, "user": new_user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Create a new user account with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "description": "Username (lowercase, no spaces)."},
                        "email": {"type": "string", "description": "User email address."},
                        "department": {"type": "string", "description": "User department."},
                        "status": {"type": "string", "description": "User status.", "default": "ACTIVE"},
                        "mfa_enabled": {"type": "boolean", "description": "Enable MFA for user.", "default": True}
                    },
                    "required": ["username", "email", "department"],
                    "additionalProperties": False
                }
            }
        }
