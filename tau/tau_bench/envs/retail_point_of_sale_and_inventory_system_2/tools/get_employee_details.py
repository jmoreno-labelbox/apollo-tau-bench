from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEmployeeDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                payload = employee
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Employee with ID {employee_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeDetails",
                "description": "Get detailed information about a specific employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee.",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
