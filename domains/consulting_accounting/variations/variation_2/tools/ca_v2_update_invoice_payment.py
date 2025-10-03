from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2UpdateInvoicePayment(Tool):
    """Modify the payment status of an invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, paid_at: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)

        if not invoice:
            return _error(f"Invoice '{invoice_id}' not found.")

        invoice["paid_at"] = paid_at

        return _ok(invoice_id=invoice_id, paid_at=paid_at, status="payment_updated")

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2UpdateInvoicePayment",
                "description": "Update the payment status of an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string"},
                    },
                    "required": ["invoice_id"],
                },
            },
        }
