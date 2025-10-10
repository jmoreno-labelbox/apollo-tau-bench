# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserIdFromFullNameAndZip(Tool): # READING
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        db = list(data.get("users", {}).values())
        filter_params = {
            "name": {
                "first_name": first_name,
                "last_name": last_name
            },
            "address": {
                "zip": zip
            }
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
                "name": "get_user_id_from_full_name_and_zip",
                "description": "Retrieve user information by user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "The user's first name."},
                        "last_name": {"type": "string", "description": "The user's last name."},
                        "zip": {"type": "string", "description": "The user's zip code."}
                    },
                    "required": ["first_name", "last_name", "zip"]
                    }
                }
            }
