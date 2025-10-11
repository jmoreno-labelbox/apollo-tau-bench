# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], hst_amount, invoice_number, publisher_id, subtotal, total_due, created_at = None, currency = "CAD", invoice_date = None, notes = "", paid_at = None, pdf_path = "", period_end = None, period_start = None, sent_at = None) -> str:
        """
        Creates a new invoice with core required fields and many optional ones.
        Non-critical fields default to None or empty string if not provided.
        """
        new_invoice = {
            "invoice_id": f'INV{invoice_number}',
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": pdf_path,
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at,
            "currency": currency,
            "notes": notes
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
