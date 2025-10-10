# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["category", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_viewership")
        out = [r for r in rows if r.get("category") == kwargs["category"] and r.get("date") == kwargs["date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category",
                                                 "description": "Read f_viewership for a category/date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["category", "date"]}}}
