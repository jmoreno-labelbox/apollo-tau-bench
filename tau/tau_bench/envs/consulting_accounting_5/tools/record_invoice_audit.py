# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Finds an invoice by number and logs an audit event for it.
        """
        invoice_number = kwargs["invoice_number"]
        invoice = next((inv for inv in data["invoices"] if inv["invoice_number"] == invoice_number), None)
        if not invoice:
            return json.dumps({"error": "Invoice not found"})

        new_event = {
            "audit_id": f"AUD_{invoice['invoice_id']}_{len(data['invoice_audit']) + 1}",
            "invoice_id": invoice['invoice_id'],
            "event_type": kwargs.get("event_type"),
            "event_timestamp": "2024-09-05T00:00:00Z",
            "notes": kwargs.get("notes", f"Event '{kwargs.get('event_type')}' triggered.")
        }
        data["invoice_audit"].append(new_event)
        return json.dumps(new_event)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "RecordInvoiceAudit",
                "description": "Records an audit event for a given invoice number.",
                "parameters": {
                    "type": "object", "properties": {
                        "invoice_number": {"type": "string"},
                        "event_type": {"type": "string"}
                    },
                    "required": ["invoice_number", "event_type"],
                },
            },
        }
