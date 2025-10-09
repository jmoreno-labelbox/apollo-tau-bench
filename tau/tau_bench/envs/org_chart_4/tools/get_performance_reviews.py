from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_performance_reviews(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        reviews = data.get("performance_reviews", [])
        filtered = [r for r in reviews if r.get("employee_id") == employee_id]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPerformanceReviews",
                "description": "Return all performance reviews for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to fetch performance reviews for",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
