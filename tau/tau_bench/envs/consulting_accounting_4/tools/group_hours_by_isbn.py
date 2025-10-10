# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GroupHoursByISBN(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        grouped = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn: 
                continue
            grouped.setdefault(isbn, 0.0)
            grouped[isbn] += float(r.get("hours_worked", 0.0))
        return json.dumps({"grouped_hours": grouped}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"group_hours_by_isbn",
            "description":"Sum hours per ISBN within a set of time entries.",
            "parameters":{"type":"object","properties":{"rows":{"type":"array","items":{"type":"object"}}},"required":["rows"]}
        }}
