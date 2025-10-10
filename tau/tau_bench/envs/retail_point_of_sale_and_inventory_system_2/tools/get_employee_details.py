# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        employees = list(data.get("employees", {}).values())
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                return json.dumps(employee, indent=2)
        return json.dumps({"error": f"Employee with ID {employee_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_details",
                "description": "Get detailed information about a specific employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Unique identifier of the employee."}
                    },
                    "required": ["employee_id"]
                }
            }
        }
