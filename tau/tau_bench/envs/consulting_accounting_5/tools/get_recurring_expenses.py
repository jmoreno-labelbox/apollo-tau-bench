# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRecurringExpenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns recurring_ids for all recurring expenses (optionally filtered by category_code).
        """
        category_code = kwargs.get("category_code")
        recs = data["recurring_schedules"]
        if category_code:
            recs = [r for r in recs if r["category_code"] == category_code]
        recurring_ids = [r["recurring_id"] for r in recs]
        return json.dumps(recurring_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecurringExpenses",
                "description": "Fetch recurring_ids for all recurring expenses, optionally filtered by category_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string", "description": "Optional filter by expense category"}
                    },
                    "required": [],
                },
            },
        }
