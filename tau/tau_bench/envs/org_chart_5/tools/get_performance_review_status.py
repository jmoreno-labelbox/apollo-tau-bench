# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_performance_review_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        employee_id = kwargs.get("employee_id")
        reviews = data.get("performance_reviews", [])

        if employee_id:
            results = [r for r in reviews if r.get("employee_id") == employee_id]
        elif department_id:
            dept_employees = {
                e["employee_id"]
                for e in list(data.get("employees", {}).values())
                if e.get("department_id") == department_id
            }
            results = [r for r in reviews if r.get("employee_id") in dept_employees]
        else:
            return json.dumps(
                {"error": "Either employee_id or department_id is required"}, indent=2
            )
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_review_status",
                "description": "List performance reviews for a department or an individual employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                },
            },
        }
