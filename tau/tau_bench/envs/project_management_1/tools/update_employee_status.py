from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, status: str = None, available_from: str = None) -> str:
        if not all([employee_id, status]):
            payload = {"error": "employee_id and status are required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["status"] = status
                if available_from:
                    employee["available_from"] = available_from
                payload = {"success": True, "employee": employee}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Employee with ID '{employee_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeeStatus",
                "description": "Update employee status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: active, bench, leave",
                        },
                        "available_from": {
                            "type": "string",
                            "description": "Date when employee becomes available",
                        },
                    },
                    "required": ["employee_id", "status"],
                },
            },
        }
