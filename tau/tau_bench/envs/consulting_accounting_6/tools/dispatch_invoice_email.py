# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DispatchInvoiceEmail(Tool):
    """Send an invoice email and (if provided) mark the invoice as sent."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publisher_id = kwargs.get("publisher_id")
        consultant_id = kwargs.get("consultant_id")
        subject = kwargs.get("subject")
        body_text = kwargs.get("body_text")
        attachment = kwargs.get("attachment")
        inv_no = kwargs.get("invoice_number")

        if inv_no:
            inv = next((i for i in data.get("invoices", []) if i.get("invoice_number") == inv_no), None)
            if inv:
                inv["sent_at"] = _now_iso()

        return json.dumps({"status": "sent",
                           "publisher_id": publisher_id,
                           "consultant_id": consultant_id,
                           "subject": subject,
                           "attachment": attachment}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "dispatch_invoice_email",
            "description": "Send invoice email to client, CC consultant.",
            "parameters": {"type": "object", "properties": {
                "publisher_id": {"type": "string"},
                "consultant_id": {"type": "string"},
                "invoice_number": {"type": "string"},
                "subject": {"type": "string"},
                "body_text": {"type": "string"},
                "attachment": {"type": "string"}
            }, "required": ["publisher_id", "consultant_id", "subject", "body_text", "attachment"]}
        }}
