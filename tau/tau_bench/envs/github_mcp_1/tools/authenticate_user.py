from tau_bench.envs.tool import Tool
import json
from typing import Any

class AuthenticateUser(Tool):
    """Validates a user by username, email, and auth_key; returns full record on success."""

    @staticmethod
    def invoke(data: dict[str, Any], username: str = "", email: str = "", auth_key: str = "") -> str:
        username = username.strip()
        email = email.strip()
        auth_key = auth_key.strip()

        reset_variables()

        if not username or not email or not auth_key:
            payload = {"error": "username, email, and auth_key are all required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Primary store: data.get("authentication", [])
        authentication = data.get("authentication", [])

        #Fallback if the DB was provided as a top-level list
        if not isinstance(authentication, list) and isinstance(data, list):
            authentication = data

        #Lookup by username first
        user = next((u for u in authentication if u.get("username") == username), None)
        if not user:
            payload = {"error": "User not found."}
            out = json.dumps(payload, indent=2)
            return out

        #Validate remaining credentials
        if user.get("email") != email or user.get("auth_key") != auth_key:
            payload = {"error": "Credentials invalid."}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": f"User '{username}' authenticated successfully.", "user": user}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuthenticateUser",
                "description": "Validates user credentials using username (primary lookup), then email and auth_key. Returns full record on success.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the user",
                        },
                        "email": {
                            "type": "string",
                            "description": "The registered email address of the user",
                        },
                        "auth_key": {
                            "type": "string",
                            "description": "Authentication key for the user",
                        },
                    },
                    "required": ["username", "email", "auth_key"],
                },
            },
        }
