from tau_bench.envs.tool import Tool
import json
from typing import Any

class RefundOrderPayment(Tool):
    """Add a refund record using the specified refund_id."""

    @staticmethod
    def invoke(data, order_id: str = None, amount: float = None, reason_code: str = None, refund_id: str = None) -> str:
        if not order_id or amount is None or not reason_code or not refund_id:
            payload = {"error": "order_id, amount, reason_code, refund_id are required"}
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
        existing = next((h for h in hist if h.get("refund_id") == refund_id), None)
        record = {
            "transaction_type": "refund",
            "amount": float(amount),
            "reason_code": reason_code,
            "refund_id": refund_id,
        }
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        payload = {"success": True, "order_id": order_id, "refund_id": refund_id}
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
                "name": "refundOrderPayment",
                "description": "Add or upsert a refund record for an order (by refund_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "reason_code": {"type": "string"},
                        "refund_id": {"type": "string"},
                    },
                    "required": ["order_id", "amount", "reason_code", "refund_id"],
                },
            },
        }
