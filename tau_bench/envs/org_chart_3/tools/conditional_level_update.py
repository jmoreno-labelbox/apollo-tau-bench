from tau_bench.envs.tool import Tool
import json
from typing import Any

class conditional_level_update(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, required_rating: str, new_level: str
    ) -> str:
        # Retrieve performance reviews
        reviews = data.get("performance_reviews", [])
        employee_reviews = [r for r in reviews if r["employee_id"] == employee_id]
        employee_reviews.sort(key=lambda r: r["period_end"], reverse=True)

        if not employee_reviews:
            payload = {"error": "No performance reviews found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest_review = employee_reviews[0]
        current_rating = latest_review.get("rating", "")

        if current_rating == required_rating:
            # Revise the level
            employees = data.get("employees", [])
            for e in employees:
                if e["employee_id"] == employee_id:
                    old_level = e.get("level_id", "")
                    e["level_id"] = new_level
                    data["employees"] = employees
                    payload = {
                        "success": f"Employee {employee_id} level updated from {old_level} to {new_level}",
                        "condition_met": f"Performance rating '{current_rating}' matches required '{required_rating}'",
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {
                "success": f"Level update skipped for employee {employee_id}",
                "condition_not_met": f"Performance rating '{current_rating}' does not match required '{required_rating}'",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pass
        #Retrieve performance reviews
        reviews = data.get("performance_reviews", [])
        employee_reviews = [r for r in reviews if r["employee_id"] == employee_id]
        employee_reviews.sort(key=lambda r: r["period_end"], reverse=True)

        if not employee_reviews:
            payload = {"error": "No performance reviews found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest_review = employee_reviews[0]
        current_rating = latest_review.get("rating", "")

        if current_rating == required_rating:
            #Revise the level
            employees = data.get("employees", [])
            for e in employees:
                if e["employee_id"] == employee_id:
                    old_level = e.get("level_id", "")
                    e["level_id"] = new_level
                    data["employees"] = employees
                    payload = {
                            "success": f"Employee {employee_id} level updated from {old_level} to {new_level}",
                            "condition_met": f"Performance rating '{current_rating}' matches required '{required_rating}'",
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {
                    "success": f"Level update skipped for employee {employee_id}",
                    "condition_not_met": f"Performance rating '{current_rating}' does not match required '{required_rating}'",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConditionalLevelUpdate",
                "description": "Update employee level only if their latest performance rating matches the required rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "required_rating": {
                            "type": "string",
                            "description": "Required performance rating (e.g., 'Exceeds')",
                        },
                        "new_level": {
                            "type": "string",
                            "description": "New level to assign if condition is met",
                        },
                    },
                    "required": ["employee_id", "required_rating", "new_level"],
                    "additionalProperties": False,
                },
            },
        }
