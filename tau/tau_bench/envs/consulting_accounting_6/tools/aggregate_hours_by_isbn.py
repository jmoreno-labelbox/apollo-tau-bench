# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AggregateHoursByISBN(Tool):
    """Aggregate hours by ISBN within a set of time entries."""
    @staticmethod
    def invoke(data: Dict[str, Any], rows) -> str:
        rows = rows or []
        grouped: Dict[str, float] = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped[isbn] = grouped.get(isbn, 0.0) + float(r.get("hours_worked", 0.0))
        return json.dumps({"grouped_hours": grouped}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "aggregate_hours_by_isbn",
            "description": "Sum hours per ISBN.",
            "parameters": {"type": "object", "properties": {
                "rows": {"type": "array", "items": {"type": "object"}}
            }, "required": ["rows"]}
        }}
