from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ListInvoiceEvents(Tool):
    """Retrieve all audit records for a specific invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        events = []
        for a in data.get("invoice_audit", []) or []:
            if invoice_id and str(a.get("invoice_id")) == str(invoice_id):
                events.append(a)
            elif invoice_number and a.get("invoice_number") == invoice_number:
                events.append(a)
        payload = {"events": events}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceEvents",
                "description": "List audit events by invoice id or number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
