# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee: dict) -> str:
        employees = data.setdefault("employees", [])
        employees.append(employee)
        return json.dumps(
            {"success": True, "employee_id": employee.get("employee_id")}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee",
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
