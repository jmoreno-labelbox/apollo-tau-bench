from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None) -> str:
        department_name = department
        users_in_dept = [
            user
            for user in data.get("users", {}).values()
            if user.get("department") == department_name
        ]
        payload = {"users": users_in_dept}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersByDepartment",
                "description": "Retrieves all users for a given department by the department's name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "The name of the department to search for (e.g., 'Engineering').",
                        }
                    },
                    "required": ["department"],
                },
            },
        }
