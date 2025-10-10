# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, updates: dict) -> str:
        employees = list(data.get("employees", {}).values())
        for e in employees:
            if e["employee_id"] == employee_id:
                e.update(updates)
                return json.dumps(
                    {"success": True, "employee_id": employee_id}, indent=2
                )
        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee",
                "description": "Update an existing employee record with the provided updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields to update in the employee record",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
