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
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, email: str = None, department: str = None, status: str = None,
    actor_id: Any = None,
    ) -> str:
        pass
        users = data.get("users", [])

        # Effectively determine the subsequent numeric identifier based on current user_ids formatted as 'U-###'
        def _extract_num(user_id: Any) -> int:
            pass
            if not isinstance(user_id, str):
                return 0
            if not user_id.startswith("U-"):
                return 0
            num_part = user_id[2:]
            return int(num_part) if num_part.isdigit() else 0

        new_id_num = max((_extract_num(u.get("user_id")) for u in users), default=0) + 1
        new_user_id = f"U-{new_id_num:03d}"
        new_user = {
            "user_id": new_user_id,
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": False,
        }
        users.append(new_user)
        data["users"] = users
        payload = new_user
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Creates a new user in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username for the new user.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address for the new user.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department the user belongs to.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The initial status of the user account (e.g., ACTIVE).",
                        },
                    },
                    "required": ["username", "email", "department", "status"],
                },
            },
        }
