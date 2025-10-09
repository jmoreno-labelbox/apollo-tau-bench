from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateUserDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, department: str = None) -> str:
        for user in data.get("users", {}).values():
            if user.get("user_id") == user_id:
                user["department"] = department
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
                "name": "UpdateUserDepartment",
                "description": "Updates the department for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "department": {"type": "string"},
                    },
                    "required": ["user_id", "department"],
                },
            },
        }
