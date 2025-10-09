from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DispatchInvoiceEmail(Tool):
    """Dispatch an invoice email and (if applicable) indicate the invoice has been sent."""

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
        if invoice_number:
            inv = next(
                (
                    i
                    for i in data.get("invoices", {}).values()
                    if i.get("invoice_number") == invoice_number
                ),
                None,
            )
            if inv:
                inv["sent_at"] = _now_iso()
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
                "name": "DispatchInvoiceEmail",
                "description": "Send invoice email to client, CC consultant.",
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
