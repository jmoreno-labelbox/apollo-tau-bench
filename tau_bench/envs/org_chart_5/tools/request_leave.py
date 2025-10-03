from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class request_leave(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, leave_data: dict = None) -> str:
        if not find_employee(data.get("employees", []), employee_id):
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_leave = leave_data.copy()
        new_leave["employee_id"] = employee_id
        if "leave_id" not in new_leave:
            new_leave["leave_id"] = f"LV_NEW_{len(data.get('leave_records', [])) + 1}"

        data.get("leave_records", []).append(new_leave)
        payload = {"success": f"Leave {new_leave['leave_id']} requested for {employee_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestLeave",
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
