from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class submit_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, review_data: dict[str, Any] = None) -> str:
        employee = find_employee(data.get("employees", []), employee_id)
        if not employee:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_review = review_data.copy()
        new_review["employee_id"] = employee_id
        if "review_id" not in new_review:
            new_review["review_id"] = (
                f"PR_NEW_{len(data.get('performance_reviews', [])) + 1}"
            )

        data.get("performance_reviews", []).append(new_review)

        if "performance_review_ids" not in employee:
            employee["performance_review_ids"] = []
        if new_review["review_id"] not in employee["performance_review_ids"]:
            employee["performance_review_ids"].append(new_review["review_id"])
        payload = {
                "success": f"Performance review {new_review['review_id']} submitted for {employee_id}"
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
                "name": "SubmitPerformanceReview",
                "description": "Submit a new performance review for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "review_data": {
                            "type": "object",
                            "description": "Details including review_id, type, rating, date",
                        },
                    },
                    "required": ["employee_id", "review_data"],
                },
            },
        }
