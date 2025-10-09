from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemoveEmployee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        original_len = len(employees)
        employees[:] = [e for e in employees if e.get("employee_id") != employee_id]

        if len(employees) == original_len:
            payload = {"error": f"Employee with ID {employee_id} not found."}
            out = json.dumps(payload)
            return out

        data["employees"] = employees
        payload = {"success": f"Employee {employee_id} removed successfully."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveEmployee",
                "description": "Remove an employee from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee to remove.",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
