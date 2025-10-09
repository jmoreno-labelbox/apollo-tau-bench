from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        """
        Check order status and details based on order ID

        Data Sources: orders.json (order status, fulfillment, payment info)
        """
        if not order_id or not order_id.strip():
            payload = {"error": "Order ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        order_id = order_id.strip()

        # Add # prefix if not provided (for convenience)
        if not order_id.startswith("#"):
            order_id = f"#{order_id}"

        # Find the order
        orders = data.get("orders", {}).values()
        target_order = None

        for order in orders.values():
            if order.get("order_id") == order_id:
                target_order = order
                break

        if not target_order:
            payload = {"error": f"Order {order_id} not found", "status": "not_found"}
            out = json.dumps(payload)
            return out

        # Rule: Only process orders with valid status: pending, processed, delivered, cancelled
        order_status = target_order.get("status")
        order_timestamp = target_order.get("timestamp")
        user_id = target_order.get("user_id")

        # Get fulfillment information
        fulfillments = target_order.get("fulfillments", [])
        tracking_info = None
        if fulfillments:
            latest_fulfillment = fulfillments[-1]  # Get most recent fulfillment
            tracking_info = {
                "tracking_id": latest_fulfillment.get("tracking_id"),
                "courier_id": latest_fulfillment.get("courier_id"),
                "courier_name": latest_fulfillment.get("courier_name"),
                "fulfillment_status": latest_fulfillment.get("status"),
                "timestamp": latest_fulfillment.get("timestamp"),
            }

        # Get payment information
        payment_history = target_order.get("payment_history", [])
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )
        total_refunded = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "refund"
        )

        # Get order items summary
        order_items = target_order.get("items", [])
        items_summary = {
            "total_items": len(order_items),
            "item_names": [item.get("name") for item in order_items],
            "item_ids": [item.get("item_id") for item in order_items],
        }

        # Get delivery address
        delivery_address = target_order.get("address", {}).values()

        # Check for cancellation info
        cancellation_info = target_order.get("cancellation_info")

        # Check for returns
        returns = target_order.get("returns", [])
        return_info = None
        if returns:
            return_info = {
                "return_requests": len(returns),
                "latest_return": returns[-1] if returns else None,
            }

        result = {
            "status": "success",
            "order_id": order_id,
            "order_details": {
                "user_id": user_id,
                "order_status": order_status,
                "order_date": order_timestamp,
                "last_updated": target_order.get("last_updated", order_timestamp),
            },
            "items_summary": items_summary,
            "payment_info": {
                "total_paid": round(total_paid, 2),
                "total_refunded": round(total_refunded, 2),
                "net_amount": round(total_paid - total_refunded, 2),
            },
            "delivery_info": {"address": delivery_address, "tracking": tracking_info},
            "cancellation_info": cancellation_info,
            "return_info": return_info,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckOrderStatus",
                "description": "Check order status and details based on order ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier (e.g., 'W6893533' or '#W6893533')",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
