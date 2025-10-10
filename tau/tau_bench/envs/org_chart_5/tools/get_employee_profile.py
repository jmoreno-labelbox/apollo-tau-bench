# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_employee_profile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        profile = employee.copy()
        profile["compensation_history"] = [
            c
            for c in data.get("compensation_records", [])
            if c.get("employee_id") == employee_id
        ]
        profile["performance_reviews"] = [
            r
            for r in data.get("performance_reviews", [])
            if r.get("employee_id") == employee_id
        ]
        profile["leave_records"] = [
            l
            for l in data.get("leave_records", [])
            if l.get("employee_id") == employee_id
        ]
        for doc_record in data.get("employee_documents", {}).get(
            "employee_documents", []
        ):
            if doc_record.get("employee_id") == employee_id:
                profile["documents"] = doc_record.get("documents", [])
                break
        return json.dumps(profile, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_profile",
                "description": "Retrieve a comprehensive profile for an employee, including job, compensation, reviews, and documents.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
