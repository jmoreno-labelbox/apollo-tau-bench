from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class get_leave_calendar(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None, employee_id: str = None, start_date: str = None, end_date: str = None) -> str:
        if not department_id and not employee_id:
            payload = {"error": "department_id or employee_id is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = data.get("leave_records", [])

        if department_id:
            dept_employees = {
                e["employee_id"]
                for e in data.get("employees", [])
                if e.get("department_id") == department_id
            }
            results = [r for r in results if r.get("employee_id") in dept_employees]

        if employee_id:
            results = [r for r in results if r.get("employee_id") == employee_id]

        if start_date:
            results = [r for r in results if r.get("end_date", "") >= start_date]

        if end_date:
            results = [r for r in results if r.get("start_date", "") <= end_date]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLeaveCalendar",
                "description": "Retrieve leave records for a department or employee, optionally within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "start_date": {"type": "string", "description": "YYYY-MM-DD"},
                        "end_date": {"type": "string", "description": "YYYY-MM-DD"},
                    },
                },
            },
        }
