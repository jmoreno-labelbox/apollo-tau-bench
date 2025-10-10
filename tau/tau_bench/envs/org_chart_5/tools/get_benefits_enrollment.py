# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_benefits_enrollment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        department_id = kwargs.get("department_id")

        if employee_id:
            employee = find_employee(list(data.get("employees", {}).values()), employee_id)
            if not employee:
                return json.dumps(
                    {"error": f"employee_id {employee_id} not found"}, indent=2
                )
            return json.dumps(employee.get("benefit_plan_ids", []), indent=2)

        if department_id:
            dept_employees = [
                e
                for e in list(data.get("employees", {}).values())
                if e.get("department_id") == department_id
            ]
            all_benefits = {
                plan_id
                for emp in dept_employees
                for plan_id in emp.get("benefit_plan_ids", [])
            }
            return json.dumps(list(all_benefits), indent=2)

        return json.dumps(
            {"error": "employee_id or department_id is required"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_benefits_enrollment",
                "description": "List benefits enrollment status for an employee or department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "department_id": {"type": "string"},
                    },
                },
            },
        }
