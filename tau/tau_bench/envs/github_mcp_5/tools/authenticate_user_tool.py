# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AuthenticateUserTool(Tool):
    """
    Tool to verify a customer's identity based on their official ID document.

    This tool confirms whether the given document corresponds to a known customer
    based on the customer_id and document number.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Validates customer identity and returns a structured result.

        get_info() -> Dict[str, Any]:
            Returns metadata about the expected input parameters and verification logic.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_name = kwargs.get("username")
        user_email = kwargs.get("email")
        auth_key = kwargs.get("auth_key")

        if not user_name or not user_email:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'user_name' and/or 'user_email'.",
                    "required": ["user_name", "user_email"],
                },
                indent=2,
            )

        users = data.get('authentication', [])
        user = next((c for c in users if c["username"] == user_name), None)
        # user = retrieve_data(users, user_name)

        if not user:
            return json.dumps(
                {"status": "fail", "verified": False, "reason": "User Name not found"},
                indent=2,
            )
        elif user_email != user['email']:
            return json.dumps(
                {"status": "fail", "verified": False, "reason": "Incorrect user email ID"},
                indent=2,
            )
        elif auth_key != user['auth_key']:
            return json.dumps(
                {"status": "fail", "verified": False, "reason": "Incorrect user authentication key"},
                indent=2,
            )
        else:
            # Imitate the logic for verifying documents.
            return json.dumps(
                {"status": "success", "verified": True, "confidence": 0.97}, indent=2
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "authenticate_user",
                "description": "Authenticate user using user name, email, and auth key.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Unique identifier of the user in the database.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Unique email address of the user.",
                        },
                    },
                    "required": ["username", "email"],
                },
            },
        }
