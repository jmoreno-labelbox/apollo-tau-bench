from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], review: dict[str, Any]) -> str:
        if not review:
            payload = {"error": "review record required"}
            out = json.dumps(payload, indent=2)
            return out
        pr = data.get("performance_reviews", [])
        pr.append(review)
        data["performance_reviews"] = pr
        payload = {"success": f'review {review["review_id"]} added'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPerformanceReview",
                "description": "Append a new performance review record.",
                "parameters": {
                    "type": "object",
                    "properties": {"review": {"type": "object"}},
                    "required": ["review"],
                    "additionalProperties": False,
                },
            },
        }
