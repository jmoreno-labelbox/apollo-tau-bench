# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateExpenseDashboard(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        quarter = kwargs.get("quarter")
        included = kwargs.get("included_expenses", [])
        if not quarter or not isinstance(included, list):
            return json.dumps({"error": "quarter and included_expenses list are required"}, indent=2)
        path = f"/dashboards/ExpenseDashboards/{quarter}/expense_dashboard_{quarter}.pdf"
        return json.dumps({"quarter": quarter,"included_expenses": included,"pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "generate_expense_dashboard","description": "Generate an expense dashboard artifact for a given quarter.","parameters": {"type": "object","properties": {"quarter": {"type": "string"},"included_expenses": {"type": "array","items": {"type": "string"}}},"required": ["quarter","included_expenses"]}}}
