# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AuthenticateUser(Tool):
    """Validates a user by username, email, and auth_key; returns full record on success."""

    @staticmethod
    def invoke(data: Dict[str, Any], auth_key = "", email = "", username = "") -> str:
        username = username.strip()
        email = email.strip()
        auth_key = auth_key.strip()

        reset_variables()

        if not username or not email or not auth_key:
            return json.dumps(
                {"error": "username, email, and auth_key are all required."},
                indent=2
            )

        # Main storage: data.get("authentication", [])
        authentication = data.get("authentication", [])

        # Alternative handling if the database is given as a top-level array.
        if not isinstance(authentication, list) and isinstance(data, list):
            authentication = data

        # Prioritize searching by username initially.
        user = next((u for u in authentication if u.get("username") == username), None)
        if not user:
            return json.dumps({"error": "User not found."}, indent=2)

        # Check the validity of the remaining credentials.
        if user.get("email") != email or user.get("auth_key") != auth_key:
            return json.dumps({"error": "Credentials invalid."}, indent=2)
    

        # Success: add complete user information
        return json.dumps(
            {
                "success": f"User '{username}' authenticated successfully.",
                "user": user
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "authenticate_user",
                "description": "Validates user credentials using username (primary lookup), then email and auth_key. Returns full record on success.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "description": "The username of the user"},
                        "email": {"type": "string", "description": "The registered email address of the user"},
                        "auth_key": {"type": "string", "description": "Authentication key for the user"}
                    },
                    "required": ["username", "email", "auth_key"]
                }
            }
        }
