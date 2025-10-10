# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, updates: Dict[str, Any]) -> str:
        employees = list(data.get("employees", {}).values())
        changes = updates

        updated = False
        for e in employees:
            if e["employee_id"] == employee_id:
                e.update(changes)
                updated = True
                break

        if not updated:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        data["employees"] = employees
        return json.dumps({"success": f"employee {employee_id} updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee",
                "description": "Patch one or more fields on an existing employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "updates": {
                            "type": "object",
                            "description": "Dictionary of field:value pairs to update",
                        },
                    },
                    "required": ["employee_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
