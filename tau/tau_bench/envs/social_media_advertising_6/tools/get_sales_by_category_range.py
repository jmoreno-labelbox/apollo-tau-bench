from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetSalesByCategoryRange(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str, start_date: str, end_date: str, date: Any = None) -> str:
        req = ["category", "start_date", "end_date"]
        err = _require({"category": category, "start_date": start_date, "end_date": end_date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_sales")
        out = [
            r
            for r in rows
            if r.get("category") == category
            and r.get("start_date") == start_date
            and r.get("end_date") == end_date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSalesByCategoryRange",
                "description": "Read f_sales summary for a category & range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }
