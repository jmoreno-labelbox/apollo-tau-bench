from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class FindUserByEmail(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str) -> str:
        users: list[dict[str, Any]] = data.get("users", [])
        for u in users:
            if u.get("email") == user_email:
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                payload = {
                    "email": user_email,
                    "name": first,
                    "last": last,
                    "dob": u.get("dob"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "email": user_email}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUserByEmail",
                "description": "Find an existing user by email and return a deterministic user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "Email of the user to look up.",
                        }
                    },
                    "required": ["user_email"],
                },
            },
        }
