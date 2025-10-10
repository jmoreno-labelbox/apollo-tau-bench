# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListExpensesByDateRangeAndCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        start = kwargs.get("start_date")
        end = kwargs.get("end_date")
        cats = kwargs.get("categories", [])
        if not start or not end or not cats:
            return json.dumps({"error":"start_date, end_date, categories are required"}, indent=2)
        exp = []
        for e in list(data.get("expenses", {}).values()):
            d = str(e.get("expense_date",""))
            if start <= d <= end and e.get("category_code") in cats:
                exp.append(e)
        return json.dumps({"expenses": exp}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_expenses_by_date_range_and_category",
            "description":"Return expenses in [start_date, end_date] for given categories.",
            "parameters":{"type":"object","properties":{
                "start_date":{"type":"string"},
                "end_date":{"type":"string"},
                "categories":{"type":"array","items":{"type":"string"}}
            },"required":["start_date","end_date","categories"]}
        }}
