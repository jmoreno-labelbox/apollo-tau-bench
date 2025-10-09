from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str, date: str) -> str:
        req = ["category", "date"]
        err = _require({"category": category, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_viewership")
        out = [
            r
            for r in rows
            if r.get("category") == category
            and r.get("date") == date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Read f_viewership for a category/date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["category", "date"],
                },
            },
        }
