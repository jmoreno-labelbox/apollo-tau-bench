# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendInvoiceEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], consultant_id, invoice_number, publisher_id, attachment = "", body_text = "", subject = "") -> str:
        """
        Simulates sending an invoice email and updates the sent_at field on the invoice.
        """
        sent_time = '2025-09-05T00:00:00Z' # Get the current date and time in ISO 8601 format.

        invoice = next((inv for inv in data["invoices"] if inv["invoice_number"] == invoice_number), None)
        if invoice:
            invoice["sent_at"] = sent_time
            return json.dumps({"status": "success", "invoice_id": invoice["invoice_id"], "sent_at": sent_time})
        return json.dumps({"status": "error", "message": "Invoice not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "SendInvoiceEmail",
                "description": "Sends an invoice email to a publisher and updates the invoice's sent_at timestamp.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string"},
                        "consultant_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"}
                    },
                    "required": ["publisher_id", "invoice_number", "subject"],
                },
            },
        }
