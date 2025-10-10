# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat = kwargs.get("category")
        d = kwargs.get("date")
        for r in data.get("f_viewership", []):
            if r.get("category") == cat and r.get("date") == d:
                return json.dumps(r)
        return json.dumps({"error": "viewership_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category",
                                                 "description": "Gets viewership for a category on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["category", "date"]}}}
