from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        department_name = name

        if not all([department_name]):
            payload = {"error": "department_name is a required parameters"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", [])

        for i, department in enumerate(departments):
            if department.get("department_name") == department_name:
                departments.pop(i)
                payload = {"success": True}
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"Department name '{department_name}' does not exist",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteDepartment",
                "description": "Delete a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Department name"},
                    },
                    "required": ["name"],
                },
            },
        }
