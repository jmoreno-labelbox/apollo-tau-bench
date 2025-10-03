from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GroupHoursByISBN(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        grouped = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped.setdefault(isbn, 0.0)
            grouped[isbn] += float(r.get("hours_worked", 0.0))
        payload = {"grouped_hours": grouped}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GroupHoursByIsbn",
                "description": "Sum hours per ISBN within a set of time entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }
