from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class AppendPaymentTool(Tool):
    """
    Add a payment or refund entry to an order's payment_history in orders.json.

    Behavior:
    - Confirms the target order exists.
    - Adds an entry with fields:
        {
          "transaction_type": "payment" | "refund",
          "amount": float,
          "payment_method_id": str,
          "timestamp": "UTC ISO"
        }
    - No automatic reconciliation occurs; the caller manages amounts.

    Input (kwargs):
        order_id (str, required)
        transaction_type (str, required: "payment" or "refund")
        amount (float, required, >0)
        payment_method_id (str, required)

    Output:
        JSON string with {"order_id","payment_history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        order_id: str = None, 
        transaction_type: str = None, 
        amount: float = None, 
        payment_method_id: str = None
    ) -> str:
        if (
            not order_id
            or transaction_type not in {"payment", "refund"}
            or not isinstance(amount, (int, float))
            or amount <= 0
            or not payment_method_id
        ):
            payload = {
                    "error": "order_id, transaction_type('payment'|'refund'), positive amount, payment_method_id required"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        entry = {
            "transaction_type": transaction_type,
            "amount": float(amount),
            "payment_method_id": payment_method_id,
            "timestamp": _now_iso(),
        }
        (order.setdefault("payment_history", [])).append(entry)
        payload = {
                "order_id": order_id,
                "payment_history_len": len(order["payment_history"]),
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
                "name": "AppendPayment",
                "description": "Append a payment or refund entry to an order's payment_history in orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "transaction_type": {
                            "type": "string",
                            "enum": ["payment", "refund"],
                        },
                        "amount": {"type": "number", "minimum": 0},
                        "payment_method_id": {"type": "string"},
                    },
                    "required": [
                        "order_id",
                        "transaction_type",
                        "amount",
                        "payment_method_id",
                    ],
                },
            },
        }
