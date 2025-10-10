# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUserIdByNameZip(Tool):
    """Find a user_id by first name, last name, and ZIP code."""

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        users = list(data.get("users", {}).values())
        for user in users:
            if (user.get("name", {}).get("first_name") == first_name and
                user.get("name", {}).get("last_name") == last_name and
                user.get("address", {}).get("zip") == zip):
                return json.dumps({"user_id": user.get("user_id")})
        return json.dumps({"error": "User not found", "first_name": first_name, "last_name": last_name, "zip": zip})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user_id from users.json by first name, last name, and ZIP code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "zip": {"type": "string"}
                    },
                    "required": ["first_name", "last_name", "zip"]
                }
            }
        }
