from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_performance_review_status(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None, employee_id: str = None) -> str:
        reviews = data.get("performance_reviews", {}).values()

        if employee_id:
            results = [r for r in reviews.values() if r.get("employee_id") == employee_id]
        elif department_id:
            dept_employees = {
                e["employee_id"]
                for e in data.get("employees", {}).values()
                if e.get("department_id") == department_id
            }
            results = [r for r in reviews.values() if r.get("employee_id") in dept_employees]
        else:
            payload = {"error": "Either employee_id or department_id is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPerformanceReviewStatus",
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
