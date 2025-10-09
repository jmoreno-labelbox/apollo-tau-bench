from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddOrderPayment(Tool):
    """Add a payment record."""

    @staticmethod
    def invoke(data, order_id=None, amount=None, payment_method_id=None, transaction_id=None) -> str:
        if not order_id or amount is None or not payment_method_id or not transaction_id:
            payload = {
                "error": "order_id, amount, payment_method_id, transaction_id are required"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        hist = _ensure_list(o, "payment_history")
        # idempotent: substitute existing with the same txn_id
        existing = next((h for h in hist if h.get("transaction_id") == transaction_id), None)
        record = {
            "transaction_type": "payment",
            "amount": float(amount),
            "payment_method_id": payment_method_id,
            "transaction_id": transaction_id,
        }
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        payload = {"success": True, "order_id": order_id, "transaction_id": transaction_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "addOrderPayment",
                "description": "Add or upsert a payment record for an order (by transaction_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "payment_method_id": {"type": "string"},
                        "transaction_id": {"type": "string"},
                    },
                    "required": [
                        "order_id",
                        "amount",
                        "payment_method_id",
                        "transaction_id",
                    ],
                },
            },
        }
