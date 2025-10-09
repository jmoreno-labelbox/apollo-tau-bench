from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CancelOrderAndRefundTool(Tool):
    """
    Cancel an order and optionally generate an automatic refund entry.

    Behavior:
    - Confirms the order exists and is not already completed or cancelled.
    - Changes order.status to "cancelled".
    - If refund_amount > 0, adds a refund entry to payment_history.
    - Does NOT modify tracking.json; callers must manage carrier processes independently.

    Input (kwargs):
        order_id (str, required)
        refund_amount (float, optional, default=0)
        payment_method_id (str, optional, required if refund_amount > 0)

    Output:
        JSON string with {"order_id","status","refund_created":bool} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, refund_amount: float = 0, payment_method_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        if refund_amount > 0 and not payment_method_id:
            payload = {"error": "payment_method_id is required when refund_amount > 0"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        orders = data.get("orders", {}).values()
        order = next((o for o in orders.values() if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        if order.get("status") in {"completed", "cancelled"}:
            payload = {"error": f"order already {order.get('status')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = {
                "order_id": order_id,
                "status": "cancelled",
                "refund_created": refund_created,
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
                "name": "CancelOrderAndRefund",
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
