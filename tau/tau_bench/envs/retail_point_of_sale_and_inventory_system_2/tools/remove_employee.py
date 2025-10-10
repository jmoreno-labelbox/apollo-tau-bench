# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveEmployee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        employees = list(data.get("employees", {}).values())
        original_len = len(employees)
        employees[:] = [e for e in employees if e.get("employee_id") != employee_id]

        if len(employees) == original_len:
                return json.dumps({"error": f"Employee with ID {employee_id} not found."})
                return json.dumps({"success": f"Employee {employee_id} removed successfully."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_employee",
                "description": "Remove an employee from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Unique identifier of the employee to remove."}
                    },
                    "required": ["employee_id"]
                }
            }
        }
