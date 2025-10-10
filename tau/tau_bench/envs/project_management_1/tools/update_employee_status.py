# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], available_from, employee_id, status) -> str:

        if not all([employee_id, status]):
            return json.dumps({"error": "employee_id and status are required"})

        employees = list(data.get("employees", {}).values())

        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["status"] = status
                if available_from:
                    employee["available_from"] = available_from
                return json.dumps({"success": True, "employee": employee})

        return json.dumps({"error": f"Employee with ID '{employee_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_status",
                "description": "Update employee status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: active, bench, leave",
                        },
                        "available_from": {
                            "type": "string",
                            "description": "Date when employee becomes available",
                        },
                    },
                    "required": ["employee_id", "status"],
                },
            },
        }
