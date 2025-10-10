# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserDetails(Tool):
    """A tool to retrieve the full details of a user using their user ID or email."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: Optional[str] = None, user_email: Optional[str] = None) -> str:
        users = list(data.get("users", {}).values())
        if user_id:
            for u in users:
                for res_id in u.get("reservations", []):
                    reservation = next((r for r in list(data.get("reservations", {}).values()) if r.get("reservation_id") == res_id), None)
                    if reservation and reservation.get("user_id") == user_id:
                        return json.dumps(u)
        if user_email:
            user = next((u for u in users if u.get("email", "").lower() == user_email.lower()), None)
            if user:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get the details of a user, including their reservations and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user's unique ID, typically a handle like 'mia.li3818'."
                        },
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address."
                        }
                    },
                    "required": []
                }
            }
        }
