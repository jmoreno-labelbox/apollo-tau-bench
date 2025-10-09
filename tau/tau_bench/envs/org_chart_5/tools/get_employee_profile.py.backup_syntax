from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_employee_profile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        employee = find_employee(data.get("employees", {}).values()), employee_id)
        if not employee:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        profile = employee.copy()
        profile["compensation_history"] = [
            c
            for c in data.get("compensation_records", {}).values()
            if c.get("employee_id") == employee_id
        ]
        profile["performance_reviews"] = [
            r
            for r in data.get("performance_reviews", {}).values()
            if r.get("employee_id") == employee_id
        ]
        profile["leave_records"] = [
            l
            for l in data.get("leave_records", {}).values()
            if l.get("employee_id") == employee_id
        ]
        for doc_record in data.get("employee_documents", {}).values().get(
            "employee_documents", []
        ):
            if doc_record.get("employee_id") == employee_id:
                profile["documents"] = doc_record.get("documents", [])
                break
        payload = profile
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeProfile",
                "description": "Retrieve a comprehensive profile for an employee, including job, compensation, reviews, and documents.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
