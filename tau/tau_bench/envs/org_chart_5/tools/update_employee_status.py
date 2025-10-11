# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, new_status) -> str:
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        employee["status"] = new_status
        if new_status.lower() == "terminated":
            employee["termination_date"] = "2025-06-24"  # Employing our typical "today" reference.
        return json.dumps(
            {"success": f"Employee {employee_id} status updated to {new_status}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_status",
                "description": "Update an employee's current status (e.g., 'Active', 'On Leave', 'Terminated').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["employee_id", "new_status"],
                },
            },
        }
