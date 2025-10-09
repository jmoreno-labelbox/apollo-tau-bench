from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEmployeeIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_name: str = None) -> str:
        employees = data.get("employees", [])

        for employee in employees:
            if employee.get("name") == employee_name:
                payload = {"employee_id": employee.get("employee_id")}
                out = json.dumps(payload)
                return out
        payload = {"employee_id": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeIdByName",
                "description": "Retrieves the employee ID for a given employee's full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_name": {
                            "type": "string",
                            "description": "The full name of the employee.",
                        },
                    },
                    "required": ["employee_name"],
                },
            },
        }
