# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetExpenseCategories(Tool):
    """Get all expense categories with deductibility rules."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_categories = data.get("expense_categories", [])
        return json.dumps(expense_categories)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_expense_categories",
                "description": "Get all expense categories with their deductibility percentages and rules.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
