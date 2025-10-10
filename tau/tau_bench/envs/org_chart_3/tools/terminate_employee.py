# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class terminate_employee(Tool):
    """
    Marks an employee as terminated by setting status, termination_date,
    and (optionally) clearing benefit and compensation links.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, termination_date: str) -> str:
        employees = list(data.get("employees", {}).values())

        for e in employees:
            if e["employee_id"] == employee_id:
                e["status"] = "Terminated"
                e["termination_date"] = termination_date
                data["employees"] = employees
                return json.dumps({"success": f"employee {employee_id} terminated"}, indent=2)

        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminate_employee",
                "description": "Soft-delete: flag employee as Terminated and record final day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "termination_date": {
                            "type": "string",
                            "description": "ISO-8601 date of last employment (YYYY-MM-DD)"
                        }
                    },
                    "required": ["employee_id", "termination_date"],
                    "additionalProperties": False
                }
            }
        }
