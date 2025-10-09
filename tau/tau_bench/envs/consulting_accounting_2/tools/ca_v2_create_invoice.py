from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2CreateInvoice(Tool):
    """Generate a new invoice."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str = None,
        invoice_number: str = None,
        publisher_id: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        subtotal: float = None,
        sent_at: str = None,
        paid_at: str = None,
        created_at: str = None,
    ) -> str:
        # Necessary parameters

        if not all(
            [
                invoice_number,
                publisher_id,
                invoice_date,
                period_start,
                period_end,
                subtotal,
            ]
        ):
            return _error(
                "Required fields: invoice_number, publisher_id, invoice_date, period_start, period_end, subtotal"
            )

        # Compute HST and overall total
        hst_amount = _calculate_hst(subtotal)
        total_due = round(subtotal + hst_amount, 2)

        # Generate invoice entry
        new_invoice = {
            "invoice_id": invoice_id or f"INV{len(data.get('invoices', {})) + 1:03d}",
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": f"/invoices/{invoice_date[:4]}/{invoice_number}.pdf",
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at or invoice_date + "T00:00:00Z",
        }

        # Insert into data
        data.setdefault("invoices", []).append(new_invoice)

        return _ok(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            total_due=total_due,
            hst_amount=hst_amount,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoice",
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
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "invoice_date",
                        "period_start",
                        "period_end",
                        "subtotal",
                    ],
                },
            },
        }
