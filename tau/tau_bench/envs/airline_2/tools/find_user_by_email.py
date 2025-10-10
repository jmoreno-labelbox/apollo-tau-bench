# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUserByEmail(Tool):
    """
    Resolve a user by email and return a deterministic user_id.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], user_email: str) -> str:
        users: List[Dict[str, Any]] = list(data.get("users", {}).values())
        for u in users:
            if u.get("email") == user_email:
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                return json.dumps({
                    "email": user_email,
                    # "id": f"{first}_{last}_1234",
                    "name": first,
                    "last": last,
                    "dob": u.get("dob"),
                })
        return json.dumps({"error": "User not found", "email": user_email})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_user_by_email",
                "description": "Find an existing user by email and return a deterministic user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "Email of the user to look up."
                        }
                    },
                    "required": ["user_email"]
                }
            }
        }
