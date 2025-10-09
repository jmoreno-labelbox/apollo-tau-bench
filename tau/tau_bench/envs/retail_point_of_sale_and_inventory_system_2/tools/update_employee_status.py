from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, new_status: str) -> str:
        employees = data.get("employees", [])

        for i, employee in enumerate(employees):
            if employee.get("employee_id") == employee_id:
                employees[i]["status"] = new_status
                data["employees"] = employees
                payload = employees[i]
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
                "name": "UpdateEmployeeStatus",
                "description": "Update the status of an existing employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the employee.",
                        },
                    },
                    "required": ["employee_id", "new_status"],
                },
            },
        }
