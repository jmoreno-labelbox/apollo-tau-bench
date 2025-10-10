# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class submit_performance_review(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, review_data) -> str:
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

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

        return json.dumps(
            {
                "success": f"Performance review {new_review['review_id']} submitted for {employee_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_performance_review",
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
