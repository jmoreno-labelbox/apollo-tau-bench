from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateUser(Tool):
    """Generates a new user in the user.json file with proper formatting and default settings."""

    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, email: str = None, department: str = None, status: str = "ACTIVE",
    actor_id: Any = None,
    ) -> str:
        try:
            users = data.get("users", [])
        except (KeyError, json.JSONDecodeError):
            users = []
        existing_ids = [
            int(item["user_id"].replace("U-", ""))
            for item in users
            if item["user_id"].startswith("U-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_id = f"U-{next_id_num:03d}"

        new_user = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": False,
        }
        users.append(new_user)
        data["users.json"] = json.dumps(users)
        payload = new_user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Creates a new user entry in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the new user.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address of the new user.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department where the new user belongs.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the new user (e.g., ACTIVE, INACTIVE).",
                        },
                    },
                    "required": ["username", "email", "department", "status"],
                },
            },
        }
