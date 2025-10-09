from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_benefits_enrollment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, department_id: str = None) -> str:
        if employee_id:
            employee = find_employee(data.get("employees", {}).values(), employee_id)
            if not employee:
                payload = {"error": f"employee_id {employee_id} not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            payload = employee.get("benefit_plan_ids", [])
            out = json.dumps(payload, indent=2)
            return out

        if department_id:
            dept_employees = [
                e
                for e in data.get("employees", {}).values()
                if e.get("department_id") == department_id
            ]
            all_benefits = {
                plan_id
                for emp in dept_employees
                for plan_id in emp.get("benefit_plan_ids", [])
            }
            payload = list(all_benefits)
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "employee_id or department_id is required"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBenefitsEnrollment",
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
