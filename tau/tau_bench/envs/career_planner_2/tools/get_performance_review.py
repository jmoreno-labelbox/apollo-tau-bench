# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPerformanceReview(Tool):
    """Fetch performance review workflows for a user and period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        per = kwargs.get("period")
        reviews = [
            wf
            for wf in data.get("hr_workflows", [])
            if wf.get("workflow_type") == "Performance Review"
            and wf.get("employee_id") == uid
            and wf.get("review_period") == per
        ]
        return json.dumps(reviews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_review",
                "description": "Get performance review by period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "period": {"type": "string"},
                    },
                    "required": ["user_id", "period"],
                },
            },
        }
