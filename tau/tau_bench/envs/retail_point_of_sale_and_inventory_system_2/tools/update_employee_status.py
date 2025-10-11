# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, new_status: str) -> str:
        employees = list(data.get("employees", {}).values())

        for i, employee in enumerate(employees):
            if employee.get("employee_id") == employee_id:
                employees[i]["status"] = new_status
        return json.dumps(employees[i], indent=2)
        return json.dumps({"error": f"Employee with ID {employee_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_status",
                "description": "Update the status of an existing employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Unique identifier of the employee."},
                        "new_status": {"type": "string", "description": "New status for the employee."}
                    },
                    "required": ["employee_id", "new_status"]
                }
            }
        }
