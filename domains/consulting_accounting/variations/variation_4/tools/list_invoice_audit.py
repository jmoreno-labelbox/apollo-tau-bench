from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        rows = []
        for a in data.get("invoice_audit", []) or []:
            if invoice_id and str(a.get("invoice_id")) == str(invoice_id):
                rows.append(a)
            elif invoice_number and a.get("invoice_number") == invoice_number:
                rows.append(a)
        payload = {"events": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceAudit",
                "description": "List audit events for an invoice by id or number.",
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
