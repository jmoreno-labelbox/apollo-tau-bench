from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_performance_review(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], performance_review: dict) -> str:
        reviews = data.setdefault("performance_reviews", [])
        data["reviews"][review_id] = performance_review
        payload = {"success": True, "review_id": performance_review.get("review_id")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPerformanceReview",
                "description": "Add a new performance review record. The performance_review object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "performance_review": {
                            "type": "object",
                            "description": "Performance review record to add",
                        }
                    },
                    "required": ["performance_review"],
                    "additionalProperties": False,
                },
            },
        }
