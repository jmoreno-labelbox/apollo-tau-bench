# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSalesByCategoryRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["category", "start_date", "end_date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_sales")
        out = [r for r in rows if
               r.get("category") == kwargs["category"] and r.get("start_date") == kwargs["start_date"] and r.get(
                   "end_date") == kwargs["end_date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_sales_by_category_range",
                                                 "description": "Read f_sales summary for a category & range.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "start_date": {"type": "string"},
                                                                               "end_date": {"type": "string"}},
                                                                "required": ["category", "start_date", "end_date"]}}}
