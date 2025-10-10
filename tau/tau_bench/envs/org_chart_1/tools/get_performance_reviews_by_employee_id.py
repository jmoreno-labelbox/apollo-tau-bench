# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_performance_reviews_by_employee_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        pr = [
            r
            for r in data.get("performance_reviews", [])
            if r["employee_id"] == employee_id
        ]
        return json.dumps(pr, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_reviews_by_employee_id",
                "description": "Return all reviews linked to the employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
