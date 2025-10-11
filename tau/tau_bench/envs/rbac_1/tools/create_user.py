# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, email, status, username) -> str:
        users = list(data.get('users', {}).values())
        new_id_num = max((int(u['user_id'][2:]) for u in users), default=0) + 1
        new_user_id = f"U-{new_id_num:03d}"
        new_user = {
                "user_id": new_user_id,
                "username": username,
                "email": email,
                "department": department,
                "status": status,
                "mfa_enabled": False
        }
        users.append(new_user)
        data['users'] = users
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_user",
                        "description": "Creates a new user in the system.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "username": {
                                                "type": "string",
                                                "description": "The username for the new user."
                                        },
                                        "email": {
                                                "type": "string",
                                                "description": "The email address for the new user."
                                        },
                                        "department": {
                                                "type": "string",
                                                "description": "The department the user belongs to."
                                        },
                                        "status": {
                                                "type": "string",
                                                "description": "The initial status of the user account (e.g., ACTIVE)."
                                        }
                                },
                                "required": ["username", "email", "department", "status"]
                        }
                }
        }
