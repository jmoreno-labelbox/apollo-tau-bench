# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_performance_reviews(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        reviews = data.get("performance_reviews", [])
        filtered = [r for r in reviews if r.get("employee_id") == employee_id]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_reviews",
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
