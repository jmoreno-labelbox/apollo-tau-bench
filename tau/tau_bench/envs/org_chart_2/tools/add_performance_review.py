# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_performance_review(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], review: Dict[str, Any]) -> str:
        if not review:
            return json.dumps({"error": "review record required"}, indent=2)
        pr = data.get("performance_reviews", [])
        pr.append(review)
        data["performance_reviews"] = pr
        return json.dumps({"success": f'review {review["review_id"]} added'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_performance_review",
                "description": "Append a new performance review record.",
                "parameters": {
                    "type": "object",
                    "properties": {"review": {"type": "object"}},
                    "required": ["review"],
                    "additionalProperties": False,
                },
            },
        }
