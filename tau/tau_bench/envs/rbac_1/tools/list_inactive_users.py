from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListInactiveUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inactive_since: str) -> str:
        inactive_since_dt = datetime.strptime(inactive_since, DT_STR_FORMAT)

        active_user_ids = {
            session["user_id"]
            for session in data.get("user_sessions", [])
            if datetime.strptime(session["end_time"], DT_STR_FORMAT)
            >= inactive_since_dt
        }

        all_user_ids = {user["user_id"] for user in data.get("users", [])}
        inactive_user_ids = list(all_user_ids - active_user_ids)
        payload = {"inactive_users": inactive_user_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInactiveUsers",
                "description": "Lists users who have not had a session since the specified date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inactive_since": {
                            "type": "string",
                            "description": "The date in ISO 8601 format (e.g., '2025-05-01T00:00:00Z').",
                        }
                    },
                    "required": ["inactive_since"],
                },
            },
        }
