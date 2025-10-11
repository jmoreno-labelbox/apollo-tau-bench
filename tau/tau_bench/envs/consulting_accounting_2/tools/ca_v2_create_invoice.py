# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

def _calculate_hst(subtotal: float, rate: float = 0.13) -> float:
    """Calculate HST (13% default for Ontario)"""
    return round(subtotal * rate, 2)

class CaV2CreateInvoice(Tool):
    """Create a new invoice."""

    @staticmethod
    def invoke(data: Dict[str, Any], invoice_date, invoice_id, invoice_number, paid_at, period_end, period_start, publisher_id, sent_at, subtotal, created_at = invoice_date + "T00:00:00Z") -> str:

        if not all([invoice_number, publisher_id, invoice_date,
                   period_start, period_end, subtotal]):
            return _error("Required fields: invoice_number, publisher_id, invoice_date, period_start, period_end, subtotal")

        # Compute HST and overall sum.
        hst_amount = _calculate_hst(subtotal)
        total_due = round(subtotal + hst_amount, 2)

        # Generate invoice entry
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
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at
        }

        # Append to data
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