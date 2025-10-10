# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWeeklySalesByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category, start_date) -> str:
        cat = category
        start = start_date
        for r in list(data.get("f_sales", {}).values()):
            if r.get("category") == cat and r.get("start_date") == start:
                return json.dumps(r)
        return json.dumps({"error": "sales_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_weekly_sales_by_category", "description": "Gets weekly sales for a category.",
                             "parameters": {"type": "object", "properties": {"category": {"type": "string"},
                                                                             "start_date": {"type": "string"}},
                                            "required": ["category", "start_date"]}}}
