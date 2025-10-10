# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateInvoice(Tool):
    """Create a new invoice."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Required parameters
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        publisher_id = kwargs.get("publisher_id")
        invoice_date = kwargs.get("invoice_date")
        period_start = kwargs.get("period_start")
        period_end = kwargs.get("period_end")
        subtotal = kwargs.get("subtotal")

        if not all([invoice_number, publisher_id, invoice_date,
                   period_start, period_end, subtotal]):
            return _error("Required fields: invoice_number, publisher_id, invoice_date, period_start, period_end, subtotal")

        # Calculate HST and total
        hst_amount = _calculate_hst(subtotal)
        total_due = round(subtotal + hst_amount, 2)

        # Create invoice record
        new_invoice = {
            "invoice_id": invoice_id or f"INV{len(data.get('invoices', [])) + 1:03d}",
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": f"/invoices/{invoice_date[:4]}/{invoice_number}.pdf",
            "sent_at": kwargs.get("sent_at"),
            "paid_at": kwargs.get("paid_at"),
            "created_at": kwargs.get("created_at", invoice_date + "T00:00:00Z")
        }

        # Add to data
        data.setdefault("invoices", []).append(new_invoice)

        return _ok(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            total_due=total_due,
            hst_amount=hst_amount
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice",
                "description": "Create a new invoice with automatic HST calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "invoice_date": {"type": "string", "format": "date"},
                        "period_start": {"type": "string", "format": "date"},
                        "period_end": {"type": "string", "format": "date"},
                        "subtotal": {"type": "number"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"}
                    },
                    "required": ["invoice_number", "publisher_id", "invoice_date", "period_start", "period_end", "subtotal"],
                },
            },
        }
