from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if employee["employee_id"] == employee_id:
                payload = employee
                out = json.dumps(payload)
                return out
        payload = {"status": "error", "reason": "Employee not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeInfo",
                "description": "Finds an employee's info using their id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to search for.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
