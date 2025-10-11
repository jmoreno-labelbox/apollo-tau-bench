# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class remove_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        employees = list(data.get("employees", {}).values())

        if employee_id is None:
            return json.dumps({"error": "employee_id must be sent"}, indent=2)

        for employee in employees:
            if employee["employee_id"] == employee_id:
                del employee

                return json.dumps(
                    {"success": "Removed employee: {}".format(employee_id)}, indent=2
                )

        return json.dumps({"error": "No employee found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_employee",
                "description": "Removes an employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to remove",
                        },
                    },
                },
            },
        }
