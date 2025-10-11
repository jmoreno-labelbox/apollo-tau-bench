# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateUser(Tool):
    """ Creates a new user in the user.json file with correct formatting and default values. """

    @staticmethod
    def invoke(data: Dict[str, Any], department, email, username, status = "ACTIVE") -> str:
        try:
           users = list(data.get('users', {}).values())
        except (KeyError, json.JSONDecodeError):
            users = []
        existing_ids = [int(item["user_id"].replace("U-", "")) for item in users if item["user_id"].startswith("U-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_id = f"U-{next_id_num:03d}"

        new_user = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "department": department,
            "status": status,  # Set to ACTIVE by default if not provided.
            "mfa_enabled": False
        }
        users.append(new_user)
        data["users.json"] = json.dumps(users)
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Creates a new user entry in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the new user."
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address of the new user."
                            },
                        "department": {
                            "type": "string",
                            "description": "The department where the new user belongs."
                            },
                        "status": {
                            "type": "string",
                            "description": "The status of the new user (e.g., ACTIVE, INACTIVE)."
                            }
                    },
                    "required": ["username", "email", "department", "status"]
                }
            }
        }
