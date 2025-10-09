from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AggregateHoursByISBN(Tool):
    """Sum hours by ISBN across a collection of time logs."""

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        grouped: dict[str, float] = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped[isbn] = grouped.get(isbn, 0.0) + float(r.get("hours_worked", 0.0))
        payload = {"grouped_hours": grouped}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AggregateHoursByIsbn",
                "description": "Sum hours per ISBN.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }
