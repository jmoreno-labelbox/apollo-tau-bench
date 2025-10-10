# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        employees = list(data.get("employees", {}).values())
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                return json.dumps(employee, indent=2)

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_details",
                "description": "Get details of a specific employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
