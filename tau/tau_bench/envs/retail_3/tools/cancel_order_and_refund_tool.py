# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOrderAndRefundTool(Tool):
    """
    Cancel an order and optionally create an automatic refund entry.

    Behavior:
    - Validates the order exists and is not already completed/cancelled.
    - Sets order.status = "cancelled".
    - If refund_amount > 0, appends a refund entry to payment_history.
    - Does NOT touch tracking.json; callers should handle carrier processes separately.

    Input (kwargs):
        order_id (str, required)
        refund_amount (float, optional, default=0)
        payment_method_id (str, optional, required if refund_amount > 0)

    Output:
        JSON string with {"order_id","status","refund_created":bool} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        refund_amount = float(kwargs.get("refund_amount", 0) or 0)
        payment_method_id = kwargs.get("payment_method_id")

        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)
        if refund_amount > 0 and not payment_method_id:
            return json.dumps(
                {"error": "payment_method_id is required when refund_amount > 0"},
                indent=2,
            )

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        if order.get("status") in {"completed", "cancelled"}:
            return json.dumps({"error": f"order already {order.get('status')}"}, indent=2)

        items_to_return = order.get("items", [])

        order["status"] = "cancelled"

        for item in items_to_return:
            product_id = item.get("product_id")
            item_id = item.get("item_id")
            if product_id and item_id:
                _adjust_stock(data, product_id, item_id, 1)

        refund_created = False
        if refund_amount > 0:
            (order.setdefault("payment_history", [])).append(
                {
                    "transaction_type": "refund",
                    "amount": refund_amount,
                    "payment_method_id": payment_method_id,
                    "timestamp": _now_iso(),
                }
            )
            refund_created = True

        return json.dumps(
            {
                "order_id": order_id,
                "status": "cancelled",
                "refund_created": refund_created,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order_and_refund",
                "description": "Cancel an existing order and optionally append a refund entry in orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "refund_amount": {"type": "number", "minimum": 0, "default": 0},
                        "payment_method_id": {
                            "type": "string",
                            "description": "Required when refund_amount > 0",
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }
