from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CreateUser(Tool):
    """
    Establish a new user account with consistent ID generation.

    kwargs:
      username: str (mandatory)
      email: str (mandatory)
      department: str (mandatory)
      status: str = "ACTIVE" (optional)
      mfa_enabled: bool = True (optional)
    """

    @staticmethod
    def invoke(data: dict[str, Any], username: str = "", email: str = "", department: str = "", status: str = "ACTIVE", mfa_enabled: bool = True,
    actor_id: Any = None,
    ) -> str:
        if not username or not email or not department:
            payload = {"error": "username, email, and department are required"}
            out = json.dumps(payload)
            return out

        # Verify if the username is already taken
        users = data.get("users", [])
        for user in users:
            if user.get("username") == username:
                payload = {"error": f"username {username} already exists"}
                out = json.dumps(payload)
                return out

        # Register a new user
        new_user = {
            "user_id": _next_id(data, "users", "U"),
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": mfa_enabled,
        }

        data.setdefault("users", []).append(new_user)
        payload = {"ok": True, "user": new_user}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Create a new user account with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Username (lowercase, no spaces).",
                        },
                        "email": {
                            "type": "string",
                            "description": "User email address.",
                        },
                        "department": {
                            "type": "string",
                            "description": "User department.",
                        },
                        "status": {
                            "type": "string",
                            "description": "User status.",
                            "default": "ACTIVE",
                        },
                        "mfa_enabled": {
                            "type": "boolean",
                            "description": "Enable MFA for user.",
                            "default": True,
                        },
                    },
                    "required": ["username", "email", "department"],
                    "additionalProperties": False,
                },
            },
        }
