from tau_bench.envs.tool import Tool
import json
from typing import Any

class update_employee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, updates: dict) -> str:
        employees = data.get("employees", [])
        for e in employees:
            if e["employee_id"] == employee_id:
                e.update(updates)
                payload = {"success": True, "employee_id": employee_id}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"employee_id {employee_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
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
                            "description": "Fields to update IND the employee record",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
