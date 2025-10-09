from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.setdefault("employees", [])
        employee = {"employee_id": employee_id}
        employees.append(employee)
        payload = {"success": True, "employee_id": employee_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addEmployee",
                "description": "Add a new employee record. The employee object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee": {
                            "type": "object",
                            "description": "Employee record to add",
                        }
                    },
                    "required": ["employee"],
                    "additionalProperties": False,
                },
            },
        }
