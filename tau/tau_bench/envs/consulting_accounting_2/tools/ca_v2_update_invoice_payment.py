# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2UpdateInvoicePayment(Tool):
    """Update invoice payment status."""

    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, paid_at) -> str:

        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)

        if not invoice:
            return _error(f"Invoice '{invoice_id}' not found.")

        invoice["paid_at"] = paid_at

        return _ok(
            invoice_id=invoice_id,
            paid_at=paid_at,
            status="payment_updated"
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_update_invoice_payment",
                "description": "Update the payment status of an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }