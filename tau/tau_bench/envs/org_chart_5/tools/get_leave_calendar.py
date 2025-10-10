# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_leave_calendar(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        employee_id = kwargs.get("employee_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not department_id and not employee_id:
            return json.dumps(
                {"error": "department_id or employee_id is required"}, indent=2
            )

        results = data.get("leave_records", [])

        if department_id:
            dept_employees = {
                e["employee_id"]
                for e in list(data.get("employees", {}).values())
                if e.get("department_id") == department_id
            }
            results = [r for r in results if r.get("employee_id") in dept_employees]

        if employee_id:
            results = [r for r in results if r.get("employee_id") == employee_id]

        if start_date:
            results = [r for r in results if r.get("end_date", "") >= start_date]

        if end_date:
            results = [r for r in results if r.get("start_date", "") <= end_date]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_leave_calendar",
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
