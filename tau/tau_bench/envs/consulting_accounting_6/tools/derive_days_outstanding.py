from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DeriveDaysOutstanding(Tool):
    """Calculate days overdue for each invoice based on a specified date."""

    @staticmethod
    def invoke(data: dict[str, Any], today: str = "2025-08-20", invoices: list = None) -> str:
        if invoices is None:
            invoices = []
        out = []
        for r in invoices:
            due = r.get("period_end") or r.get("invoice_date")
            due_iso = due[:10] if isinstance(due, str) and len(due) > 10 else due
            ds = (datetime.fromisoformat(today) - datetime.fromisoformat(due_iso)).days
            out.append(
                {"invoice_number": r.get("invoice_number"), "days_outstanding": ds}
            )
        payload = {"aging": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeriveDaysOutstanding",
                "description": "Compute days outstanding as of a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "object"}},
                        "today": {"type": "string"},
                    },
                    "required": ["invoices"],
                },
            },
        }
