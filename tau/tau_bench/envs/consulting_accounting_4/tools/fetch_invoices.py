from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FetchInvoices(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, publisher_id: str = None, date_from: str = None, date_to: str = None) -> str:
        rows = data.get("invoices", []) or []
        out = []
        for r in rows:
            if status == "open" and r.get("paid_at") is not None:
                continue
            if publisher_id and r.get("publisher_id") != publisher_id:
                continue
            if date_from and r.get("invoice_date", "") < date_from:
                continue
            if date_to and r.get("invoice_date", "") > date_to:
                continue
            out.append(r)
        payload = {"invoices": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchInvoices",
                "description": "Fetch invoices with optional filters (status/open, publisher, date range).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "date_from": {"type": "string"},
                        "date_to": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
