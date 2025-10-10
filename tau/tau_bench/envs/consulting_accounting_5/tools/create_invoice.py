# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new invoice with core required fields and many optional ones.
        Non-critical fields default to None or empty string if not provided.
        """
        new_invoice = {
            "invoice_id": f'INV{kwargs["invoice_number"]}',
            "invoice_number": kwargs["invoice_number"],
            "publisher_id": kwargs["publisher_id"],
            "invoice_date": kwargs.get("invoice_date", None),
            "period_start": kwargs.get("period_start", None),
            "period_end": kwargs.get("period_end", None),
            "subtotal": kwargs["subtotal"],
            "hst_amount": kwargs["hst_amount"],
            "total_due": kwargs["total_due"],
            "pdf_path": kwargs.get("pdf_path", ""),
            "sent_at": kwargs.get("sent_at", None),
            "paid_at": kwargs.get("paid_at", None),
            "created_at": kwargs.get("created_at", None),
            "currency": kwargs.get("currency", "CAD"),
            "notes": kwargs.get("notes", "")
        }
        data["invoices"].append(new_invoice)
        return json.dumps(new_invoice["invoice_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoice",
                "description": "Create a new invoice and append it to invoices.json. Allows optional metadata like notes, pdf_path, dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "pdf_path": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"},
                        "currency": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "subtotal",
                        "hst_amount",
                        "total_due"
                    ],
                },
            },
        }
