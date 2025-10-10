# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_level_update(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, required_rating: str, new_level: str) -> str:
        # Obtain performance evaluations
        reviews = data.get("performance_reviews", [])
        employee_reviews = [r for r in reviews if r["employee_id"] == employee_id]
        employee_reviews.sort(key=lambda r: r["period_end"], reverse=True)

        if not employee_reviews:
            return json.dumps({"error": "No performance reviews found for employee"}, indent=2)

        latest_review = employee_reviews[0]
        current_rating = latest_review.get("rating", "")

        if current_rating == required_rating:
            # Modify the level.
            employees = list(data.get("employees", {}).values())
            for e in employees:
                if e["employee_id"] == employee_id:
                    old_level = e.get("level_id", "")
                    e["level_id"] = new_level
                    data["employees"] = employees
                    return json.dumps({
                        "success": f"Employee {employee_id} level updated from {old_level} to {new_level}",
                        "condition_met": f"Performance rating '{current_rating}' matches required '{required_rating}'"
                    }, indent=2)

            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)
        else:
            return json.dumps({
                "success": f"Level update skipped for employee {employee_id}",
                "condition_not_met": f"Performance rating '{current_rating}' does not match required '{required_rating}'"
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_level_update",
                "description": "Update employee level only if their latest performance rating matches the required rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "required_rating": {"type": "string", "description": "Required performance rating (e.g., 'Exceeds')"},
                        "new_level": {"type": "string", "description": "New level to assign if condition is met"}
                    },
                    "required": ["employee_id", "required_rating", "new_level"],
                    "additionalProperties": False
                }
            }
        }
