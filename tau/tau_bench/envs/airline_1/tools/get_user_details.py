from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserDetails(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str | None = None, user_email: str | None = None
    ) -> str:
        _user_emailL = user_email or ''.lower()
        pass
        users = data.get("users", {}).values()
        if user_id:
            for u in users.values():
                for res_id in u.get("reservations", []):
                    reservation = next(
                        (
                            r
                            for r in data.get("reservations", {}).values()
                            if r.get("reservation_id") == res_id
                        ),
                        None,
                    )
                    if reservation and reservation.get("user_id") == user_id:
                        payload = u
                        out = json.dumps(payload)
                        return out
        if user_email:
            user = next(
                (u for u in users.values() if u.get("email", "").lower() == user_email.lower()),
                None,
            )
            if user:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get the details of a user, including their reservations and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user's unique ID, typically a handle like 'mia.li3818'.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address.",
                        },
                    },
                    "required": [],
                },
            },
        }
