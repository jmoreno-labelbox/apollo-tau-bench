from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetActiveUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, note: Any = None) -> str:
        active_users = [
            user["user_id"]
            for user in data.get("users", [])
            if user.get("department") == department and user.get("status") == "ACTIVE"
        ]
        payload = {"users": active_users}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetActiveUsersByDepartment",
                "description": "Retrieves a list of active users for a specific department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "The department to filter by.",
                        }
                    },
                    "required": ["department"],
                },
            },
        }
