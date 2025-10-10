# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserIdFromEmail(Tool): # ACCESS
    @staticmethod
    def invoke(data: Dict[str, Any], email: str) -> str:
        db = list(data.get("users", {}).values())
        filter_params = {
            "email": email
        }

        user = [row for row in db if _match(row, filter_params)]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        return json.dumps(user[0]["user_id"]) if user else json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id_from_email",
                "description": "Retrieve user information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "description": "The user's email address."},
                    },
                    "required": ["email"]
                }
            }
        }
