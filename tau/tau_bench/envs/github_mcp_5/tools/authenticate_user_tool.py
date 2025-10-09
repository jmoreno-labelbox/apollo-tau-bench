from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
    def invoke(data: dict[str, Any], username: str = None, email: str = None, auth_key: str = None) -> str:
        user_name = username
        user_email = email
        auth_key = auth_key

        if not user_name or not user_email:
            payload = {
                    "status": "error",
                    "message": "Missing required parameters: 'user_name' and/or 'user_email'.",
                    "required": ["user_name", "user_email"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        users = data.get("authentication", {}).values()
        user = next((c for c in users.values() if c["username"] == user_name), None)
        #user = get_data(users, user_name)

        if not user:
            payload = {"status": "fail", "verified": False, "reason": "User Name not found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif user_email != user["email"]:
            payload = {
                    "status": "fail",
                    "verified": False,
                    "reason": "Incorrect user email ID",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif auth_key != user["auth_key"]:
            payload = {
                    "status": "fail",
                    "verified": False,
                    "reason": "Incorrect user authentication key",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"status": "success", "verified": True, "confidence": 0.97}
            out = json.dumps(
                payload, indent=2
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "authenticateUser",
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
