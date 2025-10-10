# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_performance_review(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], performance_review: dict) -> str:
        reviews = data.setdefault("performance_reviews", [])
        reviews.append(performance_review)
        return json.dumps(
            {"success": True, "review_id": performance_review.get("review_id")},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_performance_review",
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
