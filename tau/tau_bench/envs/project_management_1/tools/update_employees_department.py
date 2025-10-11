# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEmployeesDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, employee_id) -> str:

        if not all([employee_id, department]):
            return json.dumps({"error": "employee_id and department are required"})

        employees = list(data.get("employees", {}).values())

        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["department"] = department
                return json.dumps({"success": True, "employee": employee})

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employees_department",
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
