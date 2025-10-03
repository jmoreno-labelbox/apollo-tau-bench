from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SendInvoiceEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        publisher_id: str = None,
        consultant_id: str = None,
        subject: str = None,
        body_text: str = None,
        attachment: str = None,
        invoice_number: str = None
    ) -> str:
        inv_no = invoice_number
        if inv_no:
            inv = next(
                (
                    i
                    for i in data.get("invoices", [])
                    if i.get("invoice_number") == inv_no
                ),
                None,
            )
            if inv:
                inv["sent_at"] = _fixed_now_iso()
        payload = {
            "status": "sent",
            "publisher_id": publisher_id,
            "consultant_id": consultant_id,
            "subject": subject,
            "attachment": attachment,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendInvoiceEmail",
                "description": "Send invoice email to publisher, CC consultant (external).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "consultant_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"},
                    },
                    "required": [
                        "publisher_id",
                        "consultant_id",
                        "subject",
                        "body_text",
                        "attachment",
                    ],
                },
            },
        }
