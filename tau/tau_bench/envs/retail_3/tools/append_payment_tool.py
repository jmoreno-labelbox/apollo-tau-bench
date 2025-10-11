# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class AppendPaymentTool(Tool):
    """
    Append a payment or refund entry to an order's payment_history in orders.json.

    Behavior:
    - Validates the target order exists.
    - Appends an entry with fields:
        {
          "transaction_type": "payment" | "refund",
          "amount": float,
          "payment_method_id": str,
          "timestamp": "UTC ISO"
        }
    - No automatic reconciliation is performed; caller controls amounts.

    Input (kwargs):
        order_id (str, required)
        transaction_type (str, required: "payment" or "refund")
        amount (float, required, >0)
        payment_method_id (str, required)

    Output:
        JSON string with {"order_id","payment_history_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], amount, order_id, payment_method_id, transaction_type) -> str:
        txn_type = transaction_type
        pm_id = payment_method_id

        if (
            not order_id
            or txn_type not in {"payment", "refund"}
            or not isinstance(amount, (int, float))
            or amount <= 0
            or not pm_id
        ):
            return json.dumps(
                {
                    "error": "order_id, transaction_type('payment'|'refund'), positive amount, payment_method_id required"
                },
                indent=2,
            )

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        entry = {
            "transaction_type": txn_type,
            "amount": float(amount),
            "payment_method_id": pm_id,
            "timestamp": _now_iso(),
        }
        (order.setdefault("payment_history", [])).append(entry)

        return json.dumps(
            {
                "order_id": order_id,
                "payment_history_len": len(order["payment_history"]),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_payment",
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