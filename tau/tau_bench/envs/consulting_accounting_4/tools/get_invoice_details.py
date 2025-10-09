from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        invs = data.get("invoices", [])
        row = None
        if invoice_id is not None:
            row = next(
                (i for i in invs if str(i.get("invoice_id")) == str(invoice_id)), None
            )
        elif invoice_number:
            row = next(
                (i for i in invs if i.get("invoice_number") == invoice_number), None
            )
        if not row:
            payload = {"error": "Invoice not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceDetails",
                "description": "Read an invoice by id or invoice_number.",
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
