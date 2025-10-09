from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateEmployeesDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, department: str = None) -> str:
        if not all([employee_id, department]):
            payload = {"error": "employee_id and department are required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()

        for employee in employees.values():
            if employee.get("employee_id") == employee_id:
                employee["department"] = department
                payload = {"success": True, "employee": employee}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Employee with ID '{employee_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeesDepartment",
                "description": "Update employee department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department",
                        },
                    },
                    "required": ["employee_id", "department"],
                },
            },
        }
