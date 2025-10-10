# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class request_leave(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        leave_data = kwargs.get("leave_data")
        if not find_employee(list(data.get("employees", {}).values()), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        new_leave = leave_data.copy()
        new_leave["employee_id"] = employee_id
        if "leave_id" not in new_leave:
            new_leave["leave_id"] = f"LV_NEW_{len(data.get('leave_records', [])) + 1}"

        data.get("leave_records", []).append(new_leave)
        return json.dumps(
            {"success": f"Leave {new_leave['leave_id']} requested for {employee_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_leave",
                "description": "Submit a new leave request for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "leave_data": {
                            "type": "object",
                            "description": "Details including a unique leave_id",
                        },
                    },
                    "required": ["employee_id", "leave_data"],
                },
            },
        }
