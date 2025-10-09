from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPerformanceReview(Tool):
    """Retrieve performance review workflows for a specific user and time frame."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, period: str = None) -> str:
        reviews = [
            wf
            for wf in data.get("hr_workflows", {}).values()
            if wf.get("workflow_type") == "Performance Review"
            and wf.get("employee_id") == user_id
            and wf.get("review_period") == period
        ]
        payload = reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPerformanceReview",
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
