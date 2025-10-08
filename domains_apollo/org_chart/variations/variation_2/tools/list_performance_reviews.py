from tau_bench.envs.tool import Tool
import json
from typing import Any

class list_performance_reviews(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, performance_reviews: list = None) -> str:
        pr = [
            r
            for r in (performance_reviews or [])
            if r["employee_id"] == employee_id
        ]
        payload = pr
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPerformanceReviews",
                "description": "Return all reviews linked to the employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
